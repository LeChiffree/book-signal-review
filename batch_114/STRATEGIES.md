# Kitap okuma 114 — NFP öncesi aralıkta iki yönlü stop emirleri

**Kapsam:** Üç ayrı PDF'nin **18 + 21 + 21 = 60 sayfası** baştan sona okundu. Atıflar PDF sayfasıdır. Backtest, paper test ve emir yapılmadı.

## 1. Pin Bar Stratejisi

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 4/Baskı 4/Pin Bar Stratejisi (18 sayfa) - @eseckal.pdf>) · [Tam metin](01_pin_bar.txt)

**Tam okuma:** S. 1–2 giriş/fiyat hareketi; s. 3–4 pin barın küçük gövde ve toplam aralığın en az üçte ikisi uzunluğunda fitil tanımı, kapanışı bekleme; s. 5–6 tanıtım/görsel; s. 7–9 geçmiş destek/dirençte pin bar örneği; s. 10–11 pin burnunun 2–3 pip ötesinde giriş, fitil ucunun 3–5 pip ötesinde stop, ilk karşı destek/dirençte çıkış; s. 12–18 seçilmiş AUDJPY örnekleri/tanıtım. Pin bar + önceki seviye + kırılım tetik mevcut arşiv adaylarıyla, özellikle [14. partideki pin/doji retest](../batch_014/STRATEGIES.md) ve diğer pin bar kurallarıyla örtüşür. Bu PDF giriş ve stop pip tamponlarını netleştirir, fakat hangi eski seviye ve hangi ilk karşı seviye seçileceğini algoritmik vermez. **Yeni bağımsız aday yok.** S. 15/18'deki +50 pip seçilmiş örnekler getiri dağılımı değildir.

## 2. NFP Stratejisi — Unathi W. Salman

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 3/Baskı 3/NFP Stratejisi - Unathi W. Salman (21 sayfa) - @eseckal.pdf>) · [Tam metin](02_nfp_salman.txt)

**Tam okuma:** S. 1–3 çeviri/giriş ve NFP; s. 4–7 önceden açıklanan haber takvimi, USD/JPY veya USD/CHF seçimi ve açık işlemleri haber öncesi kapatma; s. 8–12 H4 trend ve M5/M15 haber öncesi aralık; s. 13–17 yayından 15 dakika önce sınırları çizme, 5 dakika önce iki bekleyen stop emri, yaklaşık 30 pip hedef, geri dönüş ve hedge uyarıları; s. 18–21 sonuç/tanıtım. Kitaptaki “ilk Cuma”, saat farkı ve örnek pip hareketleri sabit veri kabul edilmez; tarihsel yayımlanma saati olay kaydıyla eşleştirilmelidir. S. 16–17'de stop “en az 10 puan” şeklinde geçer ama fiyat örnekleriyle pip/point birimi açık değildir. Geçmiş fiyat grafiği tek başına haber anındaki gerçek dolum fiyatını göstermez.

### UWS114A — NFP duyurusundan önce dondurulmuş M15 aralığının OCO kırılımı

- **Kaynak (s. 9–17):** NFP için USDJPY/USDCHF; haber öncesi M5 veya M15 yüksek/düşük aralığına alış ve satış stop emri; sınırları duyurudan 15 dakika önce, emirleri 5 dakika önce belirle; hedef yaklaşık 30 pip. Kaynak ikinci emrin dolması/hedge fikrini de tartışır. Kapanmış mumlardan üretilebilir tekil kol için ilk dolumda karşı emri iptal etmek **bizim OCO risk tanımımızdır**, kaynak hedge iddiası değildir.
- **Kapalı mum deney sözleşmesi:** Tarihsel NFP *planlı yayımlanma zamanları* ayrı arşivden, olay gününde önceden bilinen sürüm ve saat dilimiyle alınır; gerçekleşen NFP sayısı veya sonradan revize edilmiş takvim sinyal girdisi olmaz. USDJPY için tek brokerdan zaman damgalı bid/ask tick/quote; veri yoksa bu adayın dolumu doğrulanmış sayılmaz. Olay `T` için `T−30` ile `T−15` dakikaları arasında **tamamlanmış** üç M5 mumun en yüksek/alt değerleri `U,L` olarak `T−15`'te dondurulur (**bizim kesin aralık seçimimiz**). `T−5`'te hâlâ iki emir için uygun konum varsa `U+1 pip` alış stop, `L−1 pip` satış stop; fiyat bu düzeyleri daha önce geçmişse olay atlanır. Emirler yalnız `T−5`–`T+5` arası geçerli; ilk gerçek dolum karşı emri iptal eder, ikisinin dolması operasyonel hata olarak ayrı raporlanır. Stop karşı aralık sınırının 1 pip dışı; sabit 30 pip hedef kaynak kolu, 1R hedef karşılaştırma kolu. İşlem `T+30`'da zorunlu kapanır (**bizim**). Emir büyüklüğü, en kötü tahmini stop ve spread/kayma dahil hesap özsermayesinin en çok %0,25'ini riske eder; `U−L<5 pip` veya >`50 pip` ise olay atlanır (**bizim** likidite/risk filtresi). Stop emri fiyat garantisi değildir: gerçek alış ask, satış bid; gap/kotasyon boşluğu sonrası ilk gerçekleşebilir kötü fiyat; normal dönem spread'i haber anına taşınmaz. Tick sırasına göre stop/hedef; olmayan tick/senkronizasyon verisinde sonuç “belirsiz” ve ayrı sayılır.
- **Ayrışma/test:** Aynı NFP olaylarında iki yönlü aralık kırılımını, ilk **tamamlanmış** duyuru sonrası M5 kırılımına giriş ve olay dışı aynı saat/gün aralık kırılımıyla kıyasla. Dolmayanlar, spread patlaması, yeniden fiyatlama, iptal gecikmesi, net R ve olay yılı dağılımı raporlanacak. NFP yayımlanma anında kullanılan yüksek/düşük, gerçekleşen haber sayısı ve olay sonrası en avantajlı fiyat ile geriye dönük sınır çizilmeyecek. Önceki [83. parti NFP sonrası iç mum](../batch_083/STRATEGIES.md) gözleminden farkı, **yayın öncesi iki yönlü** emir ve haber anı yürütme riskidir.

## 3. Nasdaq Trading Stratejisi — Thabang Lebese

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 7/Baskı 7/Nasdaq Trading Stratejisi - Thabang Lebese (21 sayfa) - @eseckal.pdf>) · [Tam metin](03_nasdaq_lebese.txt)

**Tam okuma:** S. 1–2 kapak/pazar ve H1; s. 3–5 EMA9/EMA18, H4/D1 iki EMA üstü/altı kapanış ve H1 giriş; s. 6–14 önceki gün yüksek/düşükte V/Z ve retest; s. 15 dönüş fitili; s. 16–19 destek/direnç ve dönüş mumları; s. 20–21 sonuç/tanıtım. V/Z ve önceki gün düzeyinin reddi [111. partideki FX Goat](../batch_111/STRATEGIES.md) kitabıyla ve arşiv SFP/retest aileleriyle aynı çekirdektir. EMA filtresi için s. 4 H4/D1 seçimi ve s. 5 “crossover” zamanı tutarlı tek olay kuralı vermiyor; sonradan EMA9/18'i uygun örneklere eklemek bağımsız kaynak strateji sayılmaz. **Yeni aday yok.** S. 2'deki “asla yanılmayacaksınız” iddiası performans kanıtı değildir; kaldıraç/bakiye örnekleri deney risk kuralı yapılmadı.

## Sonuç

**1 yeni araştırma adayı:** UWS114A. Gerçek haber anı kotasyonları olmadan güvenilir backtest mümkün değildir.
