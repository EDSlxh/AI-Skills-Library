---
name: ledger-data-sync
description: Model personal expense ledgers, reporting, import/export, migration, and safe multi-device synchronization.
---
# 账本数据与同步
1. 建立稳定 ID、金额的最小货币单位（整数）、币种、时区、类型、类别、商家、时间、来源、审核状态。
2. 使用 Room + migrations；消费、收入、退款及转账分别建模，汇总时防止重复计算。
3. 日、周、月报表明确日期边界；分类统计写聚合测试；避免浮点金额误差。
4. CSV/JSON 导入导出需版本化格式、字段校验、去重、原子事务及备份。
5. 同步要设计冲突解决、离线队列、删除墓碑与设备间幂等，不能仅凭时间戳覆盖全部数据。
6. 金融记录与截图默认敏感；限制日志、明文备份和未经许可的云传输。
7. 提供数据擦除、备份恢复演练与迁移失败回滚方案。