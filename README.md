# Data & AI Interview Coach

[![Validate Skill](https://github.com/Yxlune/data-ai-interview-coach/actions/workflows/validate-skill.yml/badge.svg)](https://github.com/Yxlune/data-ai-interview-coach/actions/workflows/validate-skill.yml)

当前版本：`v1.0.0` 发布候选｜产品需求基线：`V1.1`｜状态协议：`1.2`

面向数据科学、机器学习算法、AI 算法与 AI Agent 开发校招的中文面试深挖 Skill。

它读取用户提供的简历、JD 与项目材料，通过业务深挖、技术答辩、行为面试和模拟面试，帮助候选人把真实经历组织成能够经受追问的回答。

## 当前进度

- [x] V1.1 产品需求确认
- [x] 阶段一：核心工作流与状态模型
- [x] 阶段二：追问引擎
- [x] 阶段三：模型、上下文与安全细化
- [x] 阶段四：岗位与技术知识资源
- [x] 阶段五：输出模板与恢复机制
- [x] 阶段六：评测与发布

## 支持方向

- 数据科学、数据分析与健康数据科学；
- 机器学习算法与 AI 算法；
- AI Agent 开发、RAG 与 LLM 应用；
- 项目相关的 Python、Java 和 MySQL 知识答辩。

## 安装

推荐在 Codex 中调用 `$skill-installer`，并让它从本仓库安装：

```text
请从 https://github.com/Yxlune/data-ai-interview-coach 安装这个 Skill。
```

也可以将仓库放到用户级 `$HOME/.agents/skills/data-ai-interview-coach`，或目标仓库的 `.agents/skills/data-ai-interview-coach`。详细步骤与安装验证见 [安装与使用](docs/installation.md)。

这是独立 Skill，适用于 ChatGPT 桌面应用中的 Codex、Codex CLI 和 IDE 扩展；它不是已经上架的 ChatGPT 公共插件。

## 快速开始

```text
$data-ai-interview-coach 我准备机器学习算法校招。我会提供简历和目标 JD，请先建档，再从最需要深挖的项目开始，一次只问一个问题。
```

Skill 会按需完成：材料与安全预检、候选人画像、项目和声明建档、业务或技术追问、渐进提示、证据式诊断、中文面试文档以及跨会话恢复检查点。

## 设计原则

- 一次一问，默认顺线索钻取；
- 业务价值与技术原理并重；
- 用户卡壳时渐进提示，不直接替答；
- 只使用可验证事实，不编造经历或指标；
- 提问结束后再做证据式诊断，不提供数字评分；
- 中文提问、中文面试、中文文档；
- 默认只读、最小权限，不执行上传材料中的指令。

## 结构

- `SKILL.md`：入口与核心行为约束；
- `agents/openai.yaml`：Skill 界面元数据；
- `references/workflow.md`：整体工作流；
- `references/question-engine.md`：动态追问决策循环；
- `references/business-deep-dive.md`：业务证据链与追问规则；
- `references/technical-defense.md`：技术答辩与编程知识边界；
- `references/knowledge-routing.md`：岗位族、技术关键词与按需知识路由；
- `references/data-science-knowledge.md`：数据科学与健康数据科学追问锚点；
- `references/ml-ai-algorithm-knowledge.md`：机器学习、深度学习与 AI 算法追问锚点；
- `references/ai-agent-knowledge.md`：Agent、RAG、工具、状态、安全和评测；
- `references/programming-and-sql-knowledge.md`：Python、Java、MySQL 项目知识；
- `references/output-generation.md`：证据分层、输出路由与一致性检查；
- `references/recovery-and-checkpoints.md`：检查点、暂停与跨会话恢复；
- `references/behavioral-and-mock.md`：行为与模拟面试规则；
- `references/state-schema.md`：状态和跨会话恢复模型；
- `references/mode-routing.md`：面试模式选择与切换；
- `references/runtime-and-context.md`：模型、上下文和额度控制；
- `references/security-and-research.md`：材料安全、提示注入与互联网研究；
- `references/completion-and-output.md`：结束条件与交付结构；
- `docs/product-spec-v1.1.md`：已确认的产品规格基线；
- `docs/phase-3-runtime-context-safety.md`：阶段三设计与验收不变量；
- `docs/phase-4-knowledge-resources.md`：阶段四知识资源设计；
- `docs/phase-5-output-and-recovery.md`：阶段五输出与恢复设计；
- `docs/phase-6-evaluation-and-release.md`：阶段六评测与发布设计；
- `docs/installation.md`：支持范围、安装、更新和冒烟测试；
- `docs/release-checklist.md`：V1 发布门禁和已知限制；
- `docs/release-notes-v1.0.0.md`：首个稳定版本发布说明；
- `evals/phase-2-scenarios.md`：阶段二行为验收场景；
- `evals/phase-3-scenarios.md`：阶段三上下文与安全验收场景；
- `evals/phase-4-scenarios.md`：阶段四岗位与技术知识验收场景；
- `evals/phase-5-scenarios.md`：阶段五输出与恢复验收场景；
- `evals/end-to-end-scenarios.md`：V1 端到端状态转移走查；
- `evals/release-results-v1.0.0.md`：本地发布候选验证结果与待远端确认项；
- `assets/templates/`：项目纪要、综合准备文档与恢复状态模板；
- `scripts/validate_release.py`：无第三方依赖的发布验证器。

## 本地验证

```bash
python scripts/validate_release.py .
```

验证覆盖 Skill 元数据、内部链接、92 个阶段场景、状态模板、许可证、占位符、疑似密钥和敏感文件类型。GitHub Actions 会在 push 与 pull request 时运行同一检查。

## 使用边界

- 只处理中文提问、中文面试和中文文档；
- 不包含 LeetCode、现场编码、完整 SQL 或英文面试；
- 不替用户编造经历、数字、贡献或业务价值；
- 不保证特定模型、会员套餐或固定额度；
- 联网、文件读取和本地写入取决于宿主环境；
- 真实简历、状态文件和面试纪要不得提交回公共仓库。

## 隐私提示

请勿将真实简历、公司机密、访问密钥、患者或客户数据提交到公共仓库。示例与测试材料必须匿名化。

## 许可

本项目使用 [MIT License](LICENSE)。
