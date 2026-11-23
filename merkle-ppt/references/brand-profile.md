# Merkle presentation working profile

This profile distills the supplied 2025 brand guide, 2026 assets, nine reference decks, QBR template, and official layout library. It guides work on this user's Merkle decks. It is not a claim that every historical treatment is a current official rule. The source research remains in the user's `PPT_SKILL` workspace (`design.md`, `design-patterns.md`, `design-review.md`, `reference-gallery/`).

## Visual identity and type

- Modern, clear, credible, and human. Deep blue or black pages create emphasis and transitions; light pages support explanation and data. Change density and composition with the story.
- English default **Arial Regular**; Chinese default **微软雅黑 Regular**. These are explicit user decisions, even where a source's theme declares Proxima Nova. Use bold or larger type selectively for hierarchy. Check mixed-language wrapping in the final PowerPoint environment.
- **Content-slide titles:** use bold **24 pt**, English **Arial** and Chinese **微软雅黑**. On ordinary light-background content pages use black (`#000000`), and anchor the title box **1.48 cm from the left and 1.27 cm from the top** of the slide. Align equivalent titles across the whole deck, even when content comes from different libraries. If a title wraps, grow its box or adjust nearby content to avoid overlap while preserving the anchor.
- **Special content layouts**, such as dedicated left/right split or dark sidebar layouts, may place the title differently to suit the composition; retain the same 24 pt and language-specific fonts. Use a contrasting color when a dark background requires it. Covers, section dividers and closing slides retain their own template treatments unless the user asks otherwise. A narrow body-only revision should not alter existing titles unless the user requests it.
- Default content-slide sizes in PowerPoint points (pt): **16 pt for body headings**, **14 pt for headings in compact groups**, and **12 pt for detail text**. Apply across body paragraphs, bullets, and explanatory text in cards or columns. Keep other labels legible for their purpose.
- After setting the sizes, align corresponding rows across columns and leave visible gaps between groups. Adjust text box widths and spacing to suit the copy. When a page is still dense, simplify the content or split the page.
- Prefer direct, informative titles. Use a conclusion title when evidence warrants it; otherwise name the topic. Keep the main point visually first.

## Color and background

- The 2025 guide lists Merkle Blue `#040E4B`, Merkle Red `#DD3039`, white `#FFFFFF`, and black `#000000`. **The guide's primary-color page is marked DRAFT.** Confirm version when exact current-brand compliance matters.
- Secondary blues: `#041677`, `#031FA4`, `#0328D1`, `#0391F2`; secondary reds: `#A72532`, `#711A2B`; neutrals include `#60607D`, `#8888A1`, `#AEAEBC`, `#D6D6DF`, `#E5E5E9`, `#F2F2F4`.
- Use blue and gray for most structures and charts; reserve red for small, deliberate emphasis. Do not use Merkle Red or Cobalt as broad backgrounds, red text on blue backgrounds or the reverse, red-blue gradients, or blue/red body copy. The guide's illustrative 80/15/5 color ratio is not a fixed per-slide formula.
- The supplied SVG logos use dark blue `#12295D` and red-orange `#F23A1D`; these differ from the 2025 guide's stated primary colors. Use each original SVG unchanged. Select a suitable light/dark variant; do not reconstruct the mark with theme colors.

## Logo and brand art

- Prefer the full wordmark for brand identification. Use the standalone M mark when that role is appropriate, not as a replacement for the full identity. Light background: dark wordmark; dark background: white wordmark. `Merkle_logo_black.svg` is actually the white wordmark variant; inspect the graphic rather than relying on its filename.
- The 2025 guide defines clear space around the mark from twice the triangle dimensions, a 75 px minimum for the digital full logo, and a 16 px minimum for the M mark. Do not distort, tilt, add outlines/shadows, or change component relationships.
- Prism art: use the correct light/dark asset and crop it intentionally. Use one prism type in a composition and keep it within two quadrants. Do not layer prism or macro artwork on photos, and do not pair photos with prism macro artwork in the same composition. These rules come from the 2025 guide's pages 44–47, 51, and 67.
- Use the supplied [icon library and semantic index](icon-usage.md) to select visuals by meaning. It contains Merkle-specific Medium icons and selected Phosphor Mini Fill icons, with separate guidance for use and size. Keep Merkle-specific icon colors intact.

## Layout and imagery

- The reviewed decks and full Arial template are 16:9. Start ordinary content pages with about 0.5–0.8 in safe margins, then adapt to the actual master and content; this is a working range, not an official grid measurement.
- Use shared baselines, considered grouping, and visible white space. One primary focal point per slide is a useful default. Image bleed is possible, while text and logos stay in a safe area.
- For photos, favor natural human activity, diverse people, authentic work and product context, simple compositions, and a warm tone. Keep room for copy through cropping or a suitable image. Avoid stock imagery presented as Merkle culture or client evidence.
- Apply this default outer shadow as a native PowerPoint picture effect on ordinary new flat content images, including overlapping screenshots and sample deliverables. Use black (`#000000`), 78% transparency (22% opacity), 93% size, 62 pt blur, 90° angle, and 16 pt distance. Explicit user directions and a specific source effect selected for faithful reproduction take precedence; the 3D stack below has its own settings. [User-supplied PowerPoint settings](../assets/examples/picture-shadow-settings.png)
- Use native PowerPoint objects for ordinary text, grids, diagrams, processes, tables, and basic charts. Photos, approved brand art, and complex textures can be image assets. Make meaningful data labels and relationships inspectable and editable.

### Optional gradient divider for two content blocks

- The page-level gradient divider is optional: use at most one per slide, to separate exactly two major content regions. Ordinary thin rules within one region are separate from this page-level divider.
- **Horizontal:** use primarily for layouts intentionally dividing top and bottom regions. On a regular content layout give this treatment low priority and generally omit it; consider it only when it materially improves the composition. Use a thin editable full-width rectangle (reference height approximately 0.50 cm), 90° linear gradient, no outline, no shadow, and **Rotate with shape** enabled. Use two stops: at **21%**, theme `tx2` (reference base `#5F607C`), brightness **+60%**, transparency **100%**; at **100%**, theme `bg2` (reference base `#E7E6E6`), brightness **−10%**, transparency **36%**. See slide 68 of `B2B Sales Transformation - Offering-v1.0.pptx`. [PowerPoint divider settings](../assets/examples/two-block-divider-settings.png)
- **Vertical:** use only in a dedicated left/right composition like the supplied example: a full-height strip between a narrower left introduction and a wider right detail region, not as decoration on an ordinary title-and-body page. Use an editable rectangle with **0° linear gradient**, no outline and no shadow: white (`#FFFFFF`) at 0%, transparency **100%**, and black (`#000000`) at 100%, transparency **90%**; brightness **0%**, and rotate with shape. Source slide 60 of `B2B Sales Transformation - Offering-v1.0.pptx` provides this native shape (approximately 0.98 cm wide and full slide height). [Vertical application example](../assets/examples/two-block-divider-vertical.png)
- These horizontal and vertical gradients have distinct parameters; do not create the vertical treatment by simply rotating the horizontal one. Preserve the source object where feasible and check the result in PowerPoint.

### Optional 3D stack for illustrative pictures

- Use this treatment when screenshots, mockups, or sample deliverables serve as a visual preview. Rotate the pictures to a common angle and offset them vertically so each layer is visible. Present any figures, labels, or interface details the audience needs to read in flat, legible form.
- For the demonstrated look, use native PowerPoint 3D rotation with X **300°**, Y **324.6°**, Z **60.2°**, and height from bottom **0 pt**. The reference's black outer shadow uses **72% transparency** (28% opacity), **100% size**, **22 pt blur**, **135° angle**, and **3 pt distance**. This stack has its own shadow settings. [PowerPoint reference from CRM-Messaging, slide 37](../assets/examples/layered-3d-picture-settings.png)

### White text panels with a gray outline

- For the user's latest demonstrated white panel, use an editable shape with solid white (`#FFFFFF`) fill at 0% transparency and a solid light-gray 0.5 pt outline at 0% transparency, flat cap and round join. The latest screenshot does not expose the exact outline color value; inspect the source before claiming an exact match. [Fill and outline](../assets/examples/white-panel-fill-outline-2026.png)
- Its native black (`#000000`) outer shadow uses **80% transparency** (20% opacity), **88% size**, **61 pt blur**, **90° angle**, and **26 pt distance**. Do not replace its editable shadow with a rasterized approximation. [Shadow settings](../assets/examples/white-panel-shadow-2026.png)
- An earlier source example in `CRM-Messaging_Offering_v1.4.pptx`, slide 34, has a distinct treatment: `#E7E6E6` 1 pt outline, black shadow at 93% transparency, 100% size, 21 pt blur, 90° and 16 pt distance. Preserve that combination when reproducing that specific source. [Earlier panel reference](../assets/examples/white-text-panel-shadow.png)
- Use this panel to group related information such as investment, timing, and outcomes. When a divider helps distinguish those sections, the slide 34 example uses a separate editable 0.75 pt dashed line in the outline theme color darkened to 90% luminance.

## Handling conflicts

- Historical offering decks use a navy/faceted language; Brand Promise and 2026 Credentials use black/electric-blue light. Both are observed branches. Pick according to audience, story, and applicable template rather than declaring one universally current.
- Templates and source decks include old colors, Proxima themes, small type, repeated layouts, placeholder content, and possible converter artifacts. Treat these as evidence to interpret, not rules to inherit.
- If a project has a newer official guide or client-specific template, inspect it and follow the user's project choice. Record a material departure from this working profile only when it affects brand compliance or usability.

