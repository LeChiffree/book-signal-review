# Kitap okuma 037 — kırılım, bölge seçimi, yanlış kırılım

**Kapsam:** 32 + 13 + 14 = **59 PDF sayfası**. Her PDF sayfa sıralı metne çıkarıldı ve tamamı incelendi; grafik ağırlıklı konsolidasyon s. 9–10 ile destek/direnç s. 9 ayrıca görsel kontrol edildi. Atıflar PDF sayfasıdır. Kriptoya ilişkin rakamsal sözleşmeler kaynak kuralı değil, **bizim test hipotezimizdir**. Backtest, paper test veya emir yok.

## 1. Mark K. White — Breakout Trading Stratejisi

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 17/Baskı 17/Breakout Trading Stratejisi - Mark K. White (32 sayfa) - @eseckal.pdf>) · [Tam metin](01_breakout_white.txt)

**Kaynak:** Destek/direnç kırılımından hemen giriş veya kırılan düzeyin karşı taraftan tekrar testini bekleme; ikincisi hareketi kaçırabilir (s. 3–7). Devam kırılımında trend yönünde dar konsolidasyon ve devam mumu, stop karşı sınırda (s. 9–10). Dönüş kırılımında önemli üst zaman dilimi düzeyi ve ters yönde mum fikri var (s. 10–11). Fitille anlık taşmayı kesin kırılım saymama, uzun gövde/kısa fitil ve düzey ötesinde kalma (s. 13–14); başarısız kırılımda eski düzeye dönüş ve retest sonrası karşı yönde işlem (s. 15–18). S. 25–29 Fibonacci, s. 30–32 piyasa yapısı üzerine ek bölümlerdir; s. 32 önemli salınımı yaklaşık %50 geri çekilme veya günlük ortalama aralıktan büyük tepkiyle ayırmayı önerir. Metin tercümesi yer yer bozuk, kesin lookback ve süre yok; kârlılık ifadeleri kanıt değildir.

### W37 — Kırılımda hemen giriş ile retest girişinin aynı olayda karşılaştırılması

- **Bizim D1 olay:** `t` kapanmadan önce bilinen 20 D1 barın en yüksek/high veya en düşük/low sınırı `U,L`. Son 20 D1 aralığı `<=4 ATR14[t−1]`, önceki 60 gün EMA20 eğimi kırılım yönünde olsun. `close[t]>U+0.1 ATR14[t−1]` long, short simetrik. Gövde toplam mum aralığının en az %60'ı ve kapanış yönlü son %20'dedir. Bunlar kaynağın rakamları değildir.
- **İki icra kolu:** A, kırılım kapanışından sonraki ilk uygulanabilir 1m fiyatı; B, sonraki 5 tamamlanmış D1 içinde ilk `low<=U+0.1 ATR` ve `close>U` retest kapanışından sonraki ilk 1m fiyatı. B kolunda retest yoksa işlem yok; A kolu için sonradan retest varlığına göre filtreleme yasak. Stop long `U−0.2 ATR`, short simetrik; stop girişin doğru tarafında ve maliyetin iki katından uzak olmalı. 2R hedef veya 10 D1 bar çıkış. Sabit eşikler, stop tamponu ve zaman sınırı bizim hipotezimizdir.
- **Eşdeğerlik:** Batch034 N34, batch036 C36 ve önceki breakout/retest aileleriyle aynı olay kimlikleri üzerinde kıyasla. Bu kaynak bağımsız alfa yerine **icra zamanlaması** sorusunu daha açık kuruyor.

## 2. Chris Padgett — Destek ve Direnç Seviyelerinin Tespiti

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 6/Baskı 6/Destek ve Direnç Seviyelerinin Tespiti (13 sayfa) - @eseckal.pdf>) · [Tam metin](02_support_resistance_detection.txt) · [Grafik s. 9](sr_p9.png)

**Kaynak:** Düzey tek fiyat değil **bölge**; tekrar tepki, geçmiş uç, kırıldıktan sonra karşı rol ve bölgeden uzaklaşma büyüklüğü seçimi etkiler (s. 4–5). Yazar seviyeyi fitil yerine mum **gövdesine** göre çizer (s. 6–7). Girişte az sayıda güçlü bölge, kâr alma için daha zayıf bölgeler de kabul edilebilir (s. 8–9). S. 9 görselinde fiyat direncin üstüne fitil atıp altında kapanır; güçlü düşüş/yutma mumu eşlik eder. H4 düzeyini H1 gövdelerinde inceltme örneği (s. 10–11). Temiz kırılımda gövde bölgeyi aşar, sonraki gövdeler aynı tarafta devam eder; karışık ileri geri geçişte retest ticareti uygun görülmez (s. 12–13). “Akıllı para/stop avı” yorumu gözlemlenmiş neden değildir; nesnel kural sayılmaz.

### P37 — Gövde bölgesi kalitesi ve temiz kırılım filtresi

- **Bizim H4/H1 düzey:** Son 80 tamamlanmış H4 mumda en az iki teyitli pivot high veya low (3 sol, 3 sağ bar) ve bunların gövde uçları `0.25 ATR14_H4` bandında olsun. Pivot ancak sağındaki 3 mum kapandıktan sonra bilinir. Düzey = bu gövde uçlarının medyanı; bölge `±0.25 ATR`. Tekrarlı temaslar en az 4 H4 bar aralıklı; aynı düzeye yakın adaylar tek kümeye birleştirilir. H1 inceltmesi ayrı varyanttır ve yalnız tamamlanmış H1 barları kullanır. Bu algoritma kaynağın öznel çizimini **bizim** nesnelleştirmemizdir.
- **Retest filtresi:** Long için ilk H4 gövde kapanışı bölge üstünde, ardından ikinci H4 gövde de üstte ve önceki H4 gövdesi bölgeyi iki yönlü kesmemiş olsun. Sonraki 8 H4 içinde ilk `low<=zone_upper` ve `close>zone_upper` retest; takip eden ilk 1m giriş. Stop `zone_lower−0.1 ATR`; hedef 2R veya önceki bilinen direnç (en az 2R varsa ayrı kol); 20 H4 bar zaman çıkışı. Short simetrik. Temiz kırılım koşulunun faydası ve kaçırdığı sinyaller filtresiz retest tabanına karşı ölçülür.
- **Sınır:** Bölgeyi sinyal sonrası pivotlardan kurma veya düzeyi sonradan “ayarlama” yasak. Giriş ve kâr düzeyleri için farklı önem derecesi yararlı araştırma fikri, fakat tek başına al/sat sinyali değil.

## 3. Duane Shepherd — Forex Piyasasında Konsolidasyon Breakout Sinyalleri

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 7/Baskı 7/Forex Piyasasında Konsolidasyon Breakout Sinyalleri (14 sayfa) - @eseckal.pdf>) · [Tam metin](03_consolidation_breakout.txt) · [Yanlış kırılım grafiği s. 9](consolidation_p9.png) · [ABC grafiği s. 10](consolidation_p10.png)

**Kaynak:** Kurulum ve tetik mumu birlikte güçlü olmalı (s. 1). Normal konsolidasyonda günlük tek güçlü mum veya sınırın kırılma öncesi testi (s. 2–4); orta konsolidasyonda tek mum, U dönüşü retest, küçük yeni kutu ve yanlış kırılım (s. 5–9). S. 7 zayıf ilk çıkıştan sonra sınıra dönüş ve güçlü ikinci çıkışı anlatır. Yanlış kırılımda fiyat kısa süre dışarı taşıp kutuya döner; **mum gövdesinin en az %70'i sınırın içinde** olmalı (s. 9–10); s. 9–10 grafikleri bu sekansı gösterir. Büyük kutu ve haftalık/aylık düzeyle ilişki anlatılır (s. 10–13). Forex pip cinsinden kutu büyüklükleri kriptoya taşınamaz. S. 14'teki %95 başarı iddiasının test verisi/yöntemi yok, başarı beklentisi olarak alınmaz.

### S37 — %70 gövdeyle kutuya dönüşten ters yöne aday

- **Bizim D1 olay:** `U,L` son 20 **önceki tamamlanmış** D1 mumun high/low sınırları; `2<= (U−L)/ATR14[t−1] <=6`, her sınıra `0.2 ATR` yakın en az iki önceki dokunuş. Gün `t` için üst yanlış kırılım: `high[t]>U+0.1 ATR`, `close[t]<U`; gövdenin `[L,U]` içindeki kesişim uzunluğu `body_inside=max(0,min(max(open,close),U)−max(min(open,close),L))`; `body_inside/abs(close−open)>=0.70`. Sıfır gövdeli doji geçersiz. Alt sınır simetrik. Fitilin dışarı çıkması ve gövde dönüşü kaynak fikri; 20 bar, ATR, dokunuş ve doji dışlaması bizim kurallarımızdır.
- **Giriş/risk:** Üst yanlış kırılım mumunun kapanışından sonraki ilk 1m'de short; stop `high[t]+0.1 ATR`, hedef önce kutu orta çizgisi, sonra `L+0.2 ATR` ayrı kollar. Hedef net mesafesi en az 1.5R değilse işlem yok; 10 D1 bar sonra çık. Alt yanlış kırılım long simetrik. Mum kapanışından önce fitile göre giriş yok. Aynı olayda batch034/batch036 kırılım ve önceki false-break adaylarıyla net farkı ölç.
- **Ayrı fikir:** S. 7–8'deki zayıf ilk kırılım + retest + güçlü ikinci mum, aynı düzeyde iki aşamalı teyit varyantıdır; `güçlü` kesin tanımlanmadığı için ana sinyale karıştırılmadı. S. 10'daki ABC görseli de pivot onayı tanımlanmadan canlı sinyal sayılmaz.

## Test önceliği

**S37** kaynakta sayısal %70 eşiği taşıdığı için ilk karşılaştırma adayı. **P37** bölge seçimi ve temiz kırılım filtresi; **W37** aynı olayın iki giriş zamanlaması. Hepsi için point-in-time evren, kapanış sonrası uygulanabilir giriş, ücret/spread/kayma/funding, aynı bar stop-hedef sıralaması ve zaman sıralı dış örneklem gerekir. Görsel örnekler ve kaynakların başarı iddiaları kârlılık kanıtı değildir.
