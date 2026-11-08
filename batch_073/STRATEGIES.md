# Kitap okuma 073 — iç içe yapı teyidi, piyasa rejimi, ikinci geri çekilme

**Kapsam:** Üç PDF'nin gerçek **64 + 64 + 24 = 152 sayfası** sırayla okundu. Metni kısa olan sayfalardaki grafikler [görsel olarak](figure_contacts/) kontrol edildi. Atıflar PDF sayfasıdır. Aşağıdaki eşikler kitaplardan gelmiyorsa **bizim araştırma parametrelerimizdir**. Burada kârlılık sonucu, backtest veya paper test yoktur.

## 1. Follow The Money (FTM) Stratejisi

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 6/Baskı 6/Follow The Money (FTM) Stratejisi (64 sayfa) - @eseckal.pdf>) · [Tam metin](01_ftm.txt)

**Kaynak taraması:** S. 3–14 yapı, trend ve itki/düzeltme temposunu; s. 15–27 son karşıt mumdan tanımlanan emir bloğu, fitil boşluğu/imbalance, eşit tepe-dip likiditesi ve taze bölgeyi; s. 28–38 Wyckoff şemalarını; s. 36–49 üst zaman dilimi karar bölgesi, alt zaman dilimi yapı kırılımı (BOS) ve ilk retest ile girişi anlatır. S. 50–64 grafik örnekleridir. Kaynağın tüm imbalance'ların dolacağı ve örneklerdeki çok yüksek ödül/risk iddiaları doğrulanmış istatistik değildir. Wyckoff/kurumsal emir niyeti OHLCV'den doğrudan gözlenemez.

### FTM73 — Üst dilim taze bölgesi içinde alt dilim yapı kırılımı

- **Kaynak kuralı:** H4/H1 karar noktasına geri dönüş, M5/M1'de yönlü BOS ve oluşan alt dilim OB/imbalance retesti sonrası giriş; stop bölge dışı, hedef üst dilimde beklenen sonraki swing (s. 19, 26, 36–37, 43–49). Kaynak kesin BOS eşiği veya bölümleme algoritması vermez.
- **Bizim günlük karar uyarlamamız:** Kapalı günlük barda yön `close>EMA20_D` ve son 5 günlük getiri pozitifse long, tersi short. Son 12 tamamlanmış H4 barda yönlü `close>önceki 10 H4 high` ve kırılım gövdesi `≥0,7×ATR14_H4` olduğunda, kırılım öncesi son karşıt H4 mumun high/low aralığını dondur. Bu bölgeye **ilk H4 geri dönüş** ve sonrasında tamamlanmış H1 barının dönüş öncesi 5 H1 high/low seviyesini yönlü kapanışla aşması aranır. Bölge/kırılım/swing pencereleri ve 0,7 ATR tamamen bizim nesnelleştirmemizdir; kaynakta kullanılan M1/M5 BOS'un bire bir eşdeğeri değildir.
- **Karar ve icra:** Günlük 00:00 UTC satırına yalnız o anda kapanmış H4/H1 olayları bağlanır; son 24 saatteki uygun BOS varsa sonraki uygulanabilir 1m açılışında giriş. Long stop dondurulmuş H4 bölge altı `−0,1×ATR14_H4`, short simetrik; önceden onaylı H4 swing hedefi veya 2R ayrı kollar, en çok 7 gün. Hedef lehte değil/ilk net ödül-risk <1 ise atla. Aynı 1m stop önce, ücret/kayma/funding dahil. Günlük karar saatinden *sonra* oluşan M1/M5 teyidini aynı karar satırına sızdırma.
- **Katkı/karşılaştırma:** FE72 ve önceki taze arz-talep retestleri ile aynı bölge ailesindedir. Ayrı sınanacak ek koşul **bölge dönüşünden sonra alt dilim yönlü BOS**; aynı giriş evreninde BOS'lu/BOS'suz, ilk/çoklu dokunuş ve işlem sayısı/net R karşılaştırılır. M1/M5 mikro yapı gerçek yöntemi için ayrıca gün içi karar sözleşmesi gerekir.

## 2. Forex Trading Sistemi — Sumo FX — Jaco Ferreira

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 6/Baskı 6/Forex Trading Sistemi - Sumo FX - Jaco Ferreira (64 sayfa) - @eseckal.pdf>) · [Tam metin](02_sumo_fx.txt)

**Kaynak taraması:** S. 11–13 döviz ve çoklu zaman dilimleri; s. 34–41 H1/H4 trend yönünde işlem; s. 36 Bollinger(20) orta bant eğimi/fiyat tarafı ile trend süzme, RSI/Stochastic kontrolü; s. 43–49 M15/M30 yatay piyasa ve dar/yatay Bollinger bantlarıyla sıkışma anlatır. Kalıp, trend çizgisi, pivot, Fibonacci ve temel analiz de kullanılır; sistemde mekanik giriş/çıkış kuralları tam tanımlı değildir. Çevirideki RSI “-70” ifadesi matematiksel RSI ölçeğiyle uyuşmadığı için kural yapılmadı. Kaynak FX pip/spread ve seans bağlamındadır.

### SF73 — Bollinger orta çizgi eğimi ve bant daralmasıyla rejim ayırma (özellik adayı)

- **Kaynak fikri:** Eğimi belirgin orta bant trend, dar/yatay bant range/sıkışma bağlamı sağlar (s. 35–36, 44–45). Kitap daralmanın mutlaka hangi yönde kırılacağını söylemez.
- **Bizim ölçülebilir özelliklerimiz:** Günlük kapanmış barlarda `sma20_slope_5=(SMA20_t−SMA20_{t-5})/ATR14_D`, `bb_width=(upper20,2−lower20,2)/SMA20`, genişliğin geriye dönük 120 günlük yüzdelik sırası. `|slope|≥0,25` ve fiyat orta bandın eğim tarafında ise trend; `|slope|<0,1` ve genişlik yüzdeliği ≤20 ise yatay/sıkışık; kalanlar belirsiz. 5 gün, 0,25/0,1 ve 120/20 yüzdelik **bizim ön kayıt eşiğimizdir**.
- **Test rolü:** Bu tek başına işlem açmaz. Mevcut trend devamı ve bant geri dönüş adaylarının hangi rejimde maliyet sonrası net R ürettiğini ayrı ölç; aynı sinyal ve örneklemde filtresiz kontrolle kıyasla. Band daralmasını yön tahmini gibi kullanma. Mevcut Bollinger/slope özellikleri varsa yeni kolon üretme, etkileşimi veya koşullu performansı ölç.
- **Ertelenen kısım:** S. 37–41 ve 46–49'daki pivot/Fibonacci/formasyonla kesin giriş, forex haber ve mikro zamanlama birleşimi açık tanım/veri olmadan sadık mekanik stratejiye dönüşmez.

## 3. En Başarılı 10 Price Action Modeli — Al Brooks

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 6/Baskı 6/En Başarılı 10 Price Action Modeli - Al Brooks (24 sayfa) - @eseckal.pdf>) · [Tam metin](03_al_brooks_patterns.txt)

**Kaynak taraması:** S. 3–6 trend dönüşü/final bayrak, s. 7 kapanmış barla kırılım, s. 8–9 High 2/Low 2 ikinci geri çekilme tetikleri, s. 10–11 üç itişli kama, s. 13–14 mikro kanal, s. 15–16 ölçülü hareket, s. 17–18 yatay bantta ikinci sinyal, s. 19–22 açılış ve destek/direnç dönüşleri. S. 23 grafiği ayrıca görüldü. Kaynaktaki yaklaşık %40/%60/%75 olasılık ifadelerinin veri, maliyet ve örneklem hesabı verilmez; sonuç sayılmaz. Seans açılışına bağlı örnekler 24/7 kriptoya doğrudan taşınmaz.

### AB73 — Trend içindeki ikinci geri çekilme denemesinden devam

- **Kaynak kuralı:** Boğa trendinde ilk küçük karşı hareketten sonraki High 1 devam denemesi başarısız kalıp bir geri çekilme ayağı daha oluşursa High 2 long; ayı trendinde Low 2 short (s. 8–9). Adlar mum high/low tetiklerine aittir; kitap günlük kripto için bar sayısı vermez.
- **Bizim nesnel örüntü:** Günlük `EMA20>EMA50` ve son 20 günlük getiri pozitifken önceki 20 gün high'ından en az `0,8×ATR14_D` geri çekilme başlasın. İlk tepki kapanışı önceki 3 bar high'ını aşsın fakat sonraki en çok 5 kapanmış barda yeni 20 günlük high gelmeden ikinci bir dip oluşsun; ikinci dip ilk dipten en fazla `0,5×ATR` aşağı olsun. İkinci dipten sonraki ilk `close>önceki 3 bar high` High 2 vekili ve long tetiktir. Short için yön/tepe/low simetrik. Bütün dipler, tepki ve teyit yalnız bar kapandıktan sonra bilinir; merkez pivotu geçmişte biliniyormuş gibi etiketleme. Pencereler/eşikler bizimdir; Brooks'un intrabar stop emrinden farklı kapanış vekilidir.
- **İcra/risk:** Tetik kapanışı sonrası ilk uygulanabilir 1m; long stop ikinci dip altı `−0,1×ATR`, short ikinci tepe üstü; 2R ve önceki trend zirvesi ayrı hedef kolları, 7/14 gün süre kolları. Girişte stop ve hedef doğru tarafta değilse ya da beklenen net ödül-risk <1 ise işlem yok. Aynı 1m stop önce, ücret/kayma/funding dahil.
- **Katkı/karşılaştırma:** Tek pullback devamı ve çift dipten ayrılan olay **başarısız ilk trend devam denemesinden sonraki ikinci deneme**dir. Aynı trend tanımı ile ilk deneme, ikinci deneme ve rastgele seçilmeyen tüm pullback girişlerini işlem örtüşmesi, örneklem büyüklüğü ve net R üzerinden kıyasla. Kamanın üç itişi ve ölçülü hareket önceki adaylarla örtüşür; mikro kanal yorgunluğu ise kaynakta kesin giriş vermediği için ayrı strateji yazılmadı.

## Ortak doğrulama

FTM73/AB73 tasarımdır; SF73 işlem sinyali değil, koşullu özellik hipotezidir. Point-in-time sembol evreni, yalnız kapalı UTC mumlar, sonraki 1m icrası, ücret/spread/kayma/funding, eksik bar kontrolü, 1m yolunda stop önceliği ve zaman sıralı walk-forward zorunludur. Aynı günlük karar anında kapanan H4/H1 barının canlı veri gecikmesi doğrulanmalıdır. Eski yaklaşık 1.300 özelliklik pilotta eşdeğer sütun varsa tekrarlanmaz. Bunlardan herhangi biri henüz doğrulanmış kârlı strateji değildir.
