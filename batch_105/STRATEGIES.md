# Kitap okuma 105 — dört kapanış ve üç pip teyidi

**Kapsam:** Üç PDF'nin **10 + 12 + 11 = 33 sayfası** baştan sona okundu. Atıflar PDF sayfasıdır. Backtest, paper test veya emir yapılmadı; kaynak performansı doğrulanmış sonuç değildir.

## 1. Price Action Scalper

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 7/Baskı 7/Price Action Scalper (10 sayfa) - @eseckal.pdf>) · [Tam metin](01_price_action_scalper.txt)

**Tam okuma:** S. 1–2 dört ekran kurulumu; s. 3–6 eşzamanlı yükseliş kapanışı ve 3 pip tetik; s. 7–8 düşüş simetrisi ve yapısal stop; s. 9–10 alternatif stop/hedef, haber ve çoklu çift notu. [27. partide](../batch_027/STRATEGIES.md) Thomas Carter #16 aynı M5/M15/M30/H1 saat başı renk uyumunu anlatmış, ancak burada kapanıştan sonra **3 pip kırılımın ilk 5 dakikada gerçekleşmesi** ayrı, süreli teyit hipotezi. S. 10'daki %75–80 kazanma iddiası denetlenmiş veri değildir.

### PAS105A — H1/M30/M15/M5 renk uyumu sonrası beş dakikalık 3 pip kırılımı

- **Kaynak (s. 3–9):** Saatlik mum kapandığında aynı anda kapanan son M30, M15 ve M5 mumları da yeşilse long için kapanış fiyatından 3 pip yukarının ilk beş dakika içinde görülmesini bekle; dördü kırmızıysa 3 pip aşağı short. İlk beş dakika tetiklenmezse bekleyen kurulum iptal. Kaynak s. 8–9 stop olarak önceki H1 mum low/high'ının 2 pip dışını veya 20 pip sabiti; hedef olarak stopun 2–3 katı veya 30–40 pip verir. Bunlar tek ve tutarlı çift değildir.
- **Nesnel FX araştırma sürümü:** EURUSD M1 bid/ask verisinden UTC H1, M30, M15 ve M5 barları oluştur; saat `t` kapanışında bu dört *ayrı* barın her biri `close>open` ise long, `close<open` ise short, doji/eksik bar varsa sinyal yok. `C=H1 close_t`; long tetik `C+0.0003`, short `C−0.0003`. Yalnız `t` sonrası ilk beş tamamlanmış M1 barda, uygun alış/satış kotasyonu tetik seviyesine ilk dokunduğunda giriş; M1 boşlukta ilk uygulanabilir kötü fiyatı kullan. Aynı M1 içinde sınır ve stop/target sırası çözülemiyorsa kötümser sonuç. Girişten sonra long stop kapanmış H1 low `−0.0002`, short stop H1 high `+0.0002`; stop yanlış tarafta veya mesafe sıfırsa işlemi atla. Hedef 2R; 3R, 20 pip sabit stop ve 30/40 pip hedef *ayrı* kaynak varyantlarıdır. En çok 4 saat tutma **bizim** sınırımız; açık işlem varken yeni sinyal yok. Spread/komisyon/kayma, haber takvimi kullanılırsa yalnız önceden yayımlanmış olay zamanı kaydı ve çoklu çift eşzamanlı risk sınırı gerekli.
- **Ayrışma/test:** Aynı dört mum olayında 3 pip + 5 dakika filtresiz temel kuralla, yalnız H1 renk ve H1 momentumu ile sinyal çakışması/olay sayısı/maliyet sonrası net R karşılaştır. FX pip eşiğini BTC/ETH'ye doğrudan kopyalama; kripto varyantında `3pip/H1close` gibi eski FX ölçeği değil, önceden sabit `0.1×ATR14_H1` tetik ayrı **bizim** hipotezimizdir.

## 2. Forex Grid Trade Stratejisi

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 8/Baskı 8/Forex Grid Trade Stratejisi (12 sayfa) - @eseckal.pdf>) · [Tam metin](02_forex_grid.txt)

**Tam okuma:** S. 1–3 çift yönlü bekleyen emir ve stopsuz grid tanımı; s. 4–6 üç kademe örneği; s. 7–8 gridi topluca veya karşı bacakları kapatma; s. 9–12 marj, likidite, maliyet ve tanıtım. Kaynak örneğinde üst/alt başlangıç fiyatları var ama kademe aralığı, her bacağın miktarı, kâr eşiği ve azami kayıp kuralları tek anlamlı değil. Kaynağın “zararı durdurmasız” yaklaşımı açık uçlu zarar ve marj çağrısı taşıyor; kârlılık önerisi olarak yeni aday sayılmadı. İleride grid sınırlaması araştırılacaksa kademe sayısı, marj rezervi, stres fiyat yolu ve zorunlu tasfiye önceden dondurulmalı. S. 12'deki düzenleyici iddia güncel hukuki kanıt olarak alınmadı.

## 3. Swing Failure Pattern

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 7/Baskı 7/Swing Failure Pattern (11 sayfa) - @eseckal.pdf>) · [Tam metin](03_swing_failure.txt)

**Tam okuma:** S. 1–4 likidite anlatısı ve anahtar uçlar; s. 5–6 yüksek/düşük dışına fitil ve içeri kapanış; s. 7 stop/son swing hedefi; s. 8–10 ikinci giriş, doji ve birleşimler; s. 11 sonuç. S. 5–7'nin kapanışla teyit edilen süpürme kuralı [70. partideki JK70](../batch_070/STRATEGIES.md) ve önceki pivot süpürmesi adaylarıyla eşdeğer çekirdeğe sahip. Burada pivotun “önemli” olmasının algoritması, ikinci giriş eşiği ve hedef swing seçimi kesin değil; bağımsız yeni aday sayılmadı. Fitil gözlemi gerçek stop kümelerini veya büyük aktör niyetini kanıtlamaz.

## Sonuç

**1 yeni aday**: PAS105A. Grid ve SFP değerlendirilip gerekçeleriyle kaydedildi. Bu partinin aday sayısı geriye dönük yeniden adlandırmayla çoğaltılmadı.
