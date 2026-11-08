# Kitap okuma 030 — açılışta göreli gecikme, M5 EMA scalp ve strateji elemesi

**Kapsam:** 227 + 8 + 24 = **259 PDF sayfası**. Üç PDF'nin sayfa sıralı tam metni bu klasördedir. Sayfa atıfları PDF sayfasıdır. Aşağıda kaynakta yazan kural ile bizim sınanabilir varsayımımız ayrılmıştır. Backtest, paper test veya emir yapılmadı.

## 1. Jeremy Russell — 20 Dakikalık Trader Olmanın Yolları

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 24/Baskı 24/20 Dakikalık Trader Olmanın Yolları - Her Piyasadaki Tüm Yatırımcılar İçin Vazgeçilmez Bir Rehber - Jeremy Russell (227 sayfa) - @eseckal.pdf>) · [Tam metin](01_twenty_minute_trader.txt)

### R30 — ABD açılışında endekse göre geciken hisse

- **Kaynak:** ABD hisse piyasasının ilk 20 dakikasında (09:30–09:50) bir saniyelik hisse ve Dow çizgi grafikleri ile kısa U dönüşleri izlenir (s. 98–109). Örnekte hisse ve Dow yaklaşık 10 saniye birlikte düşer; Dow yükselirken hisse yaklaşık 10 saniye yatay/gecikmiş kalır; hisseyi yakalama beklentisiyle **call opsiyonu** alınır (s. 109–110). Çıkış, iki grafiğin birlikte düşmesi veya dayanak hisse fiyatında gözlenen koşullara göre stop ile yapılır; 13 sentlik tampon belirli örneğe aittir, genel eşik değildir (s. 109–111). İşlem ücretleri brüt kazancı silebilir (s. 62).
- **Mevcut araştırmaya uygunluk:** Bu, D1/M1 kapanışlı kripto bar stratejisi değildir. Sinyalin kendisi saniyeler içinde oluşur; opsiyon alış/satış fiyatı, bid/ask, likidite, grekler ve ücret gerekir. M1 mumlarından saniyelik sıra ve fiili opsiyon dolumu geri kurulamaz. Bu yüzden mevcut kripto backtest kuyruğuna **kaynak stratejisi** olarak eklenmedi.
- **Gelecekte ayrı test sözleşmesi:** Eşzamanlı, zaman damgası denetlenmiş hisse/endeks 1s veya tick akışı ve tarihi opsiyon kotasyonları temin edilirse; yalnız 09:30–09:50 ET, geçmiş saniyelerde birlikte düşüş ve endeks toparlanırken hissenin yerinde kalışı olayları, sonraki kotasyonda uygulanabilir call alış/çıkış, spread ve ücretle sınanmalı. `U`, “yatay” ve “toparlanma” eşikleri yalnız eğitim döneminde belirlenmeli; hisse seçimi ve opsiyon vadesi/grevi olaydan önce sabitlenmeli. Grafiklere sonradan bakıp şekil seçmek ileriye bakma hatası yaratır.
- **Olası kripto benzeri:** BTC'nin altcoine saniyelik öncülüğü ayrı bir **bizim hipotezimizdir**; Russell'ın hisse–Dow call yönteminin testi diye raporlanamaz. Mevcut M1 veriyle saniyelik üstünlük iddiası kurulmaz.

## 2. 5 Dakikalık Scalp Stratejisi

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/5 Dakikalık Scalp Stratejisi (8 sayfa) - @eseckal.pdf>) · [Tam metin](02_five_minute_scalp.txt)

### S30a — EMA10/21 orta noktasına trend yönünde ilk geri çekilme

- **Kaynak:** EUR/USD M5 üzerinde EMA10, EMA21, EMA50; EMA50'nin eğimi ve yeni yüksek zirveler/düşük dipler yönü belirler. Fiyat EMA10 ve EMA21 **orta noktasına** gelince trend yönünde giriş, 5 pip + spread stop, 10 pip + spread hedef (s. 1–4). Yeni yüksek zirve yoksa veya EMA50 yataylaşmışsa giriş reddedilir (s. 4). Londra/New York açılışları önerilir, Asya seansı önerilmez (s. 2); geniş spread uyarısı s. 8. Günlük pip/kârlılık sözleri doğrulanmış performans değildir.
- **Bizim kripto M5 deneyimiz:** Yalnız likit, önceden sabitlenmiş semboller. Tam kapanmış M5 `t-1` itibarıyla long için `EMA50[t-1]>EMA50[t-6]` ve son iki **teyit edilmiş** pivot tepesinde artış (pivot sağ onayı sinyalden önce bitmiş olmalı); short simetrik. Önceden bilinen `mid[t-1]=(EMA10[t-1]+EMA21[t-1])/2`. M5 `t` içinde long `low[t]<=mid[t-1]` ve `close[t]>mid[t-1]`; short `high[t]>=mid[t-1]` ve `close[t]<mid[t-1]`. Sinyal ancak `t` kapanınca, giriş sonraki ilk 1m uygulanabilir fiyatında. Yatay EMA50 eşiği, pivot genişliği ve dokunma toleransı eğitim döneminde sabitlenir. Bunlar kaynakta sayısallaştırılmamıştır.
- **Risk/çıkış uyarlaması:** Kaynaktaki pip büyüklüğü kriptoya taşınmaz. Stop mesafesi için önceden kapanmış `ATR14_M5`'in seçilmiş kesri ve asgari uygulanabilir spread/ücret eşiği eğitimde sabitlenir; hedef **brüt 2R** ilk kaynak 5:10 oranını temsil eder. Stop ve hedef aynı M1 barda görülürse stop önce sayılır; 20 dakika azami elde tutma kaynakta tipik süre olarak geçer (s. 1), deneyde ayrıca açık bir çıkış varyantı olarak test edilir. Seans filtresi kriptoya doğrudan aktarılmaz; UTC saat dilimi koşulsuz/koşullu karşılaştırılır.
- **Karşılaştırma:** Önceki EMA10/21 **bölge** geri çekilmesiyle (batch025) aynı olaylarda orta nokta şartının ek sinyal değeri; filtreli/filtersiz ve işlem maliyeti sonrası paired ölçüm. Aynı trendde ardışık girişler bağımsız örnek diye sayılmaz.

### S30b — İlk sinyalde runner çıkışı

- **Kaynak:** Tek trendde yalnız ilk giriş; +10 pipte stop başabaşa; sonra EMA50 yataylaşınca veya ters döndüğünde çıkış (s. 6–7).
- **Bizim çıkış ablatif deneyi:** S30a'nın aynı ilk giriş havuzu ve ilk riski. +2R'ye ulaştığı **kapanmış M1 barı sonrasında** stop, işlem maliyetini içeren başabaş seviyesine çekilir; stopun aynı bar içinde önce mi sonra mı görüldüğü lehimize varsayılmaz. İlk kapanmış M5'te EMA50 eğimi yatay eşik altına düşünce çıkış; ters eğim ayrı varyant. Azami süre önceden sabitlenir. S30a sabit hedefiyle aynı girişlerde net getiri, kuyruk kaybı ve fırsat maliyeti karşılaştırılır.

## 3. 15 Dakikada Forex Kursu

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 4/Baskı 4/15 Dakikada Forex Kursu (24 sayfa) - @eseckal.pdf>) · [Tam metin](03_fifteen_minute_forex.txt)

Metin çoğunlukla forex tanıtımı ve dönemin platform/kopya işlem anlatımıdır (s. 2–5, 10, 14–19). Eylül 2011 EUR/USD olayı (s. 9) tekrar üretilebilir giriş–stop–çıkış kuralı vermez. Farklı zaman dilimlerini birlikte inceleme tavsiyesi (s. 12) mevcut sinyallerde yalnız **filtre deneyi** fikridir; hangi yön, eşik ve zamanlama olacağı bizim tanımımızı gerektirir. Bu kitaptan bağımsız yeni işlem sinyali kaydedilmedi.

**Kullanılabilir denetim:** Yüksek kazanma oranının açıkta tutulan zararı gizleyebileceği uyarısı (s. 23) nedeniyle gelecekteki backtest/paper raporunda gerçekleşmiş ve gerçekleşmemiş P&L, açık pozisyon yaşı, stop bulunmayan işlemler, maksimum düşüş ve sonlandırma kuralı ayrı gösterilmeli. Kopya işlem performansı veya pazarlama örnekleri strateji kanıtı değildir.

## Sonraki çalışma sırası

S30a, mevcut M5 EMA bölge adayından gerçekten farklı sinyal üretip üretmediği ve maliyet sonrası uygulanabilirliği için ilk adaydır; S30b aynı girişlerin çıkış varyantıdır. R30 veri gereksinimi sağlanana kadar ertelenir. Üçüncü kitap yeni sinyal vermedi. Herhangi bir kârlılık sonucu ileri sürülmez; backtest ve paper test kullanıcı istediğinde ayrı sonuç dosyasına yazılır.
