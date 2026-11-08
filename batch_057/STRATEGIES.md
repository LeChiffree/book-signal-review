# Kitap okuma 057 — Günlük RSI trendi, kural tabanlı dalga ve FU retesti

**Kapsam:** 16 + 38 + 34 = **88 PDF sayfası**. Üç PDF'nin bütün sayfaları sıralı metne çıkarıldı; atıflar PDF sayfasıdır. Görsel/dalga anlatımının mekanik yorumları **bizim test varsayımımızdır**. Backtest, paper test ve emir yapılmadı.

## 1. Göreceli Güç Endeksi — RSI Göstergesi ile Ticaret

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Göreceli Güç Endeksi -RSI Göstergesi ile Ticaret (16 sayfa) - @eseckal.pdf>) · [Tam metin](01_rsi_trading.txt)

**Kaynak:** RSI hesaplama ve basit/Wilder yumuşatma farkı (s. 4–8), 30 altından **geri üstüne çıkış** ile long ve 70 üstünden geri altına iniş ile short ortalamaya dönüş sinyalleri (s. 9–10). Alternatif trend kuralı, D1 RSI>60 kapanışı sonrası ertesi gün long, başlangıç ve izleyen stop son 10 günün low'u, RSI<40 olursa çıkış; short simetri (s. 12–13). Kaynak trend pozisyonunu RSI 70'i gördü diye kapatmamayı öğütler (s. 14). s. 10'daki yaklaşık %75 dönüş iddiası bağımsız örneklem, maliyet ve ufuk vermediği için kanıt değildir.

### RT57 — D1 RSI 60/40 kırılımı ve önceki 10 gün trailing stop

- **Gösterge ve sinyal:** UTC D1 kapanmış mumlarda RSI(14), **Wilder/RMA** tanımı; en az 100 gün ısınma. Long ilk `RSI[t]>60` ve `RSI[t−1]≤60` kapanışı; short ilk `<40` ve önceki `≥40`. Aynı yönde açık pozisyon varken ekleme yok. Gösterge çeşidi s. 8'de farklı olabildiğinden formül kodda kilitlenir.
- **Giriş/stop:** Sinyal gününün kapanışından sonraki ilk uygulanabilir 1m fiyat (ertesi UTC gün başı). Long stop sinyal anında bilinen `min(low[t−9:t])−1 tick`; short `max(high[t−9:t])+1 tick`. Stop yanlış taraftaysa işlem yok. Her yeni D1 kapanışında, **son tamamlanmış 10 gün** ekstremine güncellenen stop yalnız lehe taşınır: long `max(eski stop, yeni10Low−tick)`, short `min(...)`. Yeni stop bir sonraki 1m barından önce geçerli olur; gün içindeki gelecekteki low/high kullanılmaz. RSI long için <40, short için >60 kapanırsa ertesi ilk 1m'de çıkış; stop daha önce gerçekleşirse stop geçerli. 30 D1 bar maksimum süre bizim güvenlik sınırımız; kaynak süre vermez.
- **Ayrı kol/karşılaştırma:** 30 altından/70 üstünden geri geçiş ortalamaya dönüş kuralını **ayrı hipotez** olarak, aynı veri ve risk bütçesiyle test et; trend kuralıyla sinyalleri birleştirme. Batch056 RR56 güç bölgeleri ve önceki RSI çalışmalarına karşı sinyal örtüşmesi ve maliyet sonrası net sonuç. Kriptoda UTC D1 sınırının duyarlılığını ayrıca ölç.

## 2. Robert Prechter — Elliott Dalga Prensibinin Temelleri

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Elliott Dalga Prensibinin Temelleri - Robert Prechter (38 sayfa) - @eseckal.pdf>) · [Tam metin](02_elliott_foundations.txt)

**Kaynak:** İtki dizisi 1–5 ve karşı dalgalar 2/4 olarak tarif edilir (s. 5–8). Motif dalgada 2, 1'i; 4, 3'ü tam geri alamaz; 3, 1'in ötesine geçer; dürtü türünde 4, 1'in fiyat alanına girmez (s. 12). 2 ve 4 diplerinden çizgi, 3 tepesinden paralel kanal 5 için olası hedef rehberidir (s. 26). Alternatif sayımların ve belirsizlikte beklemenin önemi açıkça yazılır (s. 28). Geçmiş grafiğe sonradan dalga numarası koymak işlem anında sinyal oluşturmaz; Fibonacci/doğa benzetmeleri (s. 30–38) istatistiksel doğrulama değildir.

### EP57 — Teyitli 1–4 dalga geometrisi sonrası 5. dalga kırılımı

- **Pivotlar:** H4 gerçek fiyat mumlarında yalnız 3 sol/3 sağ tamamlanmış barla teyit edilen ardışık, dönüşümlü swing low/high. İlk beş pivot `P0 low, P1 high, P2 low, P3 high, P4 low` (short ters). P2>P0, P3>P1, P4>P2 ve **P4>P1** olmalı; son koşul kaynağın dalga 4/1 çakışmama kuralını karşılar. Her komşu pivot 2–30 H4 bar aralığında; hiçbir pivot üç sağ bar kapanmadan kullanılmaz. Kaynağın dalga derecesini bu sabit pivot ölçeğiyle yaklaşıkla; etiketler gerçek Elliott sayımının kesinliği değildir.
- **Tetik:** P4 teyidinden sonra en çok 12 H4 bar içinde ilk `close>P3+0,1×ATR14_H4` long (short simetri). P4'ten P3 kırılımına kadar P2 altına inilirse iptal. Sinyal H4 kapanışından sonraki ilk uygulanabilir 1m giriş. 3. dalganın 1 ve 5'ten kısa olmaması ancak **5 tamamlandıktan sonra** değerlendirilebilir; girişte gelecekteki P5'i kullanarak filtreleme yok.
- **Risk/çıkış:** Long stop P4 low `−0,1×ATR`, short simetri. Ana hedef 2R ve en çok 18 H4 bar. Kaynak kanalının ayrı kolunda P2–P4 alt çizgisine, P3'ten paralel üst çizgi çiz; P4 teyit anında dondur, hedef giriş anındaki üst çizgi değeri değil **ileriye uzatılmış çizgiyle ilk 1m kesişme**; hareketli hedefin her 1m anındaki değerini yalnız önceden dondurulmuş eğim/kesimden üret. Hedef yanlış tarafta ise bu kolu atla. Aynı 1m stop/hedefte stop önce, stop maliyetten dar ise atla.
- **Karşılaştırma:** Beş pivot kırılımını sıradan swing high kırılımıyla aynı olaylarda karşılaştır; Elliott etiketi başlı başına ek bilgi taşıyor mu? Geriye dönük farklı sayımlardan en iyi görüneni seçme.

## 3. Forex'te Bankaların Manipülasyonu

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Forex_te Bankaların Manipülasyonu (34 sayfa) - @eseckal.pdf>) · [Tam metin](03_bank_manipulation.txt)

**Kaynak:** Doji/çift tepe-dip çevresinde likidite arama (s. 15–17), seviye üstü/altı süpürme ve limit giriş (s. 20–21), “FU” mumunun likidite alıp güçlü ters kapanması (s. 23–26), bu mumun yeniden testi (s. 28) ve dengesizlik alanı (s. 30) temel unsurlar. D1 bağlam + kurumsal bölge + likidite alımı + FU retesti kontrol listesi s. 33'tedir. “Bankalar fiyatı manipüle ediyor” iddiası kaynakta piyasa mikro verisiyle kanıtlanmaz; gözlenebilen olay yalnız OHLC üzerinde süpürme, reddetme ve retesttir. Olağanüstü RR örnekleri (s. 4–5, 31) uygulanabilir dolum ve maliyet kanıtı değildir.

### BM57 — Teyitli eşit ekstrem likiditesi sonrası FU reddi ve ilk retest

- **Ön seviye:** M15'te 2 sol/2 sağ mumla teyitli son iki swing high'ın fiyat farkı `≤0,2×ATR14_M15` ise eşit high bölgesi, iki swing low için eşit low. Pivotlar sinyalden önce teyit edilmiş, araları 4–48 M15 ve sonuncusu en çok 48 M15 önce olmalı. Bölge shortta iki high'ın büyüğü, longda iki low'un küçüğüdür; geçmişte henüz görülmemiş pivot yok. Kaynaktaki çift tepe/dip likiditesinin bizim objektif vekilidir.
- **FU sinyali:** Short için tamamlanmış ilk M15 `high>eşitHigh+0,1×ATR`, `close<eşitHigh` ve üst fitil `≥1,5×gövde`; long eşit low altına süpürüp üstte kapanma ve alt fitil. Mum aralığı sıfırsa atla; gövde sıfırsa fitil koşuluna ek olarak fitil `≥0,4×tam aralık`. Bu şekil kaynağın görsel FU tanımının bizim sabitlememizdir. D1 filtresi ayrı kol: short yalnız son **tamamlanmış** D1 close<EMA20_D1, long >EMA20. Filtre kaynağın “D1 anlamlı” şartına bire bir eşit değildir.
- **Retest/icra:** FU kapanışından sonraki en çok 8 M15 mumda ilk geri dönüşte FU gövdesinin orta noktasına limit emir; short için fiyat yukarı, long için aşağı gelmeli. 1m üzerinde emir seviyesi gerçekten görülmezse dolum yok; sinyal mumunda geriye dönük dolum yok. Stop short FU high `+0,1×ATR`, long FU low `−0,1×ATR`; 2R ve 3R ayrı çıkış kolları, 24 M15 bar süre. Stop yanlış tarafta/maliyetin iki katından dar ise atla; aynı 1m stop/hedefte stop önce. İlk retestten sonra kurulum tüketilir.
- **Karşılaştırma:** Önceki sweep, wick rejection ve OB/FVG adaylarıyla olay örtüşmesini ölç. FU gövde ortası limitinin teyit kapanışı sonrası piyasa girişine göre gerçek dolum oranı, net R ve kaçırılan işlemlerini birlikte raporla. “Kurumsal akış” etiketi olmadan da bu fiyat örüntüsü açıklanabilir.

## Ortak test notu

Semboller, dönem, giriş/çıkış parametreleri, pozisyon çakışması ve eksik veri politikası testten önce dondurulmalı. Her sinyal yalnız tamamlanmış mum ve o anda teyitli pivot kullanır. Sonraki uygulanabilir 1m dolum, ücret, spread, kayma ve perpetual funding katılır. Zaman sıralı ayrılmış dönem, basit karşılaştırma, net R, örneklem, maksimum düşüş ve parametre duyarlılığı olmadan kârlılık sonucu çıkarılmaz.
