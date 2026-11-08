# Kitap okuma 013 — Hacimli kırılım, teyitli retest ve MACD–Bollinger

**Kapsam:** Üç PDF'nin **140 + 53 + 80 = 273 PDF sayfası** sayfa sırasıyla işlendi. Kaynak sayıları PDF sayfasıdır. Bunlar uygulanabilir **test hipotezleri**; kitap örnekleri ve kâr iddiaları doğrulanmış sonuç değildir. Bu partide backtest, paper test ve emir yok.

## 1. Pankaj Ladha ve Anant Ladha — 13 Swing Trading Stratejisi

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 9/Baskı 9/13 Swing Trading Stratejisi - Pankaj Ladha ve Anant Ladha (140 sayfa) - @eseckal.pdf>)

Kitap 13 başlık içeriyor (s. 32–33): hacim patlaması (s. 37–40), dar aralık sonrası kırılım (s. 43–48), 10/20/50 EMA'ya geri çekilme (s. 50–56), halka arz (s. 61–70), iki buçuk günlük satıştan dönüş (s. 71–75), MA kesişimi (s. 77–80), bilanço sonrası hareket (s. 83–95), piyasa karşısında göreli güç (s. 96–100), short squeeze (s. 104–110), ortalamaya dönüş (s. 110–115), yatay destek/direnç (s. 116–120), OFS/blok işlemler (s. 123–127), sektör rotasyonu (s. 128–132). Birçoğu Hindistan **hisse senedi**, seans, halka arz veya bilanço verisine özgü. Kaynaktaki Rs. 300, Rs. 1 crore likidite ve Nifty teyidi kripto fiyatlarına doğrudan uygulanmaz. “Büyük oyuncu alımı”, squeeze sebebi ve sektör anlatımı yalnız OHLCV ile gözlenmiş gerçek değildir.

### L13a — Dar aralıktan hacimli günlük kırılım

- **Kaynak çekirdeği:** 10/20 günlük tepe kırılımı, 10/20 EMA çevresinde daralma, yükselen trend ve yüksek hacim (s. 37–39, 43–45). Hacim patlaması için günlük ortalamanın yaklaşık 10 katı örneği s. 38'de var; bunun istikrarlı optimum olduğu gösterilmiyor. Stopun kırılım gününün dibi olması fikri s. 67'de halka arz bağlamında geçer, bu yüzden burada bizim uyarlamamızdır.
- **Bizim D1 sözleşmesi:** Her UTC günlük kapanışında `close[t] > max(high[t-20:t-1])` ve `close[t]>EMA20[t]`; son **10 tam günün** `max(high)-min(low)` aralığı `<= median(last 60 full daily ranges) × 3` ise daralma. Bu eşik bizim ön tanımımız. Önceki 20 tam gün medyan hacmine göre `volume[t]/median(volume[t-20:t-1]) >=2` filtresi ayrı; kaynak `10×` eşiği ayrıca yüksek hacim alt grubu. Giriş ertesi gün ilk yürütülebilir 1m; stop sinyal gününün low'u `-1 tick`, hedef 2R/3R ve 5/10/20 gün zaman çıkışı ayrı. Sinyal mumunun `high` değerini kırılım sınırı için kullanma; 20 gün tepesi sinyal kapanmadan sabit olmalı. Aynı olay batch 002/006 kırılım ailesiyle birleştirilir; hacim ve daralma ilavesinin marjinal değeri ölçülür.

### L13b — Yükselen EMA'ya geri çekilmeden toparlanma

- **Kaynak:** 10, 20, 50 günlük EMA'ya geri çekilmeyi güçlü ana trendde alım adayı sayıyor (s. 50–54). Tam kapanış/fitil eşiği yok.
- **Bizim D1 olay:** `EMA50[t-1]>EMA50[t-6]`, `close[t-1]>EMA50[t-1]`; gün `t` için `low[t]<=EMA20[t-1]` ve `close[t]>EMA20[t-1]` ve `close[t]>open[t]`. Alternatif temas EMA10/EMA50 ayrı etiket; sinyal kapanışından sonra giriş. Stop `low[t]-1 tick`, hedef 2R/3R veya 10 günlük tepe; 10 günlük tepe girişin yanlış tarafındaysa hedef varyantı atılır. EMA'nın **önceki kapanmış gün** değeri destek referansıdır. Batch 004 trend/MA ve batch 006 swing geri çekilme ile aynı pozisyonlar çift sayılmaz.

### L13c — Piyasa karşısında göreli güç, seçim filtresi

- **Kaynak:** Son 1–6 ayda piyasadan daha güçlü hisse, 50 günlük tepe ve EMA desteği (s. 96–100). Bu bir emir kuralından çok seçim yöntemidir.
- **Bizim evren filtresi:** Yalnız ilgili gün mevcut ve likit kripto evreni; `RS20 = coin'in son 20 tam UTC gün net getirisi - BTC'nin aynı günler getirisi`. Geçmiş 20 günlük RS20 üst çeyreğinde olan coinlerde L13a/L13b olaylarını ayrıca değerlendir. Alt çeyrek karşılaştırması ve evrende listeden düşen coinler korunur; gelecekteki listeyle geçmişi seçme. BTC karşılaştırması **bizim** kripto uyarlamamız. Hacim eşiği ve işlemin maliyeti coin bazında önceden tanımlanmalı.

**Ertelenenler:** Halka arz, bilanço, OFS/blok ve sektör verileri kripto OHLCV ile temsil edilmez. İki buçuk gün ve short squeeze seans/float varsayar. 10/20 MA kesişimi ve yatay destek/direnç önceki parti adaylarının kopyası olabilir; yeni strateji sayılmadan olay örtüşmesi ölçülür. Kitabın s. 138'deki yıllık getiri iddiası dayanak veri olarak alınmaz.

## 2. Mr. Ankya — 15 Price Action Stratejisi

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 9/Baskı 9/15 Price Action Stratejisi - Mr. Ankya (53 sayfa) - @eseckal.pdf>)

Başlıklar farklı olsa da temel akış tekrar eder: önceden çizilen destek/direnç veya boyun çizgisi kırılır, **retest ve yönlü kapanış** beklenir, stop son swing ötesi, hedef 2R/3R (s. 3–10, 17–23, 32–35). Çift dip/tepe (s. 7–8, 17–19, 27–30), üçgen (s. 9–10, 39–40), kama (s. 34–35), düşen bayrak (s. 42–43) bu akışın bağlam etiketleridir. Bazı örnekler gap ve elle çizilen seviye içerir; hiçbir grafik kâr oranı kanıtı değildir.

### A13 — Önceden bilinen sınırın kırılım–retest–teyit dizisi

- **Seviye seçimi:** Bu kaynaktaki serbest çizgiyi test edilebilir kılmak için son **20 tamamlanmış H1** yüksek/düşük sınırları sinyalden önce dondurulur. Long seviye `R=max(high[t-20:t-1])`; short `S=min(low[t-20:t-1])`. Kaynakta 20 bar yok; bizim sabit sözleşmemiz. PDH/PDL alternatif seviyeleri ayrı etiket, aynı olaya ikinci işlem değil.
- **Kırılım:** H1 long `close[t]>R+0.1 ATR14_H1[t-1]`, short `close[t]<S-0.1 ATR`. Sonraki en çok 8 H1 içinde ilk retest: long `low<=R+0.1 ATR` ve `close>=R`; short simetri. Ardından en çok 2 H1 içinde ilk yönlü `close>open && close>high[retest]` (short `close<open && close<low[retest]`). Bu **tam kapanış** sonrası ilk 1m giriş. `0.1 ATR`, 8/2 bar ve kesin teyit bizim seçimlerimiz; kaynak sadece retest/ters mum ister (s. 3–4, 8–10, 20–21, 34–35).
- **Risk/çıkış:** Long stop `min(low[break:t_confirm])-1 tick`, short simetri; 2R/3R ayrı ve 8/16 H1 zaman çıkışı. Aynı seviyenin yeniden retestleri yeni olay üretmez. Henüz tamamlanmamış üçgen/çift tepe yalnız görsel sezgiyle etiketlenmez. Batch 011 DP11b ile doğrudan çakışma tablosu gerekir; ana test retest ve teyidin ek katkısıdır.

**Ertelenen:** Çift dip/tepe, bayrak, kama ve üçgenin bağımsız örüntü etiketleri için teyitli pivot tespit gecikmesi ve sınır algoritması ayrıca dondurulmalı. “10 işlemden 3'ü” gibi s. 14 iddiası kaynakta örneklem/metot içermiyor. Seans gap örneği (s. 11–16) 24 saatlik kriptoya taşınmaz.

## 3. Markus Heitkoetter ve Mark Hodge — Basit Strateji

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 9/Baskı 9/Basit Strateji - Güçlü Bir Günlük Alım Satım Stratejisi - Markus Heitkoetter ve Mark Hodge (80 sayfa) - @eseckal.pdf>)

Bu kitap üçü içinde en net mekanik çekirdeği sunuyor. **BB(12,2)** (s. 11), **MACD(12,26,9)** (s. 13–14), isteğe bağlı **RSI(7)>70 / <30** (s. 16–18, 33). Long: MACD hem sinyal hem sıfır üzerinde, üst BB yukarı eğimli, fiyat üst BB'de/yakınında kapanınca sinyal mumunun high'ı `+1 tick` buy stop; short tam simetri (s. 18, 25–26, 33–35). Yedi tam günlük aralığın ortalaması ADR ile stop `0.10 ADR`, hedef `0.15 ADR` (s. 27, 36–37). Yazar zaman bazlı M5'i de önerir (s. 42–43), fakat asıl örnekler sıklıkla **range bar**; OHLC M5 uyarlaması aynı stratejinin birebir replikası değildir. RSI filtresi isteğe bağlıdır; filtrelenmiş sinyal sayısı ayrıca raporlanmalı. S. 27 örneğinde formül hedefi `1382.25+3.25=1385.50` iken metin `1385.00` yazıyor; testte formül esas alınır, tutarsızlık kaydedilir.

### S13 — M5 MACD/BB trend girişi, ADR stop/hedef

- **Tamamlanmış M5 sinyali:** `MACD12_26[t]>signal9[t] && MACD[t]>0`, `BB_upper12_2[t]>BB_upper[t-1]`, `close[t]>=BB_upper[t]-0.1 ATR14_M5[t-1]` long; short için MACD ikisinin altında, alt BB aşağı eğimli, `close<=BB_lower+0.1 ATR`. Kaynağın “yakınında” ifadesini `0.1 ATR` ile **biz** sabitliyoruz. BB standart sapması örneklem/popülasyon tercihi ve MACD EMA başlatma yöntemi test uygulamasında dondurulacak. RSI(7) eşiği `>70/<30` ayrı filtre ablation.
- **Emir:** Sinyal M5 kapanınca `high[t]+1 tick` buy stop / `low[t]-1 tick` sell stop; yalnız sonraki bir M5 barı boyunca geçerli. 1m intrabar veride dolum ve aynı bar stop/hedef sırası izlenir. Longda `stop=fill-0.10×ADR7`, `target=fill+0.15×ADR7`; short simetri, borsa tick'ine uygun dışa yuvarlama. `ADR7`, sinyalin ait olduğu **bugün hariç** son 7 tam UTC günün `high-low` ortalaması. Pozisyon boyu risk bütçesine göre; 0.10 ADR stop spread/kayma yanında çok küçük kalırsa işlem maliyeti filtresi ayrıca değerlendirilir. Zaman çıkışı bir sonraki UTC gün sınırı bizim gün içi sözleşmemiz.
- **Ayrı varyant:** Kaynak s. 44–47, zaman mumlarında BB seviyesinde stop emir veya sinyal kapanışı sonrası piyasa emri de anlatır. Bunlar S13 stop emrinin aynı işlem sayılabilecek farklı yürütmeleri; 1m dolum, kaçan emir, kayma ve net R ile karşılaştırılır. Günlük grafik için tam ADR stop/2R (s. 62–63) başka ufuktur ve gün içi sonuçla havuzlanmaz.

## Ortak test sırası

1. **S13** en açık kurallı aday; ardından **A13**'ün önceki retest sistemine ek değeri ve **L13a**'nın hacim/daralma etkisi. L13b/c seçim ve bağlam deneyleri.
2. Aynı işlem ücret, spread, kayma, funding, sinyal sayısı, bekleyen emrin dolmaması, net R, zaman çıkışı ve dış örneklem ile raporlanmalı. Aynı bar birden çok kitap etiketini alabilir ama tek gerçek pozisyon olarak sayılır.
3. Geleceği kullanan seviye, sonradan çizilmiş örüntü ve hayatta kalan coin seçimi yasak. Bu parti yalnız araştırma sözleşmesi ve kaynak kaydıdır.
