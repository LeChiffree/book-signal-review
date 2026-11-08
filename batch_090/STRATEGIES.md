# Kitap okuma 090 — gün içi kurallar ve fraktal teyidi

**Kapsam:** Daha önce okunmamış üç PDF'nin **29 + 29 + 139 = 197 sayfası** baştan sona tarandı. Kural ve şekil sayfalarından 14'ü [görsel olarak incelendi](figure_contacts/). Sayfa numaraları PDF sayfasıdır. **Beş yeni araştırma adayı** aşağıda; başarıları doğrulanmadı. Backtest, paper test ve emir yapılmadı.

## 1. Forex Trading 10 Altın Kural — Admiral Markets

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 10/Baskı 10/Forex Trading 10 Altın Kural - Admiral Markets - Orijinal (29 sayfa) - @eseckal.pdf>) · [Tam metin](01_ten_forex_rules.txt)

**Sayfa haritası:** s. 1–3 giriş/reklam; 4–21 eğitim, trend, demo, psikoloji, plan ve basitlik; 22–25 risk ve işlem günlüğü; 26–29 tanıtım. S. 22 görsel kontrol edildi. **Yeni sinyal yok.** S. 22–23 işlem başına %1–2 risk önerisi bir üst sınır fikridir; proje risk limitini artırmaz. Promosyon getirileri ampirik performans değildir.

## 2. Güniçi Trading ile Servet Oluşturmak — Maddy

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 12/Baskı 12/Güniçi Trading ile Servet Oluşturmak - Maddy (29 sayfa) - @eseckal.pdf>) · [Tam metin](02_intraday_wealth.txt)

**Sayfa haritası:** s. 1–5 psikoloji/risk; 6–8 M5 MA20/200 ve ilk seans mumu; 9–11 günlük ortalamadan uzaklaşma/gap; 11–13 FAB4 aralığı; 13–18 CPR; 18–22 önceki gün seviyesi ve dönüş/kırılım; 23–27 M1 Supertrend/BB scalping; 28–29 parçalı kâr/stop. S. 6, 9, 13, 20, 25, 29 görsel denetlendi.

**Tekrar/uygunluk:** İlk 5 dakika aralığı ve gap (s. 6–11) Hindistan hisse seansı açılışına bağlı. Sürekli işlem gören kripto için keyfi UTC açılışı kaynak kuralı sayılmaz. CPR, önceki gün high/low kırılımı ve Supertrend önceki partilerde var. FAB4 dikdörtgeninin hesaplanışı belirsiz. S. 21'de destekten short/dirençten long yazımı, s. 22'deki ters ve yerleşik yönle çelişiyor; otomatik kural yapılmaz.

**Yeni giriş değil, çıkış ablation'ı:** S. 28–29, +1R'de pozisyonun %60'ını kapatıp kalanın stopunu girişe taşıma ve +2R'yi hedefleme fikri verir. Testte bu ancak mevcut sinyalin çıkış kolu olabilir. Başlangıç stopu ve R girişte sabitlenmeli; +1R'ye varılmadan BE uygulanmamalı; giriş fiyatına stop, komisyon ve kayma sonrası sıfır net kâr demek değildir. Aynı M1'de stop ve hedef temasında stop önce varsayılır. Kitaptaki örnek aritmetik güvenilir performans kanıtı değildir.

## 3. Kusursuz Günlük Trading — Ivan Cavric

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 12/Baskı 12/Kusursuz Günlük Trading - Ivan Cavric (139 sayfa) - @eseckal.pdf>) · [Tam metin](03_perfect_day_trading.txt)

**Sayfa haritası:** s. 1–96 işlem özdeyişleri, psikoloji ve tekrarlar; 97–100 BB/RSI; 101–108 önceki gün yönü + EMA/fraktal; 109–115 üç MACD + fraktal; 115–119 iç bar + RSI; 119–122 yutan mum + RSI; 122–124 09:30 seans açılışı; 124–129 EMA50/100/150; 130–139 sonuç, SSS ve sözlük. S. 98, 103, 110, 117, 121, 123, 127 ve grafikleri görsel denetlendi.

### DC90A — BB19 içinde RSI14 aşırılıktan dönüş

- **Kaynak (s. 97–99):** M15 Bollinger(19,2). Long: önceki RSI14<30, son RSI14>30; son kapanış alt bant üstünde ve orta bant altında/eşit. Tamamlanan barın high+1 tick üstünde giriş emri, low−1 tick stop, 2R hedef. Short: RSI >70'ten <70'e; kapanış orta bant üstünde/eşit, üst bant altında; low−1 tick giriş, high+1 tick stop, 2R.
- **Deney kesinleştirmesi (bizim):** RSI Wilder, BB kapanış ve popülasyon standart sapması; kesişim için önceki `<=30` değil kesin `<30`, mevcut `>30`. Sinyal M15 kapanınca en çok sonraki 4 M15 boyunca stop emir geçerli; M1 high/low ile tetiklenir, aynı M1 giriş ve stop/hedef oluşursa stop önceliği. `4` süre bizim parametremiz. Kaynağın s. 99 WTI %71,69 kazanma ve 5 ay kâr iddiası denetlenmiş veri/ücret dökümü sunmaz.
- **Örtüşme:** Önceki RSI30 dönüşü ve BB aşırılık aileleriyle olay düzeyi çakışma ölçülmeli; burada ayırt edici koşul **BB19 iç bölgesi + aynı mumdaki RSI eşik geri geçişi**. Tek başına RSI geri geçişiyle maliyet sonrası ablation şart.

### DC90B — Önceki gün yönünde EMA20/50/100 geri çekilmesi ve teyitli fraktal

- **Kaynak (s. 101–108):** Önceki gün `close>open` ise yalnız long, tersi short. M5 EMA20>EMA50>EMA100 (short tersi), fiyat EMA20 tarafında, EMA20'ye geri temas sonrası Williams fraktalı, fraktal teyidinden sonra giriş. İlk stop EMA50'nin 1 tick ötesi; EMA50 izleyen stop; 2R isteğe bağlı. Kaynak örneğinde fraktal işareti yaklaşık iki mum sonra kesinleşir (s. 104).
- **Deney kesinleştirmesi (bizim):** UTC D1 yalnız tamamlanmış önceki gün; teyitli 5 bar fraktal merkez mumundan **iki M5 kapanış sonra** kullanılabilir. Temas = M5 low<=EMA20 long; fraktal teyidine kadar EMA sırası bozulursa iptal. İlk uygulanabilir sonraki M1'de giriş; stop yalnız lehe EMA50 boyunca, kısa simetri; 2R ve yalnız izleyen stop ayrı çıkış kolları. Aynı bar stop/hedef önceliği, ücret, kayma, fonlama gerekir.
- **Örtüşme:** A2/L13b EMA geri çekilmesi ve PA59 fraktal + EMA retestiyle aynı aile; önceki gün yönü ile EMA20/50/100 sıralamasının **ek katkısı** ölçülmeden bağımsız üstünlük iddia edilmez.

### DC90C — Üç MACD sıfır geçişi + teyitli Williams fraktal stopu

- **Kaynak (s. 109–115):** M30 veya daha kısa; MACD hızlı/yavaş/sinyal `(34,144,9)`, `(13,21,9)`, `(5,8,9)`. Üçü aynı yükseliş/düşüş yönündeyken herhangi birinin sıfırı yeni geçmesiyle sinyal; M30 kapanışında long/short. İlk stop son fraktal dip/tepenin 1 tick ötesi; yeni fraktallarla izleyen stop. Kaynak s. 111–114'te “sinyal çizgisi kesişimi” ile “sıfır geçişi” ifadeleri karışır.
- **Deney kesinleştirmesi (bizim):** Ana kol **MACD çizgisinin sıfır geçişi**, diğer iki MACD çizgisi aynı işarette; sinyal hattı kesişimi ayrı kol. Üç MACD aynı M30 kapanış serisinden hesaplanır (kaynakta farklı zaman dilimi ifadesiyle örnek grafik arasında belirsizlik var). Fraktal yalnız iki sağ mum kapandıktan sonra bilinir. Son teyitli fraktal stop geçersiz taraftaysa atla. Giriş sonraki ilk M1; sadece lehe stop ilerlet, süre üst sınırı 48 M30 (bizim), maliyet/çakışma kaydı.
- **Örtüşme:** M1/M24b gibi MACD teyit stratejileri ve fraktal stop aileleriyle karşılaştır; ayırt edici özellik üç ayrı hızın aynı yönü ve yeni sıfır geçişidir.

### DC90D — RSI50/70/30 filtresiyle iç bar ana mum kırılımı

- **Kaynak (s. 115–119):** M15 iç bar. Long ana mum high+1 tick, RSI `50<RSI<70`, stop ana mum low−1 tick, hedef ana mum aralığının 2 katı. Short ana mum low−1 tick, `30<RSI<50`, stop ana mum high+1 tick. Fiyat ana mum yarı aralığı kadar lehe ilerleyince stop girişe. Görsel s. 117'de RSI onayı yoksa kârlı bir breakout dahi reddedilir.
- **Deney kesinleştirmesi (bizim):** İç bar `high<=mother.high` ve `low>=mother.low`, iki eşit sınır dahil; mother bir önceki M15. RSI14 sinyal iç bar kapanışında sabit; giriş stop emri sonraki 4 M15, sonra iptal. Hedef girişten `2×mother_range`, BE tetikleyicisi girişten `0,5×mother_range`; M1 stop/hedef yolu stop önce. Aralık sıfırsa veya stop yanlış taraftaysa atla. 4 bar ömrü ve eşitlik bizim seçimimiz.
- **Örtüşme:** DP11c, RT19a, C27a iç bar kırılım ailelerine RSI orta bant filtresi ekler; filtresiz aynı sinyale karşı ablation olmadan ayrı edge sayılmaz.

### DC90E — EMA50/100/150 hizasında EMA50 altı/üstü sapma ve geri dönüş

- **Kaynak (s. 124–129):** M1 veya M5; long EMA50>100>150, üçü yükselen, fiyat önce 50 üstü; 50 altına fakat 150 üstünde kalacak şekilde sarkar; 50 üstüne geri dönünce long. Short simetri. Stop sarkma dibinin/tepesinin 1 tick ötesi; kârda BE ve son geri çekilme düzeyleriyle izleme. “25–30 derece EMA eğimi” grafik ölçeğine bağlıdır ve nesnel fiyat kuralı değildir.
- **Deney kesinleştirmesi (bizim):** M5 ana kol; tüm EMA'ların `EMA[t]>EMA[t−3]` long, short tersi. Son 6 kapanmış M5 içinde 50 altı/150 üstü bir kapanış, ardından son M5 kapanışında tekrar 50 üstü. İlk uygulanabilir M1 giriş; stop 6 M5 sarkma dibinin 1 tick altı; 2R hedef veya 24 M5 süresi ayrı kollar. `3`, `6`, `24`, 2R bizim deney parametreleri; derece filtresi kaynak adına kodlanmaz.
- **Örtüşme:** EMA çoklu hizalanma ve geri çekilme aileleri C27d, W25a/W25c ile karşılaştırılmalı; 50 ile 150 arası sarkmanın yeni bilgi getirip getirmediği ölçülmeli.

**Tekrar/uygunluk:** S. 119–122 M30 yutan mum + RSI<70/>30, S32a ve C1 gibi yutan mum+RSI ailesinin eşik varyantı; yeni başlık açılmadı. S. 122–124 09:30 ilk M15 kırılımı hisse seansına ve 10:00 haber takvimine bağlıdır; 24/7 kripto için saat aktarımı kaynak kuralı değildir. Yukarıdaki beş M1/M5/M15/M30 fikir **mevcut günlük karar anı sözleşmesine doğrudan uygun değildir**. Gün içi ayrı araştırma protokolünde kapanmış barlardan sinyal, yalnız sinyal sonrası M1 icrası, likidite evreninin geçmişten seçimi, komisyon/kayma/fonlama ve stop önce kuralı ile değerlendirilebilir. Performans örnekleri çoğunlukla petrol, endeks ve FX'tendir; kripto getirisi iddiası değildir.
