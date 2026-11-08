# Kitap okuma 162 — trend çizgisi geri testi, arz/talep ve dirgen

Üç ayrı PDF'nin **44 + 42 + 53 = 139 sayfası** sırayla incelendi. Kennedy'nin s. 24–26 grafik sayfaları ayrıca [görsel olarak](kennedy_page-24.png) denetlendi. Atıflar PDF sayfasıdır. **Yeni bağımsız strateji adayı: 1.** Backtest, paper test veya emir yapılmadı.

## 1. Çizgiyi Takas Etmek — Jeffrey Kennedy

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 14/Baskı 14/Çizgiyi Takas Etmek - Trend Çizgilerini Kullanarak Dönüşleri Tespit Etmek ve Trendleri Yakalamak - Jeffery Kennedy (44 sayfa) - @eseckal.pdf>) · [tam metin](01_trade_the_line_kennedy.txt)

**Tarama:** s. 1–4 çizgi tanımı; 5–20 trend çizme, tam mumla geçiş ve üçlü yelpaze; 21–27 boşlukla kırılım ve çizgi geri testi; 28–30 Elliott kanalı; 31–41 Kennedy kanalı; 42–44 soru/yanıt. s. 21–23 gerçek işlem boşluğu hisse/vadeli seanslarına aittir; 7/24 kriptoda normal bitişik mumlar bunu karşılamaz. s. 31–41 Elliott dalga sayımı, pivot/dalga etiketleri geriye dönük yeniden yorumlanmadan tam mekanik değildir.

### JK162A — Tam mumla trend çizgisi kırılımı, geri test ve kırılım tepesinin aşılması

- **Kaynak:** s. 24–26: İki tepeyle çizilen aşağı eğimli çizginin üzerinde iki mumun *dipleri* kalınca kırılım teyidi; sonra çizgiye bir veya iki geri test; ilk kırılma hareketinin yüksek seviyesinin yeniden aşılmasıyla long; stop test hareketinin düşük seviyesi. Bu, yalnız çizgiye dokunma girişinden farklıdır. [20. partinin](../batch_020/STRATEGIES.md) çizgi+MACD kırılımından ve [22. partinin](../batch_022/STRATEGIES.md) çizgi teması geri çekilmesinden olay sırası ve teyit bakımından ayrılır.
- **Ön kayıtlı çizgi:** BTCUSDT/ETHUSDT spot H4 kapanmış mum. Pivot tepe, `high[i]` çevresindeki iki sol ve iki sağ mumun yükseklerinden büyükse ancak `i+2` kapandıktan sonra bilinir. O anda bilinen son iki **alçalan** pivot tepe en az 5 H4 bar aralıklı olsun; ikinci pivot onayında `L(k)=h2+(h2−h1)*(k−i2)/(i2−i1)` çizgisini bu kurulum için dondur. Çizgi eğimi negatif olmalı. Yeni pivot çizgiyi geriye dönük değiştirmez. Kaynağın elle seçilen tepelerini nesnel pivotla değiştirmek **bizim test uyarlamamızdır**.
- **Olay/giriş:** İkinci pivot teyidinden sonraki ilk ardışık iki tamamlanmış H4 barın `low>L(k)` olması kırılım teyidi; ilk barın high'ı `H_break` olarak dondurulur. Sonraki en çok 10 tamamlanmış H4 içinde ilk `low<=L(k)+0,1×ATR14_H4` ve `close>L(k)` geri testi tespit edilir; çizgi altında H4 kapanışı olursa kurulum iptal. Geri testten sonraki en çok 5 tamamlanmış H4 içinde ilk `close>H_break` long tetik; aynı olaydan tek işlem. Pencere, ATR yakınlık tamponu ve kapanışla tepe aşımı **bizim seçimimizdir**. Çizgi fiyatı bar zamanında hesaplanır; gelecekteki temas pivotu kullanılmaz.
- **İcra/risk:** Tetik kapanışı sonrası ilk uygulanabilir 1m açılışta long. Stop geri test barı low'unun `0,1×ATR14_H4` altı; girişten önce hedef `entry+2R`, en çok 24 H4 bar sonra süre çıkışı; çizgi altına H4 kapanışı olursa sonraki 1m çıkış. Stop doğru tarafta değilse veya ücret sonrası 2R hedef geçersizse işlem yok. Spot, kaldıraçsız, işlem başına özsermayenin %0,25'i risk. Komisyon, spread ve kayma uygulanır; aynı 1m içinde stop/hedef çakışırsa stop önce. ATR ve 1m geçmişi yoksa işlem yok.
- **Ayrıştırma:** Çizgi üstü iki tam mum filtresiz, geri testsiz saf çizgi kırılımı ve [22. partideki](../batch_022/STRATEGIES.md) çizgi temasıyla aynı veri/masraf ve pivot algoritması altında kıyasla. İşlem sayısı, net/medyan R, maksimum düşüş, 1–2 test ayrımı, pivot genişliği ve H4/H1 duyarlılığı, dönem dışı ve BTC/ETH ayrı raporlanır. Seçilmiş grafikler performans kanıtı değildir.

## 2. Arz ve Talep Ticaretini Kolayca Öğrenin — Jason Applebaum

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 25/Baskı 25/Arz ve Talep Ticaretini Kolayca Öğrenin - Jason Applebaum (42 sayfa) - @eseckal.pdf>) · [tam metin](02_supply_demand_applebaum.txt)

**Tarama:** s. 1–12 ekonomik arz/talep eğrileri; 13–22 teknik bölge çizimi; 23–24 stop ve 3–4R; 25–30 yalnız taze bölge, yapı değişimi, Fibonacci %50–88,6 ve limit/teyit giriş planı; 31–37 puanlama ve başarısız bölge; 38–42 kurumsal anlatı ve sonuç.

**Karar:** s. 25 ilk temas filtresi ve s. 29–30 yapı kırılımı sonrası taze bölgeye dönüş, Fibonacci %50–88,6 ile 3R hedef mevcut [arz/talep](../batch_005/STRATEGIES.md), [OB %50](../batch_054/STRATEGIES.md) ve [OTE/geri test](../batch_145/STRATEGIES.md) ailelerinin bileşimidir. Kaynak s. 19/22 talep mumunu son **düşüş** mumu diye tanımlar, s. 30 ise satın alma limiti için son **yükseliş** mumu der; bire bir kodlama çelişir. 31–33 puanlamada puan bileşenleri sabit ağırlıkla tanımlanmadığı için yeni kapalı kural sayılamaz. **Yeni bağımsız aday yok**; ilk temas ve 3R mevcut adayların ablation koşulları olarak değerlendirilebilir.

## 3. Andrews Pitchfork Kullanarak Bereketli Trading Kazançları Elde Edin — Bryan V. Post

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 19/Baskı 19/Andrews Pitchfork Kullanarak Bereketli Trading Kazançları Elde Edin - Bryan V Post (53 sayfa) - @eseckal.pdf>) · [tam metin](03_pitchfork_post.txt)

**Tarama:** s. 1–10 medyan çizgi ve üç pivot; 11–17 çizgiye dönüş, kırılma ve beş kural; 18–26 Schiff kaydırması, paraleller/enerji; 27–45 destek/direnç, Fibonacci, hacim; 46–53 göstergeler ve sonuç. Medyan çizgi/Schiff çizgisi temasları, [62. partideki Andrews adayının](../batch_062/STRATEGIES.md) çizim ailesindedir. s. 14–16 çizgi ihlali ve yeniden test, kırılım ailesiyle çakışır; pivot A/B/C seçiminde tek nesnel algoritma verilmez. %80 çizgiye ulaşma iddiası (s. 11) test edilmemiş genellemedir. **Yeni bağımsız aday yok.**

**Parti sonucu:** 3 kitap, 139 sayfa, 1 yeni aday. Birikmiş toplam **393 doğrulanmamış strateji adayı**.
