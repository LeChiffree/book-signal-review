import re
from pathlib import Path

source = Path(r"D:\Paper_ML_BSH\analysis\book_signal_review\batch_003\01_candles.txt")
text = source.read_text(encoding="utf-8")
parts = re.split(r"=== PDF PAGE (\d+) ===", text)
for number, body in zip(parts[1::2], parts[2::2]):
    if re.search(r"final rules|rules re-cap|Conclusions|test results \(5 day holding", body, re.I):
        print(f"\n### PDF PAGE {number}\n{body[:5000]}")
