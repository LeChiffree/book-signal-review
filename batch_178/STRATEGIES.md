# Kitap okuma 178 — arz/talep bölgesindeki yutan mumdan ikinci giriş

Üç daha önce tamamlanmamış PDF'nin **540 sayfası** baştan sona tarandı. **Bir yeni doğrulanmamış strateji adayı** var. Kitap örnekleri backtest/paper test değildir; bunlar daha sonra yapılacak.

## 1. Mustafa Karahan — Price Action (236 PDF sayfası)

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Price Action - Mustafa Karahan (236 sayfa) - @eseckal.pdf>) · [tam metin](01_price_action_karahan.txt)

**Tam okuma:** PDF s. 1–3 içindekiler; 4–14 arz/talep bölgesi ve yutan mum; 15–24 pin ve seans; 25–33 konsolidasyon; 34–49 pin, trend ve stop; 50–60 bölge tipleri; 61–71 kaçırılan ilk girişe ikinci fırsat; 72–96 bölge, başarısızlık işaretleri ve seviye; 97–113 grafik kalıpları; 114–134 fiyat okuma ve bölge boyutu; 135–154 yutan/pin; 155–181 trend ve arz/talep; 182–203 bölge kuralları ve destek/direnç; 204–236 MA, sığ geri çekilme ve çeşitli uygulamalar. Metindeki “bankalar bunu yaptı” anlatımı işlem akışı kanıtı değildir. Çoğu konu önceki [arz/talep](../batch_005/STRATEGIES.md), [bölge + mum](../batch_121/STRATEGIES.md), mum ve kırılım adaylarıyla örtüşür.

### MK178A — İlk bölge temasındaki yutan mumun yarattığı ikinci retest

- **Kaynak ayrımı:** PDF s. 61–67, ilk H1 arz/talep bölgesine küçük tepki verilirse alt zaman diliminde yeni bölge oluşabileceğini ve onun ilk dönüşünün ikinci giriş olduğunu anlatır. S. 68–70 farklı, daha açık sürüm verir: ilk bölge temasından sonra **H1 yutan mum** bölgeden çıkar; bu mumun oluşturduğu bölgenin dış kenarına ilk dönüşe **bekleyen emir** konur, yeni pin/yutan teyidi beklenmez. Aday bu ikinci sürümdür. Yazar s. 70'te ikinci bölgeyi alt zaman dilimine inerek daraltmamayı belirtir. “İkinci giriş” başarı garantisi değildir; ilk hareketten sonra çoğu olayda tekrar temas gelmeyebilir.
- **Veri ve ilk bölge:** Likit FX çiftlerinde point-in-time H1 OHLC + M1 bid/ask. Önceden tamamlanmış H1 mumlarından mekanik bölge: en çok 3 ardışık küçük gövdeli mum (`body/range≤0,35`, `range≤1,2×ATR14_H1`) sonrası aynı yönde güçlü çıkış mumu (`body≥0,8×ATR`, `close` aralığın yön ucundaki %25'te). Talep bölgesi küçük mum kümesinin `[min(low),max(body_top)]`, arz simetri. Bölge ancak çıkış mumu **kapandığında** bilinir; 20 H1 bar içinde ilk temas izlenir. Bu eşikler kaynaktaki görsel “taban” ve “güçlü çıkış” için bizim vekilimizdir; [parti 005](../batch_005/STRATEGIES.md) bölge olaylarıyla çakışma kimliği tutulur.
- **İkinci bölge:** İlk temas H1'inde long için `low≤zone_high`, ardından `close>zone_high` ve boğa yutan mum: `close>open`, gerçek gövde bir önceki H1 gerçek gövdesini kapsar. Short simetri. Bu kapanıştan önce ikinci giriş seviyesi kurulamaz. Long ikinci bölge, yutan mumun `open` ile `low` arası; short `open` ile `high` arası olarak dondurulur; kaynak sınırları nicel vermediği için bu **bizim** nesnel mum kökeni vekilidir. Yutan mumun kendisi ilk bölgeden en az `0,5×ATR` uzaklaşmış olsun; sonraki 8 kapanmış H1 içinde ikinci bölgenin dış kenarına **ilk** dönüş beklenir. İlk bölge dibi/tepesi aşılırsa bekleyen emir iptal. Bir ana bölgeye bir ikinci şans olayı; sonradan en iyi retest seçilmez.
- **Emir/çıkış:** Long dış kenar `open_engulf` üzerinde alış limit, short simetri; limit emri ancak yutan mum kapandıktan sonra açılır. M1 ask/bid ile fill; limit seviye teması otomatik dolum kabul edilmez, gap/queue/slippage kaydedilir. Long stop `min(zone_low, engulf_low)−0,1×ATR14_H1`, short üst simetri. Stop yanlış tarafta ya da spreadin iki katından dar ise işlem yok. Risk özkaynağın `%0,25`i; hedef 2R veya 24 H1 sonra çıkış, hangisi önce. M1 içinde stop/hedef sırası belirsizse stop önce; spread, komisyon ve rollover dahil.
- **Kıyas:** Aynı ilk bölge/ilk temas olaylarında (i) ilk temas limit veya kapanış teyidi, (ii) yutan mum kapanışı sonrası doğrudan giriş, (iii) ikinci bölge ilk retesti. **Retest hiç gelmeyenler** olay tablosunda ayrı sonuç olarak kalır. Net R, dolum oranı, fırsat maliyeti, örneklem büyüklüğü, walk-forward dış örneklem ve çift/seans ayrımı raporlanır. İkinci bölgenin sadece ilk bölgenin tekrar testi olup olmadığı aynı fiyat aralığı örtüşmesiyle ölçülür.

## 2. Frank Marshall — Trader: 93 Trading Dersi (96 PDF sayfası)

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Trader - 93 Trading Dersi - Frank Marshall (96 sayfa) - @eseckal.pdf>) · [tam metin](02_trading_lessons_marshall.txt)

**Tam okuma:** PDF s. 1–20 kaset okuma, beklenti ve çalışma; 21–40 trader örnekleri, seleksiyon ve zamanlama; 41–60 stop, hacim, güçlü hareket ve piyasa döngüsü; 61–80 grafik ve trend; 81–96 yeniden giriş, psikoloji ve sonuç. Bu eser kısa Wyckoff alıntıları ve yorumlardan oluşur. S. 53–56 göreli hacim, s. 70 lider hisselerin ortalama yönü ve s. 83–85 yeni alanda ivme sonrası hafif hacimli geri çekilme önemli araştırma bağlamıdır. Ancak giriş/çıkış için tam nesnel olay sırası veya yeni eşik yok; önceki hacimli kırılım, trend geri çekilmesi, hacim ve pozisyon yönetimi adaylarıyla örtüşür. **Yeni bağımsız aday: 0.** 93 ders, 93 ayrı işlem stratejisi değildir.

## 3. Forex Okulu (208 PDF sayfası)

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Forex Okulu (208 sayfa) - @eseckal.pdf>) · [tam metin](03_forex_okulu.txt)

**Tam okuma:** PDF s. 1–51 FX temelleri/seans/emir; 52–76 destek, trend çizgisi ve mumlar; 77–111 MA, BB, MACD, SAR, stochastic, RSI ve Ichimoku; 112–151 grafik formasyonları ve pivot; 152–178 Elliott/Fibonacci/harmonik; 179–208 ayrışma, trend/yatay piyasa ve geri çekilme. Bu bir başlangıç derlemesidir. S. 140–150 pivot destek/kırılım, s. 180–194 düzenli/gizli ayrışma, s. 195–206 trendde BB ve geri çekilme örnekleri önceki aday aileleriyle örtüşür. Görsel örnekler kesin pivot/çizgi teyidi, emir ömrü ve bağımsız stop/hedef sözleşmesi vermez. **Yeni bağımsız aday: 0.** Metindeki eski piyasa büyüklüğü ve başarı genellemeleri güncel veri olarak kullanılmaz.

**Parti sonucu:** 3 PDF, **540 sayfa**, **1 yeni doğrulanmamış aday**. Kümülatif **534 tamamlanmış ayrı PDF, 25.954 sayfa, 413 strateji adayı**.
