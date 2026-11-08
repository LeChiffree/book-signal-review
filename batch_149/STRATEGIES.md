# Kitap okuma 149 — işlem kuralları, gün içi stratejiler ve arz/talep

Üç **ayrı** kitap, toplam **136 PDF sayfası** baştan sona incelendi. **Yeni bağımsız strateji adayı: 0.** Backtest, paper test ve emir yapılmadı. Sayfalar PDF sayfasıdır.

Başlangıçta çıkarılan `VWAP Trading Stratejisiyle Kolay Para — Kartik K`, [43. partide](../batch_043/STRATEGIES.md) incelenen VWAP/PVWAP kitabının aynı içerikli kopyası çıktı; [103. partide](../batch_103/STRATEGIES.md) de eşdeğerliği belirtilmiş. Üç ayrı kitap sayılmaması için 149. partinin kapsamından çıkarıldı ve yerine Patt Tomas okundu.

## 1. Trading Kuralları — Patt Tomas

Kaynak: `D:\Paper_ML_BSH\Drive_PDF\PDFler\Baskı 12\Baskı 12\Trading Kuralları - Patt Tomas (45 sayfa) - @eseckal.pdf` · [tam metin](01_trading_rules_tomas.txt)

**Tam okuma:** s. 1–15 disiplin, kaybedene eklememe ve kazananı tutma; s. 16–26 en az 1:3 risk/ödül örneği, pozisyon büyüklüğü, sektör/endeks ve üç ardışık kayıptan sonra günlük mola; s. 27–36 hisse fiyatı, hacim ve spread seçimi; s. 37–45 işlemi kovalamama, tepe/dip avından kaçınma ve grafik okuma.

**Karar:** s. 24'teki üç ardışık kayıptan sonra günün kalanında işlem yapmama, sinyal üretmeyen **risk yönetimi üst kuralı** olarak ileride sabit aday stratejilere ayrıca uygulanabilir; tek başına yeni yön stratejisi değildir. s. 31–34'teki 50 USD fiyat, 300 bin–30 milyon hisse hacmi ve 0,06 USD spread eşikleri eski ABD hisse örnekleridir; kriptoya aynen taşınmaz. s. 19 ve 21–22'deki endeks/sektör anlatımındaki %80 oranı doğrulanmış istatistik sayılmaz. Örnek işlemler seçilmiş anekdotlardır.

## 2. Güniçi İşlemlerde Ustalaşmak — Lalit Mohanty

Kaynak: `D:\Paper_ML_BSH\Drive_PDF\PDFler\Baskı 18\Baskı 18\Güniçi İşlemlerde Ustalaşmak - Kanıtlanmış Başarı Stratejileri - Lalit Mohanty (47 sayfa) - @eseckal.pdf` · [tam metin](02_intraday_mohanty.txt)

**Tam okuma:** s. 1–9 içerik, gün içi işlem ve araçlar; s. 10–12 momentum, SMA 50/200 ve RSI; s. 12–14 seans boşluğu; s. 15–17 açılışın ilk 15–30 dakika aralığı kırılımı ve hacim; s. 17–19 dönüş, mum ve diverjans; s. 19–24 scalping ile Bollinger/ortalama dönüşü; s. 24–30 haber ve algoritmik işlem; s. 30–41 risk, psikoloji, kayıt ve test planı; s. 42–47 opsiyon türleri ve kaynakça.

**Karar:** s. 15–17 açılış aralığı kırılımı [48. partide](../batch_048/STRATEGIES.md) mekanik aday; s. 10–12 MA/RSI, s. 22–24 Bollinger ortalamaya dönüşü ve s. 17–19 mum/diverjans arşivde mevcut. s. 12–14 seans boşluğu 7/24 kripto UTC gün sınırına eşdeğer değil. Haber ve opsiyon bölümleri giriş/çıkış, veri anı ve dolum kurallarını tam vermiyor. Kitabın “kanıtlanmış” başlığı test sonucu sunmuyor.

## 3. Trading Oyununda Nasıl Kazanılır — Emily Dhruv

Kaynak: `D:\Paper_ML_BSH\Drive_PDF\PDFler\Baskı 18\Baskı 18\Trading Oyununda Nasıl Kazanılır - Emily Dhruv (44 sayfa) - @eseckal.pdf` · [tam metin](03_trading_game_dhruv.txt) · [grafik sayfalarının görsel denetimi](dhruv_visual_check.jpg)

**Tam okuma:** s. 1–7 yatay alan, itki ve ret; s. 8–18 RBR/DBD/RBD/DBR arz-talep bölgeleri, bölgeden ayrılma gücü, kısa taban, ilk dönüş ve pin/yutan mum; s. 19–29 destek/direnç rol değişimi ve bölge çizimi; s. 30–40 salınım, tıkanıklık, MA/Fibonacci ve tekrarlı test/sıkışma; s. 41–44 sonuç. Metni boş veya yalnız görsel olan s. 10, 12–13, 24, 26–27, 38–39 ayrıca görüntüden incelendi; ek sayısal işlem kuralı yok.

**Karar:** s. 9–18'in taze arz/talep tabanı ve ilk retesti [5.](../batch_005/STRATEGIES.md), [72.](../batch_072/STRATEGIES.md) ve [81. partide](../batch_081/STRATEGIES.md) kayıtlı. s. 19–40 eski destek/direnç dönüşü, yükselen diplerle dirence sıkışma, önceki salınım retesti ve Fibonacci de mevcut olay aileleri. “Akıllı para” faaliyetini yalnız mum ve hacimden kesin gözlemleyemeyiz. s. 29'da önceki barın yüksek/düşüğünün destek/direnç etiketleri ters görünür; literal kodlanmadı. Yeni bağımsız aday açılmadı.

## Birikim

Bu parti sonunda **447 kitap, 149 rapor, 19.844 PDF sayfası ve 383 ayrı strateji adayı** kayıtlıdır. Bunlar ileride backtest ve paper test için araştırma adaylarıdır; doğrulanmış kazanç değildir.
