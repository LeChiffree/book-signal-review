# Kitap okuma 051 — Üçgen, harmonik AB=CD ve taze bölge

**Kapsam:** 58 + 10 + 39 = **107 PDF sayfası**. Üç PDF'nin tüm sayfaları numaralı ve sıralı metne çıkarıldı. Atıflar PDF sayfasıdır. Kaynakta eksik kalan eşik ve icra seçimleri açıkça **bizim test tanımımız** olarak yazıldı. Backtest, paper test ve emir yapılmadı.

## 1. Grafik Desenleriyle Strateji Oluşturma

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Grafik Desenleriyle Strateji Oluşturma (58 sayfa) - @eseckal.pdf>) · [Tam metin](01_chart_pattern_strategy.txt)

**Kaynak:** s. 8–17 mum kalıpları, s. 19–23 desen/har­monik çizimleri, s. 28–53 çok sayıda grafik formasyonu kataloğudur. Çift tepede iki yakın tepe ve aradaki vadi kırılımı teyidi açıkça söylenir (s. 28), çift dip (s. 29), bayrak (s. 30, 37), flama (s. 33, 43), yükselen üçgenin yatay direnci ile yükselen dipleri (s. 38) tarif edilir. Yazar kendi uygulamasında yatay dirence çoklu temas ve yükselen alt çizgi/“üçüncü dokunuş” sonrası kırılım **öncesi** long almayı anlatır (s. 26–27); ancak bu tercih temel haber ve deneyime dayalı olup o anda üçgenin kesin kırılacağı bilinemez. s. 34 simetrik üçgeni hem devam hem tersine dönüş diye anlatır; yön çıkarımı tutarsızdır. s. 48 azalan üçgen alt çizgisi “daha düşük dipler” derken yatay destek çizimi ile çelişir. Bu kitap öğretici katalogdur; tek başına 58 sayfayı 58 ayrı üstünlük kanıtı saymıyoruz.

### CP51 — Yükselen üçgende teyitli direnç kırılımı

- **Bizim noktasal şekil:** H1 gerçek OHLC; yalnız 2 sol/2 sağ H1 bar kapandıktan sonra teyit edilen pivotlar. Son 80 H1 içinde en az iki teyitli tepe `≤0.25 ATR14_H1` yakınlıkta yatay direnç oluştursun; aralarında en az 4 H1 bar olsun. Son üç teyitli dip sırasıyla daha yüksek ve son dip ikinci tepe teyidinden önce oluşmuş olsun. Direnç ikinci tepe teyidinde **dondurulur**; sonraki sinyal için o tarihten sonra tekrar daha iyi çizgi seçilmez. Bu pivot sayısı, zaman aralığı ve ATR toleransı **bizim** nesnelleştirmemizdir.
- **Olay:** En son dip teyidinden sonra, en çok 20 H1 içinde ilk `close>resistance+0.1 ATR14_H1` ve `close` mum aralığının üst %25'inde long. Önceki 5 barın herhangi biri zaten aynı direnç üstünde kapanmışsa yeni giriş sayma. Üçüncü dipte, kırılım **öncesi** erken giriş kaynakta anlatılsa da, üçüncü dip ancak sağ bar teyidinden sonra bilinir ve yanlış kırılım riski yüksektir; bu kol ancak ayrı hipotez ve aynı stop/evrenle kıyaslanır.
- **İcra/risk:** Kapanış sonrası ilk uygulanabilir 1m fiyatı. Stop son teyitli yükselen dip `−0.1 ATR`, 2R hedef veya 24 H1 bar; stop yanlış tarafta veya toplam maliyetin iki katından dar ise atla. Short simetri **kaynağın bu spesifik yükselen üçgen kuralı değildir**; ayrı aday gerektirir.
- **Karşılaştırma:** Batch050 BC50 yatay kutu kırılımı, önceki üçgen/formasyon adayları ve çıplak 80 bar direnç kırılımı ile sinyal örtüşmesi; yükselen dip filtresinin net ek katkısı.

## 2. Harmonik Desenler

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Harmonik Desenler (10 sayfa) - @eseckal.pdf>) · [Tam metin](02_harmonic_patterns.txt)

**Kaynak:** Üç Sürücüde 1.27/1.618 projeksiyon ve zaman simetrisi (s. 1–2); Kelebekte B=0.786 XA ve D≈1.27 XA ile BC projeksiyon yakınsaması (s. 3); AB=CD'de C geri çekilmesi 0.618 veya 0.786 ve BC izdüşümü sırasıyla 1.618 veya 1.27 (s. 4); Yengeçte D≈1.618 XA (s. 5); Gartley'de B≈0.618 XA, D≈0.786 XA (s. 6–7); Yarasa'da D≈0.886 XA ve B<0.618 XA (s. 8). Son iki sayfa örnek çizimlerdir. “Kesin geri dönüş” ve “çok küçük stop” ifadeleri (s. 5, 8) doğrulanmış performans değildir. Pivotları geçmişe dönük en güzel uyacak biçimde seçmek ciddi ileriye bakma hatası doğurur.

### HP51 — AB=CD oran yakınsaması ve D sonrası dönüş teyidi

- **Bizim pivot/ölçüm:** H4 gerçek OHLC'de 3 sol/3 sağ kapanmış barla teyitli dönüş pivotları; ardışık dört pivot A-B-C-D yönü boğa için high-low-high-low, ayı için tersi. Her ayak 3–40 H4 bar sürsün. `AB=|B−A|`, `BC=|C−B|`, `CD=|D−C|` ve `AB>0`. `BC/AB` `[0.588,0.648]` veya `[0.756,0.816]`; sırasıyla `CD/BC` `[1.568,1.668]` veya `[1.22,1.32]`; ayrıca `CD/AB` `[0.95,1.05]`. Kaynak merkez oranları verir, ± tolerans ve süre **bizim** ön kayıt seçimimizdir. D pivotu 3 sağ bar tamamlanmadan sinyal yok; ilk uygun pivot dörtlüsünü kronolojik seç, sonra yeniden en iyi kombinasyonu arama.
- **Olay:** D teyidinden sonraki en çok 4 H4 içinde boğa için `close>high(D-pivot-bar)` ve ayı için `close<low(D-pivot-bar)` ilk kapanışı. Giriş sonraki uygulanabilir 1m. Bu fiyat teyidi kaynakta kesin formülle verilmez, **bizim** dönüş teyidimizdir. D teyidinden önce D ekstremi aşılırsa kurulum iptal.
- **İcra/risk:** Boğa stop `D_low−0.1 ATR14_H4`, ayı `D_high+0.1 ATR`; hedef C fiyatı, ancak girişten hedefe net ödül/risk <2 ise işlem yok; 20 H4 bar süre. Stop/hedef aynı 1m'de kötümser sıra. “En küçük stop” varsayımı yapılmaz; gerçek ATR ve maliyet kullanılır.
- **Karşılaştırma:** Önceki ABCD/harmonik adaylarıyla pivot ve işlem çakışması; tek başına son pivot tersine dönüşü ve yalnız AB=CD eşitliği karşısında 0.618/0.786 + BC yakınsamasının marjinal katkısı. Gartley/Yarasa/Yengeç tek PDF'de oran özeti olsa da beş pivotlu D teyidini aynı kurala karıştırma.

## 3. Kevin Baker — Kokuşmuş İndikatörlere İhtiyacımız Yok

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Kokuşmuş İndikatörlere İhtiyacımız Yok - Kevin Baker (39 sayfa) - @eseckal.pdf>) · [Tam metin](03_no_indicators_baker.txt)

**Kaynak:** Kitap indikatörlerin gerekliliğini sorgulayıp çekiç/kayan yıldız/doji ile arz-talep bölgelerine odaklanır (s. 3–7, 17). Bölge, birkaç mumluk dar aralıktan **hızlı uzaklaşma** veya pivot çevresindeki hızlı dönüşle tanımlanır (s. 10–12); yatay aralık için 3–6 mum uygun denir (s. 15). İlk dönüşte **daha önce test edilmemiş** bölgeye ağırlık verir; her temasla bölgenin tüketilebileceğini anlatır (s. 14–16, 25). Trendle aynı yönde geri çekilmede ters mumdan sonra giriş örnekleri (s. 19), fiyat bölgeye girer girmez giriş veya üst sınırdan geri çıkışı bekleme iki yaklaşımı (s. 20, 31), karşı bölge yakınsa işlemi atlama ve stopu bölge dışına koyma (s. 15, 28, 31) vardır. Son bölüm hisse opsiyonu ve hisse açılış boşluklarıdır (s. 35–38); mevcut kripto OHLCV testine eşdeğer aday değildir. s. 23'teki çok yüksek getiri örneği ile s. 28'deki 10:1/20:1 ifadeleri seçilmiş anlatımdır, genel beklenen getiri sayılmaz.

### KB51 — Yeni oluşmuş talep/arz bölgesine ilk dönüş + reddetme

- **Bizim bölge:** H1 gerçek OHLC'de ardışık 3–6 barın `max(high)−min(low)≤1.5 ATR14_H1` dar kutusu, kutudan sonraki ilk H1 kapanışı long için `>boxHigh+0.5 ATR`, short için `<boxLow−0.5 ATR`; kırılım mumunun `range≥1.5×` önceki 20 H1 medyan range. Bölge kutunun high–low aralığıdır ve **kırılım kapanışında** dondurulur; en son/ilk nitelikli kutu çakışmasını kronolojik, en kısa kutu önceliğiyle sabitle. ATR eşikleri ve kutu seçimi bizimdir, kaynak yalnız 3–6 mum/dinamik ayrılış der (s. 11–15).
- **Tazelik/olay:** Bölge oluştuktan sonraki en çok 30 H1 içinde hiç `low≤boxHigh && high≥boxLow` teması olmadıysa taze. İlk temas H1 barında long için `low≤boxHigh` ve H1 `close>boxHigh`; short için `high≥boxLow` ve `close<boxLow`. Bölgenin karşı sınırı dışında H1 kapanışta iptal; ilk temas reddetme vermese sonraki temasla yeniden giriş yok. Kaynak s. 14–16 ilk dönüşü önemser. Yukarıdaki çift yönlü tanım yalnız kaynakta anlatılan talep/arz simetrisidir.
- **İcra/risk:** Reddetme H1 kapanışından sonraki ilk uygulanabilir 1m. Long stop `boxLow−0.1 ATR`, short `boxHigh+0.1 ATR`. Sinyal anında bilinen en yakın **önceden oluşmuş karşı bölgenin** başlangıç sınırı hedef; karşı bölge yoksa 2R hedef. Net hedef/stop mesafesi <2:1 veya stop toplam maliyetin iki katından dar ise atla. Azami 24 H1 bar; aynı 1m bar stop/hedefte kötümser sıra. Kaynağın “bölgeye girer girmez” girişi ayrı limit kolu olabilir ama canlıda teyitsiz dolum riskini ve doldurulamayan emirleri ayrı saymalı.
- **Karşılaştırma:** Batch005 arz/talep, batch049 SC49 BOS retesti ve önceki fresh-zone adaylarıyla aynı bölge/olay çakışması. 3–6 bar çıkış kutusu ile yalnız swing pivot bölgesi ayrımı; ilk temas filtresinin getirdiği örneklem azalması.

## Test önceliği ve sınırlar

CP51 yükselen dip teyidi, HP51 D pivot teyidi ve KB51 kutu oluşumundan **sonraki** ilk temas sırası ilk teknik denetimlerdir. Üçü de varlık evreni point-in-time, tamamlanmış barlar, sonraki uygulanabilir 1m fiyatı, ücret/spread/kayma/funding, eksik barlar, pozisyon çakışması ve zaman sıralı dış örneklemle test edilmeli. Bu partide hiçbir adayın kârlılığı ölçülmedi.
