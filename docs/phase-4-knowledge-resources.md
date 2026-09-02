# 阶段四：岗位与技术知识资源

## 目标

阶段四为动态追问引擎提供岗位相关的技术考察维度，使 Skill 能从用户项目中的 XGBoost、深度学习、RAG、Python、Java、MySQL 等关键词继续追问原理、选型、参数、实验、工程和局限，同时避免退化为固定题库或冷知识考试。

## 资源架构

```text
JD + 当前项目 + 技术栈图谱
  → knowledge-routing.md
  → 一个主岗位知识包
      ├─ data-science-knowledge.md
      ├─ ml-ai-algorithm-knowledge.md
      └─ ai-agent-knowledge.md
  → 可选的 programming-and-sql-knowledge.md
  → question-engine.md 选择下一问
```

混合岗位最多增加一个辅岗位知识包。语言与数据库资源只有项目或 JD 触发时加载。`technical-defense.md` 保留通用技术证据链，各知识包只存放会改变追问方向的领域规则。

## 关键决策

### 项目证据优先

知识资源不能证明用户掌握或实施了某技术。追问必须先确认技术在项目中的用途，再进入选型、原理、实现、验证和边界。理论正确但缺少项目证据时，记录为知识储备或合理方案，不能改写成个人经历。

### 深度而非覆盖数量

简历核心技术和 JD 高频能力需要深入；辅助库、未实际使用的框架和加分项可以停在概念及适用场景。一次只问一个主问题，不为了覆盖知识包连续罗列参数。

### 稳定知识与动态事实分离

稳定的数学直觉、实验设计和工程取舍保存在资源文件。框架 API、默认参数、弃用状态、模型能力、论文最新结论和公司术语按需查询官方文档或原始论文，并记录版本和查询日期。

### 编程边界

Python、Java 和 MySQL 只进行项目型知识问答，不要求编写程序或完整 SQL。问题围绕用户真实实现、性能、异常、并发、事务、索引和可维护性。

## V1 岗位范围

- 数据科学、数据分析和健康数据科学；
- 机器学习算法与 AI 算法；
- AI Agent 开发与 RAG/LLM 应用；
- Python、Java、MySQL 的项目相关基础和工程知识。

数据开发不是 V1 主岗位族；只有作为上述项目的数据管道组成部分时提供有限追问。

## 文件变更

- 新增岗位与关键词路由；
- 新增数据科学知识包；
- 新增机器学习与 AI 算法知识包；
- 新增 AI Agent 知识包；
- 新增 Python、Java 与 MySQL 项目知识包；
- 更新 Skill 入口、技术答辩路由、技术栈状态和产品进度；
- 新增阶段四验收场景。

## 验收不变量

- 主岗位知识包只能有一个，混合岗位最多增加一个辅包；
- 技术问题必须关联项目事实、岗位能力和当前缺口；
- 不把框架名、论文或外部资料当作用户实施证据；
- 不要求现场编码或完整 SQL；
- 不一次抛出参数清单或多道独立知识题；
- 版本相关事实先确认项目版本，再查对应官方来源；
- 数据科学结论区分预测、关联和因果；
- Agent 结论区分 Demo、离线评测和生产可靠性。

## 参考来源

资源设计核对了以下官方资料，用于确认稳定考察维度，不把 Skill 绑定到特定版本：

- [scikit-learn：常见陷阱与数据泄漏](https://scikit-learn.org/stable/common_pitfalls.html)
- [scikit-learn：模型指标与评分](https://scikit-learn.org/stable/modules/model_evaluation.html)
- [XGBoost：参数文档](https://xgboost.readthedocs.io/en/stable/parameter.html)
- [Python：asyncio](https://docs.python.org/3/library/asyncio.html)
- [Oracle Java：Concurrency](https://docs.oracle.com/javase/tutorial/essential/concurrency/)
- [MySQL：InnoDB Transaction Isolation Levels](https://dev.mysql.com/doc/refman/8.4/en/innodb-transaction-isolation-levels.html)
- [OpenAI Docs：Evaluate agent workflows](https://developers.openai.com/api/docs/guides/agent-evals)

运行时仍须根据用户实际版本重新核验动态事实。

