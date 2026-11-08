# Kitap okuma 022 — Fibonacci geri çekilmesi, çizgiye dönüş, EMA14/50

**Kapsam:** 93 + 114 + 28 = **235 PDF sayfası**. Sayfa sıralı tam metin dökümleri aynı klasörde saklanır; atıflar PDF sayfasıdır. Kaynağın iddiası ile bizim kripto test sözleşmemiz ayrılmıştır. Henüz bağımsız backtest, paper test veya emir yoktur.

## 1. Guillaume Alim Tremblay — Fibonacci Oranları Bir Yatırım Stratejisine Değer Katabilir Mi?

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 9/Baskı 9/Fibonacci Oranları Bir Yatırım Stratejisine Değer Katabilir Mi - Montreal Üniversitesi - Guillaume Alim Tremblay - Ekonomi Yönetimi Bilimi Yüksek Lisans Tezi - M. Justin Leroux Direktifinde (93 sayfa) - @eseckal.pdf>) · [Tam metin](01_fibonacci_thesis.txt)

Bu çalışma anlatı kitabından farklı olarak belirli Forex verisi üzerinde kural ailelerini karşılaştırır. Çift tepe/dip ve son üç mumun boyun seviyesini kıran kapanışı **DT1/DT2/DT3** olarak nesnelleştirir (s. 36–45); 23,6/38,2/50/61,8/78,6% geri çekilme girişlerini ve 1,618 ve daha büyük uzantı hedeflerini inceler (s. 30–31, 45–49). A/B pivot seçiminin ve trend tanımının öznel olmasının temel sorun olduğunu kendisi söyler (s. 31–35). Forex 2008–2011 verisinde 50% geri çekilme beklemenin hemen girişe kıyasla üç modelde getiri iyileştirdiği raporlanır (s. 16, 75–82). Fakat s. 69 maliyetleri dışarıda bıraktığını açıkça belirtir; parametre kombinasyonları çok sayıdadır ve mevcut sonuç kriptoya aktarılmaz. Tez sonuçları bağımsız tekrar edilmiş kanıt sayılmaz. S. 83–86 da sonuçların teknik analizin genel kârlılığını ispatlamadığını ifade eder.

### F22 — Aynı dönüş sinyalinde hemen giriş ile 50% geri çekilme limiti

- **Kaynak:** Onaylı dönüşten sonra `A` son üç mumun ekstremumu, `B` sinyal mumu karşı uç/son kapanışı; seçili `A–B` geri çekilme limitinde giriş, `A` stop, uzantı hedefi (s. 37–39, 45–49). Tezin asıl test ettiği soru sinyalin kendisi değil, **giriş fiyatını beklemenin marjinal değeri**.
- **Bizim D1 deney evreni:** Önceden tanımlı K18a/M18a çift dip/tepe sinyallerinin aynı karar zamanı ve sembolü. Sinyal kapanışında `A` ikinci dip/tepe ekstremumu, `B` boyun kırılımı kapanışı; A ve B sabitlenir. Long için `limit=B−0.5(B−A)`, stop `A−0.1 ATR14`; short simetrik. Limit en fazla sonraki 3 tam UTC gün aktif, dolmazsa **işlem yok**; sinyal hemen giriş kontrolü sonraki ilk 1m açılışı. Her iki kolun hedefi ortak `B+0.618(B−A)` (short ters), ayrıca 2R kontrol; H7D/H14D zaman çıkışı. 50% seviye, limit süresi, tampon ve hedef eşleştirme bizim ön tanımımızdır; tezde farklı uzantılar da denenmiştir. İlk 1m limit teması, bar içi stop/TP sırası ve ücret/kayma/funding gerçekçi çözülür.
- **Rapor gereği:** Sinyal başına limit dolum oranı, dolanlarda net R, **tüm sinyaller başına** net getiri, işlem sayısı ve kaçırılan kazanç birlikte verilir. Yalnız dolan limitlerin başarı oranını hemen girişle karşılaştırmak seçim yanlılığı doğurur. Oranlar için 50% ve basit rastgele/ATR tabanlı geri çekilme kontrolleri; çoklu deneme ve dış örneklem düzeltmesi gerekir.

## 2. Myronn Saremo — Trendline Stratejisi

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Trendline Stratejisi (114 sayfa) - @eseckal.pdf>) · [Tam metin](02_trendline_114.txt)

Bu kitap Kelvin Lee'nin batch 020 **çizgi kırılımı** yaklaşımından farklı olarak, iki onaylı salınımla çizilmiş eğimli çizgiye fiyatın **geri gelip tepki vermesini** işler. Büyükten küçüğe zaman dilimi bağlamı (s. 35–42), H1/H4 giriş (s. 43), çizgiye yakın kapanan mumun ekstremumu ötesine bekleyen emir ve son tepe/dip arkası stop (s. 44–45); çizgiye dokunur dokunmaz agresif giriş alternatifi (s. 46–51). Yakında karşıt çizgi ve olağan dışı büyük giriş mumu filtreleri (s. 53–56); trend çizgisi yanında yatay S/R kırılımı başka bir giriş varyantıdır (s. 62–64). S. 77–106 kâr artırma ve mum formasyonu örnekleri; %100 hesap artışı gibi pazarlama örnekleri bağımsız sonuç değildir. S. 107–114 özet/SSS.

### MS22 — Onaylı yükselen çizgiye temas sonrası mum tepesinin kırılımı

- **Kaynak:** En az iki daha yüksek salınım dibi ile yükselen çizgi; temas/yakınlık mumu çizginin belirgin altında kapanmasın; mum tepesinin biraz üzerinde buy stop; giriş çevresi dibinin altında stop (s. 44–45). Short simetriği s. 44. Çizgi yakınlığı ve pip ofseti Forex ölçeğindedir.
- **Bizim H4 olay tanımı:** Dört saatlik pivot dip, sağında iki **kapanmış H4** mum bulunan ve iki yandaki ikişer mumun düşüğünden düşük ekstremum. O anda bilinen son iki yükselen pivot `(i1,l1),(i2,l2)` ile çizgi `L(t)=l2+(l2−l1)(t−i2)/(i2−i1)`; çizgi sinyal mumu başlamadan dondurulur. Tamamlanan H4 `low[t] <=L(t)+0.2 ATR14_H4`, `close[t]>=L(t)−0.1 ATR` ve `high-low<=2 ATR` ise sonraki 2 H4 boyunca `high[t]+1 tick` buy stop. Dolumda stop `min(low[t],L(t))−0.1 ATR`, hedef 2R, H3D/H7D zaman çıkışları. Olaydan önce bilinen karşıt D1 direnç girişten <1R uzakta ise işlem yok. Short simetrik ve uygun perp evreni. Parametreler bizim kodlama kararlarımızdır.
- **Ablation:** Temasta ilk 1m giriş (agresif) ile mum zirve kırılımı (teyitli) aynı kaynak olayında karşılaştırılır. Kelvin Lee KL20a **çizgi kırılımı** farklı olaydır; iki hipotezin yönü ve kesişimi açık etiketlenir. H4 çizgi/stop tam mum kapanışı öncesi yeniden hesaplanmaz. Mevcut çok günlü günlük karar hattına H4 sinyali gizlice sokulmaz; ayrı H4 karar deneyi veya yalnız D1 kapanışında son altı H4 özet özelliği.

## 3. Waqar — EMA14 ve EMA50 Scalping Stratejisi

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 9/Baskı 9/EMA14 ve EMA50 Scalping Stratejisi - Waqar - Türkçe ve İngilizce (28 sayfa) - @eseckal.pdf>) · [Tam metin](03_ema14_50.txt)

PDF'nin s. 1–14 Türkçe, s. 15–28 **aynı içeriğin İngilizce tekrarıdır**; iki bağımsız strateji/deney değildir. EMA14'ün EMA50'yi yukarı/aşağı kesmesi ana kural (s. 1–3, 15–17). Kaynak M15 başlangıcı, H1'de daha uzun hamleler (s. 4, 10–13), sıkışık ve birbirine dolanmış ortalamalardan kaçınma (s. 5–6), önceden al/sat stop emri fikri (s. 5, 9) ve EMA14/50 altında/üstünde kapanışla takip ederken çıkış önerir (s. 11–13). Kısa vadeli pip hedefler Forex'e aittir; standart stop mesafesi ve kesin çıkış algoritması belirsizdir.

### W22 — M15 EMA14/50 kesişimi, sıkışma filtresi

- **Bizim intraday sözleşme:** Önceki tamamlanmış M15 `EMA14[t-1]<=EMA50[t-1]`, son tamamlanmış M15 `EMA14[t]>EMA50[t]` ve `close[t]>EMA14[t]` long; short simetrik. “Temiz kesişim” için son 8 M15 barın `median(abs(EMA14−EMA50))/ATR14_M15>=0.15` varyantı, kesişim anındaki fark değil **önceki mesafe** kullanır. Giriş sinyal mumu kapandıktan sonraki ilk 1m; stop son 8 M15 mumun düşüğü `−0.1 ATR`, hedef 2R veya sonraki kapanmış M15 EMA14 karşı tarafı, en geç 24 saat. Short perp/funding ile. `0.15`, 8 bar, 2R bizim deney eşiklerimizdir.
- **Örtüşme:** EMA kesişimi eski batch 001 EMA20/004 trend/019 EMA aileleriyle aynı temel bilgi olabilir. Temiz kesişim filtresi baz çapraza karşı eşlenmiş olaylarla ve maliyet sonrası getiride ablation. M15 sinyal D1 çok günlü karar modeline eşdeğer değildir; gerekiyorsa yalnız D1'de tamamlanmış intraday özetle temsil edilir.

## Deney kararı

Öncelik **F22'nin limit dolumu dahil aynı olayda giriş fiyatı karşılaştırmasıdır**; akademik kaynak ve gerçek yanlılık riski nedeniyle en öğretici testtir. MS22 ayrı H4 çizgiye tepki testi; W22 M15 stratejisi yüksek işlem maliyetine duyarlı intraday kontrol. Hepsinde point-in-time evren, kapanmış mum, uygulanabilir 1m dolum, stop/TP aynı 1m mumdaysa stop önceliği, ücret, spread, kayma, funding, olay çakışması ve zaman sıralı dış örneklem gerekir.
