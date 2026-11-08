# Kitap okuma 014 — 3W seviye reddi, BBMA yeniden giriş, mekanik bant dönüşü

**Kapsam:** Üç PDF'nin **56 + 54 + 75 = 185 PDF sayfası** işlendi. Sayfa referansları PDF sayfasıdır. PDF metni eksik olan BBMA örnek şekilleri görsel kontrol edildi (ör. s. 17). Kurallar test hipotezidir; kitapların başarı iddiaları kanıt sayılmaz. Bu partide backtest, paper test veya işlem yapılmadı.

## 1. Sumit Das — 3W Sistemi

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/3W Sistemi - Sumit Das (56 sayfa) - @eseckal.pdf>)

“Ne zaman, nerede, ne” yapısı: trend içinde kırılmış swing seviyesinin geri testi ve reddeden pin/doji mumu. Fiyat kapanışa uygulanan 30 hareketli ortalamanın üstünde long, altında short (s. 34); örnekler H1/H4/D1 (s. 37, 42–43, 53). Pin fitili gövdenin en az iki katı (s. 30). Longda önceden görülen swing high kırılır, seviye retest edilir, pin/doji kapanır, pin tepesinin 2 Forex pip üstüne emir; stop pin dibinin 2 pip altı (s. 35–36, 41–45). Short ters yönde. Kaynak “limit” diye yazsa da pin tepesinin **üstünde** long tetik, uygulamada buy stop koşuludur; testte emir türünü fiyat yönüne göre belirleriz. Sabit 2 pip kriptoya aktarılmaz. Kaynak %1 hesap riski ve 2R hedef söyler (s. 47–48); getiri garantisi değildir.

### W14 — H4 kırılmış swing retesti ve pin teyidi

- **Trend:** Son kapanmış H4 `close[t]>SMA30[t]` long; short ters. Kaynak MA türünü tam belirtmiyor; SMA30 bizim dondurulmuş seçimimiz. Karşılaştırma için eğim filtresi ayrı.
- **Seviye:** En az iki sağ H4 mumuyla **teyit edilmiş** son swing high/low, teyit kapanışında kullanılabilir. Long için seviye `R`, kırılım `close[t]>R`; sonraki en çok 12 H4 içinde `low<=R+0.1 ATR14_H4[t-1]` ve `close>=R` retest. Short simetrik. `2 sağ mum`, `12 H4`, `0.1 ATR` bizim nedensel nesnelleştirmemiz; kaynak öznel çizim kullanır.
- **Teyit ve emir:** Retest mumunda long alt fitil `>=2×max(gövde,1 tick)`, kapanış mum aralığının üst yarısında; short üst fitil ve alt yarı. Doji varyantı `abs(close-open)<=0.1×(high-low)` ve yönlü kapanışı **sonraki H4** bekler. Pin kapandıktan sonra `high+1 tick` buy stop / `low-1 tick` sell stop, yalnız sonraki H4 geçerli. Stop pin karşı ucu `±1 tick`, hedef 2R; gün içi 1m ile dolum ve stop/hedef sırası. Doji ve pin aynı olayın alt etiketleri. Batch 011 DP11b ve batch 013 A13 retest olaylarıyla çakışma saklanır.

## 2. John Ray — BBMA Trading Stratejisi

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 25/Baskı 25/BBMA Trading Stratejisi - John Ray (54 sayfa) - @eseckal.pdf>)

Göstergeler `BB(20,2)` kapanış, `EMA50` kapanış, `LWMA5(high/low)` ve `LWMA10(high/low)` (s. 10–11). Bollinger dışı **kapanış** CSM/momentum sayılıyor; ardından MA5/MA10 reddinde yönlü yeniden giriş öneriliyor (s. 29–34, 40). Dış bant teması ve geri dönüş ayrı **EXT/MHV** ailesi (s. 36–38, 45); CSM gelirse EXT iptal deniyor (s. 37). Çoklu zaman dilimi H4/H1/M15 doğrulaması (s. 42–45) açık ama sayısal eşzaman penceresi yok. Kritik çelişki: s. 31 `EMA50 > BB orta` için **düşüş**, s. 52 aynı durum için **yükseliş** diyor. EMA50 yönü sessizce tek kural yapılmaz. S. 17'deki şekil Mahi reddi ile aşağı harekete örnek; fiyat ve MA ölçeği üzerinden kesin giriş fiyatı vermez.

### B14 — BB dış kapanış sonrası LWMA retesti

- **Sinyal:** H1 `close[t]>BB_upper20_2[t]` ve `BB_upper[t]>BB_upper[t-1]` long CSM; short `close<BB_lower` ve alt bant eğimi aşağı. BB hareketini eğimle tanımlama **bizim** seçimimiz. CSM kapanışından sonra en çok 8 H1 içinde ilk long retest `low<=LWMA5(low)[u]` veya `low<=LWMA10(low)[u]` ve `close[u]>LWMA5(low)[u]` ve `close[u]>open[u]`; short `high>=LWMA5(high)`/`LWMA10(high)`, `close<LWMA5(high)`, ayı mum. MA5/MA10 temasları ayrı etiket. Kaynak bant dış kapanış ve MA reddi fikrini verir, `8 bar` ve net kıyas bizim sözleşmemiz.
- **Emir/çıkış:** Retest H1 kapandıktan sonraki ilk 1m giriş; stop retest mumunun karşı ucu `±1 tick`; ilk aday 2R, ayrı aday karşı BB/orta BB. Orta BB fiyatın yanlış yönündeyse kâr hedefi sayılmaz. Sinyalden sonra ters CSM gelirse bekleyen kurulum iptal. Bir açık pozisyon/varlık. İlk deneyde **EMA50/BB orta yön filtresi yok**; s. 31 ve 52 çelişkisi için iki işaretli varyant daha sonra ayrı karşılaştırılabilir. EXT/MHV ters işlem B14'ün devam sinyaliyle birleştirilmez. Batch 013 S13 BB trend sinyaliyle aynı CSM anı etiketlenir.

## 3. James Muranno — Akıl Almaz Kazançlı Mekanik Günlük Trading Stratejileri

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 17/Baskı 17/Akıl Almaz Kazançlı Mekanik Günlük Trading Stratejileri - James Muranno (75 sayfa) - @eseckal.pdf>)

Yedi hazır kombinasyon sunuluyor (s. 45–73). Çoğu HalfTrend, UT Bot, özel Williams %R, özel KDJ, özel RSI ayrışma, WTMO veya Reversal Finder **üçüncü taraf TradingView kodu** gerektiriyor; yalnız görsel ok/etiketle test, göstergenin geçmişte yeniden çizip çizmediği ve sinyal zamanı doğrulanmadan nedensel sayılamaz. S. 40'taki kısa giriş koşulları long ile aynen kopyalanmış, s. 52'de kısa çıkış seçeneklerinden ikisi kısa girişin tekrarı, s. 55'te kısa koşul “uzun pozisyona gir” diye yazıyor. Bu metin hatalarıyla özgün kod adına sonuç çıkarılmaz.

### M14 — ADX düşükken BB/RSI(5) ortalamaya dönüş

- **Kaynak:** Strateji #4: `ADX<25`, alt BB teması/altı ve RSI(5) 30 altından yukarı dönüşte long; üst BB ve RSI(5) 70 üstünden aşağı dönüşte short. Çıkış karşı BB veya karşı RSI eşiği (s. 57–59). Kitap BB ve ADX dönemlerini, stopu, mum kapanışı/tetik sırasını bu strateji için kesin söylemiyor.
- **Bizim M15 baz:** `BB(20,2)` ve Wilder `ADX14` **bizim standartlaştırmamız**. Long sinyal mumunda `ADX14[t-1]<25`, `low[t]<=BB_lower[t-1]`, `RSI5[t-1]<30 && RSI5[t]>=30`; short simetri `high>=BB_upper[t-1]`, `RSI5[t-1]>70 && RSI5[t]<=70`. BB seviyesi bir önceki kapanıştan, RSI dönüşü bugünkü kapanmış mumdan gelir. Giriş sonraki ilk 1m; stop sinyal ekstremumu `±max(1 tick,0.25 ATR14_M15[t-1])`; hedef girişte dondurulmuş **orta BB** (erken) veya karşı BB (kitaba daha yakın), 2R kontrol varyantı. Orta/karşı BB stopa göre yanlış taraftaysa işlem yok. En fazla 24 M15 zaman çıkışı bizim seçimiz. MFI/HMA stratejisi #5 (s. 61–63) standart göstergelerle ayrı kodlanabilir, fakat kitap özel mum rengi ve MTF uygulaması istediği için kod/sürüm doğrulaması sonrası aday havuzuna alınır.

**Ertelenen özel indikatör setleri:** #1 HalfTrend + Williams (s. 46–49), #2 UT Bot + KDJ (s. 50–52), #3 özel RSI ayrışma (s. 53–56), #6 WTMO + HalfTrend (s. 64–68), #7 BB + özel Reversal Finder/konsolidasyon filtresi (s. 69–73). İleride uygulama ancak kesin gösterge kodu/sürümü, repaint ve yayın zamanı denetimiyle; kitaptaki “yüksek kazanma oranı” başlığı ölçülmüş sonuç değildir.

## Deney sırası ve kayıt

1. **M14** hesaplanabilir kural; ardından **W14** ve **B14**. Önceki ADX/BB, swing retest ve BB momentum adaylarıyla aynı işlem etiketleri üzerinden marjinal katkı ölçülür.
2. Her aday için dondurulmuş varlık evreni, UTC H1/H4/M15 kapanışları, 1m yürütme, ücret/spread/kayma, net R, dolmayan emirler, sinyal sıklığı, stop/hedef sıralaması ve dış örneklem zorunlu. Ayrı parametre/çıkış varyantları aynı başarı serisi gibi havuzlanmaz.
3. Kaynakta ispatlanmamış kârlılık, davranış veya “büyük oyuncu” iddiaları işlem kuralı ya da beklenen getiri sayılmaz.
