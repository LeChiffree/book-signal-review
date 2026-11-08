# Kitap okuma 076 — kanal çıkışı, yapı teyidi, gövdeye çizilen Fibonacci

**Kapsam:** Üç PDF'nin gerçek **132 + 26 + 31 = 189 sayfası** sırayla okundu; [kritik grafikler ve metni kısa sayfalar](figure_contacts/) görsel incelendi. Atıflar PDF sayfasıdır. Kitabın vermediği sayılar **bizim test parametrelerimizdir**. Backtest/paper/emir yapılmadı.

## 1. Short — Dr. Alexander Elder

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 6/Baskı 6/Short - Dr. Alexander Elder (132 sayfa) - @eseckal.pdf>) · [Tam metin](01_short_elder.txt)

**Kaynak taraması:** Bu PDF özgün sistem kitabından çok **çalışma kılavuzu**: s. 6–19 alış/risk soruları, s. 23–43 satış/stop/kanal soruları, s. 47–57 short soruları; s. 59–129 cevaplar ve grafik açıklamaları. S. 81–84 girişten önce hedef/stopu yazma, s. 88–90 EMA veya kanal hedefleri ve gerçek kırılım/sahte kırılım bağlamı, s. 91–98 stopu aleyhte genişletmeme ve SafeZone/oynaklık, s. 115–127 shortta yükseliş tepesinden avlanmak yerine düşen kanalın değer bölgesinde satış ve alt kanalda kar alma anlatılır. S. 129–130 plan ve günlük tutma özetidir. Hisse ödünç alma, temettü, short-interest ve opsiyon soruları kripto futures OHLCV stratejisi değildir. Kitaptaki kanal çizimleri ve örnek kazançlar istatistiksel üstünlük kanıtı sayılmaz.

### SE76 — Düşen kanalda değere dönüşte short, alt bantta kısmi çıkış

- **Kaynak fikri:** Haftalık stratejik düşüşte günlük fiyat EMA ile temsil edilen değere/üst tarafa yükseldiğinde short aramak; fiyat alt kanalın düşük değer bölgesine geldiğinde pozisyonu kapatmak veya azaltmak (s. 49, 83–90, 115–117, 125–127). Bu kaynakta tek kesin giriş algoritması yoktur; aşağıdaki olay araştırma vekilidir.
- **Bizim kapalı mum olayı:** Yalnız tamamlanmış haftalık `EMA10_W<EMA20_W` ve `close_W<EMA20_W` ise ayı rejimi. Günlük `EMA20_D` eğimi son 5 günde negatif, son 10 günün en az birinde `close<EMA20_D−1×ATR14_D`, ardından bugünkü kapalı mum `high≥EMA20_D` fakat `close<EMA20_D` ise değere başarısız dönüş short. Önceki 20 tamamlanmış günlük düşüklerden `lower20=min(low)` dondurulur; short girişinde hedef `lower20` veya 2R ayrı kollar. 10/20 hafta, EMA20, 5/10/20 gün ve 1 ATR **bizim parametrelerimizdir**; kaynak belirli EMA uzunluğu vermez.
- **İcra/risk:** Günlük sinyal sonrası ilk uygulanabilir 1m short. Stop `max(signal_high, prior10_high)+0,1×ATR_D`, hedef lehte ve net ödül-risk ≥1 değilse işlem yok. Alt banda ilk temas sonrası tüm pozisyonu kapama ile yarısını kapayıp kalanını son 3 günlük high üzerinden yalnız lehte sıkılaştıran stopla sürdürme ayrı kollar; 7/14 gün süre. Stop asla aleyhte genişletilmez; aynı 1m'de stop/TP olursa stop önce, maliyet/funding dahil.
- **Karşılaştırma:** Mevcut ayı piyasası/EMA geri dönüşü adaylarıyla sinyal örtüşmesini ölç; asıl ayrı test **alt kanal hedefi ve kısmi çıkışın** sabit 2R/zaman çıkışına göre net katkısıdır. Bu yeni alpha değilse sadece çıkış modülü olarak tut. SafeZone'un özgün formülü bu PDF'de eksik olduğundan adıyla yeni hesap uydurulmadı.

## 2. Price Action — Elliot Baker

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 6/Baskı 6/Price Action - Elliot Baker (26 sayfa) - @eseckal.pdf>) · [Tam metin](02_price_action_baker.txt)

**Kaynak taraması:** S. 2–9 HH/HL ve LH/LL ile trend, kırılım ve yapı korunması; s. 10 sipariş akışını pazarlayan bölüm olup OHLCV'den gerçek defter likiditesi çıkarılamaz; s. 11–15 trend, yatay bant, çizgi/kanal; s. 16–20 mum ve H&S/kama ölçülü hedef; s. 21–24 trend içi arz-talep dönüşü ve sahte sinyalin geç teyidi; s. 25–26 risk. S. 18'deki %60–65 formasyon başarı iddiası veri/metot olmadan kabul edilmedi. Çok sayıda şekil eski kayıtlarla aynı ailede; bu PDF'nin araştırılabilir ek fikri **yapı bozulmasının ardından devam edip etmemesi için süre sınırı**dır.

### EB76 — Yapı kırılımının kısa sürede teyit edilmemesiyle başarısız kurulum filtresi

- **Kaynak fikri:** Önceki swing seviyesi kırılınca yapı değişimi ihtimali doğar; kalıcı trend için sonraki salınımların da yönü doğrulaması gerekir (s. 7–9). Sahte kurulum ile gerçek kurulum ayrımında fiyatın beklenen yönde ne kadar hızlı hareket ettiği önemlidir (s. 22–24). Kitap kesin gün sayısı vermez; takip süresi sonradan seçilmemelidir.
- **Bizim nesnel olay:** Günlük iki sağ barla onaylı son pivot high `H1`/low `L1` kullanılır. `close>H1+0,1×ATR14_D` long ilk yapı kırılımı; sonraki en fazla **3 kapanmış günlük bar** içinde `close>break_close+0,5×ATR_D` gelirse takip teyidi. Bu olmadan **yeni long giriş yok**; short simetrik. Daha önce onaylanmış alt pivotun altına kapanış olursa kırılım anında iptal. 2 bar onayı, 0,1/0,5 ATR ve 3 gün bizim ön kayıt seçimimizdir. Kırılım barındaki pivot sağ teyit olmadan kullanılamaz.
- **İcra/risk:** Teyit kapanışı sonrası ilk uygulanabilir 1m; long stop dondurulmuş `L1−0,1×ATR`, short stop `H1+0,1×ATR`, 2R ve 7/14 gün süre kolları. Teyit barı fazla uzaklaşıp net ödül-risk <1 olursa atla. Aynı 1m stop önce, maliyet/funding dahil.
- **Karşılaştırma:** Mevcut BOS/kutu kırılımı ve üçgen kırılımı adaylarına karşı **3 gün içinde takip mesafesi** filtresinin ek faydasını, gecikme ve kaçırılan büyük hareketleri birlikte ölç. Kaynağın “hızlı gerçekleşen fikirler iyidir” yorumu tek başına kanıt değildir; teyit olmadan giriş yapılan kontrol aynı evrende kalmalı.

## 3. Order Block ve Fibonacci — Bheki Mpangane

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 6/Baskı 6/Order Block ve Fibonacci -  Bheki Mpanganeb (31 sayfa) - @eseckal.pdf>) · [Tam metin](03_ob_fib_mpanganeb.txt)

**Kaynak taraması:** PDF kapağında yazar Bheki Mpangane; dosya adındaki `Mpanganeb` yazımı aynen korunmuştur. S. 3–6 kurumsal/seans iddiaları; s. 7–12 **fitil yerine mum gövdelerinin** en alt/üstünden Fibonacci ve 0,618–0,79 OTE geri çekilmesi; s. 13–17 gün içi seans ve önceki high/low süpürmesi; s. 18–21 eski zirve/dip ve yuvarlak fiyat; s. 22–27 emir bloğu, kırılınca breaker ve “boşluk dolumu”; s. 28–31 garantisiz günlük gelir tablosu. 100→100.000 dolar planı gerçek getiri kaydı değildir. “Piyasa her zaman boşluk doldurur” ve kurum niyeti gözlemsel kural değildir. RSA/NY/Londra saatleri kripto günlük karara çevrilmedi.

### BM76 — Gövdeye sabitlenen 0,618–0,79 geri çekilme ve kapalı mum dönüşü

- **Kaynak kuralı:** Yönlü hareketin fitil değil **gövde uçları** arasında Fibonacci'yi dondur; boğa için 0,618–0,79 geri çekilme bandında alış, ayı için simetri (s. 7–8, 11–12, 17). Kitap intrabar limit emir ve seans kullanır; burada kapanmış günlük barla uyarlama yapılır.
- **Bizim nesnel kurulum:** Long için kapanmış günlük barda `close>prior20_high` ve önceki 10 günün en düşük **gövde altı** (`min(open,close)`) ile kırılım barının en yüksek **gövde üstü** (`max(open,close)`) arasındaki itkiyi dondur. Bu aralığın uzunluğu `≥2×ATR14_D`. Geri çekilme bandı `body_high−[0,79,0,618]×impulse`. Sonraki 1–10 kapalı günlük barda ilk `low≤band_upper` ve `close>band_upper`, ayrıca `low≥body_low` ise long tepki; short aynası. Pivot/itki aralığı, 2 ATR, 1–10 gün, kapanış tepkisi bizim seçimimizdir. Kurulum oluştuktan sonra Fib uçlarını **yeniden seçme**; future swing high'a bakma.
- **İcra/risk:** Tepki kapanışı sonrası ilk uygulanabilir 1m; long stop `min(retest_low,body_low)−0,1×ATR`, short tersi. 2R veya önceki dondurulmuş itki high/low hedefi, 7/14 gün süre. Hedef lehte/net ilk ödül-risk <1 değilse atla; aynı 1m stop önce, maliyet/funding dahil.
- **Karşılaştırma:** Önceki Fibonacci/pullback adaylarında wick uçlarıyla çizilmiş 0,618–0,79 bandı ve sıradan 0,5–0,618 bandıyla **aynı itki setinde** karşılaştır. Bu PDF'nin gerçekten ayrı testi gövde-uç sabitlemesidir. S. 22–27 OB/FVG fikirleri FTM73 ve eski OB/FVG kayıtlarıyla örtüşür; yeni bağımsız strateji sayılmadı.

## Ortak doğrulama

Kararlar yalnız kapanmış UTC günlük ve son tamamlanmış UTC haftalık barları kullanır. Sonraki uygulanabilir 1m dolum, point-in-time sembol evreni, eksik mum/veri gecikmesi, ücret/spread/kayma/funding ve aynı 1m stop önceliği zorunludur. Walk-forward, ayrı holdout, işlem örtüşmesi ve basit kontroller olmadan kârlılık iddiası kurulmaz. Mevcut pilotta eşdeğer feature varsa yeni kolon açılmaz.
