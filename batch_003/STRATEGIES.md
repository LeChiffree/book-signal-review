# Kitap okuma 003 — mum, hacim ve grafik formasyonları

**Kapsam:** Üç PDF'nin tüm 176 + 83 + 40 = **299 sayfasının metni çıkarıldı** ve strateji bölümleri sayfa bazında incelendi. Sayfa numaraları PDF sayfasıdır. Aşağıdaki kurallar işlem tavsiyesi veya kanıtlanmış getiri değil, sonraki backtest ve paper test için **hipotez** kayıtlarıdır. Kaynakta bulunmayan sayısal tanımlar açıkça uyarlama olarak işaretlidir.

## 1. Mum Formasyonları İçin Dürüst Bir Rehber — Llewelyn James

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 19/Baskı 19/Mum Formasyonları İçin Dürüst Bir Rehber - Hedefe Yönelik Trading - Llewelyn James - Orijinal (176 sayfa) - @eseckal.pdf>)

Kitap 14 boğa/ayı mum formasyonunu hisse örnekleriyle araştırıyor. Formasyonun kendi başına yaklaşık yazı tura düzeyinde kalabildiğini, giriş ve çıkışın sonuçları ciddi değiştirdiğini kabul ediyor (s. 43–48, 173). SPY filtresi, hisse fiyatı ve lot hacmi eşikleri ile seans açılış boşlukları 7/24 kripto vadeli işlemlerine doğrudan taşınamaz. Gösterilen oranlar ve optimize edilmiş hedef/stoplar ileriye dönük kanıt değildir. Yutan mum bölümünün sonuç anlatımı ile nihai stop/hedef satırı da uyuşmuyor (s. 48); bu parametreler alınmayacak.

### C1 — Yükseliş yutan mum sonrası geri çekilme

- **Kitap:** Yükseliş yutan mumun gövde tanımı (s. 41–42); yalın sinyalin zayıf sonuçları (s. 43); RSI/stokastik/hacim filtreleri genellikle sonucu iyileştirmedi (s. 44); sonraki gün zirve teyidi yerine desen dibine geri çekilme girişi kaynak örnekleminde daha iyi çıktı (s. 46–47).
- **Uyarlama, kapalı günlük olay:** Önceki mum düşüş, bugünkü mum yükseliş; `open[t] <= close[t-1]` ve `close[t] >= open[t-1]`, `body[t] >= 0.5*ATR14[t-1]`. Son koşul kitapta yoktur. 20 günlük düşük civarı ve rejim filtresi ayrı varyanttır, aynı hipoteze gömülmez.
- **Yürütme:** Mum `t` kapanınca, yalnız `t+1` boyunca desen aralığının önceden sabitlenmiş bir noktasında alış limit emri; dolmazsa iptal. Kontrol: kapanış sonrası ilk yürütülebilir 1m açılışında alış. Stop desen dibinin altında veya 1 ATR; çıkış 3/7/14 gün ile 1R/2R varyantları. Emir dolumunda 1m fiyat yolu ve ücret kullanılır; aynı bardaki stop/hedef sırası muhafazakâr çözülür.
- **Test sorusu:** Geri çekilme girişi, dolmayan emirleri de hesaba katınca piyasa girişinden üstün mü? Mevcut yutan mum özellikleri tekrar üretilmez.

### C2 — Çekiç ve aşırı satış sonrası dönüş

- **Kitap:** Çekiçte alt fitil gövdenin en az iki katı; üst gölge küçük (s. 71–72). Önceki gün `RSI(2)<5` filtresi ve sonraki gün iki günlük dipte alış örneklemde kullanılıyor (s. 74–76).
- **Uyarlama, kapalı günlük olay:** `lower_wick >= 2*body`, `upper_wick <= 0.1*(high-low)`, `high>low`, önceki 5 günlük fiyat değişimi negatif. Ayrı ablation: önceki kapanmış gün `RSI2<5`. Önceki düşüş için 5 gün seçimi bizim parametremizdir. Fiyatın iki günlük dibe geri dönmesi için yalnız sonraki gün geçerli limit emir; dolmayanlar kayıtlı.
- **Çıkış:** Çekiç dibi altı stop, önceden dondurulmuş 1R/2R veya 3/7/14 gün çıkışları. Kitaptaki hisse bazlı getiri beklentisi aktarılmaz.

### C3 — Boşluk gerektiren üç mumlu yapılar

- **Kitap:** Sabah yıldızı ve akşam yıldızı tanımları seans boşluğu içeriyor (s. 52–55, 121–128); delici bulut ve kicker da açılış koşullarına bağlı (s. 60–69, 79–87). Sabah yıldızında desen dibine geri çekilme emri anlatılıyor (s. 55).
- **Karar:** Özgün biçimler sürekli 7/24 kripto serisinde **ertelendi**. Gap koşulunu atmak ayrı bir strateji üretir; önce eşik, kapanmış üç mum, sonraki mum onayı ve olay sayısı tanımlanacak. Önceki ekteki “gap gerektirmeyen sabah/akşam yıldızı” bu nedenle kaynak kuralı diye sunulmamalı.

## 2. Hacim Fiyat Analizi — George Milton

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 19/Baskı 19/Hacim Fiyat Analizi - Nasıl Yapılacağına Dair Nihai Yeni Başlayanlar Rehberi - George Milton (83 sayfa) - @eseckal.pdf>)

Kitap hacmi kırılım teyidi, dalga gücü, düşük hacimli düzeltme, OBV/MFI ve hacim zirvesi olarak kullanıyor (s. 22–60, 72–82). Kesin ifadeler ampirik güvence değildir. Özellikle s. 25'te DAX vadeli örneğinde 87 dalganın 40'ı belirlenen kırılım koşulunu sağlamış; bu 7/24 kripto için üstünlük kanıtı değil. S. 60'ta MFI filtresi isabeti sadece %51,29'dan %51,65'e getirmiş; bunu zorunlu filtre yapmayacağız.

### V1 — Hacimle teyit edilen bant kırılımı

- **Kitap:** Destek/direnç ötesindeki ortalama üstü hacim kırılım teyidi sayılır (s. 22). Direncin oluştuğu bardaki hacme kıyasla en az %10 fazla hacim örneği de verilir (s. 48).
- **Uyarlama, kapalı günlük olay:** `close[t] > max(high[t-20:t-1])`; `quote_volume[t] / median(quote_volume[t-20:t-1]) >= 1.2`. 20 bar, medyan ve 1.2 bizim sabit başlangıç tanımımız; kaynakta yalnız “ortalama üstü” ve farklı bir referansa göre %10 var. Kontrol: aynı kırılımın hacim filtresiz hali. Çift sayımı önlemek için s. 48'deki direnç mumu hacim oranı ayrıca alternatif filtre olur.
- **Yürütme:** Günlük kapanıştan sonraki ilk yürütülebilir 1m açılışı; aralık içine geri kapanış veya 1 ATR stop; 3/7/14 gün ve 1R/2R ayrı çıkış. Quote hacim seçimi, varlıklar arası ölçek ve geçmiş likidite filtresi veride dondurulur.

### V2 — Güçlü itki, düşük hacimli düzeltme, yeniden kırılım

- **Kitap:** En az üç trend yönlü yüksek hacimli mum “hacim dalgası” olarak anlatılıyor (s. 24, 40–42). Düzeltmede ortalama dalga hacminin yaklaşık %50 düşmesi ve önceki dalga zirvesinin üzerinde kapanışla giriş veriliyor (s. 26–29, 45). Bu, grafik formasyonu kitabının bayrak fikriyle aynı olay ailesidir; bağımsız kanıt sayılmaz.
- **Uyarlama, kapalı günlük olay:** Son 15 barda üç ardışık yukarı kapanışın her birinde `quote_volume > MA20(quote_volume)`; ardından 2–8 bar fiyat geri çekilmesi ve düzeltmenin ortalama hacmi itki ortalamasının `<=0.5` katı; bugün itki zirvesi üzerinde kapanış. 15/2–8 pencereleri bizim tanımımız. İtki, düzeltme ve kırılım bitmeden geçmiş bara etiket yazılmaz.
- **Yürütme:** Sonraki 1m açılışı; düzeltme dibi stop, 1R/2R ve süre çıkışı. 0.5 katsayısı kaynakta var; onun çevresi duyarlılık olarak ölçülür. Bayrak/dar bant baz çizgisiyle karşılaştırılmalı.

### V3 — OBV/MFI ve hacim zirvesi

- **Kitap:** OBV fiyatı teyit/ayrışma için kullanılıyor (s. 34–38); MFI filtre denemesi (s. 57–60); yüksek hacimli dar mum dönüş ihtimali (s. 43) ve satış zirvesinin mutlaka nihai dip olmadığı notu (s. 78–80).
- **Karar:** OBV/MFI ayrı yeni ana strateji sayılmıyor; V1/V2 için önceden ilan edilmiş filtre ablation'ı olabilir. Hacim zirvesi + dar aralık ancak `volume/median20`, `range/ATR14`, kapalı bar teyidi ve rejim tanımlandıktan sonra aday olur. “Büyük oyuncu birikimi” yorumu OHLCV'den kesin gözlenemez. TRIN/McClellan (s. 55, 69–71) piyasa geneli breadth verisi istediği için mevcut tekil mum veri akışında ertelendi.

## 3. Grafik Formasyonları Uzmanlığı — Lalit Mohanty

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 18/Baskı 18/Grafik Formasyonları Uzmanlığı - Lalit Mohanty (40 sayfa) - @eseckal.pdf>)

Baş ve omuz, çift tepe/dip, üçgen, bayrak/flama, dikdörtgen/kama, fincan-kulp ve boşluklar anlatılıyor (s. 9–32). Kitap formasyonların sayısal toleransını, örneklem sayısını veya sistematik performansını vermiyor. Kaynakta s. 32 sonraki bölüm diye “ada dönüşü ve kaçak boşluk” vaat edilse de kitap s. 33'te sonuca geçiyor; bunlara özgü işlem kuralı çıkarılmadı.

### G1 — Çift dip / çift tepe boyun çizgisi kırılımı

- **Kitap:** İki yaklaşık eşit dip/tepe ve aradaki boyun çizgisinin kırılmasıyla doğrulama; stop ikinci dip/tepe ötesi, hedef desen yüksekliği (s. 13–15).
- **Uyarlama, kapalı günlük olay:** Yalnız `k=3` sağ ve sol barı tamamlanmış pivotlar kullanılacak. İki dip arası 5–30 bar, dip seviyesi farkı `<=0.5 ATR14`, aradaki zirve en az `1 ATR` yukarıda; bugün boyun çizgisi üstünde kapanış. Ayı yönü tersidir. Pivot teyidi gelmeden erken tarihli işaret oluşturulmaz. Bu eşiklerin tamamı bizim mekanikleştirmemizdir.
- **Yürütme:** Sonraki 1m açılışı; ikinci dip/tepe ötesi stop; boyun çizgisi–dip yüksekliği hedefi ve 3/7/14 gün çıkışı ayrı test. Olay sayısı ve uzun/kısa asimetrisi raporlanmalı.

### G2 — Yatay bant / üçgen / bayrak ailesi

- **Kitap:** Yükselen üçgende düz direnç ve yükselen dipler (s. 17–19); bayrakta itki sonrası karşı yönlü kısa konsolidasyon ve hacim daralması (s. 20–22); dikdörtgende yatay bant ve sınır kırılımı (s. 23–26). Stop karşı sınırda, hedef formasyon yüksekliğinde anlatılıyor.
- **Karar:** İlk test için **yatay bant kırılımı** tekrarlanabilir baz olaydır: geçmiş 10 tamamlanmış barın genişliği `<=3 ATR14` ve bugünkü kapanış üst sınırın üzerinde. 10 ve 3 bizim sayısal tanımımızdır. Üçgen/bayrak ancak teyitli iki tepe ve iki dip, eğim toleransı, azami yaş ve kırılım kuralı sabitlenince alt grup olarak sınanır. V1'in hacim teyidi ve V2'nin düşük hacimli düzeltmesi, bu olayların bağımsız “yeni strateji” değil filtre varyantlarıdır.
- **Yürütme:** Sonraki 1m açılışı; önceden bilinen alt sınır veya 1 ATR stop; kanal içine geri kapanış ve süre çıkışı. Kitapta gösterilen desen yüksekliği hedefi karşılaştırma olarak eklenir.

### G3 — Baş omuz, fincan kulp ve gapler

- **Kitap:** Baş omuz boyun çizgisi (s. 10–12), fincan-kulp kulp tepesi kırılımı (s. 27–29), açılış boşluğu sınıfları (s. 30–32).
- **Karar:** Baş omuz ve fincan-kulp, teyitli pivot ve şekil toleransı olmadan öznel; ilk otomatik testte ertelendi. Gap bölümü seanslı piyasaya bağlı; sürekli kripto serisine olduğu gibi kodlanmaz.

## Birleşik test sırası ve veri sözleşmesi

1. **Bazlar:** C1 yalın yutan mum, C2 yalın çekiç, V1 hacimsiz 20 günlük kırılım, G1 teyitli çift dip, G2 yatay bant. V1 ile G2 ve önceki partideki P1 yakın akrabadır; benzer işlem listelerini ayrı keşif başarısı sayma.
2. **İkili kombinasyonlar:** C2 + yalnız kapanmış barda yüksek göreli hacim (kitap 2, s. 23); G2 + V1 hacim teyidi; V2 + piyasa trend filtresi. Üçlü veya dörtlü filtreleri olay sayısı ve dış örneklem sonucu görülmeden kurma; karmaşıklığı ablation ile gerekçelendir.
3. **Ortak karar anı:** UTC günlük kapanışından sonra özellikler; en erken sonraki yürütülebilir 1m. `high/low` ile aynı bardaki sıralama bilinmiyorsa iyimser dolum yok. Eğitim/test zaman ayrımı, komisyon, spread, kayma, funding, delist/survivorship ve dolmayan limit emirler raporlanır. Sinyal ve çıkış parametreleri test öncesi dondurulur.
4. **Mevcut pilot:** Yutan mum, çekiç, Donchian, ATR, RSI, OBV/MFI ve hacim oranı benzerleri özellik manifestinde denetlenir; eşdeğeri varsa yeni sütun yaratılmaz. Bu partide kod, backtest veya paper emir açılmadı.

**Sonraki tartışma için tercih:** En ölçülebilir ilk karşılaştırma `G2/V1 yatay bant kırılımı × hacim filtresi` ile `V2 düşük hacimli düzeltme` olur. C1/C2 daha çok giriş yöntemi ve piyasa rejimi araştırmasıdır. Seçim ancak maliyetli dış örneklem testiyle yapılır.
