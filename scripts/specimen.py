#!/usr/bin/env python3
"""Build a static SVG specimen, optional manifest and delivery ZIP (standard library only).

Recurses through the input directory. This parses SVG structure, not path geometry,
optical quality, component syntax, or accessibility of an eventual application.
"""
import argparse
from copy import deepcopy
from html import escape
import json
import math
from pathlib import Path
import re
import xml.etree.ElementTree as ET
from zipfile import ZipFile, ZIP_DEFLATED

ET.register_namespace('', 'http://www.w3.org/2000/svg')
ALLOWED = {'svg', 'path', 'circle', 'rect', 'ellipse', 'g', 'title', 'desc', 'polygon', 'polyline', 'line'}
SIZES = (16, 20, 24, 32)


def view_box(root):
    values = [float(v) for v in re.split(r'[\s,]+', root.get('viewBox', '').strip()) if v]
    if len(values) != 4 or not all(math.isfinite(v) for v in values) or min(values[2:]) <= 0:
        raise ValueError('viewBox must contain four finite numbers with positive width and height')
    return values


def read_svg(path):
    source = path.read_text(encoding='utf-8')
    if '<!DOCTYPE' in source.upper() or '<!ENTITY' in source.upper():
        raise ValueError(f'{path.name}: document types/entities are unsupported')
    root = ET.fromstring(source)
    if root.tag not in {'svg', '{http://www.w3.org/2000/svg}svg'}:
        raise ValueError(f'{path.name}: SVG root required')
    view_box(root)
    for element in root.iter():
        namespace, _, tag = element.tag.rpartition('}')
        if tag not in ALLOWED or (namespace and namespace != '{http://www.w3.org/2000/svg'):
            raise ValueError(f'{path.name}: unsupported element {element.tag}')
        for key, value in element.attrib.items():
            local = key.split('}')[-1].lower()
            if local.startswith('on') or local in {'href', 'style'} or 'url(' in value.lower():
                raise ValueError(f'{path.name}: embedded behavior/references are unsupported')
        # The repeated preview samples are decorative. Original source files stay untouched.
        for key in ('id', 'aria-labelledby', 'aria-describedby'):
            element.attrib.pop(key, None)
    return root


def render(root, size):
    clone = deepcopy(root)
    _, _, width, height = view_box(root)
    clone.set('width', f'{size * width / height:g}')
    clone.set('height', str(size))
    clone.set('aria-hidden', 'true')
    clone.set('focusable', 'false')
    return ET.tostring(clone, encoding='unicode')


def make_html(icons, directory, title):
    cards, dark = [], []
    for path, root in icons:
        name = escape(path.relative_to(directory).as_posix())
        box = escape(root.get('viewBox'))
        samples = ''.join(f'<div>{render(root, size)}<small>{size}px</small></div>' for size in SIZES)
        cards.append(f'<article><h2>{name}</h2><p class="native">Native viewBox: {box}</p>'
                     f'<div class="large">{render(root, 72)}</div><div class="sizes">{samples}</div>'
                     f'<p class="inline">{render(root, 24)}<span>Example text</span></p></article>')
        dark.append(f'<article><h2>{name}</h2><div class="sizes">{samples}</div></article>')
    title = escape(title)
    return '''<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>'''+title+'''</title><style>
*{box-sizing:border-box}body{margin:0;background:#fff;color:#171717;font:16px/1.5 Arial,sans-serif}
main{max-width:1200px;margin:auto;padding:32px}header{margin-bottom:32px}h1{font-size:28px;font-weight:500;margin:0 0 12px}
h2{font-size:16px;font-weight:400;overflow-wrap:anywhere;margin:0 0 8px}header p{max-width:72ch}
.grid,.dark{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(240px,100%),1fr));gap:32px}
article{min-width:0;border-top:1px solid #ccc;padding-top:20px}.native{font-size:12px;color:#666;margin:0 0 12px}
.large{min-height:88px;display:flex;align-items:center;overflow:auto}.sizes{display:flex;gap:22px;align-items:flex-start;margin-top:16px;flex-wrap:wrap}
.sizes>div{height:62px;display:flex;flex-direction:column;align-items:center;justify-content:space-between}
small{font-size:12px;color:#666}svg{display:block;flex-shrink:0;max-width:100%}.inline{display:flex;align-items:center;gap:12px}
.dark{background:#292929;color:#f5f5f5;padding:24px;margin-top:40px}.dark small{color:#ccc}.dark article{border-color:#666}
@media(max-width:500px){main{padding:24px 20px}.grid,.dark{grid-template-columns:1fr}.dark{padding:20px}}
</style></head><body><main><header><h1>'''+title+'''</h1>
<p>Each file is one native drawing. Samples show it at 16/20/24/32px display height, plus a 72px detail. Scaled samples are not separately tuned optical masters.</p>
</header><section class="grid" aria-label="Dark icons on light">'''+''.join(cards)+'''</section>
<section class="dark" aria-label="Light icons on dark">'''+''.join(dark)+'''</section></main></body></html>'''


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('directory', type=Path, help='SVG directory; nested native-size folders are supported')
    parser.add_argument('--output', type=Path, required=True, help='Destination HTML file')
    parser.add_argument('--title', default='Icon specimen')
    parser.add_argument('--manifest', type=Path, help='Optional JSON next to the HTML; SVGs must be under that delivery root')
    parser.add_argument('--zip', dest='archive', type=Path, help='ZIP including SVGs, HTML, optional manifest and --include files')
    parser.add_argument('--include', type=Path, action='append', default=[], help='Additional delivery file/directory under the HTML parent; repeatable; requires --zip')
    args = parser.parse_args()
    try:
        directory = args.directory.resolve()
        output = args.output.resolve()
        delivery_root = output.parent
        files = sorted(p for p in directory.rglob('*.svg') if not any(x.startswith('.') for x in p.relative_to(directory).parts))
        if not files:
            raise ValueError('No SVG files found')
        if any(p.is_symlink() or not p.resolve().is_relative_to(directory) for p in files):
            raise ValueError('SVG inputs must be regular files within the input directory')
        icons = [(p, read_svg(p)) for p in files]
        manifest_path = args.manifest.resolve() if args.manifest else None
        archive_path = args.archive.resolve() if args.archive else None
        destinations = [p for p in (output, manifest_path, archive_path) if p]
        if len(set(destinations)) != len(destinations) or set(destinations) & {p.resolve() for p in files}:
            raise ValueError('Output, manifest, ZIP and source SVG paths must be distinct')
        if manifest_path and (manifest_path.parent != delivery_root or not directory.is_relative_to(delivery_root)):
            raise ValueError('--manifest must be beside the HTML, with the SVG directory inside that delivery root')
        if args.include and not archive_path:
            raise ValueError('--include requires --zip')
        extras = []
        for requested in args.include:
            if requested.is_symlink() or not requested.exists():
                raise ValueError(f'Include must exist and not be a symlink: {requested}')
            candidates = sorted(requested.rglob('*')) if requested.is_dir() else [requested]
            for p in candidates:
                if not p.is_file() or any(x.startswith('.') or x == '__pycache__' for x in p.relative_to(requested.parent).parts):
                    continue
                if p.is_symlink() or not p.resolve().is_relative_to(delivery_root):
                    raise ValueError(f'Include must remain within the delivery root: {p}')
                if p.resolve() in destinations:
                    raise ValueError('Do not include generated outputs or the archive itself using --include')
                extras.append(p.resolve())
        html = make_html(icons, directory, args.title)
        manifest = None
        if manifest_path:
            entries = []
            for p, root in icons:
                name, variant = p.stem, None
                for suffix in ('-outline', '-solid'):
                    if name.endswith(suffix):
                        name, variant = name[:-len(suffix)], suffix[1:]
                        break
                box = view_box(root)
                entries.append({'name': name, 'variant': variant, 'native_size': box[2] if box[:2] == [0, 0] and box[2] == box[3] else None,
                                'view_box': box, 'file': p.relative_to(delivery_root).as_posix(),
                                'checks': {'xml_parsed': True, 'rendered_review': 'not_performed_by_helper', 'optical_review': 'not_performed_by_helper'}})
            manifest = json.dumps({'schema_version': 1, 'icons': entries}, indent=2) + '\n'
        # Plan archive entries before writing any files so invalid includes/collisions fail cleanly.
        archive_files = {}
        if archive_path:
            for p in files:
                name = p.relative_to(delivery_root).as_posix() if p.is_relative_to(delivery_root) else 'svg/' + p.relative_to(directory).as_posix()
                archive_files[name] = p
            for p in extras:
                archive_files[p.relative_to(delivery_root).as_posix()] = p
            generated = [output.name] + ([manifest_path.name] if manifest_path else [])
            if any(name in archive_files for name in generated):
                raise ValueError('Generated filename collides with an archive source')
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(html, encoding='utf-8')
        if manifest_path:
            manifest_path.write_text(manifest, encoding='utf-8')
        if archive_path:
            archive_path.parent.mkdir(parents=True, exist_ok=True)
            with ZipFile(archive_path, 'w', ZIP_DEFLATED) as archive:
                for name, p in sorted(archive_files.items()):
                    archive.write(p, name)
                archive.writestr(output.name, html)
                if manifest_path:
                    archive.writestr(manifest_path.name, manifest)
    except (ValueError, OSError, ET.ParseError) as exc:
        parser.error(str(exc))
    print(f'Parsed {len(icons)} SVGs. Wrote {output}. Rendered and optical review remain separate.')


if __name__ == '__main__':
    main()
