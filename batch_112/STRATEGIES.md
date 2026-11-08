# Kitap okuma 112 — çift doji sınırında iki yönlü emir

**Kapsam:** Üç ayrı PDF'nin **10 + 12 + 17 = 39 sayfası** baştan sona okundu. Atıflar PDF sayfasıdır. Backtest, paper test ve emir yapılmadı.

## 1. Trading İşlemlerinde İkili Dojinin Sırrı — Vladimir Ribakov

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 2/Baskı 2/Trading İşlemlerinde İkili Dojinin Sırrı - Vladimir Ribakov (10 sayfa) - @eseckal.pdf>) · [Tam metin](01_double_doji_ribakov.txt)

**Tam okuma:** S. 1 tanıtım; s. 2–4 doji ve art arda iki doji, tercihen belirgin hareket sonu, gövde için 2–4 pip esneklik; s. 5 iki mumun birleşik yüksek/düşük sınırları; s. 6 iki karşı yönlü stop emri, biri dolunca diğerini iptal, stop karşı sınır dışı, 1R hedef; s. 7–9 yarım yarım 1R/2R veya %80'i 0,5R ve %20'si 2R'de çıkış, H1/H4/D1 ve USD/JPY pariteleri; s. 10 kural özeti. Kaynağın %70/%80 başarı iddiaları veri ve yöntem içermiyor; doğrulanmış oran sayılmadı.

### VR112A — Art arda iki doji için OCO kırılımı

- **Kaynak (s. 2–3, 5–10):** İki bitişik doji kapanınca birleşik üst sınırın 1 pip üstüne alış stop, alt sınırın 1 pip altına satış stop; ilk dolan emir karşı emri iptal eder. Girişin karşı sınırının 1 pip dışı stop. Çıkış seçenekleri: tamamı 1R; yarısı 1R ve yarısı 2R (ilk hedef sonrası ikinci yarı başabaşa); %80'i 0,5R ve %20'si 2R. En az üç aynı renkli önceki mum tercih edilir ama zorunlu değildir.
- **Kapalı mum deney sözleşmesi:** EURUSD H1 ana evren, GBPJPY H1 önceden ayrı kol; H4/D1 duyarlılık. İki tamamlanmış bitişik mumun her birinde `|close−open|≤4 pip`, `high−low≥8 pip` ve açık/kapalı OHLC geçerli olacak. Kaynak 2–4 pip gövdeyi doji kabul eder; sıfır gövde de dahil, minimum aralık **bizim** sıfıra yakın gürültü filtremiz. `U=max(high1,high2)`, `L=min(low1,low2)`; ikinci mum kapanınca U+1 pip buy-stop, L−1 pip sell-stop OCO kur. Sinyalden sonraki ilk üç tam H1 mumunda dolmazsa ikisini de iptal et (**bizim** süre sınırımız). İlk dolumda karşı emri hemen iptal; broker akışında aynı anda iki dolum ihtimali ve stop/TP sırası için bid/ask M1 veya tick olay kaydı kullan. Yalnız OHLC H1 varsa aynı barda iki sınır görüldüğünde kurulum belirsiz sayılıp işlemden dışlanır, sonuç sonradan seçilmez. Long stop L−1 pip, short stop U+1 pip; spread, komisyon ve kayma dahil. Birincil çıkış tüm miktar 1R; iki parçalı kaynak yönetimleri ayrı önceden kayıtlı kollar. Maliyet sonrası risk pozitif, en çok %0,5 özsermaye; 24 H1 barda gerçekleşmeyen pozisyon piyasa fiyatıyla kapanır (**bizim**). İsteğe bağlı üç aynı renkli önceki mum filtresi ayrı kol, aynı örneklemin tek başına sonucu gibi sunulmaz.
- **Ayrışma/test:** Arşivdeki genel doji/inside bar ve dar aralık kırılım ailelerine karşı aynı işlem evreninde çift doji şartının, OCO icrasının ve üç çıkış politikasının ayrı katkısı ölçülecek. Tek doji, aynı toplam aralığa sahip iki rastgele mum ve iki doji kıyasları; tüm geçerli kurulumlar, doldurulmayan emirler, çifte temas dışlamaları, maliyet sonrası net R ve rejimlere göre sayımlar raporlanacak. Zaman sıralı dış örneklem ayrımı yapılacak; 4 pip ve diğer eşikler sonuçlara göre geriye dönük seçilmeyecek.

## 2. Kanal Ticareti

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 7/Baskı 7/Kanal Ticareti (12 sayfa) - @eseckal.pdf>) · [Tam metin](02_channel_trading.txt)

**Tam okuma:** S. 1–4 kapak/giriş; s. 5–6 paralel yükselen, düşen veya yatay kanal; s. 7–9 üst çizgide satış veya alt çizgide alış, stop kanal dışı, hedef karşı kenar; s. 10 kanalın sonunda kırılabileceği ve stop gereği; s. 11–12 sonuç/tanıtım. Bu çekirdek [44. partideki C44](../batch_044/STRATEGIES.md) ile aynı kanal kenarından kenara dönüş kuralıdır; yeni aday sayılmadı. Kaynak çizgilerin hangi pivotlarla ve ne zaman çizileceğini kesinleştirmediğinden C44'ün önceden sabitlenen geometrisi korunur.

## 3. Forex — JM Shepal

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 18/Baskı 18/Forex - JM Shepal (17 sayfa) - @eseckal.pdf>) · [Tam metin](03_forex_shepal.txt)

**Tam okuma:** S. 1–3 içindekiler/giriş; s. 4–5 döviz, parite ve pip; s. 6–8 broker, emir türleri, temel faktörler; s. 9–11 teknik/temel analiz, destek–direnç aralığı, gün içi, carry ve arbitraj; s. 12–13 demo hesap; s. 14–16 disiplin ve günlük; s. 17 sonuç. Aralık ticareti kanal ve destek/direnç adaylarının tekrarıdır. Carry ve arbitraj için faiz verisi, işlem yeri, yürütülebilir kotasyon, eşzamanlı dolum ve risk koşulları verilmemiştir; yalnız mum kapanışından üretilebilir bağımsız sinyal yok. Yeni aday sayılmadı. Kitabın kazanç garantisi ve arbitrajın risksizliği yönündeki ifadeleri doğrulanmış sonuç değildir.

## Sonuç

**1 yeni araştırma adayı:** VR112A. Bu aday henüz doğrulanmış işlem stratejisi değildir.
