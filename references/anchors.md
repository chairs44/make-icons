# Drawing references

## Current outline family

`../assets/outline-24/` contains 28 original 24-unit drawings. They use a nominal 1.5-unit stroke and were reviewed as a family in two Paper studies. The style direction was accepted; this is not a certification of every possible size, export, or future adaptation. Do not bundle this whole bank when a user requests only a few icons.

| Structure to study | Relevant files in `assets/outline-24/` |
|---|---|
| Container and subject proportions | `home-outline.svg`, `book-outline.svg`, `email-outline.svg`, `image-outline.svg` |
| Simple circles and directional lines | `search-outline.svg`, `arrow-right-outline.svg`, `external-link-outline.svg`, `plus-circle-outline.svg`, `check-circle-outline.svg`, `sun-outline.svg` |
| Media controls and numeral spacing | `play-outline.svg`, `pause-outline.svg`, `back-15-outline.svg`, `forward-30-outline.svg` |
| Curves and nested outlines | `headphones-outline.svg`, `microphone-outline.svg`, `podcast-outline.svg`, `focus-head-outline.svg` |
| Organic and asymmetric contours | `plant-outline.svg`, `palette-outline.svg`, `plane-outline.svg` |
| Object construction and connected parts | `flask-outline.svg`, `cart-outline.svg`, `shield-outline.svg`, `dumbbell-outline.svg`, `noodles-outline.svg`, `chip-outline.svg`, `scissors-outline.svg` |

Read the actual SVGs for coordinates. Use the supplied drawing directly when it matches the requested symbol, or adapt its structural decisions to a new symbol. Do not copy a reference's bounding box onto an unrelated shape. Return only the requested assets.

The back-15 and forward-30 numeral contours were retained from earlier font-based anchors; their rings and arrowheads were redrawn for this family. The glyphs are fixed path data, not a bundled font or a mechanism for generating arbitrary labels. For other labels, use an available suitable font and record its source in working notes. Podcast and numbered controls have dense detail at 16px; use native compact-size review before promising legibility at that size.

The focus-head drawing is a conceptual head with a focus marker. It is not a faithful reproduction of a specific brand or of the headset-equipped reference. An explicitly supplied reference always needs its own identity check.

The reference bank contains editable original drawings. External asset collections, screenshots, and private application code are not included.

## Previous solid family

`../assets/legacy-solid/` preserves these eight earlier assets byte-for-byte:

- Home, play, pause: solid and outline versions.
- Back 15 and forward 30: solid-family controls with the earlier heavier ring treatment.

Use these only to maintain or explicitly match an existing legacy set. They do not define the new 1.5-unit outline family. Keep their original geometry when the user's task is preservation rather than restyling.

## Specimen helper

Run the helper from the skill directory or use its absolute path. The command below assumes the requested icons have already been written under a separate delivery folder and its README exists:

```bash
python3 scripts/specimen.py /path/to/delivery/svg \
  --output /path/to/delivery/preview.html \
  --manifest /path/to/delivery/manifest.json \
  --zip /path/to/delivery/icons.zip \
  --include /path/to/delivery/README.md
```

Add another `--include` for a requested component directory inside the same delivery folder. These paths are illustrative; use the user's actual destination. For a simple specimen without a manifest/archive, only `directory` and `--output` are required.

The helper recursively reads `.svg` files and retains native-folder distinctions. It parses XML, checks basic shape elements/viewBoxes, and rejects embedded behavior/external references. It cannot prove that path data renders correctly. It leaves source files unchanged. Generated manifests explicitly mark rendered/optical review as unperformed by the helper; update those statuses only after actual inspection. Review display samples are labelled separately from native drawing size.

With `--manifest`, keep the SVG input directory inside the HTML's parent folder and the JSON beside the HTML so relative paths are valid both locally and in the ZIP. Use an isolated delivery folder. `--include` is explicit; the helper does not automatically scoop up working files or private references. The default review sizes are fixed at 16/20/24/32px plus 72px detail; if other review sizes or custom interactions are requested, adapt the generated specimen rather than pretending this helper supports them automatically.
