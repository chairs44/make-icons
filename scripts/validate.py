#!/usr/bin/env python3
"""Check current SVG examples, banner sources, manifests, links, and sample ZIP."""
import json
import re
import struct
import xml.etree.ElementTree as ET
from pathlib import Path
from zipfile import ZipFile
from specimen import read_svg

root = Path(__file__).resolve().parents[1]
inventory = json.loads((root / 'samples/inventory.json').read_text())
assert len(inventory) == len(set(inventory)) == 10, 'Expected ten distinct showcase names'
expected_names = {name + '-outline.svg' for name in inventory}
samples = root / 'samples/svg/24'
anchors = root / 'assets/outline-24'
assert {p.name for p in samples.glob('*.svg')} == expected_names
assert {p.name for p in anchors.glob('*.svg')} == expected_names
for name in expected_names:
    path = samples / name
    svg = read_svg(path)
    assert svg.get('viewBox') == '0 0 24 24', name
    assert svg.get('width') == svg.get('height') == '24', name
    assert svg.get('stroke-width') == '1.5', name
    assert svg.get('stroke') == 'currentColor' and svg.get('fill') == 'none', name
    assert path.read_bytes() == (anchors / name).read_bytes(), name

banner = ET.parse(root / 'docs/make-icons-showcase.svg').getroot()
ns = '{http://www.w3.org/2000/svg}'
children = banner.findall(ns + 'svg')
assert len(children) == 10
for index, (name, item) in enumerate(zip(inventory, children)):
    assert item.get('x') == str(84 + index % 5 * 240)
    assert item.get('y') == str(74 + index // 5 * 220)
    assert item.get('width') == item.get('height') == '72'
    item.attrib.pop('x'); item.attrib.pop('y')
    item.set('width', '24'); item.set('height', '24')
    normalized = ET.fromstring(ET.tostring(item, encoding='unicode').replace('#41413E', 'currentColor'))
    source = ET.parse(samples / (name + '-outline.svg')).getroot()
    assert ET.tostring(normalized) == ET.tostring(source), name
png = (root / 'docs/make-icons-showcase.png').read_bytes()
assert png[:8] == b'\x89PNG\r\n\x1a\n'
assert struct.unpack('>II', png[16:24]) == (1200, 440)

manifest = json.loads((root / 'samples/manifest.json').read_text())
assert {item['name'] for item in manifest['icons']} == set(inventory)
for item in manifest['icons']:
    assert item['file'] == 'svg/24/' + item['name'] + '-outline.svg'
    assert item['view_box'] == [0, 0, 24, 24]

with ZipFile(root / 'make-icons-samples.zip') as archive:
    expected = {'svg/24/' + name for name in expected_names} | {'LICENSE', 'README.md', 'preview.html', 'manifest.json'}
    assert set(archive.namelist()) == expected, 'Unexpected or missing ZIP contents'
    for name in expected:
        source = root / 'LICENSE' if name == 'LICENSE' else root / 'samples' / name
        assert archive.read(name) == source.read_bytes(), name

for doc in [root / 'README.md', root / 'SKILL.md', *(root / 'references').glob('*.md')]:
    for link in re.findall(r'\]\(([^)]+)\)', doc.read_text()):
        if '://' not in link and not link.startswith('#'):
            assert (doc.parent / link.split('#')[0]).exists(), (doc.name, link)
    assert not re.search(r'/Users/|app\.paper\.design/file/', doc.read_text(), re.I), doc
print('Validated ten sample/anchor pairs, exact banner SVG sources, PNG dimensions, manifest, complete ZIP contents, and documentation links. Visual review is separate.')
