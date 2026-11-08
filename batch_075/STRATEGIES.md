# Kitap okuma 075 — ayrık MACD sapması, Wyckoff spring, kırılım dönüşü

**Kapsam:** Üç PDF'nin gerçek **46 + 14 + 69 = 129 sayfası** baştan sona okunup çıkarıldı; kuralı açıklayan grafikler [görsel olarak](figure_contacts/) incelendi. Sayfa atıfları PDF sayfasıdır. Kitaplarda bulunmayan sayısal eşikler **bizim araştırma parametrelerimizdir**. Backtest/paper/emir yapılmadı.

## 1. Uyumsuzluklar — Alexander Elder

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 6/Baskı 6/Uyumsuzluklar - Alexander Elder (46 sayfa) - @eseckal.pdf>) · [Tam metin](01_divergence_elder.txt)

**Kaynak taraması:** S. 5 standart 12/26/9 MACD histogramını tanımlar; s. 6–13 iki gösterge dibi/tepesi arasında **zorunlu sıfır çizgisi geçişi** olan gerçek uyumsuzluğu, geçişsiz veya aynı yükseklikteki “sahte” örneklerden ayırır. S. 18–23 giriş, son ekstrem dışı stop ve kanal hedefi; s. 24–27 bar kapanışını bekleme, başarısızlık ve üçüncü sapma; s. 28–34 sıfır merkezli diğer indikatörler ve çoklu zaman dilimi; s. 35–38 yarı otomatik tarama; s. 39–46 alıştırma çözümleri ve ekler. Seçilmiş örnekler başarı oranı kanıtı değildir. Kaynak, durdurulma ve yeniden giriş olasılığını da açıkça kabul eder.

### AE75 — Histogramın sıfırı geçtiği ayrık iki dip/tepe sapması

- **Kaynak kuralı:** Fiyat ikinci daha düşük dip yaparken MACD histogramı ikinci **daha sığ** negatif dip yapar; iki histogram dibi arasında histogram **sıfırın üstüne geçmiş** olmalıdır. İkinci histogram dip seviyesinden yükselmeye dönünce long. Short tam tersi: daha yüksek fiyat tepesine karşı daha alçak pozitif histogram tepesi ve arada sıfır altı (s. 6–13, 19–22, 38). İkinci tepeden dönüşte sıfırı tekrar geçmesi beklenmez.
- **Bizim kapalı mum tanımı:** `H=EMA12(close)−EMA26(close)−EMA9(EMA12−EMA26)`. Günlük long için `H<0` içindeki ilk yerel minimum, ardından en az bir kapanmış `H>0` bar, sonra yeniden `H<0` içindeki ikinci minimum. Histogram minimumları ancak izleyen **iki kapalı günlük barda** yükseliş görülünce onaylanır. İki minimum arası 5–60 gün; ikinci minimum `H2>H1+0,05×ATR14_D`; aynı ilgili fiyat pencerelerindeki ikinci low `<` birinci low `−0,1×ATR14_D`. İkinci minimumun onay gününde `H_t>H_{t-1}` ise sinyal. Short işaretleri ters. 2 bar, 5–60, 0,05 ve 0,1 **bizim seçimimizdir**. Fiyat minimumu ile histogram minimumu farklı günlerde olabilir; fiyat penceresi her histogram lobunun başlangıç/bitiş günleriyle önceden belirlenir.
- **İcra/risk:** Sinyal kapanışı sonrası ilk uygulanabilir 1m. Long stop ikinci fiyat lobu minimumu `−0,1×ATR`, short maksimumu `+0,1×ATR`; 2R veya geçmiş 20 günlük kanal karşı bandı hedef kolları, 7/14 gün süre. İlk net ödül-risk <1 ise atla; aynı 1m stop önce ve bütün maliyetler dahil.
- **Karşılaştırma:** Önceki MACD/fiyat uyumsuzluğu adaylarına göre **iki lob arasında gerçek sıfır geçişi** ek koşuldur. Geçişsiz klasik pivot diverjans, geçişli ama fiyat yeni ekstrem yapmayan kontrol ve AE75 aynı örneklemde karşılaştırılmalı; sinyal örtüşmesi yüksekse yeni kolon üretilmez. KM74 sıfırdan dönüşü ise fiyat diverjansı gerektirmez, ayrı hipotezdir.

## 2. Wyckoff Yöntemi

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 6/Baskı 6/Wyckoff Yöntemi (14 sayfa) - @eseckal.pdf>) · [Tam metin](02_wyckoff.txt)

**Kaynak taraması:** S. 1–3 arz/talep, “neden-sonuç” ve hacim çaba/fiyat sonucu; s. 4–6 döngü anlatısı; s. 7–9 SC/AR ile aralık, ST, olası spring, ardından LPS/SOS ve çıkış; s. 10–12 dağıtım/UTAD ve spring/UTAD'ın **zorunlu olmadığını** açıkça söyler; s. 13–14 trend, göreli güç ve zamanlama. Bu kısa metin özgün nokta-şekil hedefleri veya ayrıntılı alış/satış testlerini vermez. “Kompozit Adam” açıklaması gözlenen veri değil, modeldir.

### WY75 — Spring sonrası aralık içi toparlanma ve direnç üstü güç teyidi

- **Kaynak kuralı:** Önce düşüş sonunda SC/AR ile yatay aralık oluşur; alt sınırın altına geçip hızla geri dönme spring olabilir; yükseliş hacim/oynaklığıyla üst sınır kırılması SOS'tur (s. 7–9). Spring görülmemesi formasyonu kendiliğinden geçersiz kılmaz (s. 8, 12).
- **Bizim nesnel kurulum:** Son 20 kapalı günlük barda `close` yönlü düşmüş ve ilk 5 barda yüksek hacimli, geniş aralıklı düşük (SC vekili) olsun. O gün dahil sonraki 10–30 günlük kapalı barın dondurulmuş `range_low/range_high` sınırları, ilk 10 bar tamamlandıktan sonra belirlenir: low/high aşırı uçları; genişlik `1–5×ATR14_D`. Sonraki bar `low<range_low−0,1×ATR` ama `close>range_low` kapatırsa spring vekili. En çok 10 gün içinde `close>range_high+0,1×ATR` ve hacim önceki 20 günlük medyandan büyükse SOS long. Short için yükseliş sonrası UTAD/SOW simetrik. SC ölçüsü, pencereler, ATR ve hacim eşiği **bizimdir**; sınırı spring veya SOS gerçekleştikten sonra yeniden hesaplama.
- **İcra/risk:** SOS kapanışı sonrası ilk uygulanabilir 1m, long stop spring low `−0,1×ATR`, short UTAD high `+0,1×ATR`; 2R veya aralık yüksekliği kadar ölçülü hedef ve 7/14 günlük süre kolları. İlk net ödül-risk <1 ise atla; aynı 1m stop önce, maliyet/funding dahil.
- **Karşılaştırma:** Önceki spring/sahte kırılım, destek-direnç kırılımı ve yüksek hacim-dar fiyat adaylarıyla örtüşmeyi ölç. Asıl ek test **spring → aralık yeniden kazanımı → karşı sınır SOS** sıralamasıdır. Basit spring tek başına, SOS tek başına, spring+SOS ve spring olmadan SOS kontrolleri zorunlu; kaynak spring'i şart koşmadığı için son kol özellikle önemlidir. Faz A–E etiketleri gelecek fiyat görülmeden otomatik bilinemez; geçmişe dönük faz etiketini sinyale sızdırma.

## 3. Forex Day Trading — Gavin Wallace

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 6/Baskı 6/Forex Day Trading - Gavin Wallace (69 sayfa) - @eseckal.pdf>) · [Tam metin](03_day_trading_wallace.txt)

**Kaynak taraması:** S. 1–20 eğitim/psikoloji ve mum/EMA anlatımı; s. 21–29 5/8 EMA ile 34/55 EMA eğilimi, stop ve ters mumla çıkış; s. 29–32 Fibonacci geri çekilmesi; s. 33–42 döviz, korelasyon ve plan; s. 43–47 günlük yön, H4 34/55 EMA ve Asya seansı sınır kırılımı; s. 49–54 destek/direnç ile geri çekilme; s. 55–69 kırılım, FX haberleri ve seçilmiş blog örnekleri. Seans, pip, haber filtresi ve FX çift korelasyonları kripto 24/7 piyasasına otomatik taşınmaz. S. 54'te yazar Asya seansı kırılımının 2017 sonrası etkinliğinin azaldığını kendisi belirtir. Gösterilen 1:13 veya yüzlerce piplik işlemler performans dağılımı değildir.

### GW75 — Günlük kırılım ve ilk geri testte H4 EMA yön teyidi

- **Kaynak kuralı:** Destek/direnç dışında **kapanan** barı bekle, sonra ilk birkaç barda aynı seviyeye geri çekilme/tepkiyle giriş; H4 34/55 EMA ve günlük genel yön uyumunu izle (s. 43–47, 52–54, 59–63). Kaynaktaki Asya seansı sınırı FX'ye özgüdür.
- **Bizim günlük uyarlama:** Günlük karar öncesindeki 20 günün sabit yüksek/düşük sınırını dondur. Günlük `close>prior20_high+0,1×ATR14_D` long kırılım; short simetrik. Sonraki 1–5 **tam kapanmış** günlük barın ilkinde `low≤prior20_high+0,2×ATR`, `close>prior20_high` tepki ve son tamamlanmış H4'te `EMA34_H4>EMA55_H4` ile `close>EMA34_H4` ise long; short ters. 20 gün, 0,1/0,2 ATR ve 1–5 günlük pencere **bizimdir**; kaynağın seans içi erken girişine göre geç günlük vekildir. H4 barı günlük karar anından sonra kapanmışsa kullanma.
- **İcra/risk:** Teyit kapanışı sonrası ilk uygulanabilir 1m, long stop retest low `−0,1×ATR_D` (short high üstü), 2R veya kırılım yönünde aralık yüksekliği hedef kolları; 7/14 gün süre. İlk net ödül-risk <1 ise atla; aynı 1m stop önce, ücret/spread/kayma/funding dahil.
- **Karşılaştırma:** Var olan günlük 20 gün kırılımı, kırılım+retest ve EMA trend adaylarıyla aynı barlarda maliyet sonrası farkı ölç. Farklılık **H4 34/55 EMA filtresi + yalnız ilk geri test** birleşimidir; ilk dokunuş şartı FE72 ile de karşılaştırılmalı. FX haber/seans tetikleri için tarihsel takvim, bid/ask ve ayrı gün içi karar sözleşmesi olmadan strateji kaydı yapılmadı.

## Ortak doğrulama

Üçü de yalnız tam kapanmış UTC günlük/son tamamlanmış H4 verisiyle karar üretecek şekilde tasarlandı. Point-in-time likit sembol evreni, veri gecikmesi, eksik bar, sonraki uygulanabilir 1m dolum, maliyet/funding ve stop önce çözümü gerekir. Etiket örtüşmesi ve eşzamanlı işlemler zaman sıralı walk-forward/holdout'ta denetlenir. Mevcut yaklaşık 1.300 feature'da eşdeğerleri varsa sütun çoğaltılmaz. Burada doğrulanmış kârlılık iddiası yoktur.
