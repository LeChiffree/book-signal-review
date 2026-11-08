# Kitap okuma 113 — günlük Fibonacci aralığı ve hacim mumu teyidi

**Kapsam:** Üç ayrı PDF'nin **15 + 16 + 15 = 46 sayfası** baştan sona okundu. Atıflar PDF sayfasıdır. Aşağıdaki adaylar araştırma sözleşmesidir; backtest, paper test ve emir yapılmadı.

## 1. Basitleştirilmiş Fibonacci Düzeltmesi — Sankar Srinivasan

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 29/Basitleştirilmiş Fibonacci Düzeltmesi -  Forex Gün İçi Ticareti İçin Karlı İşlem Yöntemi - Sankar Srinivasan - Orijinal (15 sayfa) - @eseckal.pdf>) · [Tam metin](01_fibonacci_srinivasan.txt)

**Tam okuma:** S. 1–3 kapak/içindekiler; s. 4–9 Fibonacci tarihçesi ve oranlar; s. 9–13 gün/önceki gün high-low aralığında alış `L+0,618(H−L)`, satış `H−0,618(H−L)`, karşı uç stop, önceki ekstrem ve 1,618 uzatma hedefleri; s. 14 seans açılışından 30–45 dakika bekleme ve risk önerileri; s. 15 tanıtım. Kaynak, aynı günün henüz oluşmamış high/low'sunu geriye dönük kullanmaya izin verecek kadar esnek yazılmıştır; deneyde yalnız **önceki tamamlanmış gün** seçilir. S. 7'deki ~%90 doğruluk ve s. 14'teki 6–8/10 anlatıları denetlenebilir performans verisi değildir.

### SS113A — Önceki gün aralığının %61,8 eşiklerinden iki yönlü devam

- **Kaynak (s. 9–13):** `D=H−L`; long düzeyi `L+0,618D`, short düzeyi `H−0,618D`. Long stop `L`, hedefler `H` ve `L+1,618D`; short stop `H`, hedefler `L` ve `H−1,618D`. H/L için önceki günün tamamlanmış değerleri kullanılabilir; hangi işlem seviyesi önce gelirse o yön seçilir. Kitap gün içi tekrar işlemine izin verir, ancak kesin yeniden kurulum kuralı yoktur.
- **Kapalı mum deney sözleşmesi:** EURUSD için UTC günlük sınırla önceki tamamlanmış günün `H,L` değerlerini `00:00 UTC` anında dondur; `D>max(10 pip,0,5×ATR14_D1)` değilse gün atlanır (**bizim** gürültü filtresi). Günün ilk 45 dakikası işlem yok (**kaynağın 30–45 dakika uyarısının üst sınırı**). 00:45'ten sonra yalnız ilk kez aşağıdan yukarı `L+0,618D` geçen tamamlanmış M1 kapanışı long; yalnız ilk kez yukarıdan aşağı `H−0,618D` geçen tamamlanmış M1 kapanışı short. Önceki M1 kapanışının eşiğin diğer yanında olması şartı; seans başında zaten eşik ötesindeyse geçmişe emir dolumu yok. Aynı M1 iki eşiği keserse gün atlanır. Sinyal sonrası izleyen ilk uygulanabilir M1 bid/ask fiyatıyla giriş; gün başına en çok bir işlem (**bizim**, kaynak tekrar edebilir). Stop/ilk hedef kaynak düzeyleri; 1,618 uzatma yalnız ayrı ikinci hedef kolu. Spread/ücret/kayma dahil stop mesafesi pozitif ve hedefe net alan maliyetin en az iki katı olmalı; en çok 0,5% özsermaye riski, gün bitiminde zaman çıkışı (**bizim**). Aynı bar stop/target sırası çözülmezse kötümser stop veya tick veri. Her gün için sinyal gelmese de H/L, eşik, atlama nedeni ve emir sonucu tutulacak.
- **Ayrışma/test:** Önceki gün aralığı kırılımı ve Fibonacci geri çekilmesi adaylarına karşı aynı gün evreninde `%61,8` giriş, `%50` giriş ve koşulsuz önceki gün high/low kırılımı karşılaştırılacak. Bu adayın farkı iki **iç eşikten hangisinin önce kapanışla geçildiğine** göre günün yönünü seçmesi ve karşı uçta stop kullanmasıdır. Parametreler geçmiş sonuçlara bakılarak seçilmez.

## 2. Mum Grafiğiyle Trading Tekniği — Avinash Mudaliar

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 23/Baskı 23/Mum Grafiğiyle Trading Tekniği - Avinash Mudaliar (16 sayfa) - @eseckal.pdf>) · [Tam metin](02_candles_mudaliar.txt)

**Tam okuma:** S. 1–3 çeviri kapağı/risk; s. 4–6 yüksek hacimli, ters yönlü fitilli mum ve önceki iki muma göre hacim; s. 7–9 hemen sonraki mumda harami/inside bar veya diğer dönüş şekli, onun ardındaki yön teyidi; s. 10–12 teyit mumunun ötesinde giriş, swing dışı stop ve 1R hedef; s. 12–15 Fibonacci konum filtresi ve seçilmiş örnekler; s. 16 sonuç. S. 7'deki USDJPY örneğinde mum etiketi/fitil yönü anlatımı tutarsız görünüyor; kesin test tanımı s. 5 ve s. 9'daki açıklamaya dayanır. S. 10'daki “%100” ifadesi, aynı kitabın s. 12'de “%100 sistem yok” uyarısıyla da çelişir.

### AM113A — Hacim/fitil mumu → inside bar → yön teyidi

- **Kaynak (s. 5–11):** Long için önceki iki mumdan yüksek hacimli, kırmızı ve uzun alt fitilli mum; hemen ardından ilk mum aralığı içine kalan harami/inside bar; sonraki mum yukarı kapanışla teyit. Teyit mumunun tepesinin 1 pip üstü long tetik, son swing dibinin 1 pip altı stop, 1R hedef. Short için yeşil yüksek hacimli üst fitilli mum ve ayı teyidi simetrisi. Kaynak çok sayıda alternatif mum formasyonuna izin verir; ana hipotez için yalnız inside bar seçildi. Fibonacci konumu ayrı filtre koludur, otomatik birleştirilmez.
- **Kapalı mum deney sözleşmesi:** Tek ve sabit brokerın USDJPY M5 bid/ask mumları ve *aynı brokerın* tick-volume alanı; kaynak FX hacminin merkezi işlem hacmi olmadığını açıkça raporla. Ardışık `t,t+1,t+2`: long için `close[t]<open[t]`, `lower_wick[t]≥1,5×max(body[t],1 tick)` ve `lower_wick[t]>upper_wick[t]`, `volume[t]>max(volume[t−1],volume[t−2])`; `high[t+1]<high[t] ∧ low[t+1]>low[t]` (strict inside); `close[t+2]>open[t+2] ∧ close[t+2]>high[t+1]`. Short için renk/fitil ve kapanışın inside low altı simetri. Fitil oranı ve strict iç sınır **bizim** nesnelleştirmemiz; kaynak “daha uzun” ve “önceki ikisinden daha yüksek” der. `t+2` kapanmadan sinyal yok. Sonraki en çok 2 M5 içinde `high[t+2]+1 pip` buy-stop / `low[t+2]−1 pip` sell-stop; dolmazsa iptal (**bizim** emir ömrü). Stop long `min(low[t],low[t+1],low[t+2])−1 pip`, short karşı yüksek+1 pip; hedef 1R. Aynı M1 içi dolum/stop/hedef belirsizliğinde tick veya stop önce. M1 bid/ask spread, ücret, kayma ve en çok 0,5% özsermaye riski; 12 M5 sonra zaman çıkışı (**bizim**). Eksik hacim veya sıfır aralıkta sinyal yok.
- **Ayrışma/test:** Aynı üç mum olaylarında yüksek hacim filtresi olmadan, fitil filtresi olmadan ve harami yerine sadece sonraki yön teyidiyle ablation; kaynak Fibonacci 0,5/0,618/0,886 düzeylerine önceden teyitli pivotlarla yakınlık ayrıca kayıtlı kol. Yakınlık toleransı ve pivot doğrulama veri görülmeden sabitlenmeli. Mum kapanmadan kullanılan hacim veya seçilmiş brokerlar arasında sonradan en iyi hacim serisi seçimi yasak.

## 3. Forex ve Order Block Trading Rehberi — Raymond M. Smith

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 17/Baskı 17/Forex ve Order Block Trading Rehberi - Raymond M. Smith (15 sayfa) - @eseckal.pdf>) · [Tam metin](03_order_block_smith.txt)

**Tam okuma:** S. 1–5 SMC ve kurum anlatısı; s. 6–7 destek/direnç dışına çıkıp geri dönen sözde “kurumsal mum”, ancak son mumun önceden bilinemeyeceği itirafı; s. 8–12 likidite, spread ve haber riskleri; s. 13–15 yapı kırılımı, kırılan seviyeye retest, yönlü mum teyidi, 2–3 pip stop önerisi. “Kurumsal” niyet yalnız OHLC ile kanıtlanamaz. S. 6–7 sahte kırılım [105. partideki SFP](../batch_105/STRATEGIES.md) ve önceki sweep adaylarıyla, s. 14 kırılım-retest de arşivdeki BOS/retest adaylarıyla aynı çekirdektir. Seviye seçimi ve dönüş mumu tekil kural olarak verilmediğinden yeni bağımsız aday sayılmadı. Likidite anlatısındaki sayısal spreadler veri dönemi veya broker kaydı olmadan evrensel varsayım değildir.

## Sonuç

**2 yeni araştırma adayı:** SS113A ve AM113A. İkisi de henüz doğrulanmış strateji değildir.
