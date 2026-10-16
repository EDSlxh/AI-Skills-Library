# 从索引恢复到 D 盘

## 1. 先保住本地独有数据

不要先删除 `Documents\Codex`、`Documents\ChatGPT`、`.agents` 或 `.codex`。公开包只有清单和恢复脚本，本地筛选源码包也不是完整数据备份。照片、二进制文档、生成报告及其他未入包文件仍须保留原件或另行完整备份。详细入包文件及遗漏见 D 盘备份目录的 `local-source-index.json`。

已有 `D:\AI-Home\Projects` 等目录只是早先暂存副本；不要把“目录存在”当作当前内容一致。之前的 Finish-Migration / Move-Large-Files 辅助脚本不属于这个恢复流程，也没有因打包而获得完整验收。

## 2. 应用重装属于可选步骤

扫描时已安装包名是 `OpenAI.Codex`，虽然进程可能叫 ChatGPT。安装位置仍在 C 盘 WindowsApps；部分由 Windows 管理的应用数据已经在 D 盘。不要手工复制、删除 WindowsApps 或修改其权限。

可先在 Windows“设置 → 应用 → 已安装的应用”查找应用是否提供“移动”。若支持，可通过 Windows 移到 D 盘。若要重装，先在“设置 → 系统 → 存储 → 高级存储设置 → 保存新内容的地方”检查“新的应用将保存到”能否设 D，再使用官方安装来源；应用自身可能不支持非系统盘安装，最终必须检查实际包位置。本流程不会代为改这些系统设置、卸载应用或注销账号。

重装应用不会自动把个人项目、uv/npm 缓存、模型都放到 D。Codex 的配置、登录及会话等状态由 `CODEX_HOME`（默认 `~/.codex`）管理，独立于程序安装路径。不要把账号凭据上传 GitHub；需要时重新登录。完整恢复本地会话需要另行保护原 `.codex` 状态，公开包不提供这部分恢复能力。

参考：[OpenAI 配置与状态位置](https://learn.chatgpt.com/docs/config-file/config-advanced#config-and-state-locations)、[Microsoft 存储说明](https://support.microsoft.com/en-us/windows/experience/storage-filemanagement/free-up-drive-space-in-windows)、[Microsoft Appx 官方移动命令说明](https://learn.microsoft.com/en-us/powershell/module/appx/move-appxpackage)。官方命令文档不保证本应用一定支持移动；应以当前 Windows 提供的操作和实际检测为准。

## 3. 新建 D 盘工作环境

先安装或确认 Git 与 uv 可用。在 PowerShell 进入解压后的索引目录：

```powershell
.\Verify-Package.ps1
.\Restore-To-D.ps1
.\Restore-To-D.ps1 -Apply
```

默认生成 `D:\AI-Home\Fresh-日期时间`，拒绝覆盖已有目录。脚本只克隆 `sources.json` 中固定版本的公开 Skill 库，不包含这个新增备份目录本身；源码是可恢复的历史基线。Git clone 失败时保留原件，并选择另一个新目录重试。

按脚本输出，在需要的 PowerShell 中加载新目录的 `Environment.ps1`，然后在其子进程运行工具。变量只对当前 PowerShell 及子进程生效，不自动改变桌面 App、既有项目 `.runtime` 或已有缓存的位置。

```powershell
. 'D:\AI-Home\Fresh-实际日期时间\Environment.ps1'
uv run "$env:CLAUDE_SKILL_DIR\scripts\doctor.py" --network
```

doctor 只做其实际覆盖的检查，不证明 OCR、CLIP、DINOv2 等已恢复。已有 Skill 同步程序的 `--check` 可以比较本地技能；写入前审阅差异，保留自定义内容，禁止直接覆盖 `.codex`。内置技能与插件由应用/插件管理机制恢复，不能只克隆 Skill 文本来替代服务运行环境。

## 4. 恢复个人修改与模型

将本地 `LOCAL-ONLY-selected-sources.zip` 解到一个新的临时目录，按 `local-source-index.json` 的 SHA-256 检查，再与对应项目逐项比较。压缩包以 `projects-codex/`、`personal-skills/` 等分类保留相对路径，不应直接整体解压覆盖 C 盘或现有 D 盘项目。

geo-sleuth 的两个本地兼容修复及启动脚本在本地筛选源码包中，公开库的固定基线没有这些修复。`geo-deployment-reports/local-overrides.diff`、源码副本和部署记录只留本地。恢复它们时同时核对当前上游差异。

两个模型共约 661 MiB 权重；其依赖和浏览器等还需额外空间。模型未入包。按 `sources.json` 的 revision 和 SHA-256 重用已经验证的本地权重或另行下载；实际下载和依赖安装是独立步骤，需网络与相应下载授权。本索引没有锁定全部传递依赖，也不承诺离线重装。

OCR、地图、反搜和模型推理分别进行最小验证；地图外部服务失败要如实记录。收到新照片后再启动真实定位，保留原图；反向搜图需单独取得图片提交授权，恢复脚本不会上传任何照片。

## 5. 验证以后再清理 C 盘

确认 D 盘项目实际可用、个人文件已完整另存、模型能加载，并重新检查旧 C 路径的占用者。每一类数据都应在确认备份和恢复后单独处理。本包不运行删除、目录联接、强制结束进程或系统级迁移；生成这个包本身不会释放 C 盘空间。
