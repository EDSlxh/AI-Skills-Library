"""Build one uploadable ChatGPT project source for the function-learning example."""

import argparse
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import quote, urlsplit


def build(root):
    example = root / "examples/function-learning"
    skill = root / "ai-skills/06-learning/learn-scientifically"
    paths = [example / "project-instructions.txt", skill / "SKILL.md"]
    paths += sorted((skill / "references").glob("*.md"))
    paths += [skill / "assets/learning-record.md", example / "course.md", example / "initial-state.md"]
    question_file = example / "question-bank.json"
    paths += [question_file]
    anchors = {p.resolve(): "file-" + hashlib.sha256(p.relative_to(root).as_posix().encode()).hexdigest()[:16] for p in paths}
    sections, sources = [], []
    for path in paths:
        relative = path.relative_to(root).as_posix()
        content = path.read_text(encoding="utf-8-sig").replace("\r\n", "\n").rstrip() + "\n"
        sources.append({"path": relative, "sha256": hashlib.sha256(content.encode()).hexdigest()})

        def relocate(match):
            label, target = match.groups()
            parts = urlsplit(target)
            if parts.scheme or target.startswith(("#", "//")):
                return match.group(0)
            destination = (path.parent / parts.path).resolve()
            if destination in anchors:
                return f"[{label}](#{anchors[destination]})"
            try:
                target_path = destination.relative_to(root).as_posix()
            except ValueError:
                return match.group(0)
            return f"[{label}](https://github.com/EDSlxh/AI-Skills-Library/blob/main/{quote(target_path)})"

        if path == question_file:
            json.loads(content)
            content = "教师参考区：以下 referenceSolution、expectedChoiceId 仅用于核对，不在等待用户作答时自动展示。\n\n```json\n" + content + "```\n"
        else:
            content = re.sub(r"(?<!!)\[([^\]\n]+)\]\(([^)\n]+)\)", relocate, content)
        sections.append(f'<a id="{anchors[path.resolve()]}"></a>\n\n## 来源文件：{relative}\n\n{content}')
    digest = hashlib.sha256(json.dumps(sources, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
    header = (
        "# 高中函数学习｜测试项目文件\n\n"
        "课程版本：1.0。仓库：EDSlxh/AI-Skills-Library。\n\n"
        f"源文件集合 SHA256：`{digest}`。这是资料版本摘要，不是 Git 提交号。\n\n"
        "本文件可作为 ChatGPT 项目的 Sources 上传，已合并项目指令、完整科学学习 Skill、必要引用、"
        "课程、初始记录与 16 道自编题。包内来源文件已嵌入，可按路径定位，无需再上传通用 Skill 包。"
        "项目指令仍需在项目设置中保存。读文件不等于安装原生 Skill，也不启动题卡服务。\n\n"
        "先按当前聊天或实际读取的最新学习记录续学；只有首次开始且没有记录时才用初始状态。"
        "不能用空白模板覆盖后续真实进度。若只见到文件目录而尚未读到正文，应先读取对应章节。\n\n"
        "开始时先读项目指令、Skill、本单元讲义与对应题目。参考解用于核对，不能在待答时自动泄露；"
        "未看到真实作答不评分。用户要求直接讲解或参考解时尊重请求。\n\n"
        "真实题卡需要当前客户端和服务实际支持；不可用时说明，并等用户选择文字备用。"
        "全部题目不限时、不弹窗。不要把这个通用初始文件当成某位学习者已经完成的记录。\n\n"
    )
    return header + "\n\n---\n\n".join(sections), len(paths)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    content, count = build(root)
    target = root / "examples/function-learning/function-learning-project.md"
    if args.check:
        if not target.is_file() or target.read_text(encoding="utf-8") != content:
            raise SystemExit("Function project file is missing or stale")
    else:
        target.write_text(content, encoding="utf-8", newline="\n")
    print(f"{'Verified' if args.check else 'Built'} function project: {count} embedded files")


if __name__ == "__main__":
    main()
