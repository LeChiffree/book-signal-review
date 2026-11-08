# Kitap okuma 009 — SMMA kanalı, H4 EMA5 dönüşü, üçgen kırılımı

**Kapsam:** Üç PDF'nin **11 + 20 + 30 = 61 PDF sayfası** işlendi. Sayfa numaraları PDF sayfasıdır. H4 EMA5 dosyasının s. 1–10 İngilizce, s. 11–20 Türkçe çeviridir; iki ayrı kitap veya iki bağımsız strateji sayılmadı. Kaynakta Forex pip, spread ve seans kuralları kripto fiyat ölçeğine doğrudan taşınmadı. Seçilmiş örnekler test sonucu değildir. Bu partide backtest/paper emir yapılmadı.

## 1. Russ Horn — Golden Strateji

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 9/Baskı 9/Golden Strateji - Russ Horn (11 sayfa) - @eseckal.pdf>)

Kaynak iki SMMA55'i sırasıyla `high` ve `low` üzerine, Williams %R(55) için `-25/-75`, Stochastic için `(5,5,5)` ayarlıyor (s. 2–6). Uzun için fiyat üst SMMA'nın üzerine, %R `-25` üstüne geçecek ve Stochastic ana çizgi sinyal üstünde olacak; kısa için alt kanal, `-75` ve ters Stochastic (s. 7–10). Kaynak agresif mum içi ve muhafazakâr mum kapanışı girişini ayırıyor; stop son swing ekstremumu, hedef 2R veya karşı SMMA geçişi. Başarı oranı iddiasının veri tablosu yok (s. 2).

### H9 — SMMA55 kanal kırılımı + %R55 + Stoch(5,5,5)

- **Kaynağa yakın kapalı olay:** `SMMA_high55` ve `SMMA_low55` Wilder/MT4 smoothed ortalama tanımıyla hesaplanır: ilk 55 değer SMA, sonrası `(prev×54 + x[t])/55`. `W%R55[t]=-100×(HH55[t]-close[t])/(HH55[t]-LL55[t])`; sıfır payda varsa sinyal yok. MT4 Stoch `(5,5,5)` low/high alanı, yavaşlatılmış K=SMA5(rawK5), D=SMA5(K,5). Long: `close[t-1]<=SMMA_high55[t-1]`, `close[t]>SMMA_high55[t]`, `W%R[t-1]<=-25`, `W%R[t]>-25`, `K[t]>D[t]`. Short alt kanal ve `-75` için simetri. Kitabın “fiyat geçti” şartını **kapanış geçişi** yapmak bizim nedensel yorumumuzdur; %R eşiğinin o mumda geçmesi kaynakta açık.
- **Yürütme:** t kapanışından sonraki ilk 1m giriş. Son önceden teyitli `k=2` swing dip altı `0.1 ATR14[t-1]` stop (short tepe üstü), pivot ancak iki sağ bar kapanınca bilinir. `k=2`/ATR tamponu bizim seçimimiz; kaynak “birkaç pip” der. 2R hedef veya günlük kapanışın ilgili SMMA içine dönüşü ayrı çıkışlar; 3/7/14 gün ufuk ayrıca. Aynı gün birden çok filtre tek olay. SMMA kanal kırılımı bazına %R ve Stoch ayrı ayrı eklenecek; üç fiyat türevi filtrenin marjinal katkısı bilinmiyor.
- **Kapsam:** Kitap M5 örnekleri de verse de ilk kapalı karar testi günlük olarak kaydedildi; M5/H4 ayrı kohort gerekir. Swing pivot stopunun çok uzak olduğu sinyaller için önceden sabitlenmiş azami stop/ATR kapısı gerekir.

## 2. Sterling — H4 EMA5 GBP Stratejisi

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 9/Baskı 9/H4 EMA5 GBP Stratejisi - İngilizce ve Türkçe (20 sayfa) - @eseckal.pdf>)

**Özgün sistem:** GBP/USD H4, high ve low'a uygulanmış ayrı EMA5. Mum `EMA5_low` altına en az 5 pip inerse **long** kurulumu, `EMA5_high` üstüne çıkarsa **short** kurulumu; ikisini aynı mumda aşarsa kurulum değil (s. 1–2, çeviri s. 11–12). Kurulum kapandıktan sonra long için mum tepesi `+5 pip+spread` buy stop ve mum dibi `-5 pip` koşullu stop; short simetrik. Sonraki mum daha uç kurulum yaparsa emir güncellenir, emir dolmaz ve yeni uç da yoksa başarısız dönüş barı sayılır; **iki ardışık** başarısız bardan sonra kurulum silinir (s. 2, 8–9). Dolum barı ters yönde daha aşırıysa bar kapandığında stop o yeni uca çekilir. Dolum barı kapandıktan sonra stop seviyesinde ters yön emri açılır; stopla ters pozisyon açılmışsa yeni geçerli kurulum çıkmadıkça ikinci ters emir kurulmaz (s. 3–8). 150 pip veya üstü açık kâr sonrası iki başarısız bar durumunda maksimum açık kârın %50'sini koruma stopu; hafta sonu kapanış/yeniden açılış (s. 9–10). Belgenin kendisi asıl forum kurallarıyla çelişirse forumun geçerli olduğunu söylüyor (s. 10); bu PDF tek başına “tam orijinal sistem” kanıtı değildir.

### E9a — EMA5 kanal uç hareketi sonrası ters yönde stop giriş

- **Bizim kripto H4 olayımız:** Tamamlanmış t H4'te `low[t]<EMA5_low[t]-0.1×ATR14_H4[t-1]` ve `high[t]<EMA5_high[t]+0.1×ATR14_H4[t-1]` ise yalnız long kurulumu; short için `high[t]>EMA5_high[t]+0.1 ATR` ve `low[t]>EMA5_low[t]-0.1 ATR`. İki dış sınırın da aşılması halinde sinyal yok. `0.1 ATR` Forex 5 pip yerine **bizim ölçek parametremiz**. EMA t değerleri t kapanınca sabittir; mum içi çizginin son değerini geçmiş fiyat sırasına uygulama.
- **Emir/durum:** t sonunda `buy_stop=high[t]+1 tick`, koşullu zarar stopu `low[t]-1 tick`; short ters. Sonraki H4 için 1m fiyat yolu kullan: dolmadan daha düşük dip oluşup bar kapanırsa yeni long kurulumuysa stop emrini yeni bar high'ına/stopunu low'una güncelle; dolmaz ve yeni dip yapmazsa başarısız bar sayacı +1; iki ardışık başarısız H4 sonunda iptal. Short yeni yüksek için simetri. `1 tick` giriş tamponu kaynak 5 pip değil, bizim borsa uyarlamamız; stop/girişte spread gerçek bid/ask ve ücret üzerinden değerlendirilir.
- **Temel çıkış:** İlk sürümde giriş barı yeni dip yapmışsa bar kapanınca stop daha kötü uca **yalnız o anda** güncellenir; bu stopu gevşetme riskini açıkça raporla. Sonraki H4 kapalı barlarda yeni ters kurulum varsa, stop seviyesinde ters yön stop emri bir varyant; tam s. 3–8 durum makinesi, bir stopla yön değiştirildiyse ikinci otomatik ters emir kurmama istisnasıyla kodlanmalıdır. Sade karşılaştırma olarak ters emir **olmadan** yalnız ilk giriş + ilk stop, 2R ve 3/7 gün çıkışı ayrı test edilir. Sade sürüm özgün sistem diye etiketlenmez.
- **Sınır:** Hafta sonu kuralı Forex seans boşluğuna özgü; 24/7 kriptoda uygulanmaz. `150 pip` sonrası %50 açık kâr koruma kuralı kaynakta var; kriptoya ancak önceden seçilmiş `k×ATR` eşiğiyle **adaptasyon** olur. Başlangıç testinde eşik etkisi ayrı ablation. H4 kararları günlük adaylarla aynı örneklem sayılmaz.

## 3. Trading Strategy Guides — Gelişmiş Sniper Trading Stratejisi

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 9/Baskı 9/Gelişmiş Sniper Trading Stratejisi - Trading Strategy Guides (30 sayfa) - @eseckal.pdf>)

Kitap simetrik, yükselen, alçalan üçgenlerin destek/direnç temaslarıyla çizimini (s. 2–6, 12–14), çizgi kırılımında yönü (s. 15–16), daha düşük zaman diliminde fiyatın yerleşmesini beklemeyi (s. 16–17), sabit pip stop veya üçgen yüksekliği kadar hedefi (s. 17–19) anlatıyor. “Advanced Triangle Builder” tescilli göstergesinin kodu ve geçmişte çizgileri ne zaman kesinleştirdiği verilmez (s. 7–8, 18–19); doğrudan replike edilemez. S. 20–29 tekil seçilmiş örneklerdir. “Konsolidasyon başladığında çık” sayısal değil. S. 29 kural özeti görsel/çok kısa, ek eşik vermez. Bu fikir batch 003 grafik formasyonları ve batch 007 Action Forex üçgen kırılımıyla **aynı ailede**; yeni keşif kanıtı sayılmadı.

### TR9 — Teyitli pivotlardan çizilen üçgenin kapanış kırılımı

- **Bizim nedensel tanım:** Günlük `k=2` ile teyitli pivot high/low; her iki tarafta en az iki teyitli temas. Son 30 kapalı günde high pivotlarına ve low pivotlarına ayrı doğrusal çizgi, yalnız pivot teyit zamanından sonra hesaplanır. İlk high çizgi eğimi `<=0`, low çizgi eğimi `>=0`, çizgiler arası genişlik başlangıçta `>=2 ATR14` ve karar gününe kadar daralmış olmalı. Çizgilerin t için öngördüğü üst/alt sınır **t-1 kapanışında dondurulur**. t kapanışı üst sınır `+0.1 ATR` üstünde ise long, alt sınır `-0.1 ATR` altında short. `k=2`, 30 gün, ATR eşikleri, regresyon/temas toleransı bizim kurallarımız; kaynak elle çiziyor. Simetrik/yükselen/alçalan türleri ayrı etiket.
- **Giriş/çıkış:** Kırılım t kapanışı sonrası ilk 1m; stop üçgen karşı sınırı (veya kırılım mumu karşı ucu ayrı), hedef t-1 itibarıyla dondurulmuş `max(upper-lower)` başlangıç yüksekliğinin kırılım fiyatından projeksiyonu (kaynak s. 18–19). Ayrıca 2R ve 3/7/14 gün çıkış. Fiyatın “yerleşmesi” için kırılımdan sonra ilk retest + sınır üstü/altı kapanış varyantı; kaynakta bekleme süresi yok, en fazla 3 gün bizim tercih. Dolmayan retest sinyalleri saklanır.
- **Kontrol:** Aynı günlük Donchian/bant kırılımı ve önceki G2/V2 daralan aralık bazları; üçgen çiziminin ekstra katkısı yoksa ayrı strateji sayma. Üçgen tamamlanmadan sonra seçilen pivot/çizgi ve t gününü regresyona katmak yasak.

## Ortak test kaydı

1. **Öncelik:** E9a sade giriş ve H9 kanal kırılımı; E9a'nın tam ters emir durum makinesi ancak 1m yürütme/stop sıralaması güvenilir doğrulanınca. TR9 önceki üçgen adaylarına karşı ablation.
2. Her aday için sinyal kapanışı, emir yaratma/değiştirme/iptal, dolum, stop/ters emir, ücret/spread/kayma/funding, net R, MAE/MFE ve aday çakışması kalıcı kayıt olmalı. Çoklu parametre denemelerinde dış örneklem ve rejim ayrımı şart.
3. Bu dosya ileriki backtest/paper test için uygulanabilir hipotezleri kaydeder; üstünlük veya kârlılık doğrulanmadı.
