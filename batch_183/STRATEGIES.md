# Kitap okuma 183 — korelasyonlu FX çiftlerinde ayrışma

Üç ayrı PDF'nin **467 sayfası** baştan sona metne çıkarılıp sayfa bazında incelendi. **1 yeni, doğrulanmamış strateji adayı** kaydedildi. Backtest, paper test ve emir yapılmadı. Sayfa numaraları PDF sayfasıdır.

## 1. Jon Fibonacci — Gelişmiş Teknik Analiz (106 sayfa)

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 26/Baskı 26/Gelişmiş Teknik Analiz - Jon Fibonacci - Tradehouse Houston LLC (106 sayfa) - @eseckal.pdf>) · [tam metin](01_advanced_ta_fibonacci.txt)

**Tam okuma:** S. 1–15 psikoloji ve manipülasyon; 16–24 kurumsal mum anlatısı; 25–37 korelasyon sapması ve örnek grafikler; 38–48 açık pozisyon; 49–54 yuvarlak fiyat seviyeleri; 55–63 Fibonacci; 64–67 EUR/USD, GBP/USD, EUR/GBP ilişkisi; 68–81 seçilmiş grafikler; 82–106 psikoloji, sözlük ve kapanış. Kurumsal alıcı/satıcı niyeti, yalnız mumdan gözlenmiş gerçek sayılmaz. Yuvarlak seviye ve Fibonacci temasları önceki seviye adaylarını yineler. S. 64'te EUR/GBP'nin EUR/USD/GBP/USD göreli hareketini yansıtması tek başına öngörü sinyali değildir.

### JF183A — korelasyonlu iki FX çiftinde teyitli dip/tepe ayrışması

- **Kaynak (s. 25–28, 64):** EUR/USD ve GBP/USD birlikte hareket ederken biri daha yüksek dip, diğeri daha düşük dip yaparsa yüksek dip yapan görece güçlüdür; boğa dönüşü için onu izle. Tepe ayrışmasında daha düşük tepe yapan görece zayıftır ve short tarafı incelenir. Kaynak destek, trend ve EUR/GBP teyidinden söz eder; kesin pivot genişliği, giriş, stop ve hedef vermez.
- **Veri ve nesnel olay:** Aynı New York 17:00 kapanışına hizalı EUR/USD ve GBP/USD D1 bid/ask OHLC. Son 60 D1'de günlük getiri korelasyonu `>=0,5` (bizim geçici eşik); bu koşul yoksa sinyal yok. Her çiftte 2 sol/2 sağ barlı pivotlar sadece sağ iki bar kapandığında kullanılabilir. Aynı 10 D1 penceresindeki son iki **teyitli** dipte bir çiftin ikincisi ilkinden yüksek, diğerininki düşükse yüksek dipli çift long adayıdır. Tepe için düşük tepe yapan short adayıdır. Pivotların eşleşme penceresi, eşik ve D1 zaman ölçeği bizim ölçülebilirleştirmemizdir.
- **Giriş ve risk:** Aday çiftte ikinci pivot teyidinden sonra kapanmış ilk D1'in `close`u önceki 5 tam D1 `high` üstüne çıkarsa sonraki uygulanabilir FX açılışında ask ile long; shortta 5 günlük low altı ve bid ile simetrik. Aynı anda tek pozisyon. Long stop teyitli ikinci dip altı `0,1×ATR14`, short stop ikinci tepe üstü; giriş ile stop ters taraftaysa atla. Sermaye riski en fazla `%0,25`. `2R` hedef veya 15 D1 sonunda çıkış, hangisi önceyse; spread, komisyon, swap ve hafta sonu gap'i gerçekçi fill ile. Kırılım/stop/çıkış kuralları **kaynakta yoktur, bizim backtest sözleşmemizdir**.
- **Ayırıcı test:** Aynı koşullarda yalnız 5 günlük kırılım, yalnız kendi çiftinin HH/HL trendi ve [164. partideki](../batch_164/STRATEGIES.md) para birimi gücü sıralaması ile karşılaştır. 10 günlük eşleşme, korelasyon ve pivot genişliği duyarlılığı; net R, örnek sayısı, maliyet, rejim ve dönem dışı sonuç raporlanmalı. Seçilmiş grafikler performans kanıtı değildir. EUR/GBP, cebirsel olarak iki çiftten türediği için bağımsız teyit verisi diye üç kez sayılmamalı.

## 2. Javier Luque — Ne Zaman Hisse Senedi ve Kripto Varlık Alınır (182 sayfa)

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 26/Baskı 26/Ne Zaman Hisse Senedi ve Kripto Varlık Alınır - Javier Luque (182 sayfa) - @eseckal.pdf>) · [tam metin](02_when_buy_luque.txt)

**Tam okuma:** S. 1–23 giriş ve piyasa anlatımı; 24–35 seçilmiş hisse örnekleri ve tarihsel performans iddiası; 36–40 EDC iki mum kuralı; 41–76 işlem grafikleri; 77–89 anlatı; 90–106 EDC 2.0 ve örnekler; 107–110 anlatı; 111–126 kripto örnekleri; 127–146 tepe/ayı piyasası örnekleri; 147–168 ek EDC hisseleri; 169–179 olay işlemi; 180–182 kapanış. S. 36–40'ta ilk mum alt Bollinger bandını deler, ertesi boğa mumunun kapanışı ilk mum gövdesini aşar; üçüncü mum açılışı giriş, ilk mum dibi altı stop, yarı pozisyon `+%30`da çıkış ve kalanı takip stopudur. S. 90–93'te ilk mumun yeşil olabildiği varyant vardır. Bu BB alt bant + yutan/boğa teyidi ailesi [91.](../batch_091/STRATEGIES.md) ve [137. partide](../batch_137/STRATEGIES.md) zaten kayıtlı; `%30` kâr ve üçüncü mum giriş ayrıntısı **ayrı bağımsız sinyal** değil, mevcut adayın çıkış/zamanlama varyantıdır. S. 24–34'teki geçmiş performans, 2018–2019 civarında seçilen hisselerin 2007'ye dönük uygulanması nedeniyle sağkalım/ileriye bakma yanlılığı riski taşır; doğrulanmış getiri sayılmadı. S. 32–40'taki yüksek pozisyon payı ve `%7–10` stop evrensel risk kuralı kabul edilmedi. Yeni aday: **0**.

## 3. Dean Grey — Piyasalar Arası Analiz Kullanarak Forex Trading (179 sayfa)

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 26/Baskı 26/Piyasalar Arası Analiz Kullanarak Forex Trading - Dean Grey (179 sayfa) - @eseckal.pdf>) · [tam metin](03_intermarket_grey.txt)

**Tam okuma:** S. 1–66 FX tarihi, haber/fundamental ve platform; 67–92 teknik göstergeler; 93–121 altın, petrol, dolar ve çapraz piyasaların korelasyon örnekleri; 122–139 VantagePoint tahmini ortalamalar; 140–171 tahmini ortalama ve mum örnekleri; 172–179 kapanış. Altın/dolar ve petrol/dolar ilişkileri rejime bağlı genel anlatımdır; kaynak gecikme, eşik ve işlem sözleşmesi vermez. VantagePoint öngörüleri özel model girdisi/versiyonu olmadan yeniden üretilemez. Seçilmiş grafik ve başarı oranı iddiaları bağımsız performans kanıtı değildir. Yeni aday: **0**.

**Parti sonucu:** 3 PDF, **467 sayfa**, **1 yeni doğrulanmamış aday**. Kümülatif **549 ayrı PDF, 28.242 sayfa, 421 strateji adayı**.

