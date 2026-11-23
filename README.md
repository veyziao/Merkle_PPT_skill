# Merkle PPT Skill

[中文](#中文) · [English](#english)

## 中文

Merkle PPT Skill 帮助 Codex 根据 Merkle 的模板和版式参考，制作、编辑和检查可编辑的 PowerPoint 演示文稿。

### 包含内容

- 2026 Merkle Arial 官方模板及其母版和 35 个版式。
- M 角标、Agenda 图案、可选的 dentsu 标志及相关页脚规则。
- 方案详情、时间轴、摘要与证据、交付物等内容页参考。
- 字体、字号、图片效果和交付检查规则。

Skill 会根据内容选择合适的版式。已有的客户模板和当前任务要求优先。

### 四个参考库

| 参考库 | GitHub 在线查阅 | 交互式离线版本 | 原始资料 |
| --- | --- | --- | --- |
| ICON Library | [图标目录及预览](libraries/icon-library.md) | [下载 HTML](libraries/icon-offline.html) | [ICON PPT](merkle-ppt/assets/Merkle_icon.pptx) |
| Slide Library | [页面版式及预览](libraries/slide-library.md) | [下载 HTML](libraries/slide-offline.html) | [Slide PPT](merkle-ppt/assets/Slide%20Library%20for%20ai.pptx) |
| Case Library | [案例版式及预览](libraries/case-library.md) | [下载 HTML](libraries/case-offline.html) | [Case PPT](merkle-ppt/assets/case%20library%20-%20Case%20Study%20Layout%20Types.pptx) |
| Diagram Library | [图形与架构及预览](libraries/diagram-library.md) | [下载 HTML](libraries/diagram-offline.html) | [Diagram PPT](merkle-ppt/assets/Diagram%20library%20-%20Diagram%20Elements.pptx) |

离线 HTML 请先在 GitHub 文件页面选择下载，再用浏览器打开；GitHub 页面不会直接运行其搜索功能。[Slide](libraries/slide-object-styles.csv)、[Case](libraries/case-object-styles.csv) 和 [Diagram](libraries/diagram-object-styles.csv) 的对象样式索引也可查阅；详细原始样式记录见 [说明](merkle-ppt/references/source-object-styles.md)。源案例中的客户、数据和素材仅供参考。ICON 优先使用原始 PPT 图形或经核对完全一致的版本。

### 安装

本仓库为私有仓库。使用前请确保已接受仓库邀请，并在 Codex 所在环境配置有权访问该仓库的 GitHub 凭据。

在 Codex 中发送以下内容：

```text
请使用 $skill-installer 从 GitHub 安装这个 Skill：
仓库 veyziao/Merkle_PPT_skill
分支 main
Skill 路径 merkle-ppt
```

按提示完成授权。安装成功后，在下一次对话中即可使用。

### 使用

上传资料后，在 Codex 中说明听众、语言、内容重点和交付要求。例如：

```text
请使用 $merkle-ppt，根据我上传的资料制作一份可编辑的 PowerPoint。
听众是项目管理层，语言为中文，重点说明项目背景、方案、时间安排和下一步。
```

普通浅色内容页默认使用左下角 M 角标和右下角页码。若需要在页脚中央加入 dentsu 标志，请在需求中明确说明。

### 更新

仓库更新后，已安装的本地副本需要重新安装。可以在 Codex 中发送：

```text
请将已安装的 merkle-ppt Skill 更新到
veyziao/Merkle_PPT_skill 的 main 分支最新版本。
更新前请保留现有版本的备份。
```

安装器检测到同名 Skill 时会停止。请先备份现有版本，再安装新版。更新后开启新对话使用。

如果无法访问仓库，请确认 GitHub 邀请已接受，并检查当前环境使用的账号是否具有仓库读取权限。

## English

Merkle PPT Skill helps Codex create, edit and review editable PowerPoint presentations using Merkle templates and layout references.

### What is included

- The official 2026 Merkle Arial template, including its slide master and 35 layouts.
- The M avatar, Agenda artwork, optional dentsu mark and footer guidance.
- Content-slide references for solution details, timelines, summaries with evidence, and deliverables.
- Typography, image effects and presentation review guidance.

Codex selects layouts to suit the content. The current task and any supplied client template take priority.

### Reference libraries

| Library | Browse on GitHub | Offline interactive version | Source |
| --- | --- | --- | --- |
| ICON | [Icon catalog and previews](libraries/icon-library.md) | [Download HTML](libraries/icon-offline.html) | [ICON PPT](merkle-ppt/assets/Merkle_icon.pptx) |
| Slide | [Slide layouts and previews](libraries/slide-library.md) | [Download HTML](libraries/slide-offline.html) | [Slide PPT](merkle-ppt/assets/Slide%20Library%20for%20ai.pptx) |
| Case | [Case layouts and previews](libraries/case-library.md) | [Download HTML](libraries/case-offline.html) | [Case PPT](merkle-ppt/assets/case%20library%20-%20Case%20Study%20Layout%20Types.pptx) |
| Diagram | [Diagrams and previews](libraries/diagram-library.md) | [Download HTML](libraries/diagram-offline.html) | [Diagram PPT](merkle-ppt/assets/Diagram%20library%20-%20Diagram%20Elements.pptx) |

Download the HTML file from GitHub and open it locally for interactive search; GitHub does not run it in the file view. Object-level style indexes for [Slide](libraries/slide-object-styles.csv), [Case](libraries/case-object-styles.csv) and [Diagram](libraries/diagram-object-styles.csv) are available with the [style reference guide](merkle-ppt/references/source-object-styles.md). Source clients, data and materials are examples, not evidence for a new project. Use the source ICON artwork or a verified visually identical version.

### Installation

This repository is private. Before installation, accept the repository invitation and configure GitHub credentials with read access in the environment where Codex runs.

Send the following message in Codex:

```text
Please use $skill-installer to install this skill from GitHub:
Repository: veyziao/Merkle_PPT_skill
Branch: main
Skill path: merkle-ppt
```

Complete any authorization prompts. The skill is available on the next turn after installation.

### Usage

Upload your materials and describe the audience, language, key content and desired output. For example:

```text
Use $merkle-ppt to create an editable PowerPoint based on the files I uploaded.
The audience is project leadership. Use English and cover the background,
proposed approach, timeline and next steps.
```

General light-background content slides use the M avatar at the bottom left and a page number at the bottom right. Explicitly request the centered dentsu mark if you need it.

### Updating

When the repository changes, reinstall the skill to update your local copy. In Codex, you can say:

```text
Please update my installed merkle-ppt skill to the latest version
on the main branch of veyziao/Merkle_PPT_skill.
Back up the existing version before updating.
```

The installer stops if a skill with the same name already exists. Back up the existing copy before installing the new version, then start a new conversation.

If the repository cannot be accessed, confirm that you accepted the GitHub invitation and that the credentials in the current environment have read access.

## Repository

- [Skill instructions](merkle-ppt/SKILL.md)
- [Official layout guide](merkle-ppt/references/official-layouts.md)
- [Content-page references](merkle-ppt/references/user-curated-layouts.md)

