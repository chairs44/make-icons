#!/usr/bin/env python3
"""Check shipped SVGs and that the sample ZIP contains the current source files."""
from pathlib import Path
from zipfile import ZipFile
from specimen import read_svg

root = Path(__file__).resolve().parents[1]
samples = sorted((root / 'samples/icons').glob('*.svg'))
assert len(samples) == 16, 'Expected sixteen showcase samples'
for path in [*samples, *(root / 'assets/anchors').glob('*.svg')]:
    svg = read_svg(path)
    assert svg.get('viewBox') == '0 0 24 24', path.name
    assert 'currentColor' in path.read_text(), path.name
with ZipFile(root / 'make-icons-samples.zip') as archive:
    expected = {'icons/' + p.name for p in samples} | {'LICENSE', 'specimen.html'}
    assert set(archive.namelist()) == expected, 'Unexpected or missing ZIP contents'
    for path in samples:
        assert archive.read('icons/' + path.name) == path.read_bytes(), path.name
    assert archive.read('LICENSE') == (root / 'LICENSE').read_bytes()
    assert archive.read('specimen.html') == (root / 'samples/specimen.html').read_bytes()
print('Validated 24 SVGs and exact sample ZIP contents. Visual review is separate.')
