# Kitap okuma 138 — mum kalıpları, uygulama disiplini ve CCI geri dönüşü

**Kapsam:** Üç ayrı PDF'nin **23 + 42 + 32 = 97 sayfası** baştan sona okundu. PDF sayfa numaraları kullanılır. Backtest, paper test ve emir yapılmadı.

## 1. Kolaylaştırılmış Mum Grafikleri — James Williams

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 9/Baskı 9/Kolaylaştırılmış Mum Grafikleri - James Williams (23 sayfa) - @eseckal.pdf>) · [Tam metin](01_candles_williams.txt)

**Tam okuma:** S. 1–5 döviz ve piyasa tanıtımı; s. 6–10 OHLC, doji, çekiç ve çift gölge; s. 10–14 cımbız, delici/kara bulut, yutan, yıldız ve üç asker/karga; s. 14–17 kule, yuvarlak tepe/dip ve 8–10 yeni dip/tepe; s. 18–22 RSI, stokastik, CCI, BB, MACD ve Fibonacci; s. 23 sonuç. Bunlar önceki [mum ailesi](../batch_052/STRATEGIES.md), [yutan mum](../batch_050/STRATEGIES.md) ve osilatör adaylarıyla örtüşür. S. 7'de beyazı düşüş, siyahı yükseliş olarak tarif etmesi, s. 11–14'teki boğa/ayı anlatımıyla karışır; renk yerine `close>open` kullanılmalı. S. 13 akşam yıldızının son mumunu “güçlü yükseliş” diye yazması da ayı dönüş anlatımıyla çelişir. S. 16'daki art arda 8–10 seans yeni dipten otomatik long çıkarılmaz; teyit belirtse de tam giriş/stop/çıkış yok. **Yeni bağımsız aday yok.**

## 2. Saçmalık Olmayan Rehber — David Fiacan

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 9/Baskı 9/Saçmalık Olmayan Rehber - Trade İşlemlerine Nasıl Başlanır - David Fiacan (42 sayfa) - @eseckal.pdf>) · [Tam metin](02_fiacan_guide.txt)

**Tam okuma:** S. 1–6 önsöz/başlangıç; s. 7–13 sermaye, işlem başına risk ve düşüş örnekleri; s. 14–19 gösterge çoğaltma ve arz/talep savı; s. 20–26 beklenti ve plan dışı işlemler; s. 27–34 gün içi ile günlük swing karşılaştırması; s. 35–42 sermaye büyüklüğüne göre piyasa/kontrat seçimi. Kitap yazarın arz/talep stratejisinin **giriş, stop ve hedef kurallarını vermiyor**; ücretli eğitime yönlendiriyor (s. 17–19, 33). Bu yüzden test edilebilir yeni yön sinyali yok. S. 39'daki küçük hedef ve büyük hedef için iki parçalı çıkış, mevcut stratejiler için ayrı çıkış deneyi olabilir; hedeflerin oranı/veri temeli yoktur. S. 28–30'daki HFT'nin bütün kısa kırılımları kasıtlı manipüle ettiği anlatısı bu kitapla doğrulanmaz. S. 35–42'deki sermaye, kontrat ve %5 risk önerileri dönemsel/pratik örneklerdir; strateji performans delili değildir. **Yeni bağımsız aday yok.**

## 3. Trading İşlemlerinde Başarılı Olmanın Sırları — Lee Kelvin

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 9/Baskı 9/Trading İşlemlerinde Başarılı Olmanın Sırları - Lee Kelvin (32 sayfa) - @eseckal.pdf>) · [Tam metin](03_kelvin_secrets.txt)

**Tam okuma:** S. 1–7 seviye, Fibonacci, pivot ve salınım; s. 8–11 MACD kesişimi/ayrışması; s. 12–17 ADX25 trend ve kırılım filtresi; s. 18–23 CCI ±100 trend ve ±200 sonrası geri dönüş; s. 24–27 BB20/2 ve ATR; s. 28–31 risk/ödül; s. 32 vaat edilen “MACD sırrı”nın yalnız video bağlantısı. Video içeriği PDF'de yoktur, strateji diye kaydedilmedi. ADX25, MACD ve BB kullanımları önceki adaylarla örtüşür. S. 30–31'de %50 kazanç/2R örneği, bu oranların gerçek piyasada mevcut olduğunu göstermez; ücret ve kayma eksik. S. 31'deki aylık garantili kâr iddiası doğrulanmamıştır.

### LK138A — CCI ±200 taşması sonrası ±100 geri geçişi

- **Kaynak kural:** CCI `+200` üzerine çıktıktan sonra `+100` altına geçince short; `−200` altına indikten sonra `−100` üzerine geçince long (s. 22–23). Bu, s. 18'deki `+100` üstü trend long / `−100` altı trend short kuralından **farklı bir rejim**dir; aynı anda iki karşıt yön üretilmemeli.
- **Bizim ön kayıt tanımı:** H4 tipik fiyat `(high+low+close)/3` ile standart CCI(20). Long için son 12 tamamlanmış H4 bar içinde CCI `<−200` kaydedilmiş olsun; sonra ilk `CCI[t−1]≤−100` ve `CCI[t]>−100` **kapanışında** long olayı. Shortta son 12 barda `>+200`, sonra ilk `CCI[t−1]≥+100` ve `CCI[t]<+100`. Aşırı bölgeden ilk çıkıştan sonra yeniden taşma olmadan ikinci sinyal yok. `20`, H4 ve 12 bar penceresi bizim karşılaştırma parametrelerimizdir; kaynak CCI periyodu/zaman dilimi vermez.
- **Giriş/risk/çıkış:** Sinyal kapanışını izleyen ilk işlem yapılabilir M1 açılışı; long stop aşırı bölgeye ilk girişten sinyal kapanışına kadar görülen en düşük low `−0,1 ATR14_H4[t−1]`, short simetri. Stop yanlış taraftaysa atla. Hedef 2R; en çok 18 H4 bar sonra zaman çıkışı. İşlem başına en çok %0,5 özsermaye riski; gerçek bid/ask, ücret, kayma ve aynı M1 mumunda stop önceliği dahil. Stop, 2R ve süre kaynakta verilmez, bizim test sözleşmemizdir.
- **Kıyas:** [Önceki CCI/BB adayı](../batch_071/STRATEGIES.md), yalnız CCI ±100 trend sinyali ve basit CCI ±200'den hemen dönüş ile aynı veri/maliyet üzerinde kıyasla. ±200 ve ±100 eşiklerinin seçilmiş olma riskini zaman sıralı dış örneklemde değerlendir; optimize ederek sonucu şişirme.

## Sonuç

**1 yeni araştırma adayı:** LK138A. Diğer iki kitap yeni, bağımsız kapalı mum işlem sözleşmesi sağlamadı.
