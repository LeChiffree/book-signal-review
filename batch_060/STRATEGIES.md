# Kitap okuma 060 — Hisse açılış koşucusu, hacimli üçgen, MA20 swing

**Kapsam:** PDF gerçekte **101 + 81 + 95 = 277 sayfa**. “H1 Stratejisi” dosya adında 113 sayfa yazsa da PDF sayacı **101**; günlüğe gerçek sayı girildi. Üç PDF'nin tüm sayfaları sıralı metne çıkarıldı. Atıflar PDF sayfasıdır. Backtest, paper test ve emir yapılmadı. Kodlanabilir ek eşikler kaynakta yoksa **bizim test tanımımızdır**.

## 1. Brian P. Anderson — H1 Stratejisi / High Volume Runners

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/H1 Stratejisi - Brian P.Anderson (113 sayfa) - @eseckal.pdf>) · [Tam metin](01_h1_anderson.txt)

**Kaynak:** Başlığa rağmen kitap H1 grafik stratejisi değil, **NYSE/Nasdaq/AMEX düşük fiyatlı hisselerde** ilk işlem saatinin yüksek hacimli koşucularını seçer. 1–10 USD fiyat, saat dilimine göre normal hacmin ≥30 katı, o gün ≥30.000 adet ve önceki kapanışa göre ≥%4 seçici (s. 50–52, 98). İlk 15 dakikalık açılış aralığı high üstünde stop-limit alım, açılış aralığı geri çekilme low'u altında stop (s. 59–63, 100). Yakın geçmiş satışları, büyük gerçek gap ve üstteki 30/50/200 D1 SMA kırmızı; yakın destek, uzun dar taban ve yeni yüksek yeşil filtrelerdir (s. 53–56, 99). Giriş öncesi üstte en az 3R direnç alanı (s. 65), 5m ile stopu lehe taşıma (s. 65–71). Seçilmiş %100+ hisse örnekleri (s. 8–16) strateji beklentisi kanıtı değildir.

### BA60 — Seans açılışında yüksek hacimli hisse koşucusu (kripto için ertelendi)

- **Uygunluk:** Gerçek borsa açılışı, işlem dışı gece, hisse adet hacmi, piyasa evreni ve anlık hisse tarayıcısı kaynağın ayırt edici girdileridir. 7/24 BTC/ETH'de keyfi UTC saati “açılış”, işlem boşluğunu “gap”, coin hacmini 30.000 hisse saymak kaynak stratejisi olmaz. Bu aday **mevcut kripto backtest/paper kuyruğuna alınmaz**; yalnız point-in-time hisse evreni ve seans verisi sağlanınca araştırılır.
- **Gelecekteki hisse sözleşmesi:** O günün NYSE/Nasdaq/AMEX kote evrenini, split/delist düzeltmelerini ve hayatta kalma yanlılığını koruyan tarihsel veri. İlk 20 dakikada işlem anında 1–10 USD, önceki **tam seans** kapanışa göre ≥%4, o ana kadar ≥30.000 adet, o dakikaya özgü önceki 20 seans aynı dakika kümülatif hacim medyanına göre ≥30×. İlerideki tam gün hacmi seçiciye girmez. İlk 15 dakikalık high/low 09:45 `America/New_York` yerel saatte dondurulur; ilk 15 dakika içinde alım yok. Sonraki 45 dakikada high+1 tick kırılırsa gerçek stop-limit emri, dolum gecikmesi/kayma ve emrin limit nedeniyle dolmama ihtimaliyle modellenir. Stop, emirden önce gözlenmiş açılış aralığı low−1 tick; yanlış tarafta/çok dar ise atla. Üstte önceden teyitli günlük direnç 3R'den yakınsa atla; 3R veya seans sonu süre çıkışı **bizim** sabit sadeleştirme. Kaynak gerçek zamanlı satış ve trailing içerir; bunlar ayrı kollar. Haber veya gap seçimini gün kapanışından sonra geriye dönük yapma.
- **Karşılaştırma:** Batch053 GS53 gibi gerçek seans/gap adaylarıyla farklı olay türüdür; ancak aynı veri ve maliyetlerle açılış aralığı kırılımı taban çizgisiyle karşılaştırılabilir. Kriptoya zorla taşınması beklenen performansı anlamsızlaştırır.

## 2. Ankya — Price Action Kalıpları

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Price Action Kalıpları - Ankya (81 sayfa) - @eseckal.pdf>) · [Tam metin](02_price_action_ankya.txt)

**Kaynak:** Kitap 13 boğa ve 13 ayı formasyonunu kataloglar (s. 1–5, 40); çizimlerin çoğu daha önceki bayrak/kama/ikili dip adaylarıyla örtüşür. Yükselen devam üçgeninde yatay üst sınır + yükselen dip çizgisi ve üst sınır **üstünde kapanış** teyidi (s. 6), formasyon boyunca azalan hacim ve kırılımda hacim sıçraması (s. 7). Alçalan devam üçgeninde simetrik yapı ve hacim şartı (s. 46–49). Bayrak/flamada direk ve oluşum sırasında azalan hacim, kırılımda artış (s. 20–23, 28–30). Buradaki ayrıştırıcı iddia yalnız şekil değil, **hacim doğrulaması**dır; katalog genel başarı oranı veya işlem örneklemi sunmaz.

### AK60 — Teyitli yatay sınır/yükselen dip üçgeninde hacim daralması ve kırılımı

- **Ön yapı:** H4 OHLCV'de 2 sol/2 sağ tamamlanmış barla teyitli iki swing high `|H2−H1|≤0,25×ATR14_H4` ve iki yükselen swing low `L2>L1+0,1×ATR`. İlk ve son pivot arası 8–60 H4 bar. Üst sınır iki high ortalaması, alt çizgi iki low'dan geçer; **dördüncü pivot teyidinde** ikisi dondurulur. Sonraki pivotlarla geçmiş şekil yeniden çizilmez. Önceki 20 H4'te EMA50 artıyor ve fiyat EMA50 üstünde; short için yatay iki low + düşen iki high ve ters trend. Pivot toleransı/pencere bizim sabitlememizdir.
- **Hacim hipotezi:** Son pivot teyidi anında, yapı içindeki son 6 kapanmış H4 barın medyan base-volume'u ilk 6'nın en çok %80'i olmalı; breakout H4 `volume≥1,5×önceki20 H4 volume medyanı`, hesapta breakout barı medyana dahil değil. Hacim birimi/sözleşme değişimi ve eksik barlar dışlanır. Aynı şekil sinyallerinde **hacim filtresiz** kol ayrıca ölçülür; kitabın nitel “azalmalı/artmalı” ifadesini bu eşiklerle aynîleştirme.
- **Giriş/çıkış:** Üst sınır üstünde H4 `close>upper+0,1×ATR` ilk kapanış (short altı) sinyal; son pivot teyidinden en çok 20 H4 sonra, öncesinde üst/alt ihlal yok. Sinyal kapanışı sonrası ilk uygulanabilir 1m giriş. Long stop son teyitli yükselen low `−0,1×ATR`, short son düşen high `+0,1×ATR`. 2R veya 24 H4 bar süre; stop yanlış tarafta/maliyetten dar ise atla, aynı 1m stop/hedefte stop önce. Üçgen yüksekliği hedefi yalnız önceden dondurulmuş ilk high–low aralığıyla ayrı kol.
- **Karşılaştırma:** Önceki üçgen/kama ve hacim kırılımı adaylarıyla olay örtüşmesi. Hacim filtresinin işlem sayısı, net R ve farklı likidite rejimlerinde ek katkısı.

## 3. Michael Roy — Swing Trading

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Swing Trading - Michael Roy (95 sayfa) - @eseckal.pdf>) · [Tam metin](03_swing_roy.txt)

**Kaynak:** Kitap büyük ölçüde piyasa/araç seçimi, temel analiz ve risk anlatır (s. 6–76). Açık işlem reçetesi s. 82'de: 20 dönem MA'nın altında kapanış bekle; sonra hem MA20 hem önceki gün high üstünde kapanan ilk mumda al; stop 1 ATR veya önceki low; 1,5 ATR kârda yarısını kapat; kalanını 3 günlük low altında kapanışta çıkar. Hisse bağlamı için yazılmış bu kural kriptoya gerçek seans gerektirmeden aktarılabilir, fakat ortalama türü, ATR dönemi ve “önceki gün” sabitlenmeli. Sabit %1 işlem riski önerisi (s. 83, 86) ve demo dolumunun gerçek piyasadan ayrılabileceği uyarısı (s. 39–42) önemlidir; kitap kârlılık örneklemi vermez.

### MR60 — D1 MA20 geri kazanımı, 1,5 ATR parçalı kâr ve üç gün low izleyen çıkış

- **Sinyal:** UTC D1 kapanmış mumlarda **SMA20** ve Wilder ATR14 (MA türü/dönem bizim seçimimiz), en az 100 D1 ısınma. Long, önceki tam D1 bar `close[t−1]<SMA20[t−1]` iken mevcut tamamlanmış D1 `close[t]>SMA20[t]` ve `close[t]>high[t−1]`. Bu kaynak s. 82'nin “MA altı kapanış sonra MA + önceki gün high üstünde kapanan ilk bar” sırasını açık yapar. Short simetrisi kaynakta bu reçetede verilmez; ana aday yalnız long, short ancak ayrı türetilmiş kol.
- **İcra/risk:** Sinyal günü kapanışı sonrası ilk uygulanabilir 1m giriş. Başlangıç stop `entry−ATR14[t]`; kaynağın alternatif önceki low stopu `min(low[t],low[t−1])−1 tick` ile ayrı kol. Stop yanlış tarafta, maliyetin iki katından dar veya pozisyon evreni dışında ise atla. İşlem başına en çok %1 özsermaye risk bütçesi sonuç raporu için üst sınırdır, backtestte tüm adaylara aynı risk tahsisi uygulanmalı.
- **Parçalı çıkış:** Giriş anında `entry+1,5×ATR14[t]` seviyesinde pozisyonun %50'si için hedef dondurulur. Kalan %50 için her yeni D1 kapanışında `close[t]<min(low[t−3:t−1])` olursa ertesi ilk uygulanabilir 1m'de çık; üç low hesabına **sinyal gününden sonra gelecekte oluşacak barı** önceden katma. Başlangıç stop kalan parça için etkin kalır; 30 D1 bar sürede zorunlu çıkış bizim güvenlik sınırımız. Aynı 1m stop ve hedefte stop önce. Karşılaştırma için aynı girişin tam pozisyon 2R hedef kolunu tut.
- **Karşılaştırma:** Önceki MA20/trend devam adaylarına karşı parçalı çıkışın marjinal net etkisi. D1 kapanış saati, masraf ve trend/yan piyasa rejimi duyarlılığı. Hisse özgü temel analizi kriptoya kopyalama.

## Ortak test notu

BA60 yalnız gerçek seanslı hisse ve point-in-time evren verisiyle; AK60/MR60 kripto OHLCV ile sınanabilir. Her kolda kapalı mum/teyitli pivot, sonraki uygulanabilir 1m dolum, ücret/spread/kayma/perpetual funding, eksik veri ve çakışan pozisyon politikası gerekir. Zaman sıralı ayrılmış doğrulama, net R, işlem sayısı, maksimum düşüş, dolum oranı ve yalın taban çizgileri olmadan kârlılık iddiası yoktur.
