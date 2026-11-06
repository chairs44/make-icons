---
name: make-icons
description: Create or refine custom SVG icons and cohesive icon sets, including reference-based symbols, export files, and visual specimens.
---

# Make Icons

Draw original, editable vector icons with open contours, balanced proportions, restrained rounding, and clear negative space. The default family is **outline, 24-unit grid, 1.5-unit stroke**. Personality comes from the subject's silhouette and curve handling, not forced squat proportions or decorative irregularity.

## Establish the request

Use the icon inventory, meaning, references, target context, output formats, and sizes already supplied. A single icon is a complete request. Reference images, SVGs, or a folder can define the subjects when their intended mapping is clear; inspect them before drawing. Ask one focused question only when a missing subject, ambiguous meaning, or target-specific constraint materially changes the result. Do not require a form or repeat answered questions.

Explicit user instructions and an established project's approved icon system override these defaults. Preserve requested file formats, dimensions, and naming conventions. Creating icons does not by itself authorize website integration, dependency installation, publishing, or updating this skill's permanent anchors.

## Use the specification and references

- Before creating a new family or resolving construction/export decisions, read [references/master-prompt.md](references/master-prompt.md). It is the complete, self-contained design and delivery contract. Its input block is a template for people using the prompt directly, not a mandatory intake form for skill users.
- Read [references/construction.md](references/construction.md) before drawing: it defines proportion and corner roles, structural versus organic curves, attached parts, crossings, modifiers, painted-edge clearance, and reference comparison.
- Read [references/anchors.md](references/anchors.md) before using bundled examples. The ten examples demonstrate structural, organic, and intersecting contours. Supplied references and current construction rules take precedence. Inspect their geometry and rendered behavior before adapting them; they are examples, not a mandatory inventory.
- Read the compact-size and typography sections of the master prompt when working at 16/20 native units or with letters/numerals. Read its export section for framework components, expanded paths, or raster requests.
- For a reusable prompt request, return the master prompt with **all editable inputs at the beginning**. It must work without this skill, bundled scripts, a specific design application, or private project context.

## Construct the family

Use the same stroke weight and terminal policy across related symbols. Start broad container corners around 2 units, but preserve natural circles, organic Bézier contours, directional points, and smaller structural transitions. Measure visible bounds including stroke extents. Match apparent size, not identical bounding boxes. Measure openings between painted edges, not just centerlines. Plan which contour owns each shared edge; stop hidden contours at attachments. Round caps do not correct doubled lines or poor curve tangents.

Favor long clean structural edges with short controlled corner transitions; preserve directional points and generous interiors. Distinguish continuous contours, attached details, occluded crossings, and detached modifiers. Organic forms use broad flowing curves with deliberate taper, not assemblies of rounded boxes. Carry these decisions across subjects without forcing one silhouette, orientation, or topology onto the whole family.

Keep `currentColor`, transparent negative space, and scalable SVG geometry. Use path/shape data rather than a raster substitute. Treat an expanded outline and a visually solid variant as different things. Preserve reference identity; do not replace a distinctive supplied mark with a generic symbol without explaining what would be lost.

Use real font outlines for fixed letters and numerals. Reserve label space before placing surrounding rings or arrowheads; center on the intended container, then review the complete symbol. Mirror directional geometry without mirroring text. Use the family’s chosen weight for control rings; do not thicken them independently.

A small request can go directly to finished icons. For a broad or uncertain family, establish a representative structural, directional, and organic subset internally, then complete the requested set. Stop for design approval only if the user requested that checkpoint or a material unresolved choice requires it.

## Deliver the requested scope

For ordinary file generation, default to:

- Standalone `svg/24/<name>-outline.svg` files with a `0 0 24 24` viewBox and `24 × 24` default dimensions.
- `preview.html` with 16/20/24/32px display samples, 72px details, both polarities, and text pairing.
- `README.md` and `manifest.json` identifying files, native grids, variants, practical size limits, and checks actually performed.
- `icons.zip` for a multi-icon delivery when file tools are available; omit for a single icon unless requested.

Requested components are additional unless the user asks for components only. Optional exports include React, Vue, SolidJS, React Native, Astro, expanded SVG, and PNG. Compact 16/20-unit masters are a separate design choice from displaying a 24-unit SVG at those sizes. The master prompt defines exact extensions, folders, and limitations.

Default sensibly when no export format is specified. Offer one concise format/size choice when the target is unclear and the choice changes the work, or when the user asks to choose exports. Never treat blank optional fields as blocking. A Paper-only, SVG-only, text-free, prompt-only, or narrowly scoped edit request overrides the normal package. For Paper, use editable vectors and inspect the resulting frame; do not force an HTML package into a canvas-only task.

## Reusable helpers

- [scripts/geometry.py](scripts/geometry.py): build-time circular polygon corners. Use only when exact circular corners fit the shape. It does not round arbitrary organic contours or decide optical balance.
- [scripts/specimen.py](scripts/specimen.py): standard-library SVG parsing, recursive specimens, optional manifest generation, and ZIP assembly. Run `--help` for its interface. It does not generate artwork, convert strokes, produce framework components, or certify visual quality. Include only intended deliverables in archives.

`assets/outline-24/` contains the ten editable construction examples described in [references/anchors.md](references/anchors.md). These match the downloadable samples.

## Verify and finish

Parse new SVGs and check requested inventory, native grids, bounds, consistent weight, and transparent holes. Render at the actual intended sizes when available, inspect light and dark contexts, and compare related states in fixed containers. Correct recognition, crowding, contour, or layout faults before delivery. For components or interactions, run checks appropriate to that target; static artwork does not require an interaction test suite.

The helper's parser proves only its documented structural checks. Do not equate parse success with correct path rendering, accessible integration, optical tuning, or user approval. Record unperformed checks honestly. Rebuild affected previews and archives after corrections. Reuse valid checks for unchanged work and finish once the requested files and proportionate review are complete.
