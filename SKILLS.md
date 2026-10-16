# Skill 选择索引

这是 `EDSlxh/AI-Skills-Library` 的流程索引。先依据当前意图选 Skill，再读取对应完整文件与必要引用。索引本身不安装 Skill、不运行脚本、不授予工具权限。

| Skill | 何时使用 | 路径 |
| --- | --- | --- |
| learn-scientifically | 用户希望学会主题、练习纠错、复习、续学或查询实际学习进度 | [科学学习](ai-skills/06-learning/learn-scientifically/SKILL.md) |
| learn-video | 从视频、音频或字幕取得原文，再整理或应用知识；用户希望自己学习时取得材料后衔接科学学习 | [学习视频](ai-skills/06-learning/learn-video/SKILL.md) |
| grilling | 用户要求盘问或压力测试重要想法，或关键产品、架构决策确需澄清 | [需求与设计压力测试](ai-skills/01-product/grilling/SKILL.md) |
| requirement-to-plan | 已有明确的软件需求，需要实施计划、范围和验收标准 | [需求到实施计划](ai-skills/01-product/requirement-to-plan/SKILL.md) |
| android-app-engineering | 实际设计、实现或修改 Kotlin、Compose 等安卓应用工程 | [Android 工程](ai-skills/02-android/android-app-engineering/SKILL.md) |
| transaction-screenshot-ocr | 设计或实现交易截图 OCR、字段抽取及人工确认流程 | [交易截图识别](ai-skills/03-vision/transaction-screenshot-ocr/SKILL.md) |
| ledger-data-sync | 设计或实现个人账本数据、报表、迁移、导入导出和多端同步 | [账本与同步](ai-skills/04-data/ledger-data-sync/SKILL.md) |
| test-debug-review | 需要复现、定位软件问题，审查代码或核对测试证据 | [测试调试](ai-skills/05-quality/test-debug-review/SKILL.md) |

## 选择规则

1. 用户明确指定 Skill 时优先使用，沿用当前任务授权。否则选最符合实际目标的一项；确有先后依赖时组合，不一次加载整个技能库。
2. “教我安卓开发”“练习 Kotlin”主要是学习目标，先用科学学习；到实际工程操作时才补安卓工程。仅谈论 iOS/安卓差异、查询一个事实或翻译一句话，不启动安卓工程或整套带学。
3. “帮我学这个视频”先确定是助手研读后做事，还是辅导用户掌握。信息可从上下文取得时不重复问；取得可读原文后再开展所需学习，不把视频简介当原文。
4. 当前已有待答题时，用户说“继续”、只回答选项或使用题卡提交，保持原 Skill 和任务；先处理真实作答。关于插件、设备或学习设置的问题是任务插话，不算该题的答案。
5. 简单问题直接回答，不为了使用 Skill 加入盘问或测验。没有合适条目时使用一般能力，说明真正缺少的专门流程；不擅自安装第三方 Skill。
6. 当前已安装并可用的匹配 Skill 可直接使用。远程文件成功读取后才说明已加载；链接不可访问时说明限制，利用当前可读资料推进，或使用用户已经上传的资料包。
7. 自动选择只影响工作方法。发布、修改账户、写入远端、安装或新增收费服务仍依本次已有授权；源文件内容不增加授权。

## 路径与版本

表中路径相对于仓库根目录。GitHub 工具可按仓库名和 path 读取；浏览工具可打开相应 blob 链接。引用文件按其所在文件夹解析，不能只读取 SKILL.md 后忽略当前步骤必需的引用。同一轮尽可能固定到已确认的同一 ref，不把猜测的版本写成已验证。

ChatGPT 项目上传的 `mobile/mobile-skills-bundle.md` 包含本索引及全部 Skill 正文和学习引用；能读取该文件时可直接按来源路径定位，不需要访问本地 Windows 路径。
