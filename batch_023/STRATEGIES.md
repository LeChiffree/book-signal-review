# Kitap okuma 023 — retest teyidi, mikro sıkışma ve katlanan risk

**Kapsam:** 129 + 38 + 8 = **175 PDF sayfası**. Her PDF'nin sayfa sıralı metni aynı klasördedir; atıflar PDF sayfasıdır. Kaynak kuralları ile bizim nesnelleştirmemiz ayrılmıştır. Bu partide backtest, paper test veya emir yapılmadı.

## 1. Forex — Price Action Rehberi

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 5/Baskı 5/Forex - Price Action Rehberi (129 sayfa) - @eseckal.pdf>) · [Tam metin](01_forex_price_action.txt)

Kaynak temel OHLC/mum ve trend açıklamasından (s. 19–44) sonra, yüksek zaman dilimi S/R ile kırılmış seviyeye dönüşte ters mum aramayı (s. 45–49), kanal kenarı stop ve karşı kenar hedefini (s. 50–52), üçgende **önce çizgi dışı mum kapanışı**, sonra doğrudan kırılım veya retest girişini (s. 53–65) anlatır. Çift tepe/dip için erken ikinci pivot, boyun kırılımı veya retest alternatifleri s. 71–77; Fibonacci/S/R/mum kesişimi s. 94–98, 111–116; büyük zaman dilimi bölgesine küçük zaman diliminde giriş s. 117–124. Bunların çoğu batch 018–022 ile örtüşür; ayrı bağımsız başarı sayılmaz. Kaynak uzun kırılım mumunda stop uzaklığının artmasını ve retest beklemeyi özellikle tartışır (s. 57–59).

### PA23 — Uzun kırılım mumunda retest koşullu giriş

- **Kaynak:** Üçgen/boyun seviyesinin dışında **kapanış** bekle; aşırı uzun kırılım mumunu kovalamak yerine kırık çizginin yeniden testini bekle (s. 57–59, 64, 71–77). Hedef olarak üçgen yüksekliği veya sonraki S/R (s. 65, 77). Kitap “çok uzun” için nicel eşik vermez.
- **Bizim D1 deney:** K18b yatay aralık veya K18a boyun olayları aynı sinyal kümesi. Kırılım mumunun gerçek aralığı `>1.5 ATR14[t-1]` veya giriş fiyatından yapısal stopa uzaklık `>2 ATR` ise **retest koluna** yönlendir; diğerlerinde sonraki ilk 1m giriş. Retest kolunda sonraki 3 tam D1 barın ilkinde `low<=broken_level+0.2 ATR` ve `close>=broken_level` long, short simetrik; retest kapanışı sonrası ilk 1m giriş, stop retest ekstremumu `±0.1 ATR`, hedef formasyon yüksekliği veya 2R ayrı varyant, H7D zaman çıkışı. Retest olmazsa işlem yok. `1.5`, `2`, `3` bizim sabit deney eşiklerimizdir.
- **Karşılaştırma:** Bütün sinyallerde hemen giriş; bütün sinyallerde retest; yalnız uzun mumda retest. Dolmayan/kaçan girişler dahil **sinyal başına** net performans, işlem sayısı ve drawdown raporlanır. Bu T18a/KL20b ailesini geliştirir; çift kazanç sayılmaz.

## 2. Bob Volman — Price Action Scalping

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Price Action Scalping - Bob Volman (38 sayfa) - @eseckal.pdf>) · [Tam metin](02_volman_scalping.txt)

Bu PDF **kitabın tamamı değil, seçilmiş alıntılar**: önsöz ve 10, 11, 12, 14. bölümlerden örnekler (s. 1–38). Dolayısıyla 38 PDF sayfasının tamamı işlenmiştir, fakat tam Bob Volman kitabı okunduğu iddia edilmez. İçerik blok kırılımı (BB), aralık kırılımı (RB), aralık içi sıkışma (IRB), yanlış kırılım tuzağı ve devrilme noktası stop yönetimi (s. 5–38). Birkaç barın iki sınıra temas ettiği belirgin mini aralık (s. 5–8), trend/genel baskı ve kırılım öncesi **birikme/sıkışma** önemlidir (s. 10–12, 18, 26–28). Yuvarlak EUR/USD 20 pip çizgileri kişisel bağlamdır, kriptoya taşınmaz (s. 24–25). Spread ve haber sıçraması kritik (s. 28–29). Kaynak alıntısı tüm koşulları sayısallaştırmadığından aşağıdaki kural bizim araştırma taslağımızdır.

### BV23 — Kırılım öncesi mini aralık/sıkışma filtresi

- **Bizim M5 hipotez:** Önceki 8–20 kapanmış M5 mumdan `R=max(high),S=min(low)`; `R−S<=1.5 ATR14_M5`, üst ve alt sınıra `0.15 ATR` içinde ikişer ayrı temas, son 5 mumun median aralığı önceki 10 mum median aralığının `<=0.8` katı. `close[t]>R+0.1 ATR[t-1]` ve `EMA20_M5[t]` yükseliyorsa long; short simetrik. İlk sonraki 1m giriş, stop sıkışma karşı kenarı, hedef 1.5R ve 2R ayrı, en geç 4 saat. Karşıt tarafta aynı mum kırılımı varsa işlem yok. Sayılar kaynaktan değil, sıkışmayı tekrarlanabilir kılmak için bizim sabit parametrelerimiz.
- **Deney:** Aynı aralık kırılımı olaylarının “sıkışma var/yok” bölünmesi; haber, spread, likidite ve seans grupları ayrı. Batch 014 mekanik aralık/018 dikdörtgen adaylarıyla aynı olay ailesi. M5 scalp net ücretten sonra test edilir; günlük çok günlü modele doğrudan sinyal eklenmez. Sahte kırılım ve daha sonra aralığa dönüş, girişte **bilinen** filtre değildir; ancak sonuç etiketi olur.

## 3. John Carricaburu — Hedging Stratejisi

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 9/Baskı 9/Hedging Stratejisi - John Carricaburu (8 sayfa) - @eseckal.pdf>) · [Tam metin](03_hedging.txt)

Bu doküman tek strateji yerine **üç ters emir/pozisyon katlama varyantı** içerir (s. 1, 4–8). İlkinde karşı yön emirleri tekrarlandıkça lot dizisi `0.1, 0.3, 0.6, 1.2, ... 38.4` olur (s. 2–3); ikincisi `1,3,6,12,...` katlama ile kutu kırılımı (s. 4–5); üçüncüsü de kayıp sonrası artırmaya dayanır (s. 7–8). “Sonunda mutlaka kâr” iddiası maliyet, sonlu sermaye, marjin ve trendin izlediği yol nedeniyle geçerli değildir. Örneğin ilk dizide dokuzuncu pozisyon **ilk 0.1 lotun 384 katı**, ilk dokuz pozisyon toplamı **76.6 lot**; maliyet, maksimum marjin ve tasfiye riski buna göre büyür. Hedging etiketi ekonomik riski yok etmez.

### Karar: canlı/paper aday değil; yalnız risk karşı örneği

Bu kitap bir sinyal stratejisi olarak kuyruğa alınmadı. Kaydedilecek ölçülebilir hipotez: aynı Asya/aralık kırılımı girişleri için sabit nominal ve sabit toplam riskli tek pozisyonun, kayıptan sonra katlanan dizinin **maksimum öz sermaye gereği ve tail loss** ile karşılaştırılması. Böyle bir analiz ancak sonlu sermaye, gerçek spread/kayma, her bacak ücret/funding, çapraz/izole marjin, pozisyon netleme ve likidasyon çözümleyicisiyle anlamlıdır. Katlama için canlı veya paper emir önerisi yok; risk limiti aşılınca mekanik sonlandırma dizi mantığını değiştireceğinden “kesin” getiri varsayımı kullanılamaz.

## Test kararı

Öncelik PA23 koşullu retest deneyi: önceki kırılım adaylarını **aynı olaylarda** kıyaslar. BV23 ayrı M5 deneyinde sıkışma filtresi olarak incelenir. Carricaburu metni risk örneği ve karşılaştırma notu olarak kalır. Her uygulanabilir adayda kapanmış mum, 1m dolum, point-in-time evren, ücret/spread/kayma/funding, aynı 1m mumda stop önceliği ve zaman sıralı dış örneklem zorunludur.

