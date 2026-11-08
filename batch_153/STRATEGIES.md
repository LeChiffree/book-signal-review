# Kitap okuma 153 — Payapa bölgeleri ve formasyon tekrarları

Üç ayrı PDF'nin **47 + 23 + 18 = 88 sayfası** baştan sona okundu. **Yeni bağımsız strateji adayı: 0.** Bu turda backtest, paper test veya emir yapılmadı. Kaynak sayfaları PDF sayfasıdır.

## 1. Payapa Trading Stratejisi

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 7/Baskı 7/Payapa Trading Stratejisi (47 sayfa) - @eseckal.pdf>) · [tam metin](01_payapa.txt) · görsel sayfalar [1](payapa_contact_1.jpg), [2](payapa_contact_2.jpg), [3](payapa_contact_3.jpg), [4](payapa_contact_4.jpg)

**Tam okuma:** s. 1–5 giriş, H1/M15, son 10 işlem günü H/L ve gösterge ayarı; s. 6–9 ilk grafik örnekleri; s. 10–11 gün ayırıcı ve 10 günlük tepe/dip/bölge; s. 12–29 çizilmiş bölge, reddetme, RSI ve trend çizgisi örnekleri; s. 30–44 bölge kırılımı sonrası Fibonacci %123,6–138,2 ve çok sayıda seçilmiş grafik; s. 45–47 kapanış. Metin katmanı boş olan grafik ağırlıklı sayfaların tamamı görsel temas sayfalarında ayrıca incelendi.

**Karar:** Kitap s. 11'de son 10 günün en yüksek/en düşük düzeyini sabitler; “çok fazla reddedilmenin olduğu” ikinci düzeyi, bölge genişliğini ve reddetme mumunu açık algoritmayla tanımlamaz. s. 5'te CCI(2200), RSI(1), SMA15 ve EMA5 ayarları vardır; bunların eşik/kesişim ve işleme bağlanma sırası yoktur. s. 30'daki %123,6–138,2 uzatma bandı için hangi iki doğrulanmış pivotun hangi yönde çizileceği belirsizdir. Grafikler aynı kurulumun bağımsız işlem listesi değildir. [10 günlük düzey/kırılım](../batch_118/STRATEGIES.md), [Fibonacci uzatma](../batch_035/STRATEGIES.md), [likidite ve seviye tepki](../batch_081/STRATEGIES.md) ile örtüşür. Sadece yeni oran veya seçilmiş çizim için bağımsız aday açılmadı. İleride ayrı alt kol düşünülürse pivot teyidi, çizim yönü, bölge genişliği, kapalı ret mumu ve stop önce sabitlenmeli; bunu özgün Payapa performansı diye sunmamalı.

## 2. Temel Formasyonlar Rehberi — Branko Petruci

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 22/Baskı 22/Temel Formasyonlar Rehberi - Branko Petruci - Strateji Petruci - Coin Borsaları Rehber (23 sayfa) - @eseckal.pdf>) · [tam metin](02_patterns_petruci.txt)

**Tam okuma:** s. 1–2 kapak; 3–5 bayrak/flama; 6–8 üçgen türleri; 9–11 takoz; 12–13 çift tepe/dip; 14–15 omuz-baş-omuz; 16–17 trend çizgisi; 18–22 SMA/EMA açıklaması; 23 kapanış.

**Karar:** Yükselen/alçalan üçgende yatay düzey kırılımı ve hacim vurgusu s. 6–7'de, çift tepe/dip boyun kırılımı s. 12–13'te, baş-omuz boyun kırılımı s. 14–15'te anlatılır. Bunlar [üçgen](../batch_003/STRATEGIES.md), [çift tepe/dip](../batch_035/STRATEGIES.md) ve [baş-omuz](../batch_070/STRATEGIES.md) adaylarının aynı olay aileleridir. s. 18–22 MA dönemlerinin tanıtımı yeni giriş/stop/çıkış kuralı değildir. Yeni aday yok.

## 3. Order Block ile Gelişmiş Trading Rehberi — Raymond M. Smith

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 20/Baskı 20/Order Block ile Gelişmiş Trading Rehberi - Raymond M. Smith (18 sayfa) - @eseckal.pdf>) · [tam metin](03_order_block_smith.txt)

**Tam okuma:** s. 1–4 emir bloğu, son karşı mum, BOS ve test edilmemiş bölge; 5–6 breaker diye anılan kırılım/retest ile devre kesici anlatısının birbirine karışması; 7–9 arz/talep, aralık ve dengesizlik; 10–12 SMC ve destek/dirençte geri çekilme; 13–15 trend/yanal yapı; 16–18 likidite ve seans.

**Karar:** s. 3–4'te impuls öncesi son karşı mum ve ilk bölge retesti, [mevcut order block](../batch_005/STRATEGIES.md) ile aynı çekirdektir. s. 5–6 kırılımın eski seviyeye retesti, [kırılım retesti](../batch_023/STRATEGIES.md) ile aynı olaydır. “Breaker block” s. 5'te bir yandan grafik seviyesi, bir yandan piyasayı durduran circuit breaker diye tanımlanır; bu iki mekanizma eşdeğer değildir. s. 8 aralık uçlarından osilatörle dönüş ve s. 11–12 destek/dirençte “sniper” giriş için objektif seviye/teyit formülü verilmez. Fiyat grafiğinden aktör emir niyeti ya da merkezi FX emir dengesizliği doğrudan gözlenmez. Yeni aday yok.

**Tekrar denetimi:** İlk seçimdeki `VWAP Trading Stratejisiyle Kolay Para - Kartik K`, [43. partide](../batch_043/STRATEGIES.md) okunan aynı içerikti; `Gün İçi Trading Stratejisi - Stock Trader` ise [109. partide](../batch_109/STRATEGIES.md) okunan aynı kitaptı. Üç ayrı, yeni kitap şartı için ikisi kapsamdan çıkarılıp yerlerine Payapa ve Raymond M. Smith kitapları alındı. Bu kopyalar kitap kütüğüne ya da aday sayısına eklenmedi.

**Parti sonucu:** Üç yeni kitap tamamlandı; **0 yeni bağımsız aday**. Kayıtlı 387 aday ileride maliyetli dış örneklem ve paper test için bekliyor.
