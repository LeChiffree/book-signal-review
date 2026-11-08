# Kitap okuma 143 — Endekse karşı güçlü hisse

**Kapsam:** Üç ayrı PDF'nin 30 + 36 + 40 = **106 PDF sayfası** baştan sona incelendi. Sayfa atıfları PDF sayfasıdır. Aşağıdaki mekanik eşikler, kaynakta verilmediği yerde **bizim önceden sabitlenecek test varsayımımızdır**. Backtest, paper test ve emir yapılmadı.

## 1. Yeni Başlayanlar için Smart Money Konsepti — Derek Salvon

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 19/Baskı 19/Yeni Başlayanlar için Smart Money Konsepti - Derek Salvon (30 sayfa) - @eseckal.pdf>) · [Tam metin](01_salvon_smc.txt)

**Tam okuma:** S. 1–9 BOS/CHOCH ve yapı; s. 10–16 arz/talep, likidite süpürmesi, order block, H1/H4 bölge ve CHOCH teyidi; s. 17–21 FVG geri testi ve orta noktası; s. 22–29 GBPUSD seçilmiş örnekler; s. 30 sonuç. Bölge → süpürme → yapı değişimi → FVG dönüşü dizisi [önceki SMC/FVG kayıtları](../batch_135/STRATEGIES.md) ile aynı olay ailesidir. “Güçlü bölge” ve orta nokta yorumu bağımsız kapanış sinyali sağlamaz. S. 19'daki ayı FVG açıklamasının yeşil mum demesi çeviri tutarsızlığıdır. **Yeni aday: 0.**

## 2. Risk Yönetimi — Abraham Robert C.

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 19/Baskı 19/Risk Yönetimi - Abraham Robert C. (36 sayfa) - @eseckal.pdf>) · [Tam metin](02_abraham_risk.txt)

**Tam okuma:** S. 1–12 sermaye, sabit miktar/yüzde risk, stop ve korelasyon; s. 13–23 lot büyüklüğü ve risk türleri; s. 24–33 risk uygulaması ve döviz korelasyonu; s. 34–36 sonuç. Yönlü işlem girişi tanımlamaz. S. 7'de 1:1 ve eşit sayıda kâr/zarar sonucu ücretleri dışlar. S. 19'daki yüzde özsermaye riski ile 50:1 kaldıraç eşleştirmesi matematiksel olarak aynı şey değildir; s. 33'teki kur yönü/korelasyon anlatımı da doğrudan kural alınamaz. Stop mesafesine göre miktar ve portföy korelasyonu ileride uygulama kontrolü olarak kullanılabilir. **Yeni aday: 0.**

## 3. Hisse Senedi Ticaretinde Zafer — Oliver Kell

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 7/Baskı 7/Hisse Senedi Ticaretinde Zafer - 2020 ABD Yatırım Şampiyonunu Stratejisi ve Taktikleri - Oliver Kell (40 sayfa) - @eseckal.pdf>) · [Tam metin](03_oliver_kell.txt)

**Tam okuma:** S. 1–6 özgeçmiş/içindekiler; s. 7–14 10/20 EMA fiyat döngüsü, wedge pop, ilk geri çekilme, taban ve tükenme; s. 15–17 endekse göre göreceli güç ve QQQ/LVGO yüksek dip–düşük dip örneği; s. 18–24 cup-handle, çift dip, bayrak, 2B ve gap/üst fitil; s. 25–27 stop/çıkış; s. 28–34 ZM/FSLY/PTON/AMZN seçilmiş grafikler; s. 35–36 pozisyon/portföy; s. 37–40 özdeyişler/sonuç/ek. Kitabın 2020 yarışma getirisi ve seçilmiş grafikler ileriye dönük kanıt değildir. EMA çekilmesi, taban kırılımı, bayrak ve fitil/gap varyantları mevcut formasyon/gap ailelerine yakındır; eşik belirsizliklerinden ayrı aday yapılmadı. Portföy bölümündeki yüksek marj oranları test için öneri değildir.

### OK143A — QQQ yeni düşüğünde yüksek dip yapan hisse ve EMA geri alımı

- **Kaynak fikri:** Genel endeks yeni düşük yaparken hissenin daha yüksek dip yapması göreceli güç belirtisi; LVGO/QQQ örneği iki kez tekrar eder (PDF s. 16–17). Yazar bunun ardından wedge pop alım alanını ve 10/20 EMA fiyat döngüsünü gösterir (s. 7–14, 17). Aşağıdaki pivot gecikmesi, pencereler, giriş ve çıkış eşikleri kaynakta verilmez; seçilmiş grafik örneğini sınanabilir hipoteze çevirir.
- **Evren/veri:** ABD borsasında işlem gören adi hisseler, geçmiş tarihte gerçekten listelenmiş/delist edilmiş adları da içeren point-in-time evren; D1 bölünme/temettü düzeltilmiş OHLCV, gerçek işlem fiyatı ve kurumsal işlem takvimi. Sinyal gününde kapanış fiyatı >10 USD ve önceki 20 seans ortalama hacmi ≥1 milyon hisse (kaynak s. 16); bu eşikler eski günlerde bilinen bilgilerle hesaplanır. Endeks vekili QQQ; hissenin kote olmadığı günlerde eşleştirme yok.
- **Kapalı mum sinyali:** QQQ ve hisse için aynı seans D1 low üzerinde 2 sol + 2 sağ barlı yerel dipleri yalnız ikinci sağ bar kapandıktan sonra onayla. Son 40 seanstaki ardışık iki QQQ dip değeri azalsın; bu iki QQQ dip tarihine ±2 seans yakın teyit edilmiş hisse dipleri ise artsın. İkinci çiftin tamamı bilinir olduktan sonraki en çok 10 seansta hisse kapanışı `EMA10` ve `EMA20` üstüne **alttan geçsin** (`C[t−1] ≤ max(EMA10,EMA20)[t−1]`, `C[t] > max(EMA10,EMA20)[t]`). QQQ ikinci dip tarihi ve sağ pencere kapanmadan hisse sinyali üretme. Aynı hisse için yeni bir QQQ dip çifti oluşana kadar tek sinyal. Pivot yarıçapı/pencereler ve EMA teyidi bizim sabit yorumumuzdur.
- **İcra/risk/çıkış:** Sinyal t kapanışı sonrası sonraki normal seans açılışında uygulanabilir ask fiyatından long; eksik/aşırı açılış gapinde de gerçek açılış fiyatı geçerlidir. Başlangıç stopu ikinci hisse pivot low `−0,1×ATR14`; açılış stopun altında ise işlem yok. Sabit ilk hedef 2R, ayrıca D1 kapanışı EMA20 altında ise sonraki seans açılışında çıkış; en geç 20 seans sonra çıkış. Stop/target aynı bar içinde olursa günlük veriyle güvenilir sıra kurulamadığı için ihtiyatlı stop önce senaryosu ve intraday doğrulama ayrı raporlanır. Komisyon, spread, vergi/ücret ve kayma dahil; işlem başına en çok %0,25 özsermaye riski, kaldıraç yok. Hissenin işlem durması/delist olması çıkış varsayımında açıkça işlenir.
- **Kıyas ve karar ölçüsü:** Aynı evrende yalnız EMA10/20 geri alımı, QQQ EMA rejimi ve yalnız hissenin yükselen dip filtresi ile karşılaştır; adayın katkısı **endeks düşük dip / hisse yüksek dip ayrışması**dır. Tarihi ileri taşımayan evren ve ücret sonrası sonuç, tüm hisse/sektörlerde kümeleme ve döneme göre out-of-sample ayrım gerekir. Kaynak bu sinyalin kazanma oranını veya beklenen getirisini vermiyor. Önce veri uygulanabilirliği, sonra backtest ve ardından paper test; henüz yapılmadı.

## Sonuç

**1 yeni araştırma adayı: OK143A.** 143. parti sonunda toplam **429 tamamlanmış kitap ve 381 kayıtlı strateji adayı** vardır. Aday yalnız hipotezdir; kârlılık veya işlem tavsiyesi anlamına gelmez.
