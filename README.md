# Make Icons

A coding-agent skill for making custom SVG icons that belong together. Open contours, balanced proportions, clear negative space, and editable vector geometry.

![Sixteen Make Icons samples in two rows of eight, from Face ID and a radio telescope to a download and checkmark.](docs/make-icons-showcase.png)

[Download the sample pack](https://github.com/chairs44/make-icons/raw/refs/heads/main/make-icons-samples.zip) · [Copy the complete prompt](references/master-prompt.md) · [Read the skill](SKILL.md)

## What it does

Make Icons gives your agent a drawing system, construction examples, and tools for checking a set together. The default is a 24-unit outline family with a 1.5-unit stroke. Ask for the symbols you need, or provide visual references to simplify into icons.

1. **Draw** standalone SVGs using shared proportions, circular corners, and transparent cutouts.
2. **Compare** the set at 16, 20, 24, and 32 pixels, with enlarged views and light/dark contexts.
3. **Deliver** editable files and an HTML specimen. Add solid variants, components, or motion only when requested.

Optional exports include React, Vue, SolidJS, React Native, Astro, expanded SVG, and PNG. Expanded outlines preserve the outline appearance; they are not solid variants.

The rules are defaults, not a fixed icon catalogue. Optical balance and recognition matter more than identical bounding boxes. An agent still needs to inspect the rendered result; the scripts do not certify visual quality.

## Files

| File | Purpose |
| --- | --- |
| [`SKILL.md`](SKILL.md) | Agent instructions and workflow |
| [`references/master-prompt.md`](references/master-prompt.md) | Complete copy-and-paste prompt, specifications, and construction examples |
| [`assets/outline-24/`](assets/outline-24/) | Twenty-eight current outline construction references |
| [`scripts/geometry.py`](scripts/geometry.py) | Exact circular corners for polygons, using Python's standard library |
| [`scripts/specimen.py`](scripts/specimen.py) | Recursive SVG validation, comparison sheet, manifest, and ZIP packaging |
| [`assets/legacy-solid/`](assets/legacy-solid/) | Eight preserved examples for matching the earlier family |
| [`samples/svg/24/`](samples/svg/24/) | The sixteen SVGs shown above |
| [`samples/preview.html`](samples/preview.html) | Self-contained specimen; download and open in a browser |
| [`make-icons-samples.zip`](https://github.com/chairs44/make-icons/raw/refs/heads/main/make-icons-samples.zip) | Downloadable sample pack |
| [`agents/openai.yaml`](agents/openai.yaml) | Display metadata for compatible agents |

## Installation

Install with the [Skills CLI](https://skills.sh):

```bash
npx skills add chairs44/make-icons --skill make-icons
```

Or copy this repository into your agent's skills directory as `make-icons/`. Keep `SKILL.md`, `references/`, `scripts/`, and `assets/` together so relative references resolve.

For a chat-only workflow, open the [master prompt](references/master-prompt.md), copy the whole document, and fill in its input section. SVG generation needs a model capable of writing code; running the helpers requires Python 3.10+ and a browser is useful for review. Delivered SVGs have no runtime dependencies.

## Usage

```text
Use make-icons to create a cohesive outline SVG set:
seed vault, field recorder, radio telescope, and night train.
Deliver the editable SVGs and a self-contained comparison specimen.
```

Ask explicitly for solid variants or compact native masters or a React/Astro component when needed. Attach references when a specific object or mark matters.

To inspect your own SVG directory:

```bash
python3 scripts/specimen.py ./my-icons \
  --output ./specimen.html --zip ./my-icons.zip
```

Open the HTML in a browser. Check recognition at actual size, transparent cutouts on both backgrounds, and perceived weight across the set.

## Design specifications

| Property | Default |
| --- | --- |
| Canvas | `viewBox="0 0 24 24"` |
| Visible bounds | 2–22 units including stroke; modest optical overshoot where needed |
| Character | Open outlines, natural subject proportions, restrained rounding |
| Corners | About 2 units for broad corners; 0.75–1.5 for smaller transitions |
| Default stroke | 1.5 units with round caps and joins |
| Native sizes | 24 by default; separately drawn compact 16/20 masters on request |
| Negative space | At least 2 units; preferably 2.5–3 at small sizes |
| Colour | `currentColor`; transparent cutouts, no background-coloured holes |
| Typography | Real font outlines with consistent weight and scale |
| Review | 16, 20, 24, 32px, plus enlarged views and both polarities |
| Output | SVG, preview, README, manifest, and a ZIP for sets |

Family-wide consistency takes priority over literal repetition of every token. All sixteen samples use the same 1.5-unit outline weight. Dense symbols are best at 24px or larger; the smaller previews scale the same master. The full prompt explains optical corrections, numeral spacing, accessibility, and reference simplification.

## Samples

The pack explores identity, radio astronomy, seed storage, tape, tidal power, fungi, orbital hardware, rail, field recording, trails, fermentation, kites, microscopy, book exchange, and download/confirmation controls. The banner and ZIP use the same sixteen source SVGs.

Inline SVGs inherit CSS `color`. When using an SVG as an image file, set its colour in the SVG itself. The samples are decorative by default; label icon-only buttons on their parent control, and give meaningful standalone images accessible text.

## Contributing

For a new rule or geometry change, include a small before/after specimen at actual sizes in both polarities. Explain the problem it solves. Keep generated files independent of build-time helpers, and refresh affected previews and archives together.

## License

MIT. See [LICENSE](LICENSE). The skill, helpers, and sixteen sample icons are available for personal and commercial use under that license.
