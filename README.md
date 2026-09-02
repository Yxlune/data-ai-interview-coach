# Data & AI Interview Coach

面向数据科学、机器学习算法、AI 算法与 AI Agent 开发校招的中文面试深挖 Skill。

它读取用户提供的简历、JD 与项目材料，通过业务深挖、技术答辩、行为面试和模拟面试，帮助候选人把真实经历组织成能够经受追问的回答。

## 当前进度

- [x] V1.1 产品需求确认
- [x] 阶段一：核心工作流与状态模型
- [x] 阶段二：追问引擎
- [x] 阶段三：模型、上下文与安全细化
- [x] 阶段四：岗位与技术知识资源
- [ ] 阶段五：输出模板与恢复机制
- [ ] 阶段六：评测与发布

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
- `references/behavioral-and-mock.md`：行为与模拟面试规则；
- `references/state-schema.md`：状态和跨会话恢复模型；
- `references/mode-routing.md`：面试模式选择与切换；
- `references/runtime-and-context.md`：模型、上下文和额度控制；
- `references/security-and-research.md`：材料安全、提示注入与互联网研究；
- `references/completion-and-output.md`：结束条件与交付结构；
- `docs/product-spec-v1.1.md`：已确认的产品规格基线；
- `docs/phase-3-runtime-context-safety.md`：阶段三设计与验收不变量；
- `docs/phase-4-knowledge-resources.md`：阶段四知识资源设计；
- `evals/phase-2-scenarios.md`：阶段二行为验收场景。
- `evals/phase-3-scenarios.md`：阶段三上下文与安全验收场景。
- `evals/phase-4-scenarios.md`：阶段四岗位与技术知识验收场景。

## 隐私提示

请勿将真实简历、公司机密、访问密钥、患者或客户数据提交到公共仓库。示例与测试材料必须匿名化。

## 许可

本项目使用 [MIT License](LICENSE)。

