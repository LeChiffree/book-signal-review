# Kitap okuma 053 — Gerçek açılış boşluğu, EMA200 retesti ve 2B sahte kırılım

**Kapsam:** 29 + 45 + 11 = **85 PDF sayfası**. Üç PDF'nin tüm sayfaları numaralı, sıralı metne çıkarıldı; atıflar PDF sayfasıdır. Kaynakta Forex/hisse özgü koşullar ile **bizim** OHLCV test kuralları ayrı belirtilmiştir. Backtest, paper test ve emir yapılmadı.

## 1. Jayesh Shah — GAP Trading

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/GAP Trading - Jayesh Shah (29 sayfa) - @eseckal.pdf>) · [Tam metin](01_gap_trading_shah.txt)

**Kaynak:** Kitabın “gap” tanımı önceki işlem gününün **kapanışı ile sonraki seans açılışı** arasında gerçek, işlemsiz fiyat boşluğudur (s. 2–7). Yazar %3+ gap up ve ortalama hacmin yaklaşık 3 katı hacimle hisse seçer (s. 10, 17), boşluk gününde almaz, o günün high seviyesini dondurur ve sonraki günler high aşılırsa long girer (s. 11–12, 17). Giriş günü low'unun altı stop örneğidir (s. 17–18); uyarı mumu, bir önceki gün low'u ile izleyen stop ve parça çıkış varyantları bulunur (s. 19–24). Eski direncin üstüne gerçek boşlukla çıkışa öncelik, direnç altında kalan boşluktan kaçınma anlatılır (s. 25–27). s. 12–16'daki seçilmiş hisse getirileri ve s. 18'deki “10 kez 7'si stopa gitmez” ifadesi genellenmiş performans kanıtı değildir.

### GS53 — Gerçek seans boşluğu sonrası gün high kırılımı (kripto için ertelendi)

- **Uygulanabilirlik:** Standart 7/24 BTC/ETH D1 UTC mumlarında günler arası sınırda normalde borsa kapanışı/açılışı ve **işlemsiz seans boşluğu yoktur**. `open[t]−close[t−1]` küçük farkını veya veri kesintisini kitapta anlatılan hisse gap'i yerine koymak yanlış hipotezdir. Bu nedenle mevcut kripto backtest/paper havuzuna **alınmaz**. Ancak gerçek seanslı hisse/ETF ve tarihsel point-in-time fiyat+hacim verisi sağlanırsa aşağıdaki sözleşme uygulanabilir.
- **Gelecekteki ayrı piyasa sözleşmesi:** Seanslı günlük OHLCV'de `open[t]≥1.03×close[t−1]` ve `volume[t]≥3×mean(volume[t−20:t−1])`; ortalama yalnız önceden kapanmış 20 seans. Gap günü `t` işlem yok; gün kapanınca `high[t]` dondurulur. `t+1`'den sonraki 20 seans içinde fiyat high üstüne 1 tick aşarsa, yalnız sonraki uygulanabilir fiyat ve maliyetle giriş. Seansın ilk dakikasındaki gap üzerinden doldurulmuş varsayılmaz. Stopu giriş **gününün tamamlanmış low'una** bağlamak intraday girişte geleceği kullanır; bunun yerine giriş anına kadar gerçekleşen gün içi low `−1 tick` veya önceden bilinen gap günü low'u ayrı kollar olarak dondurulmalı. 2R/20 seans süre bizim çıkış seçimimiz. Bu kol **yalnız veri ve varlık evreni değişince** gündeme gelir.
- **Karar:** Kripto için “gap stratejisi” diye sahte varyant üretme. Kitaptan taşınabilir sınama, gap sonrası yüksek kırılımında **bir tam gün beklemenin** etkisidir; ancak gap olayı gerçek değilse bu kaynak stratejisi sayılmaz.

## 2. Laurentiu Damir — Günde 50 Pips Stratejisi

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Günde 50 Pips Stratejisi - Laurentiu Damir (45 sayfa) - @eseckal.pdf>) · [Tam metin](02_fifty_pips_damir.txt)

**Kaynak:** Kitap H4'te 200 EMA'nın eğimi ve fiyatın EMA tarafıyla ana yön belirler (s. 8–12, 27). Ana trende **ters eğimli** en az iki temaslı destek/direnç çizgisinin kırılması, eski seviyeye retest ve güçlü yönde kapanış mumu temel sıradır (s. 28–36). Giriş mumu önceki 2–4 muma göre büyük gövdeli, kapanışı ekstremine yakın olmalıdır (s. 31–34). Stop retest ekstremi dışı; hedef önceden çizilen çizgi veya başka destek/dirençle riskten fazla potansiyel göstermelidir (s. 37–44). Yazar kırılımı ve mum onayını yalnız **kapanınca** geçerli sayar (s. 19, 21). “50 pip/gün” başlığı bir garanti değildir; kaynağın kendisi farklı örneklerde 420/550 pip seçilmiş işlem sonucu anlatır (s. 38). Forex pip sınırları kripto stop/hedefi olamaz.

### FD53 — EMA200 yönünde karşı eğimli çizgi kırılımı ve ilk retest

- **Bizim önceden bilinen yapı:** H4 gerçek OHLC; `EMA200_H4`, en az 300 H4 bar ısınma. Long yalnız son tam H4 `close>EMA200` ve `EMA200[t]>EMA200[t−3]`; short simetri. Long düzeltmesinde iki **teyitli** (2 sol/2 sağ) daha alçak swing high; araları 4–40 H4 bar. Bu iki noktadan karşı eğimli direnç çizgisi `L(k)`; ikinci swing teyit edilince dondurulur. Short iki yükselen swing low ile karşı eğimli destek çizgisi. Fiyat yeni bir pivot oluşturunca çizgiyi en iyi uyacak şekilde geriye dönük değiştirme. Pivot/süre ve eğim tanımı **bizim** nesnelleştirmemizdir.
- **Kırılım ve retest:** Long ilk H4 `close>L(t)+0.1 ATR14_H4`; short altında. Bundan sonra en çok 8 H4 bar içinde ilk bar `low≤L(t)+0.1 ATR` (short `high≥L(t)−0.1 ATR`) ile çizgi çevresine döner. Retest barı veya onu izleyen en çok 3 H4 barda long `close>L(t)` ve sinyal gövdesi önceki 4 H4 gövde medyanından büyük, kapanış kendi aralığının üst %25'inde; short simetri. Teyit olmadan emir yok. Tolerans, 8/3 bar ve gövde eşiği **bizim** sabitlememiz; kaynak “güçlü mum” nitel tanımlar (s. 31–36).
- **İcra/risk:** Teyit H4 kapanışı sonrası ilk uygulanabilir 1m giriş. Long stop kırılım sonrasındaki ilk retestten sinyale kadar **gözlenmiş** minimum gerçek low `−0.1 ATR`; short max high `+0.1 ATR`. 2R veya 24 H4 bar süre; stop yanlış tarafta veya toplam maliyetin iki katından dar ise atla. 2R hedef bizim standart kol; kaynağın eğimli çizgi hedefi yalnız önceden dondurulmuş ikinci çizgi ile ayrı test edilebilir. Aynı 1m stop/hedefte kötümser sıra.
- **Karşılaştırma:** Batch020 KL20a/b, batch036 T36, batch047 FT47 ve diğer trend çizgisi retestleriyle aynı olaylarda çakışma; EMA200 ve büyük gövde filtrelerinin ayrı marjinal katkısı. Kaynak günlük pip hedefi sonuç değildir.

## 3. Teknik Analizde Ayak İzleri

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Teknik Analizde Ayak İzleri (11 sayfa) - @eseckal.pdf>) · [Tam metin](03_footprints.txt)

**Kaynak:** Başlık “ayak izi” olsa da kitap bid/ask footprint veya order flow matrisini değil, **2B tepe/dip sahte kırılımı**, sapma ve iki temaslı trend çizgisini anlatır (s. 1–11). 2B tepede eski yüksek aşılır, sonra pokebar low'unun **altında kapanan** teyit mumu ardından short; 2B dipte simetrik yüksek üstü teyit (s. 1–2). Yanlış kırılımın aynı aralığa dönüşü (s. 3–4), stokastik/RSI tipi sapmayı yalnız teyit sayma (s. 8–9) ve çizgi reddinden sonra çizginin doğru yanında kapanma (s. 10) vardır. s. 2 dip için stopu “ikinci ayağın en yüksek noktası” diye yazar; long stop için mantıksal yön yanlışıdır, longda ikinci dip altı kullanılmalıdır. s. 11'deki artan kaldıraçla kayıpları kapatma söylemi kural/test kanıtı değildir; risk artırma önerisi olarak benimsenmez.

### FP53 — 2B sahte kırılım + pokebar ekstremi teyidi

- **Bizim pivotlar:** H1 gerçek OHLC; ilk swing high/low ancak 2 sol/2 sağ bar kapandıktan sonra teyitli. İlk high seviyesi `H1` dondurulur. Short için en çok 40 H1 sonra bir **tamamlanmış** pokebar `high>H1+0.1 ATR14_H1` ve `close>H1`; long ilk low `L1` altında `low<L1−0.1 ATR`, `close<L1`. Poke bar olayı kaynak s. 2'nin “yeni yüksek/düşük üzerinde kapanma” koşuluna uygundur. 0.1 ATR ve 40 bar **bizim** tolerans/penceremizdir.
- **Teyit:** Poke bar sonrası en çok 5 H1 bar içinde ilk short `close<pokeLow`, long `close>pokeHigh`; koşulun oluştuğu bar kapanmadan sinyal yok. İkinci high/low olarak pokebar ekstremi alınır; aynı kurulumda ikinci poke veya daha iyi ekstrem seçme. Önceden ters teyit gelirse iptal. Bu yöntem s. 1–2'deki iki aşamalı kırılmayı tekrar üretir; yalnız eski H1/L1 altına geri kapanışı daha erken, **ayrı** hassasiyet kolu.
- **İcra/risk:** Teyit H1 kapanışı sonrası ilk uygulanabilir 1m giriş. Short stop pokebar high `+0.1 ATR`, long pokebar low `−0.1 ATR`; 2R veya 24 H1 bar süre. Stop yanlış tarafta, maliyetten dar veya sinyalden önce stop ekstremi yeniden geçilmişse atla. Aynı 1m stop/hedefte kötümser sıra. Kitabın kaldıraçla ekleme fikri uygulanmaz.
- **Karşılaştırma:** Batch011 DP11a, batch028 G28b ve önceki 2B/likidite süpürmesi adaylarıyla aynı sinyallerde olay örtüşmesi. Pokebar ekstremi teyidinin yalnız seviyeye geri kapanmaya kıyasla gecikme, işlem sayısı ve net sonucunu ölç.

## Ortak test notu

FD53 ve FP53 yalnız kapanmış mumlar ve point-in-time pivotlar ister; sonraki uygulanabilir 1m dolum, ücret/spread/kayma/funding, varlık evreni, eksik bar ve pozisyon çakışması gerekir. GS53 gerçek seans boşluğu olmayan kripto evreninde **uygun değil**; veri kesintisini gap olarak sayma. Hiçbir adayın kârlılığı henüz ölçülmedi.
