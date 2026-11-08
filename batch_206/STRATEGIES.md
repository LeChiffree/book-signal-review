# Kitap okuma 206 — Price is Everything, volatil piyasalar ve Forex başlangıcı

Üç daha önce tamamlanmamış PDF'nin **747 sayfası** sayfa bazında metne çıkarılıp tarandı; kural sayfaları ayrıca incelendi. **Yeni bağımsız, henüz doğrulanmamış kapalı mum stratejisi adayı: 0.** Backtest, paper test veya emir yapılmadı. Sayılar PDF sayfasıdır.

## 1. Price is Everything — Orijinal Kaynak (392 sayfa)

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 10/Baskı 10/Price is Everything - Orijinal Kaynak (392 sayfa) - @eseckal.pdf>) · [tam metin](01_price_is_everything.txt)

**Tam tarama:** S. 1–4 derleme açıklaması ve içerik; 5–118 arz/talep, yutma mumu ve ilk Forex örnekleri; 119–248 seviye, Fibonacci, momentum ve çoklu zaman dilimi grafikleri; 249–370 devam eden işlem/grafik günlüğü; 371–392 arz bölgesine yaklaşırken sıkışma ve sonuç örnekleri. Derleyici s. 3–4'te belgenin esas olarak seçilmiş grafiklerden oluştuğunu söylüyor. S. 5, 8–10'daki ana olay destek/direnç veya arz/talep alanında yutma/whipsaw dönüşü. S. 379–382'de fiyat arz bölgesine yükselirken aşağı fitilli ardışık baskılarla alt talebin tüketildiği, ardından arzdan aşağı dönüş anlatılıyor. Bu, önceden kaydedilen [arz/talep bölgesine sıkışmalı yaklaşma filtresi](../batch_058/STRATEGIES.md) ile aynı hipotez ailesidir; [yutma teyidi](../batch_005/STRATEGIES.md) de daha önce tanımlandı. S. 109'da bölgeyi nesnel çizme talebi forumda da açık kalıyor; bu PDF birim sayısı, sınır toleransı ve stop/iptal için tek tutarlı kural sağlamıyor. Mevcut FL58 adayı üzerinde “aşağı fitilli yükseliş” gibi bir alt grup ancak önceden tanımlı eşikle karşılaştırılabilir; aynı dönüşleri ikinci bir bağımsız kazanç serisi saymadık. **Yeni aday: 0.**

## 2. Guy Cohen — Basitleştirilmiş Volatil Piyasalar (312 sayfa)

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 11/Baskı 11/Basitleştirilmiş Volatil Piyasalar - Guy Cohen (312 sayfa) - @eseckal.pdf>) · [tam metin](02_volatile_markets_cohen.txt)

**Tam tarama:** S. 1–33 opsiyon temelleri ve risk; 34–63 trend, boğa/ayı bayrakları, fincan-kulp ve hisse girişi/çıkışı; 64–99 opsiyon Yunanları; 100–140 straddle/strangle; 141–231 oranlı geri yayılım ve diyagonal spread; 232–270 pratik seçim, volatilite ve fiyatlama; 271–300 işlem planları/örnekler; 301–312 kapanış/ekler. S. 43–47 bayrak üst/alt sınırının kırılmasını giriş, karşı sınırı stop; s. 48–55 ilk dürtü uzunluğundan hedef ve kısmi çıkış; s. 56–57 dolmayan emirlerin işlem sayılmaması anlatılır. Bu, [bayrak/flama](../batch_016/STRATEGIES.md) ailesinin kâr yönetimi varyantıdır; kitap s. 52 trend çizgisinin çiziminde takdir payını açıkça belirtir. S. 271–281'de aynı boğa/ayı bayraklarına örnek işlem planı verilir, yeni yön olayı yoktur.

S. 100–140 straddle/strangle; 141–231 oranlı geri yayılım ve diyagonal spread; s. 282–296 bunların kazanç duyurusu, vade ve strike ile örnek uygulamalarını verir. Bu stratejilerin oluşumu/mark-to-market hesabı için tarihsel **opsiyon zinciri, bid/ask, implied volatility, strike, vade, şirket olayı ve kontrat şartları** gerekir. Yalnız kapalı hisse/FX mumlarından aynı pozisyon ve P&L hesaplanamaz. S. 283–289'daki seçilmiş yüksek getiri örnekleri strateji üstünlüğü kanıtı değildir. Opsiyon stratejileri “mum stratejisi adayı” sayılmadı; daha sonra opsiyon veri evreni kurulursa ayrı proje olarak değerlendirilebilir. **Yeni kapalı mum adayı: 0.**

## 3. Marc Stuart — Yeni Başlayanlar İçin Forex (43 sayfa)

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 10/Baskı 10/Yeni Başlayanlar İçin Forex - Marc Stuart (43 sayfa) - @eseckal.pdf>) · [tam metin](03_forex_marc_stuart.txt)

**Tam tarama:** S. 1–25 Forex işleyişi, kaldıraç ve platform; 26–29 MA, RSI ve Fibonacci; 30–32 kısa strateji özetleri; 33–43 plan, risk, hatalar ve SSS. S. 30 günlük merkezi pivot ile önceki günün %38/%50/%68 Fibonacci seviyesinin birleşmesini tarif eder, fakat “son birkaç günün ATR'si önceki kapanışı aşsın” ifadesi fiyat birimi ve kıyas bakımından sorunludur; pivot toleransı, teyit mumu, stop ve çıkış sabit değildir. Bu, mevcut [Fibonacci/pivot yakınsaması](../batch_012/STRATEGIES.md) ailesinin belirsiz varyantıdır. S. 31 hızlı/yavaş stochastic için dönemler `(21,4,10)` ve `(5,2,2)` verilir; “zıt uçlar” ve mum teyidi yön/sıra açısından tam tarif edilmez. Bu, önceki [çift stochastic](../batch_152/STRATEGIES.md) çalışmalarına parametre varyantı olabilir; seçim sonuca bakılarak yapılmamalı. S. 32 BB dış bant dönüşü ve Londra çekiç/ret mumu önceki bant dönüşü ve seans kırılımı aileleridir. Başarı iddiaları işlem dökümü içermez. **Yeni aday: 0.**

**Parti sonucu:** 3 PDF, **747 sayfa**, **0 yeni doğrulanmamış aday**. Kümülatif **618 PDF, 42.864 sayfa, 441 doğrulanmamış aday**.
