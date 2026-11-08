# Kitap okuma 082 — Ichimoku teyidi, Forex mikro sistemleri ve nicel kurallar

**Kapsam:** Üç PDF'nin gerçek **162 + 44 + 61 = 267 sayfası** sayfa sırasıyla tarandı; kritik grafikler [görsel olarak](figure_contacts/) incelendi. Atıflar PDF sayfasıdır. Yazarların seçilmiş işlem/özsermaye grafikleri kripto performansı değildir. Backtest, paper test veya emir yapılmadı. Kaynakta olmayan sayısal stop, süre ve uyarlamalar **bizim ön kayıt seçimimizdir**.

## 1. Düşük Riskli Ichimoku Stratejisi Rehberi — Karen Peloille

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Düşük Riskli Ichimoku Stratejisi Rehberi - Karen Peloille (162 sayfa) - @eseckal.pdf>) · [Tam metin](01_ichimoku_peloille.txt)

**Kaynak taraması:** S. 2–25 9/26/52 Tenkan, Kijun, Senkou A/B ve 26 dönem geriye çizilmiş Chikou; s. 26–39 çok zaman dilimli okuma; s. 40–53 mum, üçlü itki ve kapalı mum teyidi; s. 54–68 Kijun kırılımı, teknik stop, çoklu hedef; s. 69–103 kısa vadeli giriş/pozisyon yönetimi, kapanış bekleme ve oynak hedef uyarısı; s. 104–133 farklı zaman dilimi çizgilerinin çakışması; s. 134–150 trend çizgisi ve Fibonacci ile teyit; s. 151–162 disiplin/risk. Özellikle s. 73 ve 103 tamamlanmamış mumun sinyal sayılmamasını açıkça ister. S. 89–90 hareketli Kijun hedefinin işlem açıkken değişebileceğini gösterir; hedef seviyesi giriş anında dondurulmalı veya dinamik çıkış kuralı ayrı tanımlanmalı.

**Kayıt kararı:** Fiyatın Kijun'u geçmesi, bulut ve Chikou teyidi zaten [4. parti](../batch_004/STRATEGIES.md), [16. parti](../batch_016/STRATEGIES.md) ve [42. parti](../batch_042/STRATEGIES.md) kapsamındadır. Bu kitap aynı olaya **Kijun + SSB aynı fiyata yakınsa teyit**, yakın karşıt Ichimoku seviyesine kadar önceden bilinen hedef alanı ve stopu son tamamlanmış Kijun/SSB ile teknik seviyeye taşıma karşılaştırması ekler (s. 28, 54–62, 97–102, 111–113). Bunlar yeni bağımsız yön stratejisi değil; mevcut I4/I42 adayında aşağıdaki sabit filtre deneyi olarak saklanır:

- Günlük karar anında son tamamlanmış H4 barında `|Kijun26_H4−SSB_chart_H4|≤0,2×ATR14_H4` ise çakışma; `SSB_chart[t]=SSB_raw[t−26]`. Chikou için bugünkü `close[t]` t−26 konumuna çizilir; teyit olarak yalnız `close[t]>high[t−26]` long, tersi short kullanılır. Çakışmanın önceden bilinen karşıt bulut/Kijun hedefine net mesafesi başlangıç riskinin en az 1,5 katı değilse filtreli kol atlanır. `0,2 ATR`, 1,5R ve H4 seçimi **bizim** ölçülerimizdir. Aynı olay evreninde çakışmasız, çakışmalı ve hedef alanı yeterli kollarını kıyasla. Kaynağın üç mum sayımı s. 47–53'te Doji/rengi bağlama göre yeniden sınıflandırdığı için sayımın öznel biçimi bağımsız sinyale çevrilmedi.

## 2. Day Trade Forex Sistemi — Erol Bortucene ve Cynthia Macy

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 11/Baskı 11/Day Trade Forex Sistemi (44 sayfa) - @eseckal.pdf>) · [Tam metin](02_day_trade_forex.txt)

**Kaynak taraması:** S. 1–10 FX tanıtımı, risk ve platform; s. 11–18 EMA10/50, üstel BB20/2, Parabolic SAR, MACD(12,26,9), RSI14, yavaş stokastik(5,3,3) ayarı, 15–20 pip stop; s. 19–24 dar banttan 5–15 dakikalık kırılım ve göstergelerin aynı yönde oluşu; s. 25–28 EMA10/orta BB/EMA50 yönünde geri çekilme; s. 29–32 RSI/stokastik aşırı uç dönüşü; s. 33–37 hedging, %5–7 hesap riski ve platform/tanıtım; s. 38–44 bir dakikalık **EMA3 × üstel BB18 orta çizgisi**, MACD sıfır ve RSI50 teyitli mikro strateji. S. 43–44 planlı FX haberi sonrasında 1–2 dakika bekleme önerir.

**Kayıt kararı:** BB sıkışması + çoklu momentum teyidi önceki [13. parti](../batch_013/STRATEGIES.md), [46. parti](../batch_046/STRATEGIES.md) ve EMA trend dönüşleriyle büyük ölçüde örtüşür. Mikro EMA3/BB18 kurulumu ise yalnız M1/M5 kararıyla anlamlıdır; günlük kapanıştan sonra o günkü 1m kırılımını biliyormuş gibi giriş yapmak sızıntıdır. Günlük çok günlü havuza strateji başlığı eklenmedi. Ayrı bir **intraday** araştırma açılırsa, yalnız kapanmış M1 `EMA3`'ün `EMA18` (üstel BB18 orta bandı) üstüne ilk geçişi, `MACDhist>0` ve `RSI14>50` birlikte long; short simetrisi, sonraki M1 dolumu, tam maliyet ve kısa zaman çıkışı gerekir. Bu kitap böyle bir işlemin stop/çıkışını tam kurallı vermez. 5–20 pip hedefi, FX haber takvimi ve %5–7 hesap riski kriptoya aynen taşınmaz; aynı varlıkta eşzamanlı long/short “hedge” ekonomik riskin kaybolması değildir.

## 3. İşe Yarayan 5 Basit Trading Stratejisi — Jeff Swanson

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 11/Baskı 11/İşe Yarayan 5 Basit Trading Stratejisi - Jeff Swanson (61 sayfa) - @eseckal.pdf>) · [Tam metin](03_swanson_five.txt)

**Kaynak taraması:** S. 5–33 EUR vadeli/FX SMA200 ±%1 zarfı ile ters yönlü kısa vadeli işlem; ücret/kayma, gün saati, oynaklık, geniş stop ve henüz yapılmamış dış örneklem testinin etkileri; s. 34–39 RSI2 ve üç günlük toplam RSI2; s. 40–46 önceki üç günün kapanış–uç mesafesinden hesaplanan kırılım ofseti ve düşüş momentumu filtresi; s. 47–53 SMA200 altındaki dört yükseliş kapanışını short etme; s. 54–60 VIX/S&P opsiyon oynaklığına dayalı endeks modeli; s. 61 araştırma uyarıları. Zarf örneği s. 7'de M5, ileride s. 22'de bir cümlede M1 diye geçer; tek zaman dilimi ilan edip ikisini karıştırmıyoruz. S. 10–11, 31–33 stop yokluğunun büyük zarar doğurabileceğini gösterir. S. 48–53 ve 55–60 performans tablolarında komisyon/kayma düşülmemiş; sonuçlar uygulanabilir net getiri değildir. VIX, BTC/ETH için aynı ekonomik değişken olmadığından kriptoya VIX stratejisi adıyla kopyalanmaz.

### JS82A — Üç günlük kapanış–uç ofsetiyle düşüş sonrası yukarı kırılım

- **Kaynak kuralı:** Her tamamlanmış günlük mum için `m_d=max(|close_d−low_d|,|high_d−close_d|)`; üç günlük ortalama `O_t=mean(m_t,m_{t−1},m_{t−2})`. Dünkü kapanış `close_t` 40 günlük kapanış ortalamasının altındaysa gelecek seans için `close_t+O_t` stop-buy düzeyi; s. 41–42. Kaynak S&P E-mini ve M5 uygulamasıdır, short simetrisi verilmez. Stop için `O_t` ve `0,5O_t` karşılaştırılır (s. 43–46); kaynak tam çıkış süresini bu bölümde açıklamıyor.
- **Bizim günlük olay/icra:** UTC `t` D1 kapanışında yalnız tamamlanmış D1'lerden `O_t` ve `SMA40_t` hesapla. `close_t<SMA40_t` ise long bekleyen tetik `B_t=close_t+O_t` oluştur; `t+1` günündeki ilk uygulanabilir 1m'de stop-buy emrini aç, **yalnız sonraki tamamlanmış/uygulanabilir 1m fiyatı** `B_t`'yi görürse doldur. Gün sonuna kadar dolmazsa iptal; gap/1m açılışı `B_t` üstündeyse gerçek açılış ve kayma kullan. İlgili günün high değerini sinyal anında biliniyor sayma. Short kaynakta olmadığından baz değil, ancak ayrı keşif kolu olabilir.
- **Risk/çıkış:** Dolumda stop `entry−O_t`, ayrı `entry−0,5O_t`; stop mesafesi sıfır/çok küçükse atla. H3D ve H7D zaman çıkışları ve 2R ayrı ön kayıt kolları; bunlar **bizimdir**. Ücret, kayma, funding, aynı 1m stop önceliği. O gün dolmayanlar dahil tüm sinyaller sayılır.
- **Karşılaştırma:** Genel [kırılım adayları](../batch_002/STRATEGIES.md) ve [günlük aralık/ADR](../batch_006/STRATEGIES.md) ile aynı sinyal günleri. Ofset olarak 3 günlük `max(close−low,high−close)`, ATR14 ve sabit yüzdeyi **önceden** belirlenmiş kollarla karşılaştır; düşüş momentum filtresinin ek katkısını ablate et. S&P sonuçları kripto için önsel kanıt değildir.

### JS82B — SMA200 üzerinde üç günlük toplam RSI2 aşırı satımı

- **Kaynak kuralı:** S&P E-mini'de `close>SMA200`; son üç günlük `RSI2` toplamı `<45` olunca long; güncel `RSI2>65` kapanışında çıkış, 1000 USD felaket stopu (s. 34–37). Aynı bölüm yalın `RSI2<5` girişi ve `close>SMA5` çıkışını kontrol olarak verir. 1000 USD sözleşme büyüklüğüne bağlıdır.
- **Bizim kapalı D1 olay:** UTC D1 `t` kapanışında `close_t>SMA200_t` ve `RSI2_t+RSI2_{t−1}+RSI2_{t−2}<45`; aynı pozisyon açıkken tekrar giriş yok. Wilder RSI hesabı ve en az 200 günlük ısınma sabitlenir. Karar sonrası ilk uygulanabilir 1m'de long. `RSI2>65` tam günlük kapanışında, onu izleyen ilk uygulanabilir 1m'de çıkış. Long stop `entry−2×ATR14_D[t]`, H14D azami süre **bizim risk uyarlamamız**; 2R hedefi ayrı kol.
- **Karşılaştırma:** Aynı 200 günlük rejimde `RSI2<5` / `SMA5` çıkışı; [önceki RSI/BB ortalamaya dönüş](../batch_001/STRATEGIES.md) ve [RSI5 dip](../batch_070/STRATEGIES.md) ile olay çakışması. Toplam RSI2 yeni gösterge ailesi değil, giriş yoğunluğu/çıkış karşılaştırmasıdır. Yalnız ayı dönemlerinde atlanan işlemler ve maliyet sonrası net R raporlanır.

### JS82C — SMA200 altında dört ardışık yükseliş kapanışından short

- **Kaynak kuralı:** Endeks SMA200 altında; art arda en az dört gün bir öncekinden yüksek kapanış; kapanışta short; fiyat SMA5 altına düştüğünde çıkış (s. 47–48). Kaynak s. 49–53'te az işlem ve zayıf toplam katkı bulur; bu **olumsuz araştırma bulgusu** da kayıttadır. O bölümde maliyet ve koruyucu stop yoktur.
- **Bizim kapalı D1 olay:** `close_t<SMA200_t` ve `close_{t−3}<close_{t−2}<close_{t−1}<close_t`. Dört gün veya daha uzun seri sürerken **yalnız ilk dördüncü kapanış** sinyal olsun; aynı seri içinde tekrar short yok. Karar sonrası ilk uygulanabilir 1m giriş. Sonraki tam D1 `close<SMA5` olursa onu izleyen ilk uygulanabilir 1m çıkış. Stop `max(high_{t−3:t})+0,1×ATR14_D[t]`, H7D süre ve 2R ayrı kollar **bizim** seçimimizdir.
- **Karşılaştırma:** Yalnız SMA200 altı rejimde dört yukarı kapanışın ardından short, 2/3/5 gün seri kontrolleri ve [ayı piyasası stratejileri](../batch_071/STRATEGIES.md) ile aynı gün örtüşmesi. Hisse endeksi boğa sürüklenmesi/short maliyeti ile kripto funding ve short squeeze farkını ayrı ele al. Kaynaktaki zayıf sonuç nedeniyle düşük öncelikli aday.

## Ortak doğrulama

**Üç yeni araştırma başlığı** açıldı; hiçbirinin kârlılığı doğrulanmadı. [Çok günlü sözleşme](../../../research_v2/24_MULTIDAY_STRATEGY_CONTRACT.md) uyarınca yalnız karar anında bitmiş UTC D1/H4/H1, karar sonrası uygulanabilir 1m, point-in-time evren, veri boşluğu, ücret/kayma/funding ve aynı 1m'de stop önceliği geçerlidir. Kaynak tabloları, özsermaye grafikleri ve seçilmiş işlem görselleri yeniden üretilmiş backtest değildir; zaman sıralı dış örneklem ve parametre dayanıklılığı sonra araştırılacaktır.
