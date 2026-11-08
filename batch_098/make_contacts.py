from pathlib import Path
import io
import subprocess
from PIL import Image

base = Path(__file__).parent
poppler = Path(r'C:\Users\GIGABAYT\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe')
sets = [
    ('01_accumulation_momoh.txt', [19, 20, 21, 25, 27, 28, 33, 35]),
    ('03_day_trading_roy.txt', [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 39, 42, 43, 50, 51, 52, 53, 55, 59, 62, 64]),
]
out = base / 'figure_contacts'
out.mkdir(exist_ok=True)
for name, pages in sets:
    path = Path((base / name).read_text(encoding='utf-8').splitlines()[0].removeprefix('SOURCE: '))
    for page in pages:
        png = subprocess.check_output([str(poppler), '-f', str(page), '-l', str(page), '-scale-to', '1100', '-singlefile', '-png', str(path)])
        Image.open(io.BytesIO(png)).convert('RGB').save(out / f'{name.removesuffix(".txt")}_{page}.jpg', quality=85)
