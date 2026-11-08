# Kitap okuma 158 — Wyckoff, Forex anahtarları ve VWAP dönüşü

Üç ayrı PDF'nin **52 + 41 + 59 = 152 sayfası** sırayla okundu. **Yeni bağımsız strateji adayı: 1.** Sayfa atıfları PDF sayfasıdır. Aday kârlılık kanıtı değildir; backtest, paper test ve emir yapılmadı.

## 1. Günlük Hisse Senedi Ticaretimin Sırları — Richard D. Wyckoff

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 10/Baskı 10/Günlük Hisse Senedi Ticaretimin Sırları - Richard D. Wyckoff (52 sayfa) - @eseckal.pdf>) · [tam metin](01_wyckoff_daily_stock.txt)

**Tam okuma:** s. 1–12 bant okuma ve lider hisse/sektör ilişkisi; 13–18 maliyet, stop ve işlem örnekleri; 19–26 işlemlerin akışı, hacim ve emilim yorumu; 27–30 göreli güç ve haber tepkisi; 31–38 dar aralık, hacimle kırılım ve grafiklerin sınırları; 39–44 pozisyon yönetimi ve geri çekilme; 45–52 psikoloji, çıkış ve seçilmiş işlem kayıtları.

**Karar:** s. 31–34 dar banttan hacimle kırılım önceki aralık/kırılım adaylarıyla örtüşür. s. 19–26'daki işlem bandı ve emir akışı yorumu OHLCV'den bire bir çıkarılamaz; bankaların niyeti gibi nedensel çıkarımlar ölçülebilir kural değildir. s. 39–44 stop ve düzeltme örnekleri genel yönetim kurallarıdır. Seçilmiş işlemler tam performans kanıtı sayılmaz. **Yeni bağımsız aday yok.**

## 2. Başarılı Forex Ticareti için 10 Anahtar — Jared F. Martinez

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 14/Baskı 14/Başarılı Forex Ticareti için 10 Anahtar - Jared F. Martinez (41 sayfa) - @eseckal.pdf>) · [tam metin](02_martinez_ten_keys.txt)

**Tam okuma:** s. 1–14 Forex temelleri; 15–20 eğilim, çoklu zaman dilimi ve yatay bölge; 21–24 zarar durdurma; 25–30 Fibonacci düzeltme/uzatma seviyeleri; 31–41 plan, eğitim ve psikoloji.

**Karar:** Trend çizgisi, destek/direnç ve Fibonacci seviyeleri giriş, stop ve çıkışın birlikte nesnel tanımını vermiyor; seviye seçimi öznel. Anlatılan temel parçalar önceki trend, yatay aralık ve Fibonacci adaylarında mevcut. **Yeni bağımsız aday yok.**

## 3. Ortalamaya Dönüş Günlük Trading — David Harnett

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 17/Baskı 17/Ortalamaya Dönüş Günlük Trading - David Harnett (59 sayfa) - @eseckal.pdf>) · [tam metin](03_harnett_mean_reversion.txt)

**Tam okuma:** s. 1–18 ortalamaya dönüş ve trend rejimi; 19–38 sekiz gösterge fikri; 39–54 altı birleşik kurulum; 55–59 test ve kapanış. RSI/BB ve EMA200/Keltner/RSI/ADX aileleri [71. partide](../batch_071/STRATEGIES.md) zaten kaydedildi. WaveTrend, Cuban Reversion, Responsive LinReg, Blackcat ve CM Pivot Bands gibi özel göstergeler sürüm/formül ve yeniden boyama bilgisi olmadan kaynakla aynı şekilde sınanamaz. s. 45 kısa yön koşullarında çeviri çelişkisi var; kodlamaya alınmadı.

### HR158A — Günlük VWAP yönünde BB(20,1,5) taşması ve Stoch(7,4,3) dönüşü

- **Kaynak:** s. 47–48, 5 dakikalık grafikte VWAP yön filtresi, Bollinger dışına kapanış, Stoch aşırı bölgesi, banda geri kapanışta giriş; giriş mumunun ötesinde stop; karşı banda dokunuş veya Stoch karşı aşırı bölgede çıkış. Kaynak BB standart sapmasını 1,5; Stoch parametrelerini 7/4/3 verir. BB uzunluğunu, VWAP gün başlangıcını, taşmadan sonraki bekleme süresini ve ücretleri vermez. Kaynağın “en iyi” zaman dilimi iddiası doğrulanmış sonuç değildir.
- **Ön kayıtlı test tanımı (bizim seçimlerimiz):** BTCUSDT ve ETHUSDT spot 5m OHLCV. UTC 00:00'da sıfırlanan tipik fiyat × hacim VWAP; BB orta SMA20, nüfus standart sapması ×1,5; Stoch en yüksek/en düşük 7 bar, %K için SMA4, %D için SMA3. Eksik/gap bar veya sıfır hacimde sinyal yok. Gün başında 20 tam bar ve yeterli Stoch geçmişi oluşmadan işlem yok. Yalnız tamamlanmış mumlar kullanılır.
- **Long:** t0 mumunda `close < altBB` ve `%K < 20`; sonraki en çok 3 tamamlanmış 5m mumda ilk `close > altBB` ve `close > VWAP` giriş tetikleyicisidir. **Short:** t0 `close > üstBB` ve `%K > 80`; sonraki en çok 3 mumda ilk `close < üstBB` ve `close < VWAP`. t0 ve tetik aynı UTC gününde olmalı. Bu sıralama kaynakta tam belirtilmediği için test uyarlamasıdır; eşzamanlı VWAP şartı konursa olayların seyrekleşebileceği ayrıca raporlanır.
- **İcra/risk:** Tetik kapanışından sonraki ilk uygulanabilir 1m açılışta gir; eldeki 5m tetik mumu low/high ± `0,1 × ATR14_5m` stop. Hedef girişte donmuş **karşı** BB fiyatı; hedef girişe göre lehte değilse atla. Stoch `%K > 80` (long) / `< 20` (short) ilk tamamlanmış 5m kapanışında ayrıca çıkış; en çok 24 adet 5m mum tut. İki yön aynı anda açılmaz, sembol başına tek pozisyon; 1m barında stop ve hedef birlikte görülürse stop önce; komisyon, spread ve kayma uygulanır. Emir ve stop bir sonraki uygulanabilir 1m'den önce etkinleşmez. Sabit risk işlem başına sermayenin %0,25'i; kaldıraç yok.
- **Değerlendirme:** BB dışına kapanıp geri girme, VWAP filtresiz BB+Stoch ve [71. partideki BB/RSI](../batch_071/STRATEGIES.md) ile aynı veri aralığında karşılaştır. İşlem sayısı, ücret sonrası medyan/net R, maksimum düşüş, long/short ve BTC/ETH ayrımı, parametre duyarlılığı, aşırı seyrek sinyal ve dönem dışı sonuçlar raporlanmalı. Kısa örneklem veya masraf sonrası zayıf sonuçta reddedilir. Günlük tek karar akışına uygun değildir; ileride ayrı 5m veri/izleme altyapısı gerekir.

**Parti sonucu:** 3 kitap, 152 sayfa, 1 yeni aday. Birikmiş toplam **390 strateji adayı**; hepsi henüz doğrulanmamış araştırma hipotezidir.
