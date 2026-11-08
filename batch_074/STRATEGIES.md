# Kitap okuma 074 — çoklu salınım dönüşü, MACD reddi, iki kapanışlı çizgi kırılımı

**Kapsam:** Üç PDF'nin gerçek **41 + 24 + 36 = 101 sayfası** baştan sona metin olarak okundu. Kuralı taşıyan grafikler ve az metinli alıştırma sayfaları [görsel olarak](figure_contacts/) incelendi. Sayfa atıfları PDF sayfasıdır. Kitabın vermediği eşikler **bizim test parametrelerimizdir**. Backtest/paper/emir yoktur.

## 1. Bir Tersine Dönüşün Ne Zaman Gerçekleşeceğini Nasıl Belirleyebilirim

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 6/Baskı 6/Bir Tersine Dönüşün Ne Zaman Gerçekleşeceğini Nasıl Belirleyebilirim (41 sayfa) - @eseckal.pdf>) · [Tam metin](01_reversal_timing.txt)

**Kaynak taraması:** S. 3–6 birbirine yakın fiyatlarda en az iki dip/tepe ve arada belirgin karşı salınımı gösterir. S. 12–19 uzun trend sonunda karşı yön dönüşü ile geri çekilme sonunda trend devamını ayırır. S. 20–35 üst dilim dönüş alanında alt dilim aynı yapının veya güçlü ters mumun teyidini, son salınım dışı stopu ve önceki hareketin kaynağında kısmi çıkışı anlatır. S. 36–38 ilk karşı salınımın belirgin büyük olmasını ve alt zaman dilimi seçimini vurgular. S. 39–41 önceki konsolidasyon/dönüş yerlerini önerir. Kitabın banka emirlerini neden olarak anlatması OHLCV ile doğrulanmaz; çoklu salınım kârlılığına dair örneklem yoktur.

### RT74 — Uzamış trend sonunda yakın çift/üçlü dip-tepe ve büyük ilk tepki

- **Kaynak kuralı:** Uzun düşüş/yükselişten sonra yakın seviyelerde en az iki ters salınım, ilk karşı salınımın büyük olması ve alt dilim teyidi; stop en son salınımın dışında (s. 3–6, 19–27, 36–38). Kaynak günlük kripto için sayısal “uzun”, “yakın” ve “büyük” eşikleri vermez.
- **Bizim kapalı mum olayı:** Son 30 günlük yönlü getiri mutlak `≥3×ATR14_D/close` ve 20 kapanmış barın en az 14'ünde `EMA20_D` yönü aynıysa uzamış trend. Long için düşüşten sonra iki onaylı günlük pivot low: pivot ancak sağındaki 2 bar kapandığında bilinir; dipler arası 3–15 gün ve fiyat farkı `≤0,5×ATR14_D`. İlk dip sonrası aradaki yükseliş `≥1×ATR14_D` olmalı; ikinci dipten sonra `close>aradaki tepki high` kapandığında long. Short tam simetrik. 30/20/14, 3–15 gün ve ATR eşikleri **bizim seçimimizdir**. Bu günlük kapanış teyidi kaynak alt dilim erken girişinden farklıdır.
- **İcra/risk:** Teyit kapanışından sonraki ilk uygulanabilir 1m giriş; long stop iki dip minimumu `−0,1×ATR_D`, short iki tepe maksimumu `+0,1×ATR_D`; hedef 2R veya önceden onaylanmış son günlük konsolidasyon sınırı, 7/14 günlük süre kolları. Hedef lehte değil/net ilk ödül-risk <1 ise atla; aynı 1m stop önce. Önceki dipleri tanımlarken gelecekteki pivotları kullanma.
- **Ayrıştırma:** DS72 üçlü tepe/dip ile salınım sayısını, AB73 trend içi ikinci devam denemesi ile rejimi, önceki çift dip adaylarıyla **ilk tepki büyüklüğünü** karşılaştır. Eşdeğer olaysa ayrı strateji sayma; bu kaydın amacı büyük ilk tepki filtresinin ilave katkısını sınamaktır.

## 2. MACD — Karthik Marar

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 6/Baskı 6/MACD - Karthik Marar (24 sayfa) - @eseckal.pdf>) · [Tam metin](02_macd_marar.txt)

**Kaynak taraması:** S. 1–4 standart MACD geçişi, sıfır geçişi ve gecikme; s. 5–8 sinyal çizgisine yaklaşma, hook ve MACD'nin sıfır çizgisinden reddi (ZLR); s. 9–13 ADX/DMI ve Stochastic ile seçicilik; s. 14–18 haftalık MACD, günlük giriş ve histogram; s. 19–22 fiyat/MACD/histogram uyumsuzluğu ve teyit; s. 23 hacim ağırlıklı MACD deneme formülü; s. 24 avantaj/sınırlar. S. 18 mekanik sisteme dökmenin zor olduğunu açıkça kabul eder. Grafikler getiri kanıtı değildir.

### KM74 — Pozitif haftalık rejimde günlük MACD sıfır çizgisi reddi

- **Kaynak kuralı:** MACD sıfıra yaklaşıp aynı tarafta yönünü tekrar trend lehine çevirdiğinde ZLR; haftalık MACD sıfırın ve sinyalin üstündeyse günlük alım sinyalleri daha elverişli (s. 8, 14–18). Sıfıra ne kadar yaklaşılacağı kaynakta sayısal değildir.
- **Bizim ölçüm:** Günlük `MACD=EMA12(close)−EMA26(close)`, `signal=EMA9(MACD)`, histogram farkı. Long için son **tamamlanmış** UTC haftasının `MACD_w>0` ve `MACD_w>signal_w` olması; günlük MACD önceki 5 gün içinde pozitif kalırken en az bir kez `0<MACD_D≤0,25×ATR14_D` düzeyine inmiş olsun; bugünkü kapanışta `MACD_D>MACD_{D-1}`, `hist_D>hist_{D-1}` ve `hist_D>0`. Short simetrik. 5 gün, 0,25 ATR ve aynı bar histogram geçişi **bizim eşiklerimizdir**. Farklı fiyat ölçeklerinde MACD/ATR oranı kullanılır.
- **İcra/risk:** Günlük teyit sonrası ilk uygulanabilir 1m, stop son 10 kapanmış günlük low/high dışı `0,1×ATR_D`, hedef 2R veya 7/14 gün süre; hedef lehte değilse atla. Stop/TP aynı 1m'de stop önce, maliyet/funding dahil.
- **Karşılaştırma:** Basit MACD sıfır geçişi, sinyal çizgisi kesişimi ve haftalık filtreli MACD mevcut adaylarıyla aynı karar evreninde sinyal örtüşmesi/net R ölç. İlave bilgi **sıfırı geçmeden geri sekme** olayındadır. S. 19–22 histogram uyumsuzluğu önceki divergence adaylarıyla örtüştüğü için yeni bağımsız strateji yazılmadı; s. 23 hacim ağırlıklı varyant veri/normalizasyon tanımı sabitlenmeden ertelendi.

## 3. Trendline Trading Stratejisi — Rich Finegan

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 6/Baskı 6/Trendline Trading Stratejisi - Rich Finegan (36 sayfa) - @eseckal.pdf>) · [Tam metin](03_trendline_finegan.txt)

**Kaynak taraması:** S. 9–15 standart dışı `SAR(0,02,0)` grup uçlarından destek/direnç çizgileri kurar; s. 16–17 çizgi dışında ardışık iki kapanışla kırılım, s. 18 başarısız kırılımda bant içi işlem, s. 19–23 zaman dilimi/para yönetimi ve döviz seçimi; s. 24–33 çizim alıştırmaları, s. 34–36 soru-cevap. `SAR(0,02,0)` ifadesindeki maksimum ivme 0, standart SAR tanımı ve kütüphane uygulamaları açısından muğlaktır; kaynakla aynı sonuç verdiği gösterilmeden otomatik SAR çizgisi uydurulmaz. S. 20'deki %75 başarı örneği ölçülmüş sonuç değildir; %10 sermaye riski bizim risk kuralına taşınmaz.

### RF74 — Dondurulmuş iki pivot çizgisinin dışında iki günlük kapanış

- **Kaynak kuralı:** Önceden çizilmiş destek/direnç trend çizgisinin dışında art arda iki kapanıştan sonra kırılım yönü (s. 11–18). Kaynağın özgün çizim yöntemi SAR gruplarının uçlarını kullanır; aşağıdaki pivot çizgisi **araştırma vekilidir**.
- **Bizim nesnel çizgi:** Günlük grafikte sağında 2 kapanmış barla onaylanan son iki pivot high'tan direnç, son iki pivot low'dan destek çizgisi. Pivot arası 5–30 gün; her çizgiyi ikinci pivot ancak onaylandığı günde dondur. Çizgi, iki pivot `(t1,p1),(t2,p2)` üzerinden zamanla doğrusal uzatılır; karar gününde yalnız o gün önceden bilinen çizgi değeri kullanılır. Direnç üstünde ilk ve ikinci ardışık `close>line+0,1×ATR14_D` long, destek altında iki kapanış short. Çizgi ilk kırılımdan sonra yeniden çizilmez; 2 kapanış kuralı kaynaktan, pivot/ATR/pencere bizimdir.
- **İcra/risk:** İkinci kapanış sonrası ilk uygulanabilir 1m; long stop dondurulmuş çizgi altı `−0,3×ATR`, short üstü `+0,3×ATR`. 2R hedef/7 veya 14 günlük süre; ilk net ödül-risk <1 veya çizgi stopu yanlış taraftaysa atla. Aynı 1m stop önce, tüm maliyetler dahil.
- **Karşılaştırma ve sınır:** Aynı çizgide bir kapanış, iki kapanış ve kırılım+retest kollarını sinyal gecikmesi, sahte kırılım ve net R yönünden karşılaştır. Önceki trendline/pivot breakout adaylarıyla eşdeğerliği denetle. Kaynağın SAR çizgisiyle bire bir test için `SAR(0,02,0)` kütüphane bağımsız algoritmasının nasıl işleyeceği önce kaynak görsellerine karşı doğrulanmalıdır; bu vekil ona eşit sayılmaz. Bant içi salınımın s. 18'de mekanik giriş/çıkışı olmadığından ayrı aday yapılmadı.

## Ortak doğrulama

Üç aday günlük UTC karar saatinde yalnız kapanmış 1d/1w barlarla üretilebilir; haftalık özellik yalnız tamamlanmış haftadan gelir. Point-in-time evren, eksik bar ve source-close zamanı, sonraki uygulanabilir 1m giriş, ücret/spread/kayma/funding, 1m stop önceliği ve zaman sıralı walk-forward olmadan performans yorumu yapılmaz. Mevcut yaklaşık 1.300 kolonluk pilotta eşdeğeri varsa yeni kolon açılmaz. Bu sayfadaki kurallar araştırma hipotezidir; kârlılığı doğrulanmamıştır.
