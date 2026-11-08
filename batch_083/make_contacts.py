from pathlib import Path
from subprocess import run
from PIL import Image, ImageDraw

base = Path(__file__).parent
out = base / "figure_contacts"
out.mkdir(exist_ok=True)
poppler = Path(r"C:\Users\GIGABAYT\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe")
books = {
    "ayuk": (Path(r"D:\Paper_ML_BSH\Drive_PDF\PDFler\Baskı 12\Baskı 12\Kazançlı Günlük Trading Stratejisi - Caroline Ayuk (80 sayfa) - @eseckal.pdf"), [31,33,34,36,42,48,49,50,51,52,56,61]),
    "williams": (Path(r"D:\Paper_ML_BSH\Drive_PDF\PDFler\Baskı 10\Baskı 10\Basit Forex Trading Formülleri - Billy Williams (113 sayfa) - @eseckal.pdf"), [44,45,49,52,53,54,55,94,97,98,103,105,106]),
    "secrets": (Path(r"D:\Paper_ML_BSH\Drive_PDF\PDFler\Baskı 10\Baskı 10\Açığa Çıkan Trading Sırları (61 sayfa) - @eseckal.pdf"), [21,22,28,30,31,38,39,42,44,47,51,57]),
}
for name, (pdf, pages) in books.items():
    for start in range(0, len(pages), 12):
        sheet = Image.new("RGB", (1160, 1275), "white")
        draw = ImageDraw.Draw(sheet)
        for k, page in enumerate(pages[start:start + 12]):
            stem = out / f"_{name}_{page}"
            run([str(poppler), "-f", str(page), "-l", str(page), "-scale-to", "760", "-singlefile", "-jpeg", str(pdf), str(stem)], check=True, capture_output=True)
            with Image.open(stem.with_suffix(".jpg")) as im:
                im.thumbnail((284, 400))
                x, y = (k % 4) * 290 + 3, (k // 4) * 425 + 18
                sheet.paste(im, (x, y))
                draw.text((x, y - 15), f"{name} p{page}", fill="black")
            stem.with_suffix(".jpg").unlink()
        dest = out / f"{name}_{start // 12 + 1}.jpg"
        sheet.save(dest, quality=88)
        print(dest, flush=True)
