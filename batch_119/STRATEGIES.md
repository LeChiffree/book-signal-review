# Kitap okuma 119 — yuvarlak fiyat ve önceki hafta sınırının ilk teması

**Kapsam:** Üç ayrı PDF'nin **49 + 69 + 61 = 179 sayfası** baştan sona okundu. Atıflar PDF sayfasıdır. Backtest, paper test veya emir yapılmadı.

## 1. Forex Systems Research Company — Teknik Analiz Kursu

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 2/Baskı 2/Forex Systems Research Company Teknik Analiz Kursu (49 sayfa) - @eseckal.pdf>) · [Tam metin](01_forex_systems_research.txt)

**Tam okuma:** S. 1–8 piyasa ve işlem altyapısı; s. 9–20 doji, yutan, cımbız, yıldız, çekiç ve direnç/destek reddi mumları; s. 21–31 baş-omuz, takoz, 1-2-3, çift tepe/dip, trend çizgisi ve kanal; s. 32–42 dikdörtgen, üçgen, bayrak ve flama devamları; s. 43–44 sahte kırılım; s. 45–49 trend içi geri çekilme, kırılım mumuyla giriş, pivot stop ve Fibonacci hedefleri. S. 45–46'da sinyal barı oluşurken o barın high/low'unun üzerinde/altında emir tarifi vardır; bu ancak önceden belirlenen pivot mumuna göre sonraki barın kırılması şeklinde modellenebilir. Pivotun algoritmik teyidi, trendin ölçüsü ve çıkış seçeneklerinin önceliği verilmez. Çekirdekler daha önceki mum, SFP, kanal, pivot ve geri çekilme aileleriyle örtüşür. **Yeni bağımsız aday yok.** S. 4'teki “forex her zaman likit ve kaymasız” ifadesi uygulama varsayımı değildir.

## 2. Forex Trading Kursu — Heikin Ashi Trader

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 2/Baskı 2/Forex Trading Kursu - Heiken Ashi Trader (69 sayfa) - @eseckal.pdf>) · [Tam metin](02_heiken_ashi_course.txt)

**Tam okuma:** S. 1–7 Forex piyasa yapısı; s. 8–14 her 100 pip yuvarlak düzeyde 30 piplik ilk tepkiyi alma; s. 15–18 yuvarlak düzeye son 15 pipi yönünde yakalama; s. 19–28 önceki hafta H/L/C ile haftalık pivotun ilk temasından 15 pip ters dönüş; s. 29–35 haftalık pivota son 20 pip yönünde işlem; s. 36–41 geçen haftanın high/low düzeyine son 15 pip yaklaşma; s. 42–47 aynı düzeyin ilk temasında 15 pip taşma; s. 48–69 strateji çeşitlendirmesi ve risk. Başlıktaki Heikin Ashi, bu PDF'de hesaplanan sinyal veya mum dönüşüm kuralı değildir. Haftalık pivotun iki yönü [096. partide](../batch_096/STRATEGIES.md) zaten ayrı adaydır. Yuvarlak düzeye son 15 pip yaklaşma, haftalık pivota son 20 pipin seviye varyantı olduğu için ayrı aday sayılmadı; HR119A içinde yön karşılaştırması olarak tutuldu. S. 10–13 ve 39–46'da seçilmiş grafiklerden sonuçlar türetilir; s. 45–46'da “7 sinyalden 11 kazanç” ve “6 sinyalden 11 kazanç” gibi aritmetik tutarsızlıklar vardır. Performans iddiaları doğrulanmış değildir.

### HR119A — Yuvarlak 100 pip fiyat düzeyinde 30 piplik ters tepki

- **Kaynak (s. 9–14):** EURUSD/GBPUSD dışındaki seçilmiş FX çiftlerinde `1.3500` gibi yuvarlak 100 pip düzeyine limit alım/satım; ilk karşı harekette 30 pip hedef, karşı yönde 30 pip stop. Metin aynı düzeye tekrar dönüşleri de örnekler. Düzeyin emir yoğunluğuna dair anlatı, emir defteri kanıtı değildir.
- **Kapalı mum ve emir sözleşmesi:** Ana evren USDCAD, USDCHF, AUDUSD, NZDUSD, EURJPY, USDJPY, EURGBP, EURCHF M15; her çiftte standart pip boyutu ve broker'ın işlem gören kotasyonu önceden sabitlenir. `R=k×100 pip` fiyat ızgarası; günün ilk **tam kapanmış** M15 barında yakın düzey `R` henüz o gün görülmemiş ve kapanış `R`'den **30–50 pip** uzakta ise `R`'ye yaklaşma tarafına göre limit emri kur: `close>R` → `R`'de long, `close<R` → `R`'de short. 30–50 pip hazırlık aralığı ve günde bir deneme **bizim** yürütme kuralımızdır. Emir ertesi M15'ten itibaren 24 saat veya gün sonundan önce hangisi gelirse ona kadar geçerli; dolmazsa `unfilled`. Girişte hedef yaklaşma tarafına doğru 30 pip, stop ters yöne 30 pip. Tek açık işlem/çift, en çok %0,5 özsermaye riski; spread, komisyon ve kayma. Limit dolumu gerçek bid/ask temasıyla doğrulanır; yalnız mum high/low değdi diye iyimser dolum yok. Aynı mumda stop/hedef varsa tick veri, yoksa kötümser stop önce. Giriş fiyatı gap nedeniyle hedefe yaklaşmış veya 30 pip aralığının dışına taşmışsa işlem atlanır.
- **Ayrışma/test:** Düzey etkisi için her 100 pip ızgarasının **50 pip kaydırılmış** plasebo düzeyleri, [WP96A haftalık pivot ilk temas](../batch_096/STRATEGIES.md) ve aynı seviyeye son 15 pip yaklaşma kolu aynı fiyat akışı ve maliyetle kıyaslanır. Gündüz/sessiz seans, spread ve tekrar temas kesitleri raporlanır. Bu adayın ayırıcı hipotezi fiyatın **sabit psikolojik ızgaraya** ilk temasındaki kısa ters harekettir; 30 pip kâr varsayımı değildir.

### HR119B — Önceki haftanın high/low sınırında ilk temasın 15 pip devamı

- **Kaynak (s. 42–47):** Önceki haftanın yüksekliği ilk kez görüldüğünde o yönde long, düşüklüğü ilk kez görüldüğünde short; 15 pip hedef ve 15 pip stop. Kaynak ilk temas vurgular, tekrar denemeyi önermez. S. 47 hafta açılışı sınırın hemen yanında ise en az 4–5 pip uzaklaşma bekler.
- **Kapalı mum ve emir sözleşmesi:** Ana evren USDJPY ve USDCAD M15, gerçek Forex haftası ve broker sunucu zamanı yerine açık `America/New_York` Pazar 17:00–Cuma 17:00 haftası. Bir önceki **tam kapanmış** haftanın `H,L` değeri yeni hafta başladığında dondurulur. İlk tamamlanmış M15 `L+5 pip < close < H−5 pip` ise iki OCO stop emri: `H`'de buy-stop ve `L`'de sell-stop; 5 pip tampon kaynak uyarısının üst sınırıdır. Sınırın hafta başında zaten aşılması veya ilk M15 içinde teması durumunda geçmişe dolum yok; bu hafta atlanır. Hafta boyunca ilgili sınır ilk kez gerçek kotasyonda geçildiğinde o yönde giriş; diğer emir iptal. Hedef girişten 15 pip ileri, stop 15 pip geri; Cuma 17:00 New York'ta açık pozisyon kapatılır (**bizim** süre çıkışımız). En çok bir işlem/çift/hafta, %0,5 özsermaye riski; bid/ask, spread, komisyon, kayma ve hafta sonu gapleri gerçekçi fiyatla işlenir. Aynı M1'de iki OCO sınırına temas sırası çözülemiyorsa o hafta test dışı veya kötümser sıra; olay gelecekteki haftalık high/low kullanılarak seçilmez.
- **Ayrışma/test:** Aynı önceki hafta düzeylerinde ilk temas **devamı** ile ters yön limit ve [JK70 haftalık uçta SFP](../batch_070/STRATEGIES.md) adayını eşleştir. `H−15 pip`/`L+15 pip` yaklaşma kolu (s. 36–41) yalnız ablation; asıl soru sınırın **ilk geçişinden sonra** ilave 15 pip devam olup olmadığıdır. Net R, dolum oranı, gap/ilk mum atlamaları ve USDJPY/USDCAD ayrı sonuçları raporlanır.

## 3. Teknik Analiz Kursu — Bull and Bear Academy

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 2/Baskı 2/Teknik Analiz Kursu - Bull and Bear Academy (61 sayfa) - @eseckal.pdf>) · [Tam metin](03_bull_bear_technical.txt)

**Tam okuma:** S. 1–10 içerik, teknik analiz varsayımları ve Dow teorisi; s. 11–16 mum tipleri; s. 17–24 trend/destek/direnç, gap ve ada dönüşü; s. 25–33 üçgen/dikdörtgen/bayrak/takoz/baş-omuz; s. 34–43 hacim, OBV, açık pozisyon, MA, MACD, DMI/ADX, TRIN, A/D, RSI ve stokastik; s. 44–48 Elliott/Fibonacci; s. 49–52 risk ve strateji başlıkları; s. 53–61 sözlük/kaynakça. S. 52 uygulanabilir yeni birleşik strateji vermek yerine sonraki bir bölümün vaadini özetler. S. 22–24 gap/ada, s. 25–33 formasyonlar ve s. 34–43 gösterge aileleri arşivde temsil ediliyor. S. 38 ADX>20/25 ile DI kesişimi, mevcut ADX/DMI ailelerinde filtre varyantı; ayrı hipotez açılmadı. S. 35'te açık pozisyon yorumunun son satırları çeviride yön bakımından tutarsız, s. 59 stokastik eşiklerinden biri açıkça hatalı; birebir işlem kuralı olamaz. **Yeni bağımsız aday yok.**

## Sonuç

**2 yeni araştırma adayı:** HR119A ve HR119B. Bunlar geçmiş performansı doğrulanmış stratejiler değildir.
