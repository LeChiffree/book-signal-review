# Kitap okuma 209 — gün içi mumlar, Pinch ve kalabalık duyarlılığı

Üç daha önce tamamlanmamış PDF'nin **527 sayfası** sayfa bazında metne çıkarılıp tarandı; kural sayfaları ayrıca incelendi. **Yeni, henüz doğrulanmamış kapalı mum stratejisi adayı: 1.** Backtest, paper test ve emir yapılmadı. Sayılar PDF sayfasıdır.

## 1. Greg Capra — Gün İçi Trading Taktikleri (143 sayfa)

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 11/Baskı 11/Gün İçi Trading Taktikleri - Greg Capra (143 sayfa) - @eseckal.pdf>) · [tam metin](01_intraday_capra.txt)

**Tam tarama:** S. 1–43 gün içi piyasa ve bar okuma; 44–62 hareketin temizliği, üç ila beş barlık seri, COG karşı renk mumu ve daralan barlar; 63–91 açılış ve zaman dilimleri; 92–119 geri çekilme ve yönetim; 120–143 TRIN/piyasa genişliği. S. 44–46 gövde örtüşmesinin %20'den az olduğu seriyle temiz hareket, %50–60 üstünün tıkanıklık sayılması nesnelleştirilebilir bir kalite filtresi; s. 53–57 en az üç aynı renk mumdan sonra tek ters renk mumuyla COG dönüşü ve s. 58–62 daralan aralık, önceki [mum dönüşü](../batch_003/STRATEGIES.md), [teyitli fitil reddi](../batch_019/STRATEGIES.md) ve kısa seri dönüş ailelerinin varyantlarıdır. S. 92–105'teki %40–60 geri çekilme de kayıtlı düzeltme girişlerinden ayrışmıyor. S. 120–143'te TRIN, yükselen/düşen hisse sayısı ve hacmi gibi fiyat mumunda olmayan dış girdiler ister. **Yeni aday: 0.**

## 2. Oliver L. Velez — Her Operasyonda Kazanma Stratejileri (191 sayfa)

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 11/Baskı 11/Her Operasyonda Kazanma Stratejileri - Oliver L. Velez (191 sayfa) - @eseckal.pdf>) · [tam metin](02_velez_strategies.txt)

**Tam tarama:** S. 1–103 risk, açılış, çoklu zaman dilimi ve temel mum yapıları; 104–156 gün içi düzeltme ve işlem örnekleri; 157–174 endekse göre güç, açılış aralığı ve tükeniş dönüşü; 175–179 Elephant Step/Pinch sıkışması ve Mortgage Gap; 180–191 boşluk ve ek formasyonlar. S. 157–174'teki göreli güç, başarısız açılış kırılımı ve hacimli düşüş dönüşü mevcut ailelerle örtüşür. S. 179–182'de önceki kırmızı günlük mumun tepesinin üzerinde ters yönde açılan Mortgage Gap, [98. partideki](../batch_098/STRATEGIES.md) önceki ayı mumu + gap up + ilk M5 kırılımının daha sıkı koşullu varyantıdır; ikinci aday olarak sayılmadı. “Her operasyonda kazanma” başlığı performans kanıtı değildir.

### PCH209A — Yükselen 20 ortalama ile 200 ortalama tavanı arasında Pinch kırılımı

- **Kaynak çekirdeği:** S. 175–179'da fiyatın 200 periyotluk hareketli ortalamaya doğru basamaklı yükselmesi, yatay üst sınır altında yükselen dipler, 20 periyotluk ortalamanın fiyatı alttan destekleyip 200'e yaklaşması, ardından iki ortalama ve kutu tavanının üstüne çıkış. Kaynak, kutu için örneğe özgü sent cinsinden aralık verir; evrensel ATR eşiği, kapanış teyidi veya sabit hedef vermez. Aşağıdaki sayılar ön kayıt için bizim seçimimizdir.
- **Evren/veri:** Nokta zamanlı ABD listeli ve delist edilmiş likit hisseler; kurumsal işlemlere göre düzeltilmiş M15 OHLCV, önceki seans D1 kapanışı, gerçek NY borsa takvimi; M1/NBBO yürütme verisi. En az 220 tamamlanmış M15 bar ısınması. Her seans 09:30–16:00 ET; yalnız 10:00–15:15 arası sinyal. Tüm ortalamalar ve ATR yalnız tamamlanmış barlardan hesaplanır.
- **Ön kurulum:** Sinyal barı `t` öncesindeki `B=[t−n,t−1]` için `n=4…8` barı tara; birden fazla uygunsa en kısa `n`. `ATR=ATR14_(t−1)`; `(max(H_B)−min(L_B))≤1.5×ATR`. Son üç barın en düşük dibi ilk üç barın en düşük dibinden büyük olsun; en az iki `H_B` değeri `max(H_B)−0.25×ATR` içinde kalsın. Bu, yükselen dip/yatay tavan için nedensel vekildir. `SMA20_(t−1)>SMA20_(t−4)`, `0<SMA200_(t−1)−SMA20_(t−1)≤0.75×ATR` ve bu fark `t−4`'teki farktan küçük olsun. `max(H_B)` değeri `SMA200_(t−1)±0.5×ATR` bandında; son iki kurulum kapanışı kendi SMA20'sinin üstünde olsun. Kutunun üst sınırı ve tüm göstergeler `t−1` kapanışında sabittir.
- **Sinyal/giriş:** Tamamlanmış `t` M15 barında `C_t>max(H_B)` ve `C_t>SMA200_t`; ayrıca `C_t` önceki seans kapanışından ve bugünkü açılıştan yukarıda. Yalnız ilk geçiş; aynı sembolde günde bir sinyal. Sonraki M1 açılışında yürütülebilir alış fiyatı `max(H_B)+0.5×ATR` değerini aşmıyorsa long, aşarsa pas. Kaynaktaki bar içi kırılım yerine kapanış teyidi kullanımı bizim gecikmeli, geleceği görmeyen uygulamamızdır.
- **Risk/çıkış:** İlk stop `min(L_B)−0.1×ATR`; giriş-stop mesafesi pozitif ve `≤1.5×ATR` değilse pas. Pozisyon büyüklüğü girişteki portföy özsermayesinin `%0.25`ini riske atacak şekilde, hisse başına toplam ağırlık en fazla `%10`. Önce stop veya `2R` hedef; kalan pozisyon 15:55 ET'de M1 yürütülebilir fiyatından kapatılır. Aynı M1 içinde stop/hedef sırası bilinmiyorsa kötü sonuç önce; spread, komisyon, kayma, halt ve geç açılışlar ayrıca modellenir.
- **Ayırıcı test:** Aynı evren, seans ve yürütmede çıplak 4–8 bar kutu kırılımı, yalnız SMA200 üstü geçiş ve 20–200 yakınsama filtresi kaldırılmış sürümle karşılaştır. [208. partideki günlük düz taban](../batch_208/STRATEGIES.md) ve [204. partideki VCP](../batch_204/STRATEGIES.md) ile farklı zaman ölçeği ve olay eşleşmeleri ayrı raporlanır. Tüm sinyaller, reddedilen girişler, net R, maliyet duyarlılığı, aylık dağılım ve zaman sıralı dış örneklem kaydedilir. Kuralın kaynakta gösterilen grafiklerden daha geniş piyasada işe yaradığı **bilinmiyor**.

## 3. John F. Summa — Kalabalığa Karşı Trading (193 sayfa)

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 11/Baskı 11/Kalabalığa Karşı Trading - John F. Summa (193 sayfa) - @eseckal.pdf>) · [tam metin](03_summa_crowd.txt)

**Tam tarama:** S. 1–59 karşıt görüş ve put/call oranı; 60–99 Squeeze Play I/II ile put/call EMA osilatörü ve fiyat teyidi; 100–149 VXO/örtük oynaklık; 150–193 açığa satış oranları, yatırımcı anketi ve piyasa duyarlılığı. S. 60–75'te toplam put/call verisinin EMA5–EMA21 geçişi ve bir önceki günün yüksek/düşük fiyat teyidi; s. 76–99'da hisse özel opsiyon put/call EMA50–EMA100 ve üç günlük fiyat kırılımı anlatılır. Bu oranlar, VXO ve kısa satış/anket serileri yalnız dayanak hissenin kapalı OHLCV mumlarından üretilemez. Verinin tarihsel ve nokta zamanlı erişimi sağlanırsa ileride **ayrı veri gereksinimli** araştırma taslağı olabilir; bu turun mum tabanlı aday sayısına eklenmedi. Kitaptaki dönemsel testler bağımsız doğrulama olarak alınmadı. **Yeni aday: 0.**

**Parti sonucu:** 3 PDF, **527 sayfa**, **1 yeni doğrulanmamış aday**. Kümülatif **627 PDF, 44.747 sayfa, 444 doğrulanmamış aday**.
