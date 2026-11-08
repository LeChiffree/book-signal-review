# Kitap okuma 070 — BTC bant dönüşü, günlük SFP ve ölçülü formasyon hedefleri

**Kapsam:** Üç PDF'nin gerçek **68 + 23 + 36 = 127 sayfası** sırayla metne çıkarılıp incelendi; metni kısa olan grafik sayfalarının görselleri ayrıca kontrol edildi ([görsel kontrol](figure_contacts/)). Atıflar PDF sayfasıdır. Sayısal kurallar kitapta yoksa **bizim test tanımımız** olarak işaretlenir. Kitap örnekleri ve yazarın getiri iddiaları kârlılık kanıtı değildir. Backtest, paper test ve emir yapılmadı.

## 1. Bitcoin Günlük Alım Satım Stratejileri — Lawrence Keaton

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Bitcoin Günlük Alım Satım Stratejileri - Lawrence Keaton (68 sayfa) - @eseckal.pdf>) · [Tam metin](01_bitcoin_daily.txt)

**Kaynak taraması:** İlk bölümler piyasa ve risk rehberi (s. 4–19). Hazır TradingView topluluk indikatörleri s. 20–36 ve 41–42, 55–56, 59–60, 63–66'da kullanılıyor; sürüm/kod ve repaint davranışı sabitlenmeden yeniden üretilemez. Yerel OHLCV'den yapılabilecek açık kurallar s. 38–40 (SMA200 + BB10/1,5 + RSI5), s. 43–50 (HMA/BB/Stochastic), s. 51–53 (HMA/RSI), s. 57–58 (EMA5/11 + Stochastic22/5/9), s. 61 ve 67'de. Scalping örneklerinin zaman dilimi günlük çok günlü modelin ana sinyaline otomatik taşınmaz. Kitap s. 40'ta short stopunu “giriş mumunun en düşüğünün altı” yazıyor; short için yanlış taraftadır, testte bunun yerine short sinyal tepesinin üstü kullanılır.

### LK70A — SMA200 yönünde BB10 ve RSI5 aşırı uçtan geri dönüş

- **Kaynak:** Long için fiyat SMA200 üstünde, kapanış BB(10,1,5) altı ve RSI5<30; RSI'nin 30 üstüne dönmesi **veya** kapanışın alt banda geri dönmesiyle giriş. Stop giriş barı altı; üst band dışına çıkıp geri dönme **veya** RSI70 üstünden altına inme ile çıkış (s. 38–39). Short simetrisi s. 39–40. “Veya” iki tetik olarak ayrı test edilmeli; hangisi daha kârlıymış diye geçmişe bakıp seçim yapılmaz.
- **Nesnel kurulum:** BTC/ETH'de yalnız kapanmış 1h bar. `close_t>SMA200_t`, `close_t<lowerBB10_1.5_t`, `RSI5_t<30` olduğunda long setup dondur; sonraki en çok 6 kapanmış 1h'de ilk `RSI5` 30 yukarı kesişi veya `close>lowerBB` tetik. Tetikte `close>SMA200` hâlâ geçerli; aksi setup iptal. Short ters. Altı bar geçerlilik **bizim tanımımızdır**. RSI/BB tetiklerini ayrı kol ve birleşik kol olarak kaydet.
- **İcra/risk:** Tetik kapanışı sonrası ilk uygulanabilir 1m giriş. Long stop `min(setup_low, trigger_low)−0,1×ATR14_1h`; short stop `max(setup_high,trigger_high)+0,1×ATR`. Sinyalden sonra karşı BB bandı dışı→içine kapanış veya RSI70 üstü→altı (short tersi), daha önce 24 adet 1h geçerse zaman çıkışı. Stop anlık 1m, diğer çıkışlar 1h kapanışı sonrası 1m; aynı 1m stop önce. 0,1 ATR tamponu, 6/24 bar süreleri bizim seçimimiz. Mevcut BB+RSI ve SMA rejim adaylarına karşı ek katkı, maliyet sonrası net R ve sinyal örtüşmesi ölçülür.

### LK70B — Stochastic(22,5,9) kesişimi sonrası EMA5/11 yön değişimi

- **Kaynak:** Stochastic 50 altındayken yukarı geçer, EMA5 EMA11'i yukarı kestiğinde long; tersi short. Karşı EMA kesişimi veya Stochastic aşırı uçtan ters kesişim çıkışı (s. 57–58). Kitap ardışıklık penceresi ve stop belirtmez.
- **Nesnel kurulum:** Kapanmış 4h barlarda `%K` ham 22, 5 bar SMA ile yumuşatılmış; `%D` bu değerin 9 bar SMA'sı. `%K` `%D` üstüne 50 altındayken geçtiğinde kurulum; aynı bar veya sonraki 3 kapanmış 4h içinde ilk `EMA5>EMA11` yukarı kesişi long. Kesişimden önce stochastic yukarı yönünü kaybederse iptal. Short ters. Hesap yöntemi ve üç bar penceresi bizim sabitlememizdir.
- **İcra/risk:** EMA tetik barı kapanışı sonrası ilk uygulanabilir 1m; long stop son 5 kapanmış 4h'nin minimumu `−0,1×ATR14_4h`, short maksimum `+0,1×ATR`; stop yanlış taraftaysa atla. Karşı EMA kesişimi, `%K` 75 üstünden `%D` altına inişi (short 25 altından yukarı çıkış) veya 18 adet 4h süre; stop önce. Sıradan EMA kesişimi ve önceki stochastic+EMA adaylarına karşı aynı evren/maliyetle karşılaştır.

## 2. En İyi Bitcoin ve Ethereum Trading Stratejisi — James Jecool King

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/En İyi Bitcoin ve Ethereum Trading Stratejisi - James Jecool King (23 sayfa) - @eseckal.pdf>) · [Tam metin](02_bitcoin_eth.txt)

**Kaynak taraması:** Bu tek mekanik “en iyi strateji” değil, yazarın çok zaman dilimli takdire bağlı işlem planı. Günlük grafik seviye ve önyargı (s. 3–14), 30m işlem haritası ve tick/order-flow yürütme (s. 15–22), ayrı swing notları (s. 22–23). Günlük bullish engulf, önceki ayı barın altını görüp önceki high üzerinde kapanmak; bearish tersi (s. 3–4). Günlük SFP, önceki hafta/ay veya önemli swing high/low dışına taşıp içeri kapanmak (s. 4–5). Inside day'nin tek taraflı kırılıp karşı tarafa dönmesini de anlatır (s. 6). Özgün tam icra CVD, footprint, TPO/nVPOC ve opsiyon OI gerektirir (s. 8–16); elimizde yalnız OHLCV varsa bunlar doğrulanmış sayılmaz. Aşağıdaki yalın sürüm yazardan bire bir kopya değil, falsifiye edilebilir **fiyat vekili**dir. Yazarın %1/işlem ve %4/gün sınırı (s. 2) bu araştırma hattının otomatik pozisyon kuralı yapılmaz.

### JK70 — Önceki hafta uç seviyesinin günlük SFP geri kapanışı

- **Seviye ve olay:** Tamamlanmış önceki UTC haftasının high/low'u yeni hafta başlamadan dondur. Günlük `high_t>prev_week_high+0,1×ATR14_D` ve `close_t<prev_week_high` bearish SFP; `low_t<prev_week_low−0,1×ATR` ve `close_t>prev_week_low` bullish. Aynı gün iki tarafı da ihlal ederse atla. Kaynakta hafta/ay uçları var (s. 4); ATR tamponu **bizim seçimimiz**. Önceki ay seviyeleri ayrı, önceden ilan edilmiş ablation; gün sonu bilinen nihai hafta seviyesi asla kullanılmaz.
- **Giriş ve stop:** Yazar günlük olayı 30m seviyeleri ve order-flow ile yürütür (s. 5, 15–16). OHLCV vekilinde günlük kapanıştan sonraki ilk 4 kapanmış 30m içinde, long için `close_30m>max(high of previous 2 completed 30m)`; short ters. Sadece bu teyit oluşursa sonraki uygulanabilir 1m giriş. Long stop günlük SFP low `−0,1×ATR14_D`; short high `+0,1×ATR`. Dört bar teyit ve iki bar kırılım **bizim kurallarımız**. 30m teyit yerine doğrudan ertesi 1m giriş ayrı kontrol koludur; order-flow teyidi varmış gibi adlandırılmaz.
- **Çıkış/test:** İlk hedef önceki haftanın aralık orta noktası veya 2R, hangisi giriş yönünde yakınsa; hedef lehte değil veya potansiyel ödül/risk <1 ise işlem yok. En çok 3 gün süre, aynı 1m stop önce. Önceki SFP/likidite süpürmesi adayları ve PS69A ile sinyal çakışması, katma değer ve net R karşılaştırılır. Yalnız kapanmış hafta/gün/30m kullanılır; canlı seviye teslim gecikmesi modellenir.

## 3. Kripto Para Ticareti — Piyasaya Giriş, Çıkış ve Stop-Loss — Chris Lambert

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Kripto Para Ticareti - Piyasaya Giriş, Çıkış ve Stop-Loss, Bana 100.000 Doların Üzerinde Kazanç Sağlatan Trading Stratejileri - Chris Lambert (36 sayfa) - @eseckal.pdf>) · [Tam metin](03_crypto_entry_exit.txt)

**Kaynak taraması:** Baş-omuzda boyun çizgisini tek başına yeterli görmeyip önceki dip altını ve sağ omuz stopunu kullanır (s. 7–10). Çift dipte boyun kırılımı, iki dip altı stop ve formasyon yüksekliği kadar hedef (s. 13–15). Simetrik/yükselen üçgen ve düşen kama için sınır kırılımı, karşı kenar stopu ve açıklık yüksekliği kadar hedef (s. 18–26). Flama/bayrakta direk yüksekliği hedefi (s. 28–31), dikdörtgende kutu yüksekliği hedefi (s. 33–35). Bunların görsel tanımları takdire bağlı; “kripto sahte kırılımı nadirdir” iddiası s. 20, 23, 25, 31'de verisiz söylenir ve kabul edilmez. Özellikle s. 15 agresif çift dipte “stop” paragrafının sonunda yanlışlıkla yeniden “satın alma emri” yazıyor; bunu kodlanabilir stop kuralı sayma.

### CL70A — Eşit iki dip, boyun üstü kapanış ve ölçülü hedef

- **Kaynak kuralı:** Düşüş trendi sonrasında iki yakın dip, aradaki tepe boyun; boyun üstü kırılımda alım, iki dip altına stop, `boyun + (boyun−dip)` hedef (s. 13–14). Çift tepe short simetrisi s. 16–17.
- **Bizim nesnel tanım:** Günlük barlarda yalnız **onaylanmış** pivot low: merkez günün low'u önceki ve sonraki 2 tamamlanmış günden düşük. İki pivot arasında 5–30 gün; dip farkı `≤0,5×ATR14_D` (ikinci dipte bilinen ATR). İlk dipten önceki 20d getiri negatif; aradaki kapanmış barların maksimum high'ı boyun. İkinci pivot en erken `pivot+2` kapanışında bilinir. Bundan sonraki en çok 15 günde ilk `close>neckline+0,1×ATR14_D` tetik. Pencereler, eşitlik ve ATR tamponu bizim tanımımızdır; pivotu merkez gününde biliniyormuş gibi kullanma.
- **İcra/risk:** Tetik kapanışı sonrası ilk uygulanabilir 1m long. Stop `min(low1,low2)−0,1×ATR`, hedef `neckline+(neckline−mean(low1,low2))`; 14 gün süre. Hedef girişten yüksek değil veya ilk ödül/risk <1 ise atla; stop önce. Çift tepe simetri ayrı kol, önceki W/double-bottom adayları ile aynı örneklemde karşılaştır.

### CL70B — Güçlü direk sonrası dar bayrak kırılımı ve direk boyu hedef

- **Kaynak kuralı:** Keskin yükseliş sonrası kısa geri çekilen bayrak/flama; üst sınır kırılımı long, bayrak altına stop, kırılıma direk yüksekliği eklenen hedef (s. 28–31). Kaynak bayrakla flamayı ayırır; aşağıdaki ilk sürüm yalnız düz/azalan kutu vekili, formasyonun bütün takdire bağlı çeşitleri değildir.
- **Bizim nesnel tanım:** Günlük ilk direk 3–7 kapalı barda net `≥3×ATR14_D` artış ve pozitif son kapanış; hemen ardından 3–8 günlük bayrakta hiçbir kapanış direk başlangıcının altına düşmez, bayrak high-low yüksekliği direğin `≤0,5` katı, kapanış eğimi sıfır veya negatif. Bayrak başlamadan önceki direk başlangıç ve sonu sabitlenir. İlk `close>max(flag_highs)+0,1×ATR14_D` long. Direk/flag penceresi, 3 ATR ve 0,5 oranı bizim test tanımımızdır.
- **İcra/risk:** Kırılım kapanışı sonrası ilk uygulanabilir 1m; stop `min(flag_lows)−0,1×ATR`; hedef `frozen_breakout_level+pole_height`; 14 gün süre. Hedef/stop yanlış tarafta veya ilk ödül/risk <1 ise atla; aynı 1m stop önce. Basit momentum kırılımı, donmuş kutu kırılımı ve önceki bayrak adaylarına karşı net R ile ablation. Trendin sonradan gerçekten devam etmiş olması kurulum şartı değildir.

## Ortak test sözleşmesi ve öncelik

Öncelik LK70A (açık fiyat/indikatör kuralları), JK70 (önceki hafta SFP'nin 30m teyit etkisi), CL70A (ölçülü hedef) ve CL70B (direk-boyu hedef). LK70B de tanımlı adaydır fakat EMA/stochastic önceki partilerle yüksek örtüşebilir. İlk gerçek testte mevcut yaklaşık 1.300 kolonluk pilotla eşdeğerlik yapılır; aynı bilgi yeni kolon diye çoğaltılmaz. Günlük karar matrisi için 1h/4h/30m stratejiler ayrı araştırma kollarıdır, günlük ML tablosuna sızıntılı ana sinyal olarak sokulmaz. Tüm adaylarda point-in-time likit evren, kapanmış UTC barlar, eksik veri, ilk uygulanabilir 1m dolum, spread/ücret/kayma, futures funding, pozisyon çakışması ve zaman sıralı walk-forward şarttır. İşlem sayısı, maliyet sonrası net R, drawdown ve yalın taban çizgisi görülmeden kârlılık iddiası yoktur.
