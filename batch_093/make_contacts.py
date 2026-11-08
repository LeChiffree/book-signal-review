from pathlib import Path
import io
import subprocess
from PIL import Image

base = Path(__file__).parent
poppler = Path(r'C:\Users\GIGABAYT\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe')
sets = [
    ('01_professional_system.txt', [13, 14, 15, 17, 19]),
    ('02_hundred_dollars.txt', [21, 25, 33]),
    ('03_patterns_price_action.txt', [18, 19, 25, 29, 31, 37, 42, 44, 49, 56, 57, 58]),
]
out = base / 'figure_contacts'
out.mkdir(exist_ok=True)
for name, pages in sets:
    path = Path((base / name).read_text(encoding='utf-8').splitlines()[0].removeprefix('SOURCE: '))
    for page in pages:
        png = subprocess.check_output([str(poppler), '-f', str(page), '-l', str(page), '-scale-to', '1100', '-singlefile', '-png', str(path)])
        Image.open(io.BytesIO(png)).convert('RGB').save(out / f'{name.removesuffix(".txt")}_{page}.jpg', quality=85)
