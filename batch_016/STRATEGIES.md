# Kitap okuma 016 — Ichimoku/ADX, AB=CD ve bayrak kırılımı

**Kapsam:** Üç PDF'nin **73 + 17 + 22 = 112 PDF sayfası** işlendi. Kaynak numaraları PDF sayfasıdır. ABCD'nin s. 6'daki oran çizimi görsel olarak da kontrol edildi. Aşağıdaki kurallar gelecekteki backtest/paper test için hipotezdir; bu partide test veya emir yok.

## 1. Fabio Monterrey Albizu — Adım Adım Ichimoku

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 13/Baskı 13/Adım Adım Ichimoku - Fabio Monterrey Albizu (73 sayfa) - @eseckal.pdf>)

Kitabın üç tetik ailesi: **Tenkan(9)–Kijun(26) kesişimi** (s. 22–23), **fiyatın bulutu kırması** (s. 36–37) ve **fiyatın Kijun'u geçmesi** (s. 62–63). Bulut Senkou A/B için 26 mum ileri çizim, A `(Tenkan+Kijun)/2`, B 52 mumluk H/L orta noktası (s. 14–18). Fiyat/çizgilerin buluta göre konumu, her iki çizginin yönlü eğimi ve **ADX(14)>=25** filtre; çıkış ters yöne Kijun kapanışı (s. 19–23, 36, 62–63). ADX 25'i sinyalden sonra geçebilir (s. 25, 28, 46), ancak kaynak bekleme son süresini tanımlamaz. Chikou 26 mum geriye çizilir, isteğe bağlı filtre (s. 17, 23). Bulutun **grafikte ileri çizilmiş değerini bugünün biliniyor olmayan ileri fiyatı gibi kullanmak** hatalıdır; t'de çizilen bulut t−26'da hesaplanmıştır.

### I16a — H4 Tenkan/Kijun kesişimi

- **Kapanmış H4 tetik:** `Tenkan[t-1]<=Kijun[t-1] && Tenkan[t]>Kijun[t]` long; short simetrik. `Tenkan=(HH9+LL9)/2`, `Kijun=(HH26+LL26)/2`, son bar dahil, yalnız tamamlanmış H4. Longda iki çizgi `t-1` değerlerinden büyük, `close[t]>max(cloudA_visible[t],cloudB_visible[t])`, Wilder `ADX14[t]>=25`; short tüm yön ters. `cloudA_visible[t]`, t−26'da oluşan A'nın bugüne çizilmiş değeri; B de t−26'da mevcut 52 mumla. Önceki 26 mumlik warmup zorunlu.
- **Giriş/çıkış:** Tetik kapandıktan sonraki ilk işlem yapılabilir 1m. Kaynağın Kijun ters kapanış çıkışını koru; gerçek koruyucu stop ayrıca sinyal mumunun karşı ucu `±1 tick` veya giriş anında dondurulmuş Kijun'un karşısı ayrı. 2R ve 8/16 H4 zaman çıkışı karşılaştırma, kaynak kuralı değil. ADX geç kalırsa baz varyant tetik anında `>=25` ister; sonraki en çok 3 H4 içinde eşiği geçme **ayrı** ön tanımlı varyant. Aynı kesişimden ikinci sinyal yok. Chikou filtresi `close[t] > close[t-26]` long ve t−26 çevresi bulut konumu ile ayrı ablation; geçmişe çizilmiş Chikou'yu yeni bilgi gibi okumama.

### I16b/I16c — Bulut kırılımı ve Kijun geçişi

- **I16b bulut:** Long `close[t-1]<=cloud_upper_visible[t-1] && close[t]>cloud_upper_visible[t]`, `Tenkan>Kijun`, ikisi de yukarı eğimli, `ADX14>=25`; short alt bulut simetri (s. 36). Giriş sonraki 1m, stop sinyal mumunun karşı ucu, çıkış ilk ters Kijun kapanışı; 2R karşılaştırması. Bulut değeri her bar için **o bara 26 önceki kapanışta çizilmiş** değer; geleceğe sızma engellenir.
- **I16c Kijun:** Long `close[t-1]<=Kijun[t-1] && close[t]>Kijun[t]`, görünür bulut üstü, Tenkan ve Kijun pozitif eğim, `ADX>=25`; short simetri (s. 62–63). Stop sinyal mum karşı ucu veya Kijun altı ayrı; çıkış ilk ters Kijun kapanışı. Üç tetik aynı barda olabilir; tek pozisyon, üç olay etiketi. Batch 004 Ichimoku ve batch 007 candle/Ichimoku ile eşdeğerlik denetimi yapılmadan yeni bağımsız alpha sayılmaz. Kitabın “açıkça” geçiş söylemi için eşik vermemesi sebebiyle kapanışta 1 tick ayrışma bizim sınırımız.

## 2. Sundeep Bilkhu — ABCD Formasyonu

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 8/Baskı 8/ABCD Formasyonu - Sundeep Bilkhu (17 sayfa) - @eseckal.pdf>)

Kaynak AB itki, BC geri çekilme, CD'nin AB ile **1:1** veya 1.27/1.618 ölçülü uzantısı olduğunu söyler (s. 6–7). BC için çoğunlukla 0.618, en çok **0.786**; s. 6 parantezdeki `0.718` açık çeviri/yazım hatası, aynı sayfanın grafiğinde `0.786` ve s. 7 örneği bunu destekliyor. C'den giriş, stop A ötesi, D ölçülü hedef (s. 7–10, 17). AB ve CD'nin mum sayılarının benzerliği isteğe bağlı teyit (s. 7, 10–11). Örnek grafiklerde A/B/C/D **sonradan çizilmiş**: C'nin oluştuğu an ancak sağ mumlarla teyit edildikten sonra işlem yapılabilir. S. 8'de “C noktasına genişledi” gibi etiket hataları var; oranı fiyat koordinatından hesaplayacağız.

### A16 — Teyitli ABC düzeltmesinden AB ölçülü devam

- **Nedensel pivot:** H4 fraktal `left=2,right=2`; A, B, C kronolojik teyitli dönüşler. Long A=dip, B=tepe, C=daha yüksek dip; short A=tepe, B=dip, C=daha düşük tepe. `retracement=abs(B-C)/abs(B-A)` için baz `0.618±0.05` veya `0.786±0.05` iki ayrı ön tanımlı kol; `>0.786+0.05` baz dışı. Kaynak ±0.05 vermez; piyasa tick/gürültüsü için bizim toleransımız. Hem C teyidi hem oran geçerli olmadan sinyal yok.
- **Emir/çıkış:** C teyidi kapanışından sonraki ilk 1m giriş; stop long `A-1 tick` veya `C-1 tick` ayrı, short simetri. Hedef `D=C+sign(B-A)×abs(B-A)` baz, 1.27/1.618 uzantısı ayrı. Hedef girişin yanlış tarafında ya da net ödül `<=1R` ise o kol işlem dışı. AB mum süresi `T1` ve C→D'nin `T1,1.27T1,1.618T1` ufukları **sonuç etiketi**, giriş anında gelecekteki D zamanı bilinmez. 2R standart hedef ve 1/2/3×T1 zaman çıkışı ayrıca. Batch 015 F15a 123 ile aynı pivot üçlüsüne uygulanır; oranın ek değerini ve daha erken/geç girişi aynı olay evreninde ölç.

## 3. Vladimir Ribakov — Bayraklar ve Flamalar ile Trade

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 7/Baskı 7/Bayraklar ve Flamalar ile Trade - Vladimir Ribakov (22 sayfa) - @eseckal.pdf>)

İki giriş tarifi ayrılmalı. **Klasik bayrak:** düzeltme sınırının dışında mum kapanışı, stop kırılım mumunun karşı ucu, kârın %80'i 1R'de ve %20'si bayrak yüksekliği kadar hedefte (s. 4–8). **Basamak/step bayrak:** birkaç büyük itki mumundan sonra dar yatay alan, sınır kırıldığı **anda** emir, stop kırılım mumunun karşı ucu, hedef bayrak derinliği; stop mesafesi hedeften büyükse işlem yok (s. 15–21). İkinci tarifte “kırılım mumunun dibi” kırılım anında henüz kesin değil: gerçek zamanlı girişle nihai mum dibini aynı anda bilmek mümkün değildir. Dolayısıyla aşağıdaki kapalı mum sistemi kaynak anlık girişinin birebir replikası değildir. `%70` başarı (s. 15) doğrulanmış veri değildir.

### F16a — Kapanmış H1 bayrak kırılımı

- **Bizim sayısal şekil:** Son 4 H1 mumunun net hareketi `>=2 ATR14_H1[t-1]` ve hepsi aynı yön; sonra 3–8 kapanmış H1 konsolidasyon mumu. Konsolidasyon `max(high)-min(low) <=0.75 ATR14_H1[flag_start-1]`, net kapanış kayması itkinin tersine `<=0.5×itki`. Bunlar kaynağın “güçlü hareket / küçük düzeltme” ifadesi için bizim ön tanımımız. Bayrak sınırı konsolidasyon mumlarının dondurulmuş en yüksek/en düşük değeri; eğik çizgi/üçgen zorlanmaz. Long ilk `close>flag_high+1 tick`, short simetri. Giriş sonraki ilk 1m; stop kırılım mumunun karşı ucu `±1 tick`, kaynak klasik hedefleri: pozisyonun %80'i 1R, kalan %20'si bayrak yüksekliği kadar. Bayrak yüksekliği `<stop_distance` ise kaynak step filtresi ayrı varyant; baz klasik sürümde sonuç etiketidir. Mevcut NR/inside bar ve batch 013 bayrak adaylarıyla örtüşme kaydedilir.

### F16b — Önceden dondurulmuş sınır için stop emri

- Konsolidasyon tamamlandığı **kapanışta** `flag_high+1 tick` ve `flag_low-1 tick` OCO stop emirleri bir H1 bar geçerli. Bu anlık kırılıma yakın ama sinyal tamamen önceki kapalı mumlardan üretilmiş olur. Girişte bilinmeyen “kırılım mumunun dibi” stopa kullanılmaz; önceki bayrağın karşı sınırı `±1 tick` kullanılır. 1m dolumla stop/karar sırası; hedef bayrak derinliği, ödül/stop `>1` filtresi. Klasik kapanış bekleme ile aynı kurulumlarda dolum, sahte kırılım ve net R farkı raporlanır. 3–8 bar, itki ve yatay aralık seçimi kaynak ölçüsü değil bizim uyarlamamızdır.

## Öncelik ve ortak sözleşme

Önce I16a/I16b'nin mevcut Ichimoku adaylarına ek değeri, A16'nın 123'e göre oran filtresi, sonra F16a/F16b giriş zamanlaması. Ücret, spread, kayma, funding, 1m yürütme, dolmayan stop emirleri, aynı mumda stop/hedef belirsizliği, dış örneklem ve tek olayın farklı kitap etiketleri raporlanmalı. Kaynakların örnek kârları test sonucu olarak kullanılmaz.
