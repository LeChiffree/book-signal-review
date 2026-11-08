# Kitap okuma 033 — ATR risk katmanı, Heikin Ashi dönüşü ve çift momentum

**Kapsam:** 92 + 29 + 35 = **156 PDF sayfası**. Üç kitabın sayfa sıralı tam metni burada; Munroe'nun metin çıkmayan grafik sayfaları 11–13 ayrıca görsel incelendi. Atıflar PDF sayfasıdır. Kaynak ve bizim kripto test varsayımlarımız ayrıdır. Backtest/paper test/emir yapılmadı.

## 1. Aaron Lee Johnson — ATR Uzmanlığı

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 29/ATR Uzmanlığı - Aaron Lee Johnson (92 sayfa) - @eseckal.pdf>) · [Tam metin](01_atr_mastery.txt)

Kaynak TR'yi `max(high−low, |high−önceki close|, |low−önceki close|)` olarak tanımlar; ATR14 için hem basit ortalama hem Wilder güncellemesini sunar (s. 11–14). Stop için 1.5–3 ATR, pozisyon birimi için `risk bütçesi / stop mesafesi` (s. 18–22), 1.5–2 ATR kâr hedefi ve 1.5 ATR takip stopu örnekleri (s. 24–25). Kriptoya ATR uygulaması s. 69–71; ATR'nin geriye dönük/gecikmeli oluşu s. 72–77. Kitapta bağımsız yönlü giriş modeli yok; örnek “MA kesişimi + yükselen ATR” s. 24/34 genel bir fikirdir.

### A33 — Var olan sinyallerde ATR stop/pozisyon boyu ablatif testi

- **Bizim ortak sözleşme:** Her D1 sinyal `t` kapanışında hesaplanır, ATR14_D1 için ilk 14 TR'nin aritmetik ortalaması ve sonraki barlar için Wilder `(13*ATRönceki+TR)/14`; SMA14 varyantı ayrı kol. Giriş yalnız sonraki ilk uygulanabilir 1m'de. Başlangıç stopu `entry±k*ATR14_D1[t]`, `k∈{1.5,2,3}`; k seçimi eğitimde. Gerçek stop uzaklığı `R>0` ve maliyet/eşik üstünde olmalı. Testte sabit risk bütçesi `equity*0.005` varsayımıyla adet `budget/(R+beklenen işlem maliyeti)`, notional/leverage/likidite üst sınırlarıyla küçültülür. %0.5 bizim araştırma limitidir; kaynağın %1–2 örneği tavsiye olarak alınmaz.
- **Takip stopu kolu:** Long `max(eski_stop, en yüksek **önceki kapanmış D1 high**−1.5*ATR14[t])`, short `min(eski_stop, en düşük önceki low+1.5*ATR14[t])`; stop **asla gevşetilmez**. Kaynak s. 19/35 oynaklık artınca stop genişletmeyi tartışır; bu yeniden risk ekleyebilir, dolayısıyla ayrı ve üst bütçeli deney olmadan uygulanmaz. İlk D1 kapanışından önce ilk stop sabit. 2 ATR hedef, 2R hedef ve 7 günlük süre ayrı çıkış kolları; aynı 1m barda stop önce.
- **Kontrol:** Aynı giriş havuzunda sabit yüzde stop, sabit 2 ATR stop, ATR takip stop; ücret/spread/kayma ve gerçekleşen zarar, atlanan işlemler, pozisyon büyüklüğü/likidite. ATR yalnız volatilite ölçer; tek başına yön sinyali veya kazanç vaadi değildir. S. 22'de 25 birim örneğinin “25 dolarlık varlık” diye çevrilmesi birim hatasıdır; formül adet verir.

## 2. Edward Munroe — Heiken Ashi ve Stokastik Göstergeyle Swing Trading

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Heiken Ashi ve Stokastik Göstergeyle Swing Trading - Edward Munroe (29 sayfa) - @eseckal.pdf>) · [Tam metin](02_heikin_stoch.txt) · [Grafik s. 11](munroe_chart-11.png) · [Grafik s. 12](munroe_chart-12.png)

**Kaynak:** Kapanış SMA100 yön/eğim filtresi, fiyat aynı tarafta; trende ters Heikin Ashi mum dizisi sonrası trend yönüne renk dönüşü ve Stochastic 8,3,3 (low/high) yumuşak kesişim (s. 9–13). Stop gerçek geri çekilme dibi/tepesi ötesinde; 4H için yaklaşık 50 pip örneği diğer enstrümana taşınmaz (s. 10). Önce haftalık HA renk değişimi + stokastik çaprazı, ardından H4 temel girişler; sonrasında stop H4 SMA100'ün 10–20 pip ötesinde izlenir (s. 19–20). Kaynak birden fazla eklemeyle trendi izler, sabit kâr hedefi önermez (s. 17–18). Görsel s. 12, tüm işaretlerin kazanan olmadığını açıkça gösterir. S. 14'te HA açılışını `(high−low)/2` gibi açıklaması standart HA hesabıyla uyuşmaz; testte **standart HA** ve yalnız ham OHLC uygulanabilir fiyat kullanılır.

### M33 — W1 yön dönüşü ardından H4 HA/Stoch geri çekilme

- **Bizim hesap:** Ham tamamlanmış H4 barlardan `HA_close=(O+H+L+C)/4`, `HA_open=(önceki HA_open+önceki HA_close)/2`, `HA_high=max(H, HA_open, HA_close)`, `HA_low=min(L, HA_open, HA_close)`; ilk HA_open `(O+C)/2`, warmup 200 bar. Renk `HA_close>HA_open` yeşil, `<` kırmızı, eşit nötr. Stochastic raw `%K=100*(C−LL8)/(HH8−LL8)`, sıfır aralıkta sinyal yok; `SMA3(%K)` ve bunun `SMA3`'ü %D. Platformun “8,3,3” yorumu kontrol edilip birebir eşleşme doğrulanmalı. **HA open/close fill fiyatı değildir.**
- **W1 kapısı:** Son tamamlanmış UTC haftasında HA renk yönü değişmiş ve Stoch K/D aynı yönde kapanış kesişimi varsa sonraki **en çok dört tam hafta** boyunca o yön açık; yeni ters W1 olayında iptal. Dört hafta bizim sınırlamamızdır, kaynak kesin süre vermez. Açık haftanın rengi/kesişimi kullanılmaz.
- **H4 giriş:** Son tamamlanmış H4 barında `close>SMA100` ve `SMA100[t]>SMA100[t−5]` long; short simetrik. Önce en az 2 ters HA renk barı, sonra ilk long yeşil bar; aynı veya önceki 2 kapanmış H4 bar içinde Stoch `%K` `%D` üstüne kesişmiş olmalı. Long stop ters HA serisinin **ham OHLC** minimumunun `0.1 ATR14_H4` altı; short simetrik. Giriş sonraki ilk 1m. Kaynak “yumuşak” kesişimi sayısallaştırmadığından 2 bar pencere ve asgari %K eğimi bizim ablation parametremizdir.
- **Çıkış/karşılaştırma:** Başlangıç stop, her tamamlanmış H4 sonrası SMA100 çevresinde `0.25 ATR14_H4` tamponlu **yalnız sıkılaşan** takip stopu; azami H14D bizim operasyonel sonlandırmamız. W1 filtresiz H4 temel desenle aynı girişler karşılaştırılır; ekleme yapılan kol ancak toplam portföy riski sabit tutularak ayrı denenir. Önceki H4 HA adaylarıyla sinyal çakışması ölçülür.

## 3. Lee Tang — Dual Momentum Trend Trading

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 3/Baskı 3/Dual Momentum Trend Trading - Lee Tang (35 sayfa) - @eseckal.pdf>) · [Tam metin](03_dual_momentum.txt)

**Kaynak:** D1 GMMA kısa EMA kümesi {3,5,8,10,12,15}, uzun küme {30,35,40,45,50,60}; Full Stochastic kısa (5,3,2) ve uzun (20,3,8), RSI7 50 eşiği, EMA200 yönü (s. 10–13). Güçlü ayrışan GMMA grupları ve EMA200 hakim trend yönünde, iki Stoch trend yönünde ve RSI50 kesişimiyle giriş; zıt iki Stoch ve RSI teyidiyle çıkış; EMA60 takip stopu (s. 14–29). S. 31'deki tarama örneği GMMA'nın tamamını değil yalnız EMA15/30/60 + stochastic **%K artıyor** koşullarını kullanır; tam ticaret kuralı yerine geçmez. Kaynağın “iyi açı/ayrım” eşiği yoktur.

### T33 — D1 GMMA gücü + çift Stoch + RSI50

- **Bizim kapalı D1 long koşulu:** Tam `t` kapanışında `EMA200[t]>EMA200[t−10]`; kısa EMA'ların hepsi uzun EMA'ların hepsinden yukarıda, yani `min(short)>max(long)`; her iki kümedeki altı EMA'nın tümü `t−5`'e göre yükseliyor; `min(short)−max(long) >= 0.25*ATR14_D1` ayrım eşiği; son iki barda grup farkı büyüyor. `RSI7[t]>50` ve `RSI7[t−1]<=50`; kısa ve uzun Stoch **%D** `t` ve `t−1` arasında artıyor, `20<%D<80` ana kol. Short tümü simetrik. Ayrım/eğim/pencere ve 20–80 sınırı bizim nesnel yorumumuzdur; kaynak uç bölgeleri de döngü sayar. Kapanış sinyalinden sonra sonraki ilk 1m uygulanabilir fiyatında giriş.
- **Risk/çıkış:** Kaynak ilk stopu sayısal tanımlamaz, EMA60 takip stopu der. Bizim ana kolda ilk stop `entry−2 ATR14_D1[t]`, short simetrik; ardından kapanmış günün EMA60'ı ile **yalnız sıkılaşan** stop. EMA60 stop için yanlış taraftaysa o gün güncellenmez. İki Stoch %D ters eğime geçti **ve** RSI7 ters yönde 50'yi kapandıysa ertesi ilk 1m çıkış; ayrıca H30D azami süre bizim varsayımımız. Aynı 1m barda stop önceliği.
- **Karşılaştırma:** EMA200+GMMA trend filtresi yalnız, tek Stoch ve çift Stoch, RSI50 teyitli giriş; her adımın sinyal sıklığı ve ücret sonrası katkısı. Eski MA/RSI/Stoch trend adaylarıyla eşdeğerlik; uzun dönem EMA'ların birbirine yakınlığı çoklu bağımsız kanıt sanılmamalı. S. 30'daki %20 sermaye/%3 zarar örneği bizim portföy limiti olarak alınmaz.

## Öncelik

M33 ve T33 açık D1/H4 yön sözleşmeleri olarak adaydır; T33 daha çok filtre yığdığı için örnek kıtlığına dikkat. A33 yeni giriş sinyali değil, **aynı işlemlerde risk/çıkış karşılaştırması**dır. Tüm adaylar point-in-time evren, ücret/spread/kayma/funding, gerçekçi dolum ve zaman sıralı dış örneklemle değerlendirilmeli; kaynakların kâr iddiaları test sonucu sayılmaz.
