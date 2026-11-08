# Kitap okuma 020 — trend çizgisi kırılımı ve çıkış rejimi

**Kapsam:** 79 + 22 + 16 = **117 PDF sayfası**. Tam metinler aynı klasörde. Sayfalar PDF sayfasıdır. Kaynağın anlatımı ile bizim kapalı mumlu deney parametreleri ayrılmıştır. Backtest, paper test veya emir yapılmadı.

## 1. Kelvin Lee — Trendline Stratejisi

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 4/Baskı 4/Trendline Stratejisi - Kelvin Lee (79 sayfa) - @eseckal.pdf>) · [Tam metin](01_trendline_kelvin.txt)

Kitap salınım tepe/diplerini sağ ve solda mum bulunan N/V şekliyle tarif eder (s. 7–8); uzun trend çizgisinde üç salınım teması ister (s. 9–14). En güncel iki pivotla güncellenen TD çizgisi s. 15–17'de; kırılımda MACD histogramının yön değiştirmesi ve ikinci barı bekleme s. 20–22'de. Kısa çizgi kırılımından orta çizgiye, orta kırılımından uzun çizgiye hedef (s. 31–32); kırılan çizginin retestinde rol değişimi (s. 33–35); son salınım ekstremumu stop (s. 43–44) kitap sisteminin çekirdeğidir. S. 37–62 seçilmiş Forex grafik örnekleridir, hit rate ispatı değil. S. 64–79 ek blog yazıları/pivot ve psikoloji içerir; bağımsız tam işlem kuralı değildir.

### KL20a — MACD teyitli düşen trend çizgisi kırılımı

- **Kaynak:** Güncel iki tepeyle düşen direnç çizgisi, yukarı kırılma, MACD histogramının pozitife dönmesi ve ikinci histogram barı; stop son düşük, hedef orta vadeli çizgi veya geometrik projeksiyon (s. 15–22, 31–32, 43–44). MACD'nin yalnız eğim mi yoksa sıfır geçişi mi olduğu çeviride belirsiz; burada **sıfır geçişi** ayrı deney seçimi.
- **Bizim D1 mekanik sürüm:** Pivot tepe `high[i]` soldaki ve sağdaki iki kapanmış D1 mumun yükseğinden büyükse, ancak `i+2` kapanınca bilinir. O anda bilinen son iki alçalan pivot tepe `(i1,h1),(i2,h2)` ile `L(t)=h2+(h2-h1)(t-i2)/(i2-i1)`; `i2>i1`, çizgi olay başlamadan dondurulur. `close[t]>L(t)+0.1 ATR14[t-1]` ve MACD(12,26,9) histogramı `t` ile `t+1` kapanışlarında `>0` ise `t+1` kapanışı sonrası ilk 1m long. `t+1` fiyatı tekrar çizgi altına kapanmışsa iptal. Stop kırılım öncesindeki son onaylı pivot dip `−0.1 ATR`, hedef 2R baz veya olaydan önce bilinen daha eski trend çizgisi teması; hedef varyantları ayrı. H7D/H14D zaman çıkışı. Short simetrik; uygun perp evreni gerekir. `t+1` barını görmeden t anında giriş yapılmaz.
- **Ablation:** Çizgi kırılımı tek başına, MACD sıfır geçişi, histogramda iki art arda yönlü bar, ardından retest. MACD ve trend kırılımı batch 002/018 aileleriyle ortak olay olarak işaretlenir. `i+2` pivot teyidi nedeniyle geçmişe sinyal boyama engellenir.

### KL20b — Trend çizgisi rol değişimi retesti

- **Kaynak:** Kırılan direnç yeni desteğe dönüşebilir; çizgiye dönüşü bekle, retest başarısız olursa çizgi geçersiz (s. 33–35).
- **Bizim filtre:** KL20a kırılımından sonraki 1–5 tamamlanmış D1 mumda ilk kez `low<=L(t)+0.2 ATR` ve `close>L(t)` olan mum kapanışı; sonraki ilk 1m long. Stop retest dibi `−0.1 ATR`, hedef 2R, en geç H7D. Retest yoksa işlem yok. İlk uygun retest seçilir, sonradan en iyi retest aranmaz. Yatay T18a retestiyle karşılaştırma, çizgi eğiminin gerçekten katkısını gösterir.

## 2. Lance Beggs — Stoploss Stratejisi / Çıkış Stratejisinin Önemi

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Stoploss Stratejisi (22 sayfa) - @eseckal.pdf>) · [Tam metin](02_stoploss.txt)

Bu 22 sayfa **bağımsız giriş stratejisi vermez**. Aynı girişte dar/geniş stop, hedef ve takip eden stopun sonucu değiştirdiğini; işlem için hangi çıkışın en iyisi olduğunun ancak sonradan anlaşılabileceğini gösterir (s. 3–10). Yatay piyasada hedef, düzgün trendde trailing stop fikri s. 13–15; fakat bunlar yazarın piyasa inançlarıdır, ampirik evrensel kural değil. Erken fiyat/zaman çıkışı s. 17–19; ilk parçayı yakın S/R'de kapatma, ikinci parçayı trende göre izleme s. 20–21. “Önceden stop koydum, kayıp asla aşılmaz” çıkarımı yapılamaz; gap, kayma, likidite vardır.

### LB20 — Aynı girişlere çıkış rejimi ablation'ı

- **Kaynak:** Trendde salınım arkası trailing stop, yatayda yakın S/R hedefi, işlem hızla lehine gitmezse erken çıkışı değerlendirme; iki parçalı seçenek (s. 14, 17–21). Kitap ölçülebilir trend/yatay eşiği ve kaç bar beklenmesini vermiyor.
- **Bizim deney tasarımı:** Girişler sabit tutularak K18b/RT19a/KL20a olaylarına aynı 1m fiyat yolunda dört çıkış: (A) başlangıç yapısal stop + 2R TP; (B) başlangıç stop + H7D zaman çıkışı; (C) ilk kapanmış D1 `1R` lehine ilerlemeden 2 D1 geçmişse erken çıkış, aksi 2R; (D) ilk 1R'de nominalin yarısı kapatılıp kalan kısmın stopu yalnız onaylı D1 pivotun arkasına taşınır. Stop hiçbir zaman riski artıracak yönde genişletilmez. Dış örneklemde net R, expectancy, tail loss, turnover ve pozisyon çakışması raporlanır. Bu dört sayı/algoritma **bizim** ön tanımımızdır; kitabın kesin kuralları gibi gösterilmez.
- **Önemli ayrım:** Bu, yeni giriş sinyali değil **exit-policy deneyi**. Özellikle 1m aynı barda stop/TP temasında stop önceliği, ücret/kayma ve funding ile fiyat patikası gerekir. Psikolojik rahatlık iddiası yalnız getiri metriğiyle doğrulanmaz.

## 3. Triple S Stratejisi

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Triple S Stratejisi (16 sayfa) - @eseckal.pdf>) · [Tam metin](03_triple_s.txt)

Kaynak M5/M15 Forex'te trend içi geri çekilme sırasında hacmin yavaşlaması ve yeniden artışıyla trend yönünde giriş arar (s. 4–8). Açıkça “giriş kararı size kalmış” der (s. 7). 10–20 pip hedef, 5–8 pip stop, +10 pip sonrasında stopu +5 pip'e taşıma anlatılır (s. 9–10). Bunlar Forex pip değerleridir; kripto için doğrudan kullanılmaz. Forex tick hacminin eksiksiz alım satım hacmi olduğu savı (s. 3) güvenilir bir eşdeğerlik değildir. Haber etrafında ±30 dakika durma önerisi (s. 4) tarihsel makro takvimi gerektirir; OHLCV'den geriye doğru “haber yok” türetilemez.

### TS20 — Hacmi kuruyan geri çekilme sonrası genişleme

- **Bizim D1 çok günlü uyarlama:** Son tamamlanmış W1 ve D1 kapanışları EMA20 üstü; önceki 3–6 D1 mumda en az `1 ATR14` yukarı impuls. Bunu izleyen 2–4 tam D1 geri çekilme mumunda her kapanış EMA20 üstü, geri çekilme toplamı impulsun `%25–75`i, geri çekilme hacim medyanı impuls hacim medyanının `<=0.7`si. İlk `t` D1 kapanışında `volume[t]>=1.5×median(pullback volume)` ve `close[t]>max(high[pullback])` ise sonraki ilk 1m long. Stop geri çekilme dibi `−0.1 ATR`, hedef 2R, H3D/H7D çıkış. Short simetrik ve perp evreninde ayrı. Bütün eşikler, EMA ve günlük zaman dilimi **bizim hipotezimizdir**; kaynağın M5/M15 scalping sonucuyla karıştırılmaz.
- **Uygulama notu:** Volume kaynağı borsa bazında base/quote ayrımıyla sabitlenir; aynı varlığın farklı borsalarında toplamsız kıyas yapılmaz. Haber filtresi uygun takvim yoksa uygulanmaz ve bu açıkça raporlanır. Bu aday mevcut momentum/hacim kurallarına çok yakın; ilk karşılaştırmada yeni kolon değil olay filtresi olarak ölçülür.

## Test önceliği

İlk sırada **LB20 çıkış ablation'ı** var; aynı girişleri sabit tutarak stop/zaman/TP kararının etkisini ayırır. İkinci sırada **KL20a/b**, trend çizgisi ve MACD teyidinin retest üzerindeki ek değerini ölçer. TS20 günlük uyarlaması kaynak stratejisinden uzaklaştığı ve önceki momentum/hacim adaylarıyla örtüştüğü için ayrı hipotez olarak düşük önceliktedir. Hepsi kapalı UTC D1/W1 kararı, 1m uygulanabilir dolum, point-in-time evren, maliyet/funding, H3D/H7D/H14D ve zaman sıralı dış örneklem sözleşmesine tabidir.
