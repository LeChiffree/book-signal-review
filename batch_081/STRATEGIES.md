# Kitap okuma 081 — Pazartesi aralığı likidite baskını

**Kapsam:** Üç PDF'nin gerçek **80 + 28 + 83 = 191 sayfası** sayfa sırasıyla tarandı; kritik şemalar [görsel olarak](figure_contacts/) incelendi. Atıflar PDF sayfasıdır. Kaynakta bulunmayan eşikler ve çıkışlar **bizim araştırma seçimimizdir**. Backtest, paper test veya emir yapılmadı.

## 1. Price Action Stratejileri — Alpha FX

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 6/Baskı 6/Price Action Stratejileri - Alpha FX (80 sayfa) - @eseckal.pdf>) · [Tam metin](01_alpha_fx.txt)

**Kaynak taraması:** S. 1–18 fiyat yapısı ve Dow tepe/dipleri; s. 19–25 temiz ile fitilli/gürültülü yapı ayrımı; s. 26–42 D1'den H4/H1'e seviye ve pin/yutan mumla teyit; s. 44–55 trend çizgisi ve sahte kırılım; s. 56–62 yatay destek/direnç; s. 64–69 günlük seviye, sahte kırılım ve dönüş mumu birleşimi; s. 70–74 ana trende karşı düzeltme; s. 75–80 risk ve kademeli kâr alma. Üç teyidin bir araya gelmesi önceki [sahte kırılım](../batch_005/STRATEGIES.md) ve [pin + seviye](../batch_049/STRATEGIES.md) adaylarına koşul ekler. Grafiklerdeki “temiz yapı” ve çizgi seçimi tek anlamlı mekanik kural değildir. 33/33/33 veya 50/25/25 kademeli çıkış, önceki adaylara uygulanabilecek **çıkış karşılaştırmasıdır**; ayrı yön sinyali olarak sayılmadı. İlk üç hedef seviyesi işlemden önce dondurulmalı; oluşmamış sonraki pivot hedef diye alınamaz.

## 2. Supply and Demand Kılavuzu

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 6/Baskı 6/Supply and Demand Kılavuzu (28 sayfa) - @eseckal.pdf>) · [Tam metin](02_supply_demand_guide.txt)

**Kaynak taraması:** S. 1–7 denge/dengesizlik ve geniş gövdeli ERC ile bölgeden çıkış; s. 8–14 düşüş–taban–ralli ve ralli–taban–düşüşü devam yapılarına tercih, tabanda altıdan az mum, distal fitil/proksimal gövde ve ilk retest; s. 15–18 karşıt arz/talep arasında eğri ve alt/üst yarı; s. 18–23 çıkış gücü, tabanda süre, tazelik ve en az 1:2 ödül/risk ile puanlama; s. 24–26 aylık/haftalık/günlük bölge çakışması; s. 27–28 ilgili yazılar/boş sayfa. S. 18, 10/10 için limit, 8–9 için teyitli piyasa emri ve 8 altı için işlem yok önerir; alt puanların tam matematiksel tarifi verilmez. Aynı temel ve puanlama başka bir [5. parti kitabında](../batch_005/STRATEGIES.md) zaten işlenmişti; [ilk taze retest](../batch_072/STRATEGIES.md) de kayıtlı. Bu PDF yeni bağımsız yön sinyali sağlamaz. İleride aynı olay evreninde kısa taban, güçlü ERC, ilk/ikinci retest ve eğri konumunun ayrı katkıları ölçülebilir; puan iddiası kanıt sayılmaz.

## 3. Teknik Analiz Kursu — Rekt Proof

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 6/Baskı 6/Teknik Analiz Kursu - Rekt Proof (83 sayfa) - @eseckal.pdf>) · [Tam metin](03_rekt_proof.txt)

**Kaynak taraması:** S. 1–14 emir bloğu ve piyasa yapısı; s. 15–23 breaker; s. 24–35 aralık ve sapma; s. 37–41 FVG; s. 43–60 birleşik kurulumlar; s. 61–67 **Pazartesi yüksek/düşüğü, haftanın geri kalanında ilk baskın ve karşı uç**; s. 68–76 profil/POC; s. 77–83 üç aşamalı birikim–manipülasyon–genişleme. İlk konular önceki sahte kırılım, breaker, FVG ve Wyckoff/PO3 adaylarıyla örtüşür. Profilin görsel örnekleri, yalnız günlük OHLCV ile emir yoğunluğu ölçüldüğü anlamına gelmez. Kaynak s. 61'de bu bölümü tek başına giriş yöntemi olarak sunmadığını söyler; aşağıdaki kural açıkça **bizim mekanik vekilimizdir**.

### RP81 — Pazartesi aralığının hafta içi ilk süpürülüp içine kapanması

- **Kaynak fikri:** Pazartesi kapanınca o günün yüksek/düşüğünü sabitle; hafta içi bu uçların likidite baskınını izle. S. 62 yalnız mevcut ve bir önceki haftayı dikkate alır. S. 63'te Pazartesi dibinin süpürülmesinden sonra üst uca hareket; s. 64–65'te Salı üst ucunun alınmasından sonra alt uç ve H1 breaker örneği vardır. Bu örnekler başarı oranı değildir.
- **Bizim kapalı mum olayı:** Kripto UTC haftasında Pazartesi `00:00–23:59:59` D1 mumu tam kapanınca `M_H/M_L` dondur. Salı–Cuma her günün tamamlanmış D1 mumunda, o hafta **ilk kez** `high > M_H + 0,1×ATR14_D[t−1]` ve `close < M_H` ise short; `low < M_L − 0,1×ATR` ve `close > M_L` ise long. Aynı gün iki uç da aşılırsa ve yön belirsizse işlem yok. İlk uç baskınından sonraki tekrarları o hafta yeni olay sayma. Bu, kaynakta anlatılan intraday H1 breaker girişini günlük kapanışa çevirdiğimiz **daha geç teyitli** sürümdür; kaynak bu eşikleri vermez.
- **İcra/risk:** Karar tam D1 kapanışında; sonraki ilk uygulanabilir 1m'de giriş. Short stop olay gününün `high + 0,1×ATR14_D[t−1]`, long stop `low − 0,1×ATR`; pozitif risk yoksa atla. Öncelikli hedef Pazartesi aralığı orta noktası; hedef girişin doğru tarafında değilse sinyalin bu kolunu atla. Karşı Pazartesi ucu ve sabit 2R ayrı hedef kolları; en geç haftanın UTC pazar kapanışı veya H7D, hangisi önceyse. Maliyet, funding, kayma, aynı 1m'de stop önceliği ve dolmayan emir raporu sözleşmeye göre.
- **Karşılaştırma:** [Genel sahte kırılım](../batch_005/STRATEGIES.md) ve [haftalık yapı](../batch_011/STRATEGIES.md) ile olay örtüşmesi. Aynı formülü Pazartesi aralığı, önceki gün aralığı ve önceki tam hafta aralığı üzerinde karşılaştır; yalnız Pazartesi sonrasında bakıldığı için gün/volatilite etkisini eşleştir. Günlük kapanışı beklemek sinyali seyreltiyorsa H1 kapanış varyantını **ayrı ön kayıt** olarak tasarla; geriye dönük başarılı örnek seçme.

## Ortak doğrulama

Bu partide **bir yeni araştırma başlığı** açıldı; kârlılık doğrulanmadı. [Çok günlü sözleşme](../../../research_v2/24_MULTIDAY_STRATEGY_CONTRACT.md) uyarınca yalnız geçmişte tamamlanmış UTC D1/H4/H1, karar sonrası ilk uygulanabilir 1m, point-in-time evren, veri boşluğu, ücret/kayma/funding, stop önceliği ve dış örneklem geçerlidir. Eşdeğer özellikler yeni sütun diye çoğaltılmaz.
