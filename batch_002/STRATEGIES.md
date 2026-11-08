# Kitap okuma 002 — MACD, RSI, kırılım

**Durum:** Üç PDF'nin 37, 50 ve 34 sayfası baştan sona okundu; toplam **121 PDF sayfası**. Kırılım kitabındaki metin çıkmayan iki akış şeması (PDF s. 32–33) ayrıca görsel incelendi. Sayfalar PDF sayfasıdır. Aşağıdakiler kârı kanıtlanmış stratejiler değil, maliyetli geri teste hazır aday sözleşmeleridir.

## 1. MACD Uzmanlığı — Lalit Mohanty

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 18/Baskı 18/MACD Uzmanlığı - Lalit Mohanty (37 sayfa) - @eseckal.pdf>)

Kitap `MACD=EMA12(close)-EMA26(close)`, `signal=EMA9(MACD)`, `hist=MACD-signal` tanımlarını veriyor (s. 8, 12–13). Kesişim, sıfır hattı, histogram eğimi ve ayrışma anlatılıyor (s. 14–18). Kripto örnekleri s. 24–26'da senaryo anlatımıdır; işlem listesi veya gerçek performans testi yok.

### M1 — MACD sinyal hattı yukarı kesişimi

- **Kitap fikri:** MACD çizgisi sinyal çizgisini yukarı keserse yükseliş sinyali; iki çizgi pozitifse trend onayı (s. 14–15).
- **Kapalı günlük olay:** `hist[t-1]<=0 && hist[t]>0`. `macd[t]>0 && signal[t]>0` ayrı **filtreli varyant**; yalın kesişimle karşılaştırılır. Kesişimden sonra oluşan fiyat verisi aynı karar satırına alınmaz.
- **Ölçüler:** `hist/ATR14`, histogramın 1 ve 5 bar değişimi, MACD çizgisi/ATR14, son 50 bar konumu, kapanışın EMA50'ye yüzde uzaklığı. Bu sütunların çoğu mevcut günlük pilotta zaten var; yeni kolon olarak kopyalanmaz.
- **Giriş/çıkış:** UTC günlük kapanıştan sonraki ilk yürütülebilir 1m açılışı; `hist<0` kapanış çıkışı ve H3D/H7D/H14D zaman çıkışı ayrı test; ATR stop ve önceden sabitlenmiş TP, 1m yolda maliyet ve funding ile. “Pozitif bölgede kesişim daha iyi” kitapta iddia, burada doğrulanmış üstünlük değildir.

### M2 — Histogram sıfır geçişi ve eğim

- **Kitap fikri:** histogramın negatiften pozitife geçmesi ve MACD eğimi (s. 17–18).
- **Karar:** Histogram sıfır geçişi **M1 ile aynı olaydır**; ikinci bağımsız strateji sayılmaz. Histogramın kesişim öncesi/sonrası eğimi ek özellik veya ablation filtresidir. MACD çizgisinin sıfır geçişi (`MACD[t-1]<=0<MACD[t]`) farklı, daha yavaş bir olay olarak ayrıca karşılaştırılabilir.

### M3 — MACD/fiyat ayrışması

- **Kitap fikri:** fiyat düşük dip yaparken histogram yüksek dip yapması (s. 14–15, 19–20).
- **Karar:** Kitap pivot teyit süresini ve iki dip arasındaki azami uzaklığı tanımlamıyor. Nedensel pivot algoritması ve olay sayısı belirlenene kadar **işlem sinyali olarak ertelendi**. Teyitli pivot tamamlanmadan geçmiş satıra ayrışma işareti yazılamaz.

## 2. RSI İndikatöründe Ustalaşmak — Lalit Mohanty

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 18/Baskı 18/RSI İndikatöründe Ustalaşmak - Lalit Mohanty (50 sayfa) - @eseckal.pdf>)

Kitap RSI14 ve 30/70 bölgelerini, 50 trend ayrımını ve fiyat/RSI ayrışmasını anlatıyor (s. 6–19). Sayısal backtest yok; vaka çalışmaları anlatı biçiminde (s. 37–39). **Kaynak içi çelişki:** s. 19'da aynı anda “RSI aşırı satım” ve “50'nin üzerinde kalma”, s. 26'da trend onayı `RSI>50` ve alışta `RSI<30` birlikte öneriliyor. Aynı mum için bu mümkün değildir; bu satırlar doğrudan kodlanmaz.

### R1 — Yükseliş rejiminde RSI geri çekilme ve toparlanma

- **Kitap fikri:** RSI trendi teyit etmek için 50 üstü; geri çekilme sonrası giriş, örnekte RSI40 civarı; RSI70 civarı çıkış (s. 17–19, 37). Kaynak çelişkisi nedeniyle aşağıdaki ardışık olay tanımı **bizim açık yorumumuzdur**.
- **Kapalı günlük olay:** `(close/EMA50-1)>0` ve EMA50 eğimi pozitif; son 5 kapalı mum içinde `RSI14<=40` görülmüş; bugün `RSI14[t-1]<=50 && RSI14[t]>50`. 40 ve 50 eşikleri ayrı duyarlılık deneyidir; aynı gün hem 40 altı hem 50 üstü gerektirilmez.
- **Ölçüler:** RSI14 seviyesi, 1/5 bar puan farkı, 50 bar konumu, `close/EMA50-1`, ADX rejimi. Bunlar pilotta büyük ölçüde mevcut.
- **Giriş/çıkış:** sonraki yürütülebilir 1m açılışı; RSI70 üzerine çıkışta kâr alma ile sabit ufuk/ATR çıkışları ayrı karşılaştırılır. Kitap örneğindeki başarılı hisse işlemi kripto kanıtı değildir.

### R2 — RSI30 altında aralık içi dönüş

- **Kitap fikri:** RSI30 altı aşırı satım / ortalamaya dönüş (s. 15–17, 26–27), fakat güçlü trendlerde uç değer kalabilir (s. 16).
- **Kapalı günlük olay:** `RSI14[t-1]<30 && RSI14[t]>=30`; yalnız önceden tanımlı yatay rejimde (`ADX14<20`) alınan sürüm ile rejimsiz sürüm karşılaştırılır. `RSI<30` gerçekleştiği anda alış ayrı adaydır, toparlanma ile aynı strateji değildir.
- **Giriş/çıkış:** günlük kapanış sonrası 1m giriş; `RSI>=50` çıkışı veya H3D/H7D/H14D ve ATR stop/TP varyantları. Güçlü düşüşte dip yakalamaya çalışmanın zararları ayrıca raporlanmalı.

### R3 — RSI ayrışması

- **Kitap fikri:** fiyat yeni dip, RSI daha yüksek dip yaparsa boğa ayrışması; tersi ayı (s. 12–14, 38).
- **Karar:** M3 ile aynı pivot teyidi sorunu var. İlk backtestte ertelenir; önce teyitli iki fiyat/RSI pivotu ve aralarındaki 5–30 bar mesafesi için nedensel olay tanımı hazırlanır.

## 3. Başarılı Koparma Ticareti — Sinisa Persic

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Başarılı Koparma Ticareti - Sinisa Persic (34 sayfa) - @eseckal.pdf>)

Kitap hisse piyasasında 1–20 gün tutulan kırılım işlemlerini anlatıyor (s. 4). Yükselen üçgen, dikdörtgen, simetrik üçgen, bayrak/flama tanımları (s. 5–8), günlük ve 15/30/60m direnç uyumu (s. 12–18), girişten önce geçersizleşme, kısmi çıkış ve takip eden stop (s. 19–33) var. Sadece seçilmiş işlem örnekleri veriliyor; sistematik performans tablosu yok.

### P1 — Günlük dar aralık kırılımı + 4h yapı uyumu

- **Kitap fikri:** günlük formasyon ve gün içi formasyon aynı dirençteyse izleme önceliği; kırılım öncesi konsolidasyon (s. 12–18, akış şeması s. 32). Kitap intraday emir verir; bizim günlük karar saatine uyarlama ayrı hipotezdir.
- **Kapalı günlük olay:** son 10 günlük `max(high)-min(low)` / ATR14 düşük yüzdelikte; `close_t > max(high[t-10:t-1])`; son altı **tamamlanmış** 4h barın tepe aralığı aynı günlük dirence `<=0.5×daily ATR` uzaklıkta. “Düşük yüzdelik”, 10 bar ve 0.5 ATR **kaynakta yoktur**, eğitim dönemi öncesinde sınırlandırılacak mekanik yorumdur.
- **Ablation:** yalnız günlük Donchian20 kırılımı; +dar aralık; +4h direnç uyumu; +hacim artışı; +haftalık piyasa rejimi. Böylece aynı bilgiyi dört kez puanlamayız.
- **Ölçüler:** konsolidasyon yaşı/genişliği, kırılım ATR mesafesi, günlük–4h direnç farkı, quote hacim oranı, BB genişlik değişimi ve kapanışın mum içi konumu. Hacim kitapta onay sayılır ama ilk kırılımda gecikebileceği belirtilir (s. 16); zorunlu filtre yerine ayrı varyant.
- **Giriş/çıkış:** günlük kapanış sonrası ilk yürütülebilir 1m açılışı; önceden teyitli aralık dibi veya ATR stop; kanal içine geri kapanış ve H3D/H7D/H14D süre çıkışı. Gün içi emirli özgün stratejiyle aynı sonuç diye sunulmaz.

### P2 — Kırılım emri tetiklenmeden önce iptal

- **Kaynak:** s. 21–22 ve görsel akış şeması s. 33. Referans destek kırılırsa bekleyen alış emri iptal edilir. Akış şeması al emrinin ertesi gün biteceğini söylüyor.
- **Uygulama adayı:** Günlük sinyalde belirlenmiş direnç üstüne **yalnız sonraki gün geçerli** koşullu giriş; girişten önce 1m fiyat yolu destek altına inerse emir iptal. Aynı 1m barda hem alış hem iptal seviyesi görüldüğünde muhafazakâr sıra tanımı gerekiyor; yalnız OHLC sırası bilinmiyorsa işlem geçersiz/olumsuz senaryo raporlanır.
- **Karşılaştırma:** P1 kapanış sonrası piyasa girişine karşı P2 koşullu emir. Bu bir uygulama farkıdır; sinyal kalitesiyle karıştırılmamalı.

### P3 — “Hızlanmazsa azalt” ve iki aşamalı çıkış

- **Kaynak:** s. 19, 22–24, 29–30; akış şeması s. 33. İlk dalgada %25–50 kısmi çıkış, kalan için hedef veya takip eden stop. Kırılım hızlanmazsa ilk kısmı kapat/azalt.
- **Mekanik aday:** Girişten sonraki ilk tamamlanmış 4h barda `max_favorable_excursion/ATR_entry` önceden belirlenmiş eşiğe ulaşmazsa pozisyonun yarısını kapat; kalan için teyitli destek/ATR trailing stop. Kısmi çıkışın ücret ve funding maliyeti tam işlem olarak sayılır. Eşik ve pencere kitaptaki sabit kural değil; önce eğitimde seçilecek.
- **Fibonacci hedefleri:** kitap s. 19, 28 kullanıyor; salınım pivotları öznel. İlk sürümde 1R/2R veya ATR hedefiyle karşılaştır, Fib sürümünü nedensel pivot tanımı sonrası aç.

### P4 — Yükselen üçgen / bayrak / flama

- **Kaynak:** s. 5–8, 25–28.
- **Karar:** Kitap çizgi toleranslarını “esnek yorum” diye bırakıyor (s. 8–10). Bu formasyonları ilk katalogda ayrı bağımsız işlem sinyali saymıyoruz. Önce iki teyitli tepe ve iki teyitli dip, eğim toleransı, azami formasyon yaşı, kırılım onayı ve olay sayısı mekanik olarak tanımlanmalı. P1 dar aralık kırılımı daha tekrarlanabilir ilk vekildir.

## İlk test paketi ve kayıt kararı

| ID | İlk durumu | Mevcut pilotla ilişki |
|---|---|---|
| M1 | Geri test adayı | MACD kesişim ve histogram sütunları mevcut; strateji kuralı yeni |
| M2 | M1'in tekrarı / ayrı MACD çizgisi sıfır olayı | Ek sütunları körlemesine üretme |
| M3 | Pivot tanımı bekliyor | Gelecek mumla çizilen ayrışma yasak |
| R1 | Geri test adayı | RSI14/EMA50 sütunları mevcut; ardışık olay kuralı yeni |
| R2 | Geri test adayı | RSI30 yukarı geçişi mevcut; ADX filtresi ablation |
| R3 | Pivot tanımı bekliyor | M3 ile aynı altyapı kullanılabilir |
| P1 | Geri test adayı | Donchian, hacim, 4h özet mevcut; direnç uyumu olayı yeni |
| P2 | Yürütme varyantı | 1m yol/sıra çözümleyicisi gerekir |
| P3 | Çıkış varyantı | Yeni feature yerine pozisyon yönetimi kuralı |
| P4 | Formasyon tanımı bekliyor | Elle çizilen şekil otomatik sayılmaz |

**Backtest/paper test çalıştırılmadı.** İlk karşılaştırma aynı parite evreni, aynı UTC karar zamanı, ücret/kayma/funding ve H3D/H7D/H14D ufuklarıyla yapılmalı. Önce yalın olay, sonra her ek filtrenin marjinal katkısı walk-forward içinde ölçülmeli. Kitaplardan hiçbiri bu piyasa için kârlılık kanıtı sunmuyor.
