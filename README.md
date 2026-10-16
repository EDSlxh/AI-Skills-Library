# AI-Skills-Library

可复用的产品、开发和科学学习流程。可在有读取能力的聊天中按需加载，也可作为 ChatGPT 项目的资料使用；GitHub 文件本身不会自动安装为原生 Skill。

- [Skill 选择索引](SKILLS.md)：根据需求选择合适流程，包含 10 个 Skill。
- [手机使用与配置](docs/mobile-setup.md)：个性化、项目资料、GitHub 版本和题卡能力边界。
- [ChatGPT 个性化文本](mobile/personalization.txt)：复制到自定义指令中，保留原有偏好。
- [学习项目指令](mobile/project-instructions.txt)：用于独立学习项目。
- [手机项目资料包](mobile/mobile-skills-bundle.md)：上传到项目 Sources，包含索引、全部 Skill 正文与学习引用。
- [技能目录及开发协作](ai-skills/README.md)。
- [本地同步清单](skills.json)：9 个独立技能及 1 个由题卡插件管理的技能。
- [高中函数学习测试项目](examples/function-learning/README.md)：含课程、题库、初始化模板与一份可上传的合并文件。

科学学习支持目标、示例、主动尝试、反馈、图解和间隔复习。真实互动题卡仍需要可用的题卡服务与聊天宿主支持；当前仓库没有运行该服务，也不保存个人成绩。

更新 Skill 后运行 `python tools/build_mobile_bundle.py`，用 `--check` 检查项目包与源文件是否一致。再把新包上传到项目替换旧版本。

## 本地技能同步

在此仓库运行 `python tools/sync_local_skills.py --check` 查看本地与库中的差异。审阅后运行 `python tools/sync_local_skills.py --install`：更新已有个人技能，新增技能放到 `~/.agents/skills/`，保留已有的 `~/.codex/skills/` 安装位置。修改前备份到本仓库被忽略的 `.local-sync/backups/`；发现本地独有文件或重复安装位置时停止，先合并这些差异。

`learning-cards` 保留由现有插件提供工具与技能发现，同步脚本只核对其技能指令，不建立重复安装。题卡服务、运行环境和模型仍由对应工具提供；系统内置技能和官方插件缓存沿用各自的管理方式。

`geo-sleuth` 同步完整脚本、数据和参考资料，来源与 MIT 许可见其 [上游说明](ai-skills/07-geolocation/geo-sleuth/UPSTREAM.md)。本库的其余内容不因此自动改用该许可证。
