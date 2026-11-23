# General content-page footer: user-provided geometry

This footer applies to **general light-background content layouts**. Cover, agenda, and section-divider layouts use their own template treatments. PowerPoint Page Setup shows **33.87 × 19.05 cm**. The source PPTX stores approximately **33.867 × 19.05 cm**. Dimensions below are PowerPoint object bounds measured from the slide's top-left corner.

| Element | Supplied asset | X | Y | Width | Height | Rotation | Placement evidence |
|---|---|---:|---:|---:|---:|---:|---|
| M avatar, light background | [Merkle_M_logo_black.svg](../assets/Merkle_M_logo_black.svg) | 1.16 cm | 18.03 cm | 0.69 cm | 0.38 cm | 0° | [PowerPoint screenshot](../assets/examples/footer/light-content-m-avatar-geometry.png) |
| Optional center `a dentsu company` mark | [dentsu.svg](../assets/footer/dentsu.svg) | 15.43 cm | 18.13 cm | 3.00 cm | 0.35 cm | 0° | [PowerPoint screenshot](../assets/examples/footer/light-content-dentsu-geometry.png) |
| Right-side page-number text box | Native `slidenum` field | 21.66 cm | 17.57 cm | 11.27 cm | 0.85 cm | 0° | [PowerPoint screenshot](../assets/examples/footer/light-content-page-number-geometry.png) |

The official 2026 Arial template already supplies an M mark and native slide number through its master or individual layouts. In the working copy, replace the M used on the applicable light content layouts with the original `Merkle_M_logo_black.svg`, fitted proportionally within the existing box. Preserve the slide-number field. Check the combined master and layout rendering for duplicate marks or numbers.

The bundled template's master contains two overlapping `slidenum` text shapes, IDs 6 and 9, with the same bounds and field formatting. In a **working copy**, first verify that they are still duplicates, then remove only one of the duplicate shapes and retain the other live field; do not alter the original template. Inspect master, layout and slide-level objects for any other duplicates rather than deleting them by ID. Confirm the number appears once and changes with slide order in the target PowerPoint environment. The duplicate was confirmed structurally; any visible effect must be checked in the renderer. If the authoring tool cannot preserve a live field, report the limitation instead of silently typing a static page number.

The default content footer has the M avatar and slide number. Include the centered dentsu mark only when the user explicitly requests it. For that deck, add the supplied `dentsu.svg` to the applicable light content layouts in the working copy, or use the master if its visibility is limited to those layouts. Preserve its proportions within the target box and let the selected layouts pass it down to their slides.

The page-number **box** is wide, but the visible number sits at its far right. Its position is therefore not the position of the visible numeral. The inspected Arial template master uses a native `slidenum` field in a right-aligned, bottom-anchored text box, with 7 pt regular theme text in a subdued gray. Preserve a live page-number field where the authoring tool supports it; do not type a fixed example number. The field geometry matches the user's screenshot. [Slide-size screenshot](../assets/examples/footer/slide-size-16x9.png).

