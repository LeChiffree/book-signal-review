# Kitap okuma 065 — S/R kuyruğu, MACD çizgi kırılımı, histogram ivmesi

**Kapsam:** Üç PDF'nin gerçek **89 + 25 + 24 = 138 sayfası** sıralı metne çıkarılıp incelendi. Atıflar PDF sayfasıdır. Kaynakta belirtilmeyen tolerans, pencere ve icra ayrıntıları **bizim test tanımımızdır**. Backtest, paper test ve emir yapılmadı.

## 1. Mark Boardman — Forex Ayarla ve Unut Kazanç Sistemi

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Forex - Ayarla ve Unut Kazanç Sistemi - Mark Boardman (89 sayfa) - @eseckal.pdf>) · [Tam metin](01_set_forget_boardman.txt)

**Kaynak:** Üç mumlu pivot tanımı s. 33–34, kırılım ve S/R'ye geri çekilme s. 47–49, seviyedeki uzun kuyruk s. 50–53. Kuyruk fitili tüm mum yüksekliğinin en az %50'sidir (s. 51–52). S/R'de karşı yönlü iki mumluk “180” dönüşü s. 53–54; aşırı uzamış fiyat ve Bollinger kıyası s. 55–58. Kuyruk mumu kapandıktan sonra toplam mum boyunun yaklaşık üçte birlik geri çekilmesi ve yeniden hareketlenmeyle giriş s. 69–71; stop kurulum mumunun öte ucuna yakın, yaklaşık 2R hedef, yakın karşı S/R varsa 1,7R'ye kadar azaltma s. 71–73. S&R çizim yöntemi ve özel Apollo göstergesi tam mekanik değildir; aşağıdaki aday gözlenebilir vekil kullanır. Kitaptaki kesin kâr ve “fiyat daima SMA200'e döner” iddiaları (s. 55, 62, 77) doğrulanmış olasılık değildir.

### MB65 — Dondurulmuş S/R seviyesinde uzun kuyruk ve üçte bir geri çekilme

- **Seviye:** H1'de 2 sol/2 sağ kapanmış barla teyitli iki pivot low farkı `≤0,2×ATR14_H1` olan destek, pivot high'lar için direnç. İkinci pivot teyidinde seviye iki fiyatın ortalaması olarak dondurulur; sonraki mumlarla çizgi yeniden yerleştirilmez. Kaynağın görsel S/R seçimini bu pivot toleransıyla sayısallaştırıyoruz.
- **Kurulum:** Long için fiyat ilk kez desteği `≤0,2×ATR` mesafeden test ederken kapanmış H1 mumda alt fitil `min(open,close)−low ≥0,5×(high−low)` ve `high>low`; short dirençte üst fitil simetrik. Pivot teyidinden önceki testler ve aradaki temaslar saklanır, yalnız ilk temas ana kol; sonraki testler ayrı kol. SMA200 veya Bollinger filtresi ana kola eklenmez, veri/kural belirsizliği nedeniyle ayrı ablation olabilir.
- **Tetik:** Kuyruk mumunun tüm aralığı `R`. Long için kurulum kapanışından sonraki en çok üç H1 bar içinde önce `low≤high_setup−R/3` geri çekilmesi, ardından **ayrı tam H1 kapanışında** `close>high_setup−R/3` ve `close>open` ilk dönüş teyidi; short için `high≥low_setup+R/3`, ardından `close<low_setup+R/3` ve ayı mum. Aynı bar içindeki olay sırası OHLC ile bilinmiyorsa 1m sıraya bakılır; bulunmazsa sinyal atlanır. Bu kapalı mum teyidi, kaynağın bekleyen emir uygulamasından daha geçtir ve ayrı sürüm olarak etiketlenir.
- **Risk/karşılaştırma:** Teyit sonrası ilk uygulanabilir 1m giriş; long stop kurulum low `−0,1×ATR`, short high `+0,1×ATR`; 2R veya 12 H1 süre. Stop yanlış tarafta/maliyetten dar ise atla, aynı 1m stop önce. Aynı S/R pivotlarında kuyruksuz geri dönüş ve üçte bir geri çekilmesiz kuyruk kollarıyla net R/işlem sayısı kıyaslanır; önceki pin bar/S&R adaylarıyla örtüşme raporlanır.

## 2. Trading Strategy Guides — MACD Trend Takip Stratejisi

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/MACD Trend Takip Stratejisi - Trading Strategy Guides (25 sayfa) - @eseckal.pdf>) · [Tam metin](02_macd_trend_guides.txt)

**Kaynak:** MACD çizgisinde önce yüksek, sonra daha alçak swing high belirleme s. 10–11; bu iki noktadan trend çizgisi s. 13; MACD çizgisinin çizgi üstüne çıkması ve MACD-sinyal kesişimiyle alım s. 15–16; son swing low altı stop s. 16, ters MACD-sinyal kesişiminde **mum kapanışı bekleyerek** çıkış s. 18–19. Çizimlerin fiyat grafiğiyle eşleşmesine ilişkin açıklama yer yer belirsizdir; uygulamada MACD pivotu ve fiyat pivotu ayrı tanımlanır. Forex pip tamponu kriptoya aynen aktarılmaz.

### TG65 — MACD swing high çizgisinin kapanışta yukarı kırılması

- **Pivot/çizgi:** H4 MACD(12,26,9) çizgisinde 3 sol/3 sağ barla teyitli ardışık iki swing high `M1>M2`; aralarında 5–40 H4. İkinci pivot ancak sağındaki üçüncü bar kapanınca bilinir. `(bar_index,M1)` ve `(bar_index,M2)` düz çizgisi o anda dondurulur, ileri barlara doğrusal uzatılır; sonradan pivot güncellenmez. Short için iki yükselen MACD swing low ve aşağı kırılım simetrik. Kaynak pivot penceresi/dönemi vermediği için bu değerler bizimdir.
- **Giriş:** İkinci pivot teyidinden en çok 20 H4 içinde ilk kapalı barda MACD çizgisi trend çizgisini aşağıdan yukarı geçsin ve MACD çizgisi sinyal EMA9 üstünde olsun. Ana kol ayrıca MACD'nin sinyal çizgisini o bar veya önceki üç H4 içinde yukarı kesmesini ister; kesişim penceresi bizimdir. Aynı zamanlı iki şartın farklı yorumu için yalnız trend çizgisi kırılımı ayrı kol. Long stop girişte zaten teyitli son fiyat swing low `−0,1×ATR14_H4`; short simetriği. Stop yanlış tarafta/maliyetten dar ise atla.
- **Çıkış/icra:** Sinyal kapanışı sonrası ilk uygulanabilir 1m giriş. Long, MACD çizgisi sinyal çizgisini **kapalı H4'te** aşağı keserse sonraki uygulanabilir 1m çıkış; short tersi. Stop veya 60 H4 süre daha önceyse onları uygula. Aynı 1m stop önce. Yalın MACD-sinyal kesişimi ve daha önceki MACD trend/ayrışma adaylarıyla gecikme, net R ve sinyal çakışması karşılaştırılır.

## 3. Short-Term Trading Sırları — yazar belirtilmemiş

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Short-Term Trading Sırları (24 sayfa) - @eseckal.pdf>) · [Tam metin](03_short_term_secrets.txt)

**Kaynak:** ADX'in güç ve aralık ayrımı: 20 altı yatay, 25 üzeri trend başlangıcı ve 30 üstü güçlü hareket uyarısı (s. 7–8). ATR14 ve ATR'nin 10 barlık ortalamasıyla oynaklık rejimi s. 11–13. En somut işlem reçetesi s. 18–19: sıfırın uzağındaki MACD histogramı aynı yönde **son üç bar** hareket edince o yöne gir; histogram bir bar ters yönde ilerleyince çık. Keltner bantlarında trend/geri çekilme ve aralık tepkisi s. 21–22, fakat bant parametresi ve tam tetik belirtilmez. Kitap s. 24'te ek bölüm vaat eder, PDF burada biter; eksik bölümü varsaymayız.

### ST65 — MACD histogramında üç bar ivme, ilk ters barda çıkış

- **Sinyal:** H1 kapalı mumlarında MACD(12,26,9) histogramı `h`. Long için `h[t−3]<h[t−2]<h[t−1]<h[t]<0`, short için `h[t−3]>h[t−2]>h[t−1]>h[t]>0`; böylece sıfırdan uzakta üç ardışık değişim ve sıfıra yaklaşan karşı trend ivmesi ölçülür. Ancak kaynak s. 18'de negatif histogram yükselince long örneği verir; işaret seçimi bu örnekle uyumludur. Sıfırdan uzaklık filtresi `|h[t−3]|≥0,1×ATR14_H1` bizim tanımımızdır; filtresiz kol ayrıca ölçülür. En az 100 H1 ısınma.
- **İcra/çıkış:** Kapanıştan sonraki ilk uygulanabilir 1m giriş. Long için her kapanmış H1'de `h[t]<h[t−1]` ilk ters bar çıkışı, short için `h[t]>h[t−1]`; sonra ilk uygulanabilir 1m'de çık. İlk stop long `min(low[t−4:t])−0,1×ATR14_H1`, short simetriği; stop veya 24 H1 süre daha önceyse öncelikli. Stop yanlış tarafta/maliyetten dar ise atla, aynı 1m stop önce. Kaynak stop/süreyi belirlemez; bunlar bizim güvenlik sözleşmemizdir.
- **Karşılaştırma:** Üç bar ivme ile tek histogram eğimi kolu, ADX14 `<20` ve `>25` rejimleri, önceki histogram ayrışması JS62 ve teyit adayı JD64 ile olay çakışması. Kaynaktaki vadeli işlem seansı/haber bağlamı 7/24 kriptoya eşit sayılmaz.

## Ortak test sözleşmesi

Tüm olaylar kapanmış mum ve o ana dek teyitli pivotla üretilir; 1m dolumda ücret, spread, kayma, perpetual funding, eksik veri ve eşzamanlı pozisyon politikası modellenir. Zaman sıralı ayrılmış doğrulamada işlem sayısı, net R, maksimum düşüş ve yalın taban çizgileri raporlanmadan kârlılık iddiası kurulmaz.
