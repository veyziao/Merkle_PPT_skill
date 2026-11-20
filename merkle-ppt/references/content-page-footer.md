# General content-page footer: user-provided geometry

The user is specifying the footer treatment for **general content slides**. Do not apply this rule to cover, agenda, or section-divider slides. The screenshots show a white/light widescreen (16:9) slide master. PowerPoint Page Setup shows **33.87 × 19.05 cm**; the source PPTX stores approximately **33.867 × 19.05 cm**. Dimensions below are PowerPoint **object bounding boxes**, measured from the slide's top-left, not the visible ink bounds. Use the matching master/layout element when it is present; avoid a duplicate footer. Additional footer variants may follow from the user.

| Element | Supplied asset | X | Y | Width | Height | Rotation | Placement evidence |
|---|---|---:|---:|---:|---:|---:|---|
| M avatar, light background | [M_avatar.png](../assets/footer/M_avatar.png) | 1.16 cm | 18.03 cm | 0.69 cm | 0.38 cm | 0° | [PowerPoint screenshot](../assets/examples/footer/light-content-m-avatar-geometry.png) |
| Center `a dentsu company` mark | [dentsu.svg](../assets/footer/dentsu.svg) | 15.43 cm | 18.13 cm | 3.00 cm | 0.35 cm | 0° | [PowerPoint screenshot](../assets/examples/footer/light-content-dentsu-geometry.png) |
| Right-side page-number text box | Native `slidenum` field | 21.66 cm | 17.57 cm | 11.27 cm | 0.85 cm | 0° | [PowerPoint screenshot](../assets/examples/footer/light-content-page-number-geometry.png) |

The dentsu mark is centered horizontally: `15.43 + 3.00 / 2 ≈ 33.867 / 2` cm. The two image screenshots show **Lock aspect ratio** enabled. The supplied `M_avatar.png` is a 20 × 11 px transparent PNG. The supplied `dentsu.svg` declares 115 × 16 intrinsic units, whose aspect ratio differs from the PowerPoint object's displayed bounding box; preserve the asset's proportions and check the rendered appearance when placing it in the target box. Do not stretch the logo simply to force both numbers.

The page-number **box** is wide, but the visible number sits at its far right. Its position is therefore not the position of the visible numeral. The inspected Arial template master uses a native `slidenum` field in a right-aligned, bottom-anchored text box, with 7 pt regular theme text in a subdued gray. Preserve a live page-number field where the authoring tool supports it; do not type a fixed example number. The field geometry matches the user's screenshot. [Slide-size screenshot](../assets/examples/footer/slide-size-16x9.png).

The earlier phrase “bottom-right M logo” conflicts with the supplied screenshot, which places the **M avatar at bottom-left**. Treat the screenshot and the user's subsequent location wording as the precise rule. The small mark at bottom-right is the page number.
