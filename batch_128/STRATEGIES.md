# Kitap okuma 128 — tek güçlü mumun Fibonacci orta düzeyi

**Kapsam:** Üç ayrı PDF'nin **12 + 12 + 12 = 36 sayfası** baştan sona okundu. Atıflar PDF sayfasıdır. Backtest, paper test ve canlı emir yapılmadı. Daha önce okunan *Gerçek Destek ve Direnç* kitabının başka baskısı ayrı kitap olarak sayılmadı; bu partide onun yerine M. Jazuli İsmail'in farklı kitabı okundu.

## 1. Soulz — Arz ve Talep

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 6/Baskı 6/Arz ve Talep - Soulz (12 sayfa) - @eseckal.pdf>) · [Tam metin](01_soulz_supply_demand.txt)

**Tam okuma:** S. 1 kapak; s. 2 arz/talep iddiası; s. 3–4 DBR/RBR/RBD/DBD şemaları; s. 5 bölgeye iki dönüş örnekleri; s. 6–7 yutma mumu ve dengesizlik; s. 8–9 bölgeden alış/satış, alt zaman diliminde stop daraltma ve karşı seviyeye hedef; s. 10 sıkışma; s. 11 sahte kırılım; s. 12 HTF bağlamı. Büyük fonların bu bölgelerde gerçekten emir tuttuğu veya kalıbın kârlı olduğu gösterilmiyor. Bölge türleri ve ilk dönüş [PL55](../batch_055/STRATEGIES.md), yaklaşma sıkışması [FL58](../batch_058/STRATEGIES.md), HTF bölge + yutma/bos da önceki raporlarda mevcut. Kaynak bu birleşim için ayırıcı nesnel eşik veya çıkış kuralı eklemiyor. **Yeni bağımsız aday yok.**

## 2. Violeta Gaucan — Fibonacci Geri Çekilme Prensibi

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 5/Baskı 5/Fibonacci Geri Çekilme Prensibi (12 sayfa) - @eseckal.pdf>) · [Tam metin](02_fibonacci_principle.txt)

**Tam okuma:** S. 1 kapak; s. 2–4 sayı dizisi ve oranlar; s. 5–8 %23,6/%38,2/%50/%61,8 geri çekilme ve seçilmiş AUDUSD/EURUSD örnekleri; s. 8–10 yay/fan/saat/genişleme/kanal; s. 11–12 uç seçimi, geçmişte çalışan düzeyleri gözleme ve başka araçla teyit önerileri. Fiyatın Fibonacci düzeylerinde “mutlaka” döneceği iddiası veriye dayanmıyor. Özellikle grafik ölçeğine bağlı yay/fan geometrisi s. 9'da kabul ediliyor; fiyat–zaman birimleri sabitlenmeden mekanik sinyal olamaz. Geçmişte en iyi tepki veren düzeyi **sonradan** seçmek ileriye bilgi sızdırır. Standart geri çekilme ve uzatma aileleri önceki adaylarda var; yeni, tekrar üretilebilir giriş/stop/çıkış paketi sunulmadı. **Yeni bağımsız aday yok.**

## 3. M. Jazuli İsmail — Fibonacci Geri Çekilme ile Teknik Analiz

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 5/Baskı 5/Fibonacci Geri Çekilme ile Teknik Analiz - M. Jazuli İsmail (12 sayfa) - @eseckal.pdf>) · [Tam metin](03_ismail_fibonacci.txt) · [Görsel s. 1–4](ismail_contact_1.png) · [Görsel s. 5–8](ismail_contact_2.png) · [Görsel s. 9–12](ismail_contact_3.png)

**Tam okuma:** S. 1 genel iddialar; s. 2–3 Fibonacci'yi iki ayrı swing pivotu yerine **tek uzun mumun fitil dibinden tepesine** çizme ve önceki fitili aşmayan mumları eleme; s. 4 %50 bölgesine fitille dokunup reddetme, sonraki mum giriş; s. 5–6 bozuk çevrilmiş devam/dönüş örnekleri; s. 7 okunması zor 50→100, 161,8 ve 261,8 kademeleri; s. 8–10 kırma/reddetme, H4/H1 bağlamı; s. 11 D1 ilk trend mumu ve 423,6 örneği; s. 12 sonuç. S. 5–10'un metin katmanı hatalı ve tekrarlarla bozulmuş olduğu için **görsel 12 sayfanın tümü** ayrıca incelendi. Grafikler örnektir; “öncü, yeniden boyamaz” sözü tek başına garanti değildir: mum seçiminde gelecek barlar kullanılırsa görünüm yanlılığı doğar. Özel DS betiğinin kodu verilmez ve sözleşmeye alınmaz.

### JI128A — Önceki yüksek/düşüğü aşan tek H1 mumun %50 fitil reddi

- **Kaynak (PDF s. 2–4, 7–8, 11–12):** Fibonacci uçlarını tek güçlü mumun kendi `low/high` değerlerine sabitle; geri çekilmede orta düzeyin fitille dokunulup gövdeyle geri alınması sonrası sonraki mumda trend yönüne işlem; eski mum ucu ve uzatma düzeyleri hedef, ters ucu stop. Kaynak “güçlü mum”, trend ve kaç bar bekleme eşiğini vermediği için aşağıdaki değerler **bizim ön kayıtlı deney tanımımızdır**.
- **Kapalı mum sinyali:** EURUSD/GBPUSD/USDJPY, H1 sinyal, yalnız son **tamamlanmış** H4 trend filtresi. Boğa aday mumunda `close>open`, `high−low>=1,5 ATR14_H1` (ATR aday mumdan **önceki** 14 tamamlanmış bardan), `close>=low+0,8(high−low)` ve `close>high[t−1]`; H4 son kapanışı `EMA50_H4` üstünde. Mum kendi kapanışında dondurulur: `L=low[t]`, `H=high[t]`, `M=(L+H)/2`. Sonraki 1–8 tamamlanmış H1 bardan ilki `low<=M` ve `close>M` ve `close>open` şartlarını sağlıyorsa fitil reddidir; o bar kapanmadan işlem yok. Redden önce veya reddeden mumda `low<L` olursa aday iptal. Ayı yönü fiyat ve H4 ilişkilerinin tam simetriğidir. `1,5 ATR`, %80 kapanış, 8 bar, H4 EMA50 ve reddetme gövde rengi kaynakta sayılmamıştır; uygulanabilir hipotez parametreleridir.
- **Yürütme/risk/çıkış:** Ret mumundan sonraki ilk uygulanabilir M1 ask/bid'den giriş. Stop alışta `L−2 pip`, satışta `H+2 pip`; ilk risk özsermayenin `%0,5`i, tek açık işlem/çift. İlk hedef alışta `H`, satışta `L`; ilk hedefe ulaşınca pozisyonun %50'si çıkar. Kalanın hedefi tek mum boyunun `1,618` katı, alışta `L+1,618(H−L)`, satışta `H−1,618(H−L)`; 24 H1 bar içinde ne stop ne hedef olursa tam çıkış. İlk hedef girişin lehe tarafında değilse işlem açma. Gerçek spread, komisyon, kayma, haftasonu/likidite boşluğu ve aynı M1 bardaki belirsiz stop/hedef sırası hesaba katılır; belirsizlikte stop önce. Kaynağın 261,8 ve 423,6 uzatmaları ancak ayrı, önceden belirlenmiş duyarlılık kollarıdır; ana sonuç için geriye dönük en iyi düzey seçilmez.
- **Ayrışma:** Aynı tek mum olaylarında %50 reddi olmadan ilk geri çekilmede giriş, iki pivot arasındaki klasik Fibonacci ve [önceki Fibonacci geri çekilme adayı](../batch_127/STRATEGIES.md) aynı dönem/maliyet altında karşılaştırılır. Öncelikli soru, tek mumla belirlenen 50 düzeyinin genel orta nokta geri çekilmesinden net R bakımından ayrışıp ayrışmadığıdır. Aday barın H1 kapanışından önce çizilmiş gibi davranmak yasaktır.

## Sonuç

**1 yeni araştırma adayı:** JI128A. İlk iki kitap önceki strateji ailelerini tekrar ediyor.
