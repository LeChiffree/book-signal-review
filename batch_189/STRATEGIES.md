# Kitap okuma 189 — başarısız arzın talebe dönüşü

Üç PDF'nin **400 sayfası** sayfa bazında metne çıkarılıp baştan sona tarandı; kural sayfaları ayrıca ayrıntılı okundu. **1 yeni doğrulanmamış işlem stratejisi adayı** kaydedildi. Backtest, paper test ve emir yapılmadı. Sayfalar PDF sayfasıdır.

## 1. Wayne Gorman ve Jeffrey Kennedy — Elliott Dalga Ticareti Hakkında Görsel Rehber (254 sayfa)

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Elliott Dalga Ticareti Hakkında Görsel Rehber - Wayne Gorman ve Jeffrey Kennedy (254 sayfa) - @eseckal.pdf>) · [tam metin](01_elliott_visual_guide.txt)

**Tam okuma:** S. 1–24 Elliott dalga çerçevesi/giriş; 25–80 zigzag ve flat işlem örnekleri; 81–102 üçgenler; 103–128 C dalgası; 129–158 bitiş diyagonali; 159–186 göstergeler; 187–224 opsiyon yapıları; 225–247 risk ve dalga kuralları; 248–254 Bloomberg sözlüğü/dizin. S. 16'da bitiş diyagonalinin 2–4 çizgisi kapanışla kırılırsa giriş, formasyon ekstreminde stop; s. 81'de üçgenin D ucu kırılımı ve E ucu stopu anlatılır. Ancak B/D/E uçları ile derece etiketleri canlı akışta tekil ve kesin değildir: s. 92 aynı grafikte iki geçerli sayım, s. 97 E ucunun sonradan yeniden etiketlenmesi ve s. 197 farklı yönlere bakan geçerli sayımlar açıkça belirtilir. Bu nedenle kaynak kurallarını geçmiş grafiğin sonradan çizilmiş dalgalarıyla kapalı mum sinyali gibi kaydetmedik. Üçgen kırılımı ve Fibonacci hedefleri zaten önceki aday ailelerindedir; opsiyon yayılım/straddle yapıları point-in-time dalga olayı olmadan yeni fiyat sinyali değildir. **Yeni mekanik aday: 0.**

## 2. DexterrFX — Smart Money Kavramının Kutsal Kitabı (104 sayfa)

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Smart Money Kavramının Kutsal Kitabı (104 sayfa) - @eseckal.pdf>) · [tam metin](02_smart_money_bible.txt)

**Tam okuma:** S. 1–18 SMC/piyasa yapısı; 19–34 likidite ve süpürme; 35–60 arz-talep, order block, POI; 61–68 mitigation/fiyatlandırma; 69–80 ChoCH, CI, flip, devam ve FVG girişleri; 81–89 işlem yönetimi; 90–104 günlük süreç, para yönetimi ve sözlük. ChoCH, BOS, FVG `%50` ve likidite süpürmesi tek başına önceki kayıtların varyantlarıdır. S. 73–76'daki **önceden tepki vermiş son kontrol arzının yeni dip üretememesi, sonra kırılıp yeni talep bölgesinde reddedilmesi** daha belirli bir olay dizisidir. Kaynağın kurumsal niyet anlatısı gözlenebilir veri değildir; yalnız fiyat dizisi sınanır.

### DF189A — tepki veren kontrol arzının başarısızlığı ve flip bölgesi retesti

- **Kaynak (s. 73–76):** Yükseliş *flip* dört adım: kontrol eden son arzdan ilk tepki, tepkinin yeni düşük dip üretememesi, arzın kırılması ve talep oluşturulması, yeni talepte fiyat tepkisi. S. 77 modelin HTF POI/likidite bağlamında ve devam işleminde kullanılabileceğini belirtir. Mekanik pivot, bölge, süre ve çıkış tanımları aşağıda **bizim test sözleşmemizdir**; kitap bunları rakamsal vermez.
- **Veri/bölge:** EURUSD gerçek M15 bid/ask OHLC; H1 bağlamı ayrıca etiketlenir, zorunlu filtre değildir. M15 fraktal swing `left=2,right=2` ile yalnız iki sağ bar kapandıktan sonra teyit edilir. Kapanmış M15'in en son teyitli swing dibinin altında kapanması bearish BOS'tur. Bu BOS'tan önceki son bullish M15 mumunun `low–high` aralığı *kontrol arzı* olarak sabitlenir; mum bulunmazsa olay yok. Bu OB seçimi kaynakla özdeş garanti edilmez. Yalnız ilk sonraki temas `high≥zoneLow && low≤zoneHigh` izlenir. Teması takip eden en çok 8 M15'te bölgeden en az `0.5×ATR14` aşağı tepki olmalı fakat fiyat BOS'a ait teyitli dibin altına inmemeli. ATR temas öncesi son kapanışta dondurulur. Tepki sırasındaki yeni dip yasağı, s. 73'ün ikinci adımıdır.
- **Kırılım ve sinyal:** Tepkiden sonraki en çok 8 M15'te `close>zoneHigh` kontrol arzının başarısızlığıdır. Kırılım öncesindeki son bearish M15'in `low–high` bandını *yeni talep* olarak sabitle; mum yoksa sinyal yok. Sonraki en çok 12 M15'te ilk talep teması sonrası tamamlanan M15 `close>newDemandHigh` ve `close>open` ise long; **sonraki** ilk ask kotasyonundan giriş. Stop `newDemandLow−0.1×ATR14`, hedef `2R`, en geç 24 M15 sonunda çıkış. Ters yönde, son kontrol talebinin yeni tepe üretemeyip kırılması ve yeni arz retesti simetrik short araştırma koludur. Aynı kontrol bölgesinden tek işlem; eş zamanlı çoklu adayda en eski teyitli bölge seçilir.
- **İcra/risk:** Stop uzaklığı pozitif değilse veya spread girişte `>0.25R` ise atla. Özsermayenin en çok `%0,25`i stop riski; spread, komisyon, kayma ve gece finansmanı dahil. M15 içindeki temas-kırılım sırası OHLC'den varsayılmaz: ayrık kapanmış mumlar zorunlu; aynı M15 içinde stop ve hedef görünürse tick verisi yoksa aleyhte sıra. Başarı iddiası yok.
- **Ayırıcı sınama:** Sıradan son arz üstünde kapanış + retest, herhangi bir order block retesti, ChoCH+internal BOS ve ilk tepki/yeni dip yasağı kaldırılmış kollarla karşılaştır. İşlem olay örtüşmesi, net R, rejim/yıl dış örneklem, spread duyarlılığı ve bölge tanımı hassasiyeti raporlanmalı. Özellikle aynı sinyaller önceki order block adaylarıyla çakışırsa bağımsız alfa sayılmamalı.

## 3. Steve Burns ve Holly Burns — Sakin Trader: Aklınızı Kaybetmeden Kazanın (42 sayfa)

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Sakin Trader - Aklınızı Kaybetmeden Kazanın - Steve Burns ve Holly Burns  (42 sayfa) - @eseckal.pdf>) · [tam metin](03_calm_trader.txt)

**Tam okuma:** S. 1–8 giriş ve sistem disiplini; 9–19 farkındalık/nefes; 20–30 iç konuşma, portföy ve plan; 31–42 öfke, psikolojik risk ve kapanış. S. 8, 28 ve 36'daki plan takibi, uygun pozisyon boyu ve mental yorgunluk uyarıları test sürecinin operasyonel kontrol listesine uygundur. Kitap herhangi bir piyasa, gösterge, formasyon ve kapalı mum giriş/çıkış dizisi sunmaz. **Yeni aday: 0.**

**Parti sonucu:** 3 PDF, **400 sayfa**, **1 yeni doğrulanmamış aday**. Kümülatif **567 PDF, 31.209 sayfa, 430 aday**.
