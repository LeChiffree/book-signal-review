# Kitap okuma 152 — CMF, Keltner ve haftalık pivot teyitleri

Üç ayrı PDF'nin **48 + 34 + 23 = 105 sayfası** baştan sona okundu. **Yeni bağımsız araştırma adayı: 3.** Bunlar kârlılık bulgusu değildir; backtest, paper test ve emir yapılmadı. Sayfalar PDF sayfasıdır.

## 1. Günlük Alım Satım Stratejileri — Scotty Ratford

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 22/Baskı 22/Günlük Alım Satım Stratejileri - Scotty Ratford (48 sayfa) - @eseckal.pdf>) · [tam metin](01_day_trading_ratford.txt)

**Tam okuma:** s. 1–8 giriş ve avantaj iddiaları; 9–13 RSI trend çizgisi; 14–18 RSI'nın EMA21'i; 19–26 RSI ayrışması ve EMA30; 27–32 MA destek/direnç; 33–37 EMA12/35 ve CMF; 38–40 yatay rejim/ADX; 41–44 Keltner ve stokastik; 45–48 haftalık pivot, stokastik ve SAR. İlk bölümlerdeki RSI ayrışması/MA dönüşü önceki [026](../batch_026/STRATEGIES.md) ve trend/ortalama ailelerine eşdeğer; ayrı aday sayılmadı. s. 17'de RSI/EMA kesişimi yönü s. 15'in tersidir. s. 34 short için bir yerde EMA15 der, aynı kitap s. 33, 34 ve 36 EMA12 der; ana yorum EMA12'dir.

### RT152A — EMA12/35 çaprazı, CMF sıfır teyidi ve ilk EMA12 retesti

- **Kaynak çekirdeği:** EMA12, EMA35'i yukarı/aşağı keser; CMF aynı yönde sıfırın üstünde/altında olur; girişten önce EMA12 retesti önerilir. Çıkış EMA35'in ters yönde kırılmasıdır (s. 33–36). CMF dönemi ve retest penceresi kaynakta belirtilmez.
- **Kapalı mum sözleşmesi:** Likit spot BTC/ETH H4; en az 100 tamamlanmış bar. `CMF20 = sum( ((2C−H−L)/(H−L))×V,20 ) / sum(V,20)`; `H=L` barı para akışında 0, `sum(V)=0` ise sinyal yok. Long kurulumunda `EMA12[t−1]≤EMA35[t−1]`, `EMA12[t]>EMA35[t]`, `CMF20[t]>0`. Sonraki 1–6 kapanmış H4 barın **ilkinde** `low≤EMA12` ve `close>EMA12`, CMF yine >0; short simetri (`high≥EMA12`, `close<EMA12`, CMF<0). Çapraz barında giriş yok; aynı çaprazdan yalnız bir işlem. H4, CMF20 ve altı bar penceresi bizim sabitlememizdir.
- **İcra ve çıkış:** Retest barı kapandıktan sonraki ilk uygulanabilir M1 ask/bid; long stop `min(retest_low, EMA35_retest)−0,1ATR14_H4`, short simetri. Stop girişin doğru tarafında ve mesafe pozitif değilse atla. İlk olarak stop veya **kapanmış H4'te** fiyatın EMA35'in karşı tarafına geçmesi; en geç 42 H4 bar çıkış. Bağımsız 2R sabit hedef kolu da ön kayda girsin. İşlem başına özsermayenin %0,25'i, tek açık pozisyon/varlık; spread/komisyon/kayma ve varsa funding, aynı M1'de stop/hedef çakışmasında stop önce. Kaynak yalnız EMA35 çıkışını söyler; sayısal stop/takvim/risk bizim test sözleşmemizdir.
- **Ayırıcı sınama:** Yalın EMA12/35 çaprazı, CMF eklenmiş çapraz ve retest eklenmiş üç kolu aynı olay kümesinde; [CMF+MA kırılımı](../batch_006/STRATEGIES.md) ve [EMA12/36 yapı adayı](../batch_077/STRATEGIES.md) ile sinyal örtüşmesi/net R karşılaştırılsın. CMF yönünün gerçekten katkı yapıp yapmadığı ayrıştırılmadan bağımsız üstünlük iddiası yoktur.

### RT152B — Keltner dış bant teması ve yavaş stokastik aşırılıktan çıkış

- **Kaynak çekirdeği:** KC çarpanı 3, stokastik smooth 6; fiyat alt/üst KC'ye dokunurken stokastik aşırı satımdan/alım bölgesinden çıkar; karşı bant veya orta bant hedeflenir (s. 41–44). s. 40, yatay piyasa için ADX<30 örneğini verir. KC ana dönem/ATR türü, stokastik lookback ve stop kaynakta yoktur.
- **Kapalı mum sözleşmesi:** Likit spot BTC/ETH H4. `KCmid=EMA20(C)`, `KClow/high=KCmid±3×ATR20_Wilder`; `rawK14=100(C−LL14)/(HH14−LL14)`, `slowK=SMA6(rawK14)`, `D=SMA3(slowK)`. `HH14=LL14` ise sinyal yok. `ADX14[t]<30`; long son kapanmış barda `low≤KClow`, `slowK[t−1]≤20`, `slowK[t]>20`; short `high≥KChigh`, `slowK[t−1]≥80`, `slowK[t]<80`. KC ve osilatör **t kapanışında** hesaplanır. s. 44'teki “çıkış” esas alındı; yalnız bölge içinde dönüşen stokastik ayrı varyanttır. Formül ve H4 bizim açık yorumumuzdur.
- **İcra ve çıkış:** t kapanışı sonrası ilk uygulanabilir M1; long stop `low[t]−0,1ATR14_H4`, short stop `high[t]+0,1ATR`; t anındaki **dondurulmuş KC orta bandı** hedef. Hedef yönü uygun değilse veya işlem maliyeti sonrası beklenen ödül ≤ başlangıç riskine eşitse atla. En geç 6 H4 barda çıkış. %0,25 özsermaye riski, bir açık pozisyon/varlık, ücret/spread/kayma/funding ve M1 içinde çift temasın kötümser sırası. Karşı dış bant hedefi, s. 44'ün ikinci hedef seçeneği olarak ayrı kol.
- **Ayırıcı sınama:** [BB+çift stokastik](../batch_091/STRATEGIES.md), genel bant dönüşü ve tek stokastik aşırılığa karşı aynı veri/maliyetle olay örtüşmesi; ADX ve KC dokunuşu sırayla çıkarılsın. Keltner/BB bant tanımları farklıdır, ancak ortak işlemler çift aday başarısı diye toplanmaz.

### RT152C — Haftalık pivot P geçişi, stokastik çıkış ve SAR teyidi

- **Kaynak çekirdeği:** Haftalık klasik pivot çizgisinin üstünde kapanan mum + stokastik aşırı satımdan yukarı çıkış + mum altında SAR noktası long; hedef P veya R1 (s. 45–47). s. 47–48 satış anlatısı SAR üst noktasını **zorunlu kılmaz**; bu nedenle ana aday yalnız long. Giriş/çıkış eşiği ayrıntılarını aşağıda sabitliyoruz.
- **Kapalı mum sözleşmesi:** BTC/ETH H4; önceki **tamamlanmış UTC haftasının** H/L/C'sinden Pazartesi 00:00 UTC'de `P=(H+L+C)/3`, `R1=2P−L`, `S1=2P−H` hesaplanıp hafta boyunca dondurulur. Stokastik `slowK=SMA6(rawK14)` ve `D=SMA3(slowK)`, SAR başlangıç AF 0,02/artış 0,02/azami 0,20; her ikisi yalnız kapanmış barlardan. Long t: `close[t−1]≤P`, `close[t]>P`, `slowK[t−1]≤20`, `slowK[t]>20`, SAR noktası `low[t]` altında. Göstergeler aynı kapanmış H4 barında oluşur; hafta başında eksik önceki hafta yoksa sinyal yok. P'yi seçmek, SAR ayarı ve stokastik tam formülü bizim sabitlememizdir.
- **İcra ve çıkış:** t kapanışı sonrası ilk uygulanabilir M1; stop `min(low[t],P,S1)−0,1ATR14_H4`; hedef dondurulmuş R1. Girişte R1 yön olarak ileride ve net hedef mesafesi >1R değilse sinyal atlanır. En geç 42 H4 bar veya haftalık pivot yeniden hesaplanmadan hemen önce çıkış; yeni haftaya pozisyon taşıma yok. %0,25 özsermaye riski, tek pozisyon/varlık; ücret/spread/kayma/funding ve aynı M1'de stop önce. Kaynağın hedef seçimi öznel; R1 sabitlemesi bizim test kolumuzdur.
- **Ayırıcı sınama:** [Haftalık pivot ilk temas/son yaklaşma](../batch_096/STRATEGIES.md) ve [günlük pivot+BB+ayrışma](../batch_137/STRATEGIES.md) ile aynı haftalarda eşleşen olaylar karşılaştırılsın. P kırılımı tek başına, +stokastik, +SAR kollarının net R ve işlem sayısı raporlansın; SAR formülü kullanılan kütüphane ve bar sıralaması doğrulansın.

## 2. Basitleştirilmiş SMC Trading Rehberi — Kevin M. Brown

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 24/Baskı 24/Basitleştirilmiş SMC (Akıllı Para Konsepti) Trading Rehberi - Kevin M. Brown (34 sayfa) - @eseckal.pdf>) · [tam metin](02_smc_brown.txt)

**Tam okuma:** s. 1–8 price action/SMC tanıtımı; 9–15 tepe/dip ve trend yapısı; 16–22 destek/direnç ve rol değişimi; 23–27 çoklu zaman dilimi; 28–34 hacim profili ve genel yorum. Destek/direnç dönüşü, trend yönü ve hacim alanı [mevcut yapı](../batch_081/STRATEGIES.md) ve hacim profili aileleriyle örtüşür. Belirli seviye algoritması, giriş teyidi, stop ve çıkış bir arada verilmez. Yeni bağımsız aday yok; spot FX “hacmi” merkezi gerçekleşmiş toplam hacim diye kabul edilmez.

## 3. Price Action ve Orderblock ile İleri Düzey Piyasa Yapısı Trading — James Jecool King

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 25/Baskı 25/Price Action ve Orderblock ile İleri Düzey Piyasa Yapısı Trading - James Jecool King (23 sayfa) - @eseckal.pdf>) · [tam metin](03_pa_ob_king.txt)

**Tam okuma:** s. 1–7 salınım, çoklu zaman dilimi, trend/aralık/BOS; 8–14 momentum kayması, güçlü-zayıf pivot ve anlatı; 15–21 haftalık→günlük→H4→H1→M1 örneği ve yönetim; 22–23 H1 bölge kırılımı/retesti. Son iki sayfadaki kırılım→bölgeye dönüş→önceki zirve fikri [mevcut kırılım retesti](../batch_023/STRATEGIES.md) ailesidir. “Bölge”, “güçlü ret”, “en iyi talep” ve BFI niyeti nesnel/tekil tanımlanmaz; seçilmiş örnek ve s. 22–23'teki %70 iddiası kayıtlı maliyet sonrası performans değildir. Çeviride H1, “1 yıllık” diye bozulmuş (s. 18); metinden otomatik çoklu yıl koşulu türetilmez. Yeni bağımsız aday yok.

**Parti sonucu:** 3 kitap, 105 sayfa, **3 yeni aday**. Tümü yalnız test ön kaydıdır; veri ve uygulama maliyetleriyle dış örneklem sınaması yapılana kadar işlem önerisi sayılmaz.
