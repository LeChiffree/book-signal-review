# Kitap okuma 025 — M1 scalp, M5 forex sistemleri ve portföy yöntemleri

**Kapsam:** 96 + 28 + 157 = **281 PDF sayfası**. Sayfa sıralı metinlerin tamamı yan dosyalarda tutulur. Kaynak numaraları PDF sayfasıdır. Forex/altın pip, seans ve kaldıraç ayarları kriptoya doğrudan taşınmaz. Backtest, paper test ve emir yapılmadı.

## 1. Trevor Candle — 1 Dakikalık Forex Scalping Stratejisi

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 22/Baskı 22/1 Dakikalık Forex Scalping Stratejisi - Trevor Candle (96 sayfa) - @eseckal.pdf>) · [Tam metin](01_m1_scalping_trevor.txt)

Asıl pazar XAU/USD CFD, tercih edilen saat New York açılışı civarı (s. 68–70). M30 EMA200 eğimi ve fiyat konumu trendi; M15/M1 uyumu; genişleyen Bollinger bandı, EMA200 yönü, EMA20'ye geri çekilme, Parabolic SAR dönüşü ve MACD kesişimi sonrası EMA20 üzerinde/altında kapanış giriş kuralıdır (s. 77–86). Kitap 30–50 pip hedef, 100–150 pip stop **veya ters eş büyüklükte hedge** önerir (s. 73–74, 86). Bu pip ve hedge yapısı kriptoya uygun bir risk sözleşmesi değildir. S. 92–93'teki %83 kazanma ve 2,01 kâr faktörü kitap yazarının kısa dönem iddiası; bağımsız doğrulanmadı. S. 83 ve 85 örnek açıklaması ile s. 84 short MACD yönü arasında çeviri/tutarlılık sorunu vardır; yazılı kural esas alınır.

### T25 — Çoklu teyitli EMA20 geri dönüşü (ayrı M1 deney)

- **Kaynak:** M30 baskın trend (s. 79), Bollinger genişlemesi (s. 80), M1 EMA20 geri dönüşü + SAR + MACD kesişimi + EMA20 yönünde kapanış (s. 82–86).
- **Bizim kapalı mum sözleşmesi:** Son *tamamlanmış* M30'da `EMA200[t]>EMA200[t-3]` ve `close>EMA200` long (short tersi); son tamamlanmış M15 kapanışı aynı yönde EMA200 tarafında. M1 Bollinger(20,2) genişliği `width[t]>width[t-5]`; son 5 M1 barında `low<=EMA20` temas ve son kapanmış M1'de `close>EMA20`, `close>open`, `close>EMA200`, MACD(12,26,9) çizgisi sinyal üstüne kesmiş, SAR(0.02,0.2) son 3 M1 bar içinde fiyat altına dönmüş. Short simetrik. Sinyal kapanışından sonraki ilk fiyatla giriş; stop son 10 kapanmış M1 bar dibinin `0.1 ATR14_M1` altı, hedef 1.5R, süre en fazla 30 dakika. `5/3/10`, ATR tamponu, hedef ve süre bizim sabit deney parametreleri; kaynak bunları vermez.
- **Karşılaştırma:** EMA20 dönüşü tek başına, SAR/MACD eklenmiş, M30/M15 yön filtresi eklenmiş aynı olaylar. Emir defteri spreadi, fee ve kayma olmadan M1 kârlılık yorumu yapılamaz. 1m OHLC'de aynı mum stop/hedef sırası bilinmiyorsa kötümser stop önceliği veya tick veri gerekir. Kaynaktaki hedge/katlama paper adayına alınmaz.

## 2. 20 Trading Stratejisi — 20 kısa M5 forex kuralı

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 3/Baskı 3/20 Trading Stratejisi (28 sayfa) - @eseckal.pdf>) · [Tam metin](02_twenty_strategies.txt)

PDF 20 bağımsız araştırma fikrini çok kısa biçimde listeler (s. 2–27); ortak sonuç/örneklem yok. Bunları 20 ayrı doğrulanmış sistem diye saymıyoruz. Kaydırılmış EMA ve tanımsız özel histogram içeren #5 (s. 6–8), Laquerre #12 (s. 17), belirsiz MACD eşikleri #18 (s. 25) yeniden üretilebilirlik açısından düşük önceliklidir. #13'te listedeki çiftler EUR/USD ve GBP/USD iken kâr hedefinde AUD/USD de geçer (s. 18); #18'in short takip stop işareti de tutarsızdır (s. 25).

### W25a — 10/21 EMA geri çekilme bölgesi

- **Kaynak #2:** M5 trend, EMA50 eğimi; fiyat EMA10–21 bölgesine geri çekilince trend yönünde giriş, 5 pip + spread stop, 10 pip hedef (s. 3). “30 derece” grafik ölçeğine bağlıdır; kullanılmaz.
- **Bizim M5 deney:** Son 20 tamamlanmış M5 barında yükselen iki teyitli pivot zirve/dip, `EMA10>EMA21>EMA50`, `EMA50[t]>EMA50[t-5]` long. M5 düşük fiyatı EMA10–21 bandına girdikten sonra ilk kapanmış M5 `close>EMA10` ve `close>open` ise sonraki ilk 1m giriş. Stop son teyitli M5 dip altı `0.1 ATR14_M5`; hedef 2R, zaman sınırı 6 saat. Short simetrik. Kaynakta pivot, tetik ve kriptoya uygun stop tanımı yoktur; burada araştırma parametresi olarak eklenmiştir.
- **Test:** Aynı EMA50 trend olayında bölgeye dönüş var/yok; ücret sonrası sinyal ve işlem başına sonuç. Önceki EMA trend adaylarıyla aynı aile sayılır.

### W25b — Önceki saat kutusunun %20 taşması

- **Kaynak #7:** New York 08:00'de önceki saat en yüksek/düşük kutusu; kutu yüksekliğinin %20 dışına giriş, sinyal yalnız bir saat geçerli, kutunun karşı ucunda stop, kutu yüksekliğinin %400 dışı hedef ve kutu boyu iz süren stop (s. 11). Bu, forex seans kuralıdır.
- **Bizim M5 deney:** Her UTC gününde önceden belirlenmiş sabit 08:00–09:00 penceresi; 07:00–07:59 aralığı `R,S,w=R-S`, ancak `w>=0.5 ATR14_H1` ve likidite eşiği sağlanırsa. 08:00–08:59 içindeki ilk kapanmış M5 `close>R+0.2w` long, `<S-0.2w` short; sonraki ilk 1m giriş, stop karşı kutu sınırı, hedef girişten 2R veya kaynak 4w ayrı varyant, en geç 60 dakika. `0.5 ATR`, UTC saat seçimi ve 2R bizim deney şartlarımız. 08 UTC New York 08 değildir; seans etkisi ayrıca New York yerel 08 varyantıyla, yaz saati doğru ele alınarak ölçülür. Önceki aralık kırılım adaylarıyla olay çakışması raporlanır.

### W25c — EMA50/100 + yeni MACD teyidi

- **Kaynak #9:** M5 fiyat EMA50 ve EMA100 üstünde; EMA50'yi 10 pip aşma ve MACD'nin son beş barda pozitife dönmesi; beş bar dibinde stop, yarısı 2R'de çıkar, kalanı EMA50 altı dönüşte çıkar (s. 13). Short simetrik.
- **Bizim M5 deney:** `EMA50>EMA100`, son kapanmış M5 `close>EMA50`, önceki bar `close<=EMA50`, MACD(12,26,9) histogramı son 5 **tamamlanmış** bar içinde `<=0`'dan `>0`'a geçmiş ve hâlâ pozitif. Pip yerine EMA50 aşım `>=0.1 ATR14_M5`; sonraki ilk 1m long, stop önceki 5 M5 barın dibi eksi `0.1 ATR`; pozisyonun yarısı 2R'de, kalanı M5 EMA50 altı kapanışta veya 6 saatte. Stop başa başa taşınacaksa kaynak gibi 2R yarı çıkışından sonra; maliyet eklenir. Short simetrik. 10 pip ve ATR eşiği eşdeğer değildir; kripto uyarlaması ayrı hipotezdir.

## 3. Joseph Buckley — 100'den Fazla Alım Satım ve Yatırım Stratejisi

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 21/Baskı 21/100_den Fazla Alım Satım ve Yatırım Stratejisi - Pratik Rehber - Joseph Buckley (157 sayfa) - @eseckal.pdf>) · [Tam metin](03_hundred_strategies.txt)

Bu bir strateji kataloğu: risk paritesi/portföy tahsisi (s. 8–10), çiftler işlemi (s. 42–45), ETF rotasyonu (s. 66–70), faktör ve momentum yatırımı (s. 89–90), teknik analiz/formasyon/price action (s. 121–129), ayrıca hisse/opsiyon/tahvil/özel sermaye yöntemleri bulunur. Hisse temel verisi, opsiyon zinciri, tahvil nakit akışı ve birleşme haberleri gerektiren başlıklar eldeki kripto OHLCV ile uygulanabilir değildir. Teknik formasyon anlatımı önceki partilerle örtüşür; ek sinyal sütunu yapılmaz.

### B25 — Kesitsel kripto momentumunu risk dengesiyle birleştirme

- **Kaynak fikri:** Son aylarda göreli fiyat gücü yüksek varlıkları seçmek (s. 89); portföyde sermaye yerine risk katkısını dengelemek (s. 8–9). Kitap kripto, pencere, rebalance veya kârlılık sınırı tanımlamaz. Bu birleşim **bizim araştırma tasarımımız**, kaynağın tek bir hazır sistemi değildir.
- **Bizim D1 portföy sözleşmesi:** Her UTC hafta sonunda, o gün itibarıyla listeli ve önceden tanımlı likidite eşiğini geçen spot kripto evreni. Son 90 tamamlanmış D1 gününün fiyat getirisi sıralaması; son 7 günü çıkar (`return[t-90:t-7]`), ilk 5 varlık seçilir. Son 30 tamamlanmış D1 log getiri standart sapması `sigma_i`; hedef ağırlık `min(0.30, c/sigma_i)` normalizasyonuyla, toplam brüt ağırlık en çok 1 ve nakit kalana gider. Sinyal sonraki ilk 1m fiyatla haftalık rebalance; her varlıkta 2 ATR14_D1 koruyucu stop veya gelecek hafta yeniden seçimde çıkış. 90/7/5/30/0.30 ve stop bizim sabit hipotezlerimiz. İki varlık aynı şoka maruz kalabileceğinden ters oynaklık gerçek eşit risk katkısı **değildir**; tam risk paritesi için zamanında tahminli kovaryans ve optimizasyon ayrı varyanttır.
- **Karşılaştırma:** Eşit ağırlıklı aynı top-5, yalnız momentum, yalnız ters oynaklık ve BTC buy-and-hold; delist, işlem görebilirlik, turnover, kapasite, komisyon ve point-in-time evren. Çoklu varlık portföyü tek varlık işlem sinyaliyle aynı metrikte çift sayılmaz.

## Kayıt ve öncelik

Önce W25b kutu kuralının önceki kırılım ailelerine ilave değerini ve B25 portföy seçiminin basit karşılaştırmalara göre maliyet sonrası sonucunu sınamak mantıklı. T25 ve W25a/c yüksek frekans, veri kalitesi ve spread nedeniyle ayrı kuyrukta. Kaynak örnekleri veya yazar performansı kanıt değildir. Bütün adaylarda kapanmış mum, giriş anı, stop/hedef sırası, ücret/spread/kayma, point-in-time evren ve zaman sıralı dış örneklem kaydedilecektir.

