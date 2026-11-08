from pathlib import Path
from subprocess import run
from PIL import Image, ImageDraw

base = Path(__file__).parent
out = base / "figure_contacts"
out.mkdir(exist_ok=True)
poppler = Path(r"C:\Users\GIGABAYT\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe")
src = Path(r"D:\Paper_ML_BSH\Drive_PDF\PDFler\Baskı 6\Baskı 6")
books = {
    "santos": (src / "Price Action - Marcio Santos (37 sayfa) - @eseckal.pdf", list(range(11, 36))),
    "gap": (src / "Gap Trading (62 sayfa) - @eseckal.pdf", [1, 2, 4, 5, 7, 8, 9, 10, 11, 12, 14, 15, 58, 59, 60, 61, 62]),
    "unicorn": (src / "Unicorn Avantajı - Furqan Malick (TR-ENG) (56 sayfa) - @eseckal.pdf", [6, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 42, 43, 44, 46, 47, 48, 49, 50, 51, 52, 53, 54]),
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
