import fontTools.ttLib.woff2 as wf2
import base64
import os
import re
from pathlib import Path

Current_dir = Path(__file__).parent
os.chdir(Current_dir)
files = Current_dir.rglob('css/*.css')

regxy = r"url\('data:application\/octet-stream;base64,(.+)'\) format"

for fll in files:
    fily = open(fll, 'r', encoding='utf-8')
    matches = re.finditer(regxy, fily.read(), re.MULTILINE)
    match = next(matches).group(1)
    debased = base64.b64decode(match)
    woff2 = Path(f'{Current_dir}/woff2/{fll.name}.woff2')
    open(woff2, 'wb').write(debased)
    otf = Path(f'{Current_dir}/otf/{fll.name}.otf')
    wf2.decompress(woff2, otf)

# fily = open('fily.txt', 'r', encoding='utf-8')
# daty = base64.b64decode(fily.read())
# open('fily.woff2', 'wb').write(daty)
# wf2.decompress('fily.woff2', 'fily.otf')

