# Kitap okuma 061 — MA kesişimi, çapa mum dönüşü, 1-2 dalga devamı

**Kapsam:** Üç PDF'nin gerçekte **82 + 63 + 43 = 188 sayfası** sıralı metne çıkarıldı ve incelendi. Atıflar PDF sayfasıdır. Aşağıdaki sayısal eşikler kaynakta bulunmadığı yerlerde **bizim backtest tanımımızdır**. Backtest, paper test ve emir yapılmadı.

## 1. Clif Droke — Basitleştirilmiş Hareketli Ortalamalar

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Basitleştirilmiş Hareketli Ortalamalar - Clif Droke (82 sayfa) - @eseckal.pdf>) · [Tam metin](01_ma_droke.txt)

**Kaynak:** Tek ortalamanın üstünde fiyat ve yükselen ortalama koşulu s. 10–15'te anlatılır. Asıl iki ortalamalı reçete 30 dönem ortalamanın 60 dönem ortalamayı yukarı kesmesi, uzun ortalamanın yükselmesi ve ters koşulun satış için kullanılmasıdır (s. 25–27). Kitap trend piyasasını yatay piyasadan ayırmanın önemini ve kesişimlerin yatay piyasada tekrar eden yanlış sinyal üretebildiğini belirtir (s. 25, 70–74). Sabit 3–4 aylık döngü iddiası (s. 40–65) ayrı kanıt olmadan test ön kabulü yapılmaz.

### CD61 — SMA30/60 kesişimi ve uzun ortalama eğimi

- **Sinyal:** UTC D1 kapalı barlarında SMA30 ve SMA60; en az 120 D1 ısınma. Long: `SMA30[t−1]≤SMA60[t−1]`, `SMA30[t]>SMA60[t]`, ayrıca `SMA60[t]>SMA60[t−5]`. Short bunun simetriği, uzun ortalama düşmeli. Beş günlük eğim penceresi bizim ölçümümüzdür. Fiyatın SMA30 üzerinde/altında kapanması ayrı teyit kolu; ana kural kesişim ve eğimdir.
- **İcra ve çıkış:** Sinyal kapanışından sonraki ilk uygulanabilir 1m fiyatında giriş. Long ilk stop `min(low[t−9:t])−0,1×ATR14_D1[t]`, short simetriği. Stop yanlış tarafta veya maliyetin iki katından darsa sinyali atla. 2R hedef, karşı yönde teyitli SMA kesişimi ya da 90 D1 bar süre; ilk gerçekleşen çıkış. Stop ve hedef aynı 1m içinde görülürse stop önce. Stop, hedef ve süre bizim standardizasyonumuzdur.
- **Ayrıştırma:** Aynı kesişimi eğim filtresiz test et. Yatay piyasa uyarısını sınamak için kesişim öncesi 20 D1 Kaufman verimlilik oranı `|close[t−1]−close[t−21]| / Σ|Δclose|≥0,25` eklenen ayrı kol; eşik bizimdir, geçmiş pencere kesişim mumunu içermez. İşlem sayısı, net R, yatay/trend rejimi ve masraf duyarlılığı raporlansın. Önceki MA20 geri kazanımı MR60 ve diğer MA kesişimi adaylarıyla aynı evrende kıyaslansın.

## 2. Christopher Lee — Basitleştirilmiş Mum Kalıpları

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Basitleştirilmiş Mum Kalıpları - Christopher Lee (63 sayfa) - @eseckal.pdf>) · [Tam metin](02_candles_lee.txt)

**Kaynak:** Kitap s. 25–29'da gövdesi çevresine göre uzun bir **çapa mum** tanımlar; sonraki mumun çapa mumun açılışını öte yanda kapanışla geçmesi dönüş teyididir. Yalnız gölgeyle kırılmayı işlem saymama, tam mum kapanışını bekleme ilkesi s. 49–52 ve 60–62'de tekrar edilir. Mum büyüklüğü, takip süresi ve risk hedefi sabit sayılarla verilmediğinden aşağıdaki ölçüler deneysel tanımdır; örnek grafikler başarı oranı kanıtı değildir.

### CL61 — Çapa mum açılışının kapanışla ihlali

- **Çapa tespiti:** H1 kapalı mumlarında, gövde `|close−open|≥1,5×` önceki 20 H1 gövdesinin medyanı ve gövde/range `≥0,6`; önceki 20 H1 EMA20 eğimi çapa yönünde olsun. Sıfır range, eksik mum ve aşırı geniş spread atılır. Eşikler bizim operasyonel karşılığımızdır.
- **Tetik:** Boğa çapa mumundan sonra en fazla beş **tam kapanmış** H1 içinde ilk `close<anchor.open` short; ayı çapa için ilk `close>anchor.open` long. Çapa kendi seçimine dahil edilmez, sonraki mumlarda çapa tanımı geçmişe yeniden yazılmaz. Giriş teyit kapanışı sonrası ilk uygulanabilir 1m. Short stop `anchor.high+0,1×ATR14_H1`, long stop `anchor.low−0,1×ATR`; 2R ya da 24 H1 süre çıkışı. Stop yanlış tarafta/maliyetten dar ise atla; aynı 1m stop/hedefte stop önce.
- **Karşılaştırma:** Aynı çapa kümesinde yalnız gölge ihlaliyle sinyal veren kol ve eşik olmadan her büyük mumun açılış ihlali kolu. Önceki pin bar/engulfing dönüş adaylarıyla olay çakışması, sinyal gecikmesi ve net R kıyaslansın. Piyasa rejimi ve H1 volatilite dilimleri ayrı raporlansın.

## 3. Elliott Dalga Teorisi

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Elliott Dalga Teorisi (43 sayfa) - @eseckal.pdf>) · [Tam metin](03_elliott_theory.txt)

**Kaynak:** İtki ve düzeltme dizisi, ikinci dalganın başlangıcı aşmaması ve dördüncü dalga çakışma ilkesi s. 2–10'da. Kanal çizimi s. 26–27'de; alternatif dalga sayımları ve iptal seviyesi ihtiyacı s. 33–36'da. İşlem fikri, birinci/A dalgası ve ikinci/B geri çekilmesi bittikten sonra üçüncü/C hareketine katılmaktır (s. 41–43). Gerçek zamanda 3. dalgayı C düzeltmesinden kesin ayırmak mümkün olmadığından olay adı sonuç bilgisi içermez.

### EW61 — Teyitli 1-2 pivotundan ilk tepe kırılımı

- **Yapı:** H4 kapalı mumlarda 3 sol/3 sağ barla teyitli pivotlar. Long için `P0=low`, sonra `P1=high`, sonra `P2=higher low`; `P2>P0`, `0,3≤(P1−P2)/(P1−P0)≤0,8`. Short simetrik. P2 ancak üç sağ bar da kapanınca kullanılabilir; o tarihten önce sinyal üretme. Retrace aralığı ve pivot yöntemi bizim test tanımımızdır. P2 teyidi öncesinde P0 ihlali varsa yapı iptal.
- **Tetik ve risk:** P2 teyidinden itibaren en çok 12 H4 içinde ilk `close>P1+0,1×ATR14_H4` long (short ters). Sinyal kapanışı sonrası ilk uygulanabilir 1m giriş. Stop `P2−0,1×ATR`, short simetriği; 2R ya da 30 H4 süre çıkışı, ilk gerçekleşen. Stop yanlış tarafta/maliyetten dar ise atla; aynı 1m çakışmasında stop önce. Tetikten önce P2'nin kırılması yapı iptalidir. Sonradan oluşan 4. ve 5. dalgayı seçimde kullanma.
- **Karşılaştırma:** Aynı P1 tepe kırılımını P2/retrace filtresiz alan yalın swing breakout ve batch057 EP57'nin daha geç 5. dalga kırılımı. Teyit gecikmesi, iptal oranı, net R ve alternatif pivot penceresi duyarlılığı raporlansın. Geriye dönük ideal dalga sayımıyla kârlılık iddiası kurulmasın.

## Ortak test sözleşmesi

CD61, CL61 ve EW61 araştırma adaylarıdır. Tüm kollarda sinyal yalnız kapanmış bar ve o ana dek teyitli pivotla üretilecek; giriş bir sonraki uygulanabilir 1m dolum, ücret, spread, kayma, perpetual funding, eksik veri ve çakışan pozisyon kurallarıyla ölçülecek. Zaman sıralı ayrılmış doğrulama, işlem sayısı, net R, maksimum düşüş ve yalın taban çizgileri sonuç değerlendirmesi için zorunludur. Kitapların örnekleri beklenen getiri tahmini değildir.
