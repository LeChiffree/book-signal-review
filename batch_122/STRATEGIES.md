# Kitap okuma 122 — açılış aralığı ve Darvas kutusunun tekrar değerlendirmesi

**Kapsam:** Üç ayrı PDF'nin **27 + 30 + 42 = 99 sayfası** baştan sona okundu. Atıflar PDF sayfasıdır. Backtest, paper test ve emir yapılmadı.

## 1. Larry Gaines — Haftalık Opsiyonlar ve Vadeli İşlemlerle Trading Döngüleri ve Kırılmalar

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 24/Baskı 24/Haftalık Opsiyonlar ve Vadeli İşlemlerle Trading Döngüleri ve Kırılmalar - Larry Gaines (27 sayfa) - @eseckal.pdf>) · [Tam metin](01_gaines_cycles_breakouts.txt)

**Tam okuma:** S. 1–6 tanıtım, disiplin ve dört göstergeli olduğu söylenen fakat eşikleri açıklanmayan Power Cycle modeli; s. 7–11 son teyitli bir bar sol/sağ salınım uçlarından trend çizgisi; s. 12–16 vadeli/haftalık opsiyon tanıtımı ve denetlenmemiş işlem tabloları; s. 17–23 haftalık opsiyon, delta/zaman değeri; s. 24–27 seçilmiş NFLX opsiyon işlemi ve pazarlama özeti. S. 6'daki %75 kazanma, s. 25'teki %1.055 getiri iddiaları bağımsız örneklem veya maliyetli emir günlüğüyle doğrulanmaz. Dört göstergenin tam formülü, birleşim mantığı, tetikleyici ve stop verilmediği için kaynak modelinin sadık bir algoritması kurulamaz. Pivot/çizgi kırılımı önceki partilerde kayıtlıdır; **yeni bağımsız aday yok.** Haftalık opsiyonların bid/ask, theta, volatilite ve vade etkisi yalnız dayanak OHLC'den ölçülemez.

## 2. Akshay VG — Güniçi Satın Alma Stratejisi

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 4/Baskı 4/Güniçi Satın Alma Stratejisi (30 sayfa) - @eseckal.pdf>) · [Tam metin](02_intraday_buy.txt)

**Tam okuma:** S. 1–11 tanıtım ve opsiyon temeli; s. 12–15 Bank Nifty'de hafif OTM kullanım fiyatı ile açık faiz yorumu; s. 16–18 günlük pivot/önceki gün seviyeleri, H1/H4 çizgiler ve stokastik 5,3,3; s. 19–24 ilk iki M5 mum gövde sınırından 3. veya 5. mum kapanış kırılımı, yakın CPR/seviye varsa giriş ve stopu değiştirme; s. 25–27 primi %4–10 kârda veya sonraki düzeye giden yolun %60–75'inde çıkış; s. 28–30 Cuma işlem yapmama ve geçmişe bakarak doğrulama önerisi. S. 19'daki “her gün %100”, s. 28'deki “ayda üçten az kayıp” iddiaları işlem listesiyle desteklenmiyor. S. 14'te artan/azalan call OI için çelişkili satırlar ve s. 25'te “%30 uzak” hesabı belirsizdir; bu parçalar otomatik kurala aynen alınmaz.

**Mevcut araştırma ailesine uygulanabilir ablation (yeni aday sayılmadı):** [Hisse açılış aralığı](../batch_060/STRATEGIES.md) ve [VWAP/ORB](../batch_048/STRATEGIES.md) ile aynı ailede, Bank Nifty dayanak endeksinin gerçek NSE seansında ilk iki **tamamlanmış** M5 mum gövdesinin birleşik üst/alt sınırını 09:25 IST'de dondur. `max(open,close)` tepe, `min(open,close)` taban; `max(body_high[0:2])`, `min(body_low[0:2])`. İlk 09:25–09:30 M5 kapanışı üstteyse call, alttaysa put yön sinyali; kaynak s. 21'in “3. veya 5.” muğlaklığını birincil kol için yalnız ilk sonraki kapanışa indirgemek **bizim** seçimimizdir. Ayrı kol ilk beş M5 içinde ilk kapanış kırılımı. İcra sinyal kapanışından sonraki uygulanabilir opsiyon kotasyonunda; ATM'den 2 kullanım fiyatı OTM, vade günü işlem yok, Cuma işlem yok. Sözleşme evreni, o tarihte listelenmiş strike/vade ve canlı bid/ask ile belirlenir; geçmişte sonradan bilinen günün en iyi opsiyonu seçilmez. Başlangıç stopu dayanak karşı gövde sınırı; opsiyon stop dolumu dayanak tetikledikten sonraki gerçek kotasyonda, prim zararı ayrıca izlenir. Hedef seçilmiş prim girişinin %6 üstü veya gün sonu; %6 kaynak %4–10 aralığının **bizim ön seçilmiş** orta değeri. Girişte prim riski özsermayenin en çok %0,5'i, günde tek işlem, tüm komisyon/spread/kayma dahil. Karşılaştırma: ilk 10 dakika **wick** high/low ORB, gövde ORB, 15/30 dakika ORB; aynı Bank Nifty dönemleri ve gerçek opsiyon kotasyonları. CPR/OI ve stokastik ekleri yalnız point-in-time veri ve önceden sabit eşiklerle ayrı kollar olabilir. Opsiyon veri ve canlı kote erişimi yoksa sonuç “test edilemedi” kalır; dayanak endeks performansı opsiyon getirisi sayılmaz.

## 3. Alpesh Pansheriya — Darvas Box ile Trading

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 20/Baskı 20/Darvas Box ile Trading - Alpesh Pansheriya (42 sayfa) - @eseckal.pdf>) · [Tam metin](03_darvas_box.txt)

**Tam okuma:** S. 1–9 kutu, yatay üst/alt sınır, hacimli kapanış kırılımı; s. 10–15 stop/ölçülü hedef/pozisyon boyutu; s. 16–20 piyasa rejimi ve seçilmiş örnekler; s. 21–24 MA, RSI, MACD, OBV, ADX ek teyitleri; s. 25–31 yanlış kutu, sahte kırılım ve örnek olay; s. 32–42 araçlar, ATR ile kutu genişletme, trailing/ölçekleme, genel disiplin. **Darvas kutusu zaten [034. partide](../batch_034/STRATEGIES.md) strateji olarak kayıtlıdır.** Bu kitap sınırın en az üç kez teması (s. 25), hacim artışı (s. 8–9) ve kutu yüksekliği kadar hedefi (s. 13–14) filtre/çıkış ablation'ı olarak sunar. Özellikle geçmiş örnek fiyatları/sözde başarıları doğrulanmış işlem kayıtları değildir; yeni bağımsız aday yok.

## Sonuç

**0 yeni bağımsız aday.** Üç kaynak mevcut çizgi kırılımı, açılış aralığı ve Darvas stratejilerinin koşul/çıkış varyantlarını verdi. Bank Nifty gövde aralığı ancak gerçek point-in-time opsiyon kotasyonlarıyla ayrı test kolu olabilir.
