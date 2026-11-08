# Kitap okuma 019 — fiyat aksiyonu bağlamı, iç bar ve bölge tepkisi

**Kapsam:** 20 + 58 + 86 = **164 PDF sayfası**. Üçünün de tam sayfa metin dökümü bu klasördedir. Atıflar PDF sayfasınadır. Sayısal kodlama eşikleri açıkça **bizim deney tanımımızdır**. Forex örnekleri kriptoda kanıtlanmış sonuç değildir. Backtest, paper test ve emir yapılmadı.

## 1. ThinkMarkets — Price Action Rehberi

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Price Action Rehberi - Think Markets (20 sayfa) - @eseckal.pdf>) · [Tam metin](01_think_markets.txt)

Kitap iki temaslı trend çizgisini geçici, üç temaslıyı teyitli sayar (s. 6–8). S/R kırılınca rol değişimini (s. 9–10), çekiçte sonraki mumun eski zirveyi aşmasını teyit olarak (s. 11), kayan yıldızda sonraki güçlü düşüş mumunu (s. 12), doji ve üç mumluk yıldızları (s. 13–15) anlatır. Son bölümde stopun tezi bozan seviyeye bağlanması ve önceki yüksek hedefli çekiç örneği vardır (s. 17–20). Örnek kazanmış olsa da seçilmiş tek örnektir.

### TM19 — Önceki destek bölgesinde teyitli çekiç

- **Kaynak kuralı:** Düşüş sonundaki uzun alt fitilli küçük gövde; bir sonraki mum önceki zirveyi aşarsa dönüş teyidi; stop destek/tez bozulma alanı, hedef eski yüksek (s. 11, 17–20). Kaynak kesin fitil oranı ve destek pencere uzunluğu vermez.
- **Bizim kapalı D1 tanımı:** `t` başlamadan önceki 40 tamamlanmış mumdan onaylı pivot diplerin çevresinde `±0.25 ATR14` destek bölgesi dondurulur. `t` mumunun düşüğü bölgeye değer; `lower_wick >=2×body`, `upper_wick <=body`, `close` mum aralığının üst %35'inde. `t+1` kapanışı `high[t]` üstüne çıkarsa ancak **t+1 kapanışından sonra** ilk 1m açılışında long. Stop `min(low[t],low[t+1])−0.1 ATR`, hedef olaydan önce bilinen en yakın onaylı D1 direnç pivotu veya 2R; H3D/H7D/H14D zaman çıkışları ayrı. Hedef girişin üstünde değilse işlem yok.
- **Örtüşme:** Batch 003 mum, batch 018 M18a yüksek zaman dilimi S/R filtreleriyle aynı olay olabilir; karşılaştırma aynı tarih/sembol olay anahtarıyla yapılmalı. D1 kapanışı sonrasında teyit almak erken fitil girişinden farklıdır.

## 2. Rayner Teo — Price Action Rehberi

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Price Action Rehberi - Rayner Teo (58 sayfa) - @eseckal.pdf>) · [Tam metin](02_rayner_teo.txt)

Kitap statik S/R'nin çizgi değil bölge olduğunu, kırılınca rol değiştirdiğini (s. 8–9), dinamik S/R için EMA20/50'nin araç olduğunu, bu sayılara özel anlam yüklenmemesi gerektiğini söyler (s. 11–12). Trend yapısı ve ortalama eğimleri (s. 19–21), dört piyasa aşaması (s. 14–18), aralık daralması/genişlemesi (s. 24–26), fitil/gövde/kapanış konumu (s. 33–36) birer özellik ailesidir. Pin barı tek başına ters işlememeyi, yükselişte destekten boğa; düşüşte dirençten ayı pin barı seçmeyi önerir (s. 37–41). İç barı düşük volatilite işareti olarak yorumlar; kırılımı yatay ve karmaşık piyasada körlemesine almamayı vurgular (s. 43–45). En belirgin sistem s. 52–54'tedir.

### RT19a — EMA10 trendinde iç bar ve ana mum kırılımı

- **Kaynak:** Güçlü düşüş trendi ve 10 EMA'ya uyum; iç bar oluşunca **önceki/ana mumun altına** sell stop, tepesine stop; işlem dolarsa fiyat EMA10 üstünde kapanınca çık. Yükselişte simetri. İşlem başına en çok %1 öz sermaye riski önerisi ve trend/uzun aralık sonrası uygunluk s. 52–54. Kitap EMA10'ya “uyma” ve güçlü trendi sayısallaştırmıyor; ana mum mu iç mum mu stopta kullanılacağı s. 54'te açık soru bırakılıyor.
- **Bizim D1 uygulaması:** Son 10 tamamlanmış günlük kapanışta long için `EMA10[t]>EMA10[t-5]`, `close[t]>EMA10[t]`, son 5 günün en az 4 kapanışı EMA10 üstünde; short simetrik. İç bar `high[t]<high[t-1] && low[t]>low[t-1]`; sinyal `t` kapanınca bilinir. Sonraki 24 saatte `high[t-1]+1 tick` buy stop veya `low[t-1]−1 tick` sell stop; dolmazsa iptal. İlk 1m temasında uygulanabilir fiyat/kayma ile dolum, başlangıç stopu karşı ana mum ekstremumu `±1 tick`, kapanmış sonraki D1 `EMA10` karşı tarafında ise çıkış; ayrıca H14D tavan. Baz kaynakta TP yoktur; 2R TP ayrı varyant. %1 hesap riski ve pozisyon nominal tavanı birlikte uygulanır. Aynı 1m barda giriş/stop belirsizse muhafazakâr sıralama kullanılır.
- **Ablation:** EMA10 eğim/trend filtresiz iç bar, EMA10 filtreli sürüm, EMA20/50 rejim filtresi. Önceki iç bar adayları ve mevcut özellik matrisindeki inside-bar/EMA eşdeğerleriyle birleştir; tekrar kolon açma.

### RT19b — Trend yönünde S/R pin bar filtresi

- **Kaynak:** Yükselişte yalnız destek çevresinde bullish pin bar; düşüşte direnç çevresinde bearish pin bar (s. 37–41). Sayısal geometri verilmez.
- **Bizim D1 deney:** Son tamamlanmış W1 `close>EMA20_W1` long rejimi; geçmiş 40 kapanmış D1 içinden onaylı pivot destek `±0.25 ATR14` bölgesi. `lower_wick >=2 body`, `close` mum aralığı üst %30'da ve düşük bölgeye temas etmişse sonraki ilk 1m long. Stop pin bar altı `−0.1 ATR`, hedef 2R veya bilinen karşı dirençten yakın olanı, H7D çıkış. Short simetrik. Bu TM19 ile neredeyse aynı hipotezdir; ayrı strateji getirisi olarak toplama, **hemen girişe karşı ertesi mum teyidi** kıyası yap.

## 3. Atanas Matov — Price Action Rehberi

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Price Action Rehberi - Atanas Matov (86 sayfa) - @eseckal.pdf>) · [Tam metin](03_atanas_matov.txt)

Kitap OHLC ekstremumlarından çizilen S/R bölgelerini ve kırılım sonrası rol değişimini (s. 7–14), sert hareketin başladığı tabanı arz/talep bölgesi saymayı (s. 15–24) işler. Bölgeyi saptamanın öznel olabileceğini açıkça kabul eder (s. 21–23). Örnek giriş bölge ortası, stop bölge ötesi 5–10 Forex pip, 2–3R hedef (s. 25–26); pip kriptoda taşınamaz. Pin bar alt fitilinin gövdenin en az iki katı olması (s. 29), kamadan çıkışla short ve tepe üstü stop (s. 31–32), trend yönünde yutan mum (s. 34–40), iç barın trend ortasında devam ve ana S/R'de ters dönüş yorumu (s. 41–48) var. RSI, MACD, ATR ve stokastik bölümü (s. 49–67) önceki partilerin indikatör ailesiyle örtüşür. S. 68–79 trend/aralık ve geri çekilme bağlamı sunar.

### AM19 — İtki tabanından talep bölgesi retesti

- **Kaynak:** Düşüş–taban–yükseliş veya yükseliş–taban–yükseliş; bölge hızlı yükselişin başladığı tabandır, giriş çoğunlukla orta nokta, stop bölge altı, hedef 2–3R (s. 21–26). Bölgenin şekli, “hızlı” hareket ve geçerlilik süresi kesin değil.
- **Bizim D1 tanımı:** `t` kapanınca son 3–6 tamamlanmış D1 mumun aralığı `<=2 ATR14[t-1]` taban adayı; sonraki tamamlanmış iki mum içinde `close` taban üstüne `>=1 ATR14[t-1]` çıkıp her iki kapanış da taban üstünde kalırsa talep bölgesi `[min(low_base), max(high_base)]` dondurulur. Sonraki en fazla 20 D1 gün içinde ilk kez orta noktaya dokunan 1m mumda limit long; dolum yoksa iptal. Stop bölge altı `−0.1 ATR`, hedef 2R ve 3R ayrı varyant, H7D/H14D zaman çıkışı. İlk retestten önce bölge altına D1 kapanışı olursa iptal. Tüm tespit ve emir zamanı causal; “itkiyi” görmeden taban geçmişte sinyal olarak işaretlenmez. Short arz bölgesi simetrik ama perp/borrow/funding evreninde ayrı.
- **Örtüşme:** Batch 005 arz/talep ve batch 018 rol değişimiyle ortak olaylar sayılır; yeni fayda bölgenin **ilk retesti** ve sert çıkış koşulu ablation'ıyla ölçülür. Aynı 1m barda limit ve stop birlikte temas ederse stop önceliği ve uygulanabilir dolum modeli.

## Test sözleşmesi ve karar

Bu partinin ilk sıradaki adayı **RT19a**: kaynakta giriş, stop ve EMA10 çıkışı açık tarif edilmiş. İkinci sıra **AM19** bölge tanımına çok duyarlı olduğu için duyarlılık ve olay sayısı raporlanarak değerlendirilmeli. **TM19/RT19b** aynı S/R pin bar ailesinin teyit karşılaştırmasıdır. Tüm adaylarda karar anı yalnız kapanmış UTC D1 ve tamamlanmış W1; uygulama 1m; H3D/H7D/H14D, ücret, spread/kayma, funding, stop/TP eşzamanlılığında stop önceliği, point-in-time coin evreni, çakışan olayların tekilleştirilmesi ve zaman sıralı dış örneklem sözleşmesi geçerlidir. Kitapların güven ve kârlılık iddiaları henüz ölçülmedi.
