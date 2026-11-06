# Fidelity and the second visual pass

## Establish the target

Select reproduction, adaptation, or invention from the user's wording. Exact matching permits direct use of supplied paths and tracing or reconstruction of supplied imagery. Do not introduce arbitrary novelty. For a new subject in a known family, transfer its contour grammar without copying an unrelated silhouette. Existing source rights and distribution terms still apply; do not label third-party paths as newly authored or assume permission to bundle a source collection.

Inspect every input you will actually use. Verify that a crop contains the intended icon and variant, excludes neighbouring icons and UI borders, and retains all terminals. If it does not, fix the crop before drawing. Identify the subject, orientation, outline/solid variant, visible parts, openings, and key junctions. Estimate normalized landmark positions from the image; label these estimates. A screenshot cannot prove the original SVG's coordinates.

For a supplied SVG, inspect paths, viewBox, transforms and fill/stroke policy. Preserve source geometry when reproduction is requested. Scaling dimensions changes presentation; non-uniform stretching changes the drawing. Do not replace designed filled contours with a uniform stroke if that loses taper, terminal shape, or overlap treatment.

## Build a short construction map

Before coding, record the few decisions that define the drawing, internally or in a small review file:

- Silhouette landmarks: extremities, axis, major widths/heights, and directional angle.
- Parts and relationships: continuous, attached, crossing, or detached; which segment remains visible at a crossing.
- Negative spaces: count, shape, whether open to the exterior, and the boundaries they share.
- Terminal treatment: rounded cap, flat cut, chamfer, taper, or custom curve. Specify it per exposed part, not once for the whole icon.

Semantic knowledge is a sanity check, not permission to override a stylized reference. Check whether the depicted object still makes sense: handles connect to members, a blade continues on its intended axis, a doorway is the selected inset/open variant, and a stem meets its leaves without an accidental vein. Do not add realistic hardware absent from the reference. Identify ambiguity rather than inventing a pivot, hinge, or extra edge.

## Draw against evidence

Compare normalized landmarks before adding fine detail. Preserve aspect ratio and relative part size. Use clean strokes for uniform portions and custom filled contours for shaped tips or variable width; these can coexist in one SVG. `fill="currentColor" stroke="none"` on a blade is compatible with an outline family. Expanded contour geometry is not the same thing as a solid icon.

At crossings, trace each member mentally from its attachment to its tip. Interrupt only the hidden interval. Do not break a visible member early just to avoid an overlap. Calculate cap extents when a broken member uses strokes. Compare the actual junction and amount of clearance to the reference instead of imposing a universal gap value. Shared edges appear once.

## Fresh second pass: inspect the rendered artifact

Finish the first drawing, save it, render it, then look again without relying on the rationale used while drawing. If image inspection is unavailable, say visual verification is incomplete. Parsing XML or rereading coordinates does not substitute for this pass.

1. **Identity and topology.** Is it the requested subject and variant? Count the intended parts and holes. Follow attachments and crossing order. Check silhouette continuity, missing/extra details, unintended seams, and detached terminals. A wrong variant or impossible connection is a blocking defect even when the drawing looks polished.
2. **Reference fidelity.** Compare at the same apparent ink height while preserving aspect ratio, and also in the same fixed native frame. Inspect width/height ratio, landmarks, terminal angles, corner roles, relative part size, line density, and negative spaces. Use a labelled side-by-side and, when useful, a 50% overlay or difference image. Align by translation and uniform scale only; do not warp the output to improve its score.
3. **Actual-size quality.** Inspect native/target sizes and enlarged contours on light and dark backgrounds. Check disappearing gaps, apparent weight, clipping, tip quality and unintended islands. A reference-faithful reconstruction may retain a small-size limitation; report it rather than silently redesigning the reference.

A comparison helper is available at [../scripts/compare.py](../scripts/compare.py). It writes local HTML from an SVG and a reference image without altering either. Render and inspect the HTML using available browser tools; the helper itself does not grade or certify visual quality.

Record concrete evidence for each blocking issue: affected icon, observed difference, correction, and whether the final render was inspected. Avoid a generic “looks good” verdict. Fix the largest structural differences first, rerender, then check for regressions in affected views. Reuse unaffected checks. Stop when the requested fidelity and deliverables are met; if an unresolved source or tool limitation prevents that, explain it without declaring a perfect result.

For invented or adapted subjects, name the strongest plausible alternative reading at the target size. If the intended meaning depends on its filename or a large close-up, strengthen the smallest distinctive cue or simplify competing cues. For unfamiliar objects, consult a representative object reference when available; do not invent mechanical structure merely from the noun. Compare the revised icon at the same small size. If ambiguity persists, record that it needs a label or a larger size rather than treating generic recognizability as a pass.

## Report exactly what is known

Separate structural validation, visual inspection, source match, and user approval. For vector reuse, exact geometry can be checked directly. For raster reconstruction, similarity metrics are diagnostics, not proof of source equality or taste. A baseline comparison needs independent runs with identical inputs; an edited copy of the treatment is not a baseline. Do not hide a worse result behind an averaged score.
