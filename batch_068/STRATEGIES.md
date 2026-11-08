# Kitap okuma 068 — MACD/EMA geri çekilmesi, sıkışma kırılımı, Asya aralığı süpürmesi

**Kapsam:** Üç PDF'nin gerçek **95 + 63 + 14 = 172 sayfası** sıralı metne çıkarılıp incelendi. Atıflar PDF sayfasıdır. Kaynağın vermediği sayısal eşikler **bizim test tanımımızdır**. Backtest, paper test ve emir yapılmadı.

## 1. Dinamit TNT Forex Sistemi — yazar belirtilmemiş

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Dinamit TNT Forex Sistemi (95 sayfa) - @eseckal.pdf>) · [Tam metin](01_tnt_forex.txt)

**Kaynak:** H1 yeni trend MACD(12,26,9) kesişimi, EMA6/23 yön teyidi, ilk küçük geri çekilme sonunda Stochastic(5,3,3) dönüşüyle giriş (s. 8–16, 24–25). Parabolic SAR opsiyonel (s. 13, 24), uzun MACD(30,60,30) devam/trend ayrımında kullanılır (s. 9–10). Kaynak H1 EMA6'ya 10 pip yakınlık, EMA23 ötesinde stop ve yaklaşık 3R hedef önerir (s. 25–26); yakın karşı direnç/destek sinyali reddetme nedeni (s. 46). Sistem kendi ifadesiyle takdire bağlıdır (s. 46); aşağıdaki kapalı mum sürümü bir araştırma uyarlamasıdır. Pip eşikleri kripto için fiyatla ölçeklenmelidir.

### TNT68 — MACD yeni trendi, EMA6/23 teyidi ve ilk stokastik geri çekilme

- **Kurulum:** H1 kapalı barlarında MACD(12,26,9) çizgisi sinyal EMA9'u yukarı kestiğinde long kurulum başlar. Sonraki en çok altı H1 içinde EMA6>EMA23 ve `close>EMA23` teyidi gelsin; tersi short. EMA teyidi gelmedenki stokastik olay giriş değildir. MACD ve EMA yönü işlem anında hâlâ aynı olmalı. Altı bar penceresi bizim tanımımızdır.
- **İlk geri çekilme/tetik:** EMA teyidinden sonraki en çok 12 H1 içinde ilk `low≤EMA6` long geri çekilmesi (short `high≥EMA6`); sonrasında Stochastic(5,3,3) `%K` `%D`'yi kapalı H1'de yukarı keserse ve `|close−EMA6|≤0,5×ATR14_H1` ise long, short ters. Geri çekilme öncesinde aynı yönde bir stochastic kesişim varsa onu giriş sayma; ilk geri çekilmenin tek tetik hakkı vardır. Kaynaktaki stokastik çizgi renk/çeviri karmaşası nedeniyle standart `%K/%D` yorumu kullanılır; bu yorumu ve 0,5 ATR yakınlığı bizim uygulamamız olarak kaydet.
- **İcra/risk:** Tetik kapanışından sonraki ilk uygulanabilir 1m giriş. Long stop `EMA23[t]−0,25×ATR14_H1`, short `EMA23[t]+0,25×ATR`; stop yanlış tarafta/maliyetten dar ise atla. 3R hedef veya 24 H1 süre, karşı MACD kesişimi daha önceyse sonraki 1m çıkış; aynı 1m stop önce. Kaynağın opsiyonel SAR ve uzun MACD filtreleri ayrı kollar; yalın EMA6/23 geri çekilmesi ve önceki EMA/MACD adaylarıyla net R, gecikme, işlem çakışması karşılaştırılır.

## 2. AxiTrader / Sam Eder — Kazandıran Forex Trading Sistemi

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Kazandıran Forex Trading Sistemi - Axi Trader - Orijinal (63 sayfa) - @eseckal.pdf>) · [Tam metin](02_axi_system.txt)

**Kaynak:** Piyasa tipini ve sakin yatay sıkışmayı girişten önce belirleme s. 7–12. GBP/USD örneğinde düşük volatilite kurulumu, ardından **15m mumun Bollinger üst bandı üzerinde kapanması** long tetiktir (s. 14–16); alt yön simetrisi s. 16'da önerilir. Kaynak, stopu karşı banda koyup en az 3:1 potansiyeli değerlendirir (s. 16). Setup ve giriş ayrımı, alt zaman diliminde teyit s. 14–20, 30. Yeniden giriş ve risk yönetimi s. 29, 33–53. Kitaptaki örnek sonuçlar stratejinin tüm piyasalarda getirisi değildir.

### AX68 — H1 Bollinger sıkışması sonrası M15 bant dışı kapanış

- **Setup:** H1 kapalı barlarında Bollinger(20,2) bant genişliği `(upper−lower)/SMA20` önceki 120 H1 içindeki 20. yüzdelik dilimin altında ve son sekiz H1 kapanışı bandın içinde; kurulum ancak sekizinci H1 kapanışında dondurulur. Bollinger dönemi/çarpanı ve dilim eşiği kaynakta yok, bizim seçimimizdir. Sinyal sırasında yalnız geçmiş 120 bar yüzdeliği kullanılır, kurulum sonrası bant seviyesi geriye kaydırılmaz.
- **Tetik:** Kurulumdan sonraki en çok 16 M15 içinde ilk `close>M15_BBupper(20,2)` long veya `close<M15_BBlower` short; bu bar tamamlanmadan sinyal yok. Aynı M15'te iki yön birden koşul verirse atla. Giriş kapanış sonrası ilk uygulanabilir 1m. Stop long tetik anındaki karşı M15 alt bant `−0,1×ATR14_M15`, short üst bant `+0,1×ATR`; 3R hedef veya 32 M15 süre. İlk ödül/risk ve stop mesafesi maliyete uygun değilse atla; aynı 1m stop önce.
- **Karşılaştırma:** Aynı sıkışmada üst/alt kutu sınırı kırılımı, Bollinger filtresiz M15 bant kırılımı, önceki BB/squeeze adayları; net R, yalancı kırılım ve rejime göre işlem sayısı. Kitabın yeniden giriş/pozisyon ekleme fikirleri aynı olayın ayrı risk kollarıdır, ana sinyale gizlice eklenmez.

## 3. Beat The Market Maker — Piyasa Yapıcı Tuzakları

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Piyasa Yapıcı Tuzakları - Beat The Market Maker (14 sayfa) - @eseckal.pdf>) · [Tam metin](03_market_maker_traps.txt)

**Kaynak:** Kısa broşür Asya aralığının aşılması, bekleyen emirlerin tetiklenmesi, sonra gün içi uçtan dönüş anlatır (s. 6–12). “Az sayıda aktör tüm FX piyasasını kontrol ediyor”, herkesi hedef alıyor ve stopların nerede olduğu biliniyor iddiaları (s. 6–10) bu PDF'de emir defteri/örneklem verisiyle kanıtlanmaz. Gelecekten bilinen “günün yüksek/düşük seviyesi belirlendikten sonra” (s. 12) giriş şartı olamaz. Aşağıdaki hipotez yalnız fiyat olayını test eder; gizli fail/motivasyon atfetmez.

### BT68 — FX Asya aralığı üstü/altı sahte kırılım ve geri kapanış (veri koşullu)

- **Veri/uygunluk:** Gerçek EUR/USD bid/ask ve M15 geçmişi, DST'ye göre `Asia/Tokyo` seans çıpası ve likidite koşulları gerekir. Ana test için her Tokyo yerel gününde 09:00–15:00 tamamlanmış M15 barlarının high/low aralığı 15:00'te dondurulur. Bu pencere kaynakta sabitlenmemiştir, bizim test tanımımızdır. 7/24 BTC/ETH'de “Asya seansı” aynı yapısal olay değildir; kripto ana kuyruğuna alınmaz.
- **Sinyal:** Aralık dondurulduktan sonraki en çok 16 M15 içinde `high>range_high+0,1×ATR14_M15` fakat tam M15 `close<range_high` ilk yukarı sahte kırılımı short; `low<range_low−0,1×ATR` fakat `close>range_low` ilk aşağı sahte kırılımı long. Aynı günde ilk olaydan yalnız bir işlem; başka bir aralık ihlalinin önce gelmesi sinyali iptal eder. Günün nihai high/low'u ve gelecekteki dönüş bilgisi kullanılmaz.
- **İcra/risk:** Sinyal kapanışı sonrası ilk uygulanabilir 1m giriş. Short stop sinyal high `+0,1×ATR`, long low `−0,1×ATR`; hedef aralığın orta noktası veya 12 M15 süre. Hedef lehte değil/ilk ödül-risk `<1` ise atla; aynı 1m stop önce. Yalın Asya aralığı kırılımı ve önceki likidite süpürmesi adaylarıyla aynı FX maliyetleri altında karşılaştır. Veri sağlanana kadar yalnız tanımlı hipotezdir; kurumsal manipülasyon kanıtı değildir.

## Ortak test sözleşmesi

TNT68/AX68 kapalı OHLCV ile üretilebilir; BT68 tarihsel FX seans ve bid/ask verisi gerektirir. Tümünde sonraki uygulanabilir 1m dolum, ücret, spread, kayma, eksik veri, çakışan pozisyon politikası ve uygun piyasada funding modellenir. Zaman sıralı ayrılmış doğrulamada işlem sayısı, net R, maksimum düşüş ve yalın taban çizgisi olmadan kârlılık iddiası kurulmaz.
