# Kitap okuma 127 — M1 osilatör scalp, Fibonacci kademeleri, iç içe geri çekilme

**Kapsam:** Üç ayrı PDF'nin 6 + 8 + 8 = **22 PDF sayfası** baştan sona okundu. Kaynak atıfları PDF sayfasıdır. Backtest, paper test ve emir yapılmadı. Aşağıdaki sayısal varsayımlar kaynakta bulunmadığında açıkça **deney tasarımı** olarak işaretlendi.

## 1. M1/M5 Forex Scalping Strategy

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 7/Baskı 7/M1-M5 Forex Scalping Stratejisi (6 sayfa) - @eseckal.pdf>) · [Tam metin](01_m1_m5_scalping.txt)

**Tam okuma:** S. 1 kapak; s. 2–3 MACD yön yorumu; s. 4 stokastik 80/20 ve EURUSD/GBPUSD M1 ayarları; s. 5 alış/satış, stop ve M1/M5 hedefleri; s. 6 tek başarılı örnek ve reklam. S. 6'daki tek işlem ve “güçlü sistem” ifadesi performans kanıtı değildir. 4 pip stopta spread ve kayma kritik olabilir.

### MS127A — MACD sıfır yönünde stokastik 20/80 geri geçişi

- **Kaynak (PDF s. 4–6):** M1'de MACD(12,26,9) sıfırın üstündeyken yavaş stokastik(8,3,3) 20'yi aşağıdan yukarı geçerse alış; MACD sıfırın altındayken stokastik 80'i yukarıdan aşağı geçerse satış. En yakın destek/direncin 1 pip dışına stop, M1 için 15 pip ilk hedef. M5 için kaynak 25 pip hedef verir; bu adayın ana kolu M1'dir.
- **Kapalı mum sözleşmesi:** EURUSD ve GBPUSD, M1 OHLC; `MACD=EMA12(close)−EMA26(close)` ve `signal=EMA9(MACD)`, filtre olarak **MACD çizgisi** kullanılır; yavaş stokastik `fastK=100×(close−LL8)/(HH8−LL8)`, `slowK=SMA3(fastK)`, `D=SMA3(slowK)`; `HH8=LL8` ise o bar işlem yok. Alış için önceki tamamlanmış barda `slowK<=20`, güncel kapanmış barda `slowK>20`, güncel `MACD>0`. Satışta `slowK>=80` sonra `<80` ve `MACD<0`. `D` kesişimi **aranmaz**; kaynak yalnız stokastik eşik geçişini anlatır. Güncel mum tamamen kapanmadan sinyal yok. Önceki 20 tamamlanmış M1 barındaki en düşük seviye alış için destek, en yüksek satış için dirençtir; stop bunun 1 pip dışındadır. 20 barlık pencere **bizim** nesnelleştirmemizdir.
- **Yürütme/çıkış:** Sinyal barından sonraki ilk uygulanabilir M1 ask/bid kotasyonuyla giriş; sabit 15 pip hedef, stop, en geç 60 M1 bar süresi. Stop yönü yanlışsa veya maliyet dahil stop uzaklığı `<=0` ise pas. İşlem başına başlangıç riski özsermayenin `%0,25`i, bir açık pozisyon/çift; gerçek spread, komisyon, kayma, haber saatlerindeki fiyat boşluğu dahil. Aynı M1 içinde stop ve hedefe temas varsa alt zaman damgalı kotasyon yoksa stop önce varsayılır. Ayrı ön kayıtlı kol M5 sinyal/25 pip hedefi aynı kurallarla dener; M5 sinyalinin M1 giriş verisiyle ileriye dönük birleşimi gerekir. MACD sıfır filtresiz ve stokastik eşiği ters yönde geçen kollarla, ayrıca [önceki MACD/stokastik adayları](../batch_002/STRATEGIES.md) ile aynı veri/maliyet altında net R, işlem sıklığı ve yıl bazında istikrar karşılaştırılır.

## 2. Chris Padgett — Fibonacci Geri Çekilme Stratejisi

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 7/Baskı 7/Fibonacci  Geri Çekilme Stratejisi (8 sayfa) - @eseckal.pdf>) · [Tam metin](02_fibonacci_retracement.txt)

**Tam okuma:** S. 1 kapak; s. 2–3 %61,8 geri çekilme, stokastik(5,3,3) ve 127,2/161,8 uzatma ayarları; s. 4–5 boğa örneği, yutan mum, 3–5 pip stop ve kademeli kâr; s. 6–7 ayı simetriği; s. 8 son işlemin hedefe tam ulaşmadığı ve stokastik aşırı bölgenin sinyalden **önce** görülmesinin kabul edildiği notu. S. 2 “RSI” derken aynı sayfa ve örnekler stokastik kullanır; sözleşmede örnekte kullanılan stokastik esas alınır. “Tatlı nokta” ve “önemli salınım” sayısal tanımsızdır.

### CP127B — %61,8 geri çekilmede stokastik ve yutan mum, üç kademeli çıkış

- **Kaynak (PDF s. 2, 4–8):** Genişleme salınımının yaklaşık %61,8 geri çekilmesi, yakın stokastik aşırı satım/alım ve yönüne uygun yutan mum; geri çekilme ekstreminden 3–5 pip stop; eski tepe/dipte %50, 127,2 uzatmada kalan yarının %50'si, 161,8'de son kısım.
- **Kapalı mum sözleşmesi:** EURUSD/GBPUSD H1. `k=2` iki sağ bar kapanınca kesinleşen H1 pivotları. Alış için son kesinleşmiş pivot dip `L` ve onu izleyen kesinleşmiş pivot tepe `H`, `A=H−L>1 ATR14_H1`; başka yeni yüksek pivot oluşmadan geri çekilme. `Z=H−0,618A`, izinli temas `[H−0,686A,H−0,550A]`; bu bant **bizim** “tatlı nokta” nesnelleştirmemizdir. Temas barı veya önceki üç **tamamlanmış** H1 barın en az birinde yavaş stokastik(5,3,3) `%K<20`; temas sonrası en çok dört H1 içinde boğa yutma: önceki gövde kırmızı, mevcut gövde yeşil, `open_t<=close_(t−1)` ve `close_t>=open_(t−1)`. Yutma barı kapanınca sonraki ilk uygulanabilir M1 ask ile giriş. Ayı yönü tüm fiyat ilişkileri ve stokastik `>80` simetriği. `k`, ATR eşiği, bant genişliği ve zaman pencereleri deney tasarımıdır; kaynak bunları vermez. Geçmişe dönük pivot yerleştirilemez.
- **Risk/çıkış:** Stop geri çekilmede **sinyal anına kadar gözlenen** en düşük seviyenin 4 pip altı; satışta en yüksek seviyenin 4 pip üstü. Başlangıç riski özsermayenin `%0,5`i, tek pozisyon/çift. `H` veya `L` eski ekstreminde miktarın %50'sini kapat; giriş yönünde `L+1,272A` (alış) / `H−1,272A` (satış) düzeyinde **kalan miktarın %50'sini** kapat; `L+1,618A` / `H−1,618A` düzeyinde son kısmı kapat. İlk kârda kalan stopu ancak masraf dahil gerçek başabaşa taşımayı ayrı kol olarak ölç; ana kolda kaynak önerisini uygula. 72 H1 sonra kalan tüm pozisyonu kapat. Her hedef girişin lehe tarafında sıralı değilse işlem yok. Spread, komisyon, kayma, boşluk ve aynı M1 bardaki seviye sırası kötümser ele alınır. %61,8 filtresiz ve stokastik filtresiz kollar, önceki [Fibonacci adayları](../batch_113/STRATEGIES.md) ile aynı veri/maliyet altında karşılaştırılır.

## 3. Gabriel Ríos — Order Block ve Kullanımı

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 6/Baskı 6/Order Block - Gabriel Rios (8 sayfa) - @eseckal.pdf>) · [Tam metin](03_rios_order_block.txt) · [Görsel sayfalar 1–4](rios_contact_1.png) · [Görsel sayfalar 5–8](rios_contact_2.png)

**Tam okuma:** S. 1 kapak; s. 2–3 H1 büyük mum, eski yüksek/düşüğün alınmaması, TDI ayrışması ve %61,8–78,6 geri çekilme; s. 4–5 H1 Fibonacci salınımı ve M15 iç yapı; s. 6–7 H1 “tatlı nokta” içinde M15 ikinci dar bölge, dar veya geniş stop seçimi; s. 8 bitiş. Grafikler de incelendi. Metin H1/M15 iç içe geri çekilmeyi ayırıcı kural olarak sunar fakat “order block”u nesnel tanımlamaz; aşağıdaki sözleşme bunu **yalnız iç içe Fibonacci alanı** olarak test eder. TDI ayarları/büyük mum eşiği verilmediğinden TDI tek başına test kuralına dönüştürülmez. Kurum emirleri grafikten doğrulanamaz.

### GR127C — H1 %61,8–78,6 alanı içinde M15 iç geri çekilme

- **Kaynak (PDF s. 3–7):** H1'de %61,8–78,6 Fibonacci bandına çekilme; M15'e inip aynı yönde küçük salınımın %61,8–78,6 bandının H1 bandının içine yerleşmesini bekleyerek dar giriş alanı ve stop oluşturma. Kaynaktaki TDI ayrışması bilgi eksikliği nedeniyle **bu mekanik alt kümeye dahil edilmedi**; dolayısıyla aday kitabın tüm önerisi değildir.
- **Kapalı mum sözleşmesi:** EURUSD/GBPUSD H1 ana, M15 alt, M1 yürütme. İki sağ barla kesinleşmiş H1 `L→H` yukarı salınımı, `A=H−L>=1 ATR14_H1`. H1 alış alanı `[H−0,786A,H−0,618A]`; düzeyler ancak `H` pivotu kesinleştikten sonra etkin. Fiyat ilk kez bu alana girdikten sonra M15 üzerinde yalnız o ana dek iki sağ barla **teyit edilmiş** mini `l→h` yükseliş salınımını ara: `l` H1 alış alanı içinde, `h>l`, `h−l>=0,25 ATR14_H1`. Mini alış alanı `[h−0,786(h−l),h−0,618(h−l)]` bütünüyle H1 bandının içinde olmalı. Mini bant H1 bandına ilk girişten sonra en çok 24 M15 barda tespit edilir. İzleyen en çok 16 M15 barda mini banda ilk yeniden dokunuşta, dokunma mumu **bandın üst sınırının üstünde kapandıysa**, sonraki ilk uygulanabilir M1 ask'tan long. Short H1/M15 salınım ve fiyat ilişkilerinin simetriği. Pivot `k=2`, salınım boyutu, pencereler, kapanış teyidi ve iç içe bant şartının tam uygulaması **bizim** deney tasarımıdır.
- **Risk/çıkış:** Stop mini salınımın `l` dibinin `2 pip` altında; ancak H1 bandının alt sınırından yukarıdaysa geniş stop koluyla ayrıca karşılaştır. Hedef H1 `H`, sonra `L+1,272A`; ana kolda `H` düzeyinde %50 ve uzatmada kalan miktar çıkış. 48 H1 sonra süre çıkışı. İlk risk özsermayenin `%0,5`i, tek açık pozisyon/çift. Hedefler maliyet ve girişten sonra doğru sıralı değilse pas. Gerçek spread, komisyon, kayma, boşluk ve kötümser aynı M1 bar sırası dahil. Yalnız H1 alanıyla giriş kolu ve önceki [order block/Fibonacci adayları](../batch_058/STRATEGIES.md) ile aynı tarih/veri/maliyet altında karşılaştır; hipotez M15 iç bandının maliyet sonrası net R'yi iyileştirip iyileştirmediğidir.

## Sonuç

**3 yeni araştırma adayı:** MS127A, CP127B, GR127C. Üçü de maliyet ve uygulama doğrulaması bekliyor; kaynak örneklerinden kazanç çıkarımı yapılmadı.
