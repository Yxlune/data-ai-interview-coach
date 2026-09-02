# 安装与使用

## 当前支持范围

这是一个独立的本地 Skill，适用于：

- ChatGPT 桌面应用中的 Codex；
- Codex CLI；
- Codex IDE 扩展。

独立 Skill 不等同于已经上架的 ChatGPT 插件。若需要在 ChatGPT 网页端或移动端以公共插件方式安装，需要后续再进行插件封装与发布。

## 推荐安装

在 Codex 中调用 `$skill-installer`，然后提出：

```text
请从 https://github.com/Yxlune/data-ai-interview-coach 安装这个 Skill。
```

安装后可以在 Skill 列表中确认 `data-ai-interview-coach` 是否出现。Codex 通常会自动发现新安装的 Skill；如果没有显示，重启 Codex 后再检查。

## 手动安装

### 用户级安装

将完整仓库放到个人 Skill 目录：

```text
$HOME/.agents/skills/data-ai-interview-coach/
```

该目录下应直接包含 `SKILL.md`，不能额外嵌套一层同名目录。

Windows PowerShell 示例：

```powershell
git clone https://github.com/Yxlune/data-ai-interview-coach.git "$env:USERPROFILE\.agents\skills\data-ai-interview-coach"
```

macOS 或 Linux 示例：

```bash
git clone https://github.com/Yxlune/data-ai-interview-coach.git "$HOME/.agents/skills/data-ai-interview-coach"
```

### 仓库级安装

若只希望当前项目使用，可以把 Skill 放到目标仓库的：

```text
<目标仓库>/.agents/skills/data-ai-interview-coach/
```

Codex 会从当前工作目录向上扫描仓库范围内的 `.agents/skills`。

## 验证安装

1. 确认 Skill 列表中出现“数据与 AI 面试深挖教练”；
2. 显式调用：

```text
$data-ai-interview-coach 我准备数据科学校招，请先告诉我需要提供哪些材料。
```

3. 预期行为：使用中文回应，只索取当前步骤必要的材料，不立即批量提问；
4. 再提供一段匿名项目简介，确认它一次只问一个主问题；
5. 如果 Skill 没有出现，检查目录层级后重启 Codex。

## 更新

进入 Skill 目录后获取仓库最新版本。更新后 Codex 通常会自动检测；若行为仍是旧版本，重启后再次检查。

更新前请先把真实面试状态和项目纪要保存在仓库之外。仓库默认忽略 `interview-prep-state.md`、`docs/deep-dive/`、`private/` 和 `user-data/`，但用户仍需检查自己选择的保存位置。

## 开始使用

可以从以下请求开始：

```text
$data-ai-interview-coach 我准备机器学习算法校招。我会提供简历和目标 JD，请先建档，再从最需要深挖的项目开始，一次只问一个问题。
```

常用请求：

- “切换到技术答辩，继续追问刚才项目里的 XGBoost。”
- “我不知道怎么回答，请给我一个思考方向，不要直接替我编答案。”
- “今天先到这里，请生成可在新会话恢复的检查点。”
- “这个项目已经挖透了，请生成项目深挖纪要。”
- “根据已完成内容生成综合面试准备文档。”

## 隐私提醒

- 上传前删除访问密钥、密码、Cookie、连接串和内部地址；
- 对患者、客户、员工、公司项目与业务数字进行脱敏；
- 不要把真实简历、状态文件和面试纪要提交回公共 Skill 仓库；
- 需要联网查询时，只使用不含个人或公司机密的通用关键词。

## 官方兼容依据

安装位置、自动发现、显式调用和重启规则依据 [OpenAI 官方 Build skills 文档](https://learn.chatgpt.com/docs/build-skills)，核对日期为 2026-09-02。平台能力可能更新，安装异常时以最新官方说明为准。
