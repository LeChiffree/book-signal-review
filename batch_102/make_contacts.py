from pathlib import Path
import io
import subprocess
from PIL import Image

base = Path(__file__).parent
poppler = Path(r'C:\Users\GIGABAYT\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe')
out = base / 'figure_contacts'
out.mkdir(exist_ok=True)
sets = [
    ('02_fifteen_minutes_ayuk.txt', [27, 28, 31, 32, 33, 35, 43, 44, 45, 46, 47]),
    ('03_four_steps_kelly.txt', [5, 7, 9, 13, 19, 22, 26, 33, 34, 35, 37]),
]
for name, pages in sets:
    path = Path((base / name).read_text(encoding='utf-8').splitlines()[0].removeprefix('SOURCE: '))
    for page in pages:
        png = subprocess.check_output([str(poppler), '-f', str(page), '-l', str(page), '-scale-to', '1100', '-singlefile', '-png', str(path)])
        Image.open(io.BytesIO(png)).convert('RGB').save(out / f'{name.removesuffix(".txt")}_{page}.jpg', quality=85)
