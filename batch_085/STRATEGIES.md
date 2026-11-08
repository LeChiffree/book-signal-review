# Kitap okuma 085 — FX fiyat yapısı, kanal kırılması ve gösterge birleşimleri

**Kapsam:** Daha önce tamamlanmamış üç PDF'nin 43 + 34 + 77 = **154 PDF sayfası** okundu. Grafik, giriş kuralı ve tablo içeren seçilmiş sayfalar [görsel kontrol](figure_contacts/) ile karşılaştırıldı. Kaynakların örnek grafikleri performans kanıtı değildir. Bu dosya strateji **hipotezlerini** kaydeder; backtest, paper test ve işlem yapılmadı. Sayfa numaraları PDF sayfalarıdır.

## 1. En İyi 10 Forex Stratejisi — AuthenticFX / Erron Adams

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 5/Baskı 5/En İyi 10 Forex Stratejisi - Authentic FX (43 sayfa) - @eseckal.pdf>) · [Çıkarılan tam metin](01_authentic_fx.txt)

**Sayfa haritası:** s. 1–4 giriş; 5–12 Bladerunner EMA20 geri testi; 12–17 günlük Fibonacci/pivot; 17–21 BB bant sıçraması; 21–27 iki stokastik; 27–29 çakışan Fibonacci bölgeleri; 30–31 Londra çekiç; 32–34 Bladerunner reversal; 34–39 yukarı/aşağı pop/drop-and-stop; 40–43 yatay kanalın kırılması ve yeniden testi (yazarın “fraktal”ı). Grafikleri görsel olarak s. 6, 14, 19, 23, 26, 30, 33, 35, 39, 41–43'te kontrol ettim.

### AF85A — Yavaş stokastik trendiyle hızlı stokastik ters çekilmesi

- **Kaynak kuralı:** Yazar H1 örneğinde yavaş stokastik `(21,10,4)`, hızlı stokastik `(5,2,2)` ve EMA20 kullanır. Düşen eğilimde yavaş stokastik ≤20 iken hızlı stokastik ≥80'e çıktığında, EMA20 çevresindeki ayı dönüş mumu short için izlenir; yükselen eğilimde yavaş ≥80, hızlı ≤20 ve boğa mumu tersidir (PDF s. 21–27). Bu, iki osilatörün farklı ölçeklerde zıt uçlarda olmasını kullanır. Kaynak EMA yakınlığını, mum biçimini ve stopu sayısallaştırmaz.
- **Bizim kapalı mum tanımı:** Günlük UTC kararında yalnız son 24 kapanmış H1 üzerinden stokastik fast/slow üret. `%K` için rolling yüksek/düşük, sıfır aralıkta sinyal yok; üçlü parametreyi `(lookback, K SMA, D SMA)` olarak yorumla ve bu yorumu test manifestine kilitle. Long: son kapanmış H4 `close>EMA20`, H1 yavaş `%D≥80`, son üç kapanmış H1'den birinde hızlı `%D≤20`, son H1 `close>open`, `low≤EMA20+0,2 ATR14` ve `close>EMA20`. Short tam simetrik. H4 trend filtresi, 3 bar bekleme, ATR toleransı ve mum tanımı **bizim uyarlamamızdır**; kaynakta H1 eğilim/20EMA anlatımı vardır. Günlük karar öncesi aynı olay için tek sinyal.
- **İcra/risk:** Sinyal sonrası ilk uygulanabilir 1m açılışında giriş. Long stop son üç kapalı H1 diplerinin altına `0,1 ATR14`, short tersi; stop mesafesi ≤ maliyet tahmini ise atla. Ayrı 1R ve 2R tam çıkış kolları, en çok 3 gün; kaynakta başka Bladerunner için 1R/2R kullanılır, bu stratejinin açık çıkışı değildir. Ücret, kayma, funding, aynı 1m stop/TP çakışmasında stop önceliği. H1 olayunu yalnız günlük karara taşımak önemli sinyal gecikmesi yaratır; H1 icralı bağımsız test bu sözleşmeden ayrıdır.
- **Örtüşme/ablation:** [Stokastik ve EMA fikirleri](../batch_052/STRATEGIES.md) ile aynı karar günlerinin Jaccard oranını ölç. Yavaş trend filtresi, hızlı ters uç, EMA/mum teyidi katmanlarını sırayla çıkar; yavaş stokastik aşırı uç tek başına kârlılık iddiası değildir.

**Ayrı stratejiye yükseltilmeyenler:** EMA20 geri testi (s. 5–12), BB dış bant dönüşü (s. 17–21), dar aralıktan retest (s. 34–43) önceki EMA/BB/kanal adaylarıyla örtüşür. Günlük FX pivotu ve Londra/New York seansı (s. 12–17, 30–31, 35–38) sürekli kripto piyasasına doğrudan aktarılamaz; özellikle “hafta sonu boşluğu” gerekçesi uygun değildir. “Fraktal” burada Bill Williams beş mum fraktali değil, yazarın elle çizdiği yatay aralıktır. Sonradan çizilen sınırlar sinyal tarihine geri taşınamaz. Fib swing/pivot çizimlerinde kesin pivot teyidi olmadığı için ayrıca aday açılmadı.

## 2. Forex Trading Stratejileri — Edmund Loh

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 15/Baskı 15/Forex Trading Stratejileri - Edmund Loh (34 sayfa) - @eseckal.pdf>) · [Çıkarılan tam metin](02_edmund_loh.txt)

**Sayfa haritası:** s. 1–7 giriş ve piyasa tanıtımı; 8–9 emir türleri; 10–13 trend/duygu yorumu; 14–15 kısa/orta/uzun trend çizgileri; 16–20 disiplin; 21–22 kanal kırılımı; 23–24 ticari ürün karşılaştırması; 25–26 destek/direnç kırılması; 27–30 grafik/faiz; 31–34 otomasyon. S. 14, 21, 25, 33 görsel incelendi; işlem grafiği, tarihli performans tablosu veya tam mekanik parametre yok.

**Kural denetimi:** S. 21–22'de fiyatın üst kanal çizgisini aşmasını long, alt çizgiyi aşmasını short olarak anlatır; s. 25–26 kırılmayı geri çekilme beklemeye tercih eder; s. 33–34 yeni yüksek/düşük ve momentum teyidini önerir. Ancak kanal çizgisinin uç noktaları, kapanış teyidi, stop ve çıkış nicelleştirilmez. Bu fikir mevcut [kanal kırılımı adayları](../batch_073/STRATEGIES.md) ile aynı çekirdektedir; **yeni strateji başlığı açılmadı**. Kaynaktaki otomatik getiri ve “kayıp olmaz” iddiaları test verisi olarak kullanılmaz. Faiz farkı anlatımı kripto perpetual funding'inin yerine geçmez.

## 3. Günlük Trading Stratejilerinde İndikatörlerin Kullanımı — Lawrence Keaton

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 21/Baskı 21/Günlük Trading Stratejilerinde İndikatörlerin Kullanımı - Lawrence Keaton (77 sayfa) - @eseckal.pdf>) · [Çıkarılan tam metin](03_keaton_indicators.txt)

**Sayfa haritası:** s. 1–14 gösterge seçimi ve Klinger/MA örneği; 15–19 osilatör uçları ve PMax/RSI5; 20–41 on topluluk osilatörü; 42–53 beş trend göstergesi; 54–66 beş gün içi sistem; 67–77 dört scalping sistemi. Giriş kuralı görselleri s. 11, 18, 21, 23, 27, 55, 58, 60, 63, 65, 68, 71, 73, 75'te kontrol edildi. Kaynak topluluk betiklerinin sürüm, kod ve repaint davranışını vermez; bu betiklere dayalı renk/oklar tek başına yeniden üretilebilir sinyal sayılmaz.

### LK85A — Stokastik(22,5,9) ön koşulu ve EMA5/11 çaprazı

- **Kaynak kuralı:** Long için stokastik `%K` `%D`'yi 50 altında yukarı keser, sonra EMA5 EMA11'i yukarı kesince gir; short için 50 üstünde aşağı ve EMA5 EMA11 aşağı çaprazı (s. 58–59). Long çıkış EMA ters çaprazı veya 75 üstünde aşağı stokastik; short çıkış EMA ters çaprazı veya 25 altında yukarı stokastik. Kaynak stop vermez.
- **Bizim kapalı mum tanımı:** H4'te tam kapanmış barlarla `(K lookback=22, K smoothing SMA5, D SMA9)` üret. Stokastik olayı oluştuktan sonraki en çok altı H4 bar içinde EMA5/EMA11 çaprazı kapanırsa kurulum; çapraz anında stokastik yönü hâlâ geçerli olmalı. Eş zamanlı çapraz kabul. Altı bar bekleme ve H4'e taşıma **bizimdir**. Günlük UTC kararında en son teyitli kurulum alınır, aynı stokastik olayı tekrar kullanılamaz.
- **İcra/risk:** İlk uygulanabilir 1m açılışı. Long stop son altı H4 low'unun `0,1 ATR14` altı, short simetrik; 2R sabit TP veya kaynak ters çapraz çıkışı ayrı ön kayıtlı kollar. En çok 7 gün süre **bizimdir**. Yanlış taraf stop, yetersiz veri ve stop mesafesi maliyet altındaysa atla. Ücret/kayma/funding ve 1m stop önceliği zorunlu.
- **Örtüşme:** [MACD→EMA çoklu teyit](../batch_068/STRATEGIES.md) ve stokastik/EMA adaylarına karşı aynı tarihlerde olay örtüşmesi; EMA çaprazı tek başına, stokastik filtresi tek başına, birleşim karşılaştırılır.

### LK85B — Aroon çaprazı, RSI50 ve SMA10 yön filtresi

- **Kaynak kuralı:** RSI14 >50, fiyat SMA10 üstü ve Aroon Up, Aroon Down'u yukarı kestiğinde long; fiyat SMA10 altı veya Aroon Up <80 çıkış (s. 65–66). Kaynak short ve stopu vermiyor.
- **Bizim kapalı mum tanımı:** Günlük kapanmış OHLC'den Aroon(25) üret; 25 periyot **bizim ön kayıtlı seçimimizdir**. Long yalnız son kapanışta `RSI14>50`, `close>SMA10`, `AroonUp[t-1]≤AroonDown[t-1]` ve `AroonUp[t]>AroonDown[t]`. Aynı sembolde açık pozisyon varken yeni giriş yok. Short ana testte yok; simetrik short yalnız ayrı keşif kolu.
- **İcra/risk:** Karar sonrası ilk 1m açılışı; stop `entry−2 ATR14` (**bizim**), kaynak çıkışlarından ilk kapanışta gerçekleşeni sonraki 1m'de uygula; alternatif 2R TP ve 7 gün azami süre ayrı kollar. Maliyet, funding ve stop/TP önceliği ortak sözleşmeye göre. AroonUp <80 çoğu çaprazda hemen doğru olabilir; bu durumda bir barlık gereksiz işlemi önlemek için giriş gününde `AroonUp>80` koşulunu **biz ekliyoruz**; 80 koşulsuz kol karşılaştırılmalı.
- **Örtüşme:** Mevcut Aroon, RSI50 ve SMA10 özelliklerini yeniden hesaplamadan kullan; tekil filtreler ile birleşimin ek değerini ve sinyal sıklığını ölç. Yeni özellik sütunu önerisi değil, birleşik olay hipotezidir.

**Ertelenen/tekrar fikirler:** PMax, QQE, Boom Hunter, SSL ve diğer topluluk göstergeleri (s. 18–53, 55–57, 71–72) kaynakta tam hesap ve sürüm olmadan kapalı mumda güvenilir biçimde üretilemez. S. 60–62 BB10/1,5+RSI5 dönüşü ve s. 73–74 RSI2+SMA5+SMA200, önceki BB/RSI2 dönüş ailesinin varyasyonudur. S. 62 short stopunun “giriş mumunun en düşük seviyesi altı” olması yön hatasıdır; short stop high üstünde olmalıdır. S. 37–38 stochastic satış açıklamasında “aşırı satımdan sonra 80 altı” da eşik/çeviri hatasıdır. S. 77 short çıkışta HMA **altında** kapanış yazarken giriş de HMA altında kapanıştır; bu haliyle çelişir, test kuralı olamaz. Parametreleri performansa göre tüm geçmişte optimize etme önerileri final holdout'u kirletmemelidir.

## Ortak doğrulama

Bu üç yeni başlık uygulanabilir **adaydır**, kârlı olduğu bilinmez. Günlük UTC kararında yalnız kapanmış D1/W1/H4/H1 verisi, point-in-time evren, sonraki uygulanabilir 1m giriş ve maliyetli yol çözümü geçerlidir. Nihai ufuk/parametre seçimi zaman sıralı walk-forward içinde yapılır; tarihli holdout seçim için kullanılmaz. Stop ve hedef aynı 1m'de görülürse stop önce sayılır. Aynı sinyal olayından birden fazla gün pozisyon açılmaz; kaynak FX seansı/forex pip ölçüsü kripto tick ve UTC gününe birebir çevrilmez.

