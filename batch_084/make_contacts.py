from pathlib import Path
from subprocess import run
from PIL import Image, ImageDraw

base = Path(__file__).parent
out = base / "figure_contacts"
out.mkdir(exist_ok=True)
poppler = Path(r"C:\Users\GIGABAYT\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe")
books = {
    "sma_bb": (Path(r"D:\Paper_ML_BSH\Drive_PDF\PDFler\Baskı 18\Baskı 18\Basit Hareketli Ortalama (SMA) ve Bollinger Bantları Göstergelerinin Birlikte Kullanımıyla Günlük Traidng, Swing Trading ve Uzun Vadeli Yatırım Stratejileri - Aaron Lee Johnson (94 sayfa) - @eseckal.pdf"), [18, 20, 21, 25, 44, 45, 81, 82]),
    "rsi": (Path(r"D:\Paper_ML_BSH\Drive_PDF\PDFler\Baskı 18\Baskı 18\Gelişmiş RSI İndikatörü - Lalit Mohanty (75 sayfa) - @eseckal.pdf"), [9, 10, 12, 16, 21, 24, 28, 32, 40, 47]),
    "harmonic": (Path(r"D:\Paper_ML_BSH\Drive_PDF\PDFler\Baskı 8\Baskı 8\Harmonik Formasyonlar - Six000 (15 sayfa) - @eseckal.pdf"), list(range(1, 16))),
}
for name, (pdf, pages) in books.items():
    assert pdf.exists(), pdf
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
