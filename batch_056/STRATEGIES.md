# Kitap okuma 056 — RSI güç bölgeleri, ST fraktal koridoru ve saatlik pivot

**Kapsam:** 27 + 52 + 37 = **116 PDF sayfası**. Üç PDF'nin bütün sayfaları numaralı metne çıkarıldı; sayfa atıfları PDF sırasıdır. Kaynakta verilmemiş mekanik eşikler **bizim test varsayımımız** olarak belirtilmiştir. Backtest, paper test ve emir yapılmadı.

## 1. Hima Reddy — Göreceli Güç Endeksi / Bull Bear RSI Face Off

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Göreceli Güç Endeksi - Hima Reddy (27 sayfa) - @eseckal.pdf>) · [Tam metin](01_rsi_reddy.txt)

**Kaynak:** Wilder RSI(14) sabittir (s. 5). Boğa rejiminde destek 40–50, direnç 80–90; ayı rejiminde direnç 55–65, destek 20–30 (s. 4–5). Daha küçük zaman diliminde RSI boğa destek bölgesini korurken daha yüksek dip, örnek giriş bağlamıdır (s. 18). Boğa rejimindeki 80–90 bölgesinde düşüş sapması için uzunları azaltmayı; ayı destek bölgesindeki yükseliş sapmasında short kapamayı anlatır, bu sapmaları **karşı yöne tek başına giriş** saymaz (s. 16, 23, 25). Sadece bölgeye dokunma da işlem değildir (s. 25). Seçilmiş ES/CL/IBB/NQ/YM grafiklerinden tüm piyasalarda isabet çıkarılamaz.

### RR56 — RSI(14) boğa destek bölgesini koruyan H1 higher-low devamı

- **Rejim:** Tamamlanmış D1 RSI(14), Wilder/RMA formülü. Long rejim yalnız son 5 D1 kapanışın en az 3'ünde RSI>50 ve hiçbirinde RSI<40; short simetrik olarak en az 3'ü <50 ve hiçbirinde >65. Bu 5-gün kuralı kaynağın görsel boğa/ayı ayrımının bizim sabit vekilidir. D1 barı bitmeden bugünün RSI değeri yok.
- **Sinyal:** H1 RSI(14) üzerinde kapanmış mumlarda long için RSI 40–50 bölgesine iner, RSI<40 ile bozulmadan en çok 8 H1 içinde >50 kapanır. Bu aralıkta fiyatın son teyitli H1 swing low'u (2 sol/2 sağ mumla teyit) bir önceki teyitli swing low'dan daha yüksek olmalı; teyit iki sağ H1 kapandıktan sonra geçerlidir. Short için ayı 55–65 direnç bölgesine çıkıp >65 olmadan <55'e geri kapanma ve iki teyitli lower high; tüm kurallar simetrik. Bu giriş koşulları kaynaktaki bölgede tutunma fikrinin **bizim** tekrarlanabilir yorumudur.
- **İcra:** Rejim + H1 dönüş kapanışından sonraki ilk uygulanabilir 1m giriş. Long stop giriş sinyalinden önceki bölge teması ile sinyal arasındaki gözlenmiş low `−0,1×ATR14_H1`; short simetri. 2R veya 24 H1 bar süre; yanlış taraftaki/maliyetin iki katından dar stop atlanır. Aynı 1m stop ve hedefte stop önce. Kaynağın sapma örnekleri için ayrı **çıkış filtresi**: long açıkken iki teyitli H1 high arasında fiyat higher high ve RSI lower high, ikinci RSI 80–90 ise yalnız kapanıştan sonra çıkış; short için 20–30'da ters sapma. Bu çıkış ayrı ablation koludur, gecikmiş pivotu geçmiş bara geri yazma.
- **Karşılaştırma:** Önceki RSI rejim ve trend devam adaylarıyla aynı olayları eşleştir. 40–50/55–65 bölgelerinin 30/70 basit kuralı ve filtresiz higher-low karşısındaki ek katkısını ölç. Sapma uyarısını ters yöne otomatik emir haline getirme.

## 2. Vladimir Poltoratskiy — Forex Stratejisi: ST Kalıpları Trade Kılavuzu

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Forex Stratejisi - ST Kalıpları Trade Klavuzu - Vladimir Poltoratskiy (52 sayfa) - @eseckal.pdf>) · [Tam metin](02_st_patterns.txt)

**Kaynak:** Üç mum fraktalında merkez mum iki komşusundan daha yüksek/düşük olmalı; sağ mum tamamlanınca seviye kesinleşir (s. 2–3, 7). Son iki karşı fraktalın arasındaki mesafe “koridor”; kırılan fraktal başlangıç, karşı fraktal stop çizgisidir (s. 2, 6–9). EURUSD H1 örneğinde 7 pip kırılım sonrası limit giriş ve başlangıç çizgisinden koridor yüksekliğinin %400'ü hedef anlatılır (s. 4–6). %210 ara seviye, ADR(5)'in yarısı üst koridor sınırı ve çok küçük koridorları eleme vardır (s. 4, 10, 18–19). Kitaptaki %10 işlem riski (s. 10) ve seçilmiş 2017 ayına ilişkin yaklaşık %300 getiri anlatımı (s. 22–42) güvenilir genelleme veya uygun pozisyon boyutu değildir.

### ST56 — Tamamlanmış H1 fraktal koridoru kırılımı ve ilk limit retesti

- **Kurulum:** H1 mumları; üst/alt fraktal merkez mum, iki komşu **kapanmış** H1'e göre sıkı high/low ekstremi. Eşit ekstrem yok. Son teyitli üst ve alt fraktal arasında `W=upper−lower>0`; ikisi de son 48 H1 içinde, oluşum sırasına bakılmaksızın. Koridor `W` en az `0,5×ATR14_H1`, en çok **önceden kapanmış beş UTC günün** günlük high-low ortalamasının yarısı olmalı. Alt eşik bizim kripto vekilimiz; üst eşik kaynak ADR(5) kuralıdır. Tamamlanmamış fraktal hiçbir koşulda geçmişte kullanılmaz.
- **Kırılım ve emir:** Long için ilk tamamlanmış H1 `close>upper+0,1×ATR14_H1`, short `close<lower−0,1×ATR`; 0,1 ATR Forex 7 pip eşiğinin bizim volatiliteye ölçeklenmiş vekilidir. Kırılım kapanışında upper/lower, W ve ATR dondur. Sonraki 4 H1 içinde long limit `upper+0,1×ATR`, short limit `lower−0,1×ATR` ilk gerçek 1m temasta dolabilir; açılış/gap emir fiyatını atlarsa kötü uygulanabilir fiyattan doldur veya atlama politikasını önceden sabitle. İlk retest dışında yeniden deneme yok. Kaynaktaki kırılım sonra limit dönüşünü taşır.
- **Risk/hedef:** Long stop `lower−0,1×ATR`, short `upper+0,1×ATR`; kaynaktaki karşı fraktal mantığı. Hedef long `upper+4W`, short `lower−4W`. Girişten hesaplanan net risk/ödül 4R **değildir**; retest fiyatı ve tamponlar nedeniyle ayrıca hesaplanır. Hedef yanlış tarafta veya maliyetin iki katından dar stop varsa atla. 48 H1 bar süre, aynı 1m stop/hedefte stop önce. %210 ara seviyede stopu başa başa çekmek ayrı kol; bunu ana kolla karıştırma. Pozisyon riskini sabit küçük oranla değerlendir; kaynak %10'u uygulama.
- **Karşılaştırma:** Önceki fraktal kırılım adaylarına karşı koridor genişliği filtresi, retest ve 4W hedefinin ayrı katkısı. Kaynak örneklerinin seçilmiş dönem ve döviz pip birimi kripto sonucuna aktarılmaz.

## 3. Jan Arps — Swing Trading: Piyasa Dalgalarında Sörf Yapmak

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Swing Trading - Piyasa Dalgalarında Sörf Yapmak - Jan Arps (37 sayfa) - @eseckal.pdf>) · [Tam metin](03_swing_arps.txt)

**Kaynak:** ZigZag'ın son ayağı teyide kadar değişir; yalnız gerekli ters hareket tamamlanınca pivot kesinleşir (s. 9–10). Beş pivotlu swing ve Fox dalga ilişkileri verilir (s. 10–12); bu çizimleri sonradan oluşmuş pivotla geçmişe koymak ileriye bakma hatasıdır. Önceki gün/hafta/ayın high, low ve ortası destek/direnç araçlarıdır (s. 21–22). Önceki **tamamlanmış** H1 high/low/close'dan sonraki saat için klasik pivot, R1, S1 çizgileri üretme fikri açıkça anlatılır (s. 22–23). Göstergeler/ticari platform tanıtımı kârlılık delili değildir. Kitap H1 pivot çizgisine tek başına giriş, stop ve hedef vermediğinden aşağıdaki etkileşim kuralı bizim hipotezimizdir.

### JA56 — Önceki tamamlanmış H1 klasik pivot S1/R1 reddi

- **Önceden bilinen seviye:** Her H1 kapanışında `P=(H+L+C)/3`, `R1=2P−L`, `S1=2P−H` yalnız o **tamamlanmış** saatin H/L/C'siyle hesaplanır ve sonraki saat boyunca sabit kalır. Aynı anda `ATR14_H1` yalnız kapanmış barlarla hesaplanır. Gelecek saat high/low asla pivot hesabına girmez. Günlük/seanslık pivot yerine saatlik güncelleme kitabın s. 23'ündeki ayırıcı öneridir.
- **Temas/teyit:** Sonraki saat içindeki M5 mumlarından ilki long için `low≤S1+0,1×ATR14_H1` ve `close>S1` ile reddeder; short için `high≥R1−0,1×ATR` ve `close<R1`. Giriş ancak bu M5 kapanışından sonraki ilk uygulanabilir 1m fiyat. S1/R1 yalnız o saat geçerli; sonraki saatte oluşan temas eski seviyeye ait sinyal sayılmaz. Aynı saat ve yönde ilk temas. Bu retest mumu ve ATR toleransı bizim yorumumuzdur.
- **Risk/hedef:** Long stop `min(S1, sinyal M5 low)−0,1×ATR14_H1`; short simetri. Ana hedef pivot `P`, fakat yalnız girişten **en az 1R** uzaktaysa al; değilse işlem yok. 12 M5 bar süre. Ayrı 2R standart hedef kolu. Aynı 1m stop/hedefte stop önce; yanlış tarafta/maliyetten dar stopu atla.
- **Karşılaştırma:** D1 pivot ve önceki gün high/low adaylarıyla aynı zamanda net getiri ve işlem yoğunluğu karşılaştır. Saatlik pivot, çok daha sık seviye ürettiği için spread/kayma etkisi özellikle önemlidir. ZigZag/Fox için doğrulanmamış son pivot üzerinden bu adaya ek sinyal üretme.

## Ortak test notu

Her stratejide sembol evreni, zaman dilimi, parametreler ve çakışan pozisyon politikası önceden dondurulmalı. Zaman sıralı ayrılmış doğrulama, sonraki uygulanabilir 1m fiyat, ücret/spread/kayma ve perpetual funding, eksik barlar, aynı bar stop/target kötümser sırası uygulanmalı. Net R, işlem sayısı, drawdown, alt dönemler ve yalın taban çizgisi raporlanmadan “işe yarıyor” sonucu yoktur.
