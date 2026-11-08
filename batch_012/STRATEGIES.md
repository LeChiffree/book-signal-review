# Kitap okuma 012 — Trend filtresi, CPR/pivot olayları ve EMA8 dönüşü

**Kapsam:** Üç PDF'nin **61 + 103 + 43 = 207 PDF sayfası** işlendi. Aşağıdaki sayılar dosyanın PDF sayfalarıdır. Kaynakların Forex ve Hindistan endekslerinden gelen kuralları ile kripto için bizim nesnelleştirdiğimiz deneyler ayrı tutuldu. Buradaki adaylar kârlılık kanıtı değildir; bu partide backtest, paper test veya emir yapılmadı.

## 1. Oliver Hille — Mükemmel Trade Oluşturmak

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 9/Baskı 9/Mükemmel Trade Oluşturmak - Oli Hille (61 sayfa) - @eseckal.pdf>)

Kitapta tek başına eksiksiz giriş sistemi yok. Ancak 10/20/50/200 **SMA** çizgilerinin birlikte aynı yöne eğimli ve ayrışmış olmasını trend göstergesi sayıyor (s. 29). Momentum yönünde işlem, tepe/dip tahmininden kaçınma (s. 7–9), başlangıç stopu ve zarar eden pozisyona eklememe (s. 7, 9–10), en az 3:1 hedef fırsatı (s. 7, 11–12), kârda takip eden stop (s. 10–11, 27) ve korelasyonlu pozisyonların toplam riski (s. 25–26) uygulanabilir fikirler. RSI/MACD uyumunu fiyat teyidi, pivotların birleşmesini destek/direnç sayıyor (s. 30–31); sayısal giriş eşiği vermiyor. Kitaptaki %50 yön olasılığı ve 3R ile kârlılık çıkarımı istatistiksel kanıt olarak kullanılmaz.

### H12 — Dört SMA trend filtresinin marjinal katkısı

- **Sinyal değil, filtre deneyi:** Önceden tanımlı momentum/kırılım girişlerine H1 kapanışında long için `SMA10>SMA20>SMA50>SMA200` ve her SMA'nın `t` değeri `t-3` değerinden büyük; short için tam tersi. Ayrışma için dört ardışık SMA farkının da `>0.05 ATR14_H1[t-1]` olması ek varyant. Sıralama, üç bar eğim ve 0.05 ATR **bizim** kesinleştirmemiz; kaynak yalnız birlikte eğim ve ayrışma diyor. Önce filtresiz baz, sonra sıralama, eğim ve ayrışmayı ayrı ekle; mevcut batch 004/011 MA ve trend adaylarıyla aynı işlemleri yeniden bağımsız strateji diye sayma.
- **Risk kontrolü:** Sinyalin kendi fiyat temelli stopu ve R değeri korunur. 3R hedefi ile 2R ve takip eden stop aynı girişlerde karşılaştırılır. `3R` gerçekleşecek kâr vaadi değildir. İşlem riski için sabit üst sınır ve eşzamanlı korelasyonlu varlıkların toplam açık riski raporlanır; kitap s. 25'te yaklaşık %1 işlem riski örneği verir, bu zorunlu optimum değildir.

## 2. Vikram Prabhu — Pivotlarla Günlük Trading ve Price Action

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 9/Baskı 9/Pivotlarla Günlük Trading ve Price Action - Vikram Prabhu (103 sayfa) - @eseckal.pdf>)

Kaynak 15 adlandırılmış gün içi örüntü listeliyor (s. 35); önemli bölümü aynı **ilk mum / PDH-PDL / CPR kırılım veya retest** olay ailesine giriyor. Günlük merkez pivot `P=(önceki H+L+C)/3`, `R1=2P-L`, `S1=2P-H`, `R2=P+(H-L)`, `S2=P-(H-L)` (s. 8). CPR'nin üst/alt bileşen formülü metinde açık yazılmıyor; testte kullanılacak `BC=(H+L)/2`, `TC=2P-BC`, `CPR_low=min(BC,TC)`, `CPR_high=max(BC,TC)` **bizim formül sözleşmemizdir**. Kaynağın kendi test kapsamı yalnız Nifty ve Bank Nifty (s. 100); kriptoya doğrulanmış sonuç olarak aktarılamaz. İlk seans mumu, gap ve öğleden sonra etkisi 24 saatlik kriptoda yoktur; aşağıdaki UTC sınırı deneysel uyarlamadır.

### P12a — UTC gününün ilk M5 mumunda CPR'yi baştan sona geçme

- **Kaynak:** PPT'de ilk M5 boğa/ayı mumunun CPR'nin bir kenarından diğerine uzanıp dışarıda kapanması; giriş kapanışta, stop mumun/CPR'nin karşı tarafında, hedef bir sonraki direnç/destek (s. 46–49). OD'nin ilk mum PDH/PDL ötesi kapanışını ayrı etiketle (s. 36–40), aynı olayı ikinci işlem sayma.
- **Bizim test kuralı:** UTC `00:00–00:05` ilk kapanmış M5 barı için long `open<=CPR_low && close>CPR_high && close>open`, short `open>=CPR_high && close<CPR_low && close<open`. Önceki tam UTC günün H/L/C değerleri gün başında dondurulur. Giriş M5 kapanışından sonraki ilk işlem yapılabilir 1m. Stop karşı CPR sınırı `±1 tick`; mum karşı ucu alternatifi. Hedef yöndeki ilk `P/R1/R2/PDH` veya `P/S1/S2/PDL` düzeylerinden girişten sonra kalan ilk düzey; düzey `<=1R` uzaksa filtreli varyant işlem dışı. 2R ve 3R sabit hedef de karşılaştırılır. İlk mum koşulu UTC gününün borsa açılışı olduğunu iddia etmez; UTC sınırı etrafında etki yoksa strateji elenir.

### P12b — Virgin CPR'ye ilk dönüşte reddedilme

- **Kaynak:** Fiyatın önceki CPR'ye hiç girmemesiyle kalan virgin CPR'ye ilk geliş, yakınında ters mum teyidi, stop CPR'nin öteki yanında (s. 15–16, 57–60). Kaynak geçmiş 5–6 seansı daha anlamlı görüyor; bu gözlem kanıtlanmış oran değil.
- **Bizim test kuralı:** Önceki tam günde hesaplanan CPR aralığı, onu izleyen tamamlanmış günlerin hiçbir M5 `high-low` aralığıyla kesişmemişse `virgin`. Yalnız sonraki **1–5 tam UTC gün** içindeki ilk temas kabul edilir. Üstten gelen fiyat için ilk temas M5'i `low<=CPR_high` ve `close>CPR_high` ile bitirirse long; alttan gelişte `high>=CPR_low` ve `close<CPR_low` ise short. Aynı bar CPR'nin tümünü aşarsa reddedilme sayma. Stop karşı CPR kenarı `±1 tick`; hedef bugünkü P veya 2R, hangisinin uygulanacağı önceden ayrı deney. `1–5 gün`, temas ve kapanış eşiği bizim nesnelleştirmemiz. PDH/PDL başarısız kırılımlarıyla olay çakışması kaydedilir.

### P12c — Gün içi CPR konsolidasyonu sonrası ilk çıkış

- **Kaynak:** CPR içinde kısa konsolidasyon ardından güçlü mumla çıkış, stop CPR'nin karşı tarafı/çıkış mumunun karşı ucu (s. 78–81). Kaynak dar CPR'nin trendi destekleyebileceğini (s. 13–14) söylerken s. 78'de dar CPR çıkışlarının güçlü olmadığını da söylüyor: genişlik **yönsel kural değil, ölçülecek rejim etiketi**.
- **Bizim test kuralı:** Önceki tam UTC günün CPR'si sabit. Son 12 M5 barının en az 9'unun kapanışı CPR içinde ve bu aralıkta CPR dışına kapanış yoksa konsolidasyon. Sonraki ilk M5 `close>CPR_high+1 tick` (short simetrik) ve gövde `>=0.5 ATR14_M5[t-1]` ise olay. Sonraki 1m giriş; stop karşı CPR kenarı veya tetik mum karşı ucu ayrı, hedef sonraki pivot/2R, zaman çıkışı 12/24/48 M5 ayrı. `12/9`, 0.5 ATR ve zaman sınırları bizim seçimimiz. CPR genişliği `width/ATR14_1d[t-1]` kantillerinde raporlanır, en iyi kantil geçmiş veriye bakıp seçilmez.

**Birleştirilecek/ertelenecek:** Açılış drive/drive reversal (s. 36–45), büyük ilk bar retesti (s. 61–68), ilk bar ekstremumunun ters kırılması (s. 90–98) P12a ile aynı ilk mum evreninde ek olay etiketleri. Gap rejection (s. 69–77) 24/7 kriptoya taşınmaz. M/W dönüşleri (s. 82–89) önceki formasyon kayıtlarıyla çakışır. Nifty/Bank Nifty birlikte teyidi BTC ile başka coin arasında **kaynak kuralı değildir**. Yeni bağımsız strateji sayısını artırmadan önce bu etiketlerin marjinal katkısı ölçülür.

## 3. Thato Babedi — Günde 20 Pips Stratejisi

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 9/Baskı 9/Günde 20 Pips Stratejisi - Thato Babedi (43 sayfa) - @eseckal.pdf>)

Kaynak **M15 ve EMA8** kullanır (s. 28–30). Short: 4–5 yeşil mum, ilk kırmızı, ondan daha düşük ikinci kırmızı (s. 34–35), ardından EMA8 altına geçen ve kapanan kırmızı mum (s. 36). Long: 4–5 kırmızı, ilk ve ikinci yeşil; fakat s. 39–40 **ikinci yeşilin ilkinden daha düşük** olduğunu söyler. Bu, yükseliş teyidi açısından belirsizdir; sessizce “daha yüksek” diye değiştirmiyoruz. İki teyidin aynı mumda olabileceği belirtilir (s. 41). FX stop 10 pip/hedef 20 pip (s. 37, 41) kriptoda sabit değer olarak kullanılamaz. Kitabın kazanma/gelir iddiaları denetlenmiş performans değildir.

### B12 — M15 EMA8 dönüş olayı

- **Short baz:** Art arda tam 4 veya 5 yükseliş (`close>open`) M15 mumundan sonra ilk düşüş mumu `r1`; onu izleyen ilk düşüş mumu `r2` için `close[r2]<close[r1]`; `r2` veya sonraki en fazla 3 M15 mum içinde ilk düşüş mumu `open>=EMA8` ve `close<EMA8` ile aşağı geçip kapanırsa sinyal. Aradaki yeşil mumlar varsa bazda iptal. Kaynağın “daha düşük” ifadesini *kapanış* olarak sabitleme, `3 mum` pencere ve sıkı geçiş tanımı **bizim** seçimimiz; low/high kıyasını ablation yap. Dört ve beş mum ayrı etiket.
- **Long iki ön kayıtlı varyant:** (1) **Literal çeviri:** ikinci yeşil `close[g2]<close[g1]`; (2) **simetrik hipotez:** `close[g2]>close[g1]`. İki varyant asla tek sonuç gibi havuzlanmaz. Her ikisinde 4/5 kırmızı ön koşulu ve yeşil barın EMA8 üstüne geçip kapanması gerekir. Long tarafı PDF s. 39–40 yüzünden kaynak yorumu belirsiz olarak işaretlenir.
- **Çıkış:** EMA geçişi kapanınca sonraki 1m giriş. Stop short için formasyon başlangıcından sinyale kadarki en yüksek fiyat `+1 tick`; long için en düşük `-1 tick`; 2R hedef. Bu stop, FX 10 pip yerine **bizim fiyat temelli uyarlamamızdır**. `0.5 ATR14_M15` stop/2R karşılaştırması ayrı, pozisyon boyu sabit para riskiyle normalleştirilir. Stop çok uzaksa işlem sıklığı ve risk dağılımı raporlanır. EMA hesabı sinyal kapanışına dek olan veriyle; 1m yürütmede aynı bar stop/hedef çakışması açıkça ele alınır.

## Sonraki test için karar

1. **Önce P12a ve P12c:** pivot/CPR düzeyleri tamamen nedensel hesaplanabilir; fakat UTC gün açılışı ve CPR genişliği etkisi kriptoda ayrı doğrulanmalı. P12b düşük olay sayısı üretebilir; önce kapsam ve çakışma sayısı ölçülsün.
2. **B12 long çevirisi çözülmeden tek sistem olarak kodlanmasın.** Short baz ve iki long varyantı önceden ayrı tanımlandı. H12 yalnız mevcut girişlerde filtre/risk karşılaştırmasıdır.
3. Her aday için aynı varlık, dönem, ücret, spread/kayma, funding, 1m yürütme ve dış örneklem sözleşmesi; olay sayısı, dolmayan giriş, net R, en kötü kayıp serisi ve stratejiler arası aynı işlem çakışması raporlanmalı. Hiçbir kaynak stratejisi geçmiş örnek veya vaatle kârlı ilan edilmedi.
