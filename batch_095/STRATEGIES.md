# Kitap okuma 095 — EMA21 pin bar, SMA100/200 mum teyidi ve scalp maliyeti

**Kapsam:** Önceden tamamlanmamış üç PDF'nin **38 + 39 + 27 = 104 PDF sayfası** baştan sona okundu. Kural ve grafik içeren 21 sayfa [görsel olarak kontrol edildi](figure_contacts/). Bu partide **yeni bağımsız strateji başlığı yok**; ölçülebilir fikirler önceki adayların filtre, giriş veya maliyet varyantlarıdır. Backtest, paper test ve emir yapılmadı. Sayfalar PDF sayfasıdır.

## 1. Günde 40 Pips — dosya adında Giorgio Strani, iç kapakta Giorgio Tasca

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 15/Baskı 15/Günde 40 Pips - Giorgio Strani (38 sayfa) - @eseckal.pdf>) · [Tam metin](01_forty_pips_strani.txt)

**Kimlik notu:** Dosya adı “Giorgio Strani”, PDF s. 2 iç kapağı ve s. 4 telif sayfası **Giorgio Tasca** diyor. Kaydı dosya adıyla eşliyoruz; yazarlığı doğrulanmış tek isim gibi göstermiyoruz.

**Sayfa haritası:** s. 1–7 kapak/uyarı/tanıtım; 8–10 EMA21 ve H1/D1 zaman dilimi; 11–16 trend, 200 MA ve destek/direnç; 17–18 pin bar; 19–26 adım adım trend + EMA21 pin bar, stop/ilk karşı seviye hedefi; 27–29 para yönetimi/sabır; 30–38 tanıtım. S. 2, 14, 17, 19, 24–25 görsel denetlendi.

**Kaynak kuralı ve örtüşme:** Yazar D1 tercih eder, H1 altını önermiyor (s. 9–10). Orta trend için EMA21, daha uzun yön bağlamı için MA200, trend lehinde EMA21'e değen/üstünde duran pin bar ve mumun karşı ucunda stop, karşı yöndeki ilk destek/dirençte kâr hedefi anlatır (s. 8, 12–17, 19–25). Kaynak “pin bar” gövde/fitil sayısal oranını, destek/direncin pivot algoritmasını, EMA ile temas toleransını ve giriş emrinin tam tetik koşulunu vermez. Bu çekirdek zaten [PB49: trend yönünde EMA21 geri çekilmesinde pin bar](../batch_049/STRATEGIES.md) ve [H4 EMA21 + pin/yutan](../batch_059/STRATEGIES.md) ile kayıtlıdır. Aynı sinyalin D1 sürümü veya MA200 kapısı ayrı portföy fırsatı değildir.

**Gelecek filtre deneyi:** PB49 olaylarında EMA21 temaslı pin barın D1 versiyonunu, aynı olaylarda `close_D1>EMA200_D1` (short tersi) filtresi **var/yok** olarak karşılaştır. D1 pin ölçüsünü PB49'un önceden sabitlenmiş gövde/fitil algoritmasından al; EMA21 önceki kapalı bar değerini temas seviyesi olarak dondur, bugün kapanmış mumla trend doğrula ve sinyalden sonraki ilk M1 fiyatını kullan. Stop pin karşı ucu, ilk **önceden teyitli** karşı pivot en az maliyet + 1R uzakta ise kaynak hedefinin nesnel vekili; yoksa hedefli kol işlem dışı, yalın 2R/H7D karşılaştırması sürer. Pivotun 2-sol/2-sağ teyidi, 1R eşiği ve H7D bizim sözleşmemizdir; yazarın sayısı değildir. S. 17'deki “%80 başarı” ve s. 28'deki aylık getiri seçilmiş anlatı, doğrulanmış net getiri değildir. 40 pip hedef adını kripto fiyat birimi yapmayız.

## 2. Kazandıran Forex Trading - Forex'te Kazanmak için Günde 10 Dakika — dosya adında Giorgio Strani, iç metinde Giorgio Tasca

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 15/Baskı 15/Kazandıran Forex Trading - Forex_te Kazanmak için Günde 10 Dakika - Giorgio Strani (39 sayfa) - @eseckal.pdf>) · [Tam metin](02_ten_minutes_strani.txt)

**Kimlik notu:** Dosya adı “Giorgio Strani”, PDF s. 30 iletişim ve s. 36 yazar/diğer kitaplar bölümü **Giorgio Tasca** diyor. İlk PDF ile aynı isim uyuşmazlığı var; içerikler birebir aynı değil (ilki EMA21 pin, bu kitap SMA100/200 + üç mum kalıbı).

**Sayfa haritası:** s. 1–5 giriş, SMA100/200 ve D1 tercihi; 6–10 trend ve destek/direnç; 11–17 pin, yutan ve yıldız mumu; 18–24 SMA100/200 yönü, seviye bağlamı ve seçilmiş örnekler; 25–27 1:3 RR, stop, ilk karşı seviye ve bekleyen stop emirleri; 28–30 para yönetimi/sonuç; 31–39 tanıtım. S. 4, 11, 13, 15, 18, 21, 26–27 görsel denetlendi.

**Kaynak kuralı ve karar:** D1'de SMA100>SMA200 ise long yönü, tersi short (s. 18); güçlü statik/dinamik seviye yanında trend yönünde pin, yutan veya sabah/akşam yıldızı (s. 11–21). S. 27 pin veya yutan mumun ekstresi ötesine bekleyen stop giriş, karşı ekstremde stop ve ilk karşı seviyede hedef çizimleri var. Bu, [pin bar/EMA](../batch_049/STRATEGIES.md), [yutan mum + seviye](../batch_080/STRATEGIES.md) ve [mum sonrası ekstrem stop giriş](../batch_050/STRATEGIES.md) adaylarının SMA filtresiyle birleşimidir. Tek mum olayı iki strateji diye çoğaltılmamalı. Kaynak s. 18 short için SMA100<SMA200 derken grafiğin “artan” olduğunu da söyler; bu yön çelişkisi görselden kesin düzeltilemez, short şartını literal tutarsızlık olarak not ediyoruz. Sabah/akşam yıldızının s. 15 tanımı **gap şartı vermiyor**; klasik gapli yıldızla aynı olay sayılmaz ve önceki [gap uyarısı](../batch_003/STRATEGIES.md) geçerlidir.

**Gelecek karşılaştırma:** PB49 ve yutan mum adaylarının mevcut D1 karar günlerinde `SMA100_D1>SMA200_D1`/tersi filtresi ve sinyal barının teyitli S/R'ye yakınlığı ayrı ablation; yerler geçmiş kapalı D1 pivotlarından dondurulur. Sinyal sonrası yalnız ertesi D1 içinde ekstrem stop emir tetiklenirse sonraki uygun M1 ile gerçekçi dolum; tetiklenmezse iptal. Stop sinyal mumu karşı ucu, hedef ilk önceden bilinen karşı pivot en az 1R uzaktaysa; 2R ve H7D yalın çıkışla kıyasla. Ertesi gün süresi, pivot algoritması, 1R ve H7D **bizim** varsayımlarımızdır. S. 11/13/15'teki `%80/%70/%60` başarı ve s. 25'teki 1:3 matematik örneği işlem örneklemi değildir; net başarı sayılmaz.

## 3. Forex Piyasasında Nasıl Scalp Yapılır — Binary Forex Brokers

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 10/Baskı 10/Forex Piyasasında Nasıl Scalp Yapılır - Binary Forex Brokers (27 sayfa) - @eseckal.pdf>) · [Tam metin](03_scalp_binary_forex.txt)

**Sayfa haritası:** s. 1–4 giriş/içindekiler; 5–6 kısa oynaklık/haber/kaldıraç; 7–9 spread ve uygulama koşulları; 10–11 parite/likidite; 12–13 Forex seans saatleri; 14–16 scalp yaklaşımı ve haber sonrası örnek; 17–20 aralık, bayrak ve üçgen içindeki karşı yönlü kısa işlemler; 21–22 Fib uzatma seviyeleriyle trend scalpi; 23–27 risk/psikoloji/maliyet. S. 7, 12, 16–19, 21 görsel denetlendi.

**Karar:** S. 17–20 M15 bayrak/kutu içinde kenar yaklaşımından sonra **geri dönmeye başlayan** fiyata karşı yönlü scalp önerir; kırılım anında aynı işlemi taşımamayı söyler. Bu, mevcut [aralık scalpi](../batch_023/STRATEGIES.md) ve kutu/retest adaylarının kısa ömürlü varyantıdır. S. 21–22 ilk itki üzerinde %61,8/%100/%161,8 Fibonacci uzatma ve seviyeler arasında trendle işlem fikri vardır; pivot seçimi, giriş/stop/çıkış ve pozisyon süresi tanımlanmamıştır. Haber ilk şokunda bekleyip likidite geri geldikten sonra değerlendirme (s. 15–16) OHLCV'de haberin yayın saati ve gerçek spread olmadan sinyal olamaz. Forex'teki ET saatleri ve pip ölçeği kriptoya otomatik taşınmaz. Yeni bağımsız başlık açılmadı.

**Maliyet denetimi:** S. 7–8 yazarın örneğinde 30 işlem, 20×5 pip kazanç ve 10×3 pip kayıp brüt **+70 pip** eder; işlem başı 3 pip spreadle **−20 pip**, 1 pip spreadle **+40 pip** olmalıdır. PDF ikinci senaryo için **+60 pip** yazar; aritmetik hatası var (`100−30−30=40`). Bu yüzden maliyet analizi yazardaki nihai sayı kopyalanarak yapılmamalı. İleriki tüm M1/M5 scalp backtestlerinde sembol/zaman bazlı bid-ask, komisyon, kayma, gecikme, borsa min notional ve funding (uygunsa) ayrı tutulmalı; yalnız orta fiyat mumundan kâr hesaplanmamalı. Bir M1 mumunda stop ve TP birlikte görüldüyse stop önce. İstenen net hedef maliyetin altında kalıyorsa işlem atla; maliyet ölçütü ve eşik deney başlamadan dondurulmalı. Kitabın s. 26'daki kaldıraç artırma önerisi kanıtlanmış strateji kuralı olarak alınmaz.

**Parti sonucu:** 3 kitap tamamlandı; 0 yeni bağımsız aday. Mevcut strateji sayısı **330**. En somut yeni katkı, ikinci kitabın kimlik uyuşmazlığını ve üçüncü kitabın spread aritmetik hatasını açık kaydetmektir.
