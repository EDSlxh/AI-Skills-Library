---
name: android-app-engineering
description: Implement maintainable Kotlin Android apps using Compose, ViewModel, Room, coroutines, and permission-aware system integrations.
---
# Android 工程实现
用于 Android / Kotlin / Jetpack Compose 项目，尤其是记账 App。

1. 先确认 Android SDK、目标机型、MIUI/HyperOS 限制与 targetSdk，再选用 API。
2. 采用 UI (Compose) → ViewModel/StateFlow → UseCase → Repository → Room 或远端服务；防止 UI 层直接操作数据库。
3. 用结构化协程、可取消任务和生命周期感知收集数据流，确保耗时 OCR 不阻塞主线程。
4. 对状态栏快捷设置磁贴、截图、前台服务、MediaProjection 严格核查 Android 版本和用户同意要求；不能假设系统允许静默截屏。
5. 最小权限，敏感数据本地优先，生产日志不得含支付金额之外的敏感账户信息。
6. 变更需附构建、lint、单元测试或无法执行的说明。

参考：https://github.com/new-silvermoon/awesome-android-agent-skills ；https://github.com/krutikJain/android-agent-skills 。