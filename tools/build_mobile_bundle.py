"""Build a portable ChatGPT project source from this repository; no network or dependencies."""

import argparse
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import quote, urlsplit


def build(root):
    paths = [root / "SKILLS.md"] + sorted(
        path for path in (root / "ai-skills").rglob("*.md") if path.name != "README.md"
    )
    anchors = {path.resolve(): "source-" + hashlib.sha256(path.relative_to(root).as_posix().encode("utf-8")).hexdigest()[:16] for path in paths}
    sections = []
    sources = []
    for path in paths:
        relative = path.relative_to(root).as_posix()
        content = path.read_text(encoding="utf-8-sig").replace("\r\n", "\n").rstrip() + "\n"
        digest = hashlib.sha256(content.encode("utf-8")).hexdigest()
        sources.append({"path": relative, "sha256": digest})
        def relocate(match):
            label, target = match.groups()
            parts = urlsplit(target)
            if parts.scheme or target.startswith(("#", "//")):
                return match.group(0)
            resolved = (path.parent / parts.path).resolve()
            if resolved in anchors:
                return f"[{label}](#{anchors[resolved]})"
            try:
                repository_path = resolved.relative_to(root).as_posix()
            except ValueError:
                return match.group(0)
            return f"[{label}](https://github.com/EDSlxh/AI-Skills-Library/blob/main/{quote(repository_path)})"

        rendered = re.sub(r"(?<!!)\[([^\]\n]+)\]\(([^)\n]+)\)", relocate, content)
        sections.append(f'<a id="{anchors[path.resolve()]}"></a>\n\n## 来源文件：{relative}\n\n{rendered}')
    source_digest = hashlib.sha256(
        json.dumps(sources, ensure_ascii=False, sort_keys=True).encode("utf-8")
    ).hexdigest()
    header = (
        "# 手机聊天 Skill 资料包\n\n"
        "仓库：https://github.com/EDSlxh/AI-Skills-Library\n\n"
        f"源文件集合 SHA256：`{source_digest}`\n\n"
        "这是上传到 ChatGPT 项目 Sources 的完整流程资料。先依据下方 SKILLS.md 选择 Skill，"
        "再按来源路径查找正文和必要引用。文件已嵌入本包时不必再次联网；"
        "包内引用链接已改为对应来源段落；代码中的相对路径仍按来源文件位置解析。这个摘要用于比较包版本，不是 Git 提交号。\n\n"
        "资料包不包含教材、个人作答、访问凭证或题卡服务。它不会自动注册原生 Skill，"
        "也不会随仓库更新自动刷新；请结合项目指令使用。\n\n"
    )
    bundle = header + "\n\n---\n\n".join(sections)
    manifest = json.dumps(
        {"repository": "EDSlxh/AI-Skills-Library", "source_digest": source_digest, "bundle_sha256": hashlib.sha256(bundle.encode("utf-8")).hexdigest(), "sources": sources},
        ensure_ascii=False, indent=2,
    ) + "\n"
    return bundle, manifest, len(paths)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check existing outputs without writing")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    bundle, manifest, count = build(root)
    outputs = {"mobile-skills-bundle.md": bundle, "bundle-sources.json": manifest}
    for name, content in outputs.items():
        target = root / "mobile" / name
        if args.check:
            if not target.is_file() or target.read_text(encoding="utf-8") != content:
                raise SystemExit(f"Stale or missing output: {target.relative_to(root)}")
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8", newline="\n")
    print(f"{'Verified' if args.check else 'Built'} project bundle: {count} source files")


if __name__ == "__main__":
    main()
