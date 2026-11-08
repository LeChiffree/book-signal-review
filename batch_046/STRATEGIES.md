# Kitap okuma 046 — Heikin Ashi scalp, RSI ve sıkışma kırılımı

**Kapsam:** 22 + 20 + 50 = **92 PDF sayfası**. Üç PDF'nin tüm sayfaları sıralı metne aktarıldı; scalp s. 13–14 ve Heikin Ashi sıkışma s. 31–32 görselleri ayrıca incelendi. Atıflar PDF sayfasıdır. Kaynak kuralları ile bizim kapalı mumlu kripto test sözleşmesi ayrıdır. Backtest, paper test ve emir yapılmadı. Kartik K imzalı VWAP PDF'si batch043'teki VWAP metninin büyük bölümünü yinelediği için bu partinin üç kitabına dahil edilmedi.

## 1. Heikin Ashi Trader — Scalping Eğlencelidir

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 16/Baskı 16/Scalping Eğlencelidir - Heikin Ashi Trader (22 sayfa) - @eseckal.pdf>) · [Tam metin](01_scalping_fun.txt) · [İlk ters renk ve çıkış s. 13–14](scalp_p13.png)

**Kaynak:** Yazar 1 dakikalık Heikin Ashi grafiğinde belirgin mikro hareketten sonraki ilk ters renkli mumla karşı hareketi alır; renk tekrar döndüğünde çıkar (s. 10–14). Short örneği kuvvetli yükselişten sonra ilk kırmızı HA mumunda açılır, ilk yeşilde kapanır (s. 12–14). 5–10 Forex pip stop anlatılır (s. 12), fakat pip sabiti kriptoya taşınamaz. Küçük aralık, belirsiz trend, haber ve merkez bankası olayları işlem dışı sayılır (s. 15). Kitap görsel/öznel “belirgin hareket” tarifi verir; hareket büyüklüğü, likidite ve spread eşiği yoktur. S. 19–22 sonraki cildin tanıtımıdır, ek giriş kuralı içermez.

### HS46 — M1 güçlü hareketten ilk HA renk dönüşü

- **Bizim gösterge ve rejim:** Gerçek 1m OHLC'den `HAclose=(O+H+L+C)/4`, `HAopen[t]=(HAopen[t−1]+HAclose[t−1])/2`, `HAhigh=max(H,HAopen,HAclose)`, `HAlow=min(L,HAopen,HAclose)`; başlangıç `HAopen=(O+C)/2`. İcra ve P&L için yalnız **gerçek** fiyat kullan. Short öncesi en az 5 ardışık yeşil HA kapanışı, o dizide `close[t−1]/close[t−6]−1 > 3×ATR14_M1[t−1]/close[t−1]`; long tersine. 5 bar ve 3 ATR eşiği kaynakta yok, bizim “belirgin” hareket tanımımızdır. En az 100 bar ısınma ve 24 saatlik gerçek hacim/alış-satış spreadi veri kapısı.
- **Olay:** İlk kapanmış kırmızı HA mumu `t` short, ilk yeşil HA mumu long sinyali. Giriş sonraki ilk uygulanabilir 1m fiyatı; HA mumunun hesaplanan kapanış fiyatından dolum yazma. Sinyalden önceki 10 M1 barın `high−low` aralığı `<3×spread` ise işlem yok; bu sayısal dar-aralık filtresi bizimdir. Haber filtresi ancak geçmişte ilan edilmiş point-in-time olay takvimi mevcutsa ayrı deney olarak uygulanır; olmayan haber verisi geriye dönük elle seçilmez.
- **Risk/çıkış:** İlk stop short son 5 gerçek M1 barın en yüksek `high`ı `+0.1 ATR14_M1`, long son düşük `−0.1 ATR`; stop mesafesi `<2×tahmini gidiş-dönüş maliyeti` ise giriş yok. İlk ters HA rengi **M1 kapanışında** görülünce sonraki uygulanabilir fiyatla çık; stop veya en çok 15 M1 bar süre sınırı. ATR tamponu, süre ve maliyet filtresi bizim; kaynak yalnız ters renk ve Forex pip stopu verir.
- **Karşılaştırma:** İlk renk dönüşü, iki ters renk bekleme, önceki hareket eşiği olmadan aynı olay; batch045 HA D1 ve diğer HA adaylarıyla zaman dilimi/işlem örtüşmesi. M1 maliyetler net getiri için kritik; yalnız brüt küçük kârları sayma.

## 2. Alton Swanson — RSI: Göreceli Güç Endeksi

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 20/Baskı 20/RSI - Göreceli Gün Endeksi - Alton Swanson (20 sayfa) - @eseckal.pdf>) · [Tam metin](02_rsi_swanson.txt)

**Kaynak:** RSI'nin 50 üstü/altı momentum yönünü, 70/30 aşırı bölgeleri gösterir (s. 4). S. 5–10 basit ortalamalı örnekle hesaplar, Wilder yumuşatmasını alternatif olarak anar; bu nedenle platform RSI sürümü kaydedilmelidir. Birinci yaklaşım **30 altından yeniden 30 üstüne** geçince long, **70 üstünden yeniden 70 altına** geçince short; uç bölgeye ilk girişte ters pozisyon açılmamalı (s. 11–12, 16). İkinci yaklaşım RSI **60 üstü** D1 kapanışından ertesi gün long, 10 günlük dip takip stopu ve RSI **40 altı** kapanışında çıkış; short simetrik (s. 14–15). Trendde RSI70'e değdi diye long kapanmaz (s. 17). S. 12'deki yaklaşık %75 dönüş iddiası örneklem, maliyet veya bağımsız kayıtla desteklenmez; işlem kârlılığı anlamına gelmez.

### RS46a — RSI 30/70 bölgesinden çıkışla ortalamaya dönüş

- **Bizim seri:** UTC D1 kapanışından `gain=max(C[t]−C[t−1],0)`, `loss=max(C[t−1]−C[t],0)`, `AvgU=SMA14(gain)`, `AvgD=SMA14(loss)`, `RSI=100 AvgU/(AvgU+AvgD)`; sıfır paydada 50, yalnız kayıp sıfırsa 100, yalnız kazanç sıfırsa 0. **SMA14 kaynak hesap örneğine yakın**; Wilder RMA14 ayrı kol. 100 D1 bar ısınma.
- **Olay/icra:** Long `RSI[t−1]<30` ve `RSI[t]≥30` kapalı D1; short `RSI[t−1]>70` ve `RSI[t]≤70`. Sonraki ilk uygulanabilir 1m fiyatından giriş. Stop long son 10 **sinyal dahil** D1 barın en düşük gerçek low'u `−0.1 ATR14_D1`, short simetrik; 1.5R hedef veya 10 D1 bar zaman çıkışı. Stop/target/süre kaynakta verilmez, bizimdir. Bölge içinde yeni sinyal yok; karşı bölgeye kadar aynı yönde yeniden giriş engeli ayrı ablation.
- **Karşılaştırma:** RSI uç bölgeye giriş, çıkış ve 50 geçişi; batch031 RSI 80/20, batch043 güç bölgesi ve batch044 başarısızlık salınımıyla aynı olay evreninde. Yüzde 75 iddiası ölçülmüş performans diye kullanılmaz.

### RS46b — RSI 60/40 momentumla trend takibi

- **Kaynağa yakın olay:** Aynı SMA14 RSI'da ilk `RSI[t−1]≤60`, `RSI[t]>60` D1 long; short ilk `RSI[t−1]≥40`, `RSI[t]<40`. Karar yalnız tam D1 kapanışında, giriş sonraki ilk uygulanabilir 1m fiyatı. Long başlangıç stopu `min(low[t−9:t])`, short `max(high[t−9:t])`; kaynak “son 10 gün” dediği için **t dahil** pencereyi açıkça sabitledik. Stop yanlış tarafta veya maliyetin iki katından yakınsa işlem yok.
- **Takip/çıkış:** Her D1 kapanışında stop long için önceki stop ile son 10 tam D1 bar dip maksimumu, short için minimumu olacak şekilde yalnız kâr yönüne taşı; yeni stop ancak **sonraki** 1m itibarıyla geçerli. Long RSI<40, short RSI>60 kapanışında sonraki 1m'de çık. Kaynakta süre yok; 40 D1 bar süre çıkışı ayrı bizim kolumuz. `RSI>70` long çıkışı değildir.
- **Karşılaştırma:** RSI sinyali tek başına, D1 EMA200 yönüyle filtreli ayrı kol ve batch007/batch032 RSI trend adayları. RSI ortalama metodunu test dönemine bakarak seçme.

## 3. Tim Haddock ve Ravi Kapoor — Heikin Ashi Grafikleriyle Günlük Trade

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 8/Baskı 8/Heikin Ashi Grafikleriyle Günlük Trade - Tim Haddock ve Ravi Kapoor (50 sayfa) - @eseckal.pdf>) · [Tam metin](03_heikin_ashi_haddock_kapoor.txt) · [Long/short kuralları s. 31–32](ha_p31.png)

**Kaynak:** 15m kurulumda Bollinger 20 SMA±2σ bantlarının Keltner 20 ATR×1,5 içine sıkışması; EMA13/21/55 sıralaması; iki kuvvetli aynı renk HA mumunda ters yöndeki fitil/kuyruğun yok denecek kadar az olması (s. 15–16, 19–20, 26–32). Long için iki beyaz HA mumunun küçük/olmayan **alt kuyruğu**, short için kırmızıların küçük/olmayan **üst fitili**. Sinyal barının orta noktasına limit emir, yalnız sonraki barda dolarsa işleme girme; kovalamama (s. 31–32, 36–37). İlk stop sinyal barı dışında ve ardından önceki gerçek barı takip, iç bar sırasında stopu yerinde tutma (s. 32, 37). HA fiyatları gerçek kapanış değildir; normal mum grafiğini yanında tutarlar (s. 19–20). Daha yüksek zaman dilimi sıkışması destekleyicidir; bazı güçlü HA kurulumlarında sıkışma şartı gevşetilebilir (s. 31–32). Kaynak seçilmiş tek hisse/hafta örnekleri verir, genel performans kanıtı değildir (s. 33–49).

### HK46 — M15 sıkışma + iki kuvvetli HA mumu, orta nokta limit

- **Bizim göstergeler:** Gerçek 15m OHLC üzerinde `BBmid=SMA20(C)`, `BBupper/lower=mid±2 population_std20(C)`; `KCmid=EMA20(C)`, `KCupper/lower=mid±1.5 ATR20_Wilder`. **Keltner merkez/ATR yöntemi kaynakta tam verilmez, bu bizim sabitlememizdir.** Sıkışma `BBupper<KCupper` ve `BBlower>KClower` en az 3 tam 15m bar sürsün. EMA13, EMA21, EMA55 gerçek kapanıştan. HA standart formül HS46 ile aynı, ancak M15 barlardan; HA fiyatıyla emir dolumu veya kâr/zarar hesabı yok. En az 200 M15 ısınma.
- **Olay:** Son 3 barda sıkışma gerçekleşmişken iki ardışık **tam kapanmış** beyaz HA barı; ikisinde de `HAopen−HAlow≤0.1×(HAhigh−HAlow)`, ikinci gerçek mumun `high−low≥1.5 ATR14_M15`, EMA13>EMA21>EMA55, `close[t]>BBupper[t]`. Short ters renk, üst fitil, EMA dizilimi ve alt bant. Fitil %10, bar 1.5 ATR, sıkışma 3 bar ve dış banda kapanış **bizim** nesnel seçimlerimiz; kaynakta “küçük fitil” ve “yaklaşık 2 ATR” nitel/veri birimi belirsiz. Sıkışmanın ikinci HA barı sırasında açılmasına izin ver; yalnız `t` kapanışında bilinen koşullarla sinyal ver.
- **İcra:** `t` kapanışından sonra **yalnız sonraki 15m bar** için gerçek sinyal mumunun `(high[t]+low[t])/2` fiyatında limit long/short bırak; bu seviye gerçek 1m bar içinde işlem gördüyse ve aynı 1m'de stopa sıra belirsiz değilse doldur. Dolmazsa iptal, piyasa emrine çevirme. Stop long gerçek `low[t]−0.1 ATR14_M15`, short `high[t]+0.1 ATR`; limit fiyatı stopun doğru tarafında değilse iptal. Hafta sonu/gece boşluğu kaynak hisse bağlamına aittir, kriptoda UTC seans sınırı ayrıca sabitlenir.
- **Takip/çıkış:** İlk dolum sonrası her tamamlanan M15 barda stopu long için son **tamamlanmış gerçek mumun** low'u `−0.1 ATR`, short için high'ı `+0.1 ATR` yönünde taşı; iç bar (`high≤prev_high` ve `low≥prev_low`) ise stopu değiştirme. Stop ters tarafa taşınamaz ve yalnız sonraki 1m'de etkinleşir. 16 M15 bar süre sınırı bizim; 2R hedef ayrı kol, çünkü kaynak sabit hedef yerine trailing stop kullanır. Aynı bardaki fill/stop sırası bilinmiyorsa kötümser yaklaşım.
- **Karşılaştırma:** HA iki-bar şekli tek başına, squeeze eklenmiş, EMA eklenmiş, üçünün birleşimi; batch041 Bollinger squeeze ve batch045 HA renk dönüşüyle aynı olaylarda kıyas. Hisse piyasasına özel `$VOLSPD/$TICK` göstergelerini kripto için kaynaktakiyle eşdeğer varsayma; bunlar temel kolda yok.

## Ortak test notu

Üç aday için point-in-time sembol evreni, yalnız tamamlanmış bar, maliyet/spread/kayma/funding, 1m icra ve zaman sıralı dış örneklem zorunlu. HS46'nın yüksek işlem frekansında gerçekçi dolum; RS46'nın SMA/Wilder farkı; HK46'nın limit emrinin gerçekten değip değmediği ve HA fiyatlarının icraya karışmaması ilk doğrulama kapılarıdır. Kârlılık henüz test edilmedi.
