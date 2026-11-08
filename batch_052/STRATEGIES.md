# Kitap okuma 052 — Oturum geri çekilmesi, marubozu ve tam aralık MA teyidi

**Kapsam:** 19 + 31 + 16 = **66 PDF sayfası**. Üç PDF'nin tüm sayfaları numaralı, sıralı metne çıkarıldı; atıflar PDF sayfasıdır. Kaynak anlatımı ile **bizim** kripto/kapalı mum test sözleşmeleri ayrı yazıldı. Backtest, paper test ve emir yapılmadı.

## 1. ICT Stratejisi

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/ICT Stratejisi (19 sayfa) - @eseckal.pdf>) · [Tam metin](01_ict_strategy.txt)

**Kaynak:** Forex odaklı Asya, Londra ve New York seanslarını; Asya aralığı sonrasında hareket fikrini anlatır (s. 3–4). Fibonacci'yi **mum gövdelerinin** impuls dip/tepesine bağlayıp %62, %70.5 ve %79 OTE geri çekilme seviyelerini giriş bölgesi olarak verir (s. 5–7). “Üçün gücü”nde önce eski dip/tepe likiditesinin alınması, sonra ana yön hareketi tasvir edilir (s. 9–12). Yükseliş günlük eğilim, Londra gücü ve New York saatiyle 07:00 sonrası geri çekilmeyi bekleme sırası tarif edilir (s. 13); Forex için 20 pip şartı kriptoya aktarılmaz. Seans saatlerinin RSA/New York dönüşümü ve yaz saati kaynakta tutarsız/eksiktir; uygulamada IANA `America/New_York` saat dilimi ve gerçek tarih bazlı DST kullanılmalıdır. s. 14'teki “%90 doğru” ve s. 17–19'daki sabit günlük kârla 100→100.000 dolar planı doğrulanmış beklenti değildir; strateji getirisi olarak kullanılmaz. Kurumsal emir niyeti OHLCV'den gözlenemez.

### IC52 — Önceki gün dip süpürmesi sonrası gövde impulsuna OTE dönüşü

- **Bizim veri ve yön:** M15 gerçek OHLC, UTC günleri ve son **tam D1** için `close>EMA50_D1` long (short tersi). Önceki tam UTC gününün gerçek low/high'ı yeni gün başlamadan bilinir. M15 barlarının zamanları UTC saklanır; New York seans filtresi ayrı ablation kolunda `America/New_York` 07:00–09:00 yerel saatteki kapanmış barları kullanır. Kaynağın Forex seansları kriptoda doğal açılış değildir; temel kol 24/7, seanslı kol ayrıca karşılaştırılır.
- **Süpürme ve impuls:** Long için gün içindeki ilk M15 bar `low<previousDayLow−0.1 ATR14_M15` ve `close>previousDayLow`; short `high>previousDayHigh+0.1 ATR` ve `close<previousDayHigh`. Bunun ardından en çok 8 tamamlanmış M15 bar içinde long için gerçek `close` süpürme barı high'ı üstüne, short low'u altına çıkarsa impuls teyidi. Gövde Fib ankrajları long için süpürme barı `min(open,close)` (A) ile ilk impuls teyit barına kadar oluşan **en yüksek gövde ucu** (B); short simetri. Ankrajlar impuls kapanışında dondurulur. Bu süpürme/impuls seçimi ve eşikler **bizim** nesnelleştirmemizdir; kaynak olayları çizimle verir (s. 6, 9–13).
- **OTE giriş:** Impuls teyidinden sonraki en çok 8 M15 bar içinde ilk geri çekilmede long `B−0.79(B−A) ≤ close ≤ B−0.618(B−A)` ve kapanış önceki M15 kapanışından yüksekse giriş sinyali; short A/B simetrik. `0.705` ayrı orta bölge alt kolu, kaynak oranı (s. 5–7). Sinyal kapanışından sonraki ilk uygulanabilir 1m giriş. Stop long süpürme gerçek low `−0.1 ATR`, short high `+0.1 ATR`; 2R veya 24 M15 bar süre. Geri çekilme öncesi stop seviyesi ihlal edilirse iptal. Aynı 1m stop/hedefte kötümser sıra.
- **Karşılaştırma:** Önceki seans süpürmesi ve Fib geri çekilme adayları, çıplak önceki gün dip/tepe geri kazanımı, OTE ve NY saat filtresi kolları. Sinyal esnasında henüz bitmemiş D1 veya gelecekte seçilecek impuls tepesi kullanılmaz.

## 2. Mumların Dili

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Mumların Dili (31 sayfa) - @eseckal.pdf>) · [Tam metin](02_language_of_candles.txt)

**Kaynak:** Kitap boğa/ayı marubozunu gölgesiz veya çok küçük gölgeli açık–ekstrem/kapanış–ekstrem mumu olarak tanımlar; ertesi mum yön teyidi ve karşı ekstremde stop önerir (s. 1–2). Doji/topaç belirsizlik olarak anlatılır (s. 3–4). Çekiç alt fitili gövdenin en az iki katı (s. 5), asılı adam ve kayan yıldız (s. 7–8), yutan mum (s. 9–10), %50–100 kısmi yutma olarak delici/kara bulut (s. 12–13) vardır. Üç mumlu sabah/akşam yıldızı örneği gerçek hisse **gap** koşulu içerir (s. 16); kesintisiz 7/24 kriptoda gap yoksa aynı kurala zorla uydurulmaz. s. 21'de 50/100 SMA kesişimi de anlatılır; batch049 MA49 ile aynı aile. s. 24'te BB dış bandına dokunup ters işlem açma fikri, aynı sayfadaki trendde bant genişlemesi uyarısıyla birlikte okunmalıdır. “15:20 CMP” hisse kapanış öncesi örnektir; kriptoya aynen taşınmaz.

### ML52 — Marubozu sonrası aynı renk teyit mumu

- **Bizim şekil:** H4 gerçek OHLC; `range=high−low>0`, `body=|close−open|`; boğa için `close>open`, alt fitil `(open−low)/range≤0.05`, üst fitil `(high−close)/range≤0.05`, `body/range≥0.90`. Ayı simetrik. Kaynağın “hafif fiyat değişikliği kabul” ifadesinin %5/%90 eşikleri **bizim** ölçümüzdür. Sinyal yalnız H4 kapandıktan sonra geçerli.
- **Teyit ve giriş:** Marubozuyu izleyen **tek** H4 bar aynı renkte kapanır ve boğa için `close>marubozuClose` (ayı için `<`) ise, ikinci H4 kapanışından sonraki ilk uygulanabilir 1m giriş. Çıplak marubozu kapanışından hemen giriş ayrı kol; iki kolun aynı başlangıç döneminde sinyal ve fırsat maliyeti karşılaştırılır. Marubozu ertesi mum başlamadan “ertesi renk” bilgisi kullanılamaz.
- **Risk:** Long stop marubozu low `−0.1 ATR14_H4`, short high `+0.1 ATR`; 2R veya 12 H4 bar süre. Girişte stop yanlış tarafta ya da toplam maliyetin iki katından dar ise atla. Aynı 1m stop/hedefte kötümser sıra. Kitap sayısal 2R/süre vermez; bunlar test için **bizim**.
- **Karşılaştırma:** Önceki uzun gövdeli momentum/engulfing adayları ve batch050 BC50 büyük kapanış kırılımı ile sinyal örtüşmesi. Tek başına marubozunun yönlü devam mı, yoksa aşırı uzama mı verdiği dış örneklemde belirlenir; kaynak yorumu sonuç sayılmaz.

## 3. John Person — Hareketli Ortalamalarla Strateji Rehberi

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Hareketli Ortalamalarla Strateji Rehberi - John Person (16 sayfa) - @eseckal.pdf>) · [Tam metin](03_ma_strategy_person.txt)

**Kaynak:** Hareketli ortalamanın eğimi ile kapanışın konumu temel yön bilgisidir (s. 4). Daha kuvvetli filtre olarak **tüm mum aralığının** MA üstünde/altında kalmasını ve bunun iki veya daha fazla ardışık bar sürmesini önerir (s. 4–6). Farklı periyotlar/çoklu zaman dilimi tartışılır (s. 7). Stokastik %K/%D aşırı satımda yukarı, aşırı alımda aşağı kesişimi (s. 8–9), pivot yakınında stokastik ayrışma (s. 10), MACD teyidi (s. 11–13) ek araçlardır. Yazar benzer matematiksel hareketli ortalamaları üst üste eklemenin bağımsız onay olmadığını açıkça belirtir (s. 12, 14). s. 9'da %D formülü metin/çeviri hatalı görünüyor; standart %K 14 ve %K'nın SMA3 sinyal tanımı kullanılmalı, alternatif stokastik sürümleri karıştırılmamalıdır.

### JP52 — İki tam H4 aralığın SMA20 üzerinde/altında kapanması

- **Bizim gösterge:** Gerçek H4 OHLC'den `SMA20(close)`, en az 100 H4 ısınma. Long için art arda iki **tamamlanmış** H4 barda `low[t−1]>SMA20[t−1]`, `low[t]>SMA20[t]`, ayrıca `SMA20[t]>SMA20[t−2]`; short iki `high<SMA20` ve aşağı eğim. `20` kitapta tartışılan örnek periyottur (s. 7), iki bar s. 6'dandır. Her mum kendi kapanışında hesaplanan SMA ile değerlendirilir; tek kapanış üstü yetmez.
- **Olay ve icra:** Sinyal, bu iki bar koşulunun **ilk** tamamlandığı H4 kapanışında; yön devam ettiği sürece her yeni 2 bar için tekrar giriş yok. SMA tarafı bozulup tekrar iki bar sağlanırsa yeni aday. Sonraki uygulanabilir 1m giriş. Long stop iki teyit mumunun düşük min'i `−0.1 ATR14_H4`, short yüksek max'i `+0.1 ATR`; 2R veya ilk ters tarafta iki tam aralık teyidi veya 24 H4 bar (hangisi önce) çıkış. Kaynak kesin stop/hedef vermez; bunlar **bizim** test sözleşmesidir.
- **Ablation:** Yalnız `close>SMA20` iki bar, tüm aralık iki bar, tüm aralık + Stoch `%K14<30` bölgesinden `%D3` yukarı kesişimi; Stoch filtresi sadece **ayrı** kol. Stoch filtresi için Person'ın s. 9 tarifine uygun olarak long `%K<30` iken yukarı kesişim, short `%K>70` iken aşağı kesişim değerlendirilir. Gelecek barın stokastik bilgisi alınmaz.
- **Karşılaştırma:** Batch049 MA49 günlük uzun/nakit kesişimleri ve önceki MA geri çekilme sistemleriyle ayrım: JP52'nin olayı **iki tam bar aralığının** tek MA tarafında oluşmasıdır. Maliyet, geç teyit ve kaçan erken trendler raporlanır; MACD/CCI ile çoklu aynı-kökenli teyitler öncelikli değildir.

## Ortak test notu

Üç adayda point-in-time varlık evreni, gerçek kapanmış mum, sonraki uygulanabilir 1m fiyatı, ücret/spread/kayma/funding, stop/hedef sıralaması, eksik bar ve pozisyon çakışması açık tutulmalıdır. IC52'de seans saatleri ve impuls ankrajı; ML52'de kapalı marubozu teyidi; JP52'de tüm aralık/MA karşılaştırmasının gecikmesi ilk teknik kontrollerdir. Kârlılık henüz ölçülmedi.
