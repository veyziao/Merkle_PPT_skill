# Merkle presentation icon selection

Use the supplied [icon library](../assets/Merkle_icon.pptx) and [icon index](merkle-icon-index.json) to select icons by meaning and context. The index records each original slide number, shape ID, page position and SVG media reference. The source PPT remains the authority for appearance and intended use.

## Source and sizing

- **Medium** icons are the Merkle-specific branded icon set in source slides 6–22. Each image has a light-background and a dark-background variant. The index groups each pair as one icon. The original PPT recommends approximately **0.65 in** for medium icons.
- **Mini Fill** icons are the selected filled icons in source slides 24–33. The source PPT identifies these as coming from Phosphor. Its sizing example gives **0.25 in maximum** for mini icons. Treat them as the supplied third-party icons, with their own source attribution.
- The original presentation reserves the Merkle-specific set for Merkle-branded sales, thought leadership and internal communication. It says not to recolor those icons to match client branding. For a client-branded deliverable, follow the source presentation's client-use guidance and the applicable project requirements.

## Select and use

1. Describe the specific concept and the content's relationship. Search the index by Chinese scenario, English Phosphor name and tags, or source category. Start with an icon from the supplied library. Prefer the relevant Medium icon for a Merkle-branded concept when it fits the required size and context.
2. Inspect the actual vector image and its surrounding page in the source PPT before selecting it. Individual Medium names and scenarios are human visual interpretations. Mini Fill names are candidates matched against the Phosphor Core 2.1.1 catalog by comparing 32 × 32 rasterized silhouettes; a match does not prove the original name or vector geometry is identical. The index includes Phosphor's English tags and Chinese search suggestions. These matches are visual identification aids, and an icon's potential meanings depend on its context.
3. Use the original icon object or its original embedded SVG content from the indexed source slide. Keep it vector where the target PowerPoint environment supports SVG, and preserve the original colors, silhouette and proportions. Use the matching light or dark variant. Keep icons as separate objects that can be grouped with native PowerPoint text and shapes. Another version is acceptable only after verifying it is identical in appearance to the corresponding source; prefer a byte-identical source SVG, checked against the recorded SHA-256.
4. If no supplied icon fits, do not substitute a visually similar or generated icon as though it were an original. Ask the user before introducing a different or newly generated icon; in the meantime, continue with other content and omit it if a design can work without it.

## Index fields

- `id` is a stable locator in the form `P06-01`, counting the icons left to right and then top to bottom within the original page. Medium counts the light-background row only.
- `slide`, `shape_id`, `shape_name`, `x`, `y`, and `svg` locate the original SVG object. `dark_shape_id` and `dark_svg` identify the corresponding Medium variant.
- `svg_sha256` and, where applicable, `dark_svg_sha256` identify the exact SVG bytes extracted from the source PPTX; the source slide shape's SVG relationship was checked against each indexed asset.
- `confidence` describes the naming or visual interpretation method, not verification of the SVG file. Source-SVG identity is established separately by its PPT relationship and checksum.
- `name_zh` is the visual label written for Medium. `official_name` and `english_tags` are Phosphor catalog matches for Mini Fill.
- `scenario` contains potential Chinese search terms and uses. A metaphorical use is a suggestion, not evidence for a business claim.

## Cross-topic examples

| Topic | Medium examples | Mini Fill examples |
| --- | --- | --- |
| AI, intelligent analysis | P06-01–P06-04 | P28-03 circuitry, P28-04 cpu, P28-05 head-circuit |
| Customer, audience, support | P10-01–P10-12, P11-09, P12-02–P12-07 | `users`, `user-focus`, `user-check`, `identification-card` |
| Search and discovery | P07-03, P11-09, P13-07 | `gps`, `crosshair`, `binoculars` |
| Growth and business performance | P08-12, P13-02, P19-01, P19-06 | `trend-up`, `chart-bar`, `chart-line-up` |
| Collaboration and communication | P07-06, P09-09, P11-06–P11-07 | `handshake`, `users-three`, `hand-waving` |
| Environment and sustainability | P15-01–P15-08, P16-01–P16-12 | `leaf`, `recycle`, `solar-panel`, `tree` |
| Finance and investment | P18-01–P18-12, P19-03–P19-11, P20-04 | `piggy-bank`, `bank`, `credit-card`, `wallet` |
| Location and travel | P21-01–P21-11, P22-01–P22-10 | `map-pin`, `compass`, `airplane`, `train` |
