# Kitap okuma 026 — mum teyidi, RSI ayrışması ve 1-2-3 dönüşü

**Kapsam:** 162 + 45 + 7 = **214 PDF sayfası**. Üç PDF'nin sayfa sıralı çıkarılmış metni aynı klasörde; 1-2-3 kitabının metinsiz hedef grafiği ayrıca [görsel olarak](pattern_page7.png) incelendi. Atıflar PDF sayfasıdır. Kaynakların verdiği kurallar ile bizim sayısal araştırma sözleşmelerimiz ayrılmıştır. Henüz backtest, paper test veya emir yok.

## 1. P. Arul Pandi — 14 Mum Kalıbı

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 4/Baskı 4/14 Mum Kalıbı - P. Arul Pandi (162 sayfa) - @eseckal.pdf>) · [Tam metin](01_fourteen_candles.txt)

Kitap çekiç, ters çekiç, asılı adam, kayan yıldız, doji çeşitleri, yutan mum, harami, sabah/akşam yıldızı, kara bulut, delici çizgi, belt hold ve üç asker/karga ailelerini açıklar (s. 36–160). Genel uyarısı tek mumu işlem nedeni saymamak, kapanış/ek teyit ve formasyon dışı stop kullanmaktır (s. 31). “14 güvenilir formasyon” ifadesi (s. 35, 161) performans kanıtı değildir. Sabah/akşam yıldızının ve bazı doji türlerinin **gap** şartı (s. 78, 81, 116, 125) 24 saatlik likit kriptoda seyrektir; gap şartını sessizce kaldırıp aynı formasyon adıyla test etmeyiz.

### P26a — Çekiç/kayan yıldız ve izleyen kapanış teyidi

- **Kaynak:** Çekiç düşüşten sonra kısa üst gövde, alt fitil gövdenin en az iki katı; yukarı kapanış teyidi ve çekiç dibi stop (s. 36–40). Kayan yıldız yükselişten sonra kısa alt gövde, üst fitil gövdenin en az iki katı; mum dibi kırılınca short ve tepe stop (s. 56–60). Kaynak uzun fitilde stop uzaklığını ayrıca sorun sayar (s. 39–40).
- **Bizim D1 deney:** Son 20 tamamlanmış D1 kapanış getirisi negatif ve `close[t-1]<EMA20[t-1]` ise düşüş bağlamı. Gün `t` için `body=abs(C-O)`, `range=H-L`; `body<=0.35range`, alt fitil `>=2body`, üst fitil `<=0.15range`, kapanış üst üçteyse çekiç. Sonraki en çok 2 kapanmış D1 günden biri `close>H[t]` olduğunda ancak takip eden ilk 1m long. Stop `L[t]-0.1 ATR14_D1[t]`; risk `>2 ATR` ise işlem yok, hedef 2R, H7D zaman çıkışı. Kayan yıldız ve short bütün eşitsizliklerin simetriği, önceki 20D yükseliş bağlamı. Sıfır gövdeli/bozuk OHLC bar elenir. `20`, `0.35`, `0.15`, `2 gün`, stop tamponu ve 2R kaynakta yoktur.
- **Karşılaştırma:** Aynı şekil olayında hemen sonraki 1m giriş, yalnız takip eden kapanış sonrası giriş, şekil+bağlam+teyit. Teyitsiz olaylar örneklemden saklanmaz. Önceki pin bar/rejection adaylarıyla örtüşen günler bağımsız strateji sayılmaz.

### P26b — Üç asker/karga sonrası uzama mı, geri çekilme mi?

- **Kaynak:** Üç beyaz asker art arda üç güçlü yükseliş mumu, iç gövde açılışı ve giderek yüksek kapanıştır (s. 151); kaynak formasyon sonrası aşırı uzama ve geri çekilme olasılığını ayrıca söyler (s. 154–155). Üç kara karga simetriktir (s. 156–159).
- **Bizim D1 araştırma olayı:** Üç ardışık kapanmış D1 mumu aynı renk; her gövde/aralık `>=0.60`, her yeni kapanış öncekinin ötesinde, son iki açılış önceki gerçek gövde içinde. Her ilk sinyal günü yalnız bir olay sayılır. İki ayrı, önceden sabit kol: (A) sonraki ilk 1m'de yönünde giriş, (B) en fazla 3 D1 gün içinde ilk `EMA5_D1` temasından sonra tekrar yönünde kapanış gelirse sonraki ilk 1m giriş; ikisinde stop üç mumun karşı uç ekstremumu veya 2ATR sınırı, hangisi daha sıkıysa **stop girişin doğru tarafındaysa**, aksi halde işlem yok; hedef 2R/H7D. `0.60`, EMA5 ve süre bizim hipotezimizdir.
- **Amaç:** Devam ve geri çekilme kollarını aynı olaylarda, dolmama oranıyla birlikte karşılaştırmak. Tek başına “üç asker kârlıdır” varsayımı yapılmaz.

## 2. Dennis Sharpe — 2023'te Etkili Swing Trading Stratejileri

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 21/Baskı 21/2023_te Etkili Swing Trading Stratejileri - Dennis Sharpe (45 sayfa) - @eseckal.pdf>) · [Tam metin](02_swing_sharpe.txt)

Ana trend, SMA ve piyasa yapısı s. 6–15; RSI ayrışması + çift tepe/dip, trend çizgisi, EMA21 veya yutan mum teyidi s. 29–41. S. 13'te kullanılan göstergeler **SMA60/EMA26/RSI4**, fakat giriş kuralı “EMA26, **SMA50** üstüne geçiyor” der; çıkış SMA60'tır (s. 14). Bu açık çelişkiyi iki varyant olmadan tek kaynak kuralı diye kodlamayız. RSI ayrışmasının ardından doğrulama aramak gerektiği s. 33–34'te belirtilir. RSI yüksek/düşükleri geçmişten doğrulanmadan seçilirse lookahead olur.

### S26a — RSI ayrışması + EMA21 kapanış/retest

- **Kaynak:** Düzenli boğa ayrışması fiyat daha düşük dip, RSI daha yüksek dip; ayı karşılığı daha yüksek fiyat tepe/daha düşük RSI tepe (s. 29–31). Sonrasında EMA21 aşımı ve mümkünse retest (s. 37–39), en son pivot dışı stop. Alternatif teyit yutan mum (s. 40–41).
- **Bizim D1 deney:** RSI14 Wilder. Fiyat pivot dibi `low[i]` iki sol ve iki sağ kapanmış D1 barın dibinden düşükse, pivot ancak `i+2` sonunda **bilinir**. Son 60 günde kronolojik iki teyitli pivot dip bulunur; son fiyat dibi öncekinin en az `0.1 ATR14` altında, aynı pivot günlerindeki RSI14 değeri önceki RSI'dan en az 2 puan yüksekse boğa ayrışması. İkinci pivot teyidinden itibaren en fazla 10 gün içinde D1 `close>EMA21` ve önceki kapanış `<=EMA21` ise sonraki ilk 1m long; stop ikinci pivot dip altı `0.1 ATR`; hedef 2R/H7D. Short simetrik. `60`, `2+2`, fark eşikleri, 10 gün ve hedef bizim seçimimizdir. Ayrı retest varyantında EMA geçişinden sonraki 3 D1 içinde EMA21'e temas ve EMA üstünde yeniden kapanış istenir; dolmayanlar raporlanır.
- **Karşılaştırma:** Aynı pivot olaylarında RSI ayrışması var/yok ve EMA teyidi var/yok; önceki RSI divergence adaylarıyla tek olay ailesi. Pivotu oluştuğu gün bilinir saymak yasak.

### S26b — EMA26/SMA60 + RSI4 geri çekilmesi

- **Kaynak:** SMA60 yukarı eğimli, fiyat üstünde, EMA26 kesişimi ve RSI4 aşırı satımdan çıkış; SMA60 altı kapanış veya EMA26/SMA60 ters kesişim çıkışı, son swing dip stop (s. 13–15). Kaynak SMA50/SMA60 çelişkisi yukarıda.
- **Bizim D1 deney:** `EMA26>SMA60`, `SMA60[t]>SMA60[t-5]`, `close>SMA60`; RSI4 önceki kapanmış günde `<30`, sinyal gününde `>=30`, sonraki ilk 1m long. Başlangıç stopu iki sağ barla teyitli son D1 pivot dip altı `0.1 ATR14`; pivot yoksa işlem yok. D1 `close<SMA60`, EMA26/SMA60 ters geçişi veya H14D'de çıkış. Short simetrik RSI4 70. SMA50 ile ilk kesişim girişinin şart olduğu alternatif **ayrı** varyant olarak, aynı veri ve masrafla ölçülür. RSI30/70 ve H14D kaynağın açık parametresi değildir.

## 3. Sunil Mangwani — 123 Grafik Formasyonu

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 8/Baskı 8/123 Grafik Formasyonu - Sunil Mangwani (7 sayfa) - @eseckal.pdf>) · [Tam metin](03_patterns_mangwani.txt)

Bu **7 sayfalık kısa 1-2-3 broşürü**, 123 farklı formasyon kitabı değildir. Boğa dönüşte 1 ilk dip, 2 tepki tepesi, 3 daha yüksek dip; 2 kırılınca long, stop 1 veya daha agresif 3 altı, ölçülen hedef `P3+(P2-P1)` (s. 1–2). Short örneği s. 3, agresif 2–3 trend çizgisi kırılımı s. 4; Fibonacci hedef anlatımı s. 4–7. S. 7 hedef grafiği görsel incelendi; çizgi/etiket örnektir, istatistiksel ispat değildir. “Çok yüksek başarı” s. 1'de verisiz iddia.

### M26 — Teyitli pivotlu 1-2-3 kırılımı

- **Bizim D1 sözleşme:** P1, P2, P3 sırasıyla pivot dip–tepe–dip; her pivot iki sol/iki sağ **tam kapanmış** D1 ile teyitli. `P3.low>P1.low+0.1 ATR14_D1`, `P2.high-P1.low>=1 ATR`, P3 ile P1 arasında 3–20 D1; P3 teyidi anında `P2.high` hâlâ kırılmamış olmalı. P3 teyidinden sonra 10 tam D1 içinde ilk `close>P2.high` sonrasında ilk 1m long. P3 oluşmadan veya teyit edilmeden P2 kırılırsa sinyal yok. Stop P1 dibi `-0.1 ATR`; ayrı agresif varyant P3 dibi `-0.1 ATR`. Ölçülen hedef `P3.low+(P2.high-P1.low)` yalnız girişin üstündeyse geçerli; değilse o hedef varyantında işlem yok. Ayrıca 2R/H7D karşılaştırması. Short simetrik. Pivot penceresi, ATR ve süre bizim sayısal hipotezlerimiz.
- **Test:** Bu olay önceki ABCD, çift dip ve piyasa yapısı kırılım aileleriyle eşleştirilir; aynı tarih/sembol tekrar “yeni bağımsız kazanç” sayılmaz. Stop P1/P3, hedef ölçülen/2R kolları aynı olaylarda, tamamlanan ve kaçan sinyallerle raporlanır. Fibonacci 1.618 uzantısı ayrıca yalnız duyarlılık testi; oran için kaynak performans kanıtı yok.

## Sıradaki test sırası

M26 pivot kırılımı ve S26a ayrışma teyidi günlük çok günlü sözleşmeye en yakın. P26a şekil+teyit deneyi önceki mum adaylarının ablation'ı olarak ele alınmalı. Tüm varyantlarda point-in-time evren, kapanmış bar, sonraki 1m dolum, ücret/spread/kayma/funding, aynı 1m bardaki stop önceliği ve zaman sıralı dış örneklem gerekir. Kaynak eşikleri ile bizim araştırma eşikleri ayrı izlenir.
