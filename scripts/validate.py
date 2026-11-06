#!/usr/bin/env python3
"""Check shipped SVGs and that the sample ZIP contains the current source files."""
from pathlib import Path
from zipfile import ZipFile
from specimen import read_svg

root = Path(__file__).resolve().parents[1]
samples = sorted((root / 'samples/svg/24').glob('*.svg'))
assert len(samples) == 16, 'Expected sixteen showcase samples'
for path in [*samples, *(root / 'assets/outline-24').glob('*.svg')]:
    svg = read_svg(path)
    assert svg.get('viewBox') == '0 0 24 24', path.name
    assert 'currentColor' in path.read_text(), path.name
with ZipFile(root / 'make-icons-samples.zip') as archive:
    expected = {'svg/24/' + p.name for p in samples} | {'LICENSE', 'README.md', 'preview.html', 'manifest.json'}
    assert set(archive.namelist()) == expected, 'Unexpected or missing ZIP contents'
    for path in samples:
        assert archive.read('svg/24/' + path.name) == path.read_bytes(), path.name
    assert archive.read('LICENSE') == (root / 'LICENSE').read_bytes()
    assert archive.read('preview.html') == (root / 'samples/preview.html').read_bytes()
print('Validated 44 current-family SVGs and exact sample ZIP contents. Visual review is separate.')
