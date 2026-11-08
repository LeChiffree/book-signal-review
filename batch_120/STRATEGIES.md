# Kitap okuma 120 — üç gövdeli yutma ve trend çizgisi boşluğu

**Kapsam:** Üç ayrı PDF'nin **144 + 25 + 43 = 212 sayfası** baştan sona tarandı. Sayfa atıfları PDF sayfasıdır. Aşağıdaki kurallar yalnız ileriye dönük araştırma sözleşmesidir; backtest, paper test veya emir yapılmadı.

## 1. Svetlin Minev — Açıklamalı Price Action Tekniği

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 2/Baskı 2/Açıklamalı Price Action Tekniği - Svetlin Minev (144 sayfa) - @eseckal.pdf>) · [Tam metin](01_price_action_minev.txt)

**Tam okuma:** S. 1–33 salınım, destek/direnç, EMA, pivot ve Fibonacci; s. 34–63 EMA geri çekilmesi, sahte kırılım ve klasik formasyonlar; s. 64–77 ATR ve inside/NR4/NR7 barları; s. 78–100 korelasyon, mevsimsellik ve vadeli işlem takvimleri; s. 101–109 mum ve fiyat hareketi; s. 110–123 kotasyon/tik okuma ve stop süpürme; s. 124–135 Joe Ross 1-2-3, Ross Hook ve Trader's Trick Entry; s. 136–144 Al Brooks H1–H4/L1–L4, başarısızlığın başarısızlığı, çift dip/tepe bayrağı. Bunlar arşivdeki pivot, seviye reddi, kırılım/retest, mum, MA ve inside-bar aileleriyle geniş ölçüde örtüşür. Özellikle s. 110–123'teki tik büyüklüğünden büyük katılımcı çıkarımı **OHLCV verisiyle doğrulanamaz**; merkezi olmayan FX kotasyonlarından küresel emir büyüklüğü de çıkarılamaz. S. 88–90'daki mevsimsel takvimler seçilmiş tarihsel vadeli işlem örnekleri; aynı vade ve sürekli seri/roll bilgisi olmadan mevcut kripto hattına aktarılmadı. **Yeni bağımsız aday sayılmadı.** Ross TTE s. 130–134 ve iki aşamalı başarısızlık s. 138–142 daha sonra mevcut kırılım stratejileri için ablation olarak incelenebilir.

## 2. Vladimir Ribakov — Mumların Dili

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 2/Baskı 2/Mumların Dili - Vladimir Ribakov (25 sayfa) - @eseckal.pdf>) · [Tam metin](02_candles_ribakov.txt)

**Tam okuma:** S. 1–6 üç önceki mumun **gövdelerini** yutan güncel mum ve kısa karşı düzeltmeden sonra ana yönde giriş; s. 7–12 trend sonunda marubozu; s. 13–18 eşit üst/alt gölge; s. 19–25 tek uzun gölgeli, diğer gölgesi sıfır olan “hatchet” ve stop/hedef. Marubozu ve hatchet standart marubozu/çekiç ailesiyle örtüşür; eşit gölge için “trend veya düzeltme sonu” geriye dönük ve belirsizdir. Metindeki %80, %95, %99 ve “hemen her zaman” ifadeleri örneklem/masraf kaydı olmadan başarı kanıtı değildir.

### RB120A — Üç önceki gövdeyi yutan mumun devamı

- **Kaynak (s. 1–6):** Sinyal mumunun gövdesi önceki üç mumun gövdelerini kapsar; kısa karşı hareket sonrası sinyal yönünde işlem fikri. Kaynak gölge değil gövde karşılaştırır, ancak “kısa düzeltme”yi ölçmez.
- **Kapalı mum sözleşmesi:** Likit, geçmişteki veriyle seçilmiş spot kripto çiftlerinde H4. Boğa için `C[t]>O[t]`, `min(O[t],C[t]) <= min(O,C)[t-1:t-3]` ve `max(O[t],C[t]) >= max(O,C)[t-1:t-3]`; ayrıca sinyal gövdesi `>=0.8 ATR14[t-1]`. Ayı için ters renk ve aynı kapsama. Eşik `0.8 ATR`, geçmişten evren seçimi ve H4 **bizim** varsayımlarımız. Sinyal kapanınca en çok 3 H4 boyunca sinyal gövdesinin orta noktasına limit emir; boğa için yalnız sinyal mumunun dibi kırılmadan, ayı için tepe aşılmadan dolum. Dolmazsa iptal. Stop sinyal ekstremi dışına `0.1 ATR14[t-1]`; hedef 2R veya 12 H4 sonunda kapanış. Tek aktif pozisyon/çift, işlem başına özsermayenin %0,5'i risk. Limit gerçekleşmesini gerçek sonraki mum sırasıyla, belirsizse kötümser; ücret, spread, kayma ve varsa fonlama ile hesapla.
- **Ayrışma:** [Standart tek mum gövde yutması](../batch_032/STRATEGIES.md) ve aynı boyda fakat üç gövdeyi kapsamayan büyük mumlarla aynı evren/dönemde kıyasla. Böylece katkının genel momentumdan mı, *üç gövdenin kapsamından* mı geldiği görülür. Başarılı olduğu varsayılmaz.

## 3. Jeffrey Kennedy — Trend Çizgileri

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 2/Baskı 2/Trend Çizgileri (43 sayfa) - @eseckal.pdf>) · [Tam metin](03_trend_lines.txt)

**Tam okuma:** S. 1–19 trend çizgisi, kanal, paralel çizgi, üçüncü yelpaze kırılımı ve yalnız kapanış yerine barın **tamamının** çizginin karşısında kalması teyidi; s. 20–26 çizginin ötesindeki fiyat boşluğu, tek/çift yeniden test; s. 27–29 Elliott geçici/son kanal; s. 30–40 Kennedy baz, hızlanma, yavaşlama ve sonlandırma kanalları; s. 41–43 soru-cevap ve dalga bağlamı. Çizgi uçlarını olaydan sonra seçmek görünüm yanlılığı yaratır. Dalga etiketleri ve “önemli uç” seçimleri kaynakta algoritmik değildir. Tek/çift retest ve basit çizgi kırılımı arşivde mevcut; aşağıdaki adayın ayırt edici özelliği **çizginin ötesinde tamamen ayrık bar** olmasıdır.

### JK120A — Trend çizgisinden ayrık bar sonrası devam

- **Kaynak (s. 13–15, 20–23):** Geçerli kırılım için sadece kapanış yerine barın karşı tarafta kalması; çizginin üstünde/altında boşluk varsa o barın high/low'u kırılınca giriş, stop boşluk öncesi barın karşı ekstreminde.
- **Kapalı mum sözleşmesi:** Seanslı ve gerçek gap barındıran likit vadeli işlem veya hisse evreni, günlük bar. Her `t` anında yalnız `t-2`ye dek **teyit edilmiş** iki salınım tepesi/dibi (`k=2` sağ bar gecikmesi) ile eğimli çizgi kur; çizgiyi `t`ye uzatıp sinyal anında dondur. Boğa için son iki teyitli tepe üzerinden düşen direnç çizgisi ve `low[t] > line[t]`, ayrıca `low[t] > max(high[t-1], line[t])`; ayı için son iki teyitli dip üzerinden yükselen destek ve `high[t] < min(low[t-1], line[t])`. Bu sıkı `gap` tanımı, `k=2` ve çizgi seçim sırası **bizim** objektifleştirmemizdir. Sinyal kapanınca ertesi seans bir günlük stop giriş: boğa `high[t]+1 tick`, ayı `low[t]-1 tick`; dolmazsa iptal. Başlangıç stopu boğa için `low[t-1]-1 tick`, ayı için `high[t-1]+1 tick`; 2R veya 10 işlem günü sonunda çıkış. Risk %0,5/işlem, tek açık işlem/enstrüman. Gap atlayarak açılış, bid/ask, ücret, kayma ve aynı bar stop/hedef sırası gerçekçi modellenir.
- **Ayrışma:** Aynı çizgide yalnız kapanışla kırılım, tüm bar karşı tarafta fakat **gerçek gap yok** ve [önceki gap adayları](../batch_053/STRATEGIES.md) karşılaştırılır. Kriptoda kesintisiz 7/24 barların sınır boşluğu, seanslı piyasanın gerçek gap'iyle eşit kabul edilmez. Çizgi aşırı uyumunu önlemek için başlangıç barından sonra uçlar geriye dönük değiştirilmez.

## Sonuç

**2 yeni strateji adayı:** RB120A ve JK120A. Bunlar araştırma hipotezidir; getirileri ve uygulanabilirlikleri henüz ölçülmedi.
