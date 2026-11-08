# Kitap okuma 159 — Jenkins, Byeajee ve Elder

Üç ayrı PDF'nin **132 + 37 + 72 = 241 sayfası** sırayla metne çıkarılıp incelendi. PDF sayfaları atıf düzeyidir. **Yeni bağımsız strateji adayı: 1.** Henüz backtest, paper test veya emir yapılmadı.

## 1. Basitleştirilmiş Günlük Trading Teknikleri — Michael S. Jenkins

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Basitleştirilmiş Günlük Trading Teknikleri - Michael S. Jenkins (132 sayfa) - @eseckal.pdf>) · [tam metin](01_jenkins_day_trading.txt)

**Tarama:** s. 1–19 trend, zaman dilimi ve iki bar geriye stop; 20–37 ölçülü hareket, karekök oranları ve açı ölçekleri; 38–64 işlem planı, önceki gün aralığı, opsiyon vadesi ve hacim; 65–84 piyasa oyuncuları, kısa süreli kırılım ve kanal/bayrak; 85–103 zaman döngüsü ve kareler; 104–128 açı projeksiyonu ve zaman dönüşüm çubuğu; 129–132 işlem özeti.

**Karar:** s. 12–17 önceki iki barın alt/üst ihlali ile trend/stop okuması önceki iki bar kırılımı ve çoklu zaman dilimi aileleriyle örtüşür. s. 44–47 önceki gün aralığı örtüşmesi ve s. 71–77 kanal/bayrak kırılımı da mevcut kırılım/geri çekilme adaylarının varyantlarıdır. s. 25–37 ve 85–128 karekök açı, başlangıç pivotu ve fiyat/zaman ölçeğine duyarlıdır; seçilmiş grafiklerle isabet iddiası ileriye dönük kanıt değildir. s. 53–60 kurumsal işlem niyeti ve opsiyon pozisyonları yalnız OHLCV'den güvenilir biçimde çıkarılamaz; bazı dönemsel piyasa/yasa ifadeleri bugünün kuralı olarak alınmadı. **Yeni bağımsız aday yok.**

## 2. 200 Kısa Trading Psikolojisi — Yvan Byeajee

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/200 Kısa Trading Psikolojisi - Yvan Byeajee (37 sayfa) - @eseckal.pdf>) · [tam metin](02_trading_psychology_byeajee.txt)

**Tarama:** s. 1–5 giriş; 6–22 iki yüz kısa psikoloji notu; 23–37 kişisel deneyim, davranış ve işlem planı. Kayıptan sonra aceleyle pozisyon büyütmeme (s. 6), işlem öncesi risk planı ve kurala uyma (s. 7–10), sonuç/karar günlüğü (s. 14–18), stratejiyi önce test etme (s. 17) yararlı **proses kontrolleridir**. Yön, eşik, giriş ve çıkış beraber tanımlanmadığı için bağımsız fiyat sinyali sayılmadı. **Yeni aday yok.**

## 3. Adım Adım Trade — Alexander Elder

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Adım Adım Trade - Alexander Elder (72 sayfa) - @eseckal.pdf>) · [tam metin](03_step_by_step_elder.txt)

**Tarama:** s. 1–13 risk sınırı ve işlem kaydı; 14–23 grafik aracı/çoklu zaman dilimi; 24–41 EMA, Keltner, MACD ve Force Index; 42–45 Impulse renk filtresi; 46–53 haftalık rejim, günlük geri çekilme ve sahte kırılım; 54–56 Kerry Lovvorn'un dip fiyat EMA8 sistemi; 57–64 işlem örnekleri; 65–69 ATR stopu/günlük; 70–72 kaynakça ve sonuç. s. 47–53 çoklu zaman dilimi trend/geri çekilme ile MACD uyumsuzluğu önceki aday aileleriyle büyük ölçüde örtüşür. s. 43–45 Impulse kitabın kendisinin dediği gibi yalnız **yasak filtresidir**, bağımsız giriş sinyali değildir.

### EL159A — Dip fiyatın EMA8'i altında üç bar, üstünde kapanış

- **Kaynak kuralı:** s. 54–56: Kapanış EMA'sı yerine her çubuğun **low** değerinden EMA8 hesaplanır. Fiyat iki bardan fazla bu çizginin altında işlem gördükten sonra çizginin üstünde kapanırsa al; kapanış EMA8(low) altına inerse sat. Kaynak bunu gün sonunda izlenen, long yönlü ve 10–20 barlık kısa trendleri hedefleyen sistem olarak sunar. Girişte koruyucu stop, eşik tamponu ve azami bekleme kitabın bu bölümünde verilmez.
- **Ön kayıtlı olay:** BTCUSDT ve ETHUSDT spot, UTC D1 kapalı mum. `E_t = EMA8(low)_t`; gösterge için en az 30 önceki tam D1 mum gerekir. t−3, t−2, t−1 günlerinin her birinde `low_i < E_i` ve t gününde `close_t > E_t` ise long tetik. "İki bardan fazla"yı üç **ardışık** bar ve `low` ihlali olarak sabitlemek bizim seçimimizdir; `close_i<E_i` sıkı varyantı ayrıca incelenir. Kaynak üç barın ardışık olmasını söylemez. Yalnız ilk uygun tetik, pozisyonda iken yeni sinyal yok.
- **İcra ve risk:** Tetik kapanışından sonraki ilk uygulanabilir 1m açılışta long. Koruyucu stop `min(low_{t-3:t}) − 0,1 × ATR14_D1(t)`; işlem başına özsermayenin %0,25'i risk, kaldıraç yok. Girişten sonraki ilk D1 `close < EMA8(low)` olduğunda sonraki ilk uygulanabilir 1m'de çık; en çok 20 D1 sonra süre çıkışı. Stop gün içinde çalışır; aynı 1m içinde stop ve olası çıkış çakışırsa stop önce. Giriş gününün t mumuna ait EMA/ATR yalnız t kapanınca hesaplanır; hiçbir intrabar t verisi sinyal öncesi kullanılmaz. Stop tamponu, 20 gün sınırı ve risk boyutu **bizim test tanımımızdır**.
- **Karşılaştırma/ret ölçütü:** Aynı dönem/veri/masrafla standart `EMA8(close)` geri kazanımına ve basit 2-bar dönüşe karşı ölç. Komisyon, spread ve kayma dahil net R, işlem sayısı, 10/20 gün medyan getirisi, maksimum düşüş, BTC/ETH ve dönem dışı ayrımı, `low`/`close` alt koşulu ve EMA uzunluğu 6/8/10 duyarlılığı raporlanır. Masraf sonrası net sonuç ve dönem dışı istikrar yoksa aday reddedilir. Kaynak, kârlılığa dair doğrulanmış performans serisi sunmaz.

**Parti sonucu:** 3 kitap, 241 sayfa, 1 yeni aday. Birikmiş toplam **391 doğrulanmamış strateji adayı**.
