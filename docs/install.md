# 非技术成员安装指南

安装只需把一个文件夹放进 Codex 的 Skill 文件夹。你不需要安装 Git、打开命令行或创建 GitHub 令牌才能先阅读项目；具体协作能力由 Codex 的 GitHub 连接和本机授权决定。

## 下载

1. 下载 `dist/github-collaborator-skill.zip` 并解压。
2. 解压后会看到 `github-collaborator` 文件夹，里面有 `SKILL.md`、`references` 和 `assets`。请保留整个文件夹，不要只复制 `SKILL.md`。

## 安装到 Codex

将完整的 `github-collaborator` 文件夹复制到 Codex 用户 Skill 目录：

- **macOS**：在 Finder 按 `Command + Shift + G`，输入 `~/.codex/skills/`。如果 `skills` 不存在，就新建它。将文件夹放进去。
- **Windows**：在文件资源管理器地址栏输入 `%USERPROFILE%\.codex\skills\`。若目录不存在，请新建；再放入文件夹。
- **Linux**：在文件管理器打开 `~/.codex/skills/`；若不存在，新建目录后放入文件夹。

如果你的 Codex 版本使用不同的 Skill 安装入口，请使用 Codex 的 Skills 管理界面将该文件夹导入用户范围。此目录约定已对照 Codex 官方文档；本指南没有在 Windows 或 Linux 客户端上实测界面差异。

## 启用并开始

1. 完全退出并重新打开 Codex（或刷新 Skills 列表）。
2. 打开一个项目文件夹，或在消息里粘贴团队给你的 GitHub 仓库链接。
3. 发送：

   > 我是这个项目的新成员。我没有使用过 GitHub，请使用 GitHub Collaborator Skill 帮我完成所有必要配置，并告诉我现在可以做什么。

4. 如果 Codex 没有自动识别 Skill，可以直接说：“请使用 `github-collaborator` Skill。”
5. Codex 会自己检查能做什么。需要 GitHub 登录、接受邀请、组织批准或人类决定时，它会给你一个直接的下一步，不会索取密码、验证码或访问令牌。

## 如果无法继续

把 Codex 给出的原话转发给团队管理员。常见原因是账号尚未受邀、组织要求审批、Codex 没有连上 GitHub，或当前电脑没有访问该项目。没有权限不代表项目不存在。无需把密码或验证码发给任何人。

日常操作示例见[加入团队，开始工作](member-quickstart.md)。
