# Kitap okuma 116 — tek taraflı kırılım sonrası karşı sınır pususu

**Kapsam:** Üç ayrı PDF'nin **26 + 27 + 30 = 83 sayfası** baştan sona okundu. Atıflar PDF sayfasıdır. Backtest, paper test ve emir yapılmadı.

## 1. Trading Sistemi — Giovanni Del Toro

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 7/Baskı 7/Trading Sistemi - Giovanni Del Toro (26 sayfa) - @eseckal.pdf>) · [Tam metin](01_trading_system_del_toro.txt)

**Tam okuma:** S. 1–7 kapak, amaç ve risk; s. 8–13 araçlar, destek/direnç ve D1 tercih; s. 14–16 eğimi ile fiyatın SMA41 üstü/altı ve yükselen/düşen pivotlarla trend; s. 17–19 EMA15 ekleme ve trend içi geri çekilme; s. 20–23 geri çekilme `P.MIN/P.MAX` mumundan giriş, karşı pivotta stop ve eski trend ekstreminde hedef; s. 24–26 kısmi kâr/risk/genel sonuç. Kaynak short için P.MAX mumunun low altındaki emri “sell limit” diye adlandırır, ancak piyasa altındaki kırılma emri uygulamada sell-stop'tur. Long için P.MIN mumunun *açılışı* üstündeki alış fiyatını verir; short ile simetrik high üstü değildir. Pivotun ne zaman teyit edildiği ve EMA15'in sinyali nasıl filtrelediği belirtilmez. Bu çekirdek [27. partideki EMA trend geri çekilmesi](../batch_027/STRATEGIES.md) ve diğer trend/pivot devam adaylarıyla aynı hipotez ailesidir; SMA41/EMA15 sayısı ya da belirsiz P.MIN giriş fiyatı tek başına yeni aday sayılmadı. S. 25'teki sermayenin “%2/3'ü” ifadesi çeviri/birim bakımından belirsiz ve araştırma riski yapılmadı; 2–3R önerisi hedef pivotuna göre her olayda mümkün olmayabilir.

## 2. Super Scalper — Gavin Holmes

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 3/Baskı 3/Super Scalper - Gavin Holmes (27 sayfa) - @eseckal.pdf>) · [Tam metin](02_super_scalper_holmes.txt)

**Tam okuma:** S. 1–3 kapak/risk; s. 4–7 M1–M5 özel TradeGuider tarayıcısı ve VSA alarmı; s. 8–14 zaman dilimi hizası, tescilli “güç/zayıflık” işareti ve sonraki mumun sinyal mumu kapanışı üstü/altı teyidi; s. 15–17 önceki 200 M1 mumda aşırı hacim ve aynı fiyat civarına düşük hacimli dönüş; s. 18–19 risk, formülü verilmeyen avize stop; s. 20–27 Wyckoff/VSA arka planı, para yönetimi ve sinyal listeleri. [104. partideki Gavin Holmes Scalp](../batch_104/STRATEGIES.md) ile sistem ve örnek çekirdek büyük ölçüde aynıdır. Özel trend kutularının ve VSA işaretlerinin hesaplama formülü yok; yalnız “sonraki mum teyidi” bu gizli ana sinyali yeniden üretmez. Aşırı hacimden sonra düşük hacimli dönüş arşiv VSA adaylarında zaten bulunur. **Yeni bağımsız aday yok.** Hacim artışı kurumsal niyeti doğrudan ölçmez; FX tick hacmi borsa gerçekleşmiş hacmi değildir.

## 3. Forex Mum Çubuğu Pusu İşlemi — Long Hang Seng

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 19/Baskı 19/Forex Mum Çubuğu Pusu İşlemi - Long Hang Seng (30 sayfa) - @eseckal.pdf>) · [Tam metin](03_candle_ambush_seng.txt)

**Tam okuma:** S. 1–6 mum high/low ve kapanış anlatısı; s. 7–15 önceki mumun high/low düzeylerine iki stop emri, dolarsa o mum kapanışında çıkış ve dolmayan karşı emri iptal; s. 16–23 yalnız bir sınır kırılmışsa sonraki mum için **henüz kırılmamış karşı sınırda** pusu kurma; s. 24–29 EURUSD M5 örnekleri, kapanış çıkışı ve çoklu pozisyon/işlem sepeti; s. 30 tanıtım. S. 10–13 başarısız veya dolmayan örnekleri de gösterir; seçilmiş grafikler beklenen getiri kanıtı değildir. Kaynak çoklu pozisyonu sınırsız bırakır ve başlangıç stopu vermez, bu nedenle aşağıdaki ana aday tek pozisyon ve bizim tanımladığımız zorunlu stopla sınırlandı.

### LHS116A — Bir mum yalnız bir önceki sınırı aşınca karşı sınırdan dönüş

- **Kaynak (s. 16–26):** Referans mumun yüksek veya düşüğünden yalnız biri sonraki mumda kırıldıysa, henüz kırılmamış karşı düzeye takip eden mumda stop emri yerleştir. Üst sınırın önce kırılması → önceki alt sınırda short; alt sınırın önce kırılması → önceki üst sınırda long. S. 7–15'te yalnız çıplak iki yönlü kırılım da vardır, ancak bu adayın ayrışan bilgisi **ilk tek taraflı kırılım sonrası karşı tarafı beklemesidir**.
- **Kapalı mum deney sözleşmesi:** Ana evren EURUSD M5, ayrı D1 kolu USDJPY. Her iki bitmiş ardışık mum `a,b` için `U=high[a]`, `L=low[a]`; `b` kapanınca yalnız `high[b]>U ∧ low[b]>=L` ise `c` mumuna `L−1 pip` sell-stop; yalnız `low[b]<L ∧ high[b]<=U` ise `U+1 pip` buy-stop. `b` her iki sınırı kırmışsa veya hiçbirini kırmamışsa sinyal yok; `b` sıfır aralıklıysa atla. `b` kapanışı zaten hedef emir düzeyinin ters tarafındaysa emir geçmişe doldurulmaz, atlanır. Emir yalnız **hemen sonraki tek c mumu** boyunca geçerli; c kapanışında dolmadıysa iptal. Girişte short stop `max(high[a],high[b])+1 pip`, long stop `min(low[a],low[b])−1 pip` (**bizim** koruyucu stopumuz); pozisyon c kapanışında piyasa kotasyonundan kapanır (kaynak kapanış çıkışı). c içinde stopla giriş sırası tick veya bid/ask M1 ile doğrulanır; çözülmezse kötümser sıra. Tek açık işlem, en çok %0,5 özsermaye riski, spread/komisyon/kayma; c aynı zamanda yeni sinyal üretse de açık pozisyon kapanmadan ikinci pozisyon açılmaz (**bizim** çakışma kuralımız). Kaynak M5 ve günlük uygulamaya izin verir, fakat tek pazar/zaman dilimi seçimi ve 1 pip tampon bizim uygulama seçimidir.
- **Ayrışma/test:** [112. partideki çift doji OCO](../batch_112/STRATEGIES.md) ve standart önceki mum high/low kırılımıyla **aynı a,b evreninde** kıyasla. `b` tek taraf kırılımı olmadan çıplak OCO, `b` kırılan yönde devam ve burada kırılmayan karşı yönde dönüş kolları; dolum oranı, kısa vadeli ters hareket, maliyet sonrası net R, stop sıklığı ve M5/D1 ayrı sonuçları raporlanacak. `b` kapanmadan onun high/low bilgisini kullanarak `b` içinde karşı emir varmış gibi göstermek ileriye bakma hatasıdır.

## Sonuç

**1 yeni araştırma adayı:** LHS116A. Koruyucu stop ve birim normalizasyonu kaynakta verilmediği için bizim araştırma tanımı olarak işaretlendi; aday doğrulanmış strateji değildir.
