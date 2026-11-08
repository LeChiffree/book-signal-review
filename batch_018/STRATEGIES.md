# Kitap okuma 018 — formasyon, destek/direnç ve 3MS

**Kapsam:** Üç PDF, 146 + 105 + 73 = **324 PDF sayfası**. Tam sayfa metin dökümleri bu klasörde saklıdır; sayfa numaraları PDF sayfasıdır. Kitapların çevirisinde yer yer bozuk cümleler vardır. Aşağıdaki kaynak kuralları ile bizim algoritmik eşiklerimiz ayrıdır. Henüz backtest, paper test veya emir yoktur.

## 1. Yoosuf Khan — 90 Dakikada Sadeleştirilmiş Formasyon Trading Sırları

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 13/Baskı 13/90 Dakikada Sadeleştirilmiş Formasyon Trading Sırları - Yoosuf Khan (146 sayfa) - @eseckal.pdf>) · [Tam metin](01_pattern_secrets.txt)

Kitap çift tepe/dip, dikdörtgen, yükselen/alçalan kanal, bayrak, üçgen, kama, omuz baş omuz ve fincan kulp için görsel tanım ve çoğunlukla **formasyon yüksekliği kadar hedef** verir (s. 25–88). Çift tepe/dipte boyun çizgisi ile tepe/dip mesafesi (s. 25–30); dikdörtgende kanal genişliği (s. 33–34); bayrakta direk uzunluğu (s. 45–50); üçgen ve kamada şekil yüksekliği (s. 53–70) kullanılır. “Dördüncü veya beşinci temas” birçok örüntü için iddia edilir; doğrulanmış başarı olasılığı olarak alınmaz. 50/200 hareketli ortalama kesişimi (s. 111–116), RSI14 70/30 (s. 118–121) ve Fibonacci (s. 93–109) önceki partilerdeki sinyallerle örtüşür; yeni bağımsız strateji sayılmadı. Pozisyon başına sermayenin %1'i örneği s. 133–135'tedir; kayma nedeniyle kesin azami zarar garantisi değildir.

### K18a — Çift dip/tepe boyun kırılımı ve ölçülü hedef

- **Kaynak:** Yaklaşık eşit iki dip/tepe, aradaki boyun çizgisinin kırılması; hedef formasyon derinliği kadar (s. 25–30). Kitapta eşitlik toleransı, kırılım kapanışı, stop ve maksimum bekleme sayısal değil.
- **Bizim D1 olay tanımı:** Önceden tamamlanmış, sağında en az iki kapanmış mum bulunan pivotlar. Aynı yönde iki pivot arasında 5–40 gün, fiyat farkı `<=0.5 ATR14_D1`; aradaki karşı pivot boyun. İkinci pivot kesinleşince sonraki en çok 10 kapanmış D1 mumdan biri boynun `0.1 ATR` ötesinde kapanırsa olay. Long çift dip, short çift tepe. Bu tüm sayılar bizim parametrelerimizdir; geniş tarama yerine önceden sabitlenmiş adaylar olarak tutulur.
- **Uygulama:** Olay kapanışını takip eden ilk 1m açılışı giriş; stop ikinci dip/tepe ötesinde `0.1 ATR`, hedef `boyun ± |boyun − iki ekstremumun ortası|`; stop mesafesi sıfırsa işlem yok. H3D/H7D/H14D zaman çıkışları ayrı etiketler. Short yalnız uygun perp evreninde. İkinci pivotun sağ iki mumu ve boyun kırılımı tarihsel grafikte geriye boyanmaz. Önceki çift dip/tepe adaylarıyla aynı olay, bağımsız kanıt sayılmaz.

### K18b — Dar dikdörtgenin yönlü kırılımı

- **Kaynak:** Yatay üst/alt sınırlara çoklu temas, kırılım sonrası kanal genişliği hedefi; önceki trend yönü olası kırılım yönü diye anlatılır (s. 33–36). Yukarı yönlü bayrak/üçgen de aynı aileye girer (s. 45–64).
- **Bizim D1 sürüm:** Tetikten önceki 20 tamamlanmış D1 mumdan `R=max(high), S=min(low)`; genişlik `<=4 ATR14`, üst ve alt sınıra `0.2 ATR` içinde en az iki ayrı temas. `close[t]>R+0.1 ATR` long veya `close[t]<S-0.1 ATR` short; ATR ve sınırlar `t-1` itibarıyla dondurulur. İlk 1m giriş, karşı sınır stop, kanal genişliği kadar hedef, en geç H7D kapanışı. Maliyet sonrası başlangıç ödül/risk oranı ayrıca ölçülür. Bu batch 017 H17 sahte kırılımının karşı yönlü eş olayıdır; aynı seviyeyi farklı etiketle iki kez bağımsız fırsat gibi saymamak gerekir.

## 2. Michael C. Thomsett — Basitleştirilmiş Destek ve Direnç Analizi

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Basitleştirilmiş Destek ve Direnç Analizi - Michael C. Thomsett (105 sayfa) - @eseckal.pdf>) · [Tam metin](02_support_resistance.txt)

Ana katkı, desteğin kırılımdan sonra direnç, direncin kırılımdan sonra destek olarak **yeniden test edilmesi** (s. 17, 50); tek geçici taşmanın hemen yeni aralık kabul edilmemesi (s. 19–21); salınımın “yeni dip, yeniden test, aradaki direncin kırılması” gibi üç adımla teyidi (s. 42–45); hacim/OBV ile kırılımın kontrolüdür (s. 50–51, 60–64, 89–95). Kitap hisse örnekleri ve piyasa yorumu sunar, evrensel eşik/stop vermez. Hisse devir hızı/float temelli s. 96–98 ölçüsü kripto OHLCV'de aynı anlama gelmediği için aktarılmadı. Faiz/endeks ilişkileri (s. 99–103) ayrı dış veri gerektirir.

### T18a — Kapanış kırılımı, eski seviyeye retest, yeniden uzaklaşma

- **Kaynak:** Kırılan destek/direncin rol değiştirmesi, retest ve hacim teyidi (s. 17, 50–51, 79–81, 89–95). Retest zorunluluğu ve sayısal süre kitapta kesin değil.
- **Bizim D1 sürüm:** Önceki 20 kapalı D1 mumun direnci `R`; `t` kapanışı `R+0.1 ATR14[t-1]` üzerinde. Kırılım hacmi `volume[t] / median(volume[t-20:t-1]) >=1.5` ayrı teyit varyantı. Sonraki 1–5 tam D1 mumda `low` eski R'nin `±0.25 ATR14[t-1]` bandına dokunur, `close>=R` olur; bu retest mumunun kapanışından sonraki ilk 1m long. Stop retest mumunun dibi `−0.1 ATR`; hedef 2R veya H7D zaman çıkışı. Aşağı yönlü simetri short için. Retest gerçekleşmezse emir yok. Gelecekteki en iyi retest seçilmez; ilk uygun mum alınır. Batch 011/017 kırılım adaylarıyla olay örtüşmesi ölçülmeli.

### T18b — OBV ile kırılım teyidi bir filtre olarak

- **Kaynak:** Fiyat aralık dışına çıktığında OBV'nin de kendi aralığını aşması; aksi durumda fiyat kırılımına şüphe (s. 92–94). Bu bağımsız bir al/sat sistemi değil.
- **Bizim özellik/ablation:** Önceden tanımlanan K18b/T18a sinyalinde `OBV_D1[t] > max(OBV_D1[t-20:t-1])` long, simetrik alt kırılım short. `OBV` yalnız t'ye kadar kapanmış hacim ve kapanış değişimiyle hesaplanır. Baz sinyal ve OBV filtreli sinyal aynı dönem/evrende, ücret ve işlem sayısı dahil karşılaştırılır. OBV'nin kümülatif başlangıcı ve eksik hacim verisi sabitlenmeli. Mevcut özellik matrisinde OBV eşdeğeri varsa tekrar kolon açılmaz.

## 3. Frank Miller — Basitleştirilmiş Price Action

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 6/Baskı 6/Basitleştirilmiş Price Action - Frank Miller (73 sayfa) - @eseckal.pdf>) · [Tam metin](03_price_action.txt)

Kitabın 3MS yaklaşımı tek mum desenine güvenmeyip **yüksek zaman dilimi S/R alanı, trendin eski salınımı kırması ve yeni yönde iki salınım** arar (s. 22–31, 38, 43–46). Yutan mum/pin bar örneklerinin bir kısmı bu teyit yokken başarısız olarak tartışılır (s. 32–57). Çift tepede boyun kırılmadan tepeyi shortlamak reddedilir; boyun retesti, ikinci tepe üstü stop ve en yakın ana destek hedeflenir (s. 58–65). Bu hedef Khan'ın ölçülü hedefinden farklıdır. Kitap 1:3 risk/ödülü önerir (s. 12–13, 19–20), fakat tek başına kârlılık kanıtı değildir. 3MS'nin çizimleri ve pivot etiketleri geriye dönük belirginleşebilir; kodda teyit gecikmesi zorunlu.

### M18a — 3MS teyitli çift tepe/dip retesti

- **Kaynak:** Ana D1/W1 direnç/destek bölgesinde eşit veya daha düşük ikinci tepe (dipte daha yüksek ikinci dip), son trend salınımının kırılması, yeni yönde ikinci salınım; boyun retestinde giriş, ikinci tepe/dip ötesi stop, yakın ana karşı bölge hedefi (s. 43–46, 58–72).
- **Bizim D1/W1 sözleşmesi:** K18a'nın iki pivot/neckline tanımı; yalnız son **tamamlanmış** W1 veya D1 seviyesinin `±0.5 ATR14_D1` yakınındaki oluşumlar. Short için ikinci tepe birinciden yüksek değil; boyun altında kapanıştan sonra en az bir onaylı lower high ve lower low oluşsun. İlk boyun retestinde `high>=neckline−0.25 ATR` ve `close<neckline` ise sonraki ilk 1m short. Stop ikinci tepe `+0.1 ATR`; hedef olaydan önce bilinen en yakın karşı D1 pivot destek, en az 1R mesafe yoksa işlem yok. Long simetrik. Pivotlar sağda iki mum kapanana kadar bilinmez; W1 seviyesi haftalık kapanıştan önce kullanılamaz. 3MS nedeniyle giriş gecikir ve az olay üretebilir; K18a ve T18a ile ortak olay anahtarında karşılaştırılır.
- **Ablation:** Aynı formasyonun yalnız boyun kırılımı; retestli sürüm; `W1/D1 S/R + 3MS` filtreli sürüm. “Daha yüksek doğruluk” kitabın iddiası; maliyet sonrası getiri, kaçırılan hareket ve sinyal sayısıyla ayrıca sınanır.

## Tartışma ve sonraki test kuyruğu

En anlamlı karşılaştırma **tek olay ailesi** içinde yapılır: (1) formasyon kırılımı K18a/K18b, (2) rol değiştiren seviye retesti T18a, (3) hacim/OBV teyidi T18b, (4) Miller 3MS + yüksek zaman dilimi alanı M18a. Etiketler çok günlü sözleşmedeki UTC D1 karar, yalnız kapanmış W1/4h, ilk uygulanabilir 1m, H3D/H7D/H14D, ücret/kayma/funding, eşzamanlı stop/TP'de stop önceliği ve zaman sıralı dış örneklem kurallarına bağlanır. Bu partide hiçbir kitap için performans sonucunu doğrulamadık; kurallar **aday hipotez** olarak saklanır.
