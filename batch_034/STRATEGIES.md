# Kitap okuma 034 — Darvas kutusu, hacim teyitli kırılım, VWAP kırılım başarısızlığı

**Kapsam:** 59 + 54 + 58 = **171 PDF sayfası**. Sayfa sıralı tam metinler bu klasörde. Darvas PDF'si aynı sunumu İngilizce/Türkçe tekrarlar (s. 4–31 / 33–59); VWAP PDF'si de Türkçe/İngilizce tekrarlar (s. 2–29 / 31–58). Metin çıkmayan Darvas grafiklerinden s. 11 ve 29 görsel incelendi. Atıflar PDF sayfasıdır. Backtest/paper test/emir yapılmadı.

## 1. Jaynesh Kasliwal — Darvas Box Trading

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 16/Baskı 16/Darvas Box Trading - Jaynesh Kasliwal - Orijinal ve Türkçe (59 sayfa) - @eseckal.pdf>) · [Tam metin](01_darvas_kasliwal.txt) · [Grafik s. 29](darvas_page29.png)

**Kaynak:** 52 haftalık yeni yüksekten sonra izleme; sonraki üç mumun bu yüksek üzerinde kalıcı kopuş yapmamasıyla **tavan** tanımı; taban yakındaki dönüş dibi (s. 5–10, 34–39). `close>ceiling` alış, stop `floor` altı; yeni kutular oluştukça stop yeni tabana taşınır ve daha sonraki kırılımlarda küçük eklemeler yapılabilir (s. 24, 28, 53, 57). Artan hacim istenir; hisse temelleri ve sektör liderliği kaynak seçiminin parçasıdır (s. 5–7, 30, 59). Kutu süresi/genişliği için sabit eşik verilmediği s. 24/53'te açıkça söylenir. Tarihsel getiri anlatısı veya gösterilmiş grafik kârlılık kanıtı değildir.

### D34 — 52 haftalık tepe sonrası teyitli kutu tavanı kırılımı

- **Bizim UTC D1 long sözleşmesi:** En az 365 günlük veri ve listelenme/point-in-time evren. `A` gününde `high[A]>max(high[A−365:A−1])`; sonra tam üç D1 `A+1..A+3` barın hiçbirinin **high** değeri `high[A]` üstüne çıkmamalı. Tavan `C=high[A]` ancak `A+3` kapanınca kullanılabilir. Taban `F=min(low[A:A+3])` **bizim** dar kutu tanımımızdır; kitap yalnız dönüş dibi der. Kutu genişliği `(C−F)/ATR14_D1` eğitim döneminde üst sınırla filtrelenir. İlk sonraki D1 `close[t]>C` ve `volume[t]>SMA20(volume)[t−1]` long sinyal; sonraki ilk 1m uygulanabilir fiyatında giriş. `F−0.1ATR14_D1[t]` stop; ilk iki haftada kırılım yoksa kutu iptal **bizim** sonlandırmamızdır. Girişten önce `close>EMA200` ve EMA200 yükselmesi kaynak trend fikrinin nicel filtresi (s. 9). 52 haftalık “%15–20 yakınlık” önerisi sinyal tanımına zorla eklenmez.
- **Çıkış:** Yeni teyitli kutuların `F_new` seviyesi kapanmış veriyle oluşunca stop `max(eski_stop,F_new−0.1ATR)`; stop asla gevşetilmez. H30D azami süre bizim araştırma sınırı. Pyramiding yalnız ayrı kol, toplam pozisyon riski başlangıç bütçesini aşmayacak. Short Darvas metninde simetrik kural yok; otomatik short türetmiyoruz.
- **Karşılaştırma:** Klasik 365 günlük yüksek kapanış kırılımı, üç günlük kutu beklemesi ve hacim filtresi aynı olay havuzunda; önceki Donchian adaylarıyla sinyal eşdeğerliği. Kutunun `F` değerini ilerideki minimum dipten seçmek yasak.

## 2. Michael Norman — Breakout ve Pullback Trading Stratejileri

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 22/Baskı 22/Breakout ve Pullback Trading Stratejileri - Michael Norman (54 sayfa) - @eseckal.pdf>) · [Tam metin](02_breakout_pullback_norman.txt)

**Kaynak:** Direnç/destek ve V biçimli teyitli swing kırılımı ayrımı (s. 6–8). Büyük kapanışlı kırılım, seviyenin hemen altında sıkışma ve büyüyen hacim aranır (s. 6–7, 12–14). Long kırılımda VWMA yukarı eğimli olmalı; stop kırılım mumunun altı, kâr çıkışı VWMA altı kırılım (s. 15–16). Trendle, yapıya yakın ve sıkışma ardından işlem tercih edilir (s. 19–36). S. 36 yaklaşık 2 ATR stoplu başka bir örnek sunar; ilk yöntemin kırılım mumu stopuyla aynı kural değildir. S. 43–44 kırılan seviyeye geri çekilme fikri, fakat azami bekleme/tolerans/giriş tetiği verilmez. Kitap yer yer başka yazara “Rayner” diye hitap eden derleme/çeviri izleri taşıyor; kuralları tek tutarlı kaynak olarak varsaymayız.

### N34a — D1 sıkışma kırılımı + VWMA20 eğimi

- **Bizim kapanmış D1 tanımı:** Önceki 20 tam D1 barın direnci `R=max(high[t−20:t−1])`; son 5 barın yüksek–düşük aralığı `<=2 ATR14_D1[t−1]`, o barların toplam aralığı önceki 20 günlük aralık alt yarısında ve son 5 bar kapanışlarının çoğu `R−0.5ATR` üstünde ise direnç altı sıkışma. Bu sınırlar **bizim** sayısallaştırmamızdır. Sinyal `close[t]>R+0.1ATR14_D1[t−1]`, `volume[t]>SMA20(volume)[t−1]`, `VWMA20[t]>VWMA20[t−3]`, VWMA `sum(close*volume)/sum(volume)`; sıfır hacim/veri eksikse yok. Sonraki ilk 1m giriş. Stop `low[t]−0.1ATR14_D1[t−1]`, hedef kaynak gereği sabit değil: ilk tam D1 `close<VWMA20` sonrası ertesi 1m çıkış; zarar stopu intrabar izlenir, H14D bizim azami süre. Short kırılım aynı mantığın simetrik araştırma koludur, ancak kitabın s. 13–16 ayrıntısı long üzerinedir.
- **Karşılaştırma:** Sıradan 20 günlük kırılım, sıkışma filtresi, hacim, VWMA eğimi ardışık ablation. Breakout mumunun büyüklüğü ile geç giriş/çok geniş stop arasındaki ilişki ayrıca raporlanır; ilk stop `entry`den büyükse long yok.

### N34b — Aynı seviyenin ilk geri testi

- **Kaynak:** Kırılmış direnç alanına dönüşte long arama (s. 43–44); kesin mekanik tarif yok.
- **Bizim ayrı giriş kolu:** N34a olayında ilk giriş yerine, sonraki en çok 5 tam D1 içinde `low<=R+0.1ATR` ve `close>=R` olan **ilk** retest barını bekle; sonraki ilk 1m giriş, stop `min(retest low,R−0.5ATR)−0.1ATR`, çıkış N34a gibi. Retest gelmeyen kırılımlar işlem yok olarak sayılır. İlk kırılım girişleriyle **aynı kırılım havuzunda** paired kıyas; retestin geleceğini kırılım gününde biliyormuş gibi seçme yok.

## 3. Varun Speak — VWAP Breakout Başarısızlığı Stratejisi

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 22/Baskı 22/VWAP Breakout Başarısızlığı Stratejisi - Varun Speak - Türkçe ve İngilizce (58 sayfa) - @eseckal.pdf>) · [Tam metin](03_vwap_failed_breakout.txt)

**Kaynak:** Önce cari gün VWAP üstüne çıkan fiyatın yeniden VWAP altına dönmesi ve alıcıların sıkışması short kurulumu; long simetrik (s. 2–3, 31–32). Önceki gün VWAP, önceki gün yüksek/düşük/kapanış, cari açılış ve pivotlar ek karar seviyeleri (s. 4, 33). Örneklerin çoğu Hindistan seanslı hisse/endeks/emtia M5/M10/M15'tir. S. 5–13 ve 15–28 farklı teyit sıraları ve farklı stop/hedefler gösterir: örneğin 60 puan, 25 puan veya %1 stop; YDay VWAP, gün dibi veya pivot hedef. Bunlar genel sabit eşik değildir. “10:00 sonrası” yerel piyasa seansına bağlıdır (s. 2), 24/7 kriptoya doğrudan aktarılmaz.

### V34 — Cari UTC gün VWAP'ının başarısız üst/alt kırılımı

- **Bizim M15 sinyal:** UTC gün sınırında VWAP sıfırlanır; her **tam kapanmış M15** için `CVWAP[t]=sum(session typical_price*volume)/sum(session volume)`; `typical=(H+L+C)/3`, sıfır hacimde olay yok. **PVWAP** yalnız önceki tamamlanmış UTC günün ayrı değeri. Short: cari günde en az iki kapanmış M15 bar `close>CVWAP` ve en az birinde `close>PVWAP` olmuş olmalı; ardından ilk `close[t]<CVWAP[t]` ve `close[t−1]>=CVWAP[t−1]` geri kaybı. Long simetrik. Kaynak CVWAP etrafında işlemi der, iki bar ve PVWAP şartı bizim sıkışmış trader tanımıdır. Giriş sonraki ilk 1m uygulanabilir fiyatında, stop başarısız kopuş boyunca oluşmuş **önceki tamamlanmış** tepe `+0.1 ATR14_M15`, long simetrik. Risk çok genişse işlem yok; hedef PVWAP yalnız girişin kâr tarafında ve >1R ise, diğer durumda 2R veya UTC gün sonu; aynı 1m barda stop önceliği.
- **Ablation:** Yalnız CVWAP kaybı, önce PVWAP üstü/altı, önceki gün high/low veya pivot retest filtresi. Pivotlar önceki tamamlanmış gün OHLC'den sabit hesaplanır; cari gün high/low **olay anına kadar** hesaplanır. M10 barların mevcut M1 serisinden zaman sınırlarıyla kurulabilirliği doğrulanır; ana deney M15. CVWAP'ı barın tüm hacmi ile bar **içinde** işlem yapmış gibi kullanma yok; ancak kapanış sonrası sinyal.
- **Veri sınırı:** İşlem bazlı gerçek VWAP varsa ona öncelik verilir; M15 `typical*volume` yaklaşımı kaynak platform VWAP'ının birebir yeniden üretimi değildir. Venue, volume birimi, eksik mum, seans sınırı ve maliyet duyarlılığı raporlanmalı. Önceki VWAP/retest adaylarıyla aynı olayların tekrar sütun olarak eklenmesi gerekmez.

## Öncelik

V34, M15 veri kalitesi ve maliyetle; D34, mevcut 52 hafta/Donchian kırılımlarına ek değeriyle; N34a/b aynı kırılım havuzunda giriş zamanlamasıyla sınanabilir. Kârlılık iddiası yok. Tüm adaylarda point-in-time evren, geçmişten hesaplanan seviyeler, ücret/spread/kayma/funding ve zaman sıralı dış örneklem gerekir.
