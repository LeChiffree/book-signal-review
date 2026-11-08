# Kitap okuma 006 — günlük reddedilme, dar aralık ve üç gösterge

**Kapsam:** Üç PDF'nin **123 + 42 + 13 = 178 PDF sayfası** metne çıkarılıp incelendi. Sayfa numaraları PDF sayfasıdır. Kuralların çoğu Forex, hisse veya opsiyon örneklerinden gelir. Aşağıdaki kripto günlük mum tanımları **test hipotezidir**; kaynakların kanıtlanmış getirisi değildir. İşlem/backtest yapılmadı.

## 1. Frank Ochoa — 5 Adımlı Swing Trading Planı

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 9/Baskı 9/5 Adımlı Swing Trading Planı - Swing Trade Pro 2.0 - Frank Ochoa (123 sayfa) - @eseckal.pdf>)

Yazar önce riski ve günlük bar türlerini, sonra bunların sıralarını anlatıyor (s. 2–45). S. 46–103'ün önemli kısmı opsiyon yapıları; opsiyon zinciri, kullanım fiyatı, vade, prim ve örtük oynaklık olmadan bunlar OHLCV üzerinde sınanamaz. S. 104–116 kademeli giriş/çıkış, s. 117–123 işlem günlüğü. Kitabın küçük hesaplar için verdiği yüksek risk oranları (s. 4–11) portföy kuralı olarak alınmıyor.

### F1 — Reddedilme gününün orta noktasına dönüş

- **Kaynak:** Boğa reddedilme günü önceki dip civarında; günlük aralık `>1.25 ×` son 10 günün ortalama aralığı, alt fitil gövdeden `>2.5 ×` büyük, kapanış aralığın üst `%35` diliminde. `(high+low)/2` orta noktası sonraki 1–4 gün savunulursa giriş alanı; altında günlük kapanış düzeni bozar (s. 12–17). Ayı yönü simetrik taslak olarak anılıyor (s. 13).
- **Test tanımı:** ADR10 yalnız `t-1`e kadar kapanmış 10 günden; olay `t` kapandığında oluşur. Önceki dip koşulu: `low[t] <= min(low[t-10:t-1])` (**bizim** nesnel tarifimiz). `t+1...t+4` içinde orta noktaya ilk temas için limit uzun emir; emir yalnız olaydan sonra geçerli. Dolmayan emir `unfilled`. Stop `low[t]-0.1×ATR14[t-1]`; orta nokta altında günlük kapanış veya 2R/3R, ayrıca 3/7/14 gün çıkış varyantı. `0.1 ATR` tamponu ve çıkış ufukları bizim tercihimiz.
- **Ayrım:** S. 18–21'deki *failed new low* (`low[t]<low[t-1]`, ideal `close[t]>(high[t-1]+low[t-1])/2`) ve s. 22–25'teki boğa *outside day* (`high[t]>high[t-1]`, `low[t]<low[t-1]`, `close[t]>high[t-1]`, aralık `>1.05 ADR`) F1'in ayrı alt grupları olarak etiketlenecek. Aynı bar üç strateji/üç bağımsız kanıt sayılmayacak. Gün içi giriş önerileri günlük kapanışa dayalı testte kullanılmayacak.

### F2 — Emilim başarısızlığı sonrası kısa yön

- **Kaynak:** Reddedilme sonrası orta nokta çevresinde 2–5 günlük emilim ve sonra reddedilme gününün orta noktası altında günlük kapanış, uzunların çözülmesi fikri (s. 28–42).
- **Test tanımı:** F1 olayının ardından 2–5 kapalı günlük mumun her birinde aralık/orta nokta teması ve `close>=mid`; sonra ilk `close<mid` olayında kısa sinyal. Sonraki ilk yürütülebilir 1m'de giriş; stop emilim günlerinin en yükseği `+0.1 ATR`, çıkış reddedilme gününün dibi/2R veya 3/7/14 gün. “Emilim” için temas sayısı ve stop tamponu bizim nesnelleştirmemiz; kaynakta tam kod tarifi yok. F1 ile aynı kurulum kimliğine bağlanacak; F1 kaybının ardından F2 kazancını bağımsız fırsat gibi saymayacağız.
- **İkincil fikir:** S. 26–27'de `>2 ADR`, önceki yüksek üstü ve aralığın üst `%10–15`inde kapanan *stop run* günü var. F1/F2 sonrası devam alt grubu olarak kaydedilecek; güçlü tek günlük hareketin ardından olası geri çekilme nedeniyle bağımsız giriş değil, önce gözlem etiketi.

**Yürütme notu:** S. 104–116'daki 1×3/1×2 kademeli giriş ve 11/111/211 kademeli çıkış yalnız **aynı sinyalin yürütme karşılaştırması** olarak denenebilir; daha çok giriş sinyali üretmez. Günlükte kurulum, zaman, giriş, stop, dolum, ücret/funding, MAE/MFE, çıkış ve net R saklanmalı (s. 117–123).

## 2. Roman Sadowski — 9 Kazançlı Trading Stratejisi

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 9/Baskı 9/9 Kazançlı Trading Stratejisi - Roman Sadowski (42 sayfa) - @eseckal.pdf>)

Derleme; COT + stochastic (s. 5–7), MA20/60/100 (s. 8–11), Heikin-Ashi + stochastic (s. 11–18), dar aralık/kırılım (s. 22–24, 35–38), mum formasyonları (s. 25–29), kırılan seviyenin retesti (s. 29–34) ve RSI2 (s. 39–40) anlatıyor. COT verisi mevcut OHLCV'de yok. Yutan/çekiç mumlar önceki C1/C2; rol değişimi batch 005 S2/O1; Bollinger sıkışması ve aralık kırılımı önceki G2/V2 ailesiyle karşılaştırılmalı. Forex'teki sabit pip eşikleri kriptoya doğrudan aktarılamaz. Verilen örnekler performans istatistiği değildir.

### N1 — NR4/NR7 dar günlük mumun kırılımı

- **Kaynak:** Gün aralığı son 4 ya da 7 günün en darsa o günün yüksek/düşük sınırından kırılım; karşı sınır stop (s. 36–38).
- **Test tanımı:** `range[t]=high[t]-low[t]`; `range[t] < min(range[t-n+1:t-1])`, `n∈{4,7}`. Eşitlikte sinyal yok (bizim bağ kararı). `t` kapanışında iki yönlü OCO stop girişleri sınırda dondurulur; yalnız `t+1` günü geçerli. Aynı 1m barda iki sınır tetiklenirse bar sırası bilinmiyorsa muhafazakâr başarısız/dışlanan olay olarak raporlanır. Dolumda karşı sınır stop; 1R/2R veya 3/7/14 gün çıkış. NR7 çoğu zaman NR4'ün alt kümesi; ayrı işlem sayılmaz, `n` parametresi karşılaştırılır.
- **Kontrol:** Yalın günlük kırılım ve dar aralık dışı günler; maliyet sonrası net R ile farkına bak.

### N2 — İki renk değişimli Heikin-Ashi dönüşü

- **Kaynak:** S. 14'te iki yeşil HA mumundan sonra iki kırmızı kısa; iki kırmızıdan sonra iki yeşil uzun şeklinde anlatılıyor. **S. 15'in long/short ve stochastic >70/<30 eşleşmesi bununla çelişiyor.** Bu nedenle s. 15 filtresi kaynak kuralı olarak otomatikleştirilemez. S. 16'daki Accelerator Oscillator için yeniden boyanma uyarısı da var.
- **Test tanımı:** HA serisi yalnız `t` kapanmış gerçek OHLC'den nedensel hesaplanır; önceki iki HA rengi ters ve son iki renk aynı yeni yön olduğunda sinyal. Giriş/stop/çıkış **gerçek fiyat** OHLC/1m üzerinden; HA fiyatını gerçekleşebilir fill sayma. Stochastic(14,7,3) filtreli sürüm, yön eşlemesi baştan sabitlenirse ayrıca duyarlılık testi. Baz `iki renk` ile filtresini ayrı raporla. Bu adayın yönü s. 14'e dayanır; s. 15 belirsizliği dosyada korunur.

### N3 — RSI(2) aşırılığı yönünde devam

- **Kaynak:** `RSI(2)>90` alım, `<10` satım; karşı sinyalde çıkış (s. 39–40). Bu, önceki RSI aşırı satım/alım dönüş fikirlerinin **ters hipotezi**.
- **Test tanımı:** Kapanmış günlük RSI(2) eşiğinde ilk olay, sonraki ilk 1m'de giriş. Karşı sinyalde çıkış; ayrıca 3/7/14 gün sabit ufuk ve `1.5 ATR14` ilk stop (stop bizim risk tanımı). Aynı yönde üst üste aşırılıkta yeni pozisyon açma. Momentum yönü ile karşı yönde mean-reversion aynı olay seti ve maliyetlerle karşılaştırılmalı.

**Düşük öncelik:** MA20/60 kesişimi ve MA100 trend filtresi (s. 8–11) kaynakta açık, ama önceki hareketli ortalama adaylarıyla örtüşür; mevcut MA özelliklerinde ek parametre varyantı. BB(20,2) sıkışmasının `0.0100` bant eşiği (s. 35–36) Forex ölçeğine bağlı; ancak normalize bandwidth yüzdelik dilimi olarak bizim adaptasyonumuzla denenebilir, yeni bağımsız strateji diye sayılmaz.

## 3. TMP — RSI Swing Trading Stratejisi

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 9/Baskı 9/RSI Swing Trading Stratejisi - TMP (13 sayfa) - @eseckal.pdf>)

Metin MA20, RSI20 ve CMF20 kullanıyor (s. 3–7). Uzun kurulum: fiyat aynı mumda MA20 üstüne kırıp üzerinde kapanır (s. 8–9), önceki RSI salınımına **elle çizilen trend çizgisi** kırılır (s. 9–10), CMF20 sıfır üstüne çıkar (s. 11), stop MA20 altı ve CMF sıfır altına inince çıkış (s. 12). Tam özgün RSI trend çizgisinin pivot/çizgi seçim kuralı sayısal değil; kodlanmış özgün strateji iddiasında bulunmayacağız. S. 13'teki tek 385-pip örneği başarı kanıtı değil. Kitap kısa yön için tam simetrik plan vermiyor.

### T1 — MA20 kırılımı + CMF20 onayı; RSI teyidi ayrı adaptasyon

- **Temel aday:** `close[t-1]<=SMA20[t-1]` ve `close[t]>SMA20[t]` ile MA olayı. O anda `CMF20[t]>0` ise sinyal; değilse sonraki en fazla üç kapalı günde ilk `CMF20>0` olayı. `3 gün` bekleme sınırı bizim seçimi. Long yalnız sonraki ilk 1m'de. `CMF20 = sum(((2C-H-L)/(H-L))*V,20)/sum(V,20)`; `H=L` olan barda para akışı çarpanı 0. Hacim türü kaynak veri sözleşmesinde sabitlenmeli.
- **RSI adaptasyonu:** Kaynağın öznel trend çizgisi yerine ayrı sürümde `RSI20[t] > max(RSI20[t-5:t-1])` iste; beş gün bizim yaklaşımımız. Önce MA+CMF bazını, sonra RSI filtresinin marjinal katkısını karşılaştır. RSI koşulu sağlanmazsa özgün çizgiye göre karar bilinmiyor diye kaydet.
- **Risk/çıkış:** Giriş anındaki MA20'nin `0.1 ATR` altı başlangıç stopu (**tampon bizim**); `CMF20<0` günlük kapanışında veya günlük `close<MA20` varyantında sonraki ilk 1m çıkış. Ayrıca 3/7/14 gün ufuk. Stopu her gün geriye dönük yükseltme; dinamik MA stopu ayrı test.

## Ortak test ve öncelik kaydı

1. **Öncelik:** N1 (dar mum kırılımı) ve F1 (reddedilme/orta nokta), ardından T1; F2 ve N3 ayrı hipotez, N2 kaynak çelişkisi nedeniyle düşük öncelik. Aynı gün ve aynı yönde oluşan adaylar tek olay kimliğinde çakışma etiketleriyle izlenecek.
2. **Nedensellik:** Özellikler UTC kapanmış 1d OHLCV üzerinden; `t` günündeki olay `t` kapanışından önce işleme giremez. Giriş/limit/stop dolumları sonraki 1m sırasıyla, spread, komisyon, kayma ve funding dahil. Emir süresi, dolmayan emirler ve aynı dakikada sınır çatışması sayılmalı. Eğitim/dış örneklem ve rejim ayrımı önceden dondurulmalı.
3. **Değerlendirme:** Tekil sinyal getirisi yanında eşzamanlı pozisyon sınırı, portföy riski, net R, güven aralığı, örnek sayısı, parametre duyarlılığı, BTC yön/volatilite rejimi raporlanmalı. Çoklu denemeyi hesaba katmadan “işe yarıyor” hükmü verilmeyecek.
4. **Durum:** Bu dosya strateji adaylarını ve kaynak bağlarını kaydeder. **Backtest veya paper test yapılmadı; canlı emir verilmedi.**
