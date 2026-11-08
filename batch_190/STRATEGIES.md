# Kitap okuma 190 — tahıl vadeli işlemlerinde ilk geri çekilme sonrası seans kırılımı

Üç PDF'nin **441 sayfası** sayfa bazında metne çıkarılıp baştan sona tarandı; kural sayfaları ayrıca ayrıntılı okundu. **1 yeni doğrulanmamış işlem stratejisi adayı** kaydedildi. Backtest, paper test ve emir yapılmadı. Sayfalar PDF sayfasıdır.

## 1. David Bennett — Day Trading (148 sayfa)

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 10/Baskı 10/Day Trading - David Bennett (148 sayfa) - @eseckal.pdf>) · [tam metin](01_day_trading_bennett.txt)

**Tam okuma:** S. 1–30 tahıl vadeli işlemleri, risk ve piyasa yapısı; 31–40 M2 mumlar ve seans seviyesi; 41–52 yön/geri çekilme/kırılım girişi; 53–62 stop/hedef aralığı; 63–75 emir, hesaplayıcı ve fiyat limitleri; 76–113 canlı işlem anlatısı; 114–139 bir aylık seans örnekleri; 140–148 uygulama ve kapanış. Klasik trend kırılımından ayıran kombinasyon, **ilk M2 mum yönü + en az iki barlık seans uç geri çekilmesi + yalnız ilk yeniden kırılım + M2 üçüncü mum istisnası**dır. S. 41–46 ve 55–62 kuralı, s. 47–52 örnekleri verir. Kitabın kaynak işlemi kırılımda stop emirle intrabar girer; aşağıdaki kapanmış M2 teyidi özellikle bizim test uyarlamamızdır.

### DB190A — açılış yönünde ilk seans uç kırılımı, iki bar geri çekilme filtresi

- **Kaynak (s. 41–46):** İlk iki dakikalık mum boğa ise long, ayı ise short yön; doji ise ikinci mum yön belirler. Seans tepesinden sonra tepenin altında yüksek yapan en az iki sonraki M2 mum long için geri çekilme; seans dibinden sonra dibin üzerinde düşük yapan en az iki M2 short için geri çekilme. İlk yeni seans ucu kırılımında işlem; üçüncü mum istisnasında ikinci mum iç mumsa tek bar geri çekilme yeterli. S. 55–58 `r` sınırını; s. 62 örnek stop `0.5r`, hedef `1.5r`; s. 65–66 seans sonu/OCA çıkışını anlatır.
- **Veri/kurulum:** CBOT mısır, buğday ve soya vadeli işlemlerinin gerçek sözleşme M2 OHLC, RTH takvimi, tick/point değerleri, tarihsel limit-up/down, kontrat rolleri ve bid/ask. Seansın ilk tamamlanmış M2 mumu `C>O` long, `C<O` short, eşitse ikinci tamamlanmış M2 yönü; o da doji ise işlem yok. Seans başında yan tut, fakat kaynak s. 42–43'teki yön değişimi için t kapanışında önceki bilinen karşı seans ekstremumu aşılırsa yönü çevir. Her yön değişiminden sonra yeni geçerli geri çekilme gerekir. M2 barlarının yalnız kapanmış değerleriyle izlenmesi, açılışın aynı mumuna giriş yapılmasını engeller.
- **Geri çekilme/sinyal:** Long için şu ana dek oluşmuş, **sinyal barından önceki** seans tepesi `A` dondurulur. `A` oluştuktan sonra peş peşe en az iki tamamlanmış M2 mumun her birinin `high<A` olması geçerli geri çekilmedir; ardından ilk tamamlanmış M2 `close>A` long sinyali. Short için seans dibi `B`, iki `low>B`, ardından `close<B`. Seansın ikinci mumu ilk mumun içinde (`high2<high1 && low2>low1`) ise üçüncü M2 kapanışında ilk mum ekstremumunun ötesi özel **tek bar** geri çekilme koludur. Sinyal kapanışı sonrasındaki ilk uygulanabilir ask/bid'den gir; seans başına ilk gerçekleşen sinyalden sonra başka giriş yok. Kapanış yerine kaynak stop giriş varyantı ayrı raporlanır.
- **Stop/hedef/risk:** Girişten önceki son geri çekilme mumları içinde, long için bir önceki mumuna göre hem daha düşük high hem daha düşük low yapan son mumun low'u `P`; yoksa **cari seansın sinyal öncesi** dibi. `r=A−P>0`. Short için bir önceki mumuna göre hem daha yüksek high hem daha yüksek low yapan son mumun high'ı `Q`; yoksa cari seansın sinyal öncesi tepesi; `r=Q−B>0`. Özel üçüncü mum kolunda `P/Q` ikinci mum ekstremumudur. Girişten `0.5r` karşı yönde stop, `1.5r` kâr yönünde hedef; `r≤0` veya stop mesafesi işlem maliyetinden küçükse işlem yok. Özsermayenin en çok `%0,25`i stop riski, RTH kapanışından önce zorunlu çıkış. Kaynak s. 62 `0.5r/1.5r` örneği verir; `%0,25` bizim risk payımızdır. Stop/hedef aynı M2 içinde görülürse tick sırası gerekir, yoksa aleyhte sıra. Borsa fiyat limiti, boşluk, komisyon ve kayma dahil; stop garantili fiyat değildir.
- **Ayırıcı sınama:** Aynı veri üzerinde çıplak seans high/low kırılımı, açılış yönü filtresiz kırılım, tek/iki bar pullback ve kaynak intrabar stop giriş varyantı karşılaştır. Mısır/buğday/soya ve takvim yılları dış örneklemde ayrı; 2 dakikalık bar toplama saati, öğle/düşük hacim dönemi ve fiyat limitleri duyarlılığı raporlanmalı. Kitabın seçilmiş örnek grafikleri bağımsız başarı kanıtı değildir.

## 2. Marc Friedfertig ve George West — Elektronik Günlük Traderların Sırları (238 sayfa)

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 10/Baskı 10/Elektronik Günlük Traderların Sırları - Marc Friedfertig ve George West (238 sayfa) - @eseckal.pdf>) · [tam metin](02_electronic_day_traders.txt)

**Tam okuma:** S. 1–55 elektronik piyasa/NASDAQ geçmişi ve ilk görüşmeler; 56–87 Roy Sidikman; 88–108 Eric Fromen; 109–148 gün içi işlem, seviye ve risk röportajları; 149–203 diğer trader portreleri; 204–219 Jonathan Petak; 220–238 disiplin/para yönetimi özeti. S. 29–32 emir defteri ve piyasa yapıcı bağlamı, s. 114–118 daha yüksek dipten alım ve sektör eş hareketi anlatır; açık sinyal eşiği ve zamanlı çıkış yoktur. Tarihsel 1990'lar NASDAQ piyasa yapısı bugünkü kotasyon/komisyon rejimine taşınamaz. S. 220–224'te zamanlama, ortalama kazanç/kayıp ve zarar disiplini süreç ölçütleridir. **Yeni bağımsız kapalı mum adayı: 0.**

## 3. Kenneth Mann — Ticaretin Kutsal Kasesi Risk Yönetimi (55 sayfa)

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Ticaretin Kutsal Kasesi Risk Yönetimi - Kenneth Mann (55 sayfa) - @eseckal.pdf>) · [tam metin](03_risk_holy_grail.txt)

**Tam okuma:** S. 1–12 risk profili, `1:2` asgari ödül/risk, 40 pip azami stop; 13–53 on adet seçilmiş arz-talep işlem örneği ve stop/çıkarım çizelgeleri; 54–55 sonuç. Arz-talep ve yutan mum bağlamı önceki sinyallerle çakışır; örneklerde “taze/zayıf bölge” ayrımı sayısal ve canlıda tekrarlanabilir biçimde tanımlanmaz. S. 10–12'nin `1:2` ve 40 pip sınırı EURUSD için risk filtresi olarak ablation'a konabilir, fakat yeni giriş stratejisi değildir. Seçilmiş 10 işlemin toplam pip sonucu dış örneklem performansı sayılmaz. **Yeni aday: 0.**

**Parti sonucu:** 3 PDF, **441 sayfa**, **1 yeni doğrulanmamış aday**. Kümülatif **570 PDF, 31.650 sayfa, 431 aday**.
