from pathlib import Path
from subprocess import run
from PIL import Image, ImageDraw

base = Path(__file__).parent
out = base / "figure_contacts"
out.mkdir(exist_ok=True)
poppler = Path(r"C:\Users\GIGABAYT\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe")
src = Path(r"D:\Paper_ML_BSH\Drive_PDF\PDFler\Baskı 6\Baskı 6")
books = {
    "alpha": (src / "Price Action Stratejileri - Alpha FX (80 sayfa) - @eseckal.pdf", [9, 10, 11, 12, 15, 16, 17, 18, 19, 20, 21, 22, 24, 25, 28, 29, 30, 31, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 46, 47, 48, 49, 52, 53, 54, 55, 57, 58, 60, 61, 64, 65, 66, 67, 68, 70, 71, 72, 73, 74, 76, 77, 78]),
    "sdguide": (src / "Supply and Demand Kılavuzu (28 sayfa) - @eseckal.pdf", list(range(1, 27))),
    "rekt": (src / "Teknik Analiz Kursu - Rekt Proof (83 sayfa) - @eseckal.pdf", [2, 3, 4, 5, 6, 7, 9, 11, 12, 13, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 52, 53, 54, 55, 56, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 77, 78, 79, 80, 81, 82, 83]),
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
