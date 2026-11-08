# Kitap okuma 091 — günlük çift stokastik ve Bollinger geri dönüşü

**Kapsam:** Önceden tamamlanmamış üç PDF'nin **28 + 41 + 35 = 104 sayfası** baştan sona okundu; 14 önemli metin/grafik sayfası [görsel kontrol edildi](figure_contacts/). Sayfalar PDF numarasıdır. **İki yeni araştırma adayı** kaydedildi; sonuçları henüz test edilmedi.

## 1. Bollinger Band Trading — Glenn Wilson

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 14/Baskı 14/Bollinger Band Trading - Kazançlı Bir Trading Sistemi Nasıl Oluşturulur - Glenn Wilson (28 sayfa) - @eseckal.pdf>) · [Tam metin](01_bollinger_wilson.txt)

**Sayfa haritası:** s. 1–7 önsöz/reklam/feragat; 8–11 zarf ve BB(20,2) tanımı; 12–13 dış bant dönüşleri; 14–15 konsolidasyon sonrası BB + destek/direnç kırılımı; 16–17 orta bant yönü; 18–23 RSI70/30 ile dış bant dönüşü; 24–26 genel kurallar; 27–28 kapanış. S. 14, 20, 23 görsel kontrol edildi.

**Karar:** BB dış bant + RSI aşırılık fikri [090. partinin DC90A](../batch_090/STRATEGIES.md) ve daha önceki BB/RSI dönüş aileleriyle örtüşür. Burada RSI “zayıflığı” ve “banta yakın” için eşik ve zamanlama yok; ayrıca tam stop/çıkış belirtilmiyor. BB dışı kapanışın otomatik dönüş olmadığını s. 24 de söyler. BB kırılımı + destek/direnç s. 14–15 önceki sıkışma/kırılım ve seviye adaylarının aynısı. Yeni aday sayılmadı. S. 10'daki bantlar arasında gidip gelme anlatımı gerçekleşme garantisi veya ölçülmüş frekans değildir.

## 2. Forex Trading Rehberi — Jeremy Zindel

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 17/Baskı 17/Forex Trading Rehberi - 30 Dakikalık Günlük Trading Stratejisi - Jeremy Zindel (41 sayfa) - @eseckal.pdf>) · [Tam metin](02_m30_zindel.txt)

**Sayfa haritası:** s. 1–5 Forex temeli; 6–11 psikoloji/risk; 12–16 temel analiz; 17–24 teknik analiz ve hareketli ortalama; 25–28 BB band sıçraması + cımbız/yutan mum; 28–31 Fibonacci; 31–35 Bladerunner EMA20 retesti, stop ve 1R/2R parçaları; 35–41 fazla işlem yapmama ve sonuç. S. 25, 26, 32, 33 görsel denetlendi.

**Karar:** S. 25–28 BB bant sıçraması ve yutan mum; s. 31–35 Bladerunner EMA20 retesti, [085. parti](../batch_085/STRATEGIES.md) ile aynı isim ve kurallardadır; ayrıca önceki EMA20/BB adayları vardır. S. 33–34 1R'de yarı pozisyonu kapatıp kalanı giriş stopuyla 2R'ye bırakma, Maddy 090. partinin %60/+1R çıkış ablation'ının %50 varyantıdır; ayrı sinyal sayılmaz. Başlıktaki 30 dakika vaadine rağmen mekanik örnek M5'tir. S. 23 kısa MA yavaş MA altında iken long önerisi trend mantığıyla ters; s. 24 long/short stop yönü ve s. 33 emir süresi ifadeleri çeviride tutarsız. Bunları birebir kodlamak güvenilir değil. S. 22–23 faiz farkından garantili gelir, s. 8 aylık %5–10 beklentisi ve s. 40 %60 kazanma koşulu ampirik kanıt değildir. Yeni bağımsız aday açılmadı.

## 3. Günlük Forex Stratejisi — Frq Mid / Diego Núñez

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 17/Baskı 17/Günlük Forex Stratejisi - Güvenli ve Kazançlı Trading - Frq Mid (35 sayfa) - @eseckal.pdf>) · [Tam metin](03_forex_frq_mid.txt)

**Sayfa haritası:** s. 1–4 tanıtım ve D1 çerçevesi; 5–8 iki stokastik/BB20 ayarı ve parçalı risk; 8–13 trend, tip 1 ve tip 2 giriş; 14–19 EURJPY; 19–28 USDCHF; 28–35 EURUSD örnekleri. S. 5, 8, 10, 12, 14, 16, 28 ve grafikleri görsel denetlendi.

### FM91A — D1 yavaş stokastik trendinde hızlı stokastik aşırılık ve BB dış bant dönüşü

- **Kaynak (s. 5, 8–12):** D1 stokastik `K=52,D=1,slowing=10` çizgisi 50 üstünde long rejimi, altında short. `K=10,D=1,slowing=5` 20'ye düşerek geri çekilme (short için 80'e çıkış). Long aynı yönde fiyat alt BB(20,2)'ye değsin ve yeşil D1 mum alt bandın üstünde kapansın; short üst banda temas, kırmızı mum altında kapansın. S. 17 ana stokastik 50'yi ters geçerse kârlı görünse de sinyali reddeder. Giriş kapanış sonrası; stop swing ve bandın ötesi; üç eşit parça: orta bantta ilk, karşı dış bantta ikinci, sonuncu büyük trende bırakılır (s. 6–8, 22–23).
- **Nesnel ön kayıt (bizim):** Klasik SMA yumuşatmalı `%K52 = SMA10(rawStoch52)` ve `%K10 = SMA5(rawStoch10)`; D=1 çizginin kendisi. Kaynak platform formülü doğrulanmadan platform eşdeğerliği kesin değildir. Önceki **tamamlanmış** D1 stokastik52>50 ve sinyal gününde de >50 long; son 5 kapanmış D1 içinde stokastik10<=20, sonra sinyal gününde `low<=lowerBB` ve `close>lowerBB`, `close>open`. Short simetri. `5` geri çekilme süresi bizim parametremiz. BB sinyal barı kapanışlarıyla hesaplanır; işlem sonraki ilk M1 fiyatında. Sinyal kapanışı orta BB'yi geçmişse ilk hedef geçmişte kaldığından sinyali bu kol için atla.
- **Stop/çıkış:** İlk stop `min(last confirmed D1 pivot low, signal low, lowerBB)−0,1 ATR14_D1` long, short tersi; pivot 2 sağ D1 barla **önceden teyitli** olmalı, yoksa sinyal dibi/bandı kullan. Üç eşit parçayı girişte sabitle. TP1 sinyal anındaki dondurulmuş orta bant, TP2 dondurulmuş karşı bant; yalnız hedefler girişin doğru tarafında ve sırayla ise işlem geçerli. TP1 sonrası kalan stopu giriş ile ilk stop arasındaki mesafenin yarısı kadar riski azaltacak yere çek; asla stopu kötüleştirme. TP3 için kaynak kesin çıkış vermiyor: ana stokastik52'nin 50'yi ters geçtiği kapanış sonrası ilk M1 veya 30 D1 azami süre **bizim** test çıkışımız. Her parçada ücret/kayma/fonlama; aynı M1 stop/TP çatışmasında stop önce.
- **Örtüşme:** Önceki BB dönüş ve stokastik aşırılık aileleriyle sinyal eşleşmesini say; hızlı stokastik filtresini çıkaran ve yavaş trend filtresini çıkaran kolları ayrı karşılaştır. S. 21–23 birkaç seçilmiş grafik, tarih dışı kripto performans kanıtı değildir.

### FM91B — Yavaş stokastik 50 rejim değişimi sonrası ilk BB orta bant geri testi

- **Kaynak (s. 9–10, 13, 15–16, 18–20, 30–33):** D1 yavaş stokastik52 çizgisi 50'yi geçerek yeni yön belirler. Tip 1'e göre daha sığ **ilk** geri çekilmede BB orta veya ilgili dış bant test edildikten sonra yönlü mum test edilen bandın doğru tarafında kapansın; hızlı stokastik20/80 şartı aranmaz. Üç parçalı çıkış ve stop aynı aileden. Örneklerde tip 2 ilk hedefi çoğunlukla karşı dış bant, s. 6 genel metni ise orta bant der; bu tutarsızlık saklanır.
- **Nesnel ön kayıt (bizim):** Önceki D1 `stoch52<=50`, son D1 `stoch52>50` long rejim geçişi; sonraki en fazla 10 **kapanmış** D1 içinde yalnız ilk uygun long geri test. Geri test gününde `low<=middleBB` ve `close>middleBB`, `close>open`; short simetri. Rejim geçişi ile test aynı günse ilk sinyali **ertesi gün** arayarak geleceği kullanma riskini önle. `10` gün penceresi bizim. Dış bant temasını zorunlu kılan sürüm ayrı duyarlılık kolu; aynı olay iki adayda denk gelirse tek pozisyon olarak say.
- **Stop/çıkış:** FM91A'daki swing/BB/ATR stop ve sonraki ilk M1 icrası. Tip 2'de orta banttan dönüşte TP1 dondurulmuş karşı dış bant; TP2 için kaynak kesin seviye vermiyor, deney kolunda `2R`; üçüncü parça stokastik52 ters geçişi veya 30 gün. Bu hedefler **bizim** tamamlamamız; kaynağın tip 2 çıkışını birebir temsil etmez. TP1'i girişin yanlış tarafında olan, stop maliyetin iki katından dar olan veya hedef/stop sıralaması geçersiz sinyal atlanır. Stop önce, ücret/kayma/fonlama ve aynı sembolde açık pozisyon varken yeni sinyalin engellenmesi ön kayıtlıdır.
- **Örtüşme:** FM91A ve mevcut BB orta bant/ilk retest adaylarına karşı aynı D1 takviminde karşılaştır; “ilk geri test”in ek katkısını ikinci/sonraki testlerle ablation olarak ölç.

**Uygulama sınırı:** Kaynak Forex pariteleri ve 2017–2019 seçilmiş grafikler kullanır; performans, kripto perpetual için doğrulanmış değildir. Yazar s. 7'de kişisel %2–3 risk kullanımını anlatır; araştırma risk bütçesi olarak alınmaz. Çeviride bazı örneklerde fiyat yönü ve TP sırası değişir (özellikle s. 16, 28, 30–35); test edilecek kesin kurallar yukarıdaki kaynak/varsayım ayrımına göre dondurulmalıdır.
