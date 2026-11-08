# Kitap okuma 077 — Spartan 1-2-3 filtresi, RSI destekli başarısız kırılım

**Kapsam:** Üç PDF'nin gerçek **101 + 71 + 23 = 195 sayfası** sırayla okundu. Metni kısa olan Spartan alıştırma sayfaları, Stoxxme'nin bütün grafik sayfaları ve Grafik Okuma'nın kritik şekilleri [görsel olarak](figure_contacts/) incelendi. Atıflar PDF sayfasıdır. Aşağıdaki sayısal test eşikleri, açıkça kaynakta belirtilmedikçe **bizim ön kayıt seçimimizdir**. Backtest, paper test veya emir yapılmadı.

## 1. Spartan Trader Forex Sistemi — Nikos Mermigas

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 6/Baskı 6/Spartan Trader Forex Sistemi - Nikos Mermigas (101 sayfa) - @eseckal.pdf>) · [Tam metin](01_spartan_mermigas.txt)

**Kaynak taraması:** S. 10–17, 1-2-3 dip/tepe ve 2–3 trend çizgisi; s. 18 Heikin-Ashi; s. 19–20 EMA **12/36** kesişimi, EMA **200** yön filtresi ve EMA **633** destek/direnç; s. 25 dört işlem şartı; s. 26–27 2–3 kırılımı, renkli ilk mumun gövdesinin en az yarısının EMA12'nin doğru tarafında olması ve fitil aşımıyla emir; s. 29 stop ve FX hesap riski; s. 31–32 üç parçalı pozisyon ve EMA12 iz süren çıkış; s. 34 D1/H4→H1→M5 zaman dilimi sıralaması. S. 40–98 büyük ölçüde grafik alıştırmaları ve çözümleri; görsel örnekler performans kaydı değildir. S. 35'teki FX haber saati ve pip hedefleri kriptoya doğrudan taşınmaz.

### NM77 — Onaylı 1-2-3 dönüşü + EMA12/36 ve EMA200 bağlamı

- **Kaynak fikri:** Boğa 1-2-3'te 3 numaralı dip 1'den yüksek, ayıda 3 numaralı tepe 1'den düşüktür; kaynak, EMA12/36 kesişimi, destek/direnç ve seviye/2–3 çizgisi kırılımının aynı yönü göstermesini arar (s. 10–13, 19–20, 25–27). Bu dört şartın çizgileri takdire bağlıdır; aşağıdaki pivot-2 kırılımı çizgi yerine **araştırma vekilidir**, özgün M5 sisteminin bire bir kopyası değildir.
- **Bizim kapanmış veri olayı:** Her UTC günlük karar anında yalnız o ana dek tamamen kapanmış H4 mumları ve günlük mum kullanılır. H4 pivotu solda ve sağda **2'şer kapanmış H4 bar** ile onaylanır; eşit tepe/dip pivot sayılmaz. Long için sırayla pivot dip `P1`, pivot tepe `P2`, pivot dip `P3` oluşsun; `P3>P1+0,1×ATR14_H4`. `P3` sağdan teyit edildikten sonraki ilk kapanmış H4 `close>P2+0,1×ATR14_H4` olsun. Bu kırılım son 24 saatte gerçekleşmiş, son H4 `EMA12>EMA36` olmuş, EMA12'nin EMA36 üzerine kesişimi son **20 kapanmış H4** içinde görülmüş ve son H4 Heikin-Ashi mumu yükseliş renginde olup gövdesinin ≥%50'si EMA12 üzerinde olsun. Günlük `close_D>EMA200_D` de gerekli. Short tüm sıralama/eşikleri ters çevirir. HA `close=(O+H+L+C)/4`, `open=(önceki HA open+önceki HA close)/2` kronolojik hesaplanır. 2 sağ bar, 0,1 ATR, 20 H4, 24 saat ve günlük EMA200 kullanımı **bizim uyarlamamızdır**; kaynakta EMA uzunlukları ve ≥%50 gövde şartı vardır.
- **İcra/risk:** Sinyal oluşan günlük kararından sonraki ilk uygulanabilir 1m açılışında işlem; long stop `P3−0,1×ATR14_H4`, short simetri. 2R tam çıkış ile 1R'de yarı çıkıp kalanını kapanmış H4 EMA12'nin ötesine yalnız lehte sıkılaşan stopla izleme ayrı deney kolları. En geç H7D süre çıkışı. Stop geçersiz/çok uzaksa veya girişte net beklenen ödül-risk <1 ise işlem yok. Aynı 1m'de stop ve hedef birlikte görülürse stop önce; ücret, spread, kayma ve funding dahil.
- **Karşılaştırma:** Önceki [M26 1-2-3](../batch_026/STRATEGIES.md) ve EMA kesişim adaylarına karşı aynı sembol/tarihte yalın 1-2-3, yalın EMA, birleşim ve HA/günlük EMA200 filtreli birleşim kollarını ölç. Asıl yeni soru, dörtli teyidin maliyet ve gecikme sonrası ek değeridir. EMA633 yalnız kaynakta seviyeyle çakışma ipucu; mekanik sınır ve ısınma süresi belirlenmeden ek filtre değildir.

## 2. Price Action Kurulumları ve Örnekleri — Stoxxme

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 6/Baskı 6/Price Action Kurulumları ve Örnekleri - Stoxxme (71 sayfa) - @eseckal.pdf>) · [Tam metin](02_stoxxme_setups.txt)

**Kaynak taraması:** S. 3–8 kanal/kutu ve eski direncin desteğe dönüşü; s. 9–16 RSI uyumsuzluğu ve başarısız tepe/kırılım; s. 17–21 çift tepe; s. 22–24 15 dakikalık açılış aralığı; s. 25–35 destek süpürmesi, ters baş-omuz, retest ve yalancı kırılım; s. 36–58 üçgen ile diğer seviye senaryoları; s. 59–71 genel mum/formasyon özeti. Bunlar çizim açıklamalarıdır, işlem listesi veya test sonucu değildir. Hisse seansı açılış kuralı 24/7 kriptoda eşdeğer değildir. Tek başına kanal, üçgen, retest, RSI divergence veya sahte kırılım önceki kayıtlarda zaten vardır.

### SX77 — Eski direncin üstünde başarısız kapanış ve önceden doğrulanabilir RSI zayıflığı

- **Kaynak fikri:** Eski yüksek/direnç üstündeki kırılım kısa sürüp fiyat geri dönüyorsa, aynı bölgede RSI'ın daha düşük tepe yapması short dönüşünü destekleyebilir (s. 9–16, 33–35). Grafiğin sonradan görülen sağ tarafındaki tepeyi girişte biliniyor saymayız.
- **Bizim kapanmış veri olayı:** Önceki günlük fiyat tepesini sağda **2 kapanmış gün** ile onayla ve tepe günü `RSI14` değerini dondur. Tepe en çok **60 gün** eski olsun. Eski tepe `R` üstünde ilk günlük `close>R+0,1×ATR14_D` kırılımı gelsin; bu barın RSI14 değeri eski tepe günündeki RSI14'ten **≥3 puan düşük** olsun. En geç izleyen **3 kapanmış günlük bar** içinde `close<R` gelirse ilk geri dönüş kapanışında short sinyali. `R` kırılımdan sonra yeniden çizilmez; bu aralıkta daha yüksek yeni teyitli direnç seçilmez. 2 bar, 60/3 gün, 0,1 ATR ve 3 RSI puanı **bizim nesnel eşiklerimizdir**. Sinyal ancak aralığa geri kapanan günün sonunda bilinir.
- **İcra/risk:** Bir sonraki uygulanabilir 1m short; stop kırılım/geri dönüş penceresinin en yüksek fiyatı `+0,1×ATR_D`. Hedef, kırılım öncesindeki 20 tamamlanmış günlük aralığın orta noktası ile sabit 2R olarak **ayrı** kollar; hedef girişin lehinde değilse o kol atlanır. H7D süre çıkışı. Aynı 1m'de stop önce, ücret/kayma/funding dahil. Long için eski desteğin altında sahte kırılım ve RSI'ın daha yüksek dip yapması simetrik, fakat futures short ile sonuçları ayrı tutulur.
- **Karşılaştırma:** [S1](../batch_005/STRATEGIES.md), [G28b](../batch_028/STRATEGIES.md) ve [FP53](../batch_053/STRATEGIES.md) aynı sahte kırılım ailesidir. Aynı olaylarda RSI filtresiz sahte kırılım, yalnız RSI zayıflığı ve birleşimin net getirisi/sıklığı karşılaştırılır. Ayrı alpha varsayımı yok; mevcut RSI/pivot özellikleri eşdeğerse yeni sütun açılmaz.

## 3. Yeni Başlayanlar İçin Grafik Okuma Teknikleri

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 6/Baskı 6/Yeni Başlayanlar İçin Grafik Okuma Teknikleri (23 sayfa) - @eseckal.pdf>) · [Tam metin](03_chart_reading.txt)

**Kaynak taraması:** S. 1–6 mum, destek/direnç, trend çizgisi ve kanal; s. 7–15 baş-omuz, çift tepe/dip, gap, üçgen, bayrak ve mum şekilleri; s. 16–23 SMA/EMA, stokastik, CCI, RSI, momentum, Bollinger, MACD ve Fibonacci. PDF temel bir sözlük ve çizim derlemesidir. Kırılan direncin destek olarak yeniden sınanması (s. 2–3), formasyonlar (s. 7–15) ve indikatörler (s. 16–23) önceki partilerde ayrı aday olarak zaten kayıtlı; yeni bağımsız, yeterince tanımlı işlem kuralı çıkmadı. Gap örnekleri hisse seansına bağlıdır; kriptoda sürekli işlem akışına genellenmez. Bu kitap için sırf sayıyı yükseltmek amacıyla yeni strateji başlığı açılmadı.

## Ortak doğrulama ve kayıt sınırı

Karar yalnız kapanmış UTC günlük, son tamamlanmış H4 ve gerekiyorsa tamamlanmış haftalık veriden alınır. Pivotların sağ onay barları mutlaka karar zamanından önce kapanmış olmalı; aynı kaynağın çiziminde sonradan ortaya çıkan hareket girişte kullanılmaz. Point-in-time evren, veri boşluğu, 1m dolum, ücret/spread/kayma/funding ve aynı 1m stop önceliği [günlük sözleşmeye](../../../research_v2/24_MULTIDAY_STRATEGY_CONTRACT.md) uygun uygulanır. İki başlık **test edilecek hipotezdir**, kârlı olduğu gösterilmiş iki strateji değildir. Önceki adaylarla işlem örtüşmesi ve filtre ablation yapılmadan ayrı strateji sayılmaz.
