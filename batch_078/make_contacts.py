from pathlib import Path
from subprocess import run
from PIL import Image, ImageDraw

base = Path(__file__).parent
contact_dir = base / "figure_contacts"
contact_dir.mkdir(exist_ok=True)
poppler = Path(r"C:\Users\GIGABAYT\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe")
sources = {
    "sikorski": (r"D:\Paper_ML_BSH\Drive_PDF\PDFler\Baskı 6\Baskı 6\Trading Stratejileri - Simon Sikorski (148 sayfa) - @eseckal.pdf", [10, 27, 28, 29, 34, 35, 65, 79, 81, 82, 88, 91, 101, 112, 116, 121, 122, 127, 137, 138]),
    "oleg": (r"D:\Paper_ML_BSH\Drive_PDF\PDFler\Baskı 6\Baskı 6\Uyumsuzluklar - Oleg A. But (34 sayfa) - @eseckal.pdf", [3, 14, 15, 16, 17, 18, 19, 20, 23, 24, 27, 28, 29, 30]),
    "king": (r"D:\Paper_ML_BSH\Drive_PDF\PDFler\Baskı 6\Baskı 6\Price Action - James Jecool King (53 sayfa) - @eseckal.pdf", list(range(4, 19)) + list(range(20, 50))),
}
for name, (source, pages) in sources.items():
    for start in range(0, len(pages), 12):
        selection = pages[start:start + 12]
        sheet = Image.new("RGB", (4 * 290, 3 * 425), "white")
        draw = ImageDraw.Draw(sheet)
        for k, page in enumerate(selection):
            stem = contact_dir / f"_{name}_{page}"
            run([str(poppler), "-f", str(page), "-l", str(page), "-scale-to", "760", "-singlefile", "-jpeg", source, str(stem)], check=True, capture_output=True)
            with Image.open(stem.with_suffix(".jpg")) as im:
                im.thumbnail((284, 400))
                x, y = (k % 4) * 290 + 3, (k // 4) * 425 + 18
                sheet.paste(im, (x, y))
                draw.text((x, y - 15), f"{name} p{page}", fill="black")
            stem.with_suffix(".jpg").unlink()
        sheet.save(contact_dir / f"{name}_{start // 12 + 1}.jpg", quality=88)
        print(contact_dir / f"{name}_{start // 12 + 1}.jpg", flush=True)
