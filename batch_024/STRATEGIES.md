# Kitap okuma 024 — çapraz piyasa öncülüğü, haftalık açılış aralığı ve çoklu zaman dilimi

**Kapsam:** 108 + 25 + 81 = **214 PDF sayfası**. Sayfa sıralı çıkarılmış tam metinler bu klasörde. Atıflar basılı kitap değil, PDF sayfa numarasıdır. Aşağıdaki sayısal deney eşikleri kaynağın vermediği yerlerde **bizim hipotezimizdir**. Bu partide backtest, paper test veya işlem yapılmadı.

## 1. Osbert Ferguson — Kripto Para Alım Satımı ve Yatırımının Teknik Analizi

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 19/Baskı 19/Kripto Para Alım Satımı ve Yatırımının Teknik Analizi - Osbert Ferguson (108 sayfa) - @eseckal.pdf>) · [Tam metin](01_crypto_ta_ferguson.txt)

Kitap genel TA, hacim, göstergeler, mumlar ve işlem psikolojisini anlatıyor. Diğer partilerdeki RSI, MACD, hareketli ortalama ve mum ailesiyle önemli örtüşme var. Ayrı araştırma fikri, ETH direnci aşmışken BTC'nin geride kalması, BTC OBV'sinin yükselmesi ve BTC'nin ardından direnci aşması (s. 94–95). Kaynağın mutlak `105.000 OBV` kâr hedefi (s. 95) borsaya, hacim ölçeğine ve OBV başlangıç noktasına bağlı olduğu için taşınabilir değil. S. 92'deki garantili üstün getiri ve s. 95'teki OBV'nin “balina alımı” gösterdiği iddiaları kanıt sayılmaz. S. 95 alım *limit* emrini dirençte önerirken aynı anda kırılım bekler; dolum mantığı belirsizdir.

### F24 — ETH öncülüğünde BTC kırılımı, OBV teyidi

- **Kaynak fikri:** ETH ile BTC arasında asimetrik direnç kırılımı, BTC OBV yön teyidi, ardından BTC direncini aşınca long (PDF s. 94–95); stop kırılım mumunun altı, genel 2:1 hedef önerisi (s. 95–96).
- **Bizim D1 deney tanımı:** Tam kapanmış UTC gününde ETH `close[t] > max(high[t-20:t-1])`, BTC `close[t] <= max(high[t-20:t-1])`; aynı gün BTC OBV'si son 20 günlük en yükseğin üzerinde ve BTC hacmi kullanılabilir. Sonraki **3 tam gün** içinde BTC `close >` sinyal gününde sabitlenen BTC direnç seviyesi olursa kırılım gününden sonraki ilk 1m fiyatla long. BTC OBV standardı `OBV[t]=OBV[t-1]+sign(close[t]-close[t-1])*volume[t]`; başlangıç seviyesi keyfi olduğundan sadece göreli kırılım kullanılır. Stop BTC kırılım gününün dibinin `0.1 ATR14_D1` altı; hedef 2R, ayrıca H7D zaman çıkışı. `20 gün`, `3 gün`, tampon ve H7D bizim deney parametrelerimiz.
- **Karşılaştırma:** Aynı BTC 20D kırılımlarında ETH öncülüğü/OBV şartı olmadan ve ayrı ayrı şartlarla net sonuç; ETH ve BTC'nin aynı borsa veri kalitesi, sembol sürekliliği ve eşzamanlı UTC kapanışları. Bu, yeni bir bağımsız BTC kırılımı olarak değil, mevcut kırılım ailesine filtre olarak sayılacak. Çoklu piyasa korelasyonu nedensellik kanıtı değildir.

## 2. Laurentiu Damir — Momentum Trade

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 14/Baskı 14/Momentum Trade - Laurentiu Damir (25 sayfa) - @eseckal.pdf>) · [Tam metin](02_momentum_damir.txt)

Kaynak **forex ve New York kapanışlı hafta** üzerine yazılmıştır (s. 4). Son kapanmış W1 mum güçlü yönlü olmalı (s. 9–10); yeni haftanın ilk dört H4 mumu 16 saatlik kutuyu oluşturur (s. 5, 11, 24). Yalnız W1 yönünde güçlü H4 kutu kırılımı, kutu ve kırılımın EMA200 ile kesişmemesi, forex için en az 90–100 pip kutu genişliği gerekir (s. 11–12, 24). Kırılan sınıra M15 dönüşte limit emir, yakındaki küçük pivotta stop ve kırılım H4 mumunun ucunda hedef; hedef uzaklığı stop uzaklığından büyük olmalı (s. 14–16). Geç gelen retest ve uzak stop elenir (s. 19–20).

### D24 — W1 momentum + ilk 16 saat aralığı + erken retest

- **Bizim kripto H4/M15 deney tanımı:** UTC Pazartesi 00:00 hafta başlangıcı; önceki **tam** W1 mumunun gövdesi/aralığı `>=0.70`, long için kapanış üst %25'te, short için alt %25'te. İlk dört kapanmış H4 barın `R=max(high), S=min(low)` aralığı. Forex pip şartı kriptoya uygulanmaz; `R-S >= 1.0 ATR14_H4` ilk hipotez. EMA200_H4, long için hem kutunun hem kırılım H4 mumunun tüm dibinden aşağıda; short simetrik yukarıda. En geç Çarşamba 23:59 UTC'ye kadar W1 yönünde `close_H4 > R+0.1 ATR14_H4[t-1]` (short `<S-...`), H4 gövde/aralık `>=0.65` ve kapanış yön ucunun %25'inde. Bu eşikler kaynaktan değil.
- **Dolum ve risk:** Kırılım kapanışından sonra en çok 48 saat ve en geç Çarşamba 23:59 UTC içinde M15 yüksek/düşük kırık sınıra temas ederse ilk 1m'de limit dolumunu gerçekçi spread ve kaymayla simüle et. Stop, girişten önce teyitli son M15 pivotu (iki sağ M15 barı kapanmış) dışına `0.1 ATR14_M15`; pivot yoksa işlem yok. Hedef kırılım H4 mumunun ucu; hedef/giriş uzaklığı `>1 ×` stop/giriş uzaklığı değilse işlem yok. Bu kurulum için ilave H3D zaman çıkışı. Retest olmaması işlem değildir; sinyal başına dolum oranı ayrıca raporlanır.
- **Karşılaştırma:** Aynı haftalık yön/kutu olaylarında doğrudan kırılım girişi ile retest girişi; EMA200 ve erken retest filtrelerinin katkısı ayrı ablation. Haftalık kapama tanımı ve saat dilimi değişimi hassasiyet testi gerekir. H4/M15 strateji, D1 çok günlü pilotla ayrı değerlendirilir.

## 3. James Muranno — Trend Traderinin El Kitabı / Güçlü Trend Ticareti

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 17/Baskı 17/Trend Traderinin El Kitabı - Güçlü Trend Ticareti - James Muranno (81 sayfa) - @eseckal.pdf>) · [Tam metin](03_trend_muranno.txt)

Altı trend stratejisinin listesi s. 65'te. Aşağıdakiler kodlanabilir çekirdeğe sahip. Kaynak “test edilmiş/kanıtlanmış” diyor (s. 65), fakat örneklem, dönem ve maliyetli sonuç vermiyor. Topluluk göstergelerine bağlı TSI, HalfTrend/Williams %R ve AlphaTrend (s. 69–72, 75–76) tam sürüm ve yeniden boyamama doğrulanıncaya kadar test kuyruğuna alınmaz. MFI21/SMA18 + HMA65 + SMA200 kombinasyonu s. 73–74'te var, ancak “hızlı scalp” için zaman aralığı belirtilmediği ve mevcut MA/momentum ailesiyle örtüştüğü için daha düşük öncelikli.

### M24a — D1 stokastik rejimde H1 RSI2 geri dönüşü

- **Kaynak:** D1 stochastic `%K14, smoothing6, %D3`; H1 KAMA50, EMA500, RSI2. `%K/%D` 50 altında yukarı kesişirken trend long; H1 fiyat iki ortalama üstünde ve RSI2 30 altından geri üstüne çıkınca giriş; KAMA altı H1 kapanış veya D1 stochastic aşağı kesişince çıkış. Short simetrik 70 üstünden geri altına RSI2 (s. 66–67).
- **Bizim deney:** D1 sadece önceki tamamen kapanmış UTC günden okunur. Kesişim gününden itibaren en çok 5 tam gün rejim aktif; `%K` ve `%D`'yi `SMA6(raw stochastic14)` ve `SMA3(%K)` olarak hesapla, `raw=100*(close-lowest14)/(highest14-lowest14)`; sıfır paydada sinyal yok. H1 KAMA(50, fast2, slow30) ve EMA500, RSI2 Wilder; kapanmış H1'de RSI2 30 altından üstüne keserse sonraki ilk 1m'de long, H1 close her iki ortalamanın üstünde olmalı. Short simetrik. Çıkış kaynak koşulları veya H3D; başlangıç stopu son teyitli H1 pivotunun dışı, pivot yoksa `2 ATR14_H1` bizim ek risk kuralı. KAMA ve smoothing seçimi kaynaktaki açık olmayan uygulamayı sabitler.
- **Karşılaştırma:** Yalnız H1 RSI2/ortalama sinyali ile D1 stochastic filtreli aynı sinyaller; stochastic kesişimini sürekli durum sayma varyantı ayrı. D1 bilgisini gün tamamlanmadan H1'e taşımama zorunlu.

### M24b — D1 ve H1 çift MACD trend teyidi

- **Kaynak:** D1 MACD çizgisi sinyal üstünde/altında yön; H1 MACD çaprazı giriş; H1 SMA doğrulama ve tersi çapraz/SMA çıkışı (s. 77–78). S. 77 başlıkta **SMA20**, maddelerde **SMA30** der. S. 78 short stopunu giriş mumunun **dibinin altı** olarak yazar; short için bu koruyucu stop değildir.
- **Bizim deney:** MACD(12,26,9) D1 yönü önceki tam gün sonunda sabitlenir. H1 MACD çizgisi sinyal çizgisini aynı yönde kestiği kapanmış H1 barında `close>SMA30_H1` ise long, short için `<`; sonraki ilk 1m'de giriş. Long stop sinyal H1 mumunun dibinin, short stop **tepesinin** `0.1 ATR14_H1` dışı. Ters H1 MACD çaprazı veya H1 SMA30 ters kapanışı veya H3D'de çıkış. EMA ayarı, 30 seçimi, tampon ve zaman sınırı bizim test sözleşmemizdir; short stop kaynak hatası düzeltilmiştir.
- **Karşılaştırma:** Sadece H1 MACD+SMA30, D1 yön filtresiyle; SMA20 ayrı duyarlılık varyantı. M24a/M24b'nin kesişen sinyalleri bağımsız gözlem diye çift sayılmaz.

## Sonraki test için kayıt

Öncelik D24'ün ayrı H4/M15 retest testi ve F24'ün mevcut BTC kırılım olaylarında filtre deneyi. M24a ve M24b birer trend filtre hipotezi; performans iddiası yok. Tüm testlerde olay zamanı, kapanmış bar verisi, 1m dolum, point-in-time evren, spread/ücret/kayma/funding, aynı 1m barda stop önceliği ve zaman sıralı dış örneklem gerekir. Parametreler yalnız eğitim bölümünde seçilip dış örneklemde dondurulmalıdır.
