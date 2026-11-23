# Merkle PPT Skill

**A reference-driven workflow for editable, Merkle-style presentations**  
**基于 Merkle 模板和参考资料的可编辑演示文稿制作流程**

[中文](#中文) · [English](#english) · [Reference libraries](#reference-libraries)

---

## 中文

Merkle PPT Skill 帮助 Codex 基于官方模板、版式案例和品牌素材，制作、编辑及检查可编辑的 PowerPoint。它将内容组织、页面选型、图标与图示选择、样式参考和交付检查串成一套工作流程，适合方案汇报、客户案例、项目进展及架构说明等场景。

### 核心能力

- **以官方模板为基础制作。** 新建演示文稿时使用 2026 Merkle Arial 模板，保留幻灯片母版、主题和 35 个命名版式。根据页面任务选择版式，并以其标题区域、边距和正文起点作为布局基准；需要自由组织时可使用自定义版式。
- **根据内容关系选择页面。** 对照 Slide Library 判断内容适合比较、时间安排、流程、证据展示还是其他形式；案例和架构图还可分别参考 Case Library 与 Diagram Library；业务回顾和阶段汇报可结合 QBR Library。参考页提供结构和视觉方法，不应机械照搬原业务内容。
- **保持 PowerPoint 可编辑。** 文本框、形状、连接线、表格和适用的图表应使用可编辑、可组合的原生对象；连续段落保留在单个文本框内，使用自动换行。照片、品牌图形及原始 SVG 等素材可作为独立图片对象使用。
- **追溯具体视觉样式。** Slide、Case 和 Diagram 资料包含对象级样式记录，可按源文件、页码和对象定位，检查颜色、渐变、透明度、边框、阴影、3D、图层及主题继承。具体交付仍需在目标 PowerPoint 环境中核对，不能仅凭属性记录认定完全一致。
- **优先使用原始图标。** ICON Library 包含 583 条图标索引，记录图形含义、潜在场景与源 PPT 定位。使用原始图标对象或原始 SVG；使用其他版本前应核实其外观与原图完全一致。
- **检查内容与呈现。** 工作流程要求核对事实与建议的区别、页面边界、文字溢出、字体替换、对象可编辑性、品牌元素和渲染效果。参考材料中的客户信息、数据和项目描述不能自动作为新项目的事实。

用户当前任务、客户模板和明确要求优先。这里的品牌和版式参考是基于所提供资料整理的工作指南，不等同于经过审批或始终最新的官方品牌规范。

### 默认设计规则

英文默认使用 **Arial Regular**，中文默认使用 **微软雅黑 Regular**；需要层级时可调整字重。普通浅色内容页继承左下角 M 角标和右下角页码；中央 dentsu 标志仅在明确要求时加入。结束页保留模板的 M 标志和版权行，默认不添加其他文字。

### 五个参考库

| Library | 内容 | 直接在 GitHub 查看 | 下载后离线搜索 | 原始 PPT |
| --- | --- | --- | --- | --- |
| ICON | 583 条图标索引，含用途与源文件定位 | [图标目录](libraries/icon-library.md) | [HTML](libraries/icon-offline.html) | [ICON PPT](merkle-ppt/assets/Merkle_icon.pptx) |
| Slide | 139 页内容页和其他版式参考 | [版式目录](libraries/slide-library.md) | [HTML](libraries/slide-offline.html) | [Slide PPT](merkle-ppt/assets/Slide%20Library%20for%20ai.pptx) |
| Case | 45 页短案例、扩展页和旗舰案例参考，含说明页 | [案例目录](libraries/case-library.md) | [HTML](libraries/case-offline.html) | [Case PPT](merkle-ppt/assets/case%20library%20-%20Case%20Study%20Layout%20Types.pptx) |
| Diagram | 15 页图示素材，重点覆盖技术架构、数据流和系统关系 | [图示目录](libraries/diagram-library.md) | [HTML](libraries/diagram-offline.html) | [Diagram PPT](merkle-ppt/assets/Diagram%20library%20-%20Diagram%20Elements.pptx) |
| QBR | 156 页业务回顾、阶段汇报和规划版式 | [QBR 目录](libraries/qbr-library.md) | [HTML](libraries/qbr-offline.html) | [QBR PPT](merkle-ppt/assets/QBR%20SLIDE%20LIBRARY.pptx) |

GitHub 可直接显示目录文字和预览图。交互式 HTML 需先下载，再用浏览器打开。[Slide](libraries/slide-object-styles.csv)、[Case](libraries/case-object-styles.csv) 和 [Diagram](libraries/diagram-object-styles.csv) 和 [QBR](libraries/qbr-object-styles.csv) 对象索引及[样式记录说明](merkle-ppt/references/source-object-styles.md)可用于定位具体对象。

### 私有仓库访问与安装

本仓库为私有仓库，只有获授权的 GitHub 账号才能查看或下载。仓库所有者可在 **Settings → Collaborators → Add people** 中邀请同事；对方接受邀请后，即可查看、下载或克隆仓库。

**权限说明：** 当前仓库属于个人账号。GitHub 对个人私有仓库的协作者提供读写权限；如果同事只需要读取权限，可考虑组织仓库的角色管理。安装前请确认 Codex 所在环境使用的 GitHub 凭据对仓库有访问权限。

在 Codex 中发送：

```text
请使用 $skill-installer 从 GitHub 安装这个 Skill：
仓库：veyziao/Merkle_PPT_skill
分支：main
Skill 路径：merkle-ppt
```

也可以登录 GitHub 下载仓库 ZIP，再将其中的 `merkle-ppt` 文件夹安装到 Codex 的 skills 目录；请让 Codex 根据当前环境完成安装。安装或更新后开启新对话使用。

### 使用示例

```text
请使用 $merkle-ppt，根据我上传的材料制作一份可编辑的 PowerPoint。
听众是项目管理层，语言为中文。重点说明项目背景、方案、
时间安排和下一步；区分已确认事实与建议。
```

### 更新已安装版本

仓库更新不会自动覆盖本地已安装副本。可在 Codex 中要求：

```text
请备份当前 merkle-ppt skill，并将它更新到
veyziao/Merkle_PPT_skill 的 main 分支最新版本。
```

如安装器提示同名 skill 已存在，先保留备份，再按当前环境的安装方式更新。更新后开启新对话。

## English

Merkle PPT Skill helps Codex create, edit and review editable PowerPoint presentations using an official template, layout references and brand assets. It brings together content planning, layout selection, icons and diagrams, source styling, and delivery checks for proposals, case studies, project updates and architecture presentations.

### Core capabilities

- **Build from the official template.** New decks start from the 2026 Merkle Arial template, retaining its slide master, theme and 35 named layouts. Choose a layout for the page's purpose and use its title area, margins and body starting position as the grid; use the custom layout when free placement is needed.
- **Choose layouts to fit the content.** Consult the Slide Library for comparisons, timelines, processes, evidence and other content relationships. Use the Case and Diagram libraries for relevant case narratives and architecture, and the QBR Library for business reviews and stage updates. Source pages provide design references; their business content should not be copied automatically.
- **Keep PowerPoint content editable.** Use native, groupable text boxes, shapes, connectors, tables and suitable charts. Keep continuous prose in one text box with automatic wrapping. Photos, brand artwork and source SVGs can remain separate image objects.
- **Trace visual styling to source objects.** The Slide, Case and Diagram libraries include object-level records for locating and inspecting colors, gradients, transparency, outlines, shadows, 3D, layers and inherited theme properties. Validate the actual result in the target PowerPoint environment; recorded properties alone do not establish an exact match.
- **Use the source icons.** The ICON Library contains 583 indexed icons with visual interpretations, possible scenarios and source locations. Use the original PPT object or embedded SVG; verify any alternative is visually identical before use.
- **Review both content and presentation.** The workflow calls for checking facts versus proposals, slide boundaries, overflow, font substitution, editability, brand elements and rendered output. Reference client names, figures and project descriptions are not automatically evidence for a new project.

Current user instructions, client templates and project requirements take precedence. The included design profile is a working interpretation of supplied materials, not an approved or necessarily current official brand manual.

### Default design rules

The default fonts are **Arial Regular** for English and **Microsoft YaHei Regular** for Chinese, with weight adjusted for hierarchy. General light-background content slides inherit the M mark at bottom left and the page number at bottom right. Add the centered dentsu mark only when explicitly requested. The closing slide retains the template's M mark and copyright line, with no additional text by default.

### Reference libraries

| Library | Coverage | Browse on GitHub | Download for offline search | Source PPT |
| --- | --- | --- | --- | --- |
| ICON | 583 indexed icons, with scenarios and source locations | [Icon catalog](libraries/icon-library.md) | [HTML](libraries/icon-offline.html) | [ICON PPT](merkle-ppt/assets/Merkle_icon.pptx) |
| Slide | 139 pages of content and other layout references | [Slide catalog](libraries/slide-library.md) | [HTML](libraries/slide-offline.html) | [Slide PPT](merkle-ppt/assets/Slide%20Library%20for%20ai.pptx) |
| Case | 45 pages covering short-form, extensions and flagship cases, including guidance pages | [Case catalog](libraries/case-library.md) | [HTML](libraries/case-offline.html) | [Case PPT](merkle-ppt/assets/case%20library%20-%20Case%20Study%20Layout%20Types.pptx) |
| Diagram | 15 pages focused on technical architecture, data flows and system relationships | [Diagram catalog](libraries/diagram-library.md) | [HTML](libraries/diagram-offline.html) | [Diagram PPT](merkle-ppt/assets/Diagram%20library%20-%20Diagram%20Elements.pptx) |
| QBR | 156 pages for business reviews, stage updates and planning | [QBR catalog](libraries/qbr-library.md) | [HTML](libraries/qbr-offline.html) | [QBR PPT](merkle-ppt/assets/QBR%20SLIDE%20LIBRARY.pptx) |

GitHub displays the catalogs and previews directly. Download the interactive HTML files and open them locally in a browser to search. Object indexes for [Slide](libraries/slide-object-styles.csv), [Case](libraries/case-object-styles.csv) and [Diagram](libraries/diagram-object-styles.csv) and [QBR](libraries/qbr-object-styles.csv), plus the [source-style guide](merkle-ppt/references/source-object-styles.md), help locate individual objects.

### Private access and installation

This repository is private: only authorized GitHub accounts can view or download it. The owner can invite colleagues via **Settings → Collaborators → Add people**. Once an invitation is accepted, the colleague can browse, download or clone the repository.

**Permissions:** This repository is owned by a personal account. GitHub collaborators on a personal private repository have read and write access; consider an organization-owned repository if read-only access is required. Before installation, ensure the GitHub credentials used by the Codex environment can access this repository.

Send Codex:

```text
Please use $skill-installer to install this skill from GitHub:
Repository: veyziao/Merkle_PPT_skill
Branch: main
Skill path: merkle-ppt
```

Alternatively, sign in to GitHub, download the repository ZIP and ask Codex to install the `merkle-ppt` folder into its skills directory for the current environment. Start a new conversation after installing or updating.

### Example request

```text
Use $merkle-ppt to create an editable PowerPoint from the materials I uploaded.
The audience is project leadership. Use English and cover the background,
proposed approach, timeline and next steps. Distinguish confirmed facts from proposals.
```

### Updating an installed copy

Repository updates do not automatically replace an installed local copy. Ask Codex:

```text
Back up my existing merkle-ppt skill and update it to the latest version
on the main branch of veyziao/Merkle_PPT_skill.
```

If the installer reports an existing skill with the same name, retain a backup and update it using the method appropriate to the current environment. Start a new conversation afterwards.

## Repository

- [Skill instructions](merkle-ppt/SKILL.md)
- [Official layout guide](merkle-ppt/references/official-layouts.md)
- [Layout selection guidance](merkle-ppt/references/pattern-selection.md)
- [Delivery review checks](merkle-ppt/references/review-gates.md)

