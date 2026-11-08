# Kitap okuma 008 — RSI scalping, aralık/EMA sıçraması, CCI geri çekilmesi

**Kapsam:** Üç PDF'nin **30 + 27 + 35 = 92 PDF sayfası** sayfa sırasıyla incelendi. Sayfalar PDF sayfasıdır. Kitapların seçilmiş grafiklerinden kârlılık sonucu çıkarılmadı. Aşağıdaki tam sayısal kurallar kaynakta olmayan yerde açıkça **bizim test uyarlamamız** olarak belirtildi. Bu partide backtest/paper emir yok.

## 1. You Learn Forex — RSI Pro Scalping Stratejisi

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 9/Baskı 9/RSI Pro Scalping Stratejisi - You Learn Forex (30 sayfa) - @eseckal.pdf>)

Yazar M5 üzerinde RSI(8), RSI üzerine SMA(3) ve fiyat üzerine SMA(24) kullanıyor (s. 6, 10, 13, 24–29). Yükselen piyasada RSI ve fiyatın birlikte yukarı döndüğü *vadi*; düşende ikisinin birlikte aşağı döndüğü *tepe* giriş fikri (s. 10–11, 15–21). RSI Paint göstergesinin PR/NR/ND sinyalleri de anılıyor, fakat PDF bu kapalı göstergenin hesaplama formülünü vermiyor (s. 8, 12–14, 20, 23–26). Makro haber ve altın/Dow yorumları fiyat OHLCV'sinden türetilemez. Forex seansı 07–12 EST ve broker minimum stopu kriptoya taşınmaz. Kitap s. 8'de grafikten sonradan giriş seçmenin geriye bakış olduğunu kabul ediyor; bu yüzden pivotu oluştuğu anda değil, **teyit edildiği anda** kullanıyoruz.

### RP1 — M5 RSI vadisi/tepesi ve fiyatla aynı yönlü dönüş

- **Özgün fikir:** Yönü piyasa bağlamıyla seç; long için RSI vadisi ardından RSI ve fiyat birlikte yukarı, short için RSI tepesi ardından ikisi birlikte aşağı (s. 10–11, 19–21). Stop için ATR(3) ve spread toplamı alternatif olarak verilir (s. 29–30); tam hedef ve pozisyon kapama eşiği sayısal değildir.
- **Bizim kapalı M5 tanım:** `SMA24_price[t]>SMA24_price[t-1]` ve `close[t]>SMA24_price[t]` long rejim. `RSI8[t-2]>RSI8[t-1] && RSI8[t]>RSI8[t-1]` ile t kapanışında **bir bar gecikmeli** vadi teyidi; `RSI8[t]>SMA3(RSI8)[t]`, `close[t]>close[t-1]` ve `close[t]>open[t]` birlikte şart. Short tam simetri. Vadi/tepe tanımı ve SMA3 filtresinin zorunlu olması bizim mekanikleştirmemizdir. Önce yalnız RSI dönüşü + fiyat yönü, sonra SMA3 ve SMA24 filtrelerinin marjinal etkisi test edilir.
- **Yürütme:** Sinyal t M5 kapandıktan sonra ilk yürütülebilir 1m'de piyasa girişi. Başlangıç stopu `min(low[t-1],low[t])-ATR3_M5[t]` (short ters); bu mesafe, kaynağın ATR3+spread fikrinin açık bir varyantıdır, spread ayrıca gerçek yürütme maliyetinde sayılır. 1R/2R ve 6/12/24 M5 barı çıkışlar ayrı; kitap bu hedefleri vermez. Aynı varlıkta tek pozisyon, dolum/maliyet ve fiyat yolundaki 1m stop/TP sırası raporlanır.
- **Durum:** Kaynağın gerçek yöntemi haber ve RSI Paint gerektiren takdirî sistem. RP1 yalnız **mekanik alt hipotez** olarak işaretlenir; M5 veri yeterliliği doğrulanmadan günlük deneyle birleştirilmez. Özellikle scalp ücret ve kayması brüt hareketi yiyebilir.

## 2. Nikos Mermigas — Forex Bounce Trading Stratejisi

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 9/Baskı 9/Forex Bounce Trading Stratejisi - Nikos Mermigas (27 sayfa) - @eseckal.pdf>)

İki ana aile: yatay aralık sınırından dönüş ve trend içinde eski seviye/EMA dönüşü (s. 8). Aralık için 2–3 destek/direnç teması, sınırda renk değiştiren **kapanmış** mum, karşı aralık sınırı hedefi ve isteğe bağlı orta noktada yarım çıkış anlatılır (s. 11–16). EMA200/633 teması sonrası yönlü ilk mum kapanışında üç parça pozisyon; 1R, 2R, sonraki önemli seviye hedefleri (s. 17–19). Kanal/kama ve sahte kırılım örnekleri s. 20–24'tedir. “Piyasa zamanın %85'inde aralıkta” iddiası (s. 17) ölçülmüş veri olarak alınmadı.

### B1 — Önceden dondurulmuş günlük aralığın kenarından dönüş

- **Kaynak kuralı:** En az 2–3 görünür destek/direnç tekrarı, sınırdan sıçrayıp renk değiştiren mum kapanışı, stop sınırın ötesi, hedef karşı kenar; orta noktada kısmi çıkış (s. 11–16). Çizim toleransı ve bakış süresi kaynakta sayısal değil.
- **Bizim kapalı günlük tanım:** Her t-1 sonunda geçmiş 30 kapanmış bardan alt/üst bölgeyi hesapla: `L=min(low[t-30:t-1])`, `U=max(high[t-30:t-1])`. `U-L>=2 ATR14[t-1]`; her sınırın `±0.25 ATR` yakınında, birbirinden en az 3 gün ayrı **en az iki** temas ve geçmiş 20 günde `close` ile sınır dışına kırılım yok. Bölge `t-1`de dondurulur. t için long: `low[t]<=L+0.25 ATR`, `close[t]>open[t]`, `close[t]>L`; short ters. `30`, `20`, `0.25 ATR`, `2 ATR`, temas ayrımı bizim parametrelerdir. Aynı t gününün uçları aralığı yeniden çizmek için kullanılmaz.
- **Giriş/çıkış:** Sinyal kapanışından sonraki ilk 1m; stop `L-0.1 ATR` (short `U+0.1 ATR`), hedef aralık orta noktası için %50 azaltma ve karşı kenarda kalan çıkış. Yalın karşı kenar/2R ve 3/7/14 gün alternatifleri. Hedef/stop mesafesi `>=1` ve `>=2` R filtreleri ayrı; risk filtresi kaynaktaki “hedef alandan küçük olmasın” fikridir (s. 16).
- **Çakışma:** Önceki S1 başarısız kırılım, D1 talep bölgesi ve F1 reddedilme günü aynı barı işaretleyebilir. Tek olay kimliği ve fiyat sınırı türüyle karşılaştır; dört bağımsız işlem sayma.

### B2 — EMA200 veya EMA633 temasından trend yönüne kapanış

- **Kaynak kuralı:** Büyük hareket sonrası EMA200/633'e dokunma, üstten geliyorsa ilk boğa, alttan geliyorsa ilk ayı mumunun kapanışı; stop sıçrama mumunun dışı; 1R, 2R, sonraki direnç için üç parça (s. 17–19). “Büyük hareket” eşiği ve EMA altından/üstünden gelişin süresi kitapta net değil.
- **Bizim kapalı günlük tanım:** `EMA_N[t-1]>EMA_N[t-2]` ve son 10 günün en az 7 kapanışı EMA_N üstünde ise long rejim (`N=200` veya `633`). t günü `low[t]<=EMA_N[t] && close[t]>EMA_N[t] && close[t]>open[t]` ilk temas/kapanış sinyali; öncesinde en az beş kapalı gün EMA_N'e değmemiş olacak. `7/10`, beş gün ve günlük zaman dilimi bizim seçimimiz. Short simetri. EMA633 için en az 633 günlük ısınma ve likit tarih gerek.
- **Yürütme:** t sonrası ilk 1m, stop t dibi `-0.1 ATR`, 1R/2R ve önceden teyitli pivot hedefi üç parça veya tek parça bazları; 3/7/14 gün çıkış. EMA200 ile EMA633 aynı sinyali verirse bir olay. Önceki EMA30 fitil K1 ve ortalama geri çekilme fikirlerine göre ek katkısı ölçülür.

## 3. TradersGPS — Kazandıran Stratejiler

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 9/Baskı 9/Kazandıran Stratejiler - TradersGPS (35 sayfa) - @eseckal.pdf>)

Yazar günlük swing için SMA20/40 eğimi ve hizası, CCI5'in aşırı satım/alım ziyareti, 20–40 SMA alanına geri çekilme ve önceki gün ekstremumu üstünden/altından stop giriş tarif ediyor (s. 6–15). Stop önceki mum dibi/tepesi, önceki tepe/dip ilk hedef; beş işlem gününde zaman stopu (s. 20–31). Ayrıca haftalık EMA10/50 kesişimiyle pozisyon yönü öneriyor (s. 32–33). Kitap hisse senedi seanslarına dayanıyor; açılış gapleri ve %5 kâr sonrası stop taşıma kriptoya aynen aktarılmaz. S. 1'deki canlı getiri ve kazanma oranı iddiaları bağımsız doğrulanmış veri değil. S. 14'te nötr CCI ile isteğe bağlı işlem, baz kurala dahil edilmedi.

### G8 — SMA20/40 trendinde CCI5 geri çekilmesi

- **Kaynak kuralı:** Uzun için iki SMA yukarı eğimli, SMA20>SMA40, CCI5 daha önce `<-100`, düşük SMA20'ye değmiş veya altına geçmiş, kapanış SMA40 üstünde; önceki gün tepesinin bir fiyat adımı üstünde alım. Kısa yön simetri, CCI5 `>+100` (s. 11–15). Kitap s. 12'de 10 SMA'ya sığ dönüşe izin verir; bu bazın ayrı varyantı.
- **Kapalı günlük kurulum:** `SMA20[t]>SMA20[t-1]`, `SMA40[t]>SMA40[t-1]`, `SMA20[t]>SMA40[t]`; `min(CCI5[t-5:t])<-100`; `low[t]<=SMA20[t] && close[t]>SMA40[t]`. Böylece t kapanınca önceki gün tepesinin neresi olduğu bilinir. t+1 için `entry=high[t]+1 tick`, `stop=low[t]-1 tick`; short ters. CCI ziyareti için altı bar pencere **bizim** seçimimiz. CCI standart tipik fiyat `(H+L+C)/3` ve ortalama mutlak sapma formülüyle hesaplanmalı. Önceki gün ile “bugünün dibi” ifadesi (s. 13) için giriş anında bilinmeyen t+1 dibini stopta kullanma.
- **Emir/çıkış:** Pending stop giriş yalnız t+1 günü geçerli; girişten önce `low[t]-1 tick` görülürse iptal. Hedef t itibarıyla **teyitli** son pivot high; hedef girişe göre `>1R` değilse işlem dışı filtre ayrı. Baz çıkış 2R ve 5 takvim günü; kitapta 5 **hisse işlem günü** olduğundan kripto 24/7'de 5/7 gün varyantları ayrı. İlk stop ve zaman çıkışı zorunlu; s. 21'deki %30/%30/kalıntı çıkış ile s. 30'daki girişten sonra `%5` hareket olunca break-even/takip stopu yürütme ablation'ıdır. `%5` kripto volatilitesiyle otomatik eşdeğer sayılmaz.
- **Ayrıştırma:** SMA20/40 bölgeye dönüş bazına karşı CCI5 filtresi, SMA eğimi ve 10 SMA sığ dönüşün artı değeri. Önceki MA/RSI pullback adayları ve B2 EMA sıçramasıyla örtüşme; tek işlem evreninde karşılaştır.

### G9 — Haftalık EMA10/50 kesişimi, ayrı zaman ölçeği

- **Kaynak:** Tamamlanmış haftalık grafikte EMA10 üstten/altan EMA50 kesişimiyle yön (s. 32–33). Kitap çıkış/stop/pozisyon büyüklüğü için bu stratejide tam plan vermez.
- **Sözleşme:** UTC pazartesi 00:00 sınırına kadar **tamamlanmış** 7 günlük hafta barlarından EMA10/50; `EMA10[w-1]<=EMA50[w-1] && EMA10[w]>EMA50[w]` boğa, tersi ayı. Sonraki ilk yürütülebilir 1m giriş. Karşı kesişim veya 4/8/12 haftalık zaman çıkışı; başlangıç stopu `2×ATR14_weekly` bizim risk varsayımımız. Günlük strateji havuzuna eklenmez, haftalık kohort ve maliyet/funding ayrı raporlanır. Daha önceki MA kesişimlerinin başka parametre/zaman ölçeği varyantı olarak sayılır.

## Test sırası ve kayıt ilkeleri

1. **Öncelik:** G8 ve B1 kapalı günlük olayları; B2 uzun ısınma ve önceki EMA adaylarıyla örtüşme nedeniyle ikinci adım. RP1 ayrı M5 veri/maliyet uygunluğu araştırması; G9 haftalık baz karşılaştırması.
2. Her sinyalde kaynak PDF sayfası, olay zamanı, o anda dondurulan seviye, veri geçerliliği, tetik ve dolum/iptal, stop/TP, maliyet, funding, net R, MAE/MFE ve çakışan aday kimlikleri saklanacak. Gelecekte teyit edilecek pivot veya sonradan değişen aralık geçmiş sinyale yazılmayacak.
3. Eğitim/dış örneklem zaman ayrımı, likidite filtresi, BTC rejimi, parametre duyarlılığı ve çoklu deneme maliyeti olmadan strateji “işe yarıyor” diye etiketlenmeyecek. Backtest veya paper işlem bu partide yapılmadı.
