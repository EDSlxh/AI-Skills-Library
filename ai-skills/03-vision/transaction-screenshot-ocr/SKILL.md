---
name: transaction-screenshot-ocr
description: Design privacy-aware screenshot transaction extraction with OCR, app-specific fast paths, confidence scores, and human confirmation.
---
# 交易截图识别
用于淘宝、京东、支付宝、微信支付、美团及其他消费界面的通用截图记账。

1. 图片先在本地处理：裁剪区域、方向校正、OCR、布局/关键词抽取。
2. 通过可配置白名单匹配来源应用或页面模板，命中时走高置信度快速规则；不命中时回退通用解析，不能把白名单作为排除未知图片的黑名单。
3. 提取 amount、currency、merchant、category、item、timestamp、transaction_id、payment_status、source、confidence 与 evidence。
4. 区分“付款成功”“待支付”“退款”“转账”“充值”；对金额歧义、多个金额、截图重复强制人工确认或标记待核实。
5. 保存字段来源和识别版本；仅经用户确认后写入正式账本。
6. 以脱敏样本构建覆盖多平台、多主题、夜间模式、长图、遮挡、不同分辨率的回归测试。
7. 不上传原始截图到第三方服务，除非用户明确选择并知情。

本 Skill 为当前项目整理的自定义流程，而非声称第三方 OCR 模型能力。