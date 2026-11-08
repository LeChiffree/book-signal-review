# Kitap okuma 010 — Leandro swing, Gann fanı, Forex scalp

**Kapsam:** Üç PDF'nin **67 + 15 + 28 = 110 PDF sayfası** sayfa bazında işlendi. Leandro kaynağı ağırlıkla görsel slayttır; kritik s. 20–22, 29, 39, 47, 49 ve 56 ayrıca görüntü olarak incelendi. Sayfa numaraları PDF sayfasıdır. Kaynak kurallarından farklı sayısal uyarlamalar ayrıca işaretlendi. Hiçbir kitap kripto için doğrulanmış üstünlük kanıtı sunmuyor; bu partide backtest/paper emir yok.

## 1. Swing Trading Leandro Yöntemi

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 9/Baskı 9/Swing Trading Leandro Yöntemi (67 sayfa) - @eseckal.pdf>)

Günlük grafikte yaklaşık 2–10 günlük swing hedefi (s. 5), trend için yükselen tepe/dip ve MA21/50/200 bağlamı (s. 19), önce bir fiyat veya süre geri çekilmesi bekleme (s. 25–28) anlatılıyor. S. 29–48 “kurulum 1” en az 10 barlık sıkışma, hacimli güçlü kırılım, sonra daha düşük hacimli geri çekilme/retest; s. 49–55 “kurulum 2” düzeltmede destek ve 60m giriş; s. 56–59 “kurulum 3” banda göre aşırı uzamış ters mum. İşlem hacmi ve *işlem adedi* s. 30–33'te birlikte anılıyor; yalnız OHLCV verisinde işlem adedi yoksa hacim/adet ayrışması sınanamaz. S. 62–64 tarihsel Brezilya hisse listesi; güncel kripto evreni değildir. Pozisyon boyutuna dair s. 66 örneği yazılır ama gelecekte alpha kanıtı sayılmaz.

### L10a — En az 10 bar sıkışma sonrası güçlü ve hacimli kapanış kırılımı

- **Kaynak:** En az 10 bar yatay bölüm, Bollinger bandının açılması, yükselen büyük trend, ortalamanın üstünde mum aralığı ve hacim, direncin üzerinde kapanış (s. 29 görseli ve s. 30–35). Kitap “güç çubuğu” ve ortalama için tam eşik vermiyor. S. 34–38 aşırı uzama ve stop uzaklığına göre eleme/pozisyon azaltma içerir.
- **Bizim günlük olay:** `t-10...t-1` kapanmış 10 barın `max(high)-min(low) <= 2 ATR14[t-1]` ve `BBwidth20[t-1]` önceki 90 günlük dağılımın alt %30'unda; `SMA21[t-1]>SMA50[t-1]`, ikisi de yükseliyor. Direnç `R=max(high[t-10:t-1])` t-1'de dondurulur. t kapanışı `close[t]>R+0.1 ATR14[t-1]`, `range[t]>1.2 ADR20[t-1]`, `volume[t]>1.5 median(volume[t-20:t-1])`, `BBwidth20[t]>BBwidth20[t-1]`. Short simetri. **10 bar kaynak; 2 ATR, %30, 0.1, 1.2, 1.5 ve 90 gün bizim eşiklerimiz.** Kaynaktaki MA21 mesafe/volatilite oranını `abs(close-SMA21)/ATR14` sürekli değişken olarak kaydet; sınırlayıcı eşik ayrı ablation.
- **Yürütme/çıkış:** t kapanışından sonraki ilk 1m; stop sıkışma alt sınırı veya kırılım mumu dibi, iki sürüm. 1R/2R ve 3/7/10 gün çıkışı; hacim, BB genişlemesi, MA trendinin marjinal katkısı yalın 10 bar kırılımına karşı ölçülür. Önceki G2/V2 ve batch 009 TR9 ile örtüşen olaylar tek kimlik.

### L10b — Kırılım sonrası düşük hacimli ilk retest

- **Kaynak:** Kırılımdan sonra geri çekilme, azalan hacim, kırılım mumunun dibine saygı ve dönüş mumu ile ikinci giriş (s. 47 görseli); başka örnekte destek üzerinde dönüş (s. 49–54). Gün içi 60m teyit kaynakta var, günlük karar deneyinden ayrı kohort olmalı.
- **Bizim kapalı günlük olay:** L10a'nın dondurulmuş `R` seviyesi ve kırılım mumu dibi saklanır. Sonraki en çok 5 günlük barda ilk `low<=R+0.25 ATR14[t_break-1]`, `close>R`, `low>=breakout_low`, `volume<volume[break]`, `close>open` olursa retest sinyali. `5 gün`, `0.25 ATR` ve kapanış rengi bizim sayısallaştırmamız. Fiyat önce `breakout_low` altına günlük kapanırsa kurulum iptal. Short simetri.
- **Yürütme:** Retest teyit kapanışı sonrası ilk 1m; stop retest ve kırılım diplerinin min'i `-0.1 ATR`, 2R/3R ve 3/7/10 gün varyantı. Kırılım girişine karşı retest beklemenin fırsat kaçırma oranı, dolum ve net R ayrı raporlanır. Önceki S2/D1/O1 retest fikirleriyle aynı fiyat davranışı olabilir; bağımsız strateji sayılması ablation sonucuna bağlı.

### L10c — Band dışı aşırı uzama ve ters mum, düşük öncelikli karşı yön

- **Kaynak:** Bollinger bandı dışındaki ters mum ve MA21'den yaklaşık `3×VOL(21)/10` mesafe, stop mum ekstremumunda (s. 56 görseli). `VOL(21)` slaytta açık formülle tanımlanmıyor; s. 35–41 yüzde tarihsel volatilite/mesafe ölçüleriyle farklı bağlamda kullanılıyor. Bu nedenle özgün eşik doğrudan kodlanamaz.
- **Bizim ayrı hipotez:** `close[t]>BBupper20_2[t]` ve `close[t]-SMA21[t]>3 ATR14[t-1]`, üst fitil `>2×gövde`, `close[t]<open[t]` olursa short; alt band simetri. `3 ATR` kaynak formülünün eşdeğeri **değildir**. Sonraki 1m giriş, mum tepesi `+0.1 ATR` stop, SMA21 veya 1R/2R ve 3/7 gün çıkışı. Önceki Bollinger aşırılık/çekiç ve F1 reddedilme ile olay çakışması etiketlenir; ancak `VOL` netleşmedikçe düşük öncelik.

## 2. Trading Strategy Guides — Gann Trading Stratejisi

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 9/Baskı 9/Gann Trading Stratejisi - Trading Strategy Guides (15 sayfa) - @eseckal.pdf>)

Kitap pivot high/low'dan 1/1 ve 2/1 dahil fan çizgileri, 2/1 kırılımında dönüş teyidi, son swing dip altında stop ve yeni pivot dipten fanla 1/1 altı kapanış çıkışı öneriyor (s. 3–11). Ancak grafikte **45 derece**, ekranın fiyat/zaman ölçeğine bağlıdır; sabit ekonomik fiyat eğimi değildir. Hangi “önemli” pivotun seçileceği, fiyat birimi başına bar ölçeği ve fanın ne zaman yeniden çizileceği sayısal değil. S. 7 bir yerde 2/1 kırılımını giriş koşulu yaparken aynı paragrafta 1/1 üzerine çıkınca satın al diyor; s. 10 stop anlatımında 1/2 kırılımı geçiyor. Tek özgün mekanik strateji diye kodlamak yanıltıcı olur.

### GN10 — Ölçeği sabitlenmiş fan kırılımı, **araştırma adaptasyonu**

- **Olay:** `k=3` sağ barla teyitli eski pivot high `P` ancak onaylandığı kapanıştan sonra kullanılır. Pivot yüksekliği `P`, referans ölçek `q=ATR14[pivot_confirmation]` olarak dondurulur. `j` bar sonraki çizgi `P + r×q×j` (`r∈{1,2}`), kısa yön için pivot low'dan ters işaretli çizgi. Yalnız son 30 gün içinde çizilmiş fan. Fiyat önce 1/1, sonra 2/1 üstünde günlük kapanınca long olay; short simetri. `k`, ATR ölçeği, 30 gün ve çizgi matematiği **tamamen bizim hipotezimiz**, görsel 45 dereceyi birebir temsil etmez. 1/1'de giriş ile 2/1 teyitli giriş, kaynak çelişkisi nedeniyle **ayrı** sürüm.
- **Yürütme:** Onay kapanışından sonraki ilk 1m; sinyalden önce teyitli en son pivot low altı `0.1 ATR` stop, ters yön simetri. Yeni pivot low fanı için üç sağ bar onayı beklenir; 1/1 altı kapanış veya 2R/3/7/14 gün ayrı çıkışlar. Yeni pivot seçiminin gecikmesi ve dolmayan fan koşulları loglanır.
- **Karar:** Eğim seçimi keyfî ve eşik araması riski yüksek. İlk backtest önceliği **yok**; aynı pivot/ATR trend çizgisi bazına karşı ek katkı görülmeden kullanma. Kitaptaki “geriye test edildi” sözü (s. 12) veri/metodoloji sunmadığından performans kanıtı değildir.

## 3. Forex Scalping Stratejisi

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 9/Baskı 9/Forex Scalping Stratejisi (28 sayfa) - @eseckal.pdf>)

Kaynak M5/M15 giriş ve H4 ana trend bağlamı, BB, MA200/50/3/7, Momentum, ZigZag ve Fibonacci araçlarını listeliyor (s. 10–16). Satış için MA50 aşağı eğim, fiyat MA200 altında, MA3 MA7'yi aşağı keser, Momentum aşırı alımda ve ayı mumu BB çizgilerinden birinin altında kapanır; alış simetri (s. 17–18). Çıkış ters MA3/7 kesişimi veya Fibonacci %61.8; kırılırsa %127 hedef (s. 25–27). **Momentum dönemi, aşırı alım eşiği, MA türü, BB sapmaları ve “hangi BB çizgisi”** net tanımlı değil. ZigZag geçmiş pivotları sonradan yeniden çizebilir; canlı kararda ancak teyitli pivot kullanılır. Haber takvimi adımları (s. 19–24) fiyat verisiyle test edilemez. “Kararların %80'i garanti” ifadesi (s. 16) kanıt olarak alınmadı.

### FS10 — M5 MA3/7 kesişimi, H4 trend ve momentum filtresi

- **Bizim kapalı M5 baz:** MA türünü `EMA` ve M5 olarak önceden sabitle; long `EMA3[t-1]<=EMA7[t-1] && EMA3[t]>EMA7[t]`, `EMA50[t]>EMA50[t-1]`, `close[t]>EMA200[t]`, `close[t]>open[t]`. Short simetri. H4 bağlamı yalnız **son kapanmış H4** için `close_H4>EMA50_H4` ve EMA50 eğimi uygun ise geçer; H4 trend çizgisi kaynakta elle çizilir, EMA50 yerine koymak bizim adaptasyon. Temel bazda Momentum ve BB filtreleri yok; çünkü kitap tam parametre vermez.
- **Filtreli duyarlılık:** `MOM14=100×close[t]/close[t-14]` ve long için `MOM14<98` gibi “aşırı satım” eşiği, `BB(20,2)` orta çizgisi üstü kapanış bizim hipotez; 14, 98, BB20/2 kaynaktan çıkmaz. Momentumun kesişimle aynı anda aşırı satımda olması az olay üretebilir; sinyal sayısı ve geçiş sırası önce raporlanır. ZigZag/Fibonacci hedefleri ilk testte yok; önceden teyit edilmiş pivotla ayrı sürüm gerekir.
- **Yürütme:** Kapanmış M5 t sonrası ilk yürütülebilir 1m; stop `min(low[t],low[t-1])-0.1 ATR14_M5` (short ters), çıkış ters EMA3/7 kesişiminden sonraki ilk 1m, 1R/2R ve 6/12/24 M5 barı ayrı. Ücret, spread, kayma ve belirsiz 1m stop/TP sırası dahil. Kaynağın stop seviyesi sayısal değil; bu risk kuralı bizim. Batch 008 RP1 gibi M5 adaylarıyla aynı maliyet/kohort koşullarında karşılaştır.

## Ortak test kararı

1. **Öncelik:** L10a kırılım ve L10b ilk retest; mevcut sıkışma/kırılım adaylarına göre ek katkısı ölçülür. FS10 ancak yeterli kaliteli M5/1m yürütme verisi varsa ayrı kohort. GN10 ve L10c belirsiz ölçek/formül nedeniyle keşif düzeyi.
2. Her olayda kaynak sayfası, t kapanışında bilinen seviyeler, dondurulmuş pivot/bant, giriş/iptal, dolum, maliyet/funding, net R, MAE/MFE, zaman ve varlık rejimi kaydedilir. Eğitim/dış örneklem ve çoklu deneme düzeltmesi olmadan “işe yarıyor” sonucu verilmez.
3. Bu dosya yalnız strateji adaylarını saklar; backtest veya paper test yapılmadı.
