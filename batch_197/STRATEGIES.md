# Kitap okuma 197 — rejim göstergesi, nicel işlem ve teknik analiz derlemesi

Üç daha önce tamamlanmamış PDF'nin **761 sayfası** sayfa bazında metne çıkarılıp tarandı; kural sayfaları ayrıca incelendi. **Yeni nesnel, kapalı mum strateji adayı: 1.** Bu aday bir giriş ailesi değil, mevcut trend stratejisine uygulanacak ayrı bir rejim kapısıdır. Backtest, paper test ve emir yapılmadı. Sayfalar PDF sayfasıdır.

## 1. Murray Gunn — Trading Rejimi Analizi (401 sayfa)

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 10/Baskı 10/Trading Rejimi Analizi - Murray Gunn (401 sayfa) - @eseckal.pdf>) · [tam metin](01_regime_gunn.txt)

**Tam okuma:** İlk bölümler trend ve aralık rejimleri, hareketli ortalamalar ve dalga yorumları; s. 184–200 bant genişliği ve ADX; s. 230 dolayları Donchian; s. 270–274 MATE; s. 275–283 TFPI; s. 284–288 TRI; kalan bölümler rejim uygulaması ve sonuç. MATE, kısa/uzun MA farkından türeyen mevcut trend filtresinin varyantıdır. TFPI s. 281–283 sanal trend sisteminin özsermaye eğrisini izler, fakat yönlü işlem için tek başına giriş/çıkış vermez. **TRI**, fiyatın standart sapmasını kendi uzun dönem ortalamasına kıyaslayarak farklı bir rejim hipotezi kurar. Kitapta kullanılan grafikler başarı kanıtı değildir.

### MG197A — TRI ile haftalık rejim kapılı günlük Donchian kırılımı

- **Kaynak:** PDF s. 284–288. S. 285 fiyat kapanışlarının 20 dönemlik standart sapması ile bunun 200 dönemlik hareketli ortalamasını karşılaştırır; farkı ortalamanın yüzdesi olarak verir. S. 286 `TRI>0` için trend, `<0` için aralık rejimi der ve haftalık rejimin daha kısa zaman dilimindeki işlemleri süzebileceğini açıklar. Donchian kırılımı aynı kitapta s. 230 dolaylarında anlatılır; bu adayın **TRI + önceden mevcut Donchian** birleşimi bizim test tanımımızdır, kitaptaki garantili kârlı sistem olarak sunulmaz.
- **Veri/ısınma:** Aynı varlığın eksiksiz W1 ve D1 OHLCV'si. W1 ve D1 kapanışları UTC pazar 00:00 sınırına göre tutarlı oluşturulur. En az 219 tamamlanmış W1 kapanışı olmadan TRI yok; eksik haftada yeni işlem yok. Her hafta yalnız **bitmiş** haftanın verisi sonraki hafta için kullanılır. Kaynak fiyat **seviyelerinin** standart sapmasını kullanır; getiri oynaklığına sessizce dönüştürülmez.
- **Rejim:** `v_w=sample_std(Close_W1[w-19:w])`; `b_w=SMA200(v)[w]`; `TRI_w=(v_w-b_w)/b_w`. `b_w<=0` veya eksikse rejim belirsiz ve giriş kapalı. `TRI_w>0` sonraki haftanın tüm günlerinde trend işlemine izin verir; `TRI_w<=0` düz rejimdir. Sıfır eşik ilk testte dondurulur; s. 286'daki ±%50 uçlar ayrı, önceden kayıtlı duyarlılık koludur.
- **Giriş ve çıkış:** İzinli haftada D1 kapanışı son **20 önceki tamamlanmış** günün en yüksek değerini geçerse long, son 20 günün en düşük değerinin altına inerse short adayı. Aynı kapanışta iki yön oluşursa işlem yok. Sinyal sonrası ilk uygulanabilir M1 açılışında gir. Pozisyon, 10 önceki tamamlanmış günün karşı Donchian kenarını D1 kapanışında aşınca sonraki ilk M1'de çıkar; ters yönde hemen dönmek için yeni 20 günlük giriş şartı aranır. Haftalık TRI kapandığında `<=0` olursa açık trend pozisyonu da sonraki ilk uygulanabilir M1'de kapanır. Bu 20/10 yürütme parametreleri kaynak TRI formülünden değil, sınanacak Donchian baz çizgisinden gelir.
- **Risk/kıyas:** İşlem başına girişte `2×ATR14(D1)` koruyucu stop ve stop mesafesiyle özsermayenin en çok `%0,25`i risk; toplam brüt maruziyet en çok `1×`. Stop M1 verisiyle yalnız sonraki gerçek zamanlı aşımda yürütülür; bar içi sıralama bilinmiyorsa iyimser doldurma yapılmaz. Aynı evren, dönem, maliyet, risk ve çıkışla **TRI'sız Donchian20/10** ana karşılaştırmadır. Ayrıca `std20/price` veya ATR/price kapısı, BB genişliği ve ADX gibi mevcut rejim filtreleriyle ablation yapılmalı; böylece yalnız fiyat düzeyi yükselmesinden doğan sahte rejim ayrımı anlaşılır. Ücret, spread, kayma, funding/roll ve veri kesintileri kaydedilir. Eğitim/son test ayrımı ve yeterli 220 haftalık geçmiş şartı evren seçimini belirler. Henüz kâr/başarı sonucu yoktur.

## 2. Saeed Amen — Thalesians Trading (210 sayfa)

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 10/Baskı 10/Thalesians Trading - Saeed Amen (210 sayfa) - @eseckal.pdf>) · [tam metin](02_thalesians_amen.txt)

**Tam okuma:** S. 1–53 Thales anlatısı, belirsizlik, kaldıraç ve stop; 54–83 alfa/beta, FX carry, trend ve değer; 84–165 risk, davranış ve uygulama; 166–183 kalabalık işlem ve strateji kapasitesi; 184–210 backtest ve canlı uygulama farkları. S. 64–70'teki FX carry/değer için faiz, fonlama veya makro değer serileri gerekir; yalnız kapalı OHLCV mumlarından kurulamaz. Trend ailesi arşivde zaten bulunuyor. S. 186–190'daki backtest, kayma ve piyasa etkisi uyarıları doğrulama tasarımına işlendi; bağımsız kesin sinyal oluşturmaz. **Yeni aday: 0.**

## 3. David Keller (der.) — Teknik Analizde Atılımlar (150 sayfa)

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 10/Baskı 10/Teknik Analizde Atılımlar - Bloomberg - David Keller (150 sayfa) - @eseckal.pdf>) · [tam metin](03_breakthroughs_keller.txt)

**Tam okuma:** S. 1–22 Drummond Geometry; 25–33 DeMark; 50–71 mum/gap; 76–93 Gann; 105–116 opsiyon duyarlılığı ve volatilite; 119–128 P&F; 129–142 Market Profile; 143–150 döngüler. Drummond zarfı ve çoklu zaman dilimi kararları s. 11–21'de tam yeniden üretilebilir kapalı mum kurallarına indirgenmiyor. DeMark, gap, Gann ve P&F aileleri önceden kaydedildi. S. 114–115'teki güçlü fiyat + yüksek put/call açık faiz + short interest + analist kötümserliği taraması somut olsa da tarihli opsiyon açık pozisyonu, short interest ve analist tavsiye geçmişi gerektirir; mevcut OHLCV kitap hedefi için aday sayılmadı. Market Profile için seans içi fiyat/hacim dağılımı gerekir. **Yeni aday: 0.**

**Parti sonucu:** 3 PDF, **761 sayfa**, **1 yeni doğrulanmamış aday**. Kümülatif **591 PDF, 36.114 sayfa, 436 doğrulanmamış aday**.
