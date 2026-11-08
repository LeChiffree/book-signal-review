# Kitap okuma 201 — çatal geometrisi, RDS ve gün içi işlem

Üç yeni PDF'nin **1.181 sayfası** sayfa bazında metne çıkarılıp tarandı; kural sayfaları ayrıntılı incelendi. RDS PDF'sinin Türkçe ve İngilizce bölümleri aynı eserin iki dildeki tekrarıdır; PDF sayfası sayısına ikisi de dahildir. **Yeni nesnel, kapalı mum strateji adayı: 1.** Backtest, paper test ve emir yapılmadı. Sayfalar PDF sayfasıdır.

## 1. Mircea Dologa — Entegre Çatal Analizi (423 sayfa)

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 11/Baskı 11/Entegre Çatal Analizi - Dr. Mircea Dologa (423 sayfa) - @eseckal.pdf>) · [tam metin](01_integrated_pitchfork_dologa.txt)

**Tam okuma:** S. 1–65 pivot/çapa seçimi ve çatal kurma; 66–139 medyan/uyarı/tetik çizgileri; 140–221 çoklu çatal, Schiff ve aksiyon/reaksiyon; 222–300 gap/Fibonacci; 301–365 enerji dikdörtgenleri ve çoklu zaman dilimi; 366–423 örnek, para yönetimi ve sözlük. Çatallar için s. 35–65 pivot/çapa seçimi grafiği gördükten sonra değişebiliyor; tepe/dibin kaç sağ barla teyit edileceği, birden çok geçerli pivot arasındaki öncelik ve çizgiyi yeniden kurma zamanı tek mekanik kuralla verilmemiş. S. 301–324'teki dar aralık dikdörtgenleri mevcut sıkışma/kutu kırılım ailesine yakın. İleride çatal geometrisi test edilecekse sağ bar teyidi, çapa sıralaması ve her revizyonun işlem anı önceden kayıtlanmalı. **Yeni bağımsız aday: 0.**

## 2. Stephanie Radkay — RDS Forex Sistemi (562 sayfa)

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 10/Baskı 10/RDS Forex Sistemi - Stephanie Radkay - Türkçe ve İngilizce (562 sayfa) - @eseckal.pdf>) · [tam metin](02_rds_forex_radkay.txt)

**Tam okuma:** Türkçe s. 1–159 piyasa, olay, risk ve hazırlık; 160–209 RDS'nin beş kuralı; 210–280 örnek ve uygulama; İngilizce s. 281–562 aynı içeriğin özgün tekrarı, kural özeti s. 441–489. S. 162–163 güncel seans high/low orta noktası; s. 169–170 önceki seans kapanışı; s. 188–193 önceki beş günün ortalama `high−low` aralığından nötr fiyat çevresinde kademeler ve iki kademe geri çekilme; s. 194–205 M15 yön değişimi ve RSI(8) 25/75; s. 205–209 beş kuralın birlikte kullanımı. Kaynak yöntemi açıkça **takdire dayalı** sayar; aşağıdaki dar yorum kaynak sisteminin aynen tekrarı değil, sınanabilir hipotezdir.

### SR201A — RDS yön kapısı ve iki kademe geri çekilme dönüşü

- **Kaynak fikri:** PDF s. 162–170, 188–193, 194–209; İngilizce karşılık s. 443–453, 469–489. Yön için güncel gün/son beş gün orta noktaları ve önceki kapanış; beklenen hareket ölçeği için beş tamamlanmış günün ortalama `H−L` aralığı; tersine dönüş penceresinde RSI8 `<=25` long veya `>=75` short. Kaynakta “göze çarpan” tepe/dip ve tam dönüş anı yorumla seçilir; aşağıdaki 8 bar, 2 bar ve toleranslar bizim ön kayıtlı sayısallaştırmamızdır.
- **Zaman/veri:** Spot FX için tek bir likit paritede M15 ve seans OHLC; seans sınırı `America/New_York` saatiyle 17:00, DST takvimiyle. Her seans başlangıcında `N=önceki tam seans kapanışı`, `R=mean(H−L, önceki 5 tam seans)`, `step=R/4`, `W=(önceki 5 tam seansın max(H)+min(L))/2` dondurulur. `R<=0` veya eksik beş seans varsa sinyal yok. `D_t=(mevcut seansın yalnız t'ye dek bitmiş M15 barlarının max(H)+min(L))/2`; karar barı kapanmadan güncel high/low eklenmez. Kaynak RDS haftalık orta noktası için tam bitmiş hafta yerine beş gün kullanabilir; bu pilot seçimidir.
- **Long kurulumu:** Son 8 **tamamlanmış** M15 bardaki önceki yerel yüksekten sinyal öncesi gözlenmiş en düşük noktaya düşüş `>=2×step` ve bu düşüş süresince en az bir `RSI8<=25`; kurulum dibi `L*` ve daha önce gözlenmiş yüksek kaydedilir. Kurulumdan sonraki en çok 8 kapanmış M15 barda ilk `close_t>max(H[t−2:t−1])`, `close_t>N`, `close_t>W` ve `close_t>D_t` ise long. Short simetrik: `>=2×step` yükseliş, RSI8 `>=75`, sonra `close_t<min(L[t−2:t−1])` ve üç yön kapısının altında kapanış. Aynı bar hem kurulum hem teyit olamaz; 8 bar geçerse kurulum iptal. Bu açık yön değişimi, kaynak s. 194–199'un takdire dayalı fırsat penceresi yerine kullandığımız **nedensel vekildir**.
- **İcra/çıkış:** Sinyal M15 kapanışından sonraki ilk uygulanabilir M1 açılışında giriş; long ilk stop `min(L*, entry−step)−0.1×step`, short simetri. Stop mesafesi giriş fiyatının yanlış tarafındaysa işlem yok. Ana hedef girişten **2×step** lehe hareket; ayrı duyarlılık `1×step`, kaynak s. 192–193'te bir ila iki kademe hedefler. Karşı yön kapısında (`close_t<N` ve `close_t<D_t` long için) sonraki M1'de erken çık; 16 M15 bar zaman çıkışı. Stop M1'de ilk gerçek aşım ve gap/kayma ile yürütülür; aynı M1'de hedef/stop sıra bilinmiyorsa kötümser dolum.
- **Risk/kıyas:** İlk stop mesafesine göre özsermayenin en çok `%0,25`i, toplam maruziyet `1×`; aynı seans/paritede bir açık pozisyon ve bir kurulumdan tek giriş. `N/D/W` kapıları olmadan aynı RSI+iki kademe dönüşü, yalnız orta nokta kapısı ve klasik RSI25/75 dönüşü ayrı karşılaştırılır. EUR/USD/GBP/USD/JPY pip, spread, swap, gece seansı, likidite ve DST ile dış örneklem ayrımı raporlanır. Kitabın örnek sonuçları ileri performans kanıtı değildir; kaynakta kullanılan %1,25 hesap riski bu pilotta uygulanmıyor.

## 3. Justin Kuepper — Day Trading (196 sayfa)

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 11/Baskı 11/Day Trading - Justin Kuepper (196 sayfa) - @eseckal.pdf>) · [tam metin](03_day_trading_kuepper.txt)

**Tam okuma:** S. 1–75 piyasa, ürün, emir ve gün içi yatırımcı ekonomisi; 76–107 grafik, destek/direnç ve kırılım; 108–139 MA, MACD, osilatör ve hacim; 140–180 plan, sistem ve uygulama; 181–196 risk yönetimi. S. 99–105 yükselen üçgen ve seviye kırılımı, s. 118–129 MACD/RSI ve s. 161–178 sistem kurma, önceki arşiv aileleriyle örtüşüyor. Örnekler genel ilke/parametre önerileri; yeni ve kaynaktan tekil tanımlı giriş-çıkış mekanizması çıkmadı. **Yeni aday: 0.**

**Parti sonucu:** 3 PDF, **1.181 sayfa**, **1 yeni doğrulanmamış aday**. Kümülatif **603 PDF, 39.622 sayfa, 440 doğrulanmamış aday**.
