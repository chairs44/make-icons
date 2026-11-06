#!/usr/bin/env python3
"""Build a self-contained static SVG specimen using only Python's standard library."""
import argparse
from copy import deepcopy
from html import escape
from pathlib import Path
import xml.etree.ElementTree as ET
from zipfile import ZipFile, ZIP_DEFLATED

ET.register_namespace('', 'http://www.w3.org/2000/svg')
ALLOWED = {'svg', 'path', 'circle', 'rect', 'ellipse', 'g', 'title', 'desc', 'polygon', 'polyline', 'line'}

def read_svg(path):
    source = path.read_text(encoding='utf-8')
    if '<!DOCTYPE' in source.upper() or '<!ENTITY' in source.upper():
        raise ValueError(f'{path.name}: XML declarations/entities are unsupported')
    root = ET.fromstring(source)
    if root.tag.split('}')[-1] != 'svg' or not root.get('viewBox'):
        raise ValueError(f'{path.name}: SVG root and viewBox required')
    for element in root.iter():
        if element.tag.split('}')[-1] not in ALLOWED:
            raise ValueError(f'{path.name}: unsupported element {element.tag}')
        for key, value in element.attrib.items():
            local = key.split('}')[-1].lower()
            if local.startswith('on') or local in {'href', 'style'} or 'url(' in value.lower():
                raise ValueError(f'{path.name}: unsupported embedded behavior/reference')
        # The preview repeats icons; decorative samples do not need source title IDs.
        element.attrib.pop('id', None)
        element.attrib.pop('aria-labelledby', None)
        element.attrib.pop('aria-describedby', None)
    return root

def render(root, size):
    clone = deepcopy(root)
    clone.set('width', str(size)); clone.set('height', str(size))
    clone.set('aria-hidden', 'true'); clone.set('focusable', 'false')
    return ET.tostring(clone, encoding='unicode')

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('directory', type=Path, help='Directory containing standalone SVG files')
    parser.add_argument('--output', type=Path, required=True, help='Destination HTML file')
    parser.add_argument('--zip', dest='archive', type=Path, help='Optional ZIP destination')
    parser.add_argument('--title', default='Icon specimen')
    args = parser.parse_args()
    files = sorted(args.directory.glob('*.svg'))
    if not files:
        parser.error('No SVG files found')
    try:
        icons = [(path, read_svg(path)) for path in files]
    except (ValueError, ET.ParseError) as exc:
        parser.error(str(exc))
    rows = []
    dark = []
    for path, root in icons:
        name = escape(path.stem)
        sizes = ''.join(f'<div>{render(root,s)}<small>{s}px</small></div>' for s in (16,20,24,32))
        rows.append(f'<article><h2>{name}</h2><div class="large">{render(root,72)}</div><div class="sizes">{sizes}</div><p class="inline">{render(root,24)}<span>Example text</span></p></article>')
        dark.append(f'<div class="inline">{render(root,24)}<span>{name}</span></div>')
    title = escape(args.title)
    html = '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'''+title+'''</title><style>
*{box-sizing:border-box}body{margin:0;background:#f7f7f2;color:#171716;font:16px/1.5 Arial,sans-serif}main{max-width:1100px;margin:auto;padding:32px}h1{font-size:28px;font-weight:500;margin:0 0 12px}h2{font-size:16px;font-weight:400;overflow-wrap:anywhere;margin:0 0 16px}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:32px}article{border-top:1px solid #b7b7af;padding-top:20px}.large{height:88px;display:flex;align-items:center}.sizes{display:flex;gap:22px;align-items:flex-start;margin-top:20px}.sizes>div{height:62px;display:flex;flex-direction:column;align-items:center;justify-content:space-between}small{font-size:12px;color:#62625c}svg{display:block;flex-shrink:0}.inline{display:flex;align-items:center;gap:12px}.dark{background:#171716;color:#f7f7f2;padding:24px;margin-top:32px;display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:24px}.dark span{overflow-wrap:anywhere}header{margin-bottom:32px}header p{max-width:68ch}@media(max-width:500px){main{padding:24px 20px}.grid{grid-template-columns:1fr}.dark{grid-template-columns:1fr;padding:20px}}
</style></head><body><main><header><h1>'''+title+'''</h1><p>Solid and outline construction at actual sizes. Enlarged views expose geometry; small views test recognition.</p></header><div class="grid">'''+''.join(rows)+'''</div><section class="dark" aria-label="Light icons on dark">'''+''.join(dark)+'''</section></main></body></html>'''
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(html, encoding='utf-8')
    if args.archive:
        args.archive.parent.mkdir(parents=True, exist_ok=True)
        with ZipFile(args.archive, 'w', ZIP_DEFLATED) as archive:
            for path in files:
                archive.write(path, 'icons/'+path.name)
    print(f'Parsed {len(files)} SVGs. Wrote {args.output}. Rendered inspection remains separate.')

if __name__ == '__main__':
    main()
