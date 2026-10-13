---
name: test-debug-review
description: Debug systematically, write regression tests, review changes, and verify actual build/test evidence before claiming completion.
---
# 测试、调试与审查
1. 复现问题：环境、输入、预期、实际、日志、可重复步骤。
2. 列出可验证的假设；一次调整一个关键变量，区分根因与症状。
3. 先写失败测试或最小复现，修复后加入回归测试。
4. 覆盖 OCR 多金额、退款、币种、时区、重复订单、同步冲突及无网络场景。
5. 审查权限最小化、数据泄露、线程安全、生命周期、性能及异常处理。
6. 报告实际执行的命令和结果；没有运行的构建/测试不得写“已通过”。
7. 重大更改走独立分支和 PR，标注风险与回滚说明。

参考：https://github.com/obra/superpowers （systematic-debugging, test-driven-development, requesting-code-review, verification-before-completion）。