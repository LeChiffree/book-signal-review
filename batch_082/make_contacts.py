from pathlib import Path
from subprocess import run
from PIL import Image, ImageDraw

base = Path(__file__).parent
out = base / "figure_contacts"
out.mkdir(exist_ok=True)
poppler = Path(r"C:\Users\GIGABAYT\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe")
books = {
    "peloille": (Path(r"D:\Paper_ML_BSH\Drive_PDF\PDFler\Baskı 1\Baskı 1\Düşük Riskli Ichimoku Stratejisi Rehberi - Karen Peloille (162 sayfa) - @eseckal.pdf"), [6, 10, 11, 12, 28, 29, 38, 48, 54, 60, 61, 62, 69, 73, 75, 86, 90, 96, 97, 102]),
    "daytrade": (Path(r"D:\Paper_ML_BSH\Drive_PDF\PDFler\Baskı 11\Baskı 11\Day Trade Forex Sistemi (44 sayfa) - @eseckal.pdf"), [13, 15, 19, 20, 21, 25, 26, 29, 30, 38, 39, 40]),
    "swanson": (Path(r"D:\Paper_ML_BSH\Drive_PDF\PDFler\Baskı 11\Baskı 11\İşe Yarayan 5 Basit Trading Stratejisi - Jeff Swanson (61 sayfa) - @eseckal.pdf"), [7, 8, 9, 20, 21, 22, 26, 35, 37, 41, 42, 43, 44, 45, 48, 55]),
}
for name, (pdf, pages) in books.items():
    for start in range(0, len(pages), 12):
        sheet = Image.new("RGB", (1160, 1275), "white")
        draw = ImageDraw.Draw(sheet)
        for k, page in enumerate(pages[start:start+12]):
            stem = out / f"_{name}_{page}"
            run([str(poppler), "-f", str(page), "-l", str(page), "-scale-to", "760", "-singlefile", "-jpeg", str(pdf), str(stem)], check=True, capture_output=True)
            with Image.open(stem.with_suffix(".jpg")) as im:
                im.thumbnail((284, 400))
                x, y = (k % 4) * 290 + 3, (k // 4) * 425 + 18
                sheet.paste(im, (x, y))
                draw.text((x, y - 15), f"{name} p{page}", fill="black")
            stem.with_suffix(".jpg").unlink()
        dest = out / f"{name}_{start//12+1}.jpg"
        sheet.save(dest, quality=88)
        print(dest, flush=True)
