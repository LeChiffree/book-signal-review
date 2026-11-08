# Kitap okuma 027 — H4/D1 sistemler, H1 teyit ve ICT seans kavramları

**Kapsam:** 34 + 32 + 86 = **152 PDF sayfası**. Sayfa sıralı tam metin yan dosyalardadır. ICT dosyası aynı notların yaklaşık ilk 43 sayfa Türkçe, sonraki 43 sayfa İngilizce tekrarını içerir; 86 farklı strateji/sayfa fikri sayılmaz. Atıflar PDF sayfasıdır. Kaynak eşikleri ile bizim kripto deney sözleşmemiz ayrı tutulur. Backtest, paper test veya emir yok.

## 1. Thomas Carter — 17 Forex Trading Stratejisi

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 8/Baskı 8/17 Forex Trading Stratejisi - Thomas Carter (34 sayfa) - @eseckal.pdf>) · [Tam metin](01_seventeen_forex.txt)

On yedi kısa H4/D1 forex tarifi içerir (s. 4–33). D1 iç bar/SMA21 (s. 4–5), SMA dizilimi (s. 11), EMA5/50 ve ADR10 (s. 13), EMA100/stochastic (s. 14–15), SMA20/40 ve ATR20 yapı kırılımı (s. 20–24), SMA150/RSI3/stochastic (s. 25) öne çıkanlar. Pip stopları kriptoya taşınmaz. #15'te gösterge EMA9/EMA21 iken kural EMA9/EMA26 der (s. 27); kodlanmadan önce iki ayrı varyant gerekir. #3 ters yön haftalık kapanış sistemi (s. 7–8) düşük ödül/yüksek risk ve forex hafta saati bağımlılığı nedeniyle düşük önceliklidir.

### C27a — D1 iç bar ve SMA21 trendi

- **Kaynak #1:** `high[t]<high[t-1]` ve `low[t]>low[t-1]` iç bar; SMA21 yönünde, iç bar uçlarının 5 pip dışına bekleyen kırılım emri, sabit forex pip stop ve stop kadar hedef (s. 4–5).
- **Bizim D1 sözleşmesi:** Tam kapanmış UTC D1 iç bar; `SMA21[t]>SMA21[t-3]` ve `close[t]>SMA21[t]` long, short simetrik. Sonraki 2 D1 gün içinde `high >= high[t]+0.1 ATR14_D1[t]` olduğunda ilk 1m stop order dolum; stop iç bar dibi `-0.1 ATR`, hedef 1R ve 2R ayrı varyant, H3D zaman çıkışı. Aynı 1m içinde iki yön görülürse önceden seçili yön dışında işlem yok; stop/hedef sırası belirsizliğinde stop önceliği. `3 gün eğim`, ATR tamponu, iki gün geçerlilik ve 2R bizim eşiklerimiz.
- **Karşılaştırma:** Önceki iç bar adaylarının aynı olaylarında SMA21 trend filtresi var/yok; aynı kırılımı bağımsız başarı diye sayma.

### C27b — H4 SMA20/40 trend geri kazanımı ve sıkışma

- **Kaynak #12:** Kurulum H4 kapanışı iki SMA'nın üzerinde, bir önceki kapanış en az birinin altında, `HH5-LL5<2.5 ATR20`, `HH3<HH10`; sonraki üç barda HH3 dışı buy stop, LL3 stop; yarı pozisyon 0.75 ATR, kalanı 1.5 ATR veya 3-bar iz süren stop (s. 20–24). Short simetrik.
- **Bizim H4 sözleşmesi:** Kaynağın `HH3`, `HH5`, `HH10`, `LL3`, `LL5` hesapları yalnız **kurulum dahil kapanmış H4 barlardan** yapılır; `HH3<HH10` için son 10 bardaki daha eski bir tepe şarttır. Kurulum gününde EMA değil SMA20/SMA40. Kırılım için `HH3+0.1 ATR20_H4` sabitlenir; sonraki 3 H4 barda ilk 1m temasla giriş, stop `LL3-0.1 ATR`; yarısı `entry+0.75 ATR20`, kalanı `entry+1.5 ATR20`, ilk kısmi dolumdan sonra kalan stop maliyet dahil başa başa çekilir ve her kapanmış H4 sonunda yeni `LL3-0.1 ATR` ile yalnız yukarı taşınır. Short simetrik. Maksimum 3 gün; kaynak sabit pip tamponu kripto için ATR'ye çevirmek **bizim** varsayımımızdır.
- **Karşılaştırma:** Sadece SMA20/40 geri kazanımı, ek 5-bar sıkışma, ek HH3/HH10 şartı. Önceki breakout/volatilite sıkışması ailesiyle örtüşme ölçülür. ATR hesabı Wilder TR, her bar kapanışında o ana dek bilinen veridir.

## 2. Thomas Carter — 20 Forex Stratejisi

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 8/Baskı 8/20 Forex Stratejisi - Thomas Carter (32 sayfa) - @eseckal.pdf>) · [Tam metin](02_twenty_forex.txt)

Bu PDF çoğunlukla H1 forex tarifleri sunar (s. 4–31). Çoklu EMA ve osilatör kombinasyonları yoğun biçimde önceki partilerle örtüşür. #15 EMA5/21 girişine karşı çıkışta EMA5/**12** yazar (s. 25–26), tutarsız; #16 M5/M15/M30/H1 mumlarının saat başındaki aynı kapanışını birlikte okur (s. 27). Kapanmamış yüksek zaman mumu kullanılırsa lookahead olur. Aşağıda ayrı değeri daha yüksek görünen iki hipotez kaydedildi.

### C27c — H1 SMMA55 yüksek/düşük kanalı + Williams %R

- **Kaynak #5:** SMMA55 yüksek ve düşük fiyat kanalı; long için yüksek kanal üstü, Williams %R55 `>-25`, stochastic(5,5,5) çizgisi sinyal üstünde; stop son swing dip, hedef 2R veya yeniden kanal içine kapanış. Short `low SMMA55` altı, %R `<-75`, stochastic altında (s. 10–11). Kaynak mum kapanmadan agresif giriş de verir; araştırma için yalnız muhafazakâr kapanmış mum kullanılır.
- **Bizim H1 sözleşmesi:** Wilder biçimi SMMA55 ayrı `high` ve `low` serisinde; %R55 `-100*(HH55-close)/(HH55-LL55)`, stochastic `raw%K5`→SMA5→SMA5, sıfır paydada sinyal yok. İlk kapanmış H1 `close>SMMA55(high)`, `%R55>-25`, stochastic hızlı>yavaş ve önceki H1 `close<=SMMA55(high)` ise sonraki ilk 1m long. Stop iki sağ H1 barla teyitli son pivot dip `-0.1 ATR14_H1`, pivot yoksa işlem yok. Hedef 2R; ayrıca H1 kanal içine geri kapanış veya H3D süre çıkışı. Short simetrik. Pivot/tampon/zaman sınırı bizim uygulama şartımız.
- **Karşılaştırma:** Aynı kanal kırılımlarında %R ve stochastic şartlarının ayrı katkısı; önceki MA kanal adaylarıyla çakışma.

### C27d — H1 üç EMA trendi ve EMA60'a dönüş

- **Kaynak #6:** EMA5>EMA15>EMA60, EMA15 ve EMA60 yukarı eğimli iken fiyat EMA60'a döndüğünde long; short tersi; 30 pip stop/50 pip hedef (s. 12–13).
- **Bizim H1 sözleşmesi:** Önceki kapanmış H1'de EMA5>EMA15>EMA60 ve iki yavaş EMA `t>t-3` long. İzleyen en çok 12 H1 barın birinde `low<=EMA60` ve `close>EMA60` olursa sonraki ilk 1m long; EMA dizilimi giriş mumunda sürmeli. Stop o dönüş mumunun dibi `-0.1 ATR14_H1`, hedef 1.5R, H48h süre çıkışı. Short simetrik. Pips yerine yapısal stop/R bizim değişikliğimiz.
- **Karşılaştırma:** Aynı EMA diziliminde EMA60 temasını bekleme ve doğrudan giriş, bekleyen/dolmayan sinyaller dahil. Önceki trend geri çekilmesi ailesiyle birleştirilir.

## 3. 2023 ICT Mentorship GEMS (TR–ENG)

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 6/Baskı 6/2023 ICT Mentorship GEMS (TR-ENG) (86 sayfa) - @eseckal.pdf>) · [Tam metin](03_ict_gems.txt)

Bu, @SirPickle kaynaklı not/örnek koleksiyonudur; ağırlıkla **ES/NQ vadeli endeks, New York RTH** bağlamı (s. 1–42; İngilizce tekrar s. 44–86). 13:30 ve 15:00 “Judas” açılışı (s. 1–6), cuma kapanış/pazar açılış NWOG ve 17:00–18:00 NDOG (s. 7–11, 26), likidite süpürmesi + market structure shift/FVG örnekleri (s. 2–5, 28–30), 10:00–11:00 “Silver Bullet” (s. 31) anlatılır. 24/7 kriptoda vadeli endeksin seans kapanış/açılış **boşluğu aynı olay değildir**. S. 31'de “her gün %100 garantili” FVG iddiası veriyle doğrulanmış değildir ve testte ön kabul olmayacak. Birçok çizim ve jargon, işlem fiyatı/stop/süreyi tek başına tanımlamıyor.

### I27 — Önceki seans yüksek/düşük süpürmesi + kapanışlı yapısal dönüş (keşif)

- **Kaynak fikri:** Önceki seans likidite uçlarının süpürülmesi, ardından yer değiştirme/MSS ve FVG bölgesine dönüş (s. 2–5, 28–30); s. 21 piyasa yapısı değişimi için pivot altı **kapanış**ı vurgular. Kaynak bu koşulların tümü için tek ve eksiksiz mekanik kural vermez.
- **Bizim ayrı H1/M5 kripto hipotezi:** UTC 00:00–07:59 önceki oturum aralığı `R,S`. 08:00–12:00 UTC'de M5 `high>R+0.1 ATR14_M5` olup aynı veya en geç 3 M5 sonra `close<R` ise üst uç süpürmesi. Süpürmeden sonraki en çok 6 M5 kapanmış bar içinde fiyat son **önceden teyitli** 2-sol/2-sağ M5 pivot dibinin altına kapanırsa bearish MSS; ek `body/range>=0.60` ve üç bar FVG `high[t]<low[t-2]` varsa ilk FVG. Sonraki 6 M5 içinde FVG orta seviyesine ilk 1m retestte short, stop süpürme tepesinin `0.1 ATR` üstü, hedef 2R/H4h. Alt uç için simetrik. UTC seans, ATR, pivot/FVG tanımı, pencereler ve stop tamamen **bizim** yeniden üretilebilir araştırma seçimimizdir; ES/NQ saat kuralını uyguladığımız iddia edilmez.
- **Kontrol:** Süpürme tek başına, süpürme+MSS ve FVG retest kolları; üst/alt uç, likidite ve spread ayrımı. Önceki false breakout/order block/FVG adaylarıyla aynı olaylar eşleştirilir. Bu deney ancak M1/M5 veri ve maliyet modeli yeterliyse anlamlıdır.

### Ertelenenler

NWOG/NDOG, New York RTH açığı, 13:30/15:00 Judas ve 10–11 Silver Bullet orijinal ES/NQ kontratlarında, ilgili seans takvimi/tick verisi olmadan kripto sinyali olarak kuyruğa alınmaz. “Algo fiyatı çeker”, “her zaman” gibi nedensel/garantili ifadeler araştırma hipotezi sayılır. Türkçe ve İngilizce yarılar tek kaynak olarak kaydedildi.

## Test sırası ve ortak kapılar

C27b H4 kurulumu kaynakta en ayrıntılı tarif edilen yeni deney; C27a ve C27c önceki aralık/kanal ailelerinin filtre karşılaştırması; I27 yüksek frekans keşfi ve ayrı veri gerektirir. Bütün adaylar için point-in-time evren, tamamlanmış mum, sinyalden sonra dolum, spread/ücret/kayma/funding, aynı 1m mum stop önceliği ve zaman sıralı dış örneklem şarttır. Hiçbir kitap cümlesi gerçekleşmiş performans kanıtı yerine kullanılmaz.
