# Kitap okuma 040 — teyitli seviye süpürmesi ve yapı değişimi

**Kapsam:** 34 + 24 + 18 = **76 PDF sayfası**. Tam sayfa sıralı metinler kaydedildi; metne sığmayan King s. 27/30, Menda s. 14/21 ve WorldBank s. 9 grafikleri görsel incelendi. Atıflar PDF sayfasıdır. Kriptoya uyarlanmış tüm rakamsal eşikler, kaynakta açıkça verilmedikçe **bizim deney hipotezimizdir**. Backtest, paper test ve emir yapılmadı.

## 1. James Jecool King — Arz ve Talep, Saf Likidite Konsepti, BOS ve CHOCH

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 18/Baskı 18/Arz ve Talep - Saf Likidite Konsepti, BOS ve CHOCH - James Jecool King (34 sayfa) - @eseckal.pdf>) · [Tam metin](01_supply_demand_liquidity.txt) · [Bölge s. 27](king_p27.png) · [CHOCH s. 30](king_p30.png)

**Kaynak:** Trend ve güçlü/yakalanması beklenen swing ayrımı önceki tepe/dibin aşılmasıyla anlatılır (s. 5–10, 25). Aralığın orta noktası 0,5; yükselişte alt “indirim” bölgesinden alış, düşüşte üst “prim” bölgesinden satış önerilir (s. 14–17). Arz/talep veya “emir bloğu” büyük hareket öncesindeki son karşı yönlü mum/seriyle çizilir (s. 13–14, 21–22). Çift tepe/dip civarında varsayılan duraklardan ve HTF bölgede CHOCH dönüşünden söz eder (s. 23–27). S. 30 şeması önceki karşı swingin kırılmasıyla karakter değişimini resmeder. HTF BOS/CHOCH için gövde **kapanışını**, alt zaman diliminde fitilleri dikkate alır (s. 34). Kaynak pivot onayını, bölge genişliğini, kırılım tamponunu ve işlemin çıkışını kesin tanımlamaz. “Banka emri” grafikten doğrudan gözlenemez.

### K40 — Önceden belirli HTF bölgesinde kapalı mum CHOCH filtresi

- **Bizim H4/D1 kurgu:** D1'de son 60 **tam kapanmış** mumun `U=max(high)`, `L=min(low)`, orta `M=(U+L)/2`; long için bölgeye dokunma anındaki H4 kapanışı `<=M`, short için `>=M` olsun. H4 pivotu yalnız 3-sol/3-sağ tamamlanmış H4 barla teyit edilir. D1 `L±0.2 ATR14_D1` talep ve `U±0.2 ATR` arz bölgeleri bizim basit yaklaşımımızdır; kaynağın öznel “son karşı mum” bölgeleriyle eşdeğer değildir.
- **Olay/giriş:** Long için fiyat önceden bilinen alt bölgeye dokunduktan sonra, daha önce teyitli en son H4 **karşı swing high** üstünde ilk H4 **gövde kapanışı** `close>pivot_high+0.1 ATR14_H4`; short simetrik. Bu CHOCH adayıdır; kırılan pivot olaydan önce teyit edilmiş olmalı. Kapanış sonrası ilk uygulanabilir 1m giriş, stop olaydan önceki teyitli pivot low `−0.1 ATR`, 2R hedef veya 20 H4 bar zaman çıkışı. Stop doğru tarafta değilse veya toplam maliyetin 2 katından darsa geçersiz. Pencere, pivot, tampon ve risk/çıkış **bizim** test sözleşmemizdir.
- **Eşdeğerlik:** Önceki BOS/CHOCH, seviye kırılımı ve bant dönüş aileleriyle aynı pivot/olayları eşleştir; “likidite avı” sebebi kanıtlanmış sayılmaz. Kaynağın emir bloğu kuralı nesnel olmadığı için ana sinyale sessizce eklenmez.

## 2. Elad Menda — Gelişmiş Likidite Tekniği

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Gelişmiş Likidite Tekniği - Elad Menda (24 sayfa) - @eseckal.pdf>) · [Tam metin](02_advanced_liquidity.txt) · [İki senaryo s. 14](menda_p14.png) · [Örnek s. 21](menda_p21.png)

**Kaynak:** BSL/SSL terimleri önceki swing high/low ile destek/direnç ötesindeki varsayılan stop kümelerini anlatır (s. 3–8). Swingin 0,5 orta çizgisine göre “prim/indirim” konumu yorumlanır (s. 9–10). Yazar önce bir taraftaki düzeyin alınmasını bekler, sonra **karşı tarafta hedef düzey varsa** ilk FVG'yi arar (s. 13–15). S. 14/21 görsellerinde kademeli yaklaşan süpürme sonrası dönüş senaryosu; s. 22'de bir anda oluşan süpürmeden sonra dönüş beklememe örneği var. Hedefteki bekleyen emirler ve kurumların niyeti gözlenmiş veri değildir. FVG'nin kesin mum kuralı, “yavaş” yaklaşım eşiği ve stop verilmez.

### M40 — Kademeli yaklaşım sonrası swing süpürmesi ve FVG retesti

- **Bizim H4 olay:** Son 80 tamamlanmış H4 içinde 3-sol/3-sağ teyitli pivot low `S` ve pivot high `R` önceden bilinsin. Long için son dört H4 kapanışının en az üçü aşağı yönde fakat her barın `|close−open|<=1.2 ATR14_H4`; sonra `low[t]<S−0.1 ATR`, `close[t]>S` **kapalı mum süpürmesi**. Short için R simetrik. Bu yavaşlık ve süpürme tamponları **bizim** nesnelleştirmemiz; kaynağın kuralları değildir. Karşı hedef R long için, S short için sinyal anında mevcut ve girişten hedefe net ödül en az 2R olmalı.
- **FVG varyantı:** Süpürmeden sonraki üç tamamlanmış H4 mumda long için `low[i]>high[i−2]` olursa aradaki boşluk `[high[i−2],low[i]]` ancak `i` kapanışında oluşur; short simetrik. FVG'nin ilk geri testinde H4 kapanışı boşluk içinde/üstünde olup tekrar yönlü tarafta kalırsa sonraki ilk 1m giriş. Stop long süpürme dibi `−0.1 ATR`, hedef önceden bilinen R; 20 H4 bar zaman çıkışı. FVG yoksa sinyal yok; süpürme mumunda FVG'yi gelecekte varmış gibi kullanma. Bu FVG tanımı ve retest icrası bizim varyantımızdır.
- **Karşılaştırma:** Aynı teyitli pivot süpürmelerinde “kademeli” filtreli/filtresiz, FVG retestli/doğrudan giriş. Kaynaktaki her “stop avı” iddiasını gerçekleşen emir defteri olayı gibi etiketleme; fiyat OHLC'si bunu kanıtlamaz. Önceki false-break ve FVG kayıtlarıyla yinelenme kontrolü.

## 3. Trade with WorldBank — Likidite

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 7/Baskı 7/Likidite - Trade with WorldBank (18 sayfa) - @eseckal.pdf>) · [Tam metin](03_liquidity_worldbank.txt) · [Asya aralığı s. 9](worldbank_p9.png)

**Kaynak:** Önceden görülen destek/direnç ötesindeki süpürme ve arkasından karşı bölgeye hareket fikri (s. 1–7). Asya seansı aralığının tepe/dibinin alınması; “**menzil yok, ticaret yok**”, M5/M15 emir bloğu arama (s. 8–10). Emir bloğu aralığın dışındaysa o tarafa önce hareket edileceği iddia edilir (s. 13–14); bu ancak ileri testle sınanabilir, kesin yön bilgisi değildir. Kaynak forex için 5/10 pip stop söyler ve aynı sayfalarda farklı kullanım bağlamı verir (s. 3–4, 10–11, 15); pip stop kriptoya taşınmaz. Emir bloğunun kesin oluşum ve geçersizlik algoritması verilmez. S. 9 şekli Asya kutusunun altına taşma ve geri hareket örneğidir. Kitabın son iki sayfası pazarlama/sonuç görselleri, doğrulanmış performans verisi değil.

### W40 — Sabit saatli aralık süpürmesi, oturum varsayımını ayrı test et

- **Bizim intraday tanım:** Kriptoda gerçek Asya açılışı olmadığı için yalnız **önceden sabitlenmiş** UTC 00:00–08:00 aralığını araştırma kolu seç; aynı günün bu saatleri bittikten sonra bilinen M15 `U,L`. Önceki 14 günün aynı 8 saatlik aralık genişliği medyanına göre `0.5<=W/median(W14)<=1.5` ve aralık boyunca en az 4 tam M15 mum olsun; bunlar bizim “menzil” koşullarımızdır. İkinci kol UTC 02:00–10:00 gibi başka sabit saatlerle hassasiyet ölçer; iyi görünen saati sonradan seçip geçmişe uygulama yasak.
- **Olay/giriş:** 08:00–20:00 UTC arasında ilk M15 `low<L−0.1 ATR14_M15` fakat `close>L` long süpürmesi; üst taraf short simetrik. M15 kapanışından sonraki ilk uygulanabilir 1m giriş, stop süpürme ekstremumu `−/+0.1 ATR`, hedef karşı sınır `U/L` yalnız net ödül/risk ≥2 ise; aynı gün 20:00 UTC'de çık. Saatler, stop tamponu, teyit ve hedef risk filtresi bizim kurallarımızdır. Emir bloğu belirsizliğinden dolayı baz adaya eklenmedi.
- **Sınır:** Bu forex seans fikrinin 7/24 kripto için çalışacağı varsayılamaz; ilk testte yalnız karşılaştırmalı saat filtresi olarak değerlendirilir. Önceki Asya kutusu ve likidite süpürmesi sinyalleriyle olay eşdeğerliği kontrol edilir.

## Test sırası

Önce **M40**'ın doğrudan süpürme ve FVG retest kolları, ardından **K40** CHOCH filtre katkısı; **W40** kripto seans transferi nedeniyle düşük öncelikli. Her testte point-in-time evren, kapanmış mumdan sonra uygulanabilir fiyat, gerçek borsa hacmi/emir defteri varsa ayrı veri kaynağı, ücret/spread/kayma/funding, stop-hedef aynı bar sırası ve zaman sıralı dış örneklem gerekir. Grafikler kârlılık kanıtı değildir.
