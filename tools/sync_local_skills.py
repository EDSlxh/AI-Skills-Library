"""Check or install this library's skills, preserving local files and plugin ownership."""

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import shutil
import sys


IGNORED = {"__pycache__", ".geo-cache", ".DS_Store"}


def files(folder):
    result = {}
    if not folder.exists():
        return result
    for path in folder.rglob("*"):
        relative = path.relative_to(folder)
        if any(part in IGNORED for part in relative.parts) or path.suffix in {".pyc", ".pyo"}:
            continue
        if path.is_symlink():
            raise ValueError(f"Review linked files before syncing: {path}")
        if path.is_file():
            result[relative.as_posix()] = path
    return result


def digest(path):
    data = path.read_bytes()
    if path.suffix.lower() in {".md", ".py", ".json", ".yaml", ".yml", ".toml", ".txt"} or path.name == "LICENSE":
        data = data.replace(b"\r\n", b"\n")
    return hashlib.sha256(data).hexdigest()


def plan(root, user_home):
    entries = json.loads((root / "skills.json").read_text(encoding="utf-8"))["skills"]
    rows = []
    names = set()
    for entry in entries:
        name = entry["name"]
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or name in names:
            raise ValueError(f"Invalid or duplicate skill name: {name}")
        names.add(name)
        source = (root / entry["path"]).resolve()
        if not source.is_relative_to(root) or not (source / "SKILL.md").is_file():
            raise ValueError(f"Invalid skill source: {entry['path']}")
        manifest = (source / "SKILL.md").read_text(encoding="utf-8")
        actual = re.search(r"^name:\s*(\S+)\s*$", manifest, re.MULTILINE)
        if not actual or actual.group(1) != name:
            raise ValueError(f"Skill name does not match its manifest: {source}")
        if entry.get("managed_by"):
            cache = user_home / ".codex/plugins/cache"
            candidates = list(cache.glob(f"*/{entry['managed_by']}/*/skills/{name}/SKILL.md"))
            matches = [path.parent for path in candidates if digest(path) == digest(source / "SKILL.md")]
            rows.append({"name": name, "source": source, "target": matches[0] if matches else None,
                         "state": "plugin-current" if matches else "plugin-required", "changed": []})
            continue
        candidates = [user_home / ".agents/skills" / name, user_home / ".codex/skills" / name]
        present = [path for path in candidates if path.exists()]
        if len(present) > 1:
            raise ValueError(f"Duplicate installed locations require review: {name}")
        target = present[0] if present else candidates[0]
        if not target.resolve().is_relative_to(user_home.resolve()):
            raise ValueError(f"Skill target resolves outside the user directory: {target}")
        incoming, existing = files(source), files(target)
        extra = sorted(existing.keys() - incoming.keys())
        if extra:
            raise ValueError(f"Merge local-only files before installing {name}: {', '.join(extra)}")
        changed = [relative for relative in incoming
                   if relative not in existing or digest(incoming[relative]) != digest(existing[relative])]
        rows.append({"name": name, "source": source, "target": target,
                     "state": "missing" if not present else "different" if changed else "current",
                     "changed": changed,
                     "before": {relative: digest(path) for relative, path in existing.items()},
                     "incoming": {relative: digest(path) for relative, path in incoming.items()}})
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--install", action="store_true", help="Back up changed skills and copy the library versions")
    mode.add_argument("--check", action="store_true", help="Read-only comparison; this is the default")
    parser.add_argument("--user-home", type=Path, default=Path.home())
    parser.add_argument("--backup-dir", type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    rows = plan(root, args.user_home)
    if args.install:
        if any(row["state"] == "plugin-required" for row in rows):
            raise SystemExit("The learning-cards provider is missing or differs; review the plugin before syncing.")
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
        backup = (args.backup_dir or root / ".local-sync/backups" / stamp).resolve()
        changed = [row for row in rows if row["changed"]]
        if changed:
            backup.mkdir(parents=True, exist_ok=False)
            # Back up every changed existing skill before the first installation write.
            for row in changed:
                if row["target"].exists():
                    shutil.copytree(row["target"], backup / row["name"],
                                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".geo-cache"))
            receipt = [{"name": row["name"], "target": str(row["target"]),
                        "previously_installed": row["target"].exists()} for row in changed]
            (backup / "receipt.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            for row in changed:
                # Detect edits made after planning; do not overwrite new local work.
                current = next(item for item in plan(root, args.user_home) if item["name"] == row["name"])
                if current["before"] != row["before"] or current["incoming"] != row["incoming"]:
                    raise SystemExit(f"Skill changed during synchronization: {row['name']}; backup: {backup}")
                incoming = files(row["source"])
                for relative in sorted(incoming, key=lambda value: (value == "SKILL.md", value)):
                    source = incoming[relative]
                    target = row["target"] / relative
                    target.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(source, target)
            print(f"Backups: {backup}")
        rows = plan(root, args.user_home)
    for row in rows:
        print(f"{row['name']}: {row['state']} ({row['target'] or 'install the matching plugin provider'})")
    if any(row["state"] not in {"current", "plugin-current"} for row in rows):
        sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError) as error:
        raise SystemExit(str(error))
