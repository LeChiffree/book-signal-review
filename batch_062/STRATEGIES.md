# Kitap okuma 062 — Medyan çizgi, hacimli yutan mum, MACD histogram ayrışması

**Kapsam:** Üç PDF'nin gerçek **96 + 81 + 62 = 239 sayfası** sıralı metne çıkarılıp incelendi. Atıflar PDF sayfasıdır. Kaynakta verilmeyen eşik ve icra kuralları **bizim test tanımımızdır**. Backtest, paper test ve emir yapılmadı.

## 1. Patrick Mikula — En İyi Trend Çizgisi Yöntemleri

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/En İyi Trend Çizgisi Yöntemleri - Patrick Mikula (96 sayfa) - @eseckal.pdf>) · [Tam metin](01_trendlines_mikula.txt)

**Kaynak:** Andrews medyan çizgisinin A, B, C pivotlarıyla kurulması ve çizgiye dönüş gözlemleri s. 7–10'da; dirgen paralelleri ve kırılma kuralları s. 13–14, 54–57'de. Açık swing reçetesi s. 58'de: aşağı eğimli medyan çizgiye yaklaşma + Slow Stochastic(14) aşırı satım (<20) + yukarı dönüşte long; yukarı eğimli çizgi + aşırı alım (>80) + aşağı dönüşte short. Kitaptaki yaklaşık %80 çizgiye ulaşma ifadesi (s. 8, 58) bağımsız örneklemle doğrulanmış başarı oranı olarak alınmaz. Medyan çizgiye erişim süresi/pivot bölgesi s. 77–78'de anlatılır.

### PM62 — Medyan çizgi temasında stokastik aşırılık ve kapanış dönüşü

- **Yapı:** H4'te 3 sol/3 sağ kapanmış barla teyitli, sırayla A–B–C salınım pivotları. A'dan B–C orta noktasına giden medyan çizgi ve B/C'den geçen paraleller, C'nin sağındaki üçüncü bar kapanınca dondurulur; çizgi o andaki bar indeksinde değerlendirilebilir. Long için medyan çizgi aşağı eğimli, short için yukarı eğimli. Pivotlar sonrası çizgi geriye dönük taşınmaz. Çizgi tanımının bu sayısal pivot penceresi bizim seçimimizdir.
- **Kurulum/tetik:** C teyidinden sonraki en çok `max(B−A,C−B)` H4 barda `|close−median_line|≤0,25×ATR14_H4` ve Slow Stochastic(14,3,3) `%K<20` long kurulumu; short için `%K>80`. Aynı kapanışta veya sonraki üç tam H4 bar içinde long `close>high[t−1]` ve `%K[t]>%K[t−1]` ilk dönüş teyidi; short tersi. Temas toleransı, teyit ve zaman aşımı bizim ölçümümüz. Çizgiye hiç ulaşmayan veya teyit vermeyen kurulum işlem değildir.
- **İcra/risk:** Teyit kapanışı sonrası ilk uygulanabilir 1m giriş. Long stop temas ile teyit arasındaki gözlenmiş low `−0,1×ATR`; short simetriği. 2R veya 24 H4 süre, ilk gerçekleşen. Stop yanlış tarafta/masraftan dar ise atla; aynı 1m stop ve hedefte stop önce. Stokastiksiz medyan temas ve medyan çizgisiz stokastik dönüş kolları, her filtrenin ek etkisini ayırır. Önceki pitchfork/salınım adaylarıyla olay örtüşmesi ve yatay/trend rejimi kıyaslanır.

## 2. Dr. Melvin Pasternak — Her Traderin Bilmesi Gereken 21 Mum

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Her Traderin Bilmesi Gereken 21 Mum - Dr. Melvin Pasternak (81 sayfa) - @eseckal.pdf>) · [Tam metin](02_candles_pasternak.txt)

**Kaynak:** Kitap 21 mum kalıbını trend ve destek/direnç bağlamında anlatır. Yutan formasyonda ikinci gerçek gövde ilkinin tüm gövdesini kapsar, gölgeleri kapsamak zorunda değildir (s. 31). Gövde büyüklüğü ve oluşum gününün yüksek hacmi sinyali güçlendirir (s. 32); tek mumdan sonra ikinci gösterge teyidi önerilir (s. 26). Çekiç/cellat için alt gölgenin gövdenin en az iki katı olma kuralı s. 25'te, iki mumlu cımbız s. 70–71'de. Kitap çoğunlukla seçilmiş hisse örnekleri kullanır; başarı oranı sunmaz.

### MP62 — Trend sonunda hacimli büyük gövdeli yutan mum

- **Kalıp:** H4 kapalı barlarında long için önceki mum ayı, mevcut mum boğa ve `open[t]≤close[t−1]`, `close[t]≥open[t−1]`; short simetrik. İlk mumdan önceki 20 H4 `EMA20` eğimi long için aşağı, short için yukarı. Yutan gövde `≥1,5×` önceki 20 H4 gövde medyanı; mevcut base-volume `≥1,5×` önceki 20 H4 medyan hacmi. Eğim, gövde ve hacim eşikleri bizim sayısallaştırmamızdır; hacim geçmiş medyanına mevcut mum katılmaz.
- **Teyit/icra:** Kaynağın ikinci gösterge önerisi için ana kol: yutan mum tamamlandığında RSI14 long `<40`, short `>60`; sonra en çok iki H4 içinde ilk `close>high[yutan]` long veya `close<low[yutan]` short. Tetik kapanışı sonrası ilk uygulanabilir 1m giriş. Stop long yutan mum low `−0,1×ATR14_H4`, short high `+0,1×ATR`; 2R veya 24 H4 süre. RSI ve kırılım teyidi kaynakta bu değerlerle verilmez; ayrı ablation kollarında çıkarılır. Stop yanlış tarafta/maliyetten dar ise atla; aynı 1m stop önce.
- **Karşılaştırma:** Yutan mumun hacimsiz ve gövde filtresiz kolları, önceki engulfing adaylarıyla sinyal çakışması ve net R. Hisse örneklerindeki açılış boşlukları 7/24 kriptoda varsayılmaz; işlem hacmi farklı borsalar arasında normalize edilmeden birleştirilmez.

## 3. Jayden Smith — MACD Göstergesinin Sırrı

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/MACD Göstergesinin Sırrı - Jayden Smith (62 sayfa) - @eseckal.pdf>) · [Tam metin](03_macd_smith.txt)

**Kaynak:** MACD hızlı EMA eksi yavaş EMA, sinyal MACD'nin EMA'sı, histogram fark olarak tanımlanır (s. 5); örnek parametre 12/26/9 (s. 7). Fiyat daha yüksek tepe yaparken histogram daha düşük pozitif tepe yaparsa ayı ayrışması ve sonraki barda histogram/fiyat zayıflaması teyidi (s. 23). Fiyat daha düşük dip, histogram daha yüksek negatif dip yaparsa boğa ayrışması ve sonraki barda zayıflayan negatif histogram/fiyat toparlanması teyidi (s. 27). Aradaki karşı işaretli histogram alanını ayırma uyarısı s. 21, 31'de. “MACD gecikmez” iddiası (s. 13) ölçümsüz genelleme; bütün EMA hesapları geçmiş fiyatın fonksiyonudur.

### JS62 — Histogram alanları arasında teyitli fiyat ayrışması

- **Alanlar:** D1 kapalı barlarında EMA12, EMA26, sinyal EMA9 ve histogram `MACD−signal`; en az 100 D1 ısınma. Histogramın sıfır üstü ve altı ardışık alanları, ancak **karşı işaretli kapanmış en az bir bar** görüldükten sonra ayrıdır. Sıfır tam değerde önceki alana dahil etme ve en az 2, en çok 30 D1 alan uzunluğu bizim sabitlememizdir.
- **Boğa sinyali:** Tamamlanmış ilk negatif alan A'nın en düşük fiyat low'u ve en negatif histogram değeri kaydedilir. Aradaki tamamlanmış pozitif alan sonrası ikinci negatif alan B'de, B'nin o ana kadarki fiyat low'u `A.low−0,1×ATR14` altına inerken histogram minimumu `A.hist_min+0,05×ATR14` üstünde kalmalı. B sürerken sonraki D1 barında histogram bir önceki bara göre yükselir ve `close>close[t−1]`; bu kapanış ilk teyittir. ATR ile histogram birimleri uyumlu olsa da 0,05 katsayısı yalnız deneysel eşik; histogramın fiyat ölçeğine duyarlılığı ayrıca ölçülsün. Ayı sinyali pozitif alanlar, daha yüksek fiyat high, daha düşük pozitif histogram tepe ve sonraki düşen histogram/fiyatla simetrik.
- **İcra/risk:** Teyit kapanışı sonrası ilk uygulanabilir 1m giriş; long stop B alanının teyide dek gözlenmiş low `−0,1×ATR14`, short high `+0,1×ATR`. 2R ya da 30 D1 süre. Stop yanlış tarafta/maliyetten dar ise atla; aynı 1m stop önce. Tamamlanmamış B alanının ilerideki minimumunu teyit anında kullanma. Histogram ayrışmasız yalın fiyat dip/tepe dönüşü ve önceki MACD ayrışması adaylarıyla ek katkı kıyaslansın.

## Ortak test sözleşmesi

Tüm adaylarda yalnız o ana dek kapanmış mumlar ve teyitli pivotlar kullanılır; sonraki uygulanabilir 1m dolum, ücret, spread, kayma, perpetual funding, eksik veri ve eşzamanlı sinyal politikası gerekir. Zaman sıralı ayrılmış doğrulamada işlem sayısı, net R, maksimum düşüş ve yalın taban çizgileri ölçülmeden kârlılık iddiası kurulmaz.
