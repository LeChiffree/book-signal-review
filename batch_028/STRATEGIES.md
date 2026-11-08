# Kitap okuma 028 — kırılım denemesi, boyun çizgisi ve RSI kaynak sınırı

**Kapsam:** 209 + 16 + 6 = **231 PDF sayfası**. Her PDF'nin sayfa sıralı metni yan dosyalarda saklandı. Atıflar PDF sayfasıdır. Kaynakta olmayan sayısal eşikler aşağıda **bizim deney tasarımımız** olarak gösterilir. Backtest, paper test veya emir yapılmadı.

## 1. Grace Cheng — 7 Kazandıran Strateji

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 4/Baskı 4/7 Kazandıran Strateji - Grace Cheng (209 sayfa) - @eseckal.pdf>) · [Tam metin](01_seven_winning_cheng.txt)

Bu tam uzunluklu forex kitabının yedi yaklaşımı: piyasa duyarlılığı (PDF s. 60–76), trend sürüşü (s. 77–99), kırılımı ters yönde değerlendirme (s. 100–118), kırılım ticareti (s. 119–138), azalan volatiliteden kırılım (s. 139–158), faiz farkı/carry (s. 159–169) ve haber açıklaması çevresi işlemleri (s. 170–188). Forex COT, faiz ve ekonomik haber yaklaşımları kripto OHLCV'sinden üretilemez; ayrı nokta-zaman veri kaynağı gerekir. Kâr iddiaları ve grafik örnekleri kanıt sayılmaz.

### G28a — Daralan üçgende ilk kırılım girişimini atlama

- **Kaynak:** Azalan volatilite ve üçgen (s. 145–152). Üçgenin iki tarafında en az ikişer temas, ilk kırılım girişimini dikkate almama; sonraki kırılımı bekleme (s. 153–157). Yükselen/alçalan üçgende beklenenin tersi yöndeki kırılım için yarım büyüklük önerisi (s. 154–156). İsteğe bağlı EMA yataylaşması/Bollinger daralması (s. 157). Kaynak hedefi nesnel sabit bir ölçüyle vermez.
- **Bizim D1 olay tanımı:** Önceki 20–40 tamamlanmış D1 mumda iki sağ mumla **teyit edilmiş** en az iki pivot tepe ve iki pivot dip. Her iki sınır, o anda bilinen son iki pivot üzerinden doğrusal uzatılır; sınırların giriş anındaki farkı pozitif, başlangıçtaki farkından daha dar ve son 10 D1 barın realized range'i önceki 10 barınkinden küçük. İlk sınır dışı D1 kapanışı `>=0.1 ATR14_D1` taşma ancak sonraki 3 D1 içinde üçgen içine dönüş = **başarısız ilk deneme**. Sonra en fazla 10 D1 içinde aynı/karşı sınır dışı yeniden kapanış olursa sonraki ilk 1m'de yönünde giriş; stop en son teyitli karşı pivotun `0.1 ATR` dışı, hedef 2R/H7D. İki tarafın her birine ikişer temas koşulu, temasların kapanmış pivotlarda olmasıyla sağlanır. `20–40`, ATR, pencereler, range ve hedef bizim sabit varsayımlarımızdır.
- **Karşılaştırma:** Aynı üçgenlerde ilk kırılımı alan kol ile yalnız ikinciyi alan kol; sinyal başına kaçan dolum ve net sonuç. Üçgenin tipi ve beklenen/yaygın olmayan yön sınıflanır; yarım pozisyon varyantı ayrı risk deneyidir. Önceki üçgen/breakout aileleriyle olay eşleştirilir; yeni bağımsız formasyon sayılmaz. İlk denemenin “başarısızlığı” ancak dönüş kapanışı sonrası bilinir, ilk kırılım anına geri yazılmaz.

### G28b — Yatay rejimde başarısız kırılımı ters yönlü kullanma

- **Kaynak:** Sahte kırılımlar önceki gün uçları, destek/direnç ve formasyon boyunlarında görülebilir; yazar özellikle yatay piyasada kırılımı ters yönde değerlendirir (s. 106–107, 115–118). Güçlü momentumla yaklaşan seviyede ters işlemden kaçınma fikri s. 107'de. Kitap tek bir evrensel giriş kuralı vermez.
- **Bizim D1 deney:** Önceki 20 tamamlanmış D1 için `R=max(high),S=min(low)`; range `<=6 ATR14_D1`, `abs(EMA20[t]-EMA20[t-10])<=0.5 ATR` yatay rejim. Tamamlanmış D1 `high>R+0.1 ATR` ve `close<R` ise üst sahte kırılım sinyali; sonraki ilk 1m short, stop sinyal barı tepesi `+0.1 ATR`, hedef kutu ortası ve 2R ayrı, H3D çıkışı. Alt taraf simetrik. Kırılım barı range'i `>1.5 ATR` veya hacmi son 20 günlük medianın `>2×` ise **hızlı yaklaşım** filtresi ayrı varyant; kaynak bu eşikleri vermez.
- **Karşılaştırma:** Aynı aralık ucu olaylarında kırılım yönünde giriş, ters yönde giriş ve işlem yok; yatay rejim filtresi var/yok. Önceki false breakout/likidite süpürmesi adaylarıyla çakışma işaretlenir.

## 2. Alan Farley — 3 Swing Trading Örneği

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 3/Baskı 3/3 Swing Trading Örneği (16 sayfa) - @eseckal.pdf>) · [Tam metin](02_three_swing_examples.txt)

Bu **üç tarihli hisse senedi vaka anlatımı ve terim sözlüğü**; üç eksiksiz, bağımsız mekanik sistem değildir (s. 2–9, 10–16). AMZN örneğinde kısa üçgen/kupa-kulp/çift dip ve SMA200 direnci (s. 2–5); NVDA örneğinde başarısız kırılım ve gap (s. 5–6); ALKS örneğinde baş-omuz, boyun kırılması veya ilk geri dönüşte short, ölçülen hareket ve iz süren stop (s. 7–9). Şirket haberi, hisse gap'i ve 2001 fiyat seviyeleri kriptoya taşınmaz.

### F28 — Baş-omuz boyun kırılımı: hemen mi, ilk retestte mi?

- **Kaynak:** ALKS baş-omuzda baş ile boyun yüksekliği kadar ölçülen aşağı hedef; boyun kırılımı veya ilk geri çekilmede short; hedef garanti değil, trailing stop kullanılabilir (s. 8–9). Kaynağın üç omuz/pivot çizimi karar anında objektif tanımlanmış değildir.
- **Bizim D1 deney:** Önceki 90 D1 içinde iki sağ barla teyitli ardışık tepe `LS,H,RS`, `H>LS` ve `H>RS` en az `0.5 ATR`, `abs(LS-RS)<=1 ATR`; aradaki iki teyitli dipten boyun doğrusu çizilir. RS teyit edildiğinde önceki bilgiyle boyun seviyesi sabitlenir. `close_D1<neckline[t]-0.1 ATR` ilk kırılım ise kol A sonraki ilk 1m short. Kol B sonraki 3 D1 içinde `high>=neckline` ve `close<neckline` ilk retest kapanışından sonra ilk 1m short; retest yoksa işlem yok. Stop RS tepesi `+0.1 ATR`, hedef `neckline_at_break-(H-neckline_at_H)` sadece girişin altında kaldığında veya 2R ayrı; H7D çıkışı. Bütün pencere ve toleranslar bizim hipotezlerimiz.
- **Karşılaştırma:** Aynı boyun olaylarında hemen/retest, tamamlanmayan retest sayısı, hedefe mesafe, maliyet sonrası sonuç. Önceki baş-omuz/kırılım adayıyla birleştirilir; aynı olaya iki kez kazanç yazılmaz.

## 3. 7 RSI Trade Stratejisi

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 7/Baskı 7/7 RSI Trade Stratejisi (6 sayfa) - @eseckal.pdf>) · [Tam metin](03_seven_rsi.txt)

Bu altı sayfalık PDF **bir web yazısının bağlantılı özeti**. RSI2, RSI+S/R, RSI ayrışması+mum, RSI50, failure swing, RSI trend çizgisi ve RSI range shift adlarını sayıyor (s. 1–5), fakat çoğunda eşik, giriş, stop ve çıkış kuralını vermez; ayrıntı harici bağlantılarda. S. 1 mekanik uygulanınca kârlı olmalarının olası olmadığını açıkça söyler. Bu nedenle yedi hazır strateji olarak kuyruklanmadı.

### R28 — RSI50 rejim filtresi; mevcut sinyal ailelerinde ablation

- **Kaynak:** RSI50 üstü yükseliş, altı düşüş rejimi gözlemi (s. 4). RSI2 ve ayrışma+mum fikirleri (s. 2–3) önceki partilerde zaten ayrı olay aileleri.
- **Bizim D1 test:** Wilder RSI14 yalnız tam kapanmış D1. Mevcut `P26a` teyitli mum ve `G28a` üçgen olaylarında long için `RSI14[t]>50`, short için `<50` filtresi; RSI50 olmadan aynı sinyallerle paired karşılaştırma. Yalnız gün `t` RSI'si karar anında kapanmışsa kullanılır. Filtreden başka yeni giriş/stop/çıkış sütunu yaratılmaz; mevcut stratejilerin kuralları korunur.
- **Ertelenen:** Failure swing ve aralık kayması için bu PDF gerekli eşikleri vermiyor. İlgili özgün kaynaklar ayrıca okunmadan “kaynak kuralı” diye kodlanmaz.

## Öncelik ve test kapıları

G28a'daki **ilk başarısız deneme sonrası ikinci kırılım** ayrımı mevcut üçgen deneylerine anlamlı bir ek hipotezdir. F28 doğrudan boyun kırılımına karşı retesti aynı olaylarda kıyaslar. R28 filtre olarak sınanır. Tamamında point-in-time evren, teyitli pivotun geç öğrenilmesi, tamamlanmış mum, sonraki 1m dolum, ücret/spread/kayma/funding, aynı 1m mum stop önceliği ve zaman sıralı dış örneklem gerekir. Kitaptaki tarihli örnekler veya “kazandıran” başlığı başarı kanıtı değildir.
