# Kitap okuma 117 — SPY RSI(2) dönüşünde önceki tepe çıkışı

**Kapsam:** Üç ayrı PDF'nin **31 + 33 + 27 = 91 sayfası** baştan sona okundu. Atıflar PDF sayfasıdır. Bu partide backtest, paper test veya emir yapılmadı.

## 1. Wyckoff Metodolojisi

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 3/Baskı 3/Wyckoff Metodolojisi (31 sayfa) - @eseckal.pdf>) · [Tam metin](01_wyckoff_methodology.txt)

**Tam okuma:** S. 1–8 fiyat dalgalarının güç, hız ve derinlik karşılaştırması; s. 9–16 trend çizgileri ve kanallar; s. 17–26 birikim/dağıtım evreleri, spring, SOS, LPS ve UTAD; s. 27–28 emir eşleşmesi ve point-and-figure; s. 29–31 metin katmanında boş kalan hacim/fiyat uyumu ve uyumsuzluğu görselleri ayrıca incelendi. Dalgaların/pivotların teyit zamanı, hacim uyumsuzluğu eşiği ve giriş/çıkış sırası mekanik biçimde verilmez. Spring, kanal ve hacim çabası/sonucu arşivdeki Wyckoff, SFP ve VSA adaylarıyla örtüşür. **Yeni bağımsız aday yok.**

## 2. RSI Trading — Tyler Aaron

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 19/Baskı 19/RSI Trading - Tyler Aaron - Bu Stratejiyle Bir Profesyonel Gibi Trade Yapın (33 sayfa) - @eseckal.pdf>) · [Tam metin](02_rsi_tyler_aaron.txt)

**Tam okuma:** S. 1–10 RSI temelleri ve 50 çizgisi; s. 11–17 RSI(2) aşırılıkları, SPY örnekleri ve RSI(30)>50 filtresi; s. 18–22 ortalamaya dönüş ve stop tartışması; s. 23–25 SPY'de RSI(2)<15 alımı ve önceki tepenin üzerinde günlük kapanışla çıkış; s. 26–33 RSI uyumsuzluğu ve baş-omuz yorumları. RSI(2)>85 ve RSI30 filtreli modeller önceki adayların varyantlarıdır. S. 24'te verilen 470 işlem, %75 kazanma, %23 azami düşüş ve 2,3 kâr faktörü kaynak iddiasıdır; işlem listesi, masraf ve yeniden üretilebilir veri yoktur. “Stop işe yaramaz” görüşü risk kuralı olarak benimsenmedi.

### TA117A — SPY RSI(2)<15 sonrası önceki gün yüksekliği üzerinde kapanış

- **Kaynak kuralı (s. 23–24):** RSI(2) 15'in altındayken SPY long; günlük kapanış “bir önceki zirve” üstüne çıktığında pozisyonu kapat. Metin kapanış fiyatında aynı gün alış/satış varsayar. “Zirve”nin önceki barın high değeri mi, teyitli bir salınım tepesi mi olduğu açıklanmaz. Ana testte **önceki işlem gününün high değeri** önceden sabitlenmiş yorumumuzdur; teyitli pivot tepesi yalnız ayrı duyarlılık kolu olabilir.
- **Kapalı mum deney sözleşmesi:** SPY günlük, bölünme/temettü ayarlı OHLC ve gerçek ABD borsa seans takvimi. Wilder RSI(2) yalnız tamamlanmış gün kapanışlarıyla hesaplanır. Pozisyon yokken `RSI2[t]<15` ise `t+1` açılışında long; aynı kapanışta dolum sayılmaz. Pozisyondayken `close[t]>high[t-1]` ise `t+1` açılışında çık. Giriş günü kapanışı en erken çıkış sinyalidir. Girişte `2×ATR14` uzaklıkta koruyucu stop, 20 işlem günü azami elde tutma ve işlem başına en çok %0,5 özsermaye riski **bizim** araştırma/risk tanımlarımızdır; stop gap ile aşılırsa gerçek sonraki işlem fiyatı kullanılır. Tek pozisyon; aynı sinyal devam ederken tekrar giriş için RSI2'nin önce ≥15'e dönüp sonra yeniden <15 olması gerekir (**bizim** olay ayrıştırmamız). Spread, komisyon, kayma ve temettü etkisi raporlanır.
- **Ayrışma ve karşılaştırma:** Aynı SPY döneminde RSI(2)<15 / RSI(2)>85, RSI(2)<15 / SMA5 üzeri kapanış ve SPY al-tut kıyasları. Yeni hipotez giriş eşiği değil, **önceki gün high üstü kapanışın çıkış kalitesi**dir; ortalama elde tutma, piyasa maruziyeti, işlem sayısı, net getiri, azami düşüş ve maliyet duyarlılığı ölçülecek. Kaynağın aynı kapanış dolumlu sonuçları sonraki açılış uygulamasına kanıt olarak taşınmaz. Parametreler dış örnekleme bakarak seçilmez.

## 3. Güniçi Trading — B. Jonathan

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 5/Baskı 5/Güniçi Trading - B. Jonathan (27 sayfa) - @eseckal.pdf>) · [Tam metin](03_intraday_jonathan.txt)

**Tam okuma:** S. 1–8 güniçi işlem, trend çizgisi ve MACD; s. 9–10 AmiBroker EMA13/EMA9 ve `Peak(C,2,2)` taraması; s. 11–14 ilk 30 dakika yüksek/düşük kırılımı, %1 hedef/%0,5 stop; s. 15–18 beş günlük aralık/düşük oynaklık ve hacim; s. 19–20 temel etkenler; s. 21 Gann karekök düzeyleri; s. 22–27 işlem planı, Elliott dalgası ve kapanış. İlk 30 dakika açılış aralığı kırılımı mevcut [ORB/VWAP adayının](../batch_048/STRATEGIES.md) ve [hisse ORB adayının](../batch_060/STRATEGIES.md) pencere/hedef varyantıdır. S. 9–10'daki `Peak` geçmiş pivotu ileri barlarla teyit edebildiğinden kodun sinyal anında yeniden boyanmadığı gösterilmeden kullanılamaz. Beş günlük sıkışma ve hacim için kaynakta tek bir ölçü/eşik seti yoktur; mevcut sıkışma kırılımı ailelerini yeni mekanik kural diye çoğaltmadık. **Yeni bağımsız aday yok.**

## Sonuç

**1 yeni araştırma adayı:** TA117A. Toplam kayıt, bu partinin işlenmesiyle **351** olur. Kârlılık ve uygulanabilirlik daha sonra backtest/paper test ile sınanacaktır.
