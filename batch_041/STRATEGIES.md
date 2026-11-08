# Kitap okuma 041 — Supertrend, Ichimoku ve Bollinger

**Kapsam:** 80 + 40 + 28 = **148 PDF sayfası**. Üç kitabın tam sayfa sıralı metni kaydedildi; Ichimoku s. 27/30 ve Bollinger s. 14 grafikleri ayrıca görsel incelendi. Atıflar PDF sayfasıdır. Kaynak anlatımı ile bizim kapalı mumlu kripto deney sözleşmesi ayrıdır. Backtest, paper test ve emir yapılmadı.

## 1. Alpesh Pansheriya — Supertrend İndikatörü

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 20/Baskı 20/Supertrend İndikatörü - Alpesh Pansheriya (80 sayfa) - @eseckal.pdf>) · [Tam metin](01_supertrend_pansheriya.txt)

**Kaynak:** ATR ve çarpanla oynaklığa bağlı takip çizgisi; çizgi fiyat altına geçtiğinde long, üstüne geçtiğinde short/long çıkışı, çizgiyi takip stopu olarak kullanma (s. 5–7, 13, 18–19). Varsayılan 10 ATR ve 3 çarpan, swing için 10–14 ATR/3–4 çarpan, gürültülü piyasada 14/4 örneği verilir (s. 11–12, 15). Yatay piyasadaki sık renk değişimi ve üst zaman dilimi onayı (s. 14–17); D1 trend yönüyle alt zaman dilimindeki yeniden yeşile dönüşte giriş (s. 58–59). S. 65–66 RSI>50 ve 3R örneği, s. 70–73 mekanik al/ters renk çıkış fikri var. **Hesaplama tutarsızlığı:** s. 7 çizgiyi mevcut `high−kATR` veya `low+kATR` diye özetliyor, fakat yaygın bant uygulamasındaki orta fiyat, önceki bantla taşıma ve dönüş kurallarını vermiyor. Platformlar farklı sonuç üretebilir; testte varyantı sabitlemek zorunlu. Kitapta örnek işlemler seçilmiş, sonuçların bağımsız testi yok.

### ST41 — D1 trend onayıyla H4 Supertrend dönüşü

- **Bizim sabit gösterge tanımı:** H4 ve D1 için ATR Wilder RMA14, `TR=max(high−low,abs(high−prev_close),abs(low−prev_close))`, `mid=(high+low)/2`, `BU=mid+3ATR`, `BL=mid−3ATR`. Önceki nihai bantlar `FUprev,FLprev` için `FU=BU` eğer `BU<FUprev` veya `prev_close>FUprev`, aksi halde `FUprev`; `FL=BL` eğer `BL>FLprev` veya `prev_close<FLprev`, aksi halde `FLprev`. Önceki durum üst bantta ise `close>FU` durumunda long moda ve `FL` çizgisine geç, aksi halde `FU`; önceki durum alt bantta ise `close<FL` durumunda short moda ve `FU` çizgisine geç, aksi halde `FL`. Eşitlikte durum değişmez. İlk 200 bar ısınma ve ilk bantlar `BU/BL` sabit. Bu **bizim seçtiğimiz** bantlı Supertrend uygulamasıdır, s. 7'nin birebir formülü değildir; s. 7'deki basit çizgi ayrı hassasiyet kolu olmalıdır.
- **Olay/icra:** H4 `t` kapanışında Supertrend short→long değişsin; o anda bilinen **son tam kapanmış D1** Supertrend long olsun. Long sinyali için sonraki ilk 1m uygulanabilir fiyat, ilk stop H4 long çizgisi `−0.1 ATR_H4`; short simetrik. Sonraki H4 kapanışlarında stop yalnız kâr yönüne taşı, renk tersine dönerse sonraki 1m'de çık; ayrıca 3R hedef ve 40 H4 bar zaman çıkışı ayrı kollar. Stop yanlış tarafta veya maliyetin iki katından yakınsa işlem yok. ATR14/3 kısmen kaynak aralığında, ısınma/tampon/süre ve algoritmik bant uygulaması bizim kararımız.
- **Karşılaştırma:** D1 filtresiz, ATR10×3, ATR14×4 ve mevcut trend/ATR/EMA aileleri aynı olay evreninde. Çok parametreli aramayı yalnız zaman sıralı eğitim içinde yap; test dönemine göre parametre seçme.

## 2. Ahmed El Agouz — Ichimoku Kazananları

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Ichimoku Kazananları - Ahmed El Agouz (40 sayfa) - @eseckal.pdf>) · [Tam metin](02_ichimoku_winners.txt) · [Bulut filtresi s. 27](ichimoku_p27.png) · [Sonraki mum girişi s. 30](ichimoku_p30.png)

**Kaynak:** Tenkan `(HH9+LL9)/2`, Kijun `(HH26+LL26)/2`, Span A `(Tenkan+Kijun)/2` 26 bar ileri çizilir, Span B `(HH52+LL52)/2` 26 bar ileri çizilir, Chikou bugünün kapanışı 26 bar geri çizilir (s. 5–7). Long sinyali yalnız fiyat bulut **üstündeyken**, short yalnız **altındayken** (s. 21, 25–30). S. 27'de çeviri bir cümlede long için de “bulut altı” diyor, fakat grafiğin İngilizce etiketi ve s. 21/29 açıkça **bulut üstünü** long olarak gösterir; çeviri hatası olarak işaretlendi. Kijun eğimi düz değilse Tenkan/Kijun kesişiminin daha güçlü olduğu söylenir (s. 28). Fiyat/Kijun kesişiminden sonra **sonraki mum açılışında** giriş/çıkış grafiği (s. 30); tüm çizgiler uyumlu sinyal ve bulut geçişini bekleme (s. 31–34). Stop/çıkış için fiyatın Kijun'u ters kesmesi veya Tenkan/Kijun ters kesişimi (s. 35–38). Geçmişe çizilmiş Chikou noktası bugün değilmiş gibi okunursa ağır lookahead oluşur.

### I41 — Kijun kapanış kesişimi + o ana ait bulut filtresi

- **Bizim D1 veri hizası:** Tam UTC D1 barında `Tenkan[t]`, `Kijun[t]`, `A_raw[t]`, `B_raw[t]` yukarıdaki geçmiş pencerelerle hesaplanır. **Bugünkü grafikteki bulut** `A_chart[t]=A_raw[t−26]`, `B_chart[t]=B_raw[t−26]`; bugün hesaplanan `A_raw[t]` ancak `t+26` konumuna çizilir ve bugünkü bulut gibi kullanılmaz. Chikou onayı istenirse `close[t]>close[t−26]` long, tersi short; bugünkü kapanışın t−26'ya çizilmesi olay tarihini değiştirmez. 78 bar ısınma.
- **Giriş/risk:** Long ilk `close[t]>Kijun[t]` ve `close[t−1]<=Kijun[t−1]` kapanışı; ayrıca `close[t]>max(A_chart[t],B_chart[t])`. Short simetrik. Takip eden ilk uygulanabilir 1m giriş. Stop long `min(A_chart[t],B_chart[t])−0.1 ATR14_D1`, short üst kenar `+0.1 ATR`; yanlış tarafta/dar stopta işlem yok. Ters Kijun kapanışı veya ters Tenkan/Kijun kesişimi ayrı çıkış kolları, 20 D1 bar zaman sınırı; 2R hedef karşılaştırması. Stop tamponu/süre bizim, ters kesişim çıkışları kaynakta.
- **Ablation:** Kijun eğimi `Kijun[t]>Kijun[t−3]` long (short tersi) ve Chikou onayı ayrı filtreler; bulut filtresiz Kijun çaprazı taban. Önceki Ichimoku ve hareketli orta kırılım kayıtlarıyla olay eşdeğerliği kontrol edilmeli.

## 3. Glenn Wilson — Bollinger Band Trading

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 14/Baskı 14/Bollinger Band Trading - Kazançlı Bir Trading Sistemi Nasıl Oluşturulur - Glenn Wilson (28 sayfa) - @eseckal.pdf>) · [Tam metin](03_bollinger_wilson.txt) · [Breakout grafiği s. 14](bollinger_p14.png)

**Kaynak:** 20 kapanış SMA ve ±2 standart sapma bantları (s. 11). Bant kenarından karşı banda dönüş örnekleri (s. 12–13) ile daralma sonrası bandın dışına çıkan **devam kırılımı** ayrı rejimlerdir (s. 10, 14–15). S. 14 grafik ve metin bant dışına çıkışın tek başına yeterli olmadığını, **önceden bilinen destek/direnç** de aşılmalı der. RSI 70 üstü zayıflayan üst bantta short, RSI 30 yakınında alt bantta long teyidi (s. 19–23). S. 24 bant dışı kapanışın devam olabileceğini özellikle uyarır; her üst bant dokunuşu short değildir. Bant daralma eşiği, destek/direnç çizim algoritması, stop ve süre verilmez.

### B41 — Dar bant + fiyat direnci + bant birlikte kırılımı

- **Bizim D1 olay:** `mid[t]=SMA(close,20)`, `sd[t]=population_std(close,20)`, `upper/lower=mid±2sd`. Daralma yalnız `t−1` itibarıyla `width=(upper−lower)/mid` önceki 120 **tamamlanmış** gündeki en düşük %20 içinde ise. Önceden bilinen direnç `U=max(high[t−20:t−1])`, destek `L=min(low[t−20:t−1])`. Long ilk `close[t]>upper[t]` **ve** `close[t]>U+0.1 ATR14[t−1]`; short simetrik. Bandın `t` değeri ancak mum kapandığında bilinir; giriş daha sonra. Daralma yüzdeliği ve fiyat pencere/tamponu bizim nesnel tanımımızdır.
- **İcra:** Sonraki ilk 1m uygulanabilir fiyat; stop long `mid[t]−0.1 ATR`, short simetrik, yalnız doğru tarafta ve maliyetin iki katından uzaksa; 2R veya 10 D1 bar sonra çık. Başka kol, sadece RSI14 `>70` üst banda dokunup sonra `close<upper` ve RSI düşüşüyle short; alt bant `RSI<30` long simetrik, ancak bu **ayrı mean-reversion rejimi** ve trend kırılımıyla birleştirilmez. Her kolun kendi uygun piyasa koşulu önceden belirlenmeli.
- **Karşılaştırma:** Batch001 Bollinger, batch035 S35 daralma ve önceki Donchian kırılımı ile aynı olay kümesinde: yalnız bant, yalnız eski seviye, her ikisi. Ek koşulların yalnız seçimi daraltıp daraltmadığı ölçülmeli; bağımsız alfa varsayılmaz.

## Ortak test notu

Öncelik **I41** için zaman hizası ve **ST41** için hesaplama varyantı doğruluğudur; **B41** mevcut squeeze ailesine yakın. Point-in-time varlık evreni, kapanış sonrası uygulanabilir giriş, ücret/spread/kayma/funding, aynı bardaki stop-hedef sırası ve zaman sıralı dış örneklem zorunlu. Kaynak grafiklerinin sonuçları performans kanıtı değildir.
