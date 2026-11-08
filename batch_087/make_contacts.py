from pathlib import Path
import io
import subprocess
from PIL import Image, ImageDraw

base = Path(__file__).parent
poppler = Path(r'C:\Users\GIGABAYT\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe')
sets = [
    ('01_indicators.txt', [13, 23, 24]),
    ('02_daily_signals.txt', [21, 23, 52, 53]),
    ('03_robbinson.txt', [52, 53, 54, 55, 60, 63]),
]
out = base / 'figure_contacts'
out.mkdir(exist_ok=True)
for name, pages in sets:
    path = Path((base / name).read_text(encoding='utf-8').splitlines()[0].removeprefix('SOURCE: '))
    for page in pages:
        png = subprocess.check_output([str(poppler), '-f', str(page), '-l', str(page), '-scale-to', '1000', '-singlefile', '-png', str(path)])
        img = Image.open(io.BytesIO(png)).convert('RGB')
        img.save(out / f'{name.removesuffix(".txt")}_{page}.jpg', quality=85)
