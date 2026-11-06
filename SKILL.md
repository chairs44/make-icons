---
name: make-icons
description: Create or refine cohesive custom SVG icon sets with compact solid silhouettes, engineered soft corners, optional outline companions, and rendered specimens. Use for icon design, reference simplification into icons, or reusable icon-generation prompts.
---

# Make Icons

Create editable vector icons with a coherent drawing system. Default to compact, slightly squat solid silhouettes, controlled circular corners, short extensions, clear cutouts, and monochrome `currentColor`. Optional outlines share the same character. Soft edges must not become inflated or cartoon-like.

## Start from the request

Use the icon list, variants, references, framework, and interaction scope already supplied. Ask only for missing information that changes the result, especially an absent icon inventory or ambiguous symbol meaning. Do not repeat an intake form when the conversation already answers it.

Read [references/master-prompt.md](references/master-prompt.md) for the complete reusable prompt, specifications, construction examples, and delivery contract. It is also the source to adapt when the user requests a copyable generic prompt. All user-editable inputs belong at its beginning.

## Apply the system with judgment

- The reference defines **defaults**, not an override of explicit user instructions or an established project's icon system. Preserve requested sizes, formats, and local conventions. State material departures briefly.
- Keep the 24-unit grid and 1.75-unit outline consistent within the default family. Change family-wide tokens deliberately if asked; do not quietly vary weights icon by icon.
- Exact circular corners use arc commands or rounded rectangles. Bézier curves remain appropriate for deliberately organic contours. Optical balance outranks identical bounding boxes.
- For text-bearing icons, follow the master prompt’s typography section: real font outlines, shared weight/scale, and no hand-improvised digits. Design the container, arrowhead, and protected label space together; center on the container, then inspect the whole symbol. A passing bounding-box check alone is not visual approval.
- Simple controls and detailed emblems need different simplification decisions. A reference-based mark may need a larger practical minimum size. Disclose identity lost through simplification rather than forcing every motif into the same detail budget.
- Use native SVG/code for editable vector deliverables. Do not substitute raster mockups for finished SVGs.
- For a small request, draw and show the requested icons. For a large or uncertain set, start with representative structural, directional, and reference-based symbols before expanding. Do not add an approval gate to work already authorized; present genuine visual choices when they matter.
- A specimen is the default for a new family. A focused edit may reuse the existing specimen and verify only affected icons. Do not turn every minor adjustment into a full design process.
- Components, motion, production integration, publishing, and installation are separate scopes. Generate only what was requested. A request to make icons does not authorize replacing project UI or installing dependencies.

## Reusable resources

- `assets/anchors/`: eight generic SVGs: home/play/pause solid and outline, plus approved back-15/forward-30 solid controls. The numeral pair demonstrates top-tangent arrowheads and protected interior spacing. Useful starting geometry, not a universal inventory. No personal marks or source photographs are bundled.
- [scripts/geometry.py](scripts/geometry.py): standard-library Python helper for exact circular polygon corners. Import `rounded_polygon`, or pass `--points '[[7,5],[19,12],[7,19]]' --radius .75` to print path data. This is build-time generation; delivered icons must render without it.
- [scripts/specimen.py](scripts/specimen.py): creates a self-contained comparison HTML file from an SVG directory and optionally a ZIP. Shows 16/20/24/32px plus a 72px inspection view, light/dark contexts, and inline text. It validates basic SVG structure but does not claim visual QA. Run `--help` for options. Custom interaction examples should be added only when requested.

## Finish proportionately

Parse SVGs, render them when possible, inspect actual small-size appearance, and compare related states in fixed containers. Check desktop/mobile specimen overflow; test keyboard, rapid reversal, and reduced motion only when interactions are present. Existing verified geometry can be reused, but new combinations still need an optical check. For enclosed text, measure the label center and head-to-label clearance, account for stroke extents, and inspect both polarities. If the user identifies crowding, reconsider the composition rather than repeating a centering calculation. Refresh packaged assets and showcase images after changes so they match the SVGs.

Deliver working file links and a concise inventory. Distinguish structural checks, rendered checks, user approval, and production use. Do not claim unperformed checks or treat every newly generated icon as a permanent approved anchor.
