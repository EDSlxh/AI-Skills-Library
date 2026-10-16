# AI-Skills-Library

可复用 AI 开发与学习 Skills，使用标准 `SKILL.md` 结构。自动选择与路径规则见根目录 [SKILLS.md](../SKILLS.md)，手机配置见 [使用指南](../docs/mobile-setup.md)。

## 技能目录
- [Grilling — 需求与设计压力测试](01-product/grilling/SKILL.md)
- [需求到实施计划](01-product/requirement-to-plan/SKILL.md)
- [Android 工程](02-android/android-app-engineering/SKILL.md)
- [截图 OCR](03-vision/transaction-screenshot-ocr/SKILL.md)
- [账本与同步](04-data/ledger-data-sync/SKILL.md)
- [测试调试](05-quality/test-debug-review/SKILL.md)
- [科学学习](06-learning/learn-scientifically/SKILL.md)
- [学习视频](06-learning/learn-video/SKILL.md)
- [聊天内题卡](06-learning/learning-cards/SKILL.md)：配合已有题卡插件使用。
- [照片定位](07-geolocation/geo-sleuth/SKILL.md)：包含工具脚本、地区数据、参考资料和上游许可。

## 推荐协作流程
**Grilling（提出关键问题、确定决策）→ Requirement-to-Plan（确认范围、排出实施计划）→ Android / OCR / Data（执行开发）→ Test-Debug-Review（验证审查）**。

无需对每一个简单任务强制执行 Grilling；重大或模糊的产品与架构问题优先使用。

## 调用示例
对 ChatGPT 说：“读取 GitHub 仓库 EDSlxh/AI-Skills-Library 中 `ai-skills/01-product/grilling/SKILL.md`，用 Grilling 方式逐轮梳理我的 Android 记账软件；关键决策确认后按 `ai-skills/01-product/requirement-to-plan/SKILL.md` 形成开发计划。”

文件保存在 GitHub 并不等于自动安装为 ChatGPT 或 Codex 内置技能；需要显式读取，或按使用工具的规则配置技能发现目录。

## 上游参考
- [Matt Pocock — Skills / Grilling](https://github.com/mattpocock/skills)
- [obra/superpowers](https://github.com/obra/superpowers)
- [Android agent skills](https://github.com/new-silvermoon/awesome-android-agent-skills)
- [Android agent skills](https://github.com/krutikJain/android-agent-skills)

本文库的 Grilling 为中文适配版，不是对第三方文件的原样复制。第三方 Skill 或脚本需要独立核对来源、安全与许可证，不得直接执行未经审核的脚本。
