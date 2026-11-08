# Kitap okuma 088 — ayrışma, EMA/SMA/RSI ve Coffee Grounds

**Kapsam:** Üç yeni PDF'nin **20 + 33 + 48 = 101 sayfası** baştan sona okundu. Seçilen kural ve grafik sayfaları [görsel olarak incelendi](figure_contacts/). Sayfalar PDF sayfalarıdır. Aşağıdaki kurallar test ön kaydıdır; backtest, paper test ve emir yapılmadı. Kaynak getirileri bağımsız doğrulanmış sonuç değildir.

## 1. Uyumsuzluklarla Trading — BabyPips kaynaklı derleme

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 10/Baskı 10/Uyumsuzluklarla Trading (20 sayfa) - @eseckal.pdf>) · [Tam metin](01_divergences.txt)

**Sayfa haritası:** s. 1–6 klasik ve gizli ayrışma; 7–9 döviz grafiği örnekleri; 10–13 osilatör kesişimi, aşırı alım/satım çıkışı ve çizgi teyidi; 14–18 dokuz kural; 19–20 özet. S. 3, 5, 10, 18–19 görsel denetlendi.

**Tekrar kararı:** Fiyat daha düşük dip/osilatör daha yüksek dip klasik boğa; fiyat daha yüksek dip/osilatör daha düşük dip gizli boğa tanımları [032. parti](../batch_032/STRATEGIES.md) ile aynı. S. 10–11 stokastik kesişimini bekleme fikri yeni bir gösterge eşik kolu olabilir, fakat pivot teyidi, gösterge versiyonu ve kesişim bekleme sınırı kaynakta verilmez. Önceki ayrışma adayının stokastik teyit varyantı olarak değerlendirilecek; ayrı strateji sayılmadı. Kitap s. 19'da ayrışmayı tek başına giriş değil kurulum koşulu olarak ele alır. Örnek grafikleri performans kanıtı saymıyoruz; teyitli pivotu geriye dönük sinyal tarihine taşımamak gerekir.

## 2. Forex Gizli Trading Modeli — Rich Finegan

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 11/Baskı 11/Forex Gizli Trading Modeli - Rich Finegan (33 sayfa) - @eseckal.pdf>) · [Tam metin](02_hidden_model.txt)

**Sayfa haritası:** s. 1–10 gerekçe, SAR ile çizgi, SMA20/EMA20/RSI14; 11–18 iki kırılım ve ortalama/RSI stratejisi; 19–21 hedef çizgileri; 22–30 alıştırmalar/örnekler; 31–33 açıklamalar. S. 7, 11–14, 17, 19, 26 görsel denetlendi.

### RF88 — EMA20/SMA20 dizilişi ve RSI14 orta çizgi teyidi

- **Kaynak:** H1'de `EMA20>SMA20`, fiyat `EMA20` üstünde kapanır, `RSI14≥50` ise long; short simetri (s. 12–14). S. 14 genel kuralında fiyatın **iki** ortalamanın da üstünde/altında olması istenir. S. 17 trend çizgisine çok yakın sinyali atlamayı söyler fakat yakınlık eşiği vermez. SAR(0.02,0) ile çizilen trend çizgisinin iki kapanış kırılımı ayrı yöntemdir (s. 7–8, 11); SAR'ın ikinci parametresi ve çizginin algoritması tam belirli değildir.
- **Bizim kapalı mum sürümü:** UTC D1 kapanışında Wilder RSI14, kapanış SMA20 ve EMA20 (ilk SMA20 ile başlatılıp önceki en az 200 D1 barla ısıtılır). Long: `close[t]>EMA20[t]>SMA20[t]`, `RSI14[t]≥50`; short: `close[t]<EMA20[t]<SMA20[t]`, `RSI14[t]<50`. Aynı yönde ardışık koşullar için sadece **ilk yanlış→doğru geçiş** olaydır; yeni giriş için koşulun en az bir kapanışta bozulması gerekir. D1 ölçeği kaynağın s. 32'de izin verdiği aktarım olup ana H1 örneğinden farklıdır. EMA başlangıcı ve olay tekrar kuralı bizimdir.
- **İcra/risk:** Sinyalden sonraki ilk uygulanabilir 1m açılışında giriş. `2×ATR14_D1[t]` başlangıç stopu; 2R hedef veya karşıt kapalı D1 koşulundan sonraki ilk 1m çıkışı, en çok 14 gün. Stop/TP/süre bizim standardizasyonumuzdur; kaynaktaki 30 pip FX örneğini kripto fiyatına taşımıyoruz. Stop yanlış tarafta, fiyat/hacim eksikse atla. Ücret, kayma ve funding dahil; aynı 1m stop/TP'de stop önce.
- **Örtüşme:** Tek başına EMA20 veya RSI50 ile aynı karar günlerindeki olay örtüşmesi ve net sonuçları karşılaştır. SAR çizgisi filtresi, tanımı doğrulanmadan ana kola sokulmaz. EMA ve SMA ikisi de kapanış türevi olduğundan bağımsız iki kanıt gibi değerlendirilmez.

## 3. Coffee Grounds Trading Sistemi — P. K. Tournis

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 12/Baskı 12/Coffee Grounds Trading Sistemi - P. K. Tournis (48 sayfa) - @eseckal.pdf>) · [Tam metin](03_coffee_grounds.txt)

**Sayfa haritası:** s. 1–13 trend/momentum anlatısı; 14–19 göstergeler; 20–27 yedi kural ve gerekçeleri; 28–39 iddialar ve çıkış; 40–48 seçilmiş hisse örnekleri/projeksiyon. S. 18, 20–22, 31, 33 görsel denetlendi.

### CG88 — SMA10/30/100/200 dizilişinde SMA10 geri kazanımı

- **Kaynak çekirdeği:** Long için `SMA10>SMA30>SMA100>SMA200`, MACD çizgisi sinyal çizgisini yukarı keser, stokastik 20–80 aralığında kalır; önceki gün fiyat SMA10 altında, giriş gününde üstündedir. Short simetrik (s. 20–22). Kitap ayrıca hisse fiyatı ≥15 USD, hacim ≥500.000 pay ve SMA50(hacim) üstü ile **10 ardışık Waddah Attar Explosion renk barı** ister. ATR10×2,7 trailing stop çıkışı s. 31–34. Bunlar kitabın **tam** yedi koşullu sistemidir.
- **Bizim test edilebilir alt küme:** UTC D1'de yalnız standart OHLCV ile `SMA10>SMA30>SMA100>SMA200`; `close[t−1]<SMA10[t−1]`, `close[t]>SMA10[t]`; `MACD12,26,9[t−1]≤signal[t−1]` ve `MACD[t]>signal[t]`; `20<%K14[t]<80`. Short tüm eşitsizlikleri ters çevirir, stokastik yine 20–80. MACD sinyal hattı EMA9(MACD); %K14=`100×(close−LL14)/(HH14−LL14)`, sıfır aralıkta sinyal yok. En az 250 tam D1 bar ve tek aktif pozisyon. Bu **kaynağın tamamı değil, ön kayıtlı alt kümesidir**: pay sayısı ve 15 USD hisse eşiği kriptoya doğrudan aktarılmaz; Waddah renklerini sürüm/hesap doğrulanmadan varsaymıyoruz. `quote_volume[t]>median(quote_volume[t−50:t−1])` yalnız ayrı likidite varyantıdır, kaynak pay eşiğinin eşdeğeri değildir.
- **İcra/risk:** İlk uygulanabilir 1m açılışı. Başlangıç stopu girişten `2,7×ATR10_D1[t]`; sonraki her tam D1 kapanışında long stop `max(eski_stop, highest_close_since_entry−2,7×ATR10_D1)`; short için `min(eski_stop, lowest_close_since_entry+2,7×ATR10_D1)`. Güncellenen seviye ancak sonraki 1m'de geçerli. `highest_close` seçimi **bizimdir**; kitap trailing formülünü vermiyor. 2R sabit hedef yalnız karşılaştırma kolu; ana kol stop veya 30 gün sonunda kapanır. 30 gün bizim sınırımız. Ücret/kayma/funding, 1m stop yolu ve aynı mumda stop önceliği uygulanır.
- **Kritik sınırlama/karşılaştırma:** Kitap s. 18'de Waddah hızlı/yavaş uzunluklarını 44/150 verirken aynı paragrafta 12/26 EMA diye açıklar; s. 20–21 MACD “sıfır bölgesi” ile **sinyal çizgisi kesişimini** aynı şey gibi söyler. Bu nedenle Waddah eklenmeden kitaptaki orijinal yedi koşulun performansı iddia edilemez. SMA dizilişi + SMA10 dönüşü, sonra MACD, stokastik ve likiditeyi sırayla ablate et. S. 42–47 yalnız seçilmiş 2021 hisse işlemleri ve varsayımsal tekrar yatırma projeksiyonudur; veri seti/backtest kanıtı değildir. “Çeşitlendirme gerekmez” iddiasını portföy risk kuralı olarak almayız.
