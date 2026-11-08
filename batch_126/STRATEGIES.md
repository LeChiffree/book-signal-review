# Kitap okuma 126 — günlük kapanış yönü ve Asya aralığı süpürmesi

**Kapsam:** Üç ayrı PDF'nin 13 + 22 + 22 = **57 PDF sayfası** baştan sona okundu. Atıflar PDF sayfasıdır. Backtest, paper test veya canlı emir yapılmadı.

## 1. Plexus_pa — Kolaylaştırılmış Daily Bias Tespiti (TR–ENG)

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 6/Baskı 6/Kolaylaştırılmış Daily Bias Tespiti (TR-ENG) (13 sayfa) - @eseckal.pdf>) · [Tam metin](01_daily_bias.txt)

**Tam okuma:** S. 1–6 Türkçe kılavuz, s. 7 kapak, s. 8–13 aynı metnin İngilizce aslı. S. 2–3/9–10 HH/HL–LH/LL akış ve olası hedefler; s. 4/11 önceki gün tepesinin üstünde veya dibinin altında kapanışla devam önyargısı; s. 5/12 aynı seviyeyi süpürüp içeri kapanışla ters yön önyargısı; s. 6/13 önceki gün aralığı içinde kalan kapanışta işlemden kaçınma. Bunlar **ertesi gün için tahmin**, gerçekleşmiş başarı oranı değil. Türkçe “OLHC/OHLC” sırası günlük mumun gelecekteki bar içi yolunu bilmemizi sağlamaz; sözleşme bunu kullanmaz.

### PB126A — D1 kapanış konumuyla ertesi gün yön ve işlem filtresi

- **Kaynak (PDF s. 4–6; İngilizce aslı s. 11–13):** Bir önceki günün yüksek/düşük seviyesine göre kapanış dört yönlü durum verir: tepe üstünde kapanış devam long, dip altında kapanış devam short, tepeyi süpürüp altında kapanış dönüş short, dibi süpürüp üstünde kapanış dönüş long. Önceki gün aralığı içindeki diğer kapanışlarda pas geç.
- **Kapalı mum sözleşmesi:** EURUSD, GBPUSD, USDJPY; işlem günleri broker saatine göre değil **New York 17:00** gün sonuyla sabitlenir; yaz/kış saat değişimi tarihsel takvimden uygulanır. `D[t]` ancak 17:00 New York kapanışından sonra bilinir. `PDH=high[t−1]`, `PDL=low[t−1]`. Öncelik sırası: `close[t]>PDH` ise ertesi gün `+1`; `close[t]<PDL` ise `−1`; `high[t]>PDH` ve `PDL<=close[t]<PDH` ise `−1`; `low[t]<PDL` ve `PDL<close[t]<=PDH` ise `+1`; iki taraf da süpürülmüş ve içeri kapanmışsa veya sınırda eşitlik varsa `0`/işlem yok. Gövdesi içeride kalan ama yalnız sınırla eşitlenen bar da pas. Bu çakışma önceliği **bizim** seçimimizdir ve duyarlılık testinde alternatif sınıflamalarla karşılaştırılır. Bilgi ilk kez `t` gün kapanınca doğar; `t+1` açılışından önce pozisyon kurulmaz.
- **Deneysel işlem/çıkış:** Önyargı `+1/−1` ise `t+1` gününün ilk uygulanabilir M1 kotasyonunda yönünde tek işlem. Stop uzaklığı `0,75 ATR14_D1` (yalnız `t` kapanışı ve öncesinden), hedef `1,5R`, 17:00 New York kapanışından hemen önce zorunlu çıkış; açık pozisyon taşınmaz. Başlangıç riski özsermayenin `%0,5`i; spread/komisyon/kayma ve veri boşluğu maliyete girer. Aynı M1 barda stop ve hedefe temas belirsizse stop önce varsayılır. Haftasonu ilk işlem gününde açılış boşluğu yürütme fiyatına yansır. Günlük yön filtresinin kendi sinyal gücünü izole etmek için aynı stop/çıkış ve maliyetlerle rastgele yön, önceki gün mum rengi ve [eski aralık/süpürme adayları](../batch_050/STRATEGIES.md) karşılaştırılır. Ön kayıt metrikleri: yön doğruluğu, maliyet sonrası net R, işlem sayısı, düşüş ve yıl/çift bazında istikrar.

## 2. Mark Rose — Mumlar Hakkında Bilmek İsteyeceğiniz Her Şey

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 7/Baskı 7/Mumlar Hakkında Bilmek İsteyeceğiniz Her Şey - Mark Rose (22 sayfa) - @eseckal.pdf>) · [Tam metin](02_mark_rose_candles.txt)

**Tam okuma:** S. 1–6 grafik temelleri; s. 7–8 doji ve marubozu; s. 9–10 haraminin tek başına zayıflığı ve sık konsolidasyon; s. 11–13 çekiç/asılı adam/ters çekiç/kayan yıldız ve sonraki mum teyidi; s. 14–17 yutma, yıldız, üç asker/karga, delici çizgi/kara bulut; s. 18–19 tarihçe; s. 20 sonuç; s. 21 risk notu; s. 22 özet. Özellikle s. 11–13, fitilin en az gövdenin iki katı olmasını ve sonraki mumla teyidi belirtir. Bu eşikler önceki mum formasyonu kütüğünde mevcut; s. 15'te “sabah yıldızı” diye adlandırılan örnek gerçekte anlatılan düşüş dönüşüyle uyumsuz bir çeviri hatasıdır. Bağımsız yeni kural eklenmedi. **Yeni aday yok.**

## 3. MarketMakersMethod.com — Forex Eğitimi / Market Makers Method

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 7/Baskı 7/Forex Eğitimi - Market Makers Method (22 sayfa) - @eseckal.pdf>) · [Tam metin](03_market_makers_method.txt)

**Tam okuma:** S. 1–3 giriş; s. 4–5 haftalık tepe/dip ve üç aşamalı hareket şeması; s. 6–9 ilk sekiz H1 mumundan haftalık psikolojik destek/direnç ve seviye/reset açıklamaları; s. 10–11 EMA 5/13/50/200/800; s. 12–14 günlük/haftalık kurulum ve 25–50 pip av; s. 15–18 Asya aralığı en çok 50 pip, süpürme, EMA/TDI/M–W, PF/ST/SAT türleri; s. 19 Londra/ABD seansları; s. 20–22 psikoloji ve risk. “Piyasa yapıcı bunu yaptı”, %90 kazanç ve 3 günlük döngü bir hipotezdir, emir akışı kanıtı değildir. S. 22'de özsermayenin `%20–30`unu riske atma ve bakiyeye sabit lot tablosu **kabul edilemez kayıp riski** taşır; strateji sözleşmesine alınmadı. TDI köpekbalığı yüzgeci ve M/W bacakları sayısal tanımsız; aşağıdaki deney bunların ölçülebilir alt kümesidir.

### MM126B — Haftanın ilk 8 H1 aralığı ve Asya süpürmesi sonrası EMA dönüşü

- **Kaynak (PDF s. 7, 10, 13–19):** Haftanın ilk 8 H1 mumu haftalık aralık; Asya aralığı en çok 50 pip; dışarı 25–50 pip stop avı; Londra başlangıcında M15 EMA 5/13/50 dönüş teyidi. Kaynakta tüm koşulların bu kesin birleşimi mekanik olarak yazılmadığından birleşim ve aşağıdaki pencereler **bizim ön kayıtlı deney tasarımımızdır**.
- **Veri/zaman:** EURUSD, GBPUSD, USDJPY; bid/ask M1'den UTC zaman damgalı M15/H1 barlar. `pip` JPY çiftinde `0,01`, diğerlerinde `0,0001`. Haftalık aralık pazartesi `00:00–08:00 UTC` kapanmış 8 H1 mumunun en yüksek/en düşük değeridir; bu saat seçimi kaynağın “ilk seans” belirsizliğini nesnelleştirir. Günlük Asya kutusu `00:00–07:00 UTC` kapanmış M15 mumlarının high/low'u; `range<=50 pip`. Yalnız pazartesi `08:00 UTC` sonrasında haftalık aralık bilinir. Londra penceresi tarihsel `Europe/London` saatine göre `08:00–12:00`; yaz/kış saati dinamik uygulanır. Pazartesi iki pencere kesişmezse o gün pas.
- **Sinyal:** Long için günlük Asya kutusunun altına, haftalık aralık alt sınırına da en fazla 10 pip mesafede, `25–50 pip` taşan bir M15 fitili oluşsun; aynı M15 mum **Asya kutusunun içine** kapansın. `25–50 pip` ölçüsü Asya dipten fitil dibine uzaklıktır. Bu süpürmeden sonraki dört kapanmış M15 barda `EMA5>EMA13>EMA50` ilk kez sağlansın ve kapanış EMA50 üzerinde olsun. İlk böyle M15 kapanışı long teyididir. Short, kutunun üstünde ve haftalık üst sınıra yakın ters simetridir. Haftalık sınıra yakınlık `10 pip`, UTC saatleri, dört bar ve tam EMA sıralaması bizim parametrelerimizdir. Aynı gün iki yön süpürülürse pas; yalnız ilk geçerli kurulum/gün. Sinyal M15 kapanmadan kullanılmaz.
- **Yürütme/risk/çıkış:** Bir sonraki uygulanabilir M1 ask/bid'den giriş; stop süpürme ekstreminden `2 pip` dışarı; hedef `2R`, en geç New York 17:00 kapanışından önce tam çıkış. İlk risk özsermayenin `%0,5`i, bir açık pozisyon/çift. Bid/ask, komisyon, kayma ve seans/hafta sonu boşlukları dahil. Giriş ile stop arası spread dahil `<=0` ise işlem yok. Aynı M1 barda stop/hedef belirsizse stop önce. İlk 8 H1 aralık filtresiz ve EMA filtresiz karşılaştırma kolları; ayrıca önceki [Asya aralığı/süpürme adayları](../batch_089/STRATEGIES.md) ile aynı veri ve maliyet altında net R, işlem sayısı, düşüş ve yıl/çift kararlılığı karşılaştırılır. Önceki haftanın/pazartesi henüz kapanmamış mumunun bilgisi sinyal hesabına giremez.

## Sonuç

**2 yeni araştırma adayı:** PB126A ve MM126B. Kaynaklardaki başarı iddiaları bu adayların performansı olarak kabul edilmez; backtest ve paper test sonraki aşamadır.
