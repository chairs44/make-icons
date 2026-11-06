# USER INPUT: COMPLETE THIS SECTION FIRST

Replace the bracketed fields. All user-supplied information belongs here.

**REQUIRED**
- Icons to create: [LIST ICON NAMES AND CLARIFY UNUSUAL MEANINGS]

**OPTIONAL: DEFAULTS APPLY IF LEFT UNCHANGED**
- Variants: [solid / solid + outline; default: solid]
- Component format: [none / Astro / React / other; default: none]
- Interaction examples: [none / related states such as play ↔ pause; default: none]
- Motion in interaction examples: [off / restrained; default: off]
- Reference images: [attach images and identify their corresponding icons; default: none]
- Existing approved icons: [attach SVG files; default: none]
- Special constraints: [required symbols, sizes, directional behavior, output destination, or other constraints; default: none]

Standalone SVG files and a self-contained HTML specimen are the default outputs. Components are additional when requested. Explicit user instructions may narrow these outputs.

If the required inventory is missing, ask before drawing. Do not infer an inventory from a project. Reuse information already supplied in the conversation rather than asking again. Ask about optional fields only when ambiguity materially changes the result.

---

# TASK AND DESIGN DIRECTION

Create a cohesive set of editable SVG icons. Generate only the requested inventory and variants. Examples below demonstrate construction; they do not add to the inventory.

The default style is precise, compact, gently softened, and subtly unconventional. Think of purposeful markings on equipment: broad silhouettes, short extensions, controlled curves, and clear negative space. Consistency comes first. Personality comes from proportion and construction.

- Mostly solid silhouettes, slightly squat bodies, short stems, shafts, and handles.
- Straight sections connected by small deliberate curves.
- Familiar meanings and immediate recognition.
- Soft corners without inflated, bubbly, pillow-like, or cartoon forms.
- Arrowheads and other directional points remain directional. Circles remain circular.
- No decorative irregularity, texture, simulated depth, or unnecessary detail.

Explicit project constraints override defaults. When an established icon family is supplied, preserve its actual construction rather than imposing incompatible tokens. State material departures. Never distort a functional symbol merely to make it unusual.

# DIMENSIONS AND WEIGHT

All values below are SVG units on a 24 × 24 grid.

| Property | Default specification |
|---|---|
| ViewBox | `0 0 24 24` |
| Default display | `24 × 24px` |
| Inspection sizes | `16, 20, 24, 32px` |
| Standard visible bounds | `3–21` on both axes, including strokes |
| Optical overshoot | Up to `0.5` beyond standard bounds |
| Typical main body | `14–18` wide × `12–16` high |
| Structural corner radius | `0.75` |
| Broad rectangular-body radius | `1.25` where appropriate |
| Solid narrow bar | `3` |
| Solid primary bar | `3.5` |
| Outline stroke | `1.75` |
| Minimum intentional gap/cutout | `2` |
| Preferred small-size gap | `2.5–3` |
| Optical positioning correction | Up to `0.5` per axis before reconsidering geometry |

These define a family, not identical bounding boxes. Match perceived size and weight through geometry. Use smaller footprints for uninterrupted disks and other dense forms. Keep outline stroke consistent across a family; if changing it, change the family deliberately.

A 1.75-unit stroke extends 0.875 on either side of its centerline. Measure visible bounds after stroke expansion. Use decimal coordinates when needed. Bake optical correction into the SVG, not page-specific margins.

## Exact corners and nested contours

Use SVG `A` arc commands or rounded rectangles for exact circular radii. Bézier curves are appropriate for organic contours but must not be described as exact circular arcs.

For parallel nested rounded contours with uniform inset `t`:

```text
inner radius = max(0, outer radius − t)
```

Apply this only to genuinely parallel contours. Square inner corners can be correct when the inset exceeds the outer radius. Do not force unrelated interior details to share this formula.

# COLOR AND SCALING

Use `currentColor` only. Negative space stays transparent. No background-colored holes, gradients, textures, shadows, filters, or second colors. Static geometry uses full opacity. Scale strokes with the viewBox; do not use `vector-effect="non-scaling-stroke"`.

# HOW TO BUILD THEM

## SVG shells

Solid:

```svg
<svg xmlns="http://www.w3.org/2000/svg"
  width="24" height="24" viewBox="0 0 24 24"
  fill="currentColor" aria-hidden="true" focusable="false">
  <!-- Resolved geometry -->
</svg>
```

Outline:

```svg
<svg xmlns="http://www.w3.org/2000/svg"
  width="24" height="24" viewBox="0 0 24 24"
  fill="none" stroke="currentColor" stroke-width="1.75"
  stroke-linecap="round" stroke-linejoin="round"
  aria-hidden="true" focusable="false">
  <!-- Resolved geometry -->
</svg>
```

These are decorative shells. Meaningful standalone icons need an accessible name and no `aria-hidden`. Label icon-only buttons/links on the parent. Avoid duplicate title IDs when repeated.

## Construction tokens

```ts
export const iconTokens = {
  viewBox: "0 0 24 24",
  defaultSize: 24,
  inspectionSizes: [16, 20, 24, 32],
  bounds: { min: 3, max: 21, opticalOvershoot: 0.5 },
  radius: { structural: 0.75, broadBody: 1.25 },
  solid: { narrowBar: 3, primaryBar: 3.5 },
  outline: { strokeWidth: 1.75, halfStroke: 0.875 },
  gap: { minimum: 2, preferred: 2.5 },
  opticalShiftLimit: 0.5,
} as const;
```

Resolve tokens into standalone files. Use SVG kebab-case attributes or the component framework's appropriate syntax.

## Solid construction and cutouts

Draw softened silhouettes directly. Do not inflate filled shapes with an extra stroke. Use compound paths and `fill-rule="evenodd"` for transparent cutouts.

```svg
<!-- Outer radius 1.25, inset 3, square interior corners. -->
<path fill="currentColor" fill-rule="evenodd" d="
  M4.25 5 H19.75 A1.25 1.25 0 0 1 21 6.25
  V17.75 A1.25 1.25 0 0 1 19.75 19
  H4.25 A1.25 1.25 0 0 1 3 17.75
  V6.25 A1.25 1.25 0 0 1 4.25 5 Z
  M6 8 H18 V16 H6 Z
"/>
```

Naturally linear solid-family symbols may use strokes or expanded geometry at the 3 or 3.5 bar weight. Do not automatically use the thinner outline weight.

## Complete construction anchors

The following generic examples provide exact path data. Use them directly when requested or derive related geometry from their proportions. They establish the default family, not universal shapes for every project.

### Home: solid

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" focusable="false"><path d="M4 10.375 A0.75 0.75 0 0 1 4.3 9.775 L11.55 4.338 A0.75 0.75 0 0 1 12.45 4.338 L19.7 9.775 A0.75 0.75 0 0 1 20 10.375 L20 18.25 A0.75 0.75 0 0 1 19.25 19 L14.75 19 A0.75 0.75 0 0 1 14 18.25 L14 14.75 A0.75 0.75 0 0 0 13.25 14 L10.75 14 A0.75 0.75 0 0 0 10 14.75 L10 18.25 A0.75 0.75 0 0 1 9.25 19 L4.75 19 A0.75 0.75 0 0 1 4 18.25 Z" /></svg>
```

### Home: outline

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M4.875 10.725 A0.75 0.75 0 0 1 5.175 10.125 L11.55 5.338 A0.75 0.75 0 0 1 12.45 5.338 L18.825 10.125 A0.75 0.75 0 0 1 19.125 10.725 L19.125 17.375 A0.75 0.75 0 0 1 18.375 18.125 L15.625 18.125 A0.75 0.75 0 0 1 14.875 17.375 L14.875 13.875 A0.75 0.75 0 0 0 14.125 13.125 L9.875 13.125 A0.75 0.75 0 0 0 9.125 13.875 L9.125 17.375 A0.75 0.75 0 0 1 8.375 18.125 L5.625 18.125 A0.75 0.75 0 0 1 4.875 17.375 Z" /></svg>
```

### Play: solid

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" focusable="false"><path d="M7 6.306 A0.75 0.75 0 0 1 8.128 5.658 L17.889 11.352 A0.75 0.75 0 0 1 17.889 12.648 L8.128 18.342 A0.75 0.75 0 0 1 7 17.694 Z" /></svg>
```

### Play: outline

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M7.875 7.776 A0.75 0.75 0 0 1 8.99 7.121 L16.574 11.345 A0.75 0.75 0 0 1 16.574 12.655 L8.99 16.879 A0.75 0.75 0 0 1 7.875 16.224 Z" /></svg>
```

### Pause: solid

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" focusable="false"><rect x="7" y="5" width="3.5" height="14" rx=".75"/><rect x="13.5" y="5" width="3.5" height="14" rx=".75"/></svg>
```

### Pause: outline

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M8.75 5.875V18.125 M15.25 5.875V18.125"/></svg>
```

Structural corners in these anchors use 0.75-unit arcs. Pause bars are 3.5 × 14 units with a 3-unit gap. Outline pause centerlines preserve the solid bars' centers and visible height, using single strokes instead of cramped hollow rectangles.

For other polygons, construct circular corners by locating tangent points on both adjacent edges:

```text
u = unit vector from corner to previous vertex
v = unit vector from corner to next vertex
angle = acos(clamp(dot(u, v), -1, 1))
tangent distance = radius / tan(angle / 2)
arc start = corner + u × tangent distance
arc end = corner + v × tangent distance
```

Connect tangent points with circular SVG arcs, choosing sweep from the polygon's turn direction. Reject collinear/reversing vertices and radii that cause adjacent arcs to overlap. Keep delivered SVGs independent of runtime geometry code.

# ICONS CONTAINING TEXT OR NUMERALS

Use a real, appropriately licensed typeface rather than improvising letters or digits from unrelated strokes. Choose one font instance, weight, baseline policy, and uniform scale for the related icon family. Preserve natural proportions and spacing; do not stretch each label to equal width.

For fixed short labels, convert shaped glyph outlines to filled SVG paths so the delivered icon has no font dependency. Preserve glyph contours and counters. Use actual shaping for scripts or combinations that require it; simple decimal strings may use the font's advances. Keep the font source and conversion settings in working files, outside a minimal delivery ZIP.

Center the visible bounds of the complete label within its intended container, not each character separately and not an assumed text advance box. Inspect optical balance afterward. Keep directional icon geometry separate from glyph geometry so mirroring never reverses the text.

For enclosed numerals, design the container and label together. Reserve a protected label region before positioning arrowheads. Center labels on the actual circle center, which need not equal the canvas center. Put circular-arrow heads on the tangent and outside the label region; derive mirrored pairs from shared circle geometry. Measuring only text bounds is not sufficient: check label-to-head and label-to-ring clearance, including stroke expansion.

A tested starting construction for two-digit time controls uses circle center (12,13), radius 7.5, a 2.25-unit ring, a top-tangent arrowhead, and medium-bold digits at a shared 5.2-unit height centered on (12,13). Maintain at least 2.5 units of vertical clearance between the arrowhead's lowest edge and the numeral's top edge for this construction. These are coordinated example values, not universal requirements. Inspect the complete symbol at 16/20/24/32px in both polarities; numeric centering assertions do not prove optical balance. Keep a larger practical minimum size if digits cannot remain legible.

## Coordinated construction example

Use one shared geometry definition for a related pair. The complete icon may have an asymmetric outer silhouette; its label is centered on the circle, not on the full icon's bounding box.

```ts
const timeControl = {
  circle: { cx: 12, cy: 13, radius: 7.5 },
  ringWidth: 2.25,
  label: {
    referenceDigitHeight: 5.2,
    centerX: 12,
    centerY: 13,
    // One font instance and scale for all labels; retain natural overshoot.
    weight: 600,
  },
  minimumHeadToLabelVerticalGap: 2.5,
};
```

Weight 600 is a starting point for a compatible variable sans-serif, not a promise of equivalent appearance across typefaces. The reference height is measured from the font's zero. Other digits may have slightly different ink heights because of overshoot; do not rescale each string to erase those differences.

The pair's circular centerlines are:

```svg
<!-- Back: long arc, ending at the top tangent. -->
<path d="M5.505 9.25 A7.5 7.5 0 1 0 12 5.5"
  fill="none" stroke="currentColor" stroke-width="2.25"
  stroke-linecap="round"/>

<!-- Forward: horizontally mirrored circle geometry. -->
<path d="M18.495 9.25 A7.5 7.5 0 1 1 12 5.5"
  fill="none" stroke="currentColor" stroke-width="2.25"
  stroke-linecap="round"/>
```

Construct the rounded arrowheads with a 0.35-unit radius:

```ts
const backHead = [[9, 5.5], [12.5, 3.3], [12.5, 7.7]];
const forwardHead = [[15, 5.5], [11.5, 3.3], [11.5, 7.7]];
// Feed each polygon into a circular-corner generator.
// Mirror the arrow geometry only, never the numerals.
```

Typeset the full label, convert it into paths, measure its combined ink bounds, and translate it into the circle. The following is build-time inspection logic, not a runtime dependency:

```js
function labelPlacement(bounds, center = { x: 12, y: 13 }) {
  return {
    dx: center.x - (bounds.x + bounds.width / 2),
    dy: center.y - (bounds.y + bounds.height / 2),
  };
}

function verticalClearance(labelBounds, arrowBounds) {
  return labelBounds.y - (arrowBounds.y + arrowBounds.height);
}
```

Bake the placement into final path coordinates. Inspect the nearest distance to the ring separately: vertical arrow clearance does not prove clearance from all surrounding shapes. Do not report a bounding-box check as a pixel-accurate contour-distance measurement.

The approved reference pair has label ink centers at (12,13), about 3 units of vertical arrowhead clearance, and label widths of approximately 6.92 units for 15 and 8.61 for 30. Unequal widths are intentional; the font and scale are shared. These measurements are regression references for this construction, not mandatory dimensions for all numbered icons.

## Visual acceptance

- Review the arrowhead, ring, label, and gap as one composition, including at 100% display size.
- Compare both directions and all requested values together. Include the widest actual label.
- Show 16/20/24/32px in both polarities, plus an enlarged detail view for contour defects.
- Numeric checks establish geometry; rendered inspection establishes perceived balance. Neither replaces the other.
- Prefer a structural correction when the head invades the label space. Shrinking or nudging text alone may preserve the underlying fault.
- Mark user-approved results as approved only at their actual scope. Preserve that geometry as a reusable anchor; do not generalize one approval to every icon or size.
- Rebuild the specimen, exported showcase, and ZIP from the final SVGs. Check archive contents so no stale version remains.

Primary references: [Material icon construction](https://m3.material.io/styles/icons/designing-icons) explains grid-based geometry, optical corrections, and actual-size review. [Carbon icon usage](https://carbondesignsystem.com/elements/icons/usage) discusses consistent sizing and pairing icons with text. Adopt principles without silently importing another system's specific weights or geometry.

# OUTLINE COMPANIONS

Generate only when requested. Redraw for the stroke thickness while preserving orientation, proportions, and distinguishing features.

- Do not simply remove fill and stroke every solid boundary.
- Avoid doubled internal edges and cramped cavities.
- Narrow bars may become single centerline strokes; apply the choice consistently.
- Preserve recognition and negative space at small sizes.
- Optical companions do not need identical ink coverage or exact mathematical offsets.

# FAMILY RELATIONSHIPS

Use related triangle geometry for play and track controls, adjusting the footprint for terminal bars. Next/previous track use one triangle and one terminal bar; fast-forward/rewind use two triangles. Build arrow directions from common geometry. Keep stems, bars, and corners consistent. Prefer one or two primary forms, but preserve additional parts when meaning requires them.

Do not automatically mirror media controls in right-to-left interfaces; distinguish navigation direction from playback semantics.

# REFERENCE-BASED ICONS

Extract the identifying silhouette and relationships between parts. Remove perspective, texture, accidental roughness, and dispensable detail. Favor a coherent silhouette over tiny detached fragments. Preserve internal identity through negative space where possible.

Do not silently replace a specific reference with a generic symbol. Explain meaningful omissions. If the mark needs a larger minimum size, state it. Detailed emblems need not satisfy the same detail budget as simple controls.

# OPTIONAL INTERACTION EXAMPLES

Only include interactions requested in the input section. Static SVGs remain independent.

Use native buttons, fixed control dimensions, immediate action/state/label updates, and safe rapid reversal. Label the current available action. Use `aria-pressed` only for true toggles. Do not add fake loading or defer functionality until motion finishes.

When restrained motion is requested, this is the default press-feedback implementation:

```css
.icon-control {
  display: inline-grid;
  place-items: center;
  inline-size: 48px;
  block-size: 48px;
  padding: 0;
}
.icon-control__glyph {
  display: block;
  inline-size: 24px;
  block-size: 24px;
  transform-origin: center;
  transition: transform 140ms cubic-bezier(0.2, 0.8, 0.2, 1);
}
.icon-control__glyph > svg {
  display: block;
  inline-size: 100%;
  block-size: 100%;
}
.icon-control:active:not(:disabled) .icon-control__glyph {
  transform: scale(0.97);
}
.icon-control:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 4px;
}
@media (prefers-reduced-motion: reduce) {
  .icon-control__glyph { transition: none; }
  .icon-control:active:not(:disabled) .icon-control__glyph {
    transform: none;
  }
}
```

Prefer immediate symbol replacement. Do not add path morphs unless requested. No default idle loops, shimmer, blur, jelly deformation, decorative spinning, or bounce. Keep the hit area stationary. Motion should be interruptible and must not change layout. Reduced motion removes movement while preserving state changes.

# TECHNICAL OUTPUT

Deliver real editable SVGs, using paths/circles/rectangles/ellipses where possible. No rasters, external assets, filters, masks, clip paths, or background shapes. Bake static transforms into coordinates. Use concise path data with appropriate precision.

Use kebab-case filenames such as `home-solid.svg` and `home-outline.svg`. If requested, add native components named `HomeIcon` and `HomeOutlineIcon`, supporting size props, CSS sizing, forwarded SVG attributes, and accessible naming. Do not install dependencies or change project architecture.

# SPECIMEN AND VERIFICATION

Provide a responsive self-contained `preview.html` with inline SVGs:
- Each requested icon at 16/20/24/32px and an enlarged 72px view.
- Solid/outline comparisons when requested.
- Dark-on-light and light-on-dark examples.
- Examples beside regular-weight 16px text, with labels outside the artwork.
- Requested state pairs in fixed controls.

Inspect actual sizes rather than only enlarged geometry. Check perceived size/weight, open cutouts, corner consistency, stroke bounds, recognition, related symbol alignment, transparent holes, and narrow-mobile overflow. Distinguish fixed button bounds from optical stability when symbols swap; check both. For interactive examples, check keyboard activation, rapid reversal, and reduced motion.

Parse SVGs and inspect desktop/mobile rendering when tools permit. Correct material issues in a bounded pass. If rendering is unavailable, explicitly state that visual verification was not performed.

For a large uncertain set, use a representative specimen before expansion. Reuse approved shapes and prior checks for unchanged work. Newly generated icons are review candidates, not automatically permanent approved anchors. Do not require redundant approval for work already authorized.

# DELIVER

1. Complete standalone SVGs for every requested icon and variant.
2. Framework-native components if requested.
3. Self-contained `preview.html`, unless the user explicitly narrowed the deliverable.
4. A ZIP when file-writing tools are available and packaging is useful.
5. A one-line inventory and a brief factual verification note with material limitations.

Create files and provide working links when tools allow; otherwise return complete files in separate filename-labeled code blocks. No omitted paths, placeholder geometry, external library substitutions, or instructions in place of work you can complete.
