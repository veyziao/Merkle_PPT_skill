# Merkle PPT Skill 使用指南

这份 Skill 用于在 Codex 中制作、修改和检查 Merkle 风格的 PowerPoint。它包含 2026 Merkle Arial 模板、页脚素材、版式参考和已确认的制作规则。

## 1. 准备访问权限

仓库目前为私有仓库。同事需要 GitHub 账号、仓库的读取权限，以及已登录的 Codex。请联系仓库管理员开通访问权限并接受 GitHub 邀请。

仓库地址：[Merkle_PPT_skill](https://github.com/veyziao/Merkle_PPT_skill)

## 2. 安装 Skill

在 Codex 中开启对话，发送以下内容：

```text
请使用 $skill-installer 从 GitHub 安装这个 Skill：
仓库 veyziao/Merkle_PPT_skill
分支 main
Skill 路径 merkle-ppt
```

Codex 会使用当前环境的 GitHub 访问凭据获取私有仓库，并将 Skill 安装到个人 Codex 的 skills 目录。按界面提示完成所需的 GitHub 授权。安装成功后，下一次对话即可使用。

如果提示无法访问仓库，请先确认 GitHub 邀请已接受、当前凭据属于获授权的账号，然后请 Codex 重新尝试。如果提示 Skill 已存在，请参考下方的更新步骤。

## 3. 制作 PPT

在新对话中上传内容资料，然后提出制作要求。例如：

```text
请使用 $merkle-ppt，根据我上传的资料制作一份可编辑的 PowerPoint。
听众是项目管理层，语言为中文，重点说明项目背景、方案、时间安排和下一步。
```

为了得到符合用途的结果，可以在需求中说明听众、语言、页面数量、需要保留的原文、内容重点和交付格式。

Skill 默认以官方 Arial 模板为基础。普通浅色内容页使用左下角 M 角标和右下角页码。需要页脚中央出现 dentsu 标志时，请在提示中明确说明。

## 4. 更新已安装的 Skill

仓库更新后，已安装的本地副本需要重新安装才能获得新版。在 Codex 中发送：

```text
请把我已安装的 merkle-ppt Skill 更新到
veyziao/Merkle_PPT_skill 仓库 main 分支的最新版本。
更新前请保留现有版本的备份。
```

安装器遇到同名 Skill 时会停止，以保护现有副本。Codex 可先备份旧版本，再安装新版。更新后开启新对话使用。
