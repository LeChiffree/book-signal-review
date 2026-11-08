# Kitap okuma 043 — VWAP, ADX ve RSI güç bölgeleri

**Kapsam:** 24 + 11 + 27 = **62 PDF sayfası**. Üç kitabın tüm sayfaları sıralı metne aktarıldı; görsel ağırlıklı VWAP s. 9–10, 13, 15, 22 ve ADX s. 8, 10 ayrıca incelendi. Atıflar PDF sayfasıdır. Kaynaktaki gözlemler ile bizim test için eklediğimiz kurallar ayrıdır. Backtest, paper test ve emir yapılmadı.

## 1. Kolay Para ile VWAP Trade Stratejisi

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Kolay Para ile VWAP Trade Stratejisi (24 sayfa) - @eseckal.pdf>) · [Tam metin](01_vwap_easy_money.txt) · [Destek/direnç görseli s. 9](vwap_p9.png)

**Kaynak:** VWAP seans başında sıfırlanan `Σ(tipik fiyat×hacim)/Σhacim` olarak anlatılır; tipik fiyat `(H+L+C)/3` olmalıdır. S. 3'te formülün sözlü özetinde çıkarma ve parantez hataları vardır; adım 1 ve s. 4–5'teki tanım ağırlıklı ortalamayı doğrular. S. 16 PVWAP, **önceki günün bitiş VWAP değeri** olarak tanımlanır. S. 17'de tamamen VWAP ve PVWAP üstünde kalan 5m mumun tepesi üstünde alım, ikisinin altında kalan mumun dibi altında satış vardır; aralık günlerinde işlem önerilmez. S. 18–19 PVWAP'a düşük hacimli geri çekilme ve orada tutunma; s. 21–22 ilk VWAP geri çekilmesi/reddi ayrı kurulumdur. S. 8–10 görselleri VWAP yakınında gölge/pin bar/yutucu ile reddi örnekler. S. 23 hedef, stop ve takip stopundan söz eder ama sayısal seviye vermez. S. 24'teki %60–80 başarı iddiası örneklem ve bağımsız kayıt içermiyor.

### V43 — Seans VWAP + önceki seans VWAP üstünde 5m mum kırılımı

- **Bizim veri tanımı:** 7/24 kriptoda seans sınırı `00:00 UTC`; bu **bizim** açık seçimimizdir. Tamamlanmış 5m barlarda `TP=(H+L+C)/3`, `VWAP[t]=Σ_session(TP×base_volume)/Σ_session(base_volume)`; sıfır hacimde sinyal yok. `PVWAP[t]` önceki **tam UTC gününün son** VWAP değeridir ve yeni gün boyunca sabittir. İlk 30 dakika sinyal üretme; kaynak ilk açılış hareketinin gürültülü olduğunu söyler (s. 11, 16), 30 dakika eşiği bizim seçimimiz.
- **Olay:** Long kurulumunda 5m `low[t]>max(VWAP[t],PVWAP[t])`; short `high[t]<min(VWAP[t],PVWAP[t])`. Sonraki en çok üç 5m bar içinde ilk uygulanabilir 1m fiyatı sinyal mumunun `high[t]` üstüne çıkarsa long, `low[t]` altına inerse short. Sinyal barının içindeki kırılım giriş sayılmaz. Aynı kurulum yalnız bir kez; VWAP/PVWAP öteki tarafa 5m kapanışıyla geçilirse bekleyen emir iptal. Üç bar geçerlilik penceresi bizim seçimimiz.
- **Risk/çıkış:** Long stop `min(low[t],VWAP[t])−0.1 ATR14_5m`, short simetrik; 2R hedef ve 24 adet 5m bar süre sınırı. Stop yanlış taraftaysa veya net hedef maliyeti karşılamıyorsa atla. Kaynak stopu nicelleştirmez; bütün sayısal risk parametreleri bizim test sözleşmemiz. Aralık filtresi için son 12 tamamlanmış 5m barda VWAP etrafındaki kapanış geçişi `>3` ise sinyal yok; bu da kaynak s. 14, 17 gözleminin **bizim** nesnel karşılığıdır.
- **Karşılaştırma:** Yalnız VWAP, VWAP+PVWAP ve aralık filtresi eklenmiş sürüm; önceki VWAP stratejileri (batch034 dahil) ile aynı olay evreni. PVWAP'ı bugünün kapanışıyla doldurmak lookahead olur. Kripto seans açılışının hisse piyasası açılışıyla aynı davranacağı varsayılmaz.

## 2. ADX İndikatörü — Learn Price Action

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 8/Baskı 8/ADX İndikatörü - Learn Price Action (11 sayfa) - @eseckal.pdf>) · [Tam metin](02_adx_learn_price_action.txt) · [Örnek kırılım s. 10](adx_p10.png)

**Kaynak:** Varsayılan ADX 14 ve +DI/−DI bileşenleri (s. 2–4). ADX **trendin yönünü değil gücünü** ölçer (s. 2, 4); 0–25 yatay/zayıf, 25–50 trend, 50–75 güçlü, 75–100 çok güçlü olarak sınıflanır (s. 4–5). S. 7–8 güçlü ADX sırasında trend yönünde geri çekilme long örneği, s. 9–10 alt zaman diliminde güçlü ADX ile fiyat kırılımı örneği; kesin tetik, stop ve hedef formülü verilmez. ADX düşüşü trend işlemini yönetmek için uyarı olabilir (s. 7). ADX tek başına al/sat yönü vermez.

### A43 — Donchian kırılımına ADX güç filtresi

- **Bizim sabit gösterge:** H1 OHLC ile Wilder TR, +DM, −DM ve 14 bar RMA; `+DI=100 RMA(+DM)/ATR`, `−DI=100 RMA(−DM)/ATR`, `DX=100|+DI−−DI|/(+DI+−DI)`, `ADX=RMA14(DX)`. Sıfır paydada sinyal yok. 100 H1 bar ısınma. Bu Wilder hesaplamasını açıkça sabitlemek platform farkını azaltır.
- **Olay:** Önceden bilinen Donchian üstü `U=max(high[t−20:t−1])`, altı `L=min(low[t−20:t−1])`. Long `close[t]>U`, `+DI[t]>−DI[t]` ve `ADX[t]>25`; short tersi. Kırılım seviyeleri **t−1'e kadar** bilinir, ADX/DI t kapanışında; giriş sonraki ilk uygulanabilir 1m fiyatı. 20 bar Donchian ve DI yön şartı kaynakta formül olarak yoktur; ADX'i gerçekten test edilebilir bir filtre yapmak için bizim seçimimiz.
- **Risk/çıkış:** Long stop `U−0.1 ATR14_H1`, short `L+0.1 ATR`; 2R hedef veya 24 H1 bar süre çıkışı. Ayrı çıkış kolunda `ADX<25` H1 kapanışından sonraki 1m'de çık. Stop yanlış taraftaysa veya maliyetin iki katından yakınsa işlem yok. Stop/hedef/süre tamamen bizimdir.
- **Karşılaştırma:** Donchian tek başına, `ADX>25`, `ADX>50` ve `ADX yükseliyor` kolları; batch001/batch016 ADX adaylarıyla etkileşim ve işlem örtüşmesi. Kaynak s. 7 grafiğinde ADX 60+ örneği vardır ama bunun evrensel eşik olduğuna dair veri yok.

## 3. Hima Reddy — Kazanan RSI Playbook

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 11/Baskı 11/Kazanan RSI Playbook - Hima Reddy (27 sayfa) - @eseckal.pdf>) · [Tam metin](03_rsi_playbook_reddy.txt)

**Kaynak:** RSI 14 sabit tutulur (s. 13, 17). Klasik 70 üstünü otomatik short veya 30 altını otomatik long saymak güçlü trendlerde erken karşı işlem doğurabilir (s. 13–14, 19, 22–24). Ayı rejimi için RSI direnç bandı **55–65**, destek bandı **20–30**; boğa rejimi için destek **40–50**, direnç **80–90** (s. 16–18). S. 22–25 fiyat önceki tepeyi aştıktan sonra RSI'nin 40–50 üstünde tutunması ve sonrasında 80–90'a genişlemesi örneklenir. S. 27 giriş/çıkışların tam kurallarını **ayrı ücretli stratejiye** yönlendirir; bu PDF tam bir işlem sistemi sunmaz. Bölgeler performans kanıtı değil, test hipotezidir.

### R43 — Boğa RSI destek bölgesinde devam

- **Bizim rejim/tetik:** H4'te Wilder RSI14. Boğa rejimi ancak `close[t−1]>EMA200[t−1]` ve önceki 40 tamamlanmış H4 barın tepe kapanışı H4 `t−1` itibarıyla yukarı kırılmışsa aktif; bu trend tanımı **bizim**. Rejim içinde RSI en az bir kez `40≤RSI≤50` aralığına girdikten sonra ilk `RSI[t−1]≤50` ve `RSI[t]>50` kapanışı, `close[t]>EMA200[t]` koşuluyla long. Düşüşteki 55–65 bandından aşağı retest ve EMA altı short simetrik **ayrı kol**, RSI bölgeleri birebir simetrik değildir.
- **İcra/risk:** Kapanış sonrası ilk uygulanabilir 1m giriş; long stop RSI bölgesinde gerçekleşen son 5 H4 barın en düşük `low` değeri `−0.1 ATR14_H4`, short simetrik. 2R hedef veya 20 H4 bar süre. Long için `RSI<40` H4 kapanışı erken çıkış kolu; `RSI 80–90` bölgesine girince tam/yarım kâr ayrı kol. Bu emir, stop ve süre kuralları kaynakta yoktur; bizim açık hipotezimizdir.
- **Karşılaştırma:** RSI14 30/70 ters işlem tabanı, RSI 40–50 retest, EMA rejimsiz retest, genel EMA trend+pullback tabanı ve önceki RSI adayları. Bölge seçimi kaynaktan, rejim ve fiyat tetik bizim seçimimiz. S. 27'de eksik bırakılan ücretli giriş/çıkış kuralları bu taslağa kaynak kuralı olarak atfedilemez.

## Ortak test notu

Üç aday aynı point-in-time varlık evreninde, yalnız kapanmış mumla, gerçek ücret/spread/kayma/funding ve zaman sıralı dış örneklemle değerlendirilmelidir. Aynı 1m barda stop ve hedef görülürse kötümser sıra uygulanmalı. Öncelik V43'te 7/24 seans sınırı duyarlılığı, A43'te ADX'in yalnız filtre olarak marjinal katkısı, R43'te kaynakta eksik olan giriş/çıkışların güçlü tabanlarla karşılaştırılmasıdır. Hiçbirinin kârlılığı henüz doğrulanmadı.
