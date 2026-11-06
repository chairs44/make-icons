# YOUR INPUTS

Replace the fields you need. Leave optional fields blank to use their defaults. Existing instructions in this conversation also count as input.

**Required**
- **Icons or subjects:** [List the icons to create. Explain unusual meanings, or identify subjects in attached references.]

**Optional**
- **Use/context:** [For example: website navigation, audio player, dense desktop sidebar, mobile app, printed diagram.]
- **References:** [Attach images/SVGs or provide accessible paths/URLs. Identify which reference belongs to which icon.]
- **Existing family to match:** [Attach approved icons or describe the established system. Default: the drawing system below.]
- **Visual variants:** [outline / solid / both. Default: outline.]
- **Export formats:** [SVG / React / Vue / SolidJS / React Native / Astro / expanded SVG / PNG. Default: SVG. Multiple choices allowed. Write “help me choose” if useful.]
- **Native drawing sizes:** [24 / compact 16 / compact 20 / a combination / custom. Default: 24.]
- **Intended display sizes:** [Default review: 16, 20, 24, 32px, plus a 72px detail view.]
- **Delivery scope and destination:** [Files, code in chat, Paper/canvas study, or a narrower scope such as “SVG only”; output folder if relevant. Default: the file package below when file tools are available.]
- **Color/background:** [Default: currentColor and transparency. For PNG, specify foreground color, pixel sizes, and 1×/2× density; defaults if PNG is selected: black, 24px at 1×, transparent.]
- **Letters/numerals:** [Exact labels and preferred typeface if relevant. Default: a suitable available, licensed sans-serif converted to vector outlines.]
- **Interaction examples:** [State pairs or behavior to demonstrate. Default: none; no animation.]
- **Other constraints:** [Naming, minimum sizes, accessibility context, RTL behavior, preserved geometry, or project-specific overrides.]

---

# TASK

Create the requested icons as a cohesive set of original, editable vectors. Complete the requested inventory and exports, not merely a plan. A single icon is a valid set. The example SVGs below are construction references, not additional requested icons.

Use information already supplied. If the subjects are missing or genuinely ambiguous, ask one focused question before drawing. Otherwise use defaults and proceed. If export selection materially depends on an unknown target, ask one concise bundled question with SVG as the default. Do not make users answer optional fields unnecessarily.

Explicit instructions and an established approved family take precedence over defaults. Explain material departures briefly. Do not modify an application, install dependencies, publish assets, or expand the icon inventory unless that work is requested. Do not require any particular skill, paid icon library, design application, or private file for this prompt to work.

# DRAWING CHARACTER

Precise, open, gently softened, and quietly distinctive. Keep the symbol immediately recognizable. Give each subject its natural proportions: a book may be tall, a cap wide, a globe circular, and a plant asymmetric. Family resemblance comes from consistent apparent weight, clean contour transitions, and controlled detail rather than making every silhouette identical.

- Prefer open outlines and generous internal space. Use small filled details only where they clarify meaning, such as palette wells or a pen's hole.
- Join straight sections and curves cleanly. Avoid accidental cusps, dark overlap seams, doubled edges, and tiny detached fragments.
- Round container corners deliberately. Do not round every point equally: arrows still point, leaves still taper, and circles remain circular.
- Use asymmetry when the subject needs it; remove accidental wobble and unnecessary perspective or texture.
- Avoid inflated shapes, excessively squat bodies, uniformly stubby handles, decorative distress, simulated depth, gradients, shadows, and multicolored illustration.
- Capture a supplied reference's identifying silhouette and relationships. Explain meaningful simplifications; do not silently substitute a generic symbol. Brand marks retain their identity rather than inheriting arbitrary UI rounding.

# GEOMETRY AND OPTICAL BALANCE

These are defaults for the 24-unit family, not universal measurements imposed on all projects.

| Property | Default |
|---|---|
| Native coordinate frame | `viewBox="0 0 24 24"` |
| Default displayed dimensions | `width="24" height="24"` |
| Outline stroke | `1.5` units, centered on the path |
| Nominal visible live area | `2–22` on each axis, including stroke |
| Broad rectangular corner radius | About `2` units on the centerline |
| Smaller structural transitions | Usually `0.75–1.5` units where needed |
| Exposed line ends and joins | Round; use a deliberate exception where the structure requires it |
| Intentional open gaps | Aim for at least `2` units; prefer `2.5` in dense areas |
| Optical placement | Start centered; small corrections around `0.5` units are normal |
| Color | `currentColor`, full opacity, transparent negative space |

Use shape-specific keylines inside the frame. A narrow icon need not fill the live area's width; a dense disk may need a smaller footprint than an open ring. Modest overshoot is acceptable when it improves balance, provided the viewBox does not clip the painted geometry. If an icon needs large positional corrections, revisit its construction.

A 1.5-unit stroke extends 0.75 on either side of its centerline. For example, a vertical centerline at x=3.75 has a left painted edge at x=3. Use decimal coordinates intentionally; do not force every vertex onto an integer pixel. These assets scale, so one coordinate choice cannot guarantee perfect raster alignment at every display size.

Use arcs or rounded rectangles for exact circular corners and Béziers for deliberately organic contours. For genuinely parallel nested contours with inset t, the inner radius is max(0, outer radius − t). This formula does not apply to unrelated internal details. Keep weight consistent across related icons; do not quietly thicken individual symbols to compensate for unresolved proportions.

Measure the SVG frame, ink bounds, and internal protected spaces separately. A correct bounding box is not proof of perceptual centering or exact contour clearance. Review the whole family at actual size beside regular text.

# NATIVE SIZE IS NOT DISPLAY SIZE

A 24-unit SVG displayed at 16px is still the same 24-unit drawing. Its 1.5-unit stroke renders at 1px. The standard specimen shows scaled samples; do not call those independently tuned 16px or 20px icons.

When compact native masters are requested, construct separate `0 0 16 16` and/or `0 0 20 20` drawings and review them at their native size. Start near proportional weights of 1.0 and 1.25 units respectively, then choose any optical adjustment consistently for that size family. Simplify details, reopen gaps, and rebalance alignment when needed. Do not manufacture optical variants by changing width/height alone or merely rescaling every coordinate.

Include only requested native sizes. State any practical minimum-size limitation, especially for numbered controls or complex reference marks. Do not claim every detailed icon is equally legible at 16px.

# SVG CONSTRUCTION

Use standalone SVG with explicit viewBox and scalable geometry. Default shell:

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24"
  viewBox="0 0 24 24" fill="none" stroke="currentColor"
  stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"
  aria-hidden="true" focusable="false">
  <circle cx="12" cy="12" r="9"/>
  <path d="M8 12h8m-4-4v8"/>
</svg>
```

This is a complete decorative plus-circle example. For a meaningful standalone SVG, remove aria-hidden and supply an accessible name. Label icon-only controls on their parent button/link; avoid duplicate announcements and repeated hardcoded title IDs.

A complete mixed-geometry example:

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24"
  viewBox="0 0 24 24" fill="none" stroke="currentColor"
  stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"
  aria-hidden="true" focusable="false">
  <path d="M4 15v-3.5a8 8 0 0 1 16 0V15"/>
  <rect x="4" y="13" width="4" height="7" rx="2"/>
  <rect x="16" y="13" width="4" height="7" rx="2"/>
</svg>
```

Use paths, circles, rectangles, ellipses, and other native vector primitives. Keep files free of raster images, external references, scripts, filters, masks, and clip paths unless the requested integration genuinely requires a documented exception. Keep cutouts transparent; never paint them in the assumed background color. Scale strokes with the viewBox, without non-scaling-stroke. Bake static transforms into final coordinates when practical and use enough precision to preserve the drawing.

Keep clean editable strokes as the normal source. An **expanded SVG** converts those strokes into filled contours while preserving the same outlined appearance. A **solid icon** is a separately composed visual variant. Do not confuse either with **SolidJS**, the component framework.

For solid variants, design the silhouette and negative spaces intentionally. Do not simply fill every closed outline or add a thick stroke. Preserve recognition, optical size, and relationships with outline companions. Use compound paths with appropriate fill rules for real holes. Do not import the weights or proportions of an unrelated older solid family.

# LETTERS, NUMERALS, AND RELATED CONTROLS

Use real font glyphs with one consistent font instance, scale, and weight for related labels. Convert fixed labels into SVG paths, preserving counters and proportions. Do not hand-improvise digits or stretch different strings to equal width. Use shaping for scripts that require it. If font conversion is unavailable, explain the limitation rather than claiming text is outlined or using an undisclosed substitute.

Design the container, label, and directional head together. Reserve label space first. Center the label's combined ink bounds on its intended container, then inspect the complete symbol optically. Place circular arrowheads along the tangent, outside the protected label area. Check label-to-head and label-to-ring clearance including stroke extents. Compare the widest actual label. Mirror only directional geometry, never text.

Use consistent triangles for play/track controls. Next/previous track have one triangle and a terminal bar; fast-forward/rewind have two triangles. Keep state pairs stable inside fixed controls. Do not automatically mirror playback symbols for RTL; distinguish navigation from media semantics.

# DELIVERABLES AND EXPORT CHOICES

## Default file package

For a new icon or set, when file creation is available:

```text
icons/
  svg/24/home-outline.svg
  preview.html
  README.md
  manifest.json
```

The SVG path above illustrates naming, not an instruction to add a home icon. Use lowercase kebab-case names and `-outline` or `-solid` suffixes. Native size folders are `svg/16/`, `svg/20/`, `svg/24/`, or the explicitly requested custom size. Standalone width/height match the native size; consumers may resize them.

- **SVGs:** one complete file per requested icon × visual variant × native size.
- **preview.html:** self-contained inline SVG; no remote fonts, libraries, or assets. Show 16/20/24/32px display sizes and a 72px detail, both polarities, and a 24px sample beside regular 16px text. Identify each native master so rescaled displays are not mistaken for optical variants. Adapt review sizes if the user specifies another range.
- **README.md:** inventory, formats, native grids, weight choices, naming/import guidance, accessibility usage, practical minimum sizes, and concise structural/rendered verification status. Do not include personal paths or private references.
- **manifest.json:** schema version, stable icon name, visual variant, native frame/viewBox, relative SVG path, and checks actually performed. Optional documented fields may record stroke weight, intended sizes, optical notes, and limitations. Use null/unknown rather than inventing a measurement or approval.
- **icons.zip:** include the finished SVGs, preview, README, manifest, and requested optional exports for a multi-icon set. Omit the archive for a single icon unless requested. Exclude source references, third-party library assets, font files, caches, temporary scripts, and superseded outputs.

A narrow request such as “SVG only,” “components only,” “no labels,” “in Paper,” or “just the prompt” overrides this default package. Do not create extra deliverables to satisfy a template against the user's explicit scope.

## Optional formats

| Choice | Files and behavior |
|---|---|
| React | `react/24/HomeOutlineIcon.tsx` and `index.ts`; typed size/SVG props, currentColor, accessible naming support |
| Vue | `vue/24/HomeOutlineIcon.vue` and `index.ts`; size props, inherited SVG attributes, currentColor |
| SolidJS | `solidjs/24/HomeOutlineIcon.tsx` and `index.ts`; native SolidJS SVG props, currentColor |
| React Native | `react-native/24/HomeOutlineIcon.tsx` and `index.ts`; use react-native-svg primitives, explicit size/color props, appropriate native accessibility props; document the peer dependency |
| Astro | `astro/24/HomeOutlineIcon.astro`; typed size/SVG attributes and currentColor |
| Expanded SVG | `svg-expanded/24/<name>-outline.svg`; true expanded stroke geometry, with editable original retained unless excluded |
| PNG | `png/24/<name>-outline.png`; transparent raster at the requested pixel size/color. A 24px icon at 2× is a 48×48px file named `<name>-outline@2x.png` |

Use the corresponding native-size folder for compact masters. Components preserve the approved geometry and distinguish native drawing size from the display size prop. Follow the target project's existing conventions. Do not install a framework or dependency simply to export its component files. Validate syntax/builds using available project tooling and report any validation limitation. Raw web SVG is not automatically a valid React Native component.

If PNG is requested without settings, use black on transparency, 24×24px at 1×. Other default choices remain SVG-based. Never substitute raster previews for requested editable vectors.

SF Symbols need a proper compatible template and a separate validation workflow; do not promise a valid symbol export by renaming an SVG. If asked, establish the target and available tooling before claiming support.

When exporting to a canvas, make the icon paths editable, preserve the original studies, and inspect the actual rendered frame. A static mockup is not tested application behavior.

## No file tools

Return complete files in filename-labelled code blocks, without omitted path data or ellipses. For a large set, use consecutive labelled batches until the requested inventory is complete. Do not invent downloads, ZIPs, screenshots, or successful rendering. Provide the standalone SVGs even if canvas or browser tools are unavailable, and state what could not be verified.

# VERIFICATION AND HANDOFF

Parse the SVGs; check the inventory, viewBoxes, native dimensions, supported elements, color behavior, and real transparency. Syntax success alone does not prove that path data renders correctly. Inspect enlarged contours and actual-size silhouettes in both light and dark contexts. Look for closed-up counters, crowded numeric labels, clipped strokes, heavy overlaps, uneven apparent weight, and unstable state pairs.

Check specimen overflow on a narrow viewport when an HTML specimen is included. For requested interactions, verify labels, keyboard operation, immediate state changes, rapid reversal, and reduced motion if animation exists. Keep the control's hit area stationary and separate from the drawn symbol. Static icons need no invented animation or interaction demo.

Correct material faults and rebuild affected outputs, including archives, from the final SVGs. Distinguish structural validation, rendered inspection, user approval, and actual application integration. Do not claim unperformed checks or automatically promote generated icons to permanent approved references.

Deliver working file links or complete code, a concise inventory, and a factual verification note with remaining limitations. Complete the requested result without adding unnecessary approval gates or unrelated setup.
