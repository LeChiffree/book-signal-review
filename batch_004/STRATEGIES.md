# Kitap okuma 004 — Ichimoku, kripto teknik rehberi, H4 trend

**Kapsam:** Üç PDF'nin 67 + 75 + 13 = **155 PDF sayfasının** metni sayfa sayfa çıkarılıp incelendi. Boş/kapak/ayraç sayfaları strateji içermez. PDF sayfaları kaynak numarasıdır. Bu dosya kârlılık iddiası değil, backtest ve paper test için aday işlem sözleşmesidir.

## 1. Ichimoku Sisteminin Kazançlı Sinyalleri ile Nasıl Trade Yapılır — Sofia Stavropoulou

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 9/Baskı 9/Ichimoku Sisteminin Kazançlı Sinyalleri ile Nasıl Trade Yapılır - Sofia Stavropoulou - Kiss Forex (67 sayfa) - @eseckal.pdf>)

Kitap Tenkan(9), Kijun(26), Senkou A ve Senkou B(52) tanımlarını (s. 7–12), altı sinyal türünü (s. 29–39) ve H1/H4 teyitli M15 girişini (s. 62–63) veriyor. Bunlar seçilmiş Forex grafikleri ve yazar yorumu; sistematik performans tablosu yok. “Neredeyse garanti” ve “%80 kârlı” gibi anlatımlar (s. 4, 29) kanıt olarak alınmadı. Kaynağın %3–5 sermaye riski ve “sıfır risk” kaldıraç ifadesi (s. 62) uygulanacak risk kuralı değildir.

**Zaman hizalama şartı:** `Tenkan_t=(HH9_t+LL9_t)/2`, `Kijun_t=(HH26_t+LL26_t)/2`, `rawA_t=(Tenkan_t+Kijun_t)/2`, `rawB_t=(HH52_t+LL52_t)/2`. Grafikte **t konumunda çizilen** bulut `rawA[t-26]`, `rawB[t-26]` değeridir. **t anında hesaplanan ve t+26 konumunda çizilen** `rawA_t/rawB_t` yalnız mevcut veriden çıkar, fakat gelecekte oluşacak bulut/fiyat sonucu diye yorumlanamaz. Chikou'nun t-26 konumuna çizilmesi, karar t için `close_t` ile `high/low[t-26]` karşılaştırmasıdır; gelecekten veri çekilmez. Kütüphane çıktılarında ileri kaydırılmış satırların karar anına yanlış hizalanması başlıca sızıntı riskidir (s. 9–12, 34–37).

### I1 — Günlük bulut kırılımı

- **Kitap:** Fiyat bulut üstüne/altına çıktığında yönlü sinyal; bulut içinde işlem nötr (s. 6, 29, 38–39). Giriş mum kapandıktan sonra; stop karşı bulut sınırı, çıkış ters bulut geçişi veya takip eden stop (s. 38–39).
- **Kapalı günlük olay:** `close[t-1] <= max(cloudA[t-1],cloudB[t-1])` ve `close[t] > max(cloudA[t],cloudB[t])`; short simetri. `cloudA[t]=rawA[t-26]`, `cloudB[t]=rawB[t-26]`. Bulut genişliği/ATR14 ve fiyatın sınırdan ATR uzaklığı ölçülür.
- **Yürütme:** UTC günlük kapanışından sonra ilk yürütülebilir 1m açılışı. Başlangıç stopu karşı bulut sınırı; çok geniş stoplar için önceden sabitlenmiş azami ATR/pozisyon riski kapısı. Çıkış: günlük karşı bulut sınırı altında kapanış, ATR takip stopu veya H3D/H7D/H14D ayrı varyant. Bulutun düz kenarı ve Chikou teyidi **ablation**; zorunlu ana kural değil.
- **Karşılaştırma:** Aynı veri ve maliyetlerde Donchian20 kapanış kırılımı ile; “bulut” farklı bir temsil mi, ek katkı mı?

### I2 — Bulut rejiminde Tenkan/Kijun ve fiyat/Kijun kesişimleri

- **Kitap:** Tenkan Kijun'u yukarı kesince boğa; bulut üstündeki alış daha güçlü sayılır (s. 29–31). Fiyat Kijun üstüne kesince ayrı boğa sinyali (s. 32). Ters kesişim veya Kijun takip stopu çıkışı önerilir (s. 31–32).
- **Kapalı günlük olaylar:** `Tenkan[t-1]<=Kijun[t-1] && Tenkan[t]>Kijun[t]` (**I2a**); `close[t-1]<=Kijun[t-1] && close[t]>Kijun[t]` (**I2b**). Yalın ve `close_t>cloud_top_t` filtreli varyantlar ayrı. Short simetri. Chikou teyidi ayrıca `close_t>high[t-26]` gibi sayısal adaydır; bu eşik kaynakta verilmez.
- **Yürütme:** Sonraki 1m açılışı; sinyal mumunun düşüğü veya Kijun altı stop; ters kesişim, Kijun altı kapanış ve 3/7/14 gün çıkışı ayrı test. Aynı gün I1/I2a/I2b çakışması üç bağımsız işlem fırsatı sayılmaz; ortak olay kimliğiyle ablation yapılır.

### I3 — M15 karşı mumla trend devamı

- **Kitap:** M15, H1 ve H4 aynı yönde Ichimoku eğilimi; trend yönünün tersindeki M15 mum kapandıktan sonra giriş; EMA65/200 ve Chikou teyidi; Kijun stop, Tenkan/Kijun geçişiyle çıkış (s. 62–63).
- **Karar:** Kaynaktaki “%100 boğa/ayı”, “keskin bulut kenarı” sayısal değil. İlk sürümde **ertelendi**; denenecekse yalnız tamamlanmış M15/H1/H4 barlarıyla bulut ve EMA eğimi tanımlanmalı, emir sonraki 1m'ye konmalı. Günlük araştırma sözleşmesiyle aynı olay diye raporlanmaz.

## 2. Gelişmiş Kripto Trading Stratejileri — yazarı PDF'de belirtilmiyor

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 9/Baskı 9/Gelişmiş Kripto Trading Stratejileri (75 sayfa) - @eseckal.pdf>)

Kitabın s. 4–41'i kripto, eski coin/borsa/cüzdan listeleri; s. 42–57'si teknik analiz ve göstergeler; s. 58–67'si formasyonlar; s. 68–75'i türevler ve sonuç. Strateji başlığına rağmen eksiksiz, test edilmiş kripto işlem sistemi vermiyor. Fiyat, borsa ve araç anlatımı tarihsel bağlamdır; güncel seçim veya güvenilirlik tavsiyesi olarak kullanılmaz. EMA formülü s. 52'de çarpma/bölme açısından hatalı yazılmış görünüyor; uygulamada standart EMA tanımı kullanılıp bu kitabın formülü kopyalanmaz. RSI70/30 “al/sat” sözü (s. 54) trend rejiminde güvenilir kural sayılmaz.

### K1 — T‑30: EMA30 altına fitil ve yüksek hacim

- **Kitap:** “T‑30” fiyatın 30 günlük EMA altına kuyruk salması ve yüksek hacimle olası dönüş fikridir; 200 günlük ortalama bağlamı önerilir (s. 65–66). Giriş, teyit, stop ve hedef sayısal olarak tamamlanmamıştır.
- **Bizim kapalı günlük hipotez:** `low[t]<EMA30[t]`, `close[t]>EMA30[t]`, `lower_wick[t]>=2*body[t]`, `quote_volume[t]/median20[t-1]>=1.5`. Uzun rejim filtresi `close[t]>EMA200[t]` ayrı varyant. 2, 1.5 ve kapanışın EMA üstüne dönmesi **bizim kurallarımızdır**; kitabın “yüksek hacim” sözü bunları belirlemez. Aynı kitapta çekiç tanımı (s. 59–60) ve önceki partideki C2 ile örtüşme açıkça etiketlenir.
- **Yürütme:** Günlük kapanış sonrası ilk 1m; sinyal dibi altı veya 1 ATR stop; 1R/2R ve 3/7/14 gün çıkışı ayrı. C2 çekiç ve yalın EMA30 fitil olayına karşı ek katkı ölçülür. Eğer T‑30 aynı işlemleri verirse yeni strateji olarak sayılmaz.

### K2 — Göstergeler ve çizim formasyonları

- **Kaynak:** SMA kesişimleri ve hacim (s. 50), MACD/KDJ/Bollinger/RSI/Williams %R/stokastik (s. 52–56), mum desenleri (s. 59–61), çift/üçlü tepe ve baş omuz (s. 62–65).
- **Karar:** MACD, RSI, Bollinger, çekiç, yutan mum, çift dip ve bulut dışı çizim fikirleri önceki partilerde zaten kayıtlı. Yeni bağımsız strateji sayılmadı. KDJ'nin parametre/hesaplama anlatımı eksik; önce kesin `K,D,J` formülü ve karşılaştırma bazları gerek. Kitap s. 62'de sürekli kripto piyasasında klasik seans gaplerinin seyrek/uygunsuz olduğunu kendisi de belirtiyor; gap temelli desenler ertelendi. Üçlü tepe/dip için pivot teyidi ve tolerans yok, G1 genişletmesi olarak ancak daha sonra test edilebilir.

## 3. Kanıtlanmış Trading Stratejisi — Trend Trading — Adam Lemon

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 9/Baskı 9/Kanıtlanmış Trading Stratejisi - Trend Trading - Adam Lemon (13 sayfa) - @eseckal.pdf>)

Bu kitap, diğer ikisinden farklı olarak **tam bir H4 Forex emir kuralı** anlatıyor (s. 5–11). Trend tanımı 3 ve 6 ay önceki fiyata göre; H4'te trende ters güçlü mum; sonraki H4'te dönüş yönünde stop emri, tetiklenmezse veya önce geçersizleşirse iptal (s. 7–10). Forex'e özgü dört USD paritesi, Londra/NY saatleri ve 1 pip tampon kriptoya aynen taşınmaz. Yazarın 2010–2015, 628 varsayımsal işlem sonucu (s. 11–12) kendi Forex testidir; komisyon ve kayma dahil değildir, bağımsız doğrulama veya kripto sonucu değildir. Kitap s. 11'de 2R hedef derken daha büyük hedeflerin işlem başı beklentisi yüksek çıktığını da gösteriyor; hedef seçimi dış örneklemde dondurulmalı.

### T1 — Uzun trend içinde H4 aşırı ters mumundan dönüş emri

- **Özgün Forex kuralı:** Güncel fiyat 3 ve 6 ay önceki fiyattan yüksekse uzun trend. H4 mum önceki altı H4 mumun dibinin altında kapanır. Bu mumun tepesinin 1 pip üstüne buy stop, dibinin 1 pip altına zarar stopu; yalnız sonraki H4 içinde geçerli; girişten önce zarar stopu seviyesine değerse bekleyen emri iptal. Mum aralığı ATR30(H4)'ten küçük olamaz (s. 7–10). Short simetri. 2×ATR30 veya 2R hedef (s. 10–11).
- **Kripto uyarlaması, kapalı H4 olay:** `close_h4[t] > close_h4[t-540] && close_h4[t] > close_h4[t-1080]` (90/180 gün, 6 H4/gün; kitap takvim ayı der, 540/1080 bizim sabit yaklaşık karşılığımızdır); `close_h4[t]<min(low_h4[t-6:t-1])`; `high_t-low_t>=ATR30_h4[t-1]`. Karar yalnız H4 t kapanınca. Short için karşılaştırmalar ve mum yönü ters.
- **Emir ve iptal:** `entry=high_t+1 tick`, `invalidation=low_t-1 tick`; yalnız sonraki tamamlanacak H4 aralığında geçerli. Önce invalidation görüldüyse emri sil; önce entry görüldüyse giriş ve stop aktifleştir. 1m fiyat yolunda aynı dakika iki seviye görülürse sıralama belirsizdir: kötü senaryo veya işlemi belirsiz say; iyimser dolum yazma. Borsa tick ölçüsü emir anında bilinen symbol kuralından gelir. Forex 1 pip kopyalanmaz.
- **Çıkış:** İlk denemede `2R` ve `2*ATR30_h4` hedeflerini **ayrı** çalıştır; ayrıca 3/7/14 günlük zaman çıkışları. Aynı enstrümanda eşzamanlı sinyallerde kaynak s. 9–10 en çok iki pozisyon önerir; bizim ilk karşılaştırma bir açık pozisyonla sınırlanır, iki pozisyon ayrı varyanttır. Ücret, spread, kayma, funding ve emir dolmama oranı raporlanır.
- **Ablation:** 3/6 ay trend filtresi, güçlü H4 mum/ATR kapısı, yalnız bir sonraki H4'te geçerli emir, seans filtresiz kripto yürütmesi. Piyasa rejimi/BTC ile korelasyon ve bull/bear ayrımı sonucu ayrıca ölçülür. Bu sistem günlük karar deneylerinden ayrı H4 kohortudur.

## Öncelik ve kayıt kararı

| Aday | Durum | Neden |
|---|---|---|
| T1 H4 trend içi dönüş emri | **İlk backtest adayı** | Kaynakta tetik, emir ömrü, iptal, stop, hedef var; kripto uyarlaması açık. |
| I1 günlük bulut kırılımı | **İlk backtest adayı** | Objektif; ileri çizim hizalaması denetlenmeli. |
| I2 Tenkan/Kijun veya fiyat/Kijun | **Ablation adayı** | I1 ve mevcut trend özellikleriyle çakışabilir. |
| K1 T‑30 | **İkinci dalga adayı** | Kitapta eksik tanımlar çok; C2 ve EMA geri dönüşleriyle örtüşme olası. |
| I3 M15/H1/H4 yorumlu sistem, gap/üçlü tepe/KDJ | **Ertelendi** | Sayısal kural veya uygun veri/saat hizalaması eksik. |

**Ortak yürütme:** Karar yalnız tamamen kapanmış mumlardan üretilir. Giriş ancak karar sonrasındaki yürütülebilir 1m'de; emir zaman aşımı ve dolmayan emirler sonuç evreninden çıkarılıp sessizce unutulmaz. Backtestte eğitim/test zaman ayrımı, maliyetler ve çoklu deneme düzeltmesi gerekir. Bu partide backtest, paper emir veya canlı işlem yapılmadı. Mevcut özellik manifestinde eşdeğer Ichimoku/EMA/ATR/Donchian kolonları aranacak; aynı bilgi ikinci kez özellik diye eklenmeyecek.
