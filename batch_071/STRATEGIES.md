# Kitap okuma 071 — gecikmeli RSI girişi, yatay piyasa dönüşü ve ayı rejimi

**Kapsam:** Üç PDF'nin gerçek **83 + 64 + 75 = 222 sayfası** sırayla çıkarılıp incelendi; metni az olan grafik/arayüz sayfaları ayrıca [görsel olarak](figure_contacts/) kontrol edildi. Atıflar PDF sayfasıdır. Kaynağın vermediği parametreler **bizim test tanımımızdır**. Backtest, paper test ve emir yapılmadı.

## 1. Algoritmik Trading Stratejileri — Scotty Ratford

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Algoritmik Trading Stratejileri - Scotty Ratford (83 sayfa) - @eseckal.pdf>) · [Tam metin](01_algorithmic_ratford.txt)

**Kaynak taraması:** Bölüm 1 kural, çıkış ve test çerçevesi verir (s. 4–8). Bölüm 2'deki göstergelerin çoğu TradingView topluluk betiğidir (s. 10–39); sürüm, hesap formülü ve repaint davranışı sabitlenmeden bire bir yeniden üretilemez. Bölüm 3/4'te açık OHLCV kuralları da vardır: BB/RSI (s. 51–53), BB/CCI (s. 54–55), SMA15/45 ve RSI5 (s. 58), SMA9/18 geri kazanımı (s. 62–63), SMMA4/9 ve SMA15 (s. 71–72). Son bölüm bot/uyarı kurulumudur, strateji kanıtı değildir (s. 75–83). Kitabın HMA30+Stochastic kuralı (s. 49) önceki LK70 ve başka adaylarla büyük ölçüde aynıdır; yeniden ayrı sinyal sayılmadı.

### SR71A — SMA15/45 yükselişi ardından RSI5 aşırı satımdan çıkış

- **Kaynak kuralı:** Önce SMA15, SMA45'in üzerine geçer; RSI5'in 30 altına inip tekrar 30 üstüne çıkması long girişi, stop son swing low altı. Çıkış RSI70 üstünden altına dönüş (scalp) veya SMA15'in SMA45 altına geçmesi (swing) (s. 58). Bu, sıradan SMA kesişiminin **ardından** gelen geri çekilmeyi hedefler; sıra önemli.
- **Nesnel kurulum:** BTC/ETH 4h kapalı bar. `SMA15_t>SMA45_t` ve `SMA15_{t-1}≤SMA45_{t-1}` ile setup aç. Sonraki en çok 20 kapalı 4h'de RSI5<30 görülmeli; bunu izleyen en çok 5 kapalı 4h'de ilk `RSI5_{t-1}≤30<RSI5_t` tetik, SMA15>SMA45 hâlâ geçerli. 20/5 bar pencere **bizim test seçimimizdir**; aynı setup'tan tek işlem. Önceki 45 barın tamamı olmadan sinyal yok.
- **İcra/risk:** Tetik kapanışı sonrası ilk uygulanabilir 1m long. Son **onaylı** pivot low (iki sağ bar tamamlanmış) veya setup sonrası görülen minimum low altı `−0,1×ATR14_4h` stop; iki stop yöntemi ayrı kol, ileri tarihli pivot yok. İlk hedef 2R; kaynak RSI70 dönüşü ve karşı SMA kesişimi daha erken gerçekleşirse ilgili 4h kapanışı sonrası çıkış, 30 adet 4h azami süre. Stop aynı 1m'de önce. Yalın SMA15/45 kesişimi ve RSI5 geri dönüşüne karşı ek değer, işlem örtüşmesi ve net R ölçülür.

### SR71B — Yatay BB50 uç teması sonrası CCI20'nin −200 üstüne dönüşü

- **Kaynak kuralı:** Düz Bollinger(50,2) alt band teması/altına kapanış, CCI20'nin −200 altına inişi, ardından −200 üstüne geçiş long; giriş barı altına stop, üst band teması veya CCI geri dönüşü çıkışı (s. 54–55). Kitabın “bantlar düz” ifadesi sayısal değil; aşağıdaki ölçüm bize ait. Long kuralı açık, short simetrisi kitapta burada verilmediği için ilk test **yalnız long**.
- **Nesnel kurulum:** Kapanmış 1h BTC/ETH'de son 10 barın BB50 orta çizgisi mutlak değişimi `≤0,5×ATR14_1h`; `low_t≤lowerBB50_2_t` ve `CCI20_t<−200` setup. Sonraki en çok 6 kapanmış 1h'de ilk `CCI20_{t-1}≤−200<CCI20_t` tetik; tetik anında orta çizgi yatay koşulu sürmeli. Düzlük ve 6 bar bize ait.
- **İcra/risk:** Sonraki ilk uygulanabilir 1m long; stop `min(setup_low,trigger_low)−0,1×ATR14_1h`; hedef donmuş tetik üst BB bandı veya 24 adet 1h süre. Kaynaktaki “CCI aşırı satımdan sonra 100 altına düştü” çıkışı ancak önce +100 üstü görülürse anlamlıdır; ayrı kol olarak kodlanır. Girişe göre hedef lehte değil/ödül-risk <1 ise atla. Aynı 1m stop önce. Basit BB50 dokunuşu ve BB+RSI adaylarına karşı CCI ek katkısı incelenir.

## 2. Ortalama Dönüşüne Dayalı Günlük Alım Satım Stratejisi Kitabı — Rob Teally

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Ortalama Dönüşüne Dayalı Günlük Alım Satım Stratejisi Kitabı - Rob Teally (64 sayfa) - @eseckal.pdf>) · [Tam metin](02_mean_reversion_teally.txt)

**Kaynak taraması:** Kitap aşırı uzaklaşma, teyit, ortalamaya dönüş hedefi ve trend rejimi ayrımı anlatır (s. 5–28). ADX gibi trend filtresi s. 10'da gerekçelendirilir; fiyatın mutlaka döneceği iddiası doğrulanmış veri değildir. Bölüm 4'te özel TradingView gösterge sürümleri vardır (s. 29–45). Altı stratejinin bazıları bunlara bağlıdır (s. 48–53, 61–63). Standart OHLCV ile bire bir tarifli adaylar BB40/RSI5/ADX14 (s. 54–55) ve EMA200/Keltner/RSI5/ADX (s. 57–58). S. 52 short BB koşulu çeviride “alt banda dokunuyor veya üstünde” olarak çelişkili; o özel indikatör stratejisi ertelendi.

### RT71A — ADX14 düşükken BB40 dışı ve RSI5 geri dönüşü

- **Kaynak kuralı:** ADX14<25, fiyat BB(40,2) altını görürken RSI5<30; RSI 30 üstüne çıkınca long, son swing low altı stop, üst band teması çıkış. Short üst bant/RSI>70, RSI70 altına iniş, son swing high üstü stop, alt bant çıkışı (s. 54–55). Kaynak “fiyat geçiyor” der, kapalı mum teması/kapanışı ayrımını kesinleştirmez.
- **Nesnel kurulum:** BTC/ETH 1h kapalı bar. Long setup `low_t≤lowerBB40_2_t ∧ RSI5_t<30 ∧ ADX14_t<25`; sonraki en çok 6 kapanmış 1h içinde ilk RSI5 30 yukarı kesişi, tetikte ADX14<25. Short simetrisi. `low` teması seçimi ve 6 bar penceresi bizim uygulamamız; `close<lowerBB` ayrı ablation. Setup dondurulmadan önceki bant, RSI ve ADX yalnız kapanmış bar.
- **İcra/risk:** Tetik sonrası ilk uygulanabilir 1m. Long stop setup/tetik arası minimum low `−0,1×ATR14_1h`, short maksimum high `+0,1×ATR`; bu son onaylı swing vekilidir. Tetik anında donmuş karşı BB bandı hedef veya 36 adet 1h süre; hedef giriş yönünde değil/ödül-risk <1 ise atla. Aynı 1m stop önce. ADX filtresi çıkarılmış ve RSI teyidi çıkarılmış kollarla, önceki BB/RSI (LK70A dahil) adaylarıyla aynı veri/maliyet altında karşılaştır.

### RT71B — EMA200 tarafında Keltner(20,1,5) ve RSI5 ters dönüşü

- **Kaynak kuralı:** ADX<25 ve fiyat EMA200 üstündeyken alt Keltner bandı teması + RSI5<30, RSI aşırı satımdan çıkınca long; üst Keltner'e ulaşınca çıkış (s. 57). Short EMA200 altı, üst Keltner + RSI5>70, geri dönüş, alt Keltner çıkışı (s. 58). Kaynak KC orta/periyot hesabını belirtmez; varsayılan göstergeye bırakır.
- **Nesnel kurulum:** 1h kapanmış OHLCV: KC orta EMA20(typical price), bant `EMA20 ±1,5×ATR20` (bizim açık hesap seçimimiz). Long setup `ADX14<25 ∧ close>EMA200 ∧ low≤KC_lower ∧ RSI5<30`; en çok 6 kapanmış 1h içinde RSI5 30 yukarı kesişi ve filtreler hâlâ geçerli. Short ters. KC EMA/ATR periyot seçimi ve bekleme penceresi **kaynak dışı**; başka KC uygulamasını karıştırma.
- **İcra/risk:** Sonraki ilk 1m long/short; long stop setup-tetik minimum low `−0,1×ATR14`, short maksimum high `+0,1×ATR`; karşı KC bandı tetikte donmuş hedef veya 36 adet 1h süre. Stop önce, yetersiz ilk ödül/risk atlanır. RT71A ile aynı olaylarda BB yerine KC'nin, EMA200 filtresinin ve ADX'in ek katkısı ayrı ablation ile ölçülür; aynı korele sinyaller bağımsız kanıt sayılmaz.

## 3. Ayı Piyasası Trading Stratejileri — Matthew R. Kratter

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Ayı Piyasası Trading Stratejileri - Matthew R. Kratter (75 sayfa) - @eseckal.pdf>) · [Tam metin](03_bear_market_kratter.txt)

**Kaynak taraması:** Kitabın esas evreni **ABD hisse endeksi/SPY/QQQ ve hisse senetleri**, 7/24 kripto değil. 50/200 günlük ortalama rejimi s. 15–16, 18; ayı rallisinde 200 günlük çizgide başarısızlık short s. 18–21; Pazartesi satışını Çarşamba dönüşüne oynayan `%R` sistemi s. 35–40; momentum hissesinin short koşulları s. 48–58. Put opsiyonu, vadeli işlem, borrow ve likidite tartışmaları s. 23–34, 53–59. Verilen eski yıllık getiri tablosu (s. 38–40) bugün geçerli performans kanıtı değildir. Buradaki adaylar FX/kripto ana test kuyruğuna otomatik sokulmaz; tarihsel SPY/ES ve ABD işlem takvimi gerekir.

### MK71A — Ayı rejiminde 200 günlük SMA başarısız rallisini shortla (SPY/ES veri koşullu)

- **Kaynak kuralı:** Uzun yükseliş sonrası SPY SMA50'nin SMA200 altında en az dört ay kalması; 200 günlük SMA üzerine gün içi çıkışta short, bir-iki gün içinde satış başlamazsa erken çıkış, SMA50 altı kapanışta kâr alma (s. 18–19). Örnek s. 19'da gün içi üstünü gördükten sonra altına kapanış; aşağıdaki sürüm bu **başarısız kapanışı** zorunlu kılar. 5–10 yıllık önceki yükseliş ölçüsü kaynakta nesnel değil.
- **Bizim nesnel rejim/sinyal:** SPY ayarlanmış günlük OHLC ile önceki 3 yıl toplam getiri>0; `SMA50<SMA200` ardışık en az 84 ABD işlem günü; sinyal gününde `high_t>SMA200_t` ve `close_t<SMA200_t`, aynı kapanışta SMA50<SMA200. Üç yıl, 84 gün ve başarısız kapanış zorunluluğu bizim tanımımızdır. Sinyal gerçekleşene kadar günün high/close'u bilinmez; aynı günün high'ından otomatik dolum varsayılmaz.
- **İcra/risk:** Sinyalden sonraki ilk SPY seans açılışında veya point-in-time ES ön vadeli kontratının ilk uygulanabilir 1m açılışında short. Stop `signal_high+0,25×ATR14_D`; ilk iki tam seansta günlük close giriş altına inmezse sonraki açılışta çık. Aksi halde ilk `close<SMA50` sonrası açılış veya 20 seans süre. Stop önce, short borrow/temettü/kurumsal işlem maliyeti (SPY) ya da rollover/marjin (ES) dahil. Aynı rejimde basit SMA200 reddi ve yalın SMA50/200 short'a karşı net R karşılaştırılır.

### MK71B — Pazartesi panik günü, Çarşamba çıkışı; `%R` yönü doğrulanacak (SPY veri koşullu)

- **Kaynak kuralı:** Pazartesi kapanışında SPY al, Çarşamba kapanışında sat; üç günlük `%R` ve `x≤10` koşulu verir (s. 37–38). Fakat hemen altta yazdığı `%R=100×(HH3−close)/(HH3−LL3)` formülünde **dipteki kapanışta değer 100'e yakındır**, `≤10` ise tepedeki kapanışı seçer. Dolayısıyla “panik satışı” anlatımı, eşik ve formül kendi içinde çelişir. Kitaptaki 2000–2017 getiri tablosu hangi hesap sürümüyle üretildiği bilinmeden yeniden üretildi sayılamaz.
- **Ayrı deney kolları:** `R_given=100×(HH3−close)/(HH3−LL3)` hesapla; `HH3=LL3` ise sinyal yok. Kol **LITERAL**: Pazartesi `R_given≤10`; kol **PANIC**: Pazartesi `R_given≥90`. İlki formül+eşik sadakati, ikincisi anlatılan aşırı satış niyetinin bizim yorumu. İkisini de önceden sabitle; veri sonrası iyi görüneni kaynak kuralı diye yeniden adlandırma. Pazartesi ABD seansı takvimine göre belirlenir; tatil haftalarında Pazartesi seansı yoksa işlem yok.
- **İcra/risk:** Pazartesi kapanışı kullanılarak üretilen sinyal aynı kapanıştan işlem göremez. İlk uygulanabilir **Salı seans açılışında** SPY long, Çarşamba kapanışına yakın sabit MOC yöntemi veya bir sonraki uygulanabilir seans açılışı ayrı icra kolu. Veri yalnız günlükse muhafazakâr sonraki Perşembe açılışı seçilir; kaynakla dolum farkı açıkça raporlanır. Stop kaynakta yok: bizim araştırma sınırı `Monday_low−0,5×ATR14_D`, pozisyon büyüklüğü buna göre; stop önce. Çarşamba tatilse ilk sonraki işlem günü bitişi. SPY seans, temettü ve işlem maliyetleri dahil. Bu aday kaynak tutarsızlığı çözülene dek **öncelikli backtest kuralı değildir**.

## Ortak doğrulama ve karşılaştırma

SR71A/B ve RT71A/B kripto OHLCV ile üretilebilir ama gün içi araştırma koludur; mevcut günlük çok günlü karar matrisine gelecekteki 1h/4h barlar bağlanmaz. MK71A/B yalnız tarihsel ABD endeks verisiyle anlamlıdır. Her adayda point-in-time evren, kapalı bar, ilk uygulanabilir 1m/seans dolumu, spread/ücret/kayma, uygun finansman/borrow/funding, eksik bar, çakışan pozisyon ve stop-önce sıralaması kaydedilir. Yaklaşık 1.300 kolonluk pilotla aynı sinyal/özellik tekrar sütun yapılmaz. Walk-forward ve maliyet sonrası net R, işlem sayısı, maksimum düşüş, rejim ayrımı ve yalın taban çizgisi görülmeden başarı iddiası kurulmaz.
