# Drawing references

`../assets/outline-24/` contains ten original editable SVG examples on a 24-unit grid with a 1.5-unit stroke. The same files are supplied in the sample pack. Use them with [construction.md](construction.md), not as a substitute for the requested subject or visual reference.

| Construction decision | Examples |
| --- | --- |
| Continuous body, short corner transitions, inset opening | `home-outline.svg` |
| Wide container and a centered identifying detail | `camera-outline.svg` |
| Curved arch with connected parts and shared-edge ownership | `headphones-outline.svg` |
| Tapered organic contours and intentional asymmetry | `plant-outline.svg` |
| Concave cutouts and separated internal marks | `ticket-outline.svg` |
| Narrow upright mass and a single page-block boundary | `book-outline.svg` |
| Curved body and attached handle | `coffee-cup-outline.svg` |
| Matched loops and an interrupted rear member | `scissors-outline.svg` |
| Curved shoulders and a restrained inset detail | `backpack-outline.svg` |
| Nested contours and compact identifying details | `cassette-outline.svg` |

Inspect actual SVG coordinates, then compare at the intended display sizes. Match apparent weight and subject proportions rather than copying one bounding box. Draw only the requested inventory. Do not treat these examples as fixed templates for all subjects or claim user approval for future adaptations.

The examples are scalable 24-unit masters. Their 16/20px previews are resized displays, not independent optical drawings. Cassette reel details and narrow handle openings need particular care at 16px. Review a compact native master separately when the target requires dense small UI.

Files use currentColor and true transparent negative space. The decorative SVG defaults require accessible labels on meaningful images or their parent controls. No external icon collections, screenshots, application code, or font files are bundled.

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
