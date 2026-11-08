# Kitap okuma 198 — dinamik kırılım, fiyat kalıpları ve emtia işlemleri

Üç yeni PDF'nin **1.127 sayfası** sayfa bazında metne çıkarılıp tarandı; işlem kuralı bulunan bölümler ayrıntılı incelendi. **Yeni nesnel, kapalı mum strateji adayı: 1.** Backtest, paper test ve emir yapılmadı. Sayfalar PDF sayfasıdır.

## 1. Thomas Stridsman — Etkili Trading Sistemlerinin Oluşturulması ve Değerlendirilmesi (345 sayfa)

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 11/Baskı 11/Etkili Trading Sistemlerinin Oluşturulması ve Değerlendirilmesi - Thomas Stridsman (345 sayfa) - @eseckal.pdf>) · [tam metin](01_effective_systems_stridsman.txt)

**Tam okuma:** S. 1–45 performans ölçümü ve veri kalitesi; 46–91 zaman ölçeği, veri madenciliği ve sistem kavramları; 92–116 eğimli MA ve dinamik kırılım; 117–146 Bollinger ve işlem verimliliği; 147–229 çıkışlar, Gold Digger, Meander ve Black Jack; 230–259 trend/oynaklık filtreleri; 260–345 risk, para yönetimi ve portföy. S. 97–99'daki MA eğimi, Gold Digger'ın ardışık gün yönleri ve Bollinger osilatörü mevcut MA/geri dönüş aileleridir. S. 107–110'daki volatiliteyle **kanal bakış süresini değiştirme**, aynı dinamik kırılım ailesinde ikincil varyanttır. S. 111'de volatilitenin **kırılım fiyatına doğrudan eklenmesi** ayrı test edilebilir eşik üretir.

### TS198A — standart sapma tamponlu Donchian kırılımı

- **Kaynak:** PDF s. 106–111; özellikle s. 110–111 TradeStation örneği. `HistVol=0.5×StdDev(C,30)` veya aynı katsayıyla `ATR30`; long giriş `Highest(High,20)+HistVol`, short giriş `Lowest(Low,20)−HistVol`; long çıkış `Lowest(Low,20)−0.5×HistVol`, short çıkış `Highest(High,20)+0.5×HistVol`. Yazar, girişin çıkıştan daha zor olmasını hedefler. Kod ertesi gün stop emirleri kullanır; buradaki kapalı mum yürütmesi, aynı seviyelerin günlük kapanışla teyit edilen **ayrı uyarlamasıdır**.
- **Veri ve eşik:** D1 OHLCV, en az 30 tamamlanmış gün ve 20 günlük high/low. Her gün `t−1` kapanışında `upper=max(H[t−20:t−1])+0.5×sample_std(C[t−30:t−1])`; `lower=min(L[t−20:t−1])−0.5×sample_std(...)`. Karşı kanal çıkışları aynı geçmiş 20 günlük uç ve `0.25×sample_std` kullanır. `std=0` veya eksik veri varsa yeni giriş yok. Mevcut bar hiçbir eşiğin hesabına sokulmaz.
- **Kapalı mum sinyali:** Düzken gün `t` kapanışı `close_t>upper` ise long, `close_t<lower` ise short. İki yön aynı anda olamaz; her sembolde tek pozisyon. Sinyal sonrası ilk uygulanabilir M1 açılışında giriş. Long açıkken `close_t<min(L[t−20:t−1])−0.25×std30[t−1]`, short açıkken ters üst sınır kapanışı çıkıştır; sonraki ilk M1'de kapat. Aynı gün yeni ters pozisyon açılmaz. Stop veya çıkış sonrası aynı yönde yeniden giriş ancak fiyat bir gün yeniden kanalın içine kapandıktan sonra gelen yeni dış kapanışla olur; böylece her dış kapanış ayrı işlem sayılmaz. Eşikler her gün yeniden hesaplanır ve gevşeyebileceği için ayrıca sabit acil stop gerekir.
- **Risk ve kıyas:** Girişte `2×ATR14` acil stop, stopa göre işlem başına özsermayenin en çok `%0,25`i ve toplam brüt maruziyet `1×`; ilk M1'den itibaren gerçek zamanlı uygulanır. Kaynak bu risk parametrelerini s. 111'deki giriş koduna bağlamaz; test için bizim sabit yürütme sözleşmemizdir. Aynı veri, risk ve maliyetlerle **tamponu sıfır olan Donchian20/20** ve `0.5×ATR30` tamponu ayrı karşılaştırma kolları. Ücret, spread, kayma, funding/roll, M1 stop/giriş sırası ve sürekli vadeli seri ayarlama yöntemi noktasal zaman bilgisine göre işlenir. Eğitim/dış örneklem ayrımı, parametre denemeleri ve işlem örtüşmesi raporlanır. Kitabın s. 111'deki tarihsel sonuçları maliyet düşülmeden verilmiştir; adayın getirisi henüz ölçülmedi.

## 2. Martin Pring — Fiyat Kalıpları (350 sayfa)

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 11/Baskı 11/Fiyat Kalıpları - Martin Pring (350 sayfa) - @eseckal.pdf>) · [tam metin](02_price_patterns_pring.txt)

**Tam okuma:** S. 1–72 trend, destek/direnç ve hacim; 73–210 dikdörtgen, baş-omuz, çift/üç tepe-dip, üçgen, kama, elmas ve yuvarlanan yapı; 211–258 bayrak, flama, gap ve kısa vadeli formasyonlar; 259–313 iç bar, anahtar dönüş, pin bar ve iki bar dönüşü; 314–350 trend ve formasyon değerlendirmesi. Bu formasyon aileleri önceki partilerde kayıtlı. S. 88–91 kırılımın formasyon içine dönüşü ve s. 249–251 kırılım sonrası geri çekilme aynı sahte kırılım/retest adaylarına kontrol koludur. Çizilen trend çizgisi ve “anlamlı” temaslar algoritma olmadan geriye dönük öznel kalır; aynı aileyi yeni sayıyla şişirmedik. **Yeni aday: 0.**

## 3. Carley Garner — Daha Yüksek Olasılıklı Emtia Ticareti (432 sayfa)

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 11/Baskı 11/Daha Yüksek Olasılıklı Emtia Ticareti - Carley Garner (432 sayfa) - @eseckal.pdf>) · [tam metin](03_commodity_garner.txt)

**Tam okuma:** S. 1–53 kaldıraç, marj ve ürün; 54–89 MA/osilatör/kanal; 90–149 emtia temelleri ve mevsimsellik; 150–169 COT ve piyasalar arası bağlar; 170–229 swing/trend ve emir türleri; 230–279 vadeli spread/opsiyon; 280–359 portföy ve uygulama; 360–432 risk, stop ve opsiyonla koruma. Teknik MA, RSI, stokastik ve kanal yaklaşımları mevcut ailelerle örtüşüyor. S. 101–131 mevsimsellik için sözleşme/vintage ve tarihsel raporlar, s. 151–165 COT için yayımlanma zamanı belli CFTC pozisyon verisi, s. 230–279 ve 385–425 için vade/opsiyon fiyatları gerekir. Bunlar tekil kapalı OHLCV mumlarından dürüstçe türetilemez; veri sağlanırsa ayrı kapsamda ön kayıt yapılabilir. **Yeni aday: 0.**

**Parti sonucu:** 3 PDF, **1.127 sayfa**, **1 yeni doğrulanmamış aday**. Kümülatif **594 PDF, 37.241 sayfa, 437 doğrulanmamış aday**.
