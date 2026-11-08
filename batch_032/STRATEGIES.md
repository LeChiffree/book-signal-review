# Kitap okuma 032 — RSI teyidi, trend yönünde scalp, çok zamanlı ayrışma

**Kapsam:** 22 + 30 + 22 = **74 PDF sayfası**. Üç kaynağın sayfa sıralı tam metni bu klasörde. Paul Dean s. 10 ve Emperor BTC s. 18 grafik sayfaları ayrıca görsel incelendi. Atıflar **PDF sayfası**dır. Kaynak kuralları ile bizim nesnel kripto deneyimiz ayrılmıştır. Backtest/paper test/emir yapılmadı.

## 1. Roman Sadowski — RSI İndikatörü +5 Sistem Trading Stratejisi

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 7/Baskı 7/RSI İndikatörü +5 Sistem Trading Stratejisi - Roman Sadowski (22 sayfa) - @eseckal.pdf>) · [Tam metin](01_rsi_five_systems.txt)

Kaynak RSI 30/70 dönüşü ve 50 merkez çizgisi (s. 6–8), 30/70 içine geri dönüşü “failure swing” diye adlandırması (s. 11–12), RSI + yutan mum (s. 16–17), RSI + MACD (s. 18–19), RSI + MA kesişimi (s. 19) ve RSI + Bollinger sıkışması (s. 20–21) anlatır. Sonuncu için verilen **150 puan** EUR/CHF'ye bağlıdır, kriptoya taşınmaz. S. 5'teki `RSI=1/(1+RS)` formülü 0–100 RSI tanımıyla tutarsızdır; deneyde açıkça Wilder RSI kullanılmalı. Kitabın EUR/CHF örnek testi sekiz, iki, bir ve sıfır işlem gibi çok küçük örnekler taşır (s. 9–10, 17–22); ücretler, dönem dışı test ve güven aralığı yoktur. S. 22'de iki işlem için %10–15 risk örneği araştırma risk bütçesi kabul edilmez.

### S32a — RSI30/70 geri girişi + yutan mum

- **Kaynak:** RSI aşırı satım/alım işareti görüldükten sonra aynı yönde yutan mum beklenir, sonraki gün açılışında giriş örneklenir; karşı RSI seviyesiyle çıkış önerilir (s. 16–17). Aşırı seviye ile mum arasındaki azami bekleme sayısı, RSI periyodu ve “yutan” tanımı net değildir.
- **Bizim D1 sözleşmesi:** Wilder RSI14 tam UTC D1 kapanışında `<=30` olayından sonraki en çok **10 kapanmış D1** bar içinde ilk boğa gövde yutma: `close[t]>open[t]`, `close[t-1]<open[t-1]`, `open[t]<=close[t-1]`, `close[t]>=open[t-1]`; long sinyal t kapanışında, giriş sonraki ilk 1m. Short için RSI≥70 ve simetrik ayı gövde yutma. Sinyalden önce RSI karşı eşik veya yeni ekstremum gelirse eski kurulum iptal; aynı yönde tek aktif kurulum. Stop mum dip/tepe dışına `0.1 ATR14_D1`, hedef 2R veya azami H7D. 10 bar, yutma gövde yorumu, stop tamponu ve 2R **bizim** parametrelerimizdir. Ayrı çıkış kolu kaynak önerisine yakın olarak long için sonraki RSI≥70, short için RSI≤30; azami süre ikisinde de zorunlu.
- **Karşılaştırma:** Aynı RSI ekstremum havuzunda yalnız 30/70 geri dönüşü ile yutan mum teyidi; daha önceki RSI + mum adaylarıyla sinyal eşdeğerliği. “Failure swing” burada yalnız aşırı bölgeden geri dönüş anlamında kullanılır; literatürdeki çok salınımlı biçimle karıştırılmaz.

### S32b — RSI ekstremumu ardından MACD sinyal kesişimi

- **Kaynak:** RSI aşırı alım/satım sinyali ve MACD sinyal çizgisi geçişi birlikte; göstergelerden herhangi biri ters çıkış verince kapanış (s. 18–19). Kaynak, teyidin kaç bar içinde olması gerektiğini söylemez.
- **Bizim D1 filtre deneyi:** Önceki en çok 10 kapanmış bar içinde RSI14≤30 görüldüyse ve `MACD(12,26,9)[t] > signal[t]` ile `[t−1] <=` ise long; short RSI≥70 ve aşağı MACD çaprazı. Ertesi ilk 1m giriş, 1.5 ATR14_D1 stop, 2R/H7D çıkış; ters MACD çaprazında erken çıkış ayrı kol. MACD kesişimi RSI ekstremumundan önce olamaz; tek kurulum, pencerede tekrarlar yeni sinyal değil. Eşik/pencere/stop kaynakça değil deney kararı.
- **Eşdeğerlik:** Önceki RSI+MACD aileleriyle aynı olaylar çıkarsa yeni bağımsız sinyal diye saklanmaz. RSI+MA ve RSI+Bollinger kombinasyonları zaten var olan özellik ailelerine çok yakın ve kaynakta ek kesin zamanlama vermediği için bu partide yeni uygulama sözleşmesi olarak çoğaltılmadı.

## 2. Paul Dean — RSI Ölçeklendirme Stratejisi

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 7/Baskı 7/RSI Ölçeklendirme Stratejisi - Paul Dean (30 sayfa) - @eseckal.pdf>) · [Tam metin](02_rsi_scaling_dean.txt) · [İncelenen grafik](dean_page10.png)

Kaynak, aslında **RSI PRO Scalping**: M5 RSI8, RSI üzerinde SMA3, fiyat üzerinde MA24 (s. 6, 10, 26–29). Yukarı trendde RSI ve fiyat birlikte yukarı dönen “vadi”, aşağı trendde birlikte aşağı dönen “zirve” girişidir (s. 10–11, 15–16, 19–21). RSI Paint v1.04 sinyalleri ve PR/NR/ND kavramları başka kitap/özel göstergeye bağlıdır (s. 3, 8, 12–14, 23–26); bu PDF tek başına onları tam hesaplama kuralıyla vermiyor. Stop alternatifi ATR3 + spread; ATR24 genel aralık göstergesi (s. 29–30). S. 9'daki “neredeyse sıfır aleyhte hareket” ve büyük pozisyon önerisi örnek seçimiyle desteklenmez. S. 4–5 günlük getiri anlatımı uygulanabilir performans delili değildir.

### P32 — M5 RSI8 ve fiyatın eşzamanlı vadi/zirve teyidi

- **Bizim nesnel yorum:** Tam M5 `t−1` itibarıyla long rejim `close> SMA24(close)` ve `SMA24[t−1]>SMA24[t−5]`; short simetrik. RSI8 Wilder ve onun `SMA3`'ü yalnız kapanmış barlardan. Long dönüş: `RSI8[t−2] < RSI8[t−3]`, `RSI8[t−1] > RSI8[t−2]` (RSI vadisi t−2'de **t−1 kapanınca** teyit); aynı anda fiyat için `close[t−2]<close[t−3]`, `close[t−1]>close[t−2]`. Ayrıca RSI8[t−1]>SMA3(RSI8)[t−1]`. `t−1` kapanınca sinyal, `t` içindeki ilk uygulanabilir 1m fiyatında long. Short için `>`/`<` simetriği ile tepe. Bu keskin üç bar vadi/zirve ve SMA filtresi **bizim** kodlanabilir yorumumuzdur; grafikteki okların birebir yeniden üretimi iddia edilmez.
- **Risk:** `ATR3_M5[t−1] + uygulanabilir spread` asgari stop mesafesi kaynakla uyumlu başlangıç; aynı zamanda stopun işlem maliyetinden en az 2 kat büyük olması ve likidite eşiği araştırma koruması. 2R hedef, en çok 12 M5 bar, kapanmış M5'te RSI ve fiyat birlikte karşı yöne dönerse çıkış ayrı varyant. Kaynak kesin hedef/süre vermiyor. Bir trendde tekrarlı sinyaller için yalnız ilk sinyal ana kol, tekrar giriş ayrı kol; günlük kâr hedefi veya kayıp telafi amacıyla pozisyon büyütme yok.
- **Karşılaştırma:** M5 RSI8 dönüşü yalnız / fiyatla eşzamanlı / SMA24 trend filtresi. Batch030 EMA scalp ile aynı sembol-zaman örneklerinde maliyet sonrası ve sinyal örtüşmesi. Haber ve Forex seans yorumları kriptoya doğrudan kopyalanmaz.

## 3. Emperor BTC — RSI Uyumsuzlukları

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 8/Baskı 8/RSI Uyumsuzlukları - Empreror BTC (22 sayfa) - @eseckal.pdf>) · [Tam metin](03_rsi_divergence_emperor.txt) · [İncelenen örnek](emperor_page18.png)

Kaynak normal güçlü/orta/zayıf ve gizli ayrışmaları fiyat ile RSI dip/tepelerine göre ayırır (s. 7–14). Güçlü boğa: fiyat daha düşük dip, RSI daha yüksek dip; orta: eşit fiyat dibi, RSI daha yüksek dip; zayıf: fiyat daha düşük dip, eşit RSI; gizli boğa: fiyat daha yüksek dip ve RSI daha düşük dip (s. 7–10). Ayı örnekleri simetrik (s. 11–14). RSI kapanıştan hesaplandığı için fitilin ürettiği tepe/dip ile RSI'yı yanlış eşlemek konusunda uyarır (s. 16). Örnek kurgu önce yüksek zaman dilimi seviye/ayrışma, sonra düşük zaman diliminde **yapı kırılması veya aralık** teyidi, stop/hedef fiyat yapısına dayalıdır (s. 15, 18–21). S. 18 görselinde D1 ayı ayrışması, H4 yapı değişimi/retest, üst aralıkta stop ve alttaki seviyeler hedef olarak çizilir. D1 ayrışma tek başına giriş sayılmaz (s. 18–19).

### E32 — D1 RSI14 ayrışma yönü + H4 yapı kırılması

- **Bizim D1 sinyal:** Yalnız **teyit edilmiş** iki D1 pivot yüksekliği (solda/sağda 2 bar; ikinci pivot ancak sağdaki iki D1 kapanınca bilinir), `close` tepeleri ve aynı pivot barlarındaki Wilder RSI14 karşılaştırılır. Ayı yönü için ikinci fiyat **kapanış** tepesi > ilk tepe ve ikinci RSI tepesi < ilk RSI tepesi; boğa tersi. Eşitlik için önceden sabitlenmiş `0.1 ATR14_D1` fiyat toleransı ve 2 RSI puanı ayrı orta/zayıf kollar; gizli ayrışma trend devamı kolu ve klasik ters dönüşle karıştırılmaz. Pivot tarihi sinyal tarihi olarak geriye yazılmaz.
- **Bizim H4 tetik:** D1 teyidinden sonraki en çok 15 tam H4 barda, ayı için son teyitli H4 pivot dibinin **altında kapanış**, boğa için son teyitli H4 pivot tepesinin üstünde kapanış. Pivot da kırılmadan önce sağ onaylı olmalı. Kırılım sonrası sonraki ilk 1m giriş; H4 kırılım seviyesi retesti ayrı, en çok 6 H4 barlık varyant. Stop son H4 karşıt pivot ötesine `0.1 ATR14_H4`; hedef önceki tamamlanmış D1 destek/dirençten >1R koşuluyla veya 2R; azami H7D. Toleranslar, pencereler, pivot genişliği ve 2R bizim somutlaştırmamızdır.
- **Kontrol:** Aynı teyitli pivotlarda D1 ayrışma tek başına, H4 yapı kırılması tek başına ve ikisi birlikte; batch031 R31'deki H4 RSI8/50 ekstremum modelinden farklıdır. Ulaşılamayan/teyit beklerken kaçan sinyalleri de raporla. Örneğin tarihsel BTC tepesini sonradan seçmek ileriye bakma hatası yaratır.

## Öncelik

E32 iki zaman dilimli teyidin ek değerini ölçmek için, P32 ise M5'te işlem maliyetini aşma koşuluyla adaydır. S32 birleşimleri önce eski RSI özellikleriyle eşdeğerlikten geçirilir. Hiçbir kaynak örnek sonucu kriptoda kârlılık garantisi vermez; tüm ölçüm point-in-time evren, sonraki uygulanabilir fiyat, ücret/spread/kayma/funding ve zaman sıralı dış örneklem gerektirir.
