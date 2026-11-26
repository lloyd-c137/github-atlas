# GitHub Collaborator

让 Codex 代办 GitHub 项目协作，让成员只需用自然语言表达想法、完成工作和作出决定。

> **Humans collaborate. Agents operate. GitHub remembers.**

本仓库包含可安装的 `github-collaborator` Skill、非技术成员安装与使用指南、项目负责人配置指南、场景验收清单和本次实测报告。Skill 使用 Agent Skills 开放目录格式，不需要额外服务器、数据库或 MCP Server。

## 交付结构

```text
github-collaborator/
├── SKILL.md
├── references/       # 按任务按需读取的协作流程和安全规则
└── assets/templates/ # Issue 模板
```

本仓库还提供：

- [架构与设计说明](docs/architecture.md)
- [非技术成员安装指南](docs/install.md)
- [新成员快速开始](docs/member-quickstart.md)
- [项目负责人配置指南](docs/maintainer-guide.md)
- [自然语言使用示例](docs/examples.md)
- [测试场景与验收标准](tests/scenarios.md)
- [实际测试报告和限制](tests/results.md)
- `dist/github-collaborator-skill.zip`：包含整个 Skill 文件夹的独立安装包

## 首次使用提示词

> 我是这个项目的新成员。我没有使用过 GitHub，请使用 GitHub Collaborator Skill 帮我完成所有必要配置，并告诉我现在可以做什么。

## 本地检查

需要 Python 3（标准库即可）：

```sh
python3 scripts/validate_skill.py
```

检查只验证 Skill 包装结构、必需元数据和文档引用，不会连接或写入 GitHub。

## 规范与调研

- [Agent Skills Specification](https://agentskills.io/specification)
- [OpenAI：Build skills](https://developers.openai.com/plugins/build/skills)
- [OpenAI：Testing Agent Skills systematically](https://developers.openai.com/blog/eval-skills)
- [GitHub CLI authentication](https://docs.github.com/en/github-cli/github-cli/authenticating-to-github)
- [GitHub CLI manual](https://cli.github.com/manual/)
- [GitHub CLI 官方 `gh` Skill](https://github.com/cli/cli/tree/trunk/skills/gh)
- [GitHub Issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues)
- [GitHub pull request reviews](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews)
- [GitHub Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects)
- [GitHub rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets)
- [GitHub Actions](https://docs.github.com/en/actions/about-github-actions/understanding-github-actions)
- [GitHub CODEOWNERS](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)

架构选择与平台限制详见设计说明及测试报告。
