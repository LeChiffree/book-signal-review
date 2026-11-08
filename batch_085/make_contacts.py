from pathlib import Path
import io
import subprocess
from PIL import Image, ImageDraw

base = Path(__file__).parent
poppler = Path(r'C:\Users\GIGABAYT\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe')
sets = [
    ('01_authentic_fx.txt', [6, 14, 19, 23, 26, 30, 33, 35, 39, 41, 42, 43]),
    ('02_edmund_loh.txt', [14, 21, 25, 33]),
    ('03_keaton_indicators.txt', [11, 18, 21, 23, 27, 55, 58, 60, 63, 65, 68, 71, 73, 75]),
]
out = base / 'figure_contacts'
out.mkdir(exist_ok=True)
for name, pages in sets:
    path = Path((base / name).read_text(encoding='utf-8').splitlines()[0].removeprefix('SOURCE: '))
    tiles = []
    for page in pages:
        png = subprocess.check_output([str(poppler), '-f', str(page), '-l', str(page), '-scale-to', '580', '-singlefile', '-png', str(path)])
        img = Image.open(io.BytesIO(png)).convert('RGB')
        tile = Image.new('RGB', (620, 845), 'white')
        tile.paste(img, ((620-img.width)//2, 25))
        ImageDraw.Draw(tile).text((10, 5), f'{name} PDF page {page}', fill='black')
        tiles.append(tile)
    for offset in range(0, len(tiles), 8):
        group = tiles[offset:offset+8]
        sheet = Image.new('RGB', (620*4, 845*2), 'white')
        for idx, tile in enumerate(group):
            sheet.paste(tile, ((idx%4)*620, (idx//4)*845))
        sheet.save(out / f'{name.removesuffix(".txt")}_{offset//8+1}.jpg', quality=83)
