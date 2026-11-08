# Kitap okuma 099 — mumlar, emir blokları ve maliyet duyarlı scalp

**Kapsam:** Daha önce tamamlanmamış üç PDF'nin **23 + 27 + 33 = 83 PDF sayfası** baştan sona okundu. Tam sayfa metinler aşağıda; grafik/kural taşıyan 30 sayfa [görsel denetlendi](figure_contacts/). **Bir yeni araştırma adayı** açıldı. Sayfalar PDF sayfasıdır. Backtest, paper test ve emir yapılmadı.

## 1. Kripto Ticaretinde Mum Grafiklerini Okumak İçin Profesyonel Bir Kılavuz — Emily Dhruv

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 18/Baskı 18/Kripto Ticaretinde Mum Grafiklerini Okumak İçin Profesyonel Bir Kılavuz - Kripto Paranızı Nasıl Koruyacağınızı Keşfedin - Emily Dhruv (23 sayfa) - @eseckal.pdf>) · [Tam metin](01_crypto_candles_dhruv.txt)

**Sayfa haritası:** s. 1–5 OHLC ve mum gövde/fitil; 6–10 destek/direnç, trend ve daha yüksek zaman dilimi; 11–16 yutan, çekiç, kayan yıldız, asılı adam ve üçgen; 17–23 kripto cüzdan güvenliği. S. 13 çekiç için **mum kapanışını bekleyip sonra high geçişinde** giriş, s. 10 formasyon karşı ucundan tamponlu stop anlatır.

**Karar:** Çekiç high kırılımı, yutan mum ve üçgen önceki [mum/formasyon adaylarında](../batch_003/STRATEGIES.md) mevcut. “Önemli” destek/direncin seçimi nesnel verilmediği için geriye dönük çizilen seviyeleri yeni sinyal saymıyoruz. S. 11'de asılı adamı destek yakınında boğa diye yorumlaması klasik tepe bağlamıyla karışıyor; s. 5'te 50.000 üstü örneği 60.000 reddiyle karıştırılıyor. Son bölüm cüzdan güvenliği, işlem işareti değil. Yeni aday açılmadı.

## 2. Order Block Trading — Emily Dhruv

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 18/Baskı 18/Order Block Trading - Emily Dhruv (27 sayfa) - @eseckal.pdf>) · [Tam metin](02_order_block_dhruv.txt)

**Sayfa haritası:** s. 1–10 varsayımsal kurumsal emir blokları, konsolidasyon/hacim ve direnç süpürmesi; 11–15 seans açılış aralığı; 16–21 mum/yutan ve aralık kırılımıyla “emir akışı” yorumu; 22–26 gerçek seans boşluğu ve dolum/reddedilme; 27 sonuç.

**Karar:** S. 5–7 aralıkta yüksek hacim ve ardından destek/direnç kırılımı, [kutu kırılımı](../batch_023/STRATEGIES.md) ile örtüşür. OHLCV'den **hangi banka veya merkez bankasının emir verdiği** tanımlanamaz; s. 4 Level 2 emir miktarından söz etse de işlem uygulanacak eşik ve veri kaynağı vermez. S. 11–15 ORB zaten kayıtta; s. 22–26 boşluk dolumu ve geri reddi önceki gap adaylarına yakındır. “Boşlukların >%90'ı dolar” s. 23–26 iddiasında evren, süre ve sayım yöntemi bulunmaz, olasılık kabul edilmez. Geriye bakarak doldurulan gap'i seçip açılışta işlem sinyali saymak lookahead olur. Yeni aday açılmadı.

## 3. Scalping Stratejileri — S. Connell

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 18/Baskı 18/Scalping Stratejileri - S. Connell (33 sayfa) - @eseckal.pdf>) · [Tam metin](03_scalping_connell.txt)

**Sayfa haritası:** s. 1–6 plan ve scalp tanımı; 7–12 yavaş MA eğimi yönünde hızlı MA geri çekilmesi ve kitap içi test tabloları; 13–19 dış Bollinger bandından merkeze dönüş, bant genişliğine göre stop/hedef ve örnekler; 20–23 otokorelasyon örneği; 24–28 spread/komisyon duyarlılığı; 29–33 kaldıraç, stop ve evren. Kaynakta M1/M5 FX pip değerleri ve broker varsayımları vardır; kripto para fiyatına sabit pip olarak taşınmaz.

### BC99 — Dış Bollinger temasından bant içine dönüş, genişliğe bağlı mikro hedef

- **Kaynak çekirdeği:** Alt/üst dış Bollinger bandına temas, fiyatın bandın merkezine doğru geri çekilmeye başlaması ve yönlü giriş; yaklaşık **bant genişliğinin %5'i** kâr hedefi, stop **genişliğin yarısından fazla değil** (s. 13–16). Kitap birden fazla küçük pozisyonu dizi halinde açar ve 10.000 USD başına 1 FX lot toplam tavan verir (s. 13–17). Dönüşü barın **içinde** gözler; yalnız OHLC kapanmış mumla bire bir replikasyon mümkün değildir. S. 15'te stop cümlesinin çevirisi muğlak olsa da 20 pip bant için 10 pip stoplu tablo, yarım genişlik yorumunu destekler. S. 18–19 test koşuları işlem listesi, veri ve kodla bağımsız doğrulanmış sonuç değildir.
- **Bizim tek pozisyonlu kapalı mum pilotumuz:** Başlangıç evreni yüksek likit BTC/ETH perpetual M1; M5 ayrı duyarlılık kolu. Tamamlanmış barlarda `mid=SMA20(close)`, `sigma=population_std20(close)`, `upper/lower=mid±2sigma`, `W=upper−lower`; 100 bar ısınma. Long `low[t]≤lower[t] && close[t]>lower[t]`, short `high[t]≥upper[t] && close[t]<upper[t]`. Bant/temas barı tamamen kapandığı anda sinyal, giriş ancak sonraki ilk uygulanabilir bid/ask M1 kotasyonu. Long ve short sinyali aynı barda veya `W≤0` ise işlem yok. Bant penceresi, kapanışla içeri dönüş ve eşik yorumları **bizim mekanik uyarlamamızdır**.
- **Filtre/risk/çıkış:** Kaynak dar aralıkta iyi ve trendde kötü der (s. 13–15); bizim ana kolumuzda `ADX14[t]<20` ve son 20 M1 mid çizgisi eğiminin mutlak değeri `<0.1 W` şartı, filtresiz kol kontrol. Tek sembolde **en fazla bir pozisyon**; kaynakta geçen üst üste ekleme ilk deneyde uygulanmaz. Giriş fiyatından `0.5 W[t]` stop, `0.05 W[t]` hedef; 10 M1 bar süre çıkışı ve en fazla 0.25% özsermaye planlı risk. ADX eşiği, eğim, 10 bar, risk ve tek pozisyon **bizim seçimlerimizdir**. Gidiş-dönüş spread+komisyon+kayma tahmini `0.05W` hedeften küçük değilse sinyal **başlamadan** elenir. Aynı M1 stop/hedef belirsizliğinde stop önce, kotasyon yoksa iyimser OHLC dolumu yok. Stop, gap/kaymayla beklenen kaybı aşabilir.
- **Karşılaştırma ve karar kapısı:** Yalın BB dış bant teması, kapalı mumla içeri dönüş, ADX/eğim filtreli sürüm ve [önceki BB dönüş adayları](../batch_071/STRATEGIES.md) aynı maliyet/veriyle ölçülür. `0.5W` stop ve `0.05W` hedefin brüt başabaş kazanma oranı **%90,91**'dir; ücretler bunu artırır. Kaynak s. 24–28 küçük spread farkının kârı tersine çevirebildiğini gösterir. Gerçek kotasyon, derinlik ve işlem maliyeti olmadan bu adayı paper teste alma. Kitap içi geçmiş getirisi kripto beklentisi değildir.

**Açılmayan fikirler:** S. 7–10 yavaş MA eğimiyle hızlı MA'ya karşıt çekilme, önceki MA trend/geri çekilme ailesine tekrar. S. 20–23 otokorelasyon hesaplaması var ama hangi pencere/eşik, long-short kararı ve stop/çıkış birleştirilmemiş; araştırma özelliği olabilir, ayrı işlem stratejisi değil. Dizi halinde ortalama almak ek maliyet ve birikimli risk taşır; tek giriş pilotu makul sonuç vermedikçe aynı barlarda çoğaltılmayacak.
