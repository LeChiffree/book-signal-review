# Kitap okuma 129 — order block içindeki ikinci destek sınaması

**Kapsam:** Üç ayrı PDF'nin **14 + 12 + 18 = 44 sayfası** baştan sona okundu. Atıflar PDF sayfasıdır. Backtest, paper test ve emir yapılmadı. Şekilli son PDF'nin yalnız başlık taşıyan s. 13–18 sayfaları görsel olarak da incelendi.

## 1. Düşük Zaman Dilimlerinde Order Block Tespiti

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 6/Baskı 6/Düşük Zaman Dilimlerinde Order Block Tespiti (14 sayfa) - @eseckal.pdf>) · [Tam metin](01_low_tf_order_block.txt)

**Tam okuma:** S. 1–2 H1 kırılım öncesi ters mum bloğunu M15'te daraltma; s. 3–7 11→6 pip ve 17,6→6 pip seçilmiş alış örnekleri, M5/M1 BOS ile ilave teyit; s. 8–10 ikinci alış örneği; s. 11–14 satış örneği ve daha küçük blok. Giriş bölgesini sonradan kazanan muma daraltmak görünüm yanlılığı yaratır. Yalnız kazanan örneklerde RR'yi büyütmek beklenen getiriyi artırdığını göstermez; kaçan limit emirleri ve daha sık stopları saymak gerekir. H1 bloğu içindeki M15 alt bölge, stop ve dolum karşılaştırması [JK58](../batch_058/STRATEGIES.md) ile aynı test ailesidir. **Yeni bağımsız aday yok.**

## 2. Lucius — ICT Blok Tipleri

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 6/Baskı 6/ICT Blok Tipleri (Orijinal) (12 sayfa) - @eseckal.pdf>) · [Tam metin](02_ict_block_types.txt)

**Tam okuma:** S. 1 kapak; s. 2 klasik order block, gövdenin orta eşiği, kırılım/geri test; s. 3 prim–iskonto; s. 4 mitigation; s. 5 breaker; s. 6 rejection; s. 7–8 reclaimed; s. 9–10 **propulsion block**un eski blokla ilk temas eden mumdan türeyip sonraki geri testte %50 düzeyinin korunması; s. 11–12 seans/haber boşluğu “vacuum block”. Breaker, rejection, OB ve gap aileleri kütükte mevcut. Kurumsal “sponsorluk”, sıkışmış pozisyonlar ve gelecekteki stop emirleri grafikten doğrudan gözlenmez. Kaynak s. 2 gövde orta noktasını önerir; bunu fitil aralığı orta noktasıyla karıştırmayacağız.

### LU129A — İlk order block temasından doğan propulsion mumunun %50 yeniden testi

- **Kaynak (PDF s. 2, 9–10; ayrıca Lumi Traders s. 12, 18):** Fiyat eski boğa/ayı order block'a dokunduktan sonra yeni “propulsion” mumu destek/direnç rolü alabilir. Bu mumun gövde orta eşiği sonraki geri çekilmede korunuyorsa devam beklenir. Lumi Traders s. 18'in çizimi nihayetinde fiyatın ters döndüğü bir örnektir; %50 korunması **kalıcı trend garantisi değildir**.
- **Kapalı mum sözleşmesi:** EURUSD/GBPUSD, H1 ana blok, M15 propulsion/sinyal, M1 yürütme. H1 boğa bloğu: teyitli (`k=2` sağ bar) önceki H1 pivot tepesinin üstünde kapanan ilk H1 BOS'tan önceki en yakın düşüş mumu; bu mumun `[low,high]` aralığı dondurulur ve yalnız BOS kapanışından sonra kullanılabilir. En çok 12 H1 içinde ilk M15 `low` bu aralığa değsin; aynı M15 bar `close>open` ve `close` blok orta düzeyinin üstünde olsun. Bu ilk temas/tepki barı `P` olarak dondurulur. Ardından en çok dört M15 içinde bir kapanış `high[P]` üstünde gerçekleşsin; ancak o kapanıştan sonra `P`nin gövde aralığı `[open[P],close[P]]` yeni propulsion alanı olur, orta eşik `M=(open[P]+close[P])/2`. Sonraki en çok sekiz M15 barda ilk kez `low<=close[P]`, `low>=M` ve `close>close[P]` ise ikinci temas teyidiyle long; M15 barı kapanmadan sinyal yok. Short bütün fiyat ilişkilerinin simetriği. `k=2`, 12/4/8 bar pencereleri, mum renk/kapanış koşulları ve eski blok tanımı **bizim mekanik deney seçimimizdir**; kaynak bunları sayıyla vermez. İlk temas barını sonraki kazanan harekete bakıp değiştirmek yasaktır.
- **Yürütme/çıkış:** Sinyal sonrası ilk uygulanabilir M1 ask/bid'den giriş. Stop `P` ekstremi ile eski H1 blok ekstreminden girişe **daha yakın** olanın 2 pip dışı; ancak stop girişin yanlış tarafındaysa ya da maliyetin iki katından darsa pas. Hedef `2R`, en geç 24 H1 bar sonra çıkış; ilk risk özsermayenin `%0,5`i, tek açık pozisyon/çift. Gerçek spread, komisyon, kayma, boşluk ve aynı M1 bar stop/hedef çakışmasında kötümser sıra. Eski H1 blok ilk temasında doğrudan giriş ve propulsion `%50` koşulsuz ikinci temas kollarıyla aynı olay, tarih ve maliyette net R, dolum, stop ve işlem sayısı karşılaştırılır. Özellikle [JK58](../batch_058/STRATEGIES.md) M15 daraltma kolundan ek değer ayrıştırılır.

## 3. Lumi Traders — ICT Block Örnekleri

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 6/Baskı 6/ICT Block Örnekleri (18 sayfa) - @eseckal.pdf>) · [Tam metin](03_ict_block_examples.txt) · [Görsel s. 13–18](ict_examples_contact.png)

**Tam okuma:** S. 1 kapak; s. 2–3 breaker ve stop avı sonrası yapı kırılımı; s. 4–7 klasik OB ve %50 eşik; s. 8 reclaimed; s. 9–10 mitigation ve boşluğun %50 doldurulması; s. 11 rejection; s. 12 propulsion; s. 13–18 her türün çizilmiş örneği. Propulsion görseli s. 18, yukarı giden ilk tepkinin daha sonra aşağı dönebildiğini gösterir. Mitigation içindeki “void” fiyat aralığı/seans gap'i olarak kesin tanımlanmadığı için burada yeni bir mekanik aday sayılmadı; ikinci kez uydurma bir blok sınıfı oluşturulmadı. Kitabın ayırt edici %50 propulsion koşulu **LU129A'ya ikinci kaynak** olarak eklendi. Kalan kalıplar önceki OB/süpürme/retest aileleriyle örtüşür.

## Sonuç

**1 yeni araştırma adayı:** LU129A. Bu aday bir performans iddiası değildir; sonraki aşamada maliyetli ve zaman sıralı backtest gerekir.
