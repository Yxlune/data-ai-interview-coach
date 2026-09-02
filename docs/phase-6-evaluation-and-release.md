# 阶段六：评测、安装验证与发布

## 目标

阶段六将前五个阶段的设计转化为可重复验证的 V1 发布候选，覆盖结构、行为、安全、恢复、安装和仓库发布卫生。

## 评测分层

### 1. 结构验证

使用 OpenAI Skill Creator 验证器检查 `SKILL.md` 的 frontmatter、名称和基础结构。

### 2. 仓库发布门禁

`scripts/validate_release.py` 使用 Python 标准库检查：

- 必需文件、MIT License 和 UI 元数据；
- Skill 名称、description 范围与默认调用提示；
- Markdown 内部链接；
- 阶段场景编号与期望数量；
- 状态模板 1.2 的恢复字段；
- 未完成占位符、疑似密钥、私钥和敏感文件类型；
- 真实状态文件与默认用户数据目录没有进入公共仓库。

`scripts/test_validate_release.py` 使用隔离副本确认验证器会拒绝缺失入口、失效链接、疑似密钥、真实状态文件和编号断裂，避免门禁只验证正向路径。

### 3. 原子行为场景

阶段二至五共 92 个场景，分别覆盖动态追问、模型与安全、岗位技术知识、输出与恢复。它们验证行为不变量，不锁定具体措辞。

### 4. 端到端流程

`evals/end-to-end-scenarios.md` 用 14 条跨阶段流程检查从材料摄入到输出恢复的状态转移。该走查由当前维护会话完成，不冒充独立模型基准测试。

### 5. 隔离安装冒烟测试

将仓库文件复制到临时 `.agents/skills/data-ai-interview-coach` 目录，确认 `SKILL.md` 位于正确层级，并对安装副本重新运行发布门禁。测试不写入用户真实 Skill 目录。

### 6. 持续验证

`.github/workflows/validate-skill.yml` 在 push 与 pull request 时使用 Python 3.12 执行同一发布门禁，防止后续改动破坏结构、场景或隐私边界。

实际本地结果记录在 `evals/release-results-v1.0.0.md`，尚未执行的远端动作保持待确认状态。

## 安装与兼容

依据 2026-09-02 核对的 [OpenAI 官方 Build skills 文档](https://learn.chatgpt.com/docs/build-skills)：

- 独立 Skill 可用于 ChatGPT 桌面应用中的 Codex、Codex CLI 和 IDE 扩展；
- 用户级 Skill 可以放在 `$HOME/.agents/skills`；
- 仓库级 Skill 可以放在仓库范围内的 `.agents/skills`；
- 可以让 `$skill-installer` 从其他仓库下载 Skill；
- Codex 通常自动检测改动，未出现时重启；
- 更广泛的网页、移动端和公共目录分发应考虑封装为插件。

## 发布候选

- Skill 版本：`v1.0.0`；
- 产品需求基线：`V1.1`；
- 状态文件 Schema：`1.2`；
- License：MIT；
- 发布形式：公开 GitHub 独立 Skill；
- 后续可选方向：公共插件封装、独立跨模型评测、更多岗位知识包。

## 不夸大的结论

- 自动验证通过不代表所有模型回答完全一致；
- 隔离安装测试验证目录和资源完整性，不等于所有宿主界面都已实机测试；
- 当前会话的规则走查不称为独立评测；
- Plus 或其他套餐的可用性和额度仍以宿主界面与最新官方规则为准。
