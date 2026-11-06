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
| Intentional open gaps | Measure painted-edge clearance; aim around `1.5–2` units where parts must remain separate |
| Optical placement | Start centered; small corrections around `0.5` units are normal |
| Color | `currentColor`, full opacity, transparent negative space |

Use shape-specific keylines inside the frame. A narrow icon need not fill the live area's width; a dense disk may need a smaller footprint than an open ring. Modest overshoot is acceptable when it improves balance, provided the viewBox does not clip the painted geometry. If an icon needs large positional corrections, revisit its construction.

A 1.5-unit stroke extends 0.75 on either side of its centerline. For example, a vertical centerline at x=3.75 has a left painted edge at x=3. Use decimal coordinates intentionally; do not force every vertex onto an integer pixel. These assets scale, so one coordinate choice cannot guarantee perfect raster alignment at every display size.

Use arcs or rounded rectangles for exact circular corners and Béziers for deliberately organic contours. For genuinely parallel nested contours with inset t, the inner radius is max(0, outer radius − t). This formula does not apply to unrelated internal details. Keep weight consistent across related icons; do not quietly thicken individual symbols to compensate for unresolved proportions.

Measure the SVG frame, ink bounds, and internal protected spaces separately. A correct bounding box is not proof of perceptual centering or exact contour clearance. Review the whole family at actual size beside regular text.

# CONTOUR CONSTRUCTION

The target is compact editorial line art: economical silhouettes, deliberate transitions, and quiet internal detail. A matching stroke token is necessary but does not establish style.

## Establish the silhouette

For each subject, identify the outer mass, one or two identifying cues, and the openings that must survive. Draw the outer contour first and view it at 24px. Add detail only where recognition needs it. A book should read as a narrow bound volume before a spine line is added; a sprout should read as leaves and a stem before veins or a container are considered.

Use a small set of shape-specific starting keylines, not a universal box: circular forms around 18 units in diameter; upright objects around 14 × 18; horizontal objects around 18 × 14. These are drawing aids, not required final bounds. Compare mass beside text and neighboring icons. Never stretch a finished path non-uniformly to force it into a keyline.

## Make the contour, not a pile of parts

- A rectangle, circle, or capsule is useful when it describes the object. Do not assemble every organic object from rounded boxes. Leaves taper; soft bags have shoulders; earcups need room inside the arch.
- Use the fewest curve segments that preserve the silhouette. At a smooth join, incoming and outgoing tangents must share a direction. For a cubic leaving a vertical edge, place its first control point on that vertical; approaching a horizontal edge, place its last control point on that horizontal. Tangent continuity removes kinks; handle lengths still need visual tuning to prevent swelling or flat spots.
- A round linejoin only rounds the stroke at a vertex. It does not replace a designed corner or repair a poorly drawn curve. Use actual arcs or curves for structural transitions. Treat narrow tips separately so they retain direction without needle-like spikes.
- Plan ownership of shared edges before drawing. Two parts sharing a boundary draw it once. A contour passing behind another part stops at the attachment or occlusion; do not leave a doubled segment or a cap bulging past a join. Do not hide these errors with background-colored patches.
- Distinguish a junction from a gap. Connected lines meet intentionally; separated parts need visible air. For stroke width w and parallel centerline separation d, clear space is d − w. Two centerlines 2 units apart with 1.5-unit strokes leave only 0.5 units, not a 2-unit opening. For unrelated openings, aim for roughly 1.5–2 units of painted-edge clearance at 24 units; simplify dense details when this cannot survive the intended display size. Intentional tapered closures are different.
- Maintain one stroke policy across the set. Do not change individual weights, add tiny detail, or inflate every corner to make an unresolved silhouette feel more finished.

## Proportion, corners, and visual economy

Build a clear, compact silhouette with a generous interior. Use long uninterrupted straights where the object is structural, then short controlled transitions at corners. Avoid making every short edge a curve: excessive rounding turns books, devices, and containers into inflated capsules. Conversely, a bare polygon with round joins can remain stiff and mechanically pointed.

Treat corners by role rather than applying one radius everywhere:

- Broad body corners use the family’s approximately 2-unit starting radius where space permits. Preserve enough straight wall and base to read as structure.
- Direction changes such as a roof apex, folder shoulder, or camera step use a shorter transition. Retain their angle and identity; soften the vertex without flattening the entire peak into a dome.
- Concave notches and apertures have their own fit. Make their opening deliberate and readable, not a tiny rounded dent. A contour that enters a recess must return cleanly to the body.
- Leaf ends, blade tips, and directional points may taper. Keep the tip intentional; do not force a circular corner onto every endpoint or leave a protruding miter.

For approximately symmetric subjects, construct the primary silhouette around a shared axis. Match corresponding slopes, shoulders, and side heights before making an optical correction. A roof and body should read as one stable mass; a lens belongs to the camera body’s visual center, which need not be the center of the full silhouette including its top step. Do not compensate for poor proportions by casually shifting individual details.

Default to a front-facing or otherwise direct view when it communicates the subject. Perspective, extra rims, seams, and texture must earn their place through recognition. Choose the simplest identifiable variant, not the variant with the most drawn parts. A closed book can need only its outer contour and a page-block boundary; a camera can need only a body and lens. A sprout does not need a pot unless the requested subject is a potted plant. Simplicity means removing redundant information, not making every subject a generic box.

## Connected parts, crossings, and secondary symbols

Decide how parts relate before choosing SVG elements. There are four distinct cases:

| Relationship | Construction decision |
|---|---|
| Continuous object | Use a coherent contour; avoid arbitrary seams between primitive shapes. |
| Attached detail | Meet the body at a deliberate junction; draw a shared boundary once. |
| Foreground crossing | Keep the foreground contour continuous and interrupt the rear contour with visible clearance. |
| Detached modifier | Reserve its space and terminate the host outline before it crowds or crosses the modifier. |

Round caps extend half the stroke width past an open path endpoint. Account for that extension when cutting a rear line or opening a host contour. Inspect painted clearance on both sides of a crossing; equal centerline gaps can look unequal on diagonals. Keep gaps intentional and localized. Do not scatter decorative breaks around an otherwise continuous symbol.

A modifier, such as a plus, arrow, link, or status mark, should remain legible without overpowering its host. Prefer a consistent attachment region across related variants. Preserve the base object’s principal proportions and alignment; remove or interrupt the local contour behind the modifier instead of shrinking the whole host indiscriminately. Do not let a badge touch the frame or collide with an adjacent part.

Choose between an inset detail and an opening in the outer silhouette. They are different constructions, not interchangeable SVG tricks. An inset arch may meet a base boundary; an open recess replaces that boundary. Keep the chosen topology consistent within closely related variants. For linked loops, show the connection through controlled interruptions and continuous segments rather than stacking complete closed loops into a dark knot.

## Organic curves and directional energy

Use a small number of broad, smooth curves for organic masses. Preserve a clear change in curvature between a full lobe, a narrowing side, and a tapered end. Do not assemble a heart from two obvious circles and straight sides or make leaves into rounded rectangles. The shoulder of a heart should flow into its side; its valley and lower point should remain distinct without looking pinched or needle-sharp.

Organic asymmetry should describe growth or orientation. Two leaves can differ in height, angle, and fullness while meeting a shared stem naturally. Give each leaf one clear convex outer sweep and a complementary returning curve; omit veins unless they materially help recognition. Let stems connect at deliberate junctions instead of extending through an enclosed leaf as an accidental extra stroke.

For tools and diagonal objects, preserve the action implied by the silhouette. Use repeated handles or loops with matched dimensions and a coherent pivot. A crossing can use a continuous leading member and a broken rear member; it need not have a decorative pivot dot. Keep long blades or shafts purposeful instead of shortening them until the tool looks toy-like. Different valid variants may use open lines or enclosed blades; choose one construction language for the requested set.

## Reference interpretation and transfer

A screenshot supports judgments about silhouette, relative proportions, visual density, and contour relationships. It does not by itself establish native coordinates, exact radii, stroke expansion, or pixel alignment. Keep verified family tokens as defaults; do not invent precise measurements from enlarged raster samples. Compare normalized renderings at the same displayed size before changing the family’s weight.

Transfer the decisions, not the subject list: economical structure applies to containers and devices; full-to-tapered curves apply to organic objects; controlled interruptions apply to modifiers, interlocks, and crossings. Do not add house-specific roof proportions as a universal rule, force all organic objects to be asymmetric, or force every symbol to have a broken outline. Keep external reference names and artwork out of the distributed instructions and assets unless explicitly requested.

## Review against evidence

Use any supplied reference at the same displayed size and color. Compare silhouette proportions, line density, curve transitions, junctions, and negative space separately. Extract construction principles; do not trace third-party paths or redistribute their artwork without permission. A reference with expanded fills may still be line art.

For a set, inspect one upright, one circular/diagonal, and one organic subject before extending the vocabulary. This is an internal drawing pass, not an extra user approval requirement. If a supplied reference and a bundled example disagree, follow the requested reference and explain any meaningful construction change.

Inspect at actual size before enlarged views. At 16/20/24/32px, look for disappearing openings, fuzzy clusters, excessive apparent size, and weak recognition. At 8×, inspect tangents, joins, overshooting caps, and accidental double edges. Use both polarities. Compare a structural container, an organic contour, and a crossing/modifier when those categories occur in the requested set. Reject inflated corner transitions, redundant seams, crowded badges, ambiguous over/under relationships, and loss of the subject’s characteristic proportions. Fix identifiable defects in one consolidated pass, then confirm the affected views. Do not call a drawing approved because XML validation passed.

Keep generated studies separate from approved anchors. Acceptance of a general direction does not approve every example. Record structural checks, rendered review, and user approval as separate facts. Instructions improve repeatability; no prompt guarantees expert-level drawing or an exact style match without visual review.

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

A complete connected-contour example. The arch meets the earcups at their outside junctions without retracing their side edges:

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M4.5 14.5v-3a7.5 7.5 0 0 1 15 0v3"/><path d="M8 13H6a1.5 1.5 0 0 0-1.5 1.5V18A1.5 1.5 0 0 0 6 19.5h.5A1.5 1.5 0 0 0 8 18v-5ZM16 13h2a1.5 1.5 0 0 1 1.5 1.5V18a1.5 1.5 0 0 1-1.5 1.5h-.5A1.5 1.5 0 0 1 16 18v-5Z"/></svg>
```

Use paths, circles, rectangles, ellipses, and other native vector primitives. Keep files free of raster images, external references, scripts, filters, masks, and clip paths unless the requested integration genuinely requires a documented exception. Keep cutouts transparent; never paint them in the assumed background color. Scale strokes with the viewBox, without non-scaling-stroke. Bake static transforms into final coordinates when practical and use enough precision to preserve the drawing.

Keep clean editable strokes as the normal source. An **expanded SVG** converts those strokes into filled contours while preserving the same outlined appearance. A **solid icon** is a separately composed visual variant. Do not confuse either with **SolidJS**, the component framework.

For solid variants, design the silhouette and negative spaces intentionally. Do not simply fill every closed outline or add a thick stroke. Preserve recognition, optical size, and relationships with outline companions. Use compound paths with appropriate fill rules for real holes. Match the established family’s apparent weight and proportions.

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
