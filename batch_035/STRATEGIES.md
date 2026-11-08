# Kitap okuma 035 — sıkışma kırılımı, çift tepe/dip ve Fibonacci çıkışları

**Kapsam:** 15 + 9 + 37 = **61 PDF sayfası**. Sayfa sıralı tam metinler burada. Slayt ağırlıklı Fibonacci PDF'sinin grafik sayfaları 5, 6, 12, 17, 21, 24, 28, 29 ve 34 görsel incelendi. Atıflar PDF sayfasıdır; kaynak sözü ve bizim sayısal deney sözleşmemiz ayrıdır. Backtest/paper test/emir yapılmadı.

## 1. Alton Swanson — Breakout Trading

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 20/Baskı 20/Breakout Trading - Alton Swanson (15 sayfa) - @eseckal.pdf>) · [Tam metin](01_breakout_swanson.txt)

**Kaynak:** Kanal, trend çizgisi ve yatay konsolidasyon kopuşları; devam/dönüş ayrımı (s. 8–9). Üçgenlerde yükselen taban, alçalan tepe veya simetrik daralma (s. 10). Daralan volatiliteyi Bollinger veya ATR ile izle (s. 11); MACD/RSI momentumu kopuşu teyit edebilir (s. 12–13). Metin kesin mum kapanışı, lookback, stop ve çıkış kuralı vermez; “haber yoksa sahte kopuş” iddiası veriyle doğrulanmaz. Aynı aile batch029 ve batch034 kırılımlarına yakındır.

### S35 — Daralan bant sonrası yönlü kapanış kırılımı, ek filtre olarak

- **Bizim D1 deney:** Tam UTC D1 `t−1` itibarıyla Bollinger(20,2) bant genişliği `(upper−lower)/middle`, önceki 120 tamamlanmış gündeki en düşük %20'lik dilimde olsun; eşik yalnız geçmiş gözlemlerle yürüyen yüzde dilim. İlk `close[t]>max(high[t−20:t−1])` long veya `close[t]<min(low[t−20:t−1])` short. `MACD(12,26,9)` histogram işareti aynı yönde olmalı; RSI14>50/<50 ayrı filtre kolu. Giriş sonraki ilk 1m, 2 ATR14_D1 stop, 2R veya H7D çıkış. 20/120/%20/2R **bizim** varsayımlarımız; kaynak eşikleri değildir.
- **Karşılaştırma:** Batch034 N34 sıkışma ve VWMA koluyla aynı kırılım havuzunda bant sıkışması vs fiyat aralığı sıkışması; yalnız 20 gün Donchian, MACD/RSI filtreli ve filtresiz. Üçgeni sonradan seçilmiş tepe/diplerle geriye dönük tanımlama yasak; kitap buna yetecek nesnel pivot kuralları vermediği için ayrı üçgen sinyali kaydedilmedi.

## 2. Trendin Tersine Dönüş Modelleri — IFC Markets

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Trendin Tersine Dönüş Modelleri (9 sayfa) - @eseckal.pdf>) · [Tam metin](02_reversal_patterns.txt)

**Kaynak:** Baş-omuz / tersi için üç pivot ve boyun çizgisi kırılımı, hedef `N±|H−N|` (s. 2–3). Çift tepe/dipte ikinci ekstremum sonrası ara destek/direnç kırılınca formasyon tamam; hedef formasyon yüksekliği kadar projeksiyon (s. 4–5). Üçlü tepe/dip aynı mantık (s. 6–7). Elmas sağ sınır kırılımı ve yükseklik hedefi (s. 8). S. 9, formasyonun tam trend dönüşü yerine duraklama da olabileceğini söyler. “Eşit” tepe/dip toleransı, pivot onayı, stop ve süre tanımlanmaz.

### R35 — Teyitli çift tepe/dip + boyun kırılımı

- **Bizim H4 tanımı:** Pivot high/low solda 3 ve sağda 3 **tam kapanmış** H4 barla teyit edilir; olay tarihi sağ onay barının kapanışıdır. Çift tepe için art arda iki teyitli pivot high `P1,P2` arası 4–40 H4 bar, `|high[P2]−high[P1]|<=0.25 ATR14_H4[P2]`, aradaki en düşük **teyitli** pivot low `N`; `P2` onayından sonraki ilk `close[t]<N−0.1ATR14_H4[t−1]` short. Çift dip simetrik ve ara teyitli pivot high `N`. Pencere/tolerans/kırılım tamponu bizim seçimimizdir. İkinci pivotun sağındaki barlar tamamlanmadan işleme girme yok.
- **Giriş/risk/hedef:** Kırılım kapanışından sonraki ilk 1m uygulanabilir fiyatı; short stop `max(high[P1],high[P2])+0.1ATR`, hedef `N−(max(high[P1],high[P2])−N)`; long simetrik. Hedef kâr yönünde >1R değilse işlem yok, en çok 30 H4 bar sonra çıkış. Kaynak hedef projeksiyonunu verir; stop, R filtresi ve süre bizim deney şartımızdır. Boyun eğimi için iki ara pivot varsa s. 2–3 baş-omuz örneği ayrı tasarım ister; tek yatay boyunlu çift tepeye karıştırılmaz.
- **Karşılaştırma:** Aynı iki pivot olayında boyun kırılımı ile ikinci tepe/dip oluşumunda erken giriş; önceki double-top/bottom ve M/W aileleriyle eşdeğerlik. Üçlü modeller ancak üçüncü ekstremum **o sırada teyitli** olduğunda ayrı kol; bir çift tepe olayı sonradan “üçlü” diye yeniden etiketlenmez.

## 3. Manish Patel / Octa FX — Fibonacci ile TP ve SL

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 8/Baskı 8/Destek ve Direnç Seviyesi Olarak TP ve SL Bulmak İçin Fibonacciyi Anlamak - Octa FX (Manish Patel) (37 sayfa) - @eseckal.pdf>) · [Tam metin](03_fibonacci_tp_sl.txt) · [Grafik s. 6](fib_page6.png) · [Grafik s. 28](fib_page28.png)

**Kaynak:** Geri çekilme 23.6/38.2/50/61.8/78.6% (s. 2, 6), uzantı düzeyleri kaynağın iki yerinde **farklı listelenir**: s. 3'te 61.8/100/161.8/200/261.8%; s. 20'de 123.6/138.2/150/161.8/261.8%. Seçilen salınımın tepe/dip noktası ve çizimin yönü belirtilmeden düzey mutlak fiyat olamaz. Grafik s. 6, X→A itişinden sonra B geri çekilmesinde alış/satış fikrini gösterir; s. 17'de 127.2/161.8 hedef etiketleri görülür, fakat 127.2 s. 3/20 listesinde yoktur. S. 27'de kırılan destek/direnç rol değişimi; s. 28'de yükselişte destekten alış ve sonraki desteğin altına stop; s. 29–30'da seviyeyi kırdı diye hemen ters yöne giriş yapmama ve başka teknik teyit arama. Grafikler sonucunu sonradan bilinen noktaları işaretliyor; canlı sinyal sayılmaz.

### F35 — Mevcut trend girişlerinde sabitlenmiş Fibonacci çıkış varyantı

- **Bizim H4 referans:** Sadece **teyitli** iki H4 pivotla son tamamlanmış yukarı itiş `L→H` seçilir; H, sağında 3 kapanmış H4 barla teyit edilmeden Fib seviyeleri oluşmaz. `Δ=H−L>0`; long geri çekilme adayları `H−rΔ`, `r∈{0.382,0.5,0.618}`. Düşen itişte simetri. İlk kapanmış H4 `low<=level+0.1 ATR` ve `close>=level` long teyit; sonraki ilk 1m giriş. Stop bir sonraki daha derin **önceden sabit** Fib düzeyi `−0.1ATR`; örn. 0.382 girişte 0.5 altı. Stop girişin yanlış tarafında veya maliyetlerin 2 katından dar ise işlem yok. Kaynak bu teyidi/toleransı vermez; bizim hipotezdir.
- **Hedef kolu:** Long için `H` ilk hedef; devam ederse s. 20'deki 1.236 ve 1.618 projeksiyonları `L+ratio*Δ` ayrı kollar. Açık H4 barda uç/anchor yeniden seçilmez. Alternatif 2R/H14D aynı girişlerde karşılaştırılır; bu hedeflerin >1R mesafesi olmayan adaylar ayrıca sayılır. S. 17'deki 1.272 görselini liste dışı **ayrı** hassasiyet kolu diye etiketle, temel kurala sessizce ekleme.
- **Öncelik/eşdeğerlik:** Daha önceki Fibonacci pullback aileleriyle büyük ölçüde örtüşebilir; önce aynı pivot/anchor ve sinyal satırları karşılaştırılmalı. Başka trend stratejisinin aynı girişlerinde yalnız TP/SL ablation da yapılabilir; yeni alfa otomatik varsayılmaz.

## Sonraki test için not

R35, mekanik şekil/neckline sınaması için en somut yeni aday. S35 ve F35 mevcut kırılım/Fibonacci ailelerinin filtre ve çıkış varyantlarıdır. Her testte point-in-time varlık evreni, sonraki uygulanabilir fiyat, ücret/spread/kayma/funding, stop önceliği ve zaman sıralı dış örneklem gerekir. Kaynakların “olası” dönüş/kopuş anlatımı kârlılık kanıtı değildir.
