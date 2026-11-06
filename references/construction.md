# Contour construction

Read this before drawing a new family. The target is compact editorial line art: economical silhouettes, deliberate transitions, and quiet internal detail. A matching stroke token is necessary but does not establish style.

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
