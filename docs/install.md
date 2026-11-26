# 非技术成员安装指南

先把团队项目链接发给 Codex，并说“帮我安装 GitHub Collaborator 并加入这个项目”。若已安装兼容版本的 GitHub CLI，Codex 可在得到你的请求后用官方 `gh skill install` 从该项目链接安装 Skill，并验证安装结果；不需要你打开命令行。当前验证环境为 GitHub CLI 2.97.0，带 `gh skill` 预览功能；其他版本可能没有此命令，Codex 必须先检查而不能假定可用。Codex 不能自动完成登录、组织审批或人类接受邀请。

如果自动安装不可用，Codex 应先说明原因，再使用已验证可用的 Codex Skill 安装入口。手动复制是最后备用方案。你不需要安装 Git 或创建访问令牌才能先阅读项目。

## 下载

1. 下载 `dist/github-collaborator-skill.zip` 并解压。
2. 解压后会看到 `github-collaborator` 文件夹，里面有 `SKILL.md`、`references` 和 `assets`。请保留整个文件夹，不要只复制 `SKILL.md`。

## 备用：手动安装

仅当 Codex 确认自动安装不可用时，才将完整文件夹复制到 Codex 用户 Skill 目录：

- **macOS**：在 Finder 按 `Command + Shift + G`，输入 `~/.codex/skills/`。如果 `skills` 不存在，就新建它。将文件夹放进去。
- **Windows**：在文件资源管理器地址栏输入 `%USERPROFILE%\.codex\skills\`。若目录不存在，请新建；再放入文件夹。
- **Linux**：在文件管理器打开 `~/.codex/skills/`；若不存在，新建目录后放入文件夹。

Codex 支持的目录因版本和运行方式可能不同；优先使用当前界面明确提供的安装方式，不要假设重启或复制就一定成功。

## 启用并开始

1. 让 Codex 检查是否已找到 `github-collaborator`。
2. 若当前版本需要新会话才能发现，按 Codex 的提示开启新会话。
3. 在消息里粘贴团队给你的 GitHub 仓库链接。
3. 发送：

   > 我是这个项目的新成员。我没有使用过 GitHub，请使用 GitHub Collaborator Skill 帮我完成所有必要配置，并告诉我现在可以做什么。

4. 如果未自动触发，说：“请使用 GitHub Collaborator 帮我加入这个项目。”
5. Codex 会核实账号、项目和能做的事。需要登录、接受邀请或组织批准时，它会给出一个明确下一步，不会索取密码、验证码或访问令牌。

## 如果无法继续

把 Codex 给出的原话转发给团队管理员。常见原因是账号尚未受邀、组织要求审批、Codex 没有连上 GitHub，或当前电脑没有访问该项目。没有权限不代表项目不存在。无需把密码或验证码发给任何人。

日常操作示例见[加入团队，开始工作](member-quickstart.md)。
