# Kitap okuma 029 — yüksek/düşük MA kanalı ve pivot dönüşü

**Kapsam:** 192 + 24 + 58 = **274 PDF sayfası**. Sayfa sıralı tam metinler aynı klasörde. Atıflar PDF sayfasıdır. Kaynak eşikleri ve bizim kripto uyarlamamız ayrılmıştır. Backtest, paper test veya emir yapılmadı.

## 1. Jacob Bernstein — 30 Günde Piyasa Ustalığı

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 4/Baskı 4/30 Günde Piyasa Ustalığı - Jacob Bernstein (192 sayfa) - @eseckal.pdf>) · [Tam metin](01_market_mastery_bernstein.txt)

Kitabın genel çerçevesi **kurulum → tetik → takip/çıkış** (s. 10–12). Mevsimsel örnekler, eski vadeli kontrat grafikleri ve COT verisi (s. 27–54, 135–150) kripto OHLCV'den çıkmaz. Momentum28 ayrışması s. 55–87, yüksek/düşük fiyat hareketli ortalama kanalı s. 88–100, 8 bar açılış/kapanış ortalaması s. 127–130. Tarihi örnek kâr tabloları bugünkü kripto getirisi değildir. Kitap s. 99'da MAC yönteminin tam mekanik kullanılmamasını kendi önerisi olarak da belirtir; aşağıdaki koşullar yalnız sınanabilir hipotezdir.

### B29a — İki tam barla SMA(high,10) dışına taşma

- **Kaynak:** `MAH=SMA10(high)`, `MAL=SMA8(low)`; bütün OHLC bar MAH üzerinde iki ardışık bar long tetik, bütün bar MAL altında iki ardışık bar short tetik (s. 88–89). İlk iki tam barın **tamamının** kanal dışında olması, yalnız kapanış kırılımından farklıdır. Karşıt ortalama trend içinde destek/direnç olarak yorumlanır (s. 89, 94–95).
- **Bizim D1 deney:** Tam kapanmış UTC D1 `low[t-1]>MAH[t-1]` ve `low[t]>MAH[t]`, önceki barla başlayan seride daha önce aynı yönde tetik yoksa long; short `high[t-1]<MAL[t-1]` ve `high[t]<MAL[t]`. Ortalamalar her barın kendi kapanmış OHLC'siyle hesaplanır; sinyal ancak `t` bitince bilinir. Sonraki ilk 1m'de giriş. Long stop `entry-2*(MAH[t]-MAL[t])`, short simetrik; genişlik sıfır/negatif veya stop yanlış taraftaysa işlem yok. Hedef 2R/H7D; ayrıca tam karşıt iki bar sinyali geldiğinde çıkış ayrı varyant. `2 kanal genişliği` kaynakta s. 95'te swing uygulamasına bağlanır; burada temel kırılım deneyine aktarımı **bizim** seçimimizdir.
- **Karşılaştırma:** Aynı MAH/MAL olaylarında tek tam bar, iki tam bar, yalnız kapanış üstünde iki bar. Önceki kanal/kırılım aileleriyle sinyal çakışması raporlanır. S. 95'teki beş tam bar girişinin altıncı bar açılışı ve beş bar aralığı hedefi ayrı kol olabilir; ilk iki bar varyantıyla aynı sinyal ailesi sayılır.

### B29b — SMA8(close) ve SMA8(open) kesişimi, filtre olarak

- **Kaynak:** Açılış ve kapanışın ayrı SMA8'leri kesişince yön değişimi sinyali; giriş sonraki açılış veya kapanış, fakat kitap bunun kendi başına tam ticaret sistemi olmadığını söyler (s. 127–130). Çıkışta son 8 bar aralığına eşit kısmi hedef veya kârdaysa beşinci bar çıkışı tartışılır (s. 130).
- **Bizim D1 filtre deneyi:** `SMA8(close)[t]>SMA8(open)[t]` ve önceki gün `<=` ise long yön olayı; short simetrik. Mevcut D1 trend/breakout adaylarında yalnız sinyal günü kapanmış verilerle yön filtresi olarak `SMA8(close)>SMA8(open)` kullanılır. Tek başına emir yaratmaz. Aynı olayları filtreli/filtersiz paired ölç; book kaynaklı sekiz bar hedefi istenirse ayrı çıkış kolu. Bu, zaten bulunan MA momentum sütunlarının kopyası olabilir; önce eşdeğerlik kontrolü yapılır.

## 2. 25 Trade Kuralı

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/25 Trade Kuralı (24 sayfa) - @eseckal.pdf>) · [Tam metin](02_trade_rules.txt)

Bu belge ağırlıkla işlem disiplini ve risk öğütleri içerir (s. 2–15, 18–24). Önceki gün/hafta/ay kırılımı fikirleri s. 16–18'de. **S. 16 başlığı “önceki günün aralığı” der, açıklama ise “önceki gün kapanışı” üstü/altı der:** aynı eşik değildir. S. 18–20 kârdaki pozisyona ekleme ve kaybedene eklememe önerir; pozisyon büyüklüğü için sistematik risk bütçesi tanımlamaz. Eski marjin oranlarını bugünkü borsaya varsaymayız.

### K29 — Önceki dönem ekstremumu ve kapanışı arasındaki fark

- **Kaynak:** Haftalık ve aylık yüksek/düşük kırılımını yön sinyali olarak kullanma (s. 17–18). Günlük kuralın başlık/metin uyuşmazlığı (s. 16).
- **Bizim D1 araştırma:** Her tam UTC D1 kapanışında üç **ayrı** olay: (A) `close[t]>high[t-1]`; (B) `close[t]>` önceki tamamlanmış UTC haftanın en yükseği; (C) `close[t]>` önceki tamamlanmış takvim ayının en yükseği. Short tersleri. S. 16 metin varyantı ayrıca `(D) close[t]>close[t-1]` olarak raporlanır, “aralık kırılımı” diye etiketlenmez. Her adayda ilk kapanmış kırılım sonrası ilk 1m giriş, 2 ATR14_D1 stop, 2R/H7D çıkış. Bir dönem içinde tekrar eden kapanışlar yeni olay değil; eşik dönem değişene veya fiyat tekrar altına inene kadar sinyal kilidi. Stop/hedef bizim varsayımımızdır.
- **Karşılaştırma:** Aynı varlık/tarihlerde A/B/C/D sinyallerinin örtüşmesi, ücretten sonraki sonuç, sinyal sıklığı ve rejim. Önceki Donchian/period breakout adaylarıyla eşdeğerlik kontrolü; yeni bağımsız sinyal sütunu otomatik eklenmez.

## 3. 1 Saatte Profesyonel Bir Trader Gibi Forex Piyasasında Nasıl Trade Yapılır

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 3/Baskı 3/1 Saatte Profesyonel Bir Trader Gibi Forex Piyasasında Nasıl Trade Yapılır (58 sayfa) - @eseckal.pdf>) · [Tam metin](03_one_hour_forex.txt)

Metin pivot seviyeleri ve H1 trendi/M5 girişini birleştirir: EMA9/18 ve MACD iki zaman diliminde (s. 7–16); kırılmış pivot seviyesine geri çekilme ve sıradaki pivot hedefi (s. 11–15); daha sonra H1 pivot dışı **kapanışı** ek teyit olarak verir (s. 16). S. 43–45'te pivot formülü tablosu çeviri/dizgi hataları taşır: örneğin `R2=P-(S1+R1)` ve orta noktaların parantezsiz yazımı klasik pivot hesabıyla tutarlı değildir. S. 42, olay sırasında pivotları yeniden hesaplamayı önerir; bu geçmiş veriden tahmin edilen sabit seviyeyi değiştireceği için testimizde kullanılmaz. Haftalık pip/kazanç iddiaları (s. 15, 55–57) doğrulanmış sonuç sayılmaz.

### H29 — Önceki gün sabit pivot kırılımı ve ilk retest

- **Kaynak:** Önceki seans OHLC ile pivot seviyesi, fiyatın seviyeyi kırması ve ona geri dönüşte H1/M5 MACD teyidiyle giriş, bir sonraki pivot hedefi (s. 9–16, 43–46). Kaynak “pivotun mümkün olduğunca yakınında” der, tolerans vermez.
- **Bizim H1/M5 sözleşmesi:** Önceki **tam UTC D1** `P=(H+L+C)/3`, `R1=2P-L`, `S1=2P-H`, `R2=P+(H-L)`, `S2=P-(H-L)`; ara seviyeler `M=(komşu iki seviyenin aritmetik ortalaması)` olarak **bizim düzeltilmiş hesap standardımızdır**, PDF tablosunun birebir kodu değildir. Gün boyunca seviyeler sabit. H1 ilk `close>R1+0.1 ATR14_H1` long; son tamamlanmış H1 `EMA9>EMA18` ve MACD(12,26,9) çizgisi sinyal üstünde; sonraki 6 M5 barda ilk `low<=R1+0.1 ATR` ve `close>=R1` retestte sonraki ilk 1m long, M5 MACD sinyal çizgisi `>0` olmalı. Stop retest M5 dibi `-0.1 ATR14_M5`, hedef sonraki yüksek sabit pivot `R2` yalnız `R2>entry+risk` ise; aksi durumda işlem yok. En geç UTC gün sonu çıkış. Short `S1/S2` simetrik. Pencereler, ATR ve hedef/risk eşiği bizim deney kurallarıdır.
- **Karşılaştırma:** Pivot kırılımına hemen giriş, ilk retest sonrası giriş ve H1/M5 teyitli retest; sabit seviyeye dönmeyen kurulumlar raporlanır. Önceki pivot/retest ailesiyle aynı olay havuzu. D1/H1/M5 kapanışı oluşmadan bilgi kullanma, aynı 1m mumda stop önceliği.

## Sıradaki test için öncelik

B29a kanalın **tam bar** şartı kaynakta açık ve mevcut breakout özelliklerinden ayrıştırılabilir. H29 pivot retesti ancak sabit önceki gün seviyeleriyle ve tutarlı veriyle denenir. K29 dönem kırılımları daha çok mevcut özelliklerle eşdeğerlik denetimidir. Bütün adaylarda point-in-time evren, ücret/spread/kayma/funding, gerçekçi dolum, stop önceliği ve zaman sıralı dış örneklem gerekir. Kaynak örnekleri başarı garantisi vermez.
