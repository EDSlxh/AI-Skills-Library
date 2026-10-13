---
name: requirement-to-plan
description: Turn confirmed software requirements into a scoped, testable implementation plan; use grilling first for unresolved high-impact product or architecture decisions.
---
# 需求到实施计划
在需求基本明确、需要拆分实现任务或验收标准时使用。

## 入口与 Grilling 的衔接
- 如果目标、截图权限方案、隐私边界、同步策略等关键决策仍未确认，先调用 `../grilling/SKILL.md`，通过决策树逐轮澄清。
- 读取 Grilling 输出、并经用户确认的「共识摘要」作为本 Skill 的输入。单纯的 AI 推荐不等于用户决定。
- 对于未确认但阻塞实现的重大事项，返回 Grilling 继续讨论；低优先级事项明确标记为假设或延期项。
- 无需强制每次都运行 Grilling：简单 bug 修复或需求明确的任务可以直接规划。

## 计划生成
1. 重述经确认的目标、环境、范围与限制；引用已确认的决策和待验证事实。
2. 按用户旅程划分 MVP / 后续迭代；避免未经要求引入复杂基础设施。
3. 设计数据流、权限边界、失败路径、隐私策略。
4. 输出文件级实现步骤、依赖关系、风险、验证方法与回滚办法。
5. 给出可测试的验收标准和设备/环境测试矩阵。
6. 标注仅能在真实设备验证的功能，不假装已经测试。
7. 重大取舍由用户决定，未经授权不自动执行开发或部署。

参考：https://github.com/obra/superpowers （brainstorming、writing-plans、verification-before-completion）。
