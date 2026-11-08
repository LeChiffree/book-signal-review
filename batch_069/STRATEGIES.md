# Kitap okuma 069 — kural kaynağı ayrımı ve mum formasyonları

**Kapsam:** Üç PDF'nin gerçek **72 + 94 + 47 = 213 sayfası** sıralı incelendi. İkinci PDF'nin metin çıkmayan 71–94. sayfalarındaki görseller ayrıca toplu olarak görüldü; bunlar çoğunlukla müşteri mesajı, otomobil, tanıtım ve hesap ekranı, işlem kuralı değil. Atıflar PDF sayfasıdır. Aşağıdaki sayısal eşikler açıkça belirtilmedikçe **bizim test tanımımızdır**. Backtest, paper test ve emir yapılmadı.

## 1. Craig Harris'in Forex Trading Metodolojisi — Lynn Brown

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Craig Harris_in Forex Trading Metodolojisi (72 sayfa) - @eseckal.pdf>) · [Tam metin](01_craig_harris.txt)

**Kaynak değerlendirmesi:** Kitap esas olarak MT4, emir, maliyet ve sistem terimleri sözlüğü. Harris yönteminin 15m mum kullandığını (s. 29), iç/dış barı (s. 31–33), renk değiştiren RC'yi (s. 33–34), MA/fraktal/stokastiği (s. 34–35), Tokyo aralığı ve yuvarlak seviyeleri (s. 37–40) tanımlar. Gerçek giriş sırası, kombinasyon eşikleri ve çıkış için defalarca Gene Ballard'ın ayrı kılavuzuna yönlendirir (s. 32–40). Buradaki tanımları **Craig Harris sisteminin tam stratejisi** diye sunmak yanlış olur. Maliyet bölümü (s. 42–49) FX spread ve döviz dönüştürmeyi hatırlatır. 15m ve 5m ana günlük model girdisi değildir; günlük karara uyarlama ayrı hipotez gerektirir.

### CH69 — İç/dış bar, RC ve fraktal sözlüğü (özellik adayı; işlem stratejisi ertelendi)

- **Kapalı mum özellikleri:** `inside_t = high_t≤high_{t-1} ∧ low_t≥low_{t-1}`; `outside_t = high_t≥high_{t-1} ∧ low_t≤low_{t-1}`; `RC_t = sign(close_t−open_t)≠sign(close_{t-1}−open_{t-1})`, iki gövde de sıfır dışı. 5 bar fraktalı merkez `t-2` için ancak `t` kapanınca kullanılabilir; aksi lookahead olur (s. 31–35). Eşit yüksek/düşük kabulü kitap tanımındadır; doji RC değildir, bu bizim netleştirmemizdir.
- **Karar:** Bu kitap tek başına yön, giriş, stop ve hedef bağlamaz. Bu yüzden emir üreten aday **değil**, mevcut günlük formasyon kolonlarıyla eşdeğerlik kontrolüne alınacak veri tanımıdır. İç/dış bar ve fraktal daha önceki partilerde de var; yeni ayrı sütun açma gerekçesi yok. Orijinal Gene Ballard kılavuzu bulunursa birleşik yöntem yeniden değerlendirilebilir.

## 2. Forex Broker Killer Edition — Kgopotso Mmutlane

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Forex Broker Killer Edition - Kgopotso Mmutlane (94 sayfa) - @eseckal.pdf>) · [Tam metin](02_broker_killer.txt) · [Görsel sayfalar](broker_images/)

**Kaynak değerlendirmesi:** Kitap forex ve MT4 emir türlerini anlatır (özellikle s. 59–68). 100 pip stop/300 pip hedef örneği yalnız **buy stop emri girme öğretimi** içindedir (s. 64–67); bir giriş sinyali veya ampirik 3R stratejisi değildir. Yedinci bölüm başlığı “bir dakikalık strateji” olsa da kitap stratejinin belgede bulunmadığını, videolar/üyelikle öğrenileceğini açıkça söyler (s. 69–70). 71–94. sayfalar görsel incelendi: tanıtım, mesaj ve sonuç iddiaları var; uygulanabilir açık kural yok. Görseldeki kâr ekranları doğrulanmış performans sayılmaz.

### FBK69 — Bir dakikalık strateji (kaynakta kural yok; ertelendi)

- **Durum:** Kapalı mumdan üretilecek tetik, ürün/evren, stop mesafesinin gerekçesi ve çıkış sırası tanımlanamadığı için backtest kuyruğuna alınmaz. 100/300 pip örneğini sinyal olarak kodlama. M1 işlem iddiası ayrıca mevcut günlük karar sözleşmesinin dışında kalır.
- **Yeniden açma koşulu:** Kaynakta vaat edilen gerçek video veya kural dokümanı arşive eklenir ve giriş/çıkış baştan sona doğrulanırsa ayrı kaynak olarak işlenir. Üyelik, tanıtım ve sonuç ekranlarından kural tersine mühendisliği yapılmaz.

## 3. Para Sihirbazı — Mum Çubukları ile Farklı Bir Analiz Yöntemi — Zeki Çelik

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Para Sihirbazı - Mum Çubukları ile Farklı Bir Analiz Yöntemi - Zeki Çelik (47 sayfa) - @eseckal.pdf>) · [Tam metin](03_para_sihirbazi.txt)

**Kaynak:** Kitap bobin ve engulf ile arz/talep bölgesi çizer, bölge tekrar test edilip tepki verince giriş ister (s. 11–17). Ayrıca fake pinbar (s. 27), pin + engulf (s. 28), ters/çift engulf (s. 29–30), trend devam (s. 32) tarif eder. Tek formasyona güvenmemeyi, trend/momentum ve 2–3 teyidi (s. 42–43) ve stopu yapıya göre kurmayı (s. 44–46) vurgular. “Maker/balina emirleri” yorumu OHLCV'den gözlenemez; aşağıdaki hipotezler sadece ölçülebilir fiyat davranışını test eder.

### PS69A — Önceki kutu dışına iğne ve kutu içine geri kapanış

- **Kaynak kuralı:** Büyük ana barın high/low kutusunda kalan küçük barlardan sonra son bar kutu dışına uzun fitil atıp içeri döner; dışarı atılan yönün tersi işlem yönü (s. 27). Kitap 4h ve üzeri, trend yönü ve destek/direnç yakınlığını önerir. Bu aday mevcut likidite süpürmesi ve inside-bar sahte kırılım fikirlerine yakın; yalnız **önceden kurulmuş ana-bar kutusu** koşulunun ek katkısı sınanır.
- **Bizim nesnel kurulum:** Günlük `m` ana barın range'i önceki 20 günlük range medyanının ≥1,5 katı; sonraki 2–5 kapalı günlük barın tüm high/low'ları `[low_m,high_m]` içinde. İlk sonraki günlük `t`, `high_t>high_m+0,1×ATR14` ve `close_t<high_m` ise short; `low_t<low_m−0,1×ATR14` ve `close_t>low_m` ise long. İki tarafı da delerse atla. Ana bar büyüklüğü, 2–5 pencere ve 0,1 ATR bize ait. Tek kutu için ilk tetik bir kez kullanılır.
- **İcra/risk:** `t` kapandıktan sonraki ilk uygulanabilir 1m'de giriş; short stop `high_t+0,1×ATR14`, long stop `low_t−0,1×ATR14`; hedef kutu orta noktası veya 3 günlük süre. Hedef lehte değilse veya ilk ödül/risk <1 ise atla; aynı 1m'de stop önce. Trend filtresi (önceki 20d getirinin yönü) ve eski destek/direnç yakınlığı ayrı ablation kolu, gelecekteki swing kullanılmaz.

### PS69B — Pinbar sonrası iki barlık engulf teyidi

- **Kaynak kuralı:** Üstten satıcı toplayan pinbarı hemen shortlamak yerine en az iki bar beklenir; sonraki iki bar aşağı engulf oluşturursa teyit (s. 28). Long simetrisi kaynakta açık ayrıntılı değil; long kolu **bizim simetrik uzatmamızdır**. Pinbar/engulf adayları zaten mevcut, burada yeni unsur *iki bar bekleme ve teyit*.
- **Bizim nesnel kurulum:** Günlük üst pinbar `upper_wick≥2×body`, `upper_wick≥0,5×range`, `close` barın alt yarısında. Tam sonraki iki kapanmış günlük bar karşılaştırılır; ikinci teyit barı düşen, gövdesi birincinin gövdesini yutar ve `close` pinbarın orta fiyatı altındadır → short. Doji/0 gövde atla. Long ters kurallar ayrı kolda. Fitil oranları ve pinbar orta fiyatı bizim eşiklerimizdir; kaynak yön ve teyit sırasını verir.
- **İcra/risk:** İkinci teyit barı kapanışından sonraki ilk uygulanabilir 1m giriş. Short stop pinbar high `+0,1×ATR14`, long low `−0,1×ATR14`; 2R hedef veya 7 günlük süre. Stop geçersizse/çok uzaksa atla; aynı 1m stop önce. Yalın pinbar ve yalın engulf ile aynı evren, dönem ve maliyette karşılaştır.

### PS69C — Trend içinde uzun–kısa–uzun üç bar devamı

- **Kaynak kuralı:** Trend önceki tepe/dibi aşmış olmalı; yön dizisi long için yukarı–aşağı–yukarı, short için tersi; orta gövde iki kenardakinden kısa. Üçüncü bar kapanışı sonrası giriş veya orta gövde bölgesinin tekrar testi; bölgenin aksi yönde kapanış çıkış işareti (s. 32). Kitabın trend tespiti takdire bağlıdır.
- **Bizim nesnel kurulum:** Günlük long trend `close_{t-3}>max(high_{t-23:t-4})` ve `EMA20_{t-3}>EMA50_{t-3}`; sonra `t-2,t-1,t` gövdeleri sırasıyla pozitif/negatif/pozitif, orta gövde her iki dış gövdeden küçük ve üçüncü `close_t>high_{t-1}`. Short simetrisi. 20 günlük tepe, EMA'lar ve son bar kırılımı bizim seçimimizdir; trend hesabı formasyon başlamadan bilinir.
- **İcra/risk:** Üçüncü kapanış sonrası ilk uygulanabilir 1m giriş. Long stop orta bar low `−0,1×ATR14`, short high `+0,1×ATR14`; 2R hedef, orta bar gövde bölgesi dışına karşı yönlü günlük kapanış veya 7 günlük süre ilk gerçekleşende çıkış. Stop/TP aynı 1m'de ise stop önce. Basit EMA trend devamı ve genel üç-bar formasyonuyla ek katkı, işlem örtüşmesi ve net R karşılaştırılır.

## Ortak uygulama ve öncelik

PS69A/B/C yalnız **araştırma adayıdır**; öncelik PS69A'nın önceden kurulu kutu şartı ve PS69B'nin iki bar teyidi. Günlük UTC kapanışı karar anıdır; haftalık/4h özellik eklenecekse yalnız son kapanmış bar kullanılacak. Üçünü de mevcut yaklaşık 1.300 özelliklik pilotla eşdeğerlikten geçir; mevcut aynı formasyon sütununu yineleme. Her adayda point-in-time likit evren, eksik bar denetimi, ilk uygulanabilir 1m açılışında ücret/spread/kayma ve futures ise funding, stop-önce sıralaması, pozisyon çakışması, zaman sıralı walk-forward ve yalın taban çizgisi gerekir. Bu kayıt kârlılık kanıtı değildir.
