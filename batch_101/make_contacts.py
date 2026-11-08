from pathlib import Path
import io
import subprocess
from PIL import Image

base = Path(__file__).parent
poppler = Path(r'C:\Users\GIGABAYT\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe')
out = base / 'figure_contacts'
out.mkdir(exist_ok=True)
for name, pages in [('01_simple_forex_balde.txt', [7, 8, 9, 11, 12, 13, 15])]:
    path = Path((base / name).read_text(encoding='utf-8').splitlines()[0].removeprefix('SOURCE: '))
    for page in pages:
        png = subprocess.check_output([str(poppler), '-f', str(page), '-l', str(page), '-scale-to', '1100', '-singlefile', '-png', str(path)])
        Image.open(io.BytesIO(png)).convert('RGB').save(out / f'{name.removesuffix(".txt")}_{page}.jpg', quality=85)
