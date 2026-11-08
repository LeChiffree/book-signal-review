# Kitap okuma 038 — trend fanı, EMA200 uyumu, üç kapanış

**Kapsam:** 43 + 25 + 14 = **82 PDF sayfası**. Her kitabın tüm sayfaları sıralı metinde; grafik ağırlıklı Yang s. 14/24, Damir s. 15 ve Trend Kırıcı s. 6 ayrıca görsel incelendi. Atıflar PDF sayfasıdır. Kaynağın kuralı ile bizim kripto deney parametreleri ayrıdır. Backtest, paper test ve emir yapılmadı.

## 1. Albert Yang — Trend Çizgileri

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 5/Baskı 5/Trend Çizgileri - Albert Yang (43 sayfa) - @eseckal.pdf>) · [Tam metin](01_trendlines_yang.txt) · [Fan s. 14](yang_p14.png) · [Kırılım seviyeleri s. 24](yang_p24.png)

**Kaynak:** Bir trend çizgisinin bitiş noktasını sonraki çizginin başlangıcı yaparak art arda çizgilerden “fan” kurar (s. 11–16). İki kullanım ayrıdır: geçmiş ekstremumdan sonraki ekstremuma kadar fan ve kırılma noktaları (tip 1), geçmiş ekstremumdan **mevcut** fiyata kadar çizilen fanın pürüzsüzlük göstergesi (tip 2; s. 18–24, 35–39). Fanın kırılma ve uç noktaları yatay destek/direnç olarak önerilir (s. 24–33); iki karşı fanın yakın eğimleri kama/karar bölgesi oluşturabilir (s. 40–42). S. 14/24 şekilleri hangi ara noktanın hangi çizginin bitişi olacağını gösterir, ancak kesin algoritma önceki **ayrı** kitaptaki trend çizgisi tanımına dayanır (s. 12–13). S. 25 güçlü desteğin altına geçilmeden short düşünmeme ve s. 26 direncin üstüne stop örnekleri vardır. Kaynakta emir zamanlaması, tolerans ve çıkış kuralları yok. Fanı geçmiş grafik üzerinden sonradan çizmek ileriye bakma riski taşır.

### Y38 — Teyitli fan kırılma düzeyinin ek filtre olarak denenmesi

- **Bizim H4 araştırma tanımı:** Sağında ve solunda üçer tamamlanmış H4 bar bulunan pivotları yalnız sağ onay barı kapandıktan sonra kullan. Son 120 H4 içindeki **onaylı** en yüksek pivot `A` ve ondan sonra onaylanan en düşük pivot `B` ile düşüş kolu; yükseliş kolu simetrik. A–B arasında ardışık en az üç onaylı alt tepe üzerinden çizilen eğimlerin monoton değişmesi ve birbirini takip etmesi durumunda “fan” adayı; son fan segmentinin geçmişte onaylanan kırılma yüksekliği/düşüklüğü yatay düzey `F`. Yeni H4 kapanışı `F±0.1 ATR14` dışına çıkarsa yalnız var olan trend kırılımı adaylarına filtre. Pivot 3/3, 120, segment sayısı, monotonluk ve ATR **bizim** seçtiğimiz nesnel yaklaşım; yazarın çiziminin eşdeğeri olduğu iddia edilmez.
- **Karar:** Çizgi zincirinin eşsiz biçimde seçilememesi ve önceki kitabın eksik olması nedeniyle **bağımsız al/sat stratejisi olarak ertelendi**. Test edilirse stop/2R/20 H4 bar mevcut trend kırılımı sözleşmesinden alınır ve fanın ek bilgisi karşılaştırılır. S. 24'teki yatay seviyeler yalnız oluştukları anda bilinen noktalardan türetilir; sonradan belirlenen uçlar geçmiş sinyallere uygulanmaz.

## 2. Laurentiu Damir — Destek Direnç Bölgeleriyle Günlük Trade

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 7/Baskı 7/Destek Direnç Bölgeleriyle Günlük Trade - Laurentiu Damir (25 sayfa) - @eseckal.pdf>) · [Tam metin](02_zones_damir.txt) · [Giriş grafiği s. 15](damir_p15.png)

**Kaynak:** H4 **ve** H1'de fiyat EMA200'ün aynı tarafında, EMA eğimi de o yönde olmalı; EMA'yı sık sık kesen yatay piyasa elenir (s. 5–8). H1'de benzer büyüklükte önemli destek/direnç dönüşleri izlenir (s. 9–12). Kırılım mumu seviyenin ötesinde kapanmalı ve gövdesinin **yarısından fazlası** dışarıda olmalı; sırf küçük mumun bu eşiği karşılaması yetmez (s. 12–14). Kırılım sonrası seviye retesti, retest başladığı kırılım yönündeki fiyatın stop emriyle aşılması ve retest ucunun ötesine stop (s. 15–17). S. 15 grafiği retest **sonrasında** sell-stop'u önceki dipte, stopu retest tepesinde gösterir. Kârda kama/karşı trend çizgisi kırılımı, yoksa H1 EMA200 karşı kapanışı çıkış olarak anlatılır (s. 18–21); eski dirençleri birleştiren çizgi TP için önerilir (s. 24–25). Kama sıklığı ve örnek getiriler doğrulanmış performans değildir. “Retestin bittiği” nokta ancak sonraki fiyatlarla bilinir; geçmişe giriş yazılamaz.

### D38 — İki zaman dilimi EMA200 + güçlü gövde + retest devam emri

- **Bizim H1/H4 hazırlık:** H1 `t` kapanışında en son **tam kapanmış** H4 barını kullan. Long için her iki çerçevede `close>EMA200` ve `EMA200[t]>EMA200[t−5]`; ayrıca son 20 barda EMA200'ü kesen kapanış sayısı en fazla 2. Short simetrik. H1'de son 80 tamamlanmış barda 3-sol/3-sağ onaylı, en az `1 ATR14_H1` salınım genlikli pivotlardan düzey oluştur; en az iki tepki `±0.2 ATR` yakın olsun. Genlik, pencere ve dokunuş eşiği bizim operasyonelleştirmemizdir.
- **Kırılım:** Long H1 mumunda `close>level+0.1 ATR`, mumun **gerçek gövdesinin** düzey üstündeki payı >%50 ve `abs(close−open)>=median(abs(close−open),önceki 20 H1)`; short simetrik. Kaynaktaki gövde yarısı kuralı korunur; medyan “küçük değil” için bizim ölçümüzdür.
- **Retest ve icra:** Kırılımdan sonraki 8 tamamlanmış H1 içinde fiyat düzeyin `±0.2 ATR` bölgesine döner; retest mumunun kapanışında kırılım tarafında kalır. O anda bilinen retest uçlarıyla long buy-stop `max(high[break],high[retest])+0.1 ATR`, stop `min(low[retest penceresi])−0.1 ATR`; short simetrik. Emir sonraki 4 H1 içinde **gelecekte tetiklenirse** gir; önceden dolmuş sayma. Stop yanlış tarafta veya maliyetin 2 katından yakınsa sinyal yok. 3R veya H1 EMA200 karşı kapanışı ayrı çıkış kolları; 48 H1 bar zaman sınırı. Kırılım/retest penceresi, ATR tamponları ve hedef bizim test tanımıdır. Kaynaktaki kamayı pivot algoritması olmadan varsayılan çıkışa ekleme.
- **Karşılaştırma:** EMA200 filtreli/kaldırılmış ve retestli/doğrudan giriş kollarını aynı kırılım olaylarında ölç; önceki destek/direnç retest kayıtlarıyla çakışmayı say.

## 3. Trading Strategy Guides — Trend Kırılımı Strateji Rehberi

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 10/Baskı 10/Trend Kırılımı Strateji Rehberi - Trading Strategy Guide (14 sayfa) - @eseckal.pdf>) · [Tam metin](03_trend_break_guide.txt) · [Kural görseli s. 6](guide_p6.png)

**Kaynak:** MACD(12,26,9), SMA8 ve EMA20; H4/H1'de en az **üç** destek veya direnç temasıyla trend çizgisi, M15'te gösterge kesişimleri ve çizginin ötesinde **üç kapanmış mum** bekleme (s. 3–6). S. 6 metni kesişimlerin çizgi teması/kırılımından **önce** olmasını şart koşar; M15 yön ifadesinde çeviri tutarsız olsa da örneklerde yukarı kırılım alış, aşağı kırılım satış (s. 10–13). Son M15 destek/direnç ötesine stop (s. 7–8), hedef **3R** (s. 8). S. 9 hesap riskini %2'nin altında tutmayı önerir. Pivot seçimi, çizgi toleransı, kesişimlerin ne kadar önce olması gerektiği ve geçersizlik süresi verilmez. Görseldeki üç mum tamamlanmadan sinyal oluşmaz.

### G38 — Önceden teyitli iki kesişim + üç M15 kapanış trend çizgisi kırılımı

- **Bizim H4/H1 çizgi:** Her iki çerçevede pivotlar 3-sol/3-sağ kapalı barla teyitli. Son 80 H1 içindeki aynı yönde üç onaylı pivot high veya low üzerinden ilk ve son pivotu birleştir; orta pivot çizgiye `<=0.2 ATR14_H1` uzaklıkta, üç pivot kronolojik ve birbirinden en az 4 H1 bar aralıklı. H4'te aynı yönlü trend durumu son 3 teyitli swing ile belirlensin. M15 kapanış anında yalnız o anda onaylanmış H1/H4 pivottan çizgiyi ileri uzat; yeni pivotla geçmiş çizgiyi yeniden kurma. Bu seçim algoritması tamamen bizimdir.
- **Tetik:** Long için M15 MACD çizgisi sinyali aşağıdan yukarıya ve SMA8 EMA20'yi aşağıdan yukarıya **çizgi ilk aşılmadan önceki 12 tamamlanmış M15 bar içinde** kessin; iki kesişim için yön aynı, sıra serbest. Ardından çizginin `0.1 ATR14_M15` üstünde art arda **üç M15 kapanışı**; üçüncü kapanıştan sonraki ilk uygulanabilir 1m'de giriş. Short simetrik. Kesişim penceresi ve ATR tamponu bizim varsayımımız; kaynak sadece önce olmasını ve üç kapanışı söyler.
- **Risk/çıkış:** Long stop en son **teyitli** M15 pivot low `−0.1 ATR`; short simetrik. Stop geçerli değil veya maliyetin 2 katından yakınsa sinyal yok. Kaynağa uygun hedef 3R; 96 M15 bar zaman sınırı bizim. Üçüncü kapanışa kadar MACD/SMA sinyali tersine dönerse iptal varyantı ayrı ölçülsün. %2 hesap riski, pozisyon boyutlandırmada **üst sınır** olarak kaydedilir; kârlılık iddiası değildir.
- **Karşılaştırma:** Aynı çizgi kırılma anında 1 kapanış/3 kapanış, yalnız MACD/ikili kesişim, 2R/3R kolları. Üç kapanış daha geç giriş ve daha az sinyal getirebilir; bunu sonuçtan önce varsayım olarak ölç.

## Ortak test notu

Öncelik **D38** ve **G38**: ikisinde de kaynak tetik koşulları açıktır; **Y38** önce çizgi üretiminde birebirlik sorunu çözülene kadar ek filtre hipotezi. Point-in-time varlık evreni, yalnız kapanmış mum, doğru zaman dilimi birleşimi, sonraki uygulanabilir fiyat, ücret/spread/kayma/funding, aynı bar stop-hedef sırası ve zaman sıralı dış örneklem zorunludur. Kaynak örnekleri backtest sonucu değildir.
