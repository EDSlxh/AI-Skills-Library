---
name: requirement-to-plan
description: Turn a software feature request into a scoped, testable implementation plan with tradeoffs and acceptance criteria.
---
# 需求到实施计划
在新增重要功能、架构修改、需求模糊时使用。

1. 重述用户目标、环境和限制；明确已知与假设。
2. 按用户旅程划分 MVP / 后续迭代；避免未经要求加入复杂基础设施。
3. 设计数据流、权限边界、失败路径、隐私策略。
4. 输出文件级实现计划、验证方法与回滚办法。
5. 标注仅能在真实设备验证的功能，不假装已经测试。
6. 重大产品取舍由用户决定，不擅自更改原需求。

参考：https://github.com/obra/superpowers （brainstorming, writing-plans, verification-before-completion）。