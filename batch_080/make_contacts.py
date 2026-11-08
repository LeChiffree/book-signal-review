from pathlib import Path
from subprocess import run
from PIL import Image, ImageDraw

base = Path(__file__).parent
out = base / "figure_contacts"
out.mkdir(exist_ok=True)
poppler = Path(r"C:\Users\GIGABAYT\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe")
src = Path(r"D:\Paper_ML_BSH\Drive_PDF\PDFler\Baskı 6\Baskı 6")
books = {
    "masters": (src / "Price Action - Market Masters Academy (89 sayfa) - @eseckal.pdf", [15, 18, 19, 20, 21, 25, 26, 27, 28, 36, 40, 43, 47, 48, 51, 52, 53, 54, 55, 57, 58, 59, 60, 61, 65, 67, 69, 71, 72, 73, 74, 76, 80, 82, 87, 88, 89]),
    "dias": (src / "Price Action Kursu - Junior Dias (72 sayfa) - @eseckal.pdf", [18, 19, 22, 23, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 45, 46, 50, 53, 57, 58, 59, 64, 65]),
    "supply": (src / "Supply and Demand Eğitim Kursu (94 sayfa) - @eseckal.pdf", [5, 6, 7, 8, 9, 10, 18, 19, 22, 24, 25, 26, 29, 30, 31, 32, 33, 34, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 58, 59, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 73, 74, 75, 76, 77, 78, 79, 80, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94]),
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
