# Kitap okuma 066 — Ölçülü dikdörtgen, düşen üç yöntem, perakende pozisyonlanması

**Kapsam:** Üç PDF'nin gerçek **40 + 48 + 80 = 168 sayfası** sıralı metne çıkarılıp incelendi. Atıflar PDF sayfasıdır. Sayısal eşikler kaynakta yoksa **bizim test tanımımızdır**. Backtest, paper test ve emir yapılmadı.

## 1. Forex GDP — Forex Grafik Desenleri: Eksiksiz Bir Kılavuz

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Forex Grafik Desenleri - Eksiksiz Bir Kılavuz - Forex GDP (40 sayfa) - @eseckal.pdf>) · [Tam metin](01_patterns_gdp.txt)

**Kaynak:** Flama/bayrak için trend yönünde kırılım ve ilk hareketin boyunu hedef alma s. 4–7. Dikdörtgende yatay sıkışma sonrası kırılım ve **dikdörtgen yüksekliği kadar** ölçülü hareket s. 7–9. Çift tepe/dipte ara boyun seviyesinin kırılması ve şekil yüksekliği hedefi s. 15–20. Üçgenlerde kırılım ve ilk dalga mesafesi hedefi s. 26–34. Sahte kırılım ve desen seçme belirsizliği s. 35–36. Desenlerin “kesin” sonuç verdiği ifadeler bağımsız örneklem kanıtı değildir; içeriğin çoğu önceki desen kitaplarıyla örtüşür.

### FG66 — Trend içi dikdörtgen kırılımında dondurulmuş yükseklik hedefi

- **Yapı:** H4 kapalı barlarında öncesindeki 20 H4 `EMA20[t−1]>EMA20[t−6]` long trendi (short ters). Sonraki 8–24 barlık yatay kutunun tamamlanmış yüksekleri içinde iki teyitli swing high ve düşükleri içinde iki teyitli swing low; 2 sol/2 sağ teyit, iki high farkı ve iki low farkı ayrı ayrı `≤0,25×ATR14_H4`. İkinci çift pivot teyidinde kutu üst/alt sınırları iki high/low ortalamaları olarak **dondurulur**. Kutunun yüksekliği `H=upper−lower≥0,5×ATR`; sonraki fiyatla kutu çizilmez. Pencere, pivot ve tolerans bizim tanımımızdır.
- **Tetik/çıkış:** Pivot teyidinden sonraki en çok 12 H4 içinde ilk `close>upper+0,1×ATR` long, short alt sınır simetriği. Sinyal kapanışı sonrası ilk uygulanabilir 1m giriş. Long stop `lower−0,1×ATR`, short `upper+0,1×ATR`; hedef long `upper+H`, short `lower−H` ve en geç 24 H4 süre. Hedef giriş fiyatının kazanç yönünde değilse veya başlangıç ödül/risk `<1` ise sinyali atla. Stop yanlış tarafta/maliyetten dar ise atla; aynı 1m stop önce.
- **Karşılaştırma:** Aynı olaylarda sabit 2R hedef, kutu yüksekliği hedefi ve kutu kırılımı olmayan trend sinyali. Önceki dikdörtgen/üçgen adaylarıyla işlem örtüşmesi; yalnız hedef değişiminin net R, dolum ve süre etkisi. Kitaptaki diğer katalog desenleri yeni bağımsız aday sayılmaz.

## 2. Mum Çubuklarını Anlamak — yazar belirtilmemiş

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Mum Çubuklarını Anlamak (48 sayfa) - @eseckal.pdf>) · [Tam metin](02_candles_understanding.txt)

**Kaynak:** İlk 42 sayfa boğa/ayı dönüş ve devam mumlarının kataloğu; son 6 sayfa temel mum açıklamalarıdır. Ayı **düşen üç yöntem**: düşüş trendinde büyük ayı mumu, onun high–low aralığı içinde kalan iki ila beş küçük ara mum, ardından ilk mumun altına yeni dip yapan ayı devam mumu (s. 21). Kaynak ara mumların üçle sınırlı olmadığını özellikle belirtir. Yutan mum ve üçlü dışarıda yukarı s. 28, 32; doji ve önceki trend bağlamı s. 46–48. “Güvenilirlik” etiketleri bu PDF'de yöntem ve sayısal örneklemle desteklenmez.

### UC66 — Düşen üç yöntemde ilk mum aralığı içinde kısa duraklama

- **Rejim/kalıp:** UTC D1 kapalı mumlarında ilk mumdan önce EMA20 düşüyor ve kapanış EMA20 altında. İlk mum ayı, gövde `≥1,2×ATR14_D1`. Sonraki **2–5** kapalı mumun her biri `high≤first.high`, `low≥first.low` ve gövde `≤0,5×first.body`; renk serbest. Son mum ayı ve `close<first.low−0,1×ATR14`. İki-beş ara mum kaynaktır; EMA/gövde/ATR eşikleri bizim sayısallaştırmamızdır. Desen ancak son mum kapandığında bilinir.
- **İcra/risk:** Son mum kapanışı sonrası ilk uygulanabilir 1m short. Stop `max(first.high, middle.high_max)+0,1×ATR14_D1`; 2R ya da 20 D1 süre. Stop yanlış tarafta/maliyetten dar ise atla, aynı 1m stop önce. Aynı sinyalde ara mum aralığı kuralı çıkarılmış kol ve yalın 5–8 bar düşük kırılımı kolu; önceki ayı bayrak/flama adaylarıyla olay çakışması, net R ve işlem sayısı karşılaştırılır. Kripto D1 UTC barlarının hisse seansı açılış boşluğuna sahip olduğu varsayılmaz.

## 3. Blue Edge Financial — EDGE Trading Sırları

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/EDGE Trading Sırları - Blue Edge Financial (80 sayfa) - @eseckal.pdf>) · [Tam metin](03_edge_secrets.txt)

**Kaynak:** Kitap FX perakende uzun/kısa konumlanmasını Myfxbook, Oanda, FXCM/DailyFX gibi kaynaklardan izlemeyi önerir (s. 9–15). %50 üstü net long'a karşı short ve %50 altı net long'a karşı long şeklinde basit ters yön filtresi s. 16'da verilir; fakat aynı kitap duyarlılık düzeyinin trend devamını tek başına öngörmediğini de söyler (s. 16, 20). FXCM hesap örneği 2014–15 döneminde ortalama kazanç/kayıp asimetrisini gösterir (s. 48–55); bu nedensellik veya kripto stratejisi başarısı kanıtı değildir. Grid/martingale ve gerçekleşmemiş zararın gizlenmesi riskleri s. 46, 74–77'de. “Akıllı para her perakende işlemin karşı tarafıdır” varsayımı gözlenmiş piyasa verisi değildir.

### BE66 — Perakende konumlanma karşı yön filtresi (FX verisine kadar ertelendi)

- **Gerekli veri:** En az bir sağlayıcı için tarihsel **yayın anı damgalı** FX uzun/kısa pozisyon oranı; veri kapsamı, hesap evreni, değişen metodoloji ve revizyonlar korunmalı. Bugün gösterilen web sayfasını eski barlara geriye doğru doldurmak veya borsa open interest'ini aynı seri saymak yasak. Mevcut yerel kripto OHLCV bu bilgiyi içermez; aday mevcut kripto backtest/paper kuyruğuna alınmaz.
- **Gelecekteki FX hipotezi:** EUR/USD H4 barı kapanmadan önce yayımlanmış en son Myfxbook net long yüzdesi `>55` ise yalnız short, `<45` ise yalnız long; 45–55 arası işlem yok. `%55/%45` nötr tamponu bizim ön seçimimiz, kaynağın yalın `%50` filtresi ayrı kol. Sinyal için aynı anda gözlenen 20 H4 kapanış kırılımı ve EMA20 yönü; giriş sonraki uygulanabilir 1m, stop karşı 10 H4 uç ±0,1 ATR14, 2R veya 24 H4 süre. Bunlar kaynak stratejisini eksik yerlerinden tamamlayan deneysel sözleşmedir, veri gelene dek performans iddiası yok.
- **Karşılaştırma:** Aynı FX kırılımını duyarlılık filtresiz ve ters filtreyle eşleştir; farklı sağlayıcılardaki seri farkı, veri gecikmesi ve örneklem dışı dönem ölçülür. İşlem başına başlangıç stopu, kaldıraç tavanı ve **mark-to-market** maksimum düşüş raporu zorunludur; zarar büyüdükçe pozisyon ekleme yok. Kitaptaki perakende hesap gözlemi tek başına sinyalin beklenen getirisini belirlemez.

## Ortak test sözleşmesi

FG66/UC66 kapanmış OHLCV ve teyitli pivotlarla üretilebilir; BE66 ayrıca tarihsel yayın damgalı FX pozisyonlanma verisi gerektirir. Giriş/çıkışta uygulanabilir 1m fiyat, ücret, spread, kayma, perpetual funding (uygun piyasada), eksik veri ve çakışan pozisyon politikası gerekir. Zaman sıralı ayrılmış doğrulamada işlem sayısı, net R, maksimum düşüş ve yalın taban çizgileri olmadan kârlılık iddiası kurulmaz.
