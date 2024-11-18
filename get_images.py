#!/usr/bin/env python3

from pathlib import Path
from shutil import copyfile
import unicodedata

from manimal.core import emojis, emojis_names

SRC_DIR = Path('/home/jurandy/Projetos/3rd/GoogleFonts/noto-emoji/png/512')
TMPL_IMG = 'emoji_u{code}.png'

for animal in emojis:
    name = unicodedata.name(animal).lower()
    if name in emojis_names:
        code = hex(ord(animal))[2:]
        src = SRC_DIR / TMPL_IMG.format(code=code)
        slug = name.replace(' ', '_')
        dst = Path(f'./images/{slug}.png')
        copyfile(src, dst)
        print(f'Copied {src} to {dst}')