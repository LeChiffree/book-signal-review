# Kitap okuma 005 — swing yapısı, arz–talep ve emir blokları

**Kapsam:** Üç PDF'nin 40 + 23 + 50 = **113 PDF sayfası** işlendi. Sayfalar PDF sayfasıdır. Swing PDF'sinin `(1)` kopyası özgün dosyayla SHA-256 düzeyinde aynıdır; **tek kitap** sayıldı. Order block PDF'sinin bazı satırları kaynak baskıda bozuk/karışık dilli; PDF s. 18 ve 21 ayrıca görsel açıldı ve bozukluk görüntünün kendisinde de doğrulandı. Anlaşılan kurallar aşağıda, çözülemeyen yerler bilinmeyen olarak kaydedildi. Buradaki sinyaller kanıtlanmış getiri veya kurum işlemi gözlemi değildir.

## 1. Swing Yüksekleri ve Swing Düşüklerini Kullanarak Pazarın Ne Durumda Olduğunu Daha İyi Anlamak

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 9/Baskı 9/Swing Yüksekleri ve Swing Düşüklerini Kullanarak Pazarın Ne Durumda Olduğunu Daha İyi Anlamak (40 sayfa) - @eseckal(1).pdf>)

Kitap trenddeki swing high/low, önemli yapısal pivot, sahte yüksek/düşük ve önceki swing seviyesine dönüş örnekleri veriyor (s. 3–19, 20–40). “Bankalar işlem açtı/kâr aldı” açıklaması (ör. s. 4–8, 13–18, 21–23) OHLCV ile görülemez; yalnız yazarın yorumu. Yazar s. 5 ve 17'de dönüş nedeni oluşurken bilinemez diyor. Forex için anılan **50 pip** aşım sınırı (s. 29–31, 36–40) kriptoya veya farklı fiyat ölçeklerine taşınamaz; sabit 50 pip uygulanmayacak.

### S1 — Teyitli swing seviyesinin aşılması ve başarısız kırılım

- **Kaynak fikri:** Eski swing tepesinin çok az aşılması sonrası fiyatın tekrar altına dönmesi, yeni trend kanıtı sayılmayabilir (s. 20–24); aşım miktarı ve sonra kırılan karşı swing seviyesi önemlidir (s. 28–31).
- **Bizim kapanmış günlük tanım:** Pivot high için `k=3` sol ve `k=3` sağ günlük barın high değerlerinden yüksek merkez high; pivot ancak üçüncü sağ bar **kapandığında** bilinir. Son teyitli pivot high `P`. `high[t]>P+0.1*ATR14[t-1]` ve `close[t]<P` ise tek barda başarısız yukarı kırılım; alternatif iki barlık varyantta t kapanışı P üstü, t+1 kapanışı P altı. Short olayı ikincinin kapanışında doğar. Dip için simetri. `0.1 ATR`, k=3 ve iki bar tanımı kaynak değil, bizim hipotezdir.
- **Giriş/çıkış:** Olay kapanışı sonrası ilk yürütülebilir 1m; stop sahte aşımın en uç seviyesi + 0.1 ATR, çıkış karşı teyitli pivot veya 1R/2R, ayrıca H3D/H7D/H14D. Aynı fiyat seviyesi için yinelenen sinyaller tek olay grubu. Yüksek likiditeli varlık ve yeterli ATR ön filtresi; geçmişte teyit edilmemiş pivot hiçbir erken satıra yazılmaz.
- **Kontrol:** Yalın pivot kırılımı sonrası devam ile başarısız kırılım dönüşünün ayrı performansı. Bu aday, önceki partideki G1 çift tepe/dip ile örtüşebilir; ayrı keşif kanıtı sayılmaz.

### S2 — Yapı kırılımı sonrası teyitli pivot bölgesinin yeniden testi

- **Kaynak fikri:** Önceki swing high kırıldıktan sonra daha yüksek dip oluşumu ve bu alanın tekrar testinde mum teyidi; örnekte yutan mumla uzun giriş, stop swing dip altında (s. 33–40). Yazarın kurum motivasyonu kanıt diye alınmaz.
- **Bizim kapalı günlük olay:** `close[t] > last_confirmed_pivot_high + 0.25 ATR14[t-1]` ile BOS yukarı; bu anda bilinen son teyitli pivot low etrafında `±0.25 ATR` bölgesi dondurulur. Sonraki 1–20 günlük barda bölgeye ilk geri dönüş ve `close>open` ile kapanış teyidi varsa uzun sinyal. `k=3`, 0.25 ATR, 20 bar ve boğa mumu eşiği bizim tanımlarımız; yutan mum teyidi mevcut özellik olarak ayrı ablation.
- **Yürütme:** Teyit kapanışı sonrası ilk 1m; dondurulmuş pivot low altı stop; son teyitli tepe/2R veya 3/7/14 günlük çıkış. BOS sonrasında pivotu geriye dönük seçme ve ilk testten sonra bölgeyi yeniden “taze” sayma yasak.

## 2. Arz ve Talep Bölgeleri — Fahmi Lamar

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 9/Baskı 9/Arz ve Talep Bölgeleri - Fahmi Lamar (23 sayfa) - @eseckal.pdf>)

Kitap düşüş–taban–ralli (DBR), ralli–taban–düşüş (RBD), düşüş–taban–düşüş (DBD) ve ralli–taban–ralli (RBR) yapılarını gösteriyor (s. 5–8). Bölgeden çıkış gücü, tabanda 1–6 mum, ilk testin “tazeliği” ve en az 3:1 hedef/stop alanı ile puan öneriyor (s. 13–23). Puan tarifi tutarsız: s. 13 her unsur için 3 puan derken s. 14–16 ilk iki unsurun azamisini 2 yapıyor; s. 15 `1–6` mumu kabul ediyor, s. 23 altı mum örneğine 0 veriyor. Bu yüzden **8/10 eşiklerini doğrudan otomatik karar kuralı olarak almıyoruz**. “Doldurulmamış kurumsal emir” varlığı OHLCV ile ölçülmüyor.

### D1 — Dondurulmuş kısa taban bölgesine ilk dönüş

- **Kaynak fikri:** Hızlı çıkışlı, az mumlu, daha önce test edilmemiş bölgeye dönüş; 10 puan için proksimal çizgide limit, 8–9 puan için bölge içine kapanış ve sonra bölge dışına çıkış teyidi (s. 13–23).
- **Bizim günlük oluşum kuralı:** 1–5 ardışık gün boyunca `max(high)-min(low)<=1.0*ATR14` olan taban; ardından tamamlanmış 1–3 barda net yönlü yer değiştirme `>=1.5*ATR14` ve taban yüksekliğinin üstünde kapanış (talep, DBR/RBR). Arz için simetri. Bölge, çıkış barı kapandığında tabanın `low/high` sınırlarıyla **dondurulur**. 1–5, 1.0, 1–3 ve 1.5 bizim objektifleştirmemiz; kaynakta yoktur. Trend öncesi yön DBR/RBR ayrımında ayrıca kayıtlı.
- **Giriş:** Oluşum sonrası 20 gün içinde **ilk** bölge teması için ertesi yürütülebilir 1m yolunda proksimal sınır limit emri, en fazla 1 gün geçerli; alternatif, bir tamamlanmış günlük mum bölgede kapanıp sonraki tamamlanmış günlük mum bölge üstünde kapandığında piyasa girişi. İkinci sürüm kaynak teyidinin nedensel uyarlamasıdır. Dolmayan limitler silinmez, `unfilled` sayılır.
- **Stop/çıkış:** Talepte taban dibi altı 0.1 ATR, arzda tersi; karşı önceden teyitli bölgeye kadar mesafe/riski **işlem anında** hesapla. Hedef `2R`/`3R`, 3/7/14 gün ve karşı bölge ayrı. 3:1 alan filtresi, geçmişte bilinen seviyelerle hesaplanır; gelecekte oluşacak direnç kullanılamaz.
- **Ablation:** ilk temas vs sonraki temas, kısa taban, güçlü çıkış, 3:1 önceden bilinen alan. 8/10 puan iddiası ayrı test edilmeden kullanılmaz.

## 3. Piyasa Yapısı ve Order Block Sanatında Ustalaşmak — Wisdom Muke

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 19/Baskı 19/Piyasa Yapısı ve Order Block Sanatında Ustalaşmak - Wisdom Muke (50 sayfa) - @eseckal.pdf>)

Kitabın temel fikri, **yukarı yapı kırılımından önceki son düşüş mumunu** boğa emir bloğu; aşağı kırılımdan önceki son yükseliş mumunu ayı emir bloğu olarak almak ve fiyat dönünce bölgeyi gözlemek (s. 17–23). Yüksek zaman dilimi yapı bağlamı, arz–talep ve trend çizgisi/Fibonacci teyidi öneriyor (s. 24–27). Metin baskıdan itibaren yer yer bozulmuş; s. 18 ve 21 görüntüsü bile anlamsız diziler içeriyor. S. 24–27'de tam emir tetik/stop/iptal eşiği yok. “Kurumların emri orada” çıkarımı fiyat grafiğinden doğrulanmaz.

### O1 — Yapı kırılımından önceki karşı renk mum bölgesinin ilk retesti

- **Kaynak fikri:** Son düşüş mumu + sonrasında daha yüksek yapı kırılımı, boğa blok; ters yapı ayı blok (s. 18–23). İlk dönüşte tutunma varsayımı görsel örneklerle anlatılıyor (s. 19–22), sistematik istatistik yok.
- **Bizim kapalı günlük olay:** Önceki k=3 ile teyit edilmiş pivot high `P` üstünde `close[t]>P+0.25*ATR14[t-1]`. `t` öncesindeki son 10 kapalı bardan **son düşüş mumu** (`close<open`) seçilir; aralık `[low,high]` bölge olarak kırılım kapanışında dondurulur. Aynı bar yoksa sinyal yok. Bu k=3, 0.25 ATR ve 10 bar bizim tanımlarımız. Short simetri.
- **Giriş/çıkış:** Dondurulmuş bölgenin sonraki 20 gün içindeki ilk testinde proksimal sınırda bir günlük limit emri veya bölge içi günlük kapanıştan sonra yeniden blok üstü kapanış teyidi; iki emir yöntemi ayrı test. Stop blok dibi altı 0.1 ATR, 2R/3R ve 3/7/14 gün çıkışı. Limitin dolmaması, aynı 1m'de stop/limit sırası, komisyon, spread, kayma, funding kaydedilir.
- **Çakışma denetimi:** O1 çoğu zaman D1 bölgesi veya S2 pivot retestiyle aynı seviyeyi bulabilir. Önce yalnız BOS bazına karşı O1 bölgesi, D1 bölgesi ve kesişimleri karşılaştır; üç yöntem aynı işlemi işaretliyorsa üç ayrı kazanan strateji sayma. Fib/trend çizgisi çoklu teyitleri, kaynakta sayısal tolerans olmadığı için ertelendi.

## Ortak test kaydı

1. **Öncelik:** Önce S1 (sahte kırılım) ve D1 (ilk taze bölge dönüşü) tekil olayları. Sonra S2/O1/D1 örtüşmesini tek işlem evreninde ablation ile ölç.
2. **Veri:** UTC kapanmış 1d OHLCV özellikleri, geçmişte bilinen teyitli pivotlar, sinyal kapanışından sonra 1m yürütme. Var olan `bull_engulf_event` kolonunu S2 teyidinde yeniden kullan; yeni pivot/bölge durumları manifestte eşdeğer yoksa eklenebilir.
3. **Çıktı ölçüleri:** olay, tetik, dolum, başarısız dolum, net R, ücret/funding, maksimum ters hareket, bölüm bazlı BTC rejimi, dış örneklem, parametre duyarlılığı. Bölge/stop/karşı seviye sinyal anında sabitlenir; sonradan çizilen bölge geçmiş barlara işaretlenmez.
4. Bu partide **backtest, paper emir ve canlı işlem yapılmadı**. Kaynak sayfalarından üstünlük iddiası çıkarılmadı.
