---
name: merkle-ppt
description: Create, edit, or review Merkle-style PowerPoint decks using the supplied brand assets, Arial template, and evidence-based design system. Use for Merkle presentations; do not apply to unrelated brands.
---

# Merkle PPT

Use this skill when the user asks for a Merkle presentation, a Merkle-style redesign, or a review of a Merkle deck. Start from the audience and message, then choose the visual form that makes the content easiest to understand. The reference pages are examples of design decisions, not pages to copy.

## Source priority

1. Follow the current user's instructions and project-specific requirements, including supplied client templates and confidentiality rules.
2. Use the official Merkle assets and the applicable brand guide. The bundled research is a **working design profile**, not an approved or necessarily current brand manual. Check version differences when they materially affect the deliverable.
3. Use the research references to interpret recurring design methods. Treat historical slide content, data, and layouts as examples only.

The user explicitly set **English: Arial Regular** and **Chinese: 微软雅黑 Regular** as defaults. This overrides Proxima declarations in older files and in the 2025 guide for this workflow. Use other weights only when hierarchy needs them. Preserve supplied SVG logos exactly; their colors differ from the 2025 guide's palette and must not be recolored to conceal that difference.

## Create or revise a deck

1. Establish the audience, purpose, language, delivery mode, expected length, mandatory content, sources, and the decision or action the deck should support. Infer routine details from supplied material; ask only for information that materially changes the result. Separate verified facts, assumptions, and proposals.
2. Organize the story before designing pages. For a substantial new deck, make a page outline with each page's task, key point, supporting evidence, and likely visual form. If the user asks to proceed directly, continue without a separate approval step.
3. Choose a layout by the information relationship and page purpose. Use [pattern-selection.md](references/pattern-selection.md) to route business reviews to QBR, case stories to Case, technical systems to Diagram, and general content to Slide; compare relevant candidates across libraries whenever useful. Expand related Chinese and English terms, inspect the original pages and their usage notes, and adapt the structure to the actual content. The four earlier DEMO examples are options, not an exhaustive set. Vary composition and density while keeping the deck coherent.
4. For a new Merkle deck, copy the [official 2026 Arial template](assets/2026%20Merkle%20PPT%20Template%20-%20ARIAL.pptx) and remove its 40 example slides from the working copy. Keep its slide master, 35 named layouts, theme, and associated assets. Select a named layout using the [official layout and placeholder guide](references/official-layouts.md). Use its composition, margins, spacing, and body starting position as the page grid, applying the user's title position and typography rules where they differ. Fill appropriate native placeholders and add editable elements suited to the content. Apply the user's [preferred content compositions](references/user-curated-layouts.md) where they fit, using the template's `自定义版式` for compositions requiring free placement. Keep each slide linked to its layout.
5. Apply the brand rules in [brand-profile.md](references/brand-profile.md). Set up the [footer](references/content-page-footer.md) on the master or the relevant layouts so general light-background content slides inherit the lower-left M avatar and live lower-right page number. Include the centered dentsu logo only when the user explicitly asks for it. Use the template's own treatments for cover, agenda, and section-divider slides. Use photos, prism artwork, and icons for a clear communication purpose. Keep reference business text, customer names, figures, diagrams, and screenshots out of the new project's content.
6. Render and inspect every slide after authoring. Check content, native editability, overflow, font substitution, contrast, logo clear space, chart labels, sources, and cross-slide rhythm using [review-gates.md](references/review-gates.md). Verify in the target PowerPoint environment when possible; distinguish converter artifacts from source defects. Deliver the requested editable format and state any material limits that remain.

For Agenda slides, use the bundled [Agenda artwork](assets/agenda-right-artwork.png) as the default right-side graphic. Follow the placement in the [Agenda layout reference](references/user-curated-layouts.md#2-agenda--ao4).

For the Closing slide, keep the template's M mark, background, and copyright line. Add text to the page only when the user explicitly requests it.

For content slides, use the [title and body typography defaults](references/brand-profile.md#visual-identity-and-type). Align ordinary content-page titles consistently across sources and layouts; apply the approved size and fonts to special content layouts as well, while preserving their composition-dependent title position. Follow explicit instructions for a narrow edit.

For QBRs, business reviews, project updates, stage reviews, performance analysis, planning and other suitable reports, also consult the [QBR slide library](references/qbr-slide-library-usage.md). Its examples can be used outside quarterly reviews when the content relationship fits; compare it with the general slide library.

Use native PowerPoint text boxes, shapes, connectors and tables that can be edited and grouped. Keep each prose passage in a single text box with automatic wrapping. Choose icons using the supplied [icon library and semantic index](references/icon-usage.md), and use its original SVG graphics when appropriate.

For system architecture, data flows, ownership boundaries and platform diagrams, consult the [diagram library](references/diagram-library-usage.md) and select both suitable components and an overall composition. Preserve the actual meaning of zones, nodes and connections; adapt and simplify source examples to the current content and audience.

For specific Slide Library, Case Library, Diagram Library and QBR Library examples, consult the [object-level source style records](references/source-object-styles.md) and original slide. Inspect actual fills, gradients, transparency, outlines, shadows, 3D, images, geometry, and grouping—including inherited theme formatting—and preserve meaningful differences. Verify the finished slide visually in PowerPoint; do not claim an exact match merely because the properties were recorded.

For a narrow edit, preserve unrelated wording, order, slide count, objects, and formatting unless the user asks for a broader redesign. For a review-only request, inspect and report without creating a new deck.

Use the available presentation authoring and rendering tools for the actual file work. This skill supplies Merkle-specific design decisions; it does not replace the relevant tool's file-format workflow.

