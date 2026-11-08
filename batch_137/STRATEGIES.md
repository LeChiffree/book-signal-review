# Kitap okuma 137 — pivot, Bollinger ve stokastik birleşimi

**Kapsam:** Üç ayrı PDF'nin **33 + 43 + 38 = 114 sayfası** baştan sona okundu. Sayfa numaraları PDF sayfasıdır. Backtest, paper test ve emir yapılmadı.

## 1. Yalan Söylemeyen Trading Rehberi — Glennmaru

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 9/Baskı 9/Yalan Söylemeyen Trading Rehberi - Glennmaru - Alkimey Investment Clan (33 sayfa) - @eseckal.pdf>) · [Tam metin](01_glennmaru.txt)

**Tam okuma:** S. 1–7 önsöz; s. 8–10 kapanmış dönüş mumu, önceki eğim ve mum stopu; s. 11–12 önceki gün OHLC'sinden standart pivot PP/S1–S3/R1–R3; s. 13–15 stokastik 9/3/3 düzenli ve gizli ayrışma; s. 16–17 Bollinger alt/orta/üst bant ve rejim; s. 18–21 dört giriş türünü birleştiren M15 sistemi, 10–15 pip stop ve 30 pip hedef; s. 22–25 risk hesabı; s. 26–33 psikoloji, aracı ve platform. Kaynak, long dönüş için S1/S2 civarında boğa dönüş mumu, BB alt banda değme/delme, **düzenli pozitif stokastik ayrışma** ve mum kapanışı; short simetri ister (s. 18–19). Trend kolunda herhangi pivot seviye + BB orta/dış bant + gizli ayrışma vardır (s. 19). 3 pip seviye bölgesi Forex içindir, kriptoya aktarılmaz. S. 18'deki %85 geçmiş kazanma oranı doğrulanmış kayıt değildir; s. 24'teki başabaş kazanma hesabı ücret/kaymayı içermez.

### GM137A — Günlük pivot bölgesinde BB ve stokastik ayrışmalı dönüş mumu

- **Kaynak çekirdeği:** S. 11–15 ve 18–20: önceki günün klasik pivotları; M15'te dış BB ile çakışan S1/S2 veya R1/R2; stokastik 9/3/3 düzenli ayrışması; kapanmış yönlü mum; kaynak stopu mum ekstremine, hedefi Forex'te 30 pipe yerleştirir.
- **Bizim ön kayıt tanımı:** UTC gününün başlamasından önce **tamamlanmış önceki UTC günü** H/L/C ile `PP=(H+L+C)/3`, `R1=2PP−L`, `S1=2PP−H`, `R2=PP+(R1−S1)`, `S2=PP−(R1−S1)` dondur. M15 BB(20,2) kapanış serisi, stokastik %K(9) ve %D=SMA3(SMA3(%K)) kullan; kaynağın 9/3/3 SMA tanımıyla uyumlu. Longda M15 `t` barının low'u `S1` veya `S2` çevresinde `±0,1 ATR14_M15[t−1]` ve BB alt banda temas etsin. Kapanmış t boğa yutan gövde veya alt fitili en az 2×gövde olan, pozitif gövdeli çekiç olsun. Son iki **2 sol/2 sağ barla teyitli** M15 fiyat dibi arasında ikinci fiyat low daha düşükken ikinci %K dip daha yüksek ve ilk %K dip `<20` olsun. İkinci pivot ancak sağ iki bar kapandıktan sonra bilinir; t bu teyitten erken olamaz. Shortta R1/R2, üst BB, negatif ayrışma ve ayı mumu simetrik. `0,1 ATR`, pivot genişliği, mum oranı bizim mekanik seçimlerimizdir; kaynakta yoktur.
- **Giriş/risk/çıkış:** t kapanışı sonrası ilk işlem yapılabilir M1 açılışında giriş; long stop sinyal mumu low `−0,1 ATR14_M15[t−1]`, short simetri. Kar 2R; 16 M15 bar içinde hedef/stop yoksa zaman çıkışı. Tek seviyede stop sonrası aynı UTC gününde yeniden giriş yok; kaynak s. 11 bunu önerir. Ücret, gerçek bid/ask, kayma ve aynı M1 mumunda stop önceliği dahil. İşlem başına en çok %0,5 özsermaye riski. Kaynağın 30 pip hedefi ve 10–15 pip stopu kriptoya uygulanmaz.
- **Kıyas:** Pivot+mum, BB+mum ve stokastik ayrışma+mum kollarına karşı olay eşleştirmesi; üçlü uyumun işlem sıklığı, maliyet sonrası beklenti ve dış örneklem katkısı ayrı ölçülsün. [Önceki BB/stokastik birleşimleri](../batch_092/STRATEGIES.md) ile ortak olaylar çift kanıt sayılmasın. BB, pivot ve ayrışma t anında bilinen veriden dondurulmalı.

## 2. Trading Hub 2.0 — Mr. Khan

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 9/Baskı 9/Trading Hub 2.0 - Mr. Khan (43 sayfa) - @eseckal.pdf>) · [Tam metin](02_trading_hub_khan.txt)

**Tam okuma:** S. 1–9 ana/küçük yapı, BOS ve CHoCH; s. 10–13 FVG, order flow, OB ve süpürme mumu; s. 14–24 eşit tepe/dip, iç/dış ve “mühendislik” likiditesi; s. 25–30 HTF alanında LTF teyidi, tek mum, ping pong ve ölçekleme; s. 31–38 çoklu zaman dilimi ve seçilmiş GBPUSD grafik örnekleri; s. 39–43 işlem yönetimi/psikoloji. OB için önceki karşıt mum ve dengesizlik, CHoCH için arz/talep temasından sonra ilk küçük yapının kırılması anlatılır; ancak pivot tanımı, dengesizlik büyüklüğü, girişte hangi mumun kapandığı, stop ve hedef sayısal değildir. Bunlar [önceki BOS/OB/likidite adaylarıyla](../batch_054/STRATEGIES.md) aynı olay ailesidir. S. 28'deki iki yönlü “ping pong” riskten korunma, farklı varlık/pozisyon büyüklüğü ve çıkış vermeden bağımsız alpha değildir. S. 40'taki her işlemin %50 kazanma olasılığı iddiası kanıt değildir. **Yeni bağımsız aday yok.**

## 3. King of Pips Teknik Analiz Kılavuzu — Alberto Orozco

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 9/Baskı 9/King of Pips Teknik Analiz Kılavuzu - Alberto Orozco (38 sayfa) - @eseckal.pdf>) · [Tam metin](03_king_of_pips.txt)

**Tam okuma:** S. 1–6 grafik türleri; s. 7–16 destek, direnç, trend çizgisi ve kanal; s. 17–23 baş-omuz, çift tepe/dip ve yuvarlak dönüş; s. 24–29 tek günlük dönüş, bayrak/flama/üçgen/dikdörtgen; s. 29–30 fiyat boşlukları; s. 30–38 MA, Momentum, RSI, MACD ve stokastik. Çift tepe/dip için **en az bir ay** pivotlar arası süre tavsiyesi (s. 21–22) [mevcut çift dip/tepe adayının](../batch_070/STRATEGIES.md) ayrı süre filtresi olabilir; bağımsız sinyal değil. Simetrik üçgende kırılımın yaklaşık üçte iki oluşum mesafesinde gelmesi (s. 27), [önceki üçgen adaylarına](../batch_003/STRATEGIES.md) filtre olarak denenebilir; üçgen apex'ini sinyal anında teyitli iki kenarın ileri uzatımından hesaplamak gerekir. Hacim yön asimetrisi (yukarı kırılımda artış, aşağıda zorunlu değil) s. 8–15 ve 27–29'da tekrarlanır; sonraki hacimle geriye dönük sinyal seçilmemeli. Göstergeler ve dönüş kalıpları mevcut ailelerle örtüşür. S. 34'te RSI ekstremi “garanti” gibi sunulur, fakat aynı sayfa hemen dönüşün zorunlu olmadığını söyler; performans kanıtı sayılmaz. **Yeni bağımsız aday yok.**

## Sonuç

**1 yeni araştırma adayı:** GM137A. Diğer iki kitaptaki ayrıntılar mevcut adaylara filtre veya ikinci kaynak olarak not edildi.
