# Kitap okuma 044 — Fibonacci kanal, fiyat kanalı ve RSI başarısızlık salınımı

**Kapsam:** 22 + 10 + 15 = **47 PDF sayfası**. Tam sayfa sıralı metinler kaydedildi; Fibonacci s. 6, 8, 9, 12 ve RSI s. 14 görselleri ayrıca incelendi. Atıflar PDF sayfasıdır. Kaynak anlatımı ve bizim test için sabitlediğimiz nesnel seçimler ayrıdır. Backtest, paper test ve emir yapılmadı.

## 1. Fibonacci Kanal Stratejisi — Trading Strategy Guides

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 7/Baskı 7/Fibonacci Kanal Stratejisi - Trading Strategy Guides (22 sayfa) - @eseckal.pdf>) · [Tam metin](01_fibonacci_channel.txt) · [Kanal görseli s. 8](fib_p8.png) · [Stop aktarımı s. 12](fib_p12.png)

**Kaynak:** Kanalların **içinde** işlem amaçlanır (s. 2). Short örneğinde güçlü düşüş, dipte ilk konsolidasyon, üstte ikinci konsolidasyon ve bu iki alanla eğimli Fibonacci kanalının çizilmesi anlatılır (s. 3–8). Üst kanal yakınındaki geri çekilmede ilk short; fiyat %50 kanal çizgisine ulaşınca ikinci short (s. 7–9). %100 alt kanal çizgisinde iki pozisyonu kapat; %50'ye inince ilk girişin stopunu %38 çizgisine, %78'e inince ikisinin stopunu %50 çizgisine taşı (s. 10–13). Long ters yöndür (s. 14). **Kaynak belirsizliği:** İlk stop fiyatı ve “konsolidasyon” için matematiksel tanım verilmemiştir; s. 3 başlığındaki “satış” metni yer yer “yükseliş” derken grafik açıkça düşüş kanalını gösterir. Kanalı geçmiş grafik üzerinde elle seçmek lookahead üretebilir.

### FC44 — Teyitli eğimli kanalda içeri dönüş

- **Bizim kanal geometrisi:** H1'de 2 sol/2 sağ barla teyit edilmiş pivotlar. Short için sırasıyla iki **alçalan** pivot tepe `P1=(i,H_i)`, `P2=(j,H_j)`, `j−i≥8` ve `≤80`; üst çizgi bu iki tepeyi birleştirir: `U(t)=H_i+(H_j−H_i)(t−i)/(j−i)`. İki tepe arasında teyitli en düşük dipten geçen paralel alt çizgi `L(t)=U(t)−w`; `w>2 ATR14_H1` olmalı. `P2` ancak sağdaki iki H1 mum kapanınca kanal **o anda** sabitlenir; bütün sonraki seviyeler sabit eğimle ilerletilir, geçmiş sinyaller yeni pivota göre yeniden hesaplanmaz. Long için iki yükselen dipten alt çizgi ve aradaki yüksek tepeden paralel üst çizgi. Bunlar kaynak çiziminin **bizim** deterministik karşılığıdır.
- **Olay:** Kanal onayından sonra en çok 30 H1 bar içinde short için ilk `high[t]≥U(t)−0.1w` ve `close[t]<U(t)−0.1w`, ayrıca kapanış kanal içinde olsun. Long alt çizgide simetrik. İlk giriş kapanıştan sonraki uygulanabilir 1m fiyatı. Stop short `U(t)+0.1 ATR14_H1`; long karşı simetri. Kanal kırılıp dışında H1 kapanışı gelirse yeni giriş iptal ve açık pozisyon sonraki 1m'de çık. `0.1w`, stop tamponu ve 30 bar sınırı bizimdir.
- **Ölçekleme/çıkış:** Short `F50(t)=U(t)−0.5w`, `F38(t)=U(t)−0.382w`, `F78(t)=U(t)−0.786w`, `F100(t)=L(t)`. İlk girişten **sonraki** tam H1 bar `low≤F50` olursa, sonraki 1m'de yalnız fiyat hâlâ `≤F50` ise ikinci eşit riskli giriş; ilk stop `F38` düzeyine çekilir, ama stop mevcut fiyatın doğru tarafında değilse giriş eklenmez. Sonraki bar `low≤F78` olunca iki stop `F50` düzeyine taşınır; `low≤F100` olunca hedef çıkış. Long simetrik. İşlem maliyeti ve iki kolun toplam risk bütçesi ayrı hesaplanır; ikinci giriş önceden belirlenmiş toplam risk üst sınırını aşamaz. Aynı 1m içinde birden çok seviye temasında kötümser sıra. 40 H1 bar süre sınırı bizimdir.
- **Karşılaştırma:** İlk giriş tek başına, ikinci girişli sürüm, aynı kanalın Fib stop aktarımı olmadan düz stop sürümü. Batch044 fiyat kanalı ve önceki Fibonacci kurulumlarıyla olay örtüşmesi ölçülmeli. Örneklerdeki seçilmiş işlemler getiri kanıtı değildir.

## 2. Kanal Trading — Alton Swanson

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 20/Baskı 20/Kanal Trading - Alton Swanson (10 sayfa) - @eseckal.pdf>) · [Tam metin](02_channel_swanson.txt)

**Kaynak:** İki yaklaşık paralel sınırla yükselen, düşen veya yatay fiyat kanalı çizilir (s. 3–4). Düşen kanalda üst dirençte short, stop üst sınırın ötesi, hedef alt destek; yükselen kanalda alt destekten long ve üst dirence hedef (s. 5–7). Orta bölgede işlem aranmaması ve kanal kırıldığında hızla çıkılması vurgulanır (s. 5, 8). Kaynak çizgileri öznel seçer; temas toleransı, teyit ve kanalın ne zaman geçersiz olduğu sayısal değildir.

### C44 — Teyitli paralel kanalda kenardan kenara dönüş

- **Bizim yapı:** H1'de 2 sol/2 sağ teyitli pivotlarla son iki yükselen dip veya alçalan tepe; kaynak s. 3'teki paralelliği sağlamak için diğer sınır bu iki pivot arasındaki karşı pivot ekstreminden paralel çizilir. `width>2 ATR14_H1`, çizgi en az bir kez karşı tarafta temas görmüş ve onaydan sonra fiyat kanal içinde kalmış olmalı. Kanal yalnız ikinci pivotun sağ iki barı tamamlandıktan sonra kullanılabilir. Geometri FC44 ile aynı sabitlenmiş çizgi algoritmasıdır; fark giriş ve çıkıştadır.
- **Olay/icra:** Yükselen kanalda `low[t]≤L(t)+0.1 width` ve `close[t]>L(t)+0.1 width` ile alt kenar reddi; düşen kanalda `high[t]≥U(t)−0.1 width`, `close[t]<U(t)−0.1 width`. H1 kapanışından sonraki ilk uygulanabilir 1m giriş; orta bantta yeni giriş yok. Stop long `L(t)−0.1 ATR14`, short `U(t)+0.1 ATR`; hedef karşı kenar çizgisinin t anındaki seviyesi. H1 kanal dışı kapanışında sonraki 1m'de çık; 30 H1 bar süre. Dokunma toleransı, ATR tamponu ve süre bizimdir.
- **Karşılaştırma:** FC44 ile aynı kanal tespitinde eşit işlem maliyeti/riskle C44 tek girişini ve FC44 kademeli girişini kıyasla. Yatay kanal için eğim `|slope|≤0.05 ATR/bar` ayrı kol; s. 4 yatay kanal örneği vardır ama bu eşik bizimdir.

## 3. Erich Senft — RSI: Traderin Gizli Silahı

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 11/Baskı 11/RSI - Traderin Gizli Silahı - Erich Senft (15 sayfa) - @eseckal.pdf>) · [Tam metin](03_rsi_senft.txt) · [123 başarısızlık salınımı s. 14](rsi_p14.png)

**Kaynak:** RSI14 ve 70/30 tercih edilir; 9 ile 25 periyot hassasiyet seçenekleri anlatılır (s. 6). Aşırı alım/satım **tek başına** ters işlem değildir; uzun süre bu bölgelerde kalabilir (s. 6–7, 12–13). RSI trend çizgisi fiyat direnciyle birlikte sınanır (s. 7–9), fakat çizgi manuel çizildiği için algoritmikleştirme gerekir. En belirgin formasyon, RSI'da 1 tepe, geri çekilen 2 dip, 1'i aşamayan 3 tepe ve 2 altına kırılım; yazar bunun ardından **fiyatın mevcut dip altına inmesini bekleyerek** short önerir (s. 13–14). Long tersidir. RSI'yi fiyatın yerine geçen bağımsız sinyal değil, fiyat hareketi onayı olarak kullanır (s. 5, 15). S. 10'daki “yön değişikliği neredeyse garantidir” ifadesi desteklenmiş performans ölçümü değildir.

### RS44 — RSI 1–2–3 başarısızlık salınımı + fiyat dip kırılımı

- **Bizim formasyon makinesi:** H1 Wilder RSI14; başlangıç short için RSI kapanışta `>70`. Sonrasında 2 sol/2 sağ barla **teyit edilmiş** RSI pivot tepe `R1>70`, sonra teyitli RSI dip `R2`, sonra teyitli tepe `R3<R1` ve `R3>R2` gelsin. Formasyon sırası indekslerle sabit; `R1` ile `R3` arası en çok 30 H1 bar. `R3` ancak sağ iki bar kapanınca bilinir. Long için RSI `<30`, dip1, tepe2, dip3>dip1. Bu pivot/pencere tanımı bizim objektifleştirmemizdir.
- **İki aşamalı sinyal:** Short için `R3` teyidinden sonra ilk `RSI[t]<R2` kapanışında RSI teyidi. O ana kadar bilinen son 10 H1 barın en düşük fiyatı `P` olarak sabitle. Sonraki en çok 3 H1 bar içinde `close<P` olursa short; long tersinde RSI `>R2`, fiyat bilinen son 10 barın tepesini aşmalı. Giriş ancak fiyat kırılımı H1 kapanışından sonraki 1m'de. RSI ve fiyatın aynı kapanışta birlikte kırılmasına izin ver; bu durumda P yalnız `t−1` öncesinden hesaplanır. Fiyat tetik yoksa kurulum biter.
- **Risk/çıkış:** Short stop `R3` pivot teyidine kadar oluşmuş fiyat tepesinin `+0.1 ATR14_H1` üstü; long simetrik. 2R hedef ve 24 H1 bar süre; ters RSI50 kapanışı ayrı erken çıkış kolu. Stop/süre ve RSI50 çıkışı **bizim**; kaynak yalnız fiyat dip kırılımıyla girişi verir.
- **Karşılaştırma:** RSI 70/30 tek başına, RSI 2 çizgisi kırılımı tek başına, RSI+fiyat çift teyidi; mevcut RSI divergence adaylarıyla olay örtüşmesi. Sağ bar pivot teyidi ve fiyat seviyesinin sinyalden önce sabitlenmesi lookahead'i önler.

## Ortak test notu

Tüm adaylarda yalnız tamamlanmış H1/1m verisi, point-in-time varlık evreni, ücret/spread/kayma/funding, aynı bardaki stop-hedef için kötümser sıra ve zaman sıralı dış örneklem gerekir. Öncelik FC44/C44 kanal seçiminin ileri bilgi kullanmaması, RS44'te pivot gecikmesinin doğru uygulanmasıdır. Kârlılık henüz doğrulanmadı.
