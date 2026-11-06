#!/usr/bin/env python3
"""Write an offline reference/output comparison. No visual verdict is computed."""
import argparse
import base64
import html
import mimetypes
from pathlib import Path
from specimen import read_svg

def data_uri(path):
    mime = mimetypes.guess_type(path.name)[0]
    if mime not in {'image/png', 'image/jpeg', 'image/webp', 'image/svg+xml'}:
        raise ValueError('Use PNG, JPEG, WebP, or SVG references')
    if mime == 'image/svg+xml':
        read_svg(path)
    return 'data:' + mime + ';base64,' + base64.b64encode(path.read_bytes()).decode()

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('reference', type=Path)
    p.add_argument('svg', type=Path)
    p.add_argument('--output', type=Path, required=True)
    args = p.parse_args()
    if args.output.resolve() in {args.reference.resolve(), args.svg.resolve()}:
        p.error('Output must not overwrite an input')
    read_svg(args.svg)
    ref, out = data_uri(args.reference), data_uri(args.svg)
    title = html.escape(args.svg.stem)
    page = '''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Reference review</title>
<style>body{font:16px system-ui;margin:24px;background:#f5f4f0;color:#30302e}main{max-width:1000px;margin:auto}.row{display:flex;flex-wrap:wrap;gap:20px}figure{margin:0;flex:1;min-width:220px}figcaption{padding:12px 0}.stage{height:260px;position:relative;background:#ddd;border:1px solid #aaa;overflow:hidden}.stage img{position:absolute;width:200px;height:200px;object-fit:contain;left:50%;top:50%;transform:translate(-50%,-50%)}label{display:block;margin:16px 0}input{max-width:100%}.sizes{display:flex;align-items:center;gap:24px;padding:24px;background:white}.dark{background:#171717;color:white}.sizes img{filter:none}.dark img{filter:invert(1)}p{line-height:1.5;max-width:75ch}</style>
<main><h1>__TITLE__</h1><p>Reference, output, and overlay. Fit boxes preserve aspect ratio but do not automatically align ink bounds. Adjust uniform scale and translation for comparison; do not use alignment to hide proportion differences. No similarity score or approval is implied.</p><div class="row"><figure><div class="stage"><img alt="Reference" src="__REF__"></div><figcaption>Reference</figcaption></figure><figure><div class="stage"><img alt="Output" src="__OUT__"></div><figcaption>Output</figcaption></figure><figure><div class="stage"><img alt="Reference underlay" src="__REF__"><img id="over" alt="Output overlay" src="__OUT__" style="opacity:.5"></div><figcaption>Overlay</figcaption></figure></div>
<label><input id="invert" type="checkbox"> Invert overlay output for a light reference on dark</label><label>Output scale <input id="scale" type="range" min=".25" max="3" step=".01" value="1"></label><label>Horizontal shift <input id="x" type="range" min="-100" max="100" value="0"></label><label>Vertical shift <input id="y" type="range" min="-100" max="100" value="0"></label><label>Output opacity <input id="opacity" type="range" min="0" max="1" step=".05" value=".5"></label><p>24-unit master displayed at 16, 20, 24, and 32px. These are scaled displays, not independent optical variants.</p>__SIZES__<p>Check subject and variant; attachments and crossing order; silhouette and terminals; native-size clarity. Record unresolved differences before delivery.</p></main>
<script>const ids=['scale','x','y','opacity'];function update(){const v=Object.fromEntries(ids.map(id=>[id,Number(document.getElementById(id).value)]));const el=document.getElementById('over');el.style.transform=`translate(calc(-50% + ${v.x}px),calc(-50% + ${v.y}px)) scale(${v.scale})`;el.style.opacity=v.opacity}ids.forEach(id=>document.getElementById(id).addEventListener('input',update));document.getElementById('invert').addEventListener('change',event=>document.getElementById('over').style.filter=event.target.checked?'invert(1)':'none');</script></html>'''
    sizes = ''.join('<div class="sizes '+mode+'">'+''.join(f'<img alt="{n}px output" width="{n}" height="{n}" src="{out}">' for n in [16,20,24,32])+'</div>' for mode in ['', 'dark'])
    page = page.replace('__TITLE__',title).replace('__REF__',ref).replace('__OUT__',out).replace('__SIZES__',sizes)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(page)
    print(args.output)

if __name__ == '__main__':
    main()
