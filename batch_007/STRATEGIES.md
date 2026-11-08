# Kitap okuma 007 — SMA/RSI, Momentum ayrışması, mum–Ichimoku

**Kapsam:** 7 + 23 + 82 = **112 PDF sayfası** sayfa numarasıyla çıkarılıp incelendi. Aşağıdaki sayılar PDF sayfasıdır. Kaynaklarda Forex ve seçilmiş 2009 grafikleri bulunur; bunlar kripto getirisi kanıtı değildir. Tamamlanmış mumla üretilemeyen çizim yorumları sayısal hipotez olarak ayrıca işaretlendi. Backtest ve paper test yapılmadı.

## 1. 5 SMA 5 RSI Forex Trading Stratejisi

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 9/Baskı 9/5 SMA 5 RSI Forex Trading Stratejisi (7 sayfa) - @eseckal.pdf>)

PDF iki yakın kılavuz içeriyor. İlki SMA5 geçişi, RSI5'in 50 üzerinde/altında olması, sinyal mumunun ötesinde stop giriş ve karşı uç stop ile 3R hedefini veriyor (s. 1–3). İkincisi aynı çekirdeğe belirgin mum, sıkışma/kırılım ve dalgalı piyasa uyarısı ekliyor (s. 4–7). İlk kılavuzun satış bölümünde alış emri ve alış stopu sözcükleri tekrar edilmiş (s. 2–3); kısa yön için ikinci kılavuzun açık satış tarifi (s. 6) esas alınacak. `10`, `2–5` ve `5` pip Forex'e özgü, kriptoya kopyalanmaz.

### SR1 — SMA5 geçişi ve RSI5 yön teyidi

- **Kaynak kuralı:** Fiyat SMA5 üzerine geçip mum üzerinde kapanır ve RSI5>50 ise boğa; kapanmış sinyal mumunun biraz üstünde alış stop emri, düşük ucun biraz altında zarar stopu, 3R veya önceden görülen swing tepe hedefi (s. 1–2, 5). Aşağı geçiş, RSI5<50, mum altından satış stopu ve yüksek ucun üstünde zarar stopu kısa yön (s. 6). Yatay piyasada yanlış sinyal uyarısı (s. 3, 7).
- **Kapalı günlük olay:** `close[t-1]<=SMA5[t-1] && close[t]>SMA5[t] && RSI5[t]>50` uzun, tersi kısa. RSI Wilder hesabı sabitlenecek. Kaynağın `>10 pip` ayrışması yerine SMA'dan uzaklık `abs(close[t]-SMA5[t])/ATR14[t-1]` raporlanır; `>=0.1` ATR filtresi **bizim varyantımız**, baz kural değildir.
- **Emir:** t kapanınca `high[t]+1 tick` buy stop veya `low[t]-1 tick` sell stop; yalnız sonraki bir gün açık (**emir ömrü bizim seçimimiz**). İlk stop karşı mum ucu `±1 tick`; ancak stop uzaklığı en fazla `3 ATR14[t-1]` ise işlem kabulü, bu kapı da bizim risk kontrolümüz. Hedef `3R`, ayrıca 1R/2R ve 3/7/14 gün duyarlılık sürümleri. Dolmayan emirler ve girişten önce karşı uç kırılması ayrı sayılır; 1m fiyat sırası ile çözülür.
- **Ayrıştırma:** Yalın SMA5 geçişine karşı RSI>50 filtresinin marjinal katkısı, sonra ATR uzaklık kapısı ve sıkışma filtresi ayrı karşılaştırılır. RSI ve SMA aynı yakın dönem fiyatını kullandığından çakışma yüksek olabilir. Aynı gün kitap 004 I2 veya MA kesişimiyle çakışırsa tek olay kimliği.

## 2. Jus Forex Signals — Forex Momentum Stratejisi

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 12/Baskı 12/Forex Momentum Stratejisi - Jus Forex Signals (23 sayfa) - @eseckal.pdf>)

Kaynak günlük/H4 için Momentum(7) kullanıyor (s. 5–8). Fiyatın daha düşük dip yaparken osilatörün daha yüksek dip yapması boğa; daha yüksek tepeye karşı daha düşük momentum tepesiyse ayı ayrışması. **Giriş, ayrışmadaki osilatör ara tepe/dibinin kırılmasıdır** (s. 8–12; s. 11 grafiği görsel denetlendi). Önceki fiyat ekstremumu ±5 pip stop (s. 13), fiyat yeni barın önceki bar uçları ötesinde kapanınca stop taşıma (s. 13), Fibonacci hedefleri (s. 15) önerilir. Haftalık/aylık destek ve direnç ile RSI7 ayrışma teyidi (s. 20–22) seçmeli. Metin öznel karar gerektirdiğini açıkça söyler (s. 3). Haber filtresi mevcut fiyat verisiyle bilinmez; veri sağlanmadıkça uygulanmaz.

### M1 — Teyitli iki pivot arasında Momentum(7) ayrışması ve osilatör kırılımı

- **Kaynak fikri:** Fiyat dip 2 < dip 1, Momentum dip 2 > dip 1; aradaki Momentum tepesinin aşılması uzun tetik. Short simetri. Kaynak Momentum formülünü belirtmiyor; implementasyonda `MOM7[t]=100×close[t]/close[t-7]` seçimi **bizim tanımımızdır**. `close[t]-close[t-7]` sürümü ayrı duyarlılık testi, sonuçlar karıştırılmamalı.
- **Nedensel pivot:** Günlük dip `p` ancak iki sağ mum kapandıktan sonra (`k=2`) onaylı. Son iki onaylı fiyat dipleri en fazla 30 gün arayla ve `low[p2]<low[p1]`; aynı pivot günlerindeki MOM7 `MOM[p2]>MOM[p1]`. İki pivot arasında, `p2` onaylandığı anda bilinen `max(MOM[p1:p2])` tetik seviyesini dondur. Sonraki en fazla 10 kapanmış günlük mumda `MOM[t-1]<=level && MOM[t]>level` ilk kez olursa sinyal. `k=2`, 30 ve 10 gün **bizim nesnelleştirmemiz**; kaynak kesin sınır vermez. Short: iki onaylı fiyat tepesinde higher high / MOM lower high ve aradaki `min(MOM)` altına geçiş.
- **Yürütme:** MOM kırılımı ancak t kapanışında bilinir; giriş sonraki ilk 1m. Long ilk stop `low[p2]-0.1 ATR14[t-1]`, short `high[p2]+0.1 ATR`; 0.1 ATR Forex 5 pip yerine bizim ölçek uyarlamamız. Stop taşımayı, yalnız günlük kapanış `close[t]>high[t-1]` (short ters) olduğunda bir önceki bar dibi üzerinden **ayrı** sürümde dene; stop hiçbir zaman gevşetilmez. 2R/3R ve 3/7/14 gün çıkışları, Fibonacci hedeflerinden ayrı bazlardır.
- **Kontrol:** Aynı iki pivotun yalnız fiyat dönüş sinyali, RSI7 ayrışma filtresi, haftalık/aylık destek yakınlığı ayrı ablation. RSI7 filtresi de aynı pivot günleriyle ve teyit zamanıyla hesaplanır. Önceki batch 002 RSI/MACD ayrışmaları ve batch 005 S1 ile aynı fiyat pivotları çakışabilir; tekil sinyal değil, gösterge ek değerini karşılaştır.

## 3. Action Forex — Gelişmiş Mum ve Ichimoku Stratejileri

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 9/Baskı 9/Gelişmiş Mum ve Ichimoku Stratejileri - Action Forex (82 sayfa) - @eseckal.pdf>)

S. 4–22 trend, destek/direnç, üçgen ve baş-omuz gibi formasyonları; s. 23–28 Fibonacci çekilme/projeksiyonlarını; s. 29–39 mumları; s. 40–47 Ichimoku bileşenlerini açıklar. S. 48–81, ağırlıkla 2009 Forex H4 örnekleri ve grafiklerdir; s. 82 sonuçtur. Çekiç, yutan mum, çift tepe/baş-omuz, bulut kırılımı ve Tenkan/Kijun kesişimi önceki batch 003–005 ve 004 I1/I2'de kayıtlıdır. Tekrardan bağımsız başarı kanıtı çıkarılmadı. Kitap s. 25'te Fibonacci uç seçiminin “sanat” olduğunu kabul eder; geçmişten sonra seçilen uçlarla geriye dönük kusursuz seviyeler kurulamaz.

### AI1 — Tenkan/Kijun kesişimi sonrası Kijun/bulut geri çekilmesi

- **Kaynak:** Tenkan9, Kijun26'yı yukarı kesince alış; fiyat ikisinin ve bulutun üzerindeyse daha güçlü. Stop Kijun altında; ters kesişim çıkış (s. 41–45). 20 Mayıs 2009 örneğinde kesişimden sonra Tenkan'a veya kırılan dirence dönüşten alış düşünülür (s. 48–50). 30 Haziran örneğinde bulut üstüne çıkıştan sonra Kijun üstünde dönüş girişi anlatılır (s. 71–75). Bunlar seçilmiş işlemler.
- **Test sürümü:** Önceden kayıtlı I2a boğa kesişimi t gününde oluşur; `close[t]>cloud_top[t]` koşulu. `cloud_top[t]=max(rawA[t-26],rawB[t-26])`; `rawA=(Tenkan9+Kijun26)/2`, `rawB=(HH52+LL52)/2`. Yalnız sonraki 1–10 gün içinde ilk `low<=Kijun` teması ve `close>Kijun && close>cloud_top` teyidi kapanınca uzun sinyal. Kijun çizgisinin gün içinde değişmesi nedeniyle limit emri yerine **kapanış teyidi** seçildi. 10 gün ve teyit eşiği bizim uyarlamamız; kaynakta sabit süre yok. Short simetri.
- **Yürütme:** Teyit sonrası ilk 1m; stop sinyal anında bilinen Kijun/bulut alt sınırından daha aşağı olanı `-0.1 ATR14`, short simetri. 2R ve 3/7/14 gün, ters Tenkan/Kijun kesişimi ayrı çıkışlar. Baz: tüm I2a kesişimleri; geri dönüş beklemenin dolum oranı ve net katkısı raporlanır. Böylece AI1 yeni bağımsız Ichimoku stratejisi sayılmadan I2a **giriş varyantı** olarak test edilir.

### AI2 — Bulut sınırında dönüş mumu, keşif alt grubu

- **Kaynak:** Bulut/Kijun çevresindeki sabah yıldızı, kayan yıldız, çekiç ve akşam yıldızı seçilmiş girişleri destekliyor (s. 58–62, 69–71, 77–79). Mumların tek başına bağlam dışı teyit olarak alınmaması gerektiği s. 31, 34, 38–39'da vurgulanır.
- **Test kararı:** Önceki C1/C2 mum olaylarına `abs(close-cloud_boundary)<=0.25 ATR14[t-1]` ve `Kijun` yakınlığı etiketleri eklenebilir; `0.25 ATR` bizim eşik. Aynı mum I1/I2/AI1 ile çakışırsa yeni işlem üretmez. Sinyal ertesi 1m, stop mum ekstremumu, 2R ve 3/7/14 gün çıkışı C1/C2 ile aynıdır. Bulut yakınlığının yalın mum ve yalın buluta göre ek katkısı ölçülecek. Kripto 24/7 piyasasında klasik sabah/akşam yıldızı gap koşulları nadir olabilir; gapsiz eşdeğer ayrı hipotez olarak etiketlenmeli.

### Ertelenen/tekrar fikirler

- Üçgen, bayrak, baş-omuz ve ölçülen hedefler (s. 14–22) önceki grafik formasyonu aileleriyle çakışır; burada pivot/çizgi belirleme sınırları tam kodlanmadığı için yeni strateji sayılmadı.
- Fibonacci `%38.2/%50/%61.8` geri çekilme ve uzatma (s. 23–28), sonradan en iyi ucu seçme sızıntısı olmadan ancak **önceden teyit edilmiş** iki pivotla denenebilir. Tek başına alım sinyali değildir; AI1 hedef/filtre ablation adayı.
- Kitabın `Chikou`yu grafiği sadeleştirmek için çıkarma tercihi s. 47'de açık. AI1 bazında Chikou şartı eklenmedi. Bulutun ileri çizimi gelecek fiyat bilgisi değildir; uygulama I1'in zaman hizalamasını kullanır.

## Ortak uygulama kaydı

1. **Öncelik:** M1 (özgün osilatör tetikli ayrışma) ve SR1 (tam emir şemasına yakın basit baz). AI1 ve AI2 mevcut Ichimoku/mum adaylarının ek katkı testleri.
2. **Veri:** UTC kapanmış günlük OHLCV; yalnız onaylanmış pivot ve o anda bilinen gösterge. H4 kaynak örnekleri günlük kripto testinin sonucu gibi gösterilmez; H4 sürümü ayrı kohort olur.
3. **İşlem simülasyonu:** Karar t kapanınca; giriş en erken sonraki 1m, pending emir ömrü ve dolmama kaydı, 1m sıralaması, spread/komisyon/kayma/funding, eşzamanlı pozisyon sınırı. Sonuçlarda net R, işlem sayısı, belirsiz dolum, rejim ve dış örneklem duyarlılığı. Kitapların tekil kazanç örnekleri başarı oranı yerine geçmez.
4. **Durum:** Strateji sözleşmeleri kaydedildi; backtest, paper emir veya canlı işlem yok.
