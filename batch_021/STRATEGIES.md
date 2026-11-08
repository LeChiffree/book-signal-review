# Kitap okuma 021 — arz/talep geometrisi, Londra kutusu, James16

**Kapsam:** 121 + 8 + 12 = **141 PDF sayfası**. Her PDF'nin sayfa sıralı tam metin dökümü bu klasörde. Atıflar PDF sayfasıdır. Kaynak koşulları ile kriptoya çevirmek için eklediğimiz koşullar açıkça ayrılır. Bu parti backtest, paper test veya emir içermez.

## 1. Christopher — Price Action Scalping Stratejisi

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 20/Baskı 20/Price Action Scalping Stratejisi - Christopher (121 sayfa) - @eseckal.pdf>) · [Tam metin](01_christopher_scalping.txt)

Kitabın en somut katkısı arz/talep bölgesini tarif eden mum geometrisi: taban mumu gövdesi yaklaşık toplam aralığın %25–30'u veya daha küçük (s. 22), çıkış/itki mumu gövdesi toplam aralığın >%70'i (s. 23). DBR/RBR talep ve RBD/DBD arz şemaları (s. 26–35); talep bölgesinde proksimal sınır taban gövde tepesi, distal sınır taban veya çıkış mumunun daha aşağı düşüğü (s. 36–48, 58–62). Arzda gövde altı ve üst fitil/çıkış tepesi simetriği (s. 64–68). Kitap bölgeye dönüşte proksimal çevresinden giriş ve distal ötesi stop önerir. “Bekleyen büyük oyuncu emirleri” bu OHLCV geometrisinden doğrulanamaz. S. 69–94'te hacim ile mum aralığı uyuşmazlıkları ve yüksek hacimli alıcı/satıcı tuzak mumu; s. 95–115'te 1h bölge içine 5m bölge veya 1m SMA5/tuzağı yerleştiren scalping örnekleri var. Son bölüm özellikle NIFTY/BANKNIFTY opsiyonlarından söz eder (s. 112–115); kriptoya performans aktarımı yoktur.

### C21a — Geometrik DBR/RBR talep bölgesinin ilk retesti

- **Kaynak:** Düşüş veya yükseliş yönlü itki mumu, bir veya birkaç küçük gövdeli taban, güçlü boğa çıkış mumu; taban gövde tepesine yakın giriş, taban/çıkış düşük ekstremumu altı stop (s. 22–23, 26–38, 58–62).
- **Bizim kapalı D1 sözleşmesi:** Giriş itki mumu `body/range>=0.70`, taban 1–3 ardışık mumda her `body/range<=0.30`, çıkış boğa mumunda `body/range>=0.70`, `close>max(high_base)`, `range>0`; yön için giriş mumunun rengi DBR/RBR'yi belirler. Çıkış **kapandıktan** sonra `prox=max(max(open,close) for base)`, `dist=min(low_base,low_exit)` çizilir. `dist<prox` ve bölge genişliği `<=2 ATR14` şartı bizim veri kalite filtremizdir. Sonraki 20 tam gün içinde ilk geri dönüşte `prox+0.1 ATR` limit buy; uygulama 1m temas ve kaymayla, stop `dist−0.1 ATR`, hedef 2R, H7D/H14D ayrı zaman çıkışı. Önce `close_D1<dist` olursa bölge geçersiz. İşlem ve bölge yalnız çıkış mumu kapandıktan sonra aktif; geçmişte taban üzerine sinyal yazılmaz.
- **Karşılaştırma:** Batch 019 AM19'da taban genişliği/impuls ATR ile tanımlandı. Aynı olay evreninde `Christopher gövde oranı` ve `Matov ATR` bölge tanımı birer ablation; mükerrer trade sayılmaz. RBD/DBD arz short simetrik ama ayrıca perp ve funding modeliyle.

### C21b — SMA5 altındaki yüksek hacimli satıcı tuzağı (ayrı mikro yapı hipotezi)

- **Kaynak:** 1m grafikte SMA5 altında fiyat mumuna boşluk, önceki mumdan yüksek hacim, kırmızı satıcı tuzağı veya yeşil geri alma; mum tepesinin kırılımında long, mum dibi stop, en az 2R hedef (s. 88–90, 109–112). Short simetriği s. 91–95, 112–115. Kitap “boşluk” için kesin tolerans vermez.
- **Bizim M1 araştırma tanımı:** `high[t]<SMA5_M1[t]−1 tick`, `volume[t]>volume[t-1]`, `close[t]<open[t]`; sonraki en fazla 3 kapanmış 1m mum içinde `close>high[t]` olursa bunu takip eden ilk uygulanabilir 1m açılışında long. Stop `low[t]−1 tick`, hedef 2R, 60 dakika zaman çıkışı. M1 SMA yalnız kapanmış mumdan. Seans/likidite/ücret filtresi zorunlu. **Mevcut çok günlü D1 sözleşmesinin dışında** ayrı intraday test kuyruğu; günlük stratejinin 1m dolum akışına sinyal olarak gizlice karıştırılmaz. Kaynağın yüksek hacimli kırmızı mumunun gerçekten “satıcı tuzağı” olduğunu OHLCV tek başına kanıtlamaz.

## 2. Londra Koparma Stratejisi

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 9/Baskı 9/Londra Koparma Stratejisi (8 sayfa) - @eseckal.pdf>) · [Tam metin](02_london_breakout.txt)

Forex GBP/USD için Asya seansı high/low kutusunu çizip Londra açılışında kutu dışında **mum kapanışı** bekler; long stop kırılım mumu dibi, short stop tepesidir, hedef 30–50 Forex pip (s. 3–6). Yazar sahte kırılım ve kutuya dönüş riskini kabul eder (s. 7). S. 7–8 reklam performans sayıları doğrulama değildir. Kaynak zaman dilimi, Asya seans başlangıç/bitiş saati ve Londra açılışı için UTC zaman kuralı vermez.

### L21 — Asya kutusu sonrası seans kırılımı

- **Bizim kripto M15 sözleşmesi:** Takvim her tarih için IANA `Europe/London` ile Londra yerel saati; Londra açılışı 08:00, Asia kutusu **önceden belirlenen** 00:00–07:45 London kapanmış M15 mumları. DST otomatik takvimle çözülür. 08:00–10:00 London arasında ilk `close_M15>AsiaHigh+0.1 ATR14_M15` long veya `<AsiaLow−0.1 ATR` short. Sinyal mumunun kapanışından sonra ilk 1m açılışı, stop sinyal mumunun karşı ekstremumu, TP 2R, en geç 12:00 London çıkış. Kaynak 30–50 pip hedefi yalnız GBP/USD ölçüsüdür; kriptoya kopyalanmaz. Bir gün ilk kırılım dışında tekrar giriş yok. Kutu aralığı sıfırsa işlem yok; büyük kırılım mumu nedeniyle stop mesafesi >2 ATR ise işlem yok (bizim risk filtremiz).
- **Test ayrımı:** Kripto 24/7 olduğu için Asya/Londra açılışı Forex piyasa mekanizmasıyla eşdeğer değildir. Hacim ve volatilite saat profili, spread ve hafta içi/sonu ayrı raporlanır. Bu M15 hipotezi D1 çok günlü kuyruğundan ayrıdır; sessizce aynı modele eklenmez.

## 3. James16 Trading Stratejisi

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 9/Baskı 9/James16 Trading Stratejisi (12 sayfa) - @eseckal.pdf>) · [Tam metin](03_james16.txt)

Kaynak D1/W1 trend yönünde geri çekilme bağlamında iki mumluk eşit dip/yüksek ve dış barlar tanımlar (s. 3–8). DBLHC: iki yaklaşık eşit düşük ve ikinci mum daha yüksek kapanış; DBHLC: iki eşit yüksek ve ikinci daha düşük kapanış (s. 4–5). BUOVB/BEOVB ise ikinci mumun ilkini hem yüksek hem düşük bakımından kapsaması ve ters yönde kapanmasıdır (s. 7–8). Pin barın doğru S/R konumunda olması s. 9–10. Kaynak 2 ve 25 pip eşiklerini Forex için verir; kriptoya aynı birimle uygulanmaz. Eşit zirvelerin boğa, eşit diplerin ayı olarak da anlatıldığı s. 5–6 çeviri/kural açısından alışılmış sezgiye ters; bunu bağımsız testte açık varyant saymak gerekir.

### J21 — Trend yönünde çift mum eşit dip/yüksek kapanış farkı

- **Bizim D1 aday:** Son tamamlanmış W1 kapanışı EMA20_W1 üstünde ve D1 EMA20 eğimi pozitifse long rejim. Ardışık `t-1,t` D1 mumlarda `abs(low[t]−low[t-1])<=0.2 ATR14_D1[t-1]`, `close[t]>close[t-1]`; `t` kapanışı sonrası ilk 1m long; stop `min(low[t-1],low[t])−0.1 ATR`, TP 2R, H3D/H7D çıkış. Short için eşit yüksek ve `close[t]<close[t-1]` simetri. `0.2 ATR` ve EMA rejimi bizim parametrelerimiz; kaynak yalnız yaklaşık 2 pip ve yükseliş trendi der. Kaynaktaki 25 pip bekleyen stop alternatifi kriptoda `0.1 ATR` tetik ofseti olarak ayrı varyant; sinyal kapanışı ile stop tetiklemeli giriş aynı işlem değildir.
- **Ablation:** Eşit dip/yüksek filtresi, yalnız kapanış üstünlüğü ve W1 rejimi ayrı ayrı; mevcut double-bottom/inside-outside ve pin bar kolonlarıyla eşdeğerlik denetimi. Dış bar BUOVB/BEOVB ayrıca raporlanabilir ama bu partide eşit dip/yüksekten bağımsız kazanç iddiası üretilmedi.

## Öncelik ve sınırlar

En anlamlı çok günlü deneme **C21a'nın AM19 bölge tanımıyla bire bir karşılaştırması** ve **J21'in iki mum özelliğinin mevcut trend taban çizgisine ek değeri**. C21b ve L21 intraday kuyruğuna ayrılır; bunların D1 sözleşmesini yanlışlıkla sağlamış gibi raporlanmaması gerekir. Tüm denemelerde point-in-time coin evreni, kapanmış veri, 1m uygulanabilir fiyat, ücret/spread/kayma/funding, eşzamanlı stop/TP'de stop önceliği, olay tekilleştirme ve zaman sıralı dış örneklem şarttır.
