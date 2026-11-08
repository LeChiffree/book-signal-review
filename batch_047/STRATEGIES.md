# Kitap okuma 047 — Heikin Ashi scalp devamı, RSI varyantları ve Fibonacci trend çizgisi

**Kapsam:** 44 + 58 + 25 = **127 PDF sayfası**. Üç PDF'nin mevcut tüm sayfaları sıralı metne aktarıldı; atıflar PDF sayfasıdır. Kaynakta geçen nitel çizim/örnekler ile bizim kapalı mumlu kripto test seçimleri ayrı işaretlendi. Backtest, paper test ve emir yapılmadı.

## 1. Heikin Ashi Trader — Eğlenceli Scalping 2

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 17/Baskı 17/Eğlenceli Scalping 2 - Heikin Ashi Trader (44 sayfa) - @eseckal.pdf>) · [Tam metin](01_scalping_fun_2.txt)

**Kaynak:** İlk ciltteki HA renk değişimi kuralına, güçlü hareketten sonra mumların küçülmesi, doji/topaç oluşumu ve ilk ters renkli **tamamlanmış** mum teyidi eklenir (s. 7–13). Doji/topaç tek başına trendin biteceği garantisi değildir (s. 10–12). Ters renkte pozisyon kapama veya önceden bilinen destek/dirençte hedef alma seçenekleri vardır (s. 13–15, 17–18). Önceki günün dip/tepe seviyesindeki renk dönüşleri (s. 27–29) ve kırılan desteğin dirence dönüşü (s. 27) giriş bağlamıdır. Yazar s. 33–39'da çok güçlü **trend gününde** ilk küçük ters renkleri körlemesine işlememenin önemini, ana yöne geri çekilme sonrası katılmayı anlatır. Forex pip ve yuvarlak sayı örnekleri kriptoya evrensel eşik vermez. S. 41–44 üçüncü cildin tanıtımıdır.

### HF47 — Önceki UTC gününün seviyesinde HA zayıflama ve ters renk

- **Bizim gösterge/veri:** M1 gerçek OHLC'den standart HA; hesaplanan HA fiyatından dolum yapma. Önceki **tam UTC gününün** gerçek `high`/`low` seviyeleri, bugünkü tüm M1 barları için önceden bilinir. Gün sınırı ve temas toleransı bizim sabitlememizdir. En az 100 M1 bar ısınma; point-in-time hacim/spread kapısı.
- **Olay:** Short: son 10 M1 bar içinde önceki günün high seviyesine `≤0.2 ATR14_M1` mesafede veya üstüne temas; en az 3 yeşil HA mumundan sonra `HA_body/HA_range≤0.2` doji/topaç, ardından ilk kırmızı HA **kapanışı**. Long önceki gün low'da tersi. Doji sinyali en çok 3 bar geçerli; karşı renkli kapanıştan sonraki ilk uygulanabilir 1m fiyatı giriş. `0.2 ATR`, gövde oranı ve üç bar penceresi **bizim** tanımımız; kaynak yalnız nitel şekli tarif eder.
- **Trend günü kapısı:** Short için son tam H4 bar `close>EMA50` ve EMA50 son 3 H4 barda artıyorsa karşı trend sinyali **ayrı yasak kolunda** atılır; long tersidir. Bu s. 33–39'daki “güçlü trende kör karşı işlem açma” uyarısının bizim ön kayıtlı temsilidir. Temel kol filtresiz, filtreli kol ayrıca test edilir; H4 kapanmamış mum kullanılmaz.
- **İcra/risk:** Stop short sinyal anına dek oluşmuş son 10 M1 gerçek yüksek `+0.1 ATR`, long düşük `−0.1 ATR`; ilk ters HA rengi kapandığında sonraki 1m çıkış. Ayrıca stop, 15 M1 bar süre ve sinyal anında bilinen önceki 10 M1 karşı swing seviyesinde sabit hedef **ayrı** kol. Stop mesafesi toplam maliyetin iki katından azsa giriş yok. Forex pipleri kullanılmaz.
- **Karşılaştırma:** Batch046 HS46 ilk renk dönüşüyle **aynı olaylarda** doji ve önceki gün seviyesinin marjinal katkısı; `doji+seviye`, yalnız doji, yalnız seviye, çıplak renk dönüşü. Seçilmiş grafik örnekleri sonuç kanıtı değildir.

## 2. Alpesh Pansheriya — RSI

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 20/Baskı 20/RSI - Alpesh Pansheriya (58 sayfa) - @eseckal.pdf>) · [Tam metin](02_rsi_pansheriya.txt)

**Kaynak:** Wilder tarzı 14 periyot RSI ve alternatif periyot/eşikler (s. 4–5, 10–13). 30 altından 30 üstüne dönüş ile long, 70 üstünden 70 altına dönüş ile short (s. 18–19, 29, 32); bu batch046 RS46a ile aynı aile. Fiyat daha düşük dip, RSI daha yüksek dip yaparsa boğa uyumsuzluğu; tersi ayı (s. 19). RSI “swing rejection” için 30 altı→30 üstü→30 üstünde ikinci dip→ara RSI tepesini kırma long; 70 üstü→70 altı→70 altında ikinci tepe→ara RSI dibini kırma short (s. 19–20). Ayrıca RSI trend çizgisi kırılımı ve RSI+MA kesişimi önerilir (s. 20–22). BTC örneğinde 30 üstüne dönüşe MACD yükseliş teyidi eklenir (s. 32–34). Kitap çok sayıda kavram/örnek içerir; parametreleri genişçe arayıp test döneminde seçmeyi haklı çıkarmaz.

### RP47 — RSI swing rejection için teyitli durum makinesi

- **Bizim gösterge:** H4 gerçek kapanışta Wilder RSI14 (`gain/loss` için başlangıç SMA14, sonra RMA14), 100 bar ısınma. Long durum sırası: (1) kapanış `RSI<30`; (2) ilk kapanış `RSI>30`, o ana kadarki yükselişin **ilk** RSI tepesini ilerideki 2 sol/2 sağ barla teyit et; (3) teyitli RSI dip `>30` ve ilk dipten yüksek; (4) daha önce sabitlenmiş RSI tepesinin üzerine ilk kapanış. Her olay ancak oluştuğu kapanışta bilinir; sağ bar teyidi tamamlanmadan pivot kullanma. `2+2`, en çok 30 H4 bar ve eşitliğin geçersiz sayılması bizim nesnelleştirmemizdir. Short 70 üstü, 70 altı ve ara dip kırılımıyla simetrik.
- **İcra/risk:** Son durumun tamamlandığı H4 kapanışı ardından ilk uygulanabilir 1m giriş. Long stop kurulum başlangıcından sinyale kadar görülen **gerçek** low'un `−0.1 ATR14_H4` altı, short yüksek üstü; 2R hedef veya 24 H4 bar süre, karşı yönde RSI50 kapanışında erken çıkış ayrı kol. Risk kuralları kaynakta nicel verilmez, bizimdir. Stop yanlış tarafta veya maliyetten dar ise atla.
- **Karşılaştırma:** Basit RSI30/70 çıkışı RS46a ve batch044 RS44 başarısızlık salınımıyla formasyon sırası/olay örtüşmesini ölç; RSI swing rejection bağımsız alfa varsayılmaz. 14/7/21 varyantı yalnız eğitim dönemi ön kaydıyla, test döneminde yeniden seçilmez.

### RP47b — RSI 30 dönüşüne MACD teyidi

- **Kaynak dayanağı ve bizim filtre:** Kitabın BTC örneği RSI30 üstü dönüş ve MACD yükseliş onayı içerir (s. 32–34), fakat “yükseliş onayı” kesin tanımlanmaz. D1'de ilk `RSI[t−1]<30`, `RSI[t]≥30` kapanışında `MACD12,26[t]>signal9[t]` **veya** histogram `hist[t]>hist[t−1]` kollarını **ayrı** dene; short 70 altı ve karşı yönde aynı koşullar. Giriş sonraki 1m, stop son 10 D1 bar ekstremi `±0.1 ATR14`, 2R veya 10 D1 bar çıkış. Göstergeler kapalı t barından hesaplanır. Aynı RS46a sinyallerine MACD filtrelemesinin net etkisi doğrudan ölçülür.

## 3. Fibonacci Trend Çizgisi Strateji Rehberi

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 8/Baskı 8/Fibonacci Trend Çizgisi Strateji Rehberi - Trading Strategy Guides (25 sayfa) - @eseckal.pdf>) · [Tam metin](03_fibonacci_trendline.txt)

**Kaynak:** Trend çizgisinin geçerli sayılması için en az **iki** fitil/mum teması istenir (s. 5–6, 24). Yükselişte teyitli swing dip→tepe, düşüşte tepe→dip Fib; fiyat düzeltmede trend çizgisine **%38,2–61,8 bölgesi içinde** temas etmeli (s. 2, 4, 7, 9). Long için ilgili bölgeye göre %38,2 veya %50 üstünde, short için altında **mum kapanışı** beklenecek; %50–61,8 bölgesine inen long ancak %50 üstü kapanırsa (s. 10–11, 15). Kaynak örneğinde stop %50–61,8 arasında ama genel olarak önceki destek/dirence göre seçilir; 3R/4R hedef örnekleri vardır (s. 11–14). Trend çizgisinin elle çizimi, swing'in sonradan seçilmesi ve stop yeri öznel bırakılmıştır.

### FT47 — İki teyitli temasla trend çizgisi + Fib bölgesinde retest

- **Bizim noktasal yapı:** H1 gerçek OHLC'de swing high/low ancak 2 sol/2 sağ bar kapandıktan sonra teyitli. Long için iki **yükselen** teyitli dip `L1=(i,low_i)`, `L2=(j,low_j)`, `8≤j−i≤80` ve `low_j>low_i`; bunlardan destek doğrusu `T(t)` geçirilir, yalnız `L2` teyit anından sonra kullanılabilir. Fib impulsu `L2` ile ondan **sonra gelen ve iki sağ barla teyitli** son tepe `H` arasında dondurulur; arada yeni düşük varsa iptal. `F382=H−0.382(H−L2)`, `F50=H−0.5(H−L2)`, `F618=H−0.618(H−L2)`. Short iki alçalan tepe ve sonraki teyitli dip için simetrik. Bu pivot pencereleri ve tek impuls seçimi bizimdir.
- **Olay:** İmpuls teyidinden **sonra** ilk H1 barın gerçek low'u `F618≤low[t]≤F382` ve destek doğrusu `|low[t]−T(t)|≤0.1 ATR14_H1` olsun; ayrıca mum `close[t]>F382` eğer temas `low[t]≥F50`, aksi halde `close[t]>F50`. Short ters. Trend çizgisi altında H1 kapanışı gelirse kurulum iptal. Fiyat temas edip kapanış teyidi vermezse en çok 3 H1 bar bekle; teyit gelecekteki barın kendi kapanışında, eski mumda sinyal varmış gibi sayılmaz. Temas toleransı ve 3 bar bizimdir.
- **İcra/risk:** Teyitli H1 kapanışından sonraki ilk uygulanabilir 1m giriş. Stop long `min(L2,T(t),F618)−0.1 ATR14_H1`, short simetrik; kaynak örneğinin %50–61,8 arası stopu özellikle derin temasta yanlış tarafta kalabilir, bu nedenle bu **bizim daha tutarlı** dış stop koludur. Kaynağa yakın daha dar stop yalnız sığ temaslarda ayrı hassasiyet kolu. 3R hedef, 24 H1 bar süre, stop/hedef aynı 1m'de ise kötümser sıra. Stop yanlış tarafta veya risk/ödül net maliyet sonrası uygunsuzsa atla.
- **Karşılaştırma:** Fib bölgesi tek başına, trend çizgisi tek başına, birleşim; batch042 F42 golden-zone ve batch044 kanal stratejisiyle olay örtüşmesi. Trend çizgisini sonradan en iyi duran iki dip üzerinden tekrar çizme.

## Ortak test notu

Point-in-time varlık evreni, yalnız kapanmış mum, sonraki uygulanabilir 1m fiyatı, ücret/spread/kayma/funding, pozisyon çakışması ve zaman sıralı dış örneklem zorunlu. HF47'de M1 maliyet ve H4 filtresi, RP47'de pivot teyidinin gecikmesi, FT47'de çizgi/Fib ankrajının donması ilk teknik kontrollerdir. Kârlılık henüz ölçülmedi.
