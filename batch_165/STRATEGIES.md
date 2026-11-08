# Kitap okuma 165 — mum repertuvarı, günlük işlem ve Hançer deseni

Üç ayrı PDF'nin **50 + 46 + 48 = 144 sayfası** sırayla tarandı. Atıflar PDF sayfasıdır. **Yeni bağımsız araştırma adayı: 1.** Backtest, paper test veya emir yapılmadı.

## 1. Japon Mum Çubuklarına Kolay Bir Yaklaşım — Stefano Calicchio

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 14/Baskı 14/Japon Mum Çubuklarına Kolay Bir Yaklaşım - Stefano Calicchio (50 sayfa) - @eseckal.pdf>) · [tam metin](01_candles_calicchio.txt)

**Tarama:** s. 1–12 tarihçe ve OHLC mum yapısı; 13–17 gölgeler/doji; 18–26 sabah/akşam yıldızı, çekiç, asılı adam ve ters çekiç; 27–38 yutan, kara bulut, delici, harami, cımbız ve üç asker/karga; 39–45 boşluk ve üç yöntem/itme çizgisi devam kalıpları; 46–50 örnekler ve sonuç. Kapanış teyidi, trend bağlamı ve seans boşluğu açıklamaları var, fakat tekil yeni giriş/stop/çıkış sırası yok. Mum aileleri [3.](../batch_003/STRATEGIES.md), [50.](../batch_050/STRATEGIES.md) ve [138. partide](../batch_138/STRATEGIES.md) kayıtlı. S. 19–20 başarı ima eden anlatım ölçülmüş olasılık değildir. **Yeni bağımsız aday yok.**

## 2. Günlük Alım Satım — Anthony Smith

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 19/Baskı 19/Günlük Alım Satım - Para Kazanmanın ve Başarıya Ulaşmanın Gizli Stratejileri (Orijinal) - Anthony Smith (46 sayfa) - @eseckal.pdf>) · [tam metin](02_day_trading_smith.txt)

**Tarama:** s. 1–13 günlük işlemin genel yapısı ve enstrümanlar; 14–19 volatil/likit hisse ve izleme listesi; 20–25 broker/platform ücretleri; 26–28 zihinsel hazırlık; 29–36 plan, kayıp sonrası değerlendirme ve işlem kaydı; 37–42 düşük fiyatlı hisselerin riskleri; 43–46 broker ve sonuç. Kitapta başlığın vaat ettiği nesnel al/sat sinyali, kapanmış mum koşulu ve tam çıkış kuralı verilmez. S. 11–12 vergi, düzenleme veya broker koşulları güncel kabul edilmez. S. 37–42 düşük fiyat tek başına getiriyi öngörmez; likidite ve spread ölçülmelidir. **Yeni bağımsız aday yok.**

## 3. Price Action — Derek Salvon

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 19/Baskı 19/Price Action - Derek Salvon (48 sayfa) - @eseckal.pdf>) · [tam metin](03_price_action_salvon.txt)

**Tarama:** s. 1–8 Donchian kanalına temasla M15 scalping; 9–15 kırılım/retest, PPR; 15–19 Hançer; 20–30 gösterge ve fiyat hareketi; 31–35 M5 seviye/pin ile 3R scalping; 36–42 VSA/hacim; 42–45 vadeli işlem marj bölgeleri; 46–48 özet. M15 Donchian bant dönüşü [103. partide](../batch_103/STRATEGIES.md) H1/120 kanal olarak kayıtlı; M15 ve 4–5 pip stop yalnız parametre farkı. PPR, pin bar, kırılım/retest ve VSA önceki ailelerle örtüşür. S. 43'te marjın minimum fiyat adımına bölünmesi fiyat mesafesi için boyutsal olarak eksik görünüyor: kontrat çarpanı/değer birimi olmadan uygulanabilir tam sistem değil. S. 42'de “piyasa yapıcının işlemi” hacim barından doğrudan gözlenmez. Hançer, [tek mum %50 reddi](../batch_128/STRATEGIES.md) adayına ek olarak **ikinci üst zaman dilimi mumunun %50 üzerinde kapanması ve %61,8 altına fitil atmaması, ardından alt dilim fitili ve onun kırılması** olay sırasını verir.

### DS165A — Hançer: üst dilim 50/61,8 tutulması ve alt dilim geri tepme kırılımı

- **Kaynak (PDF s. 15–19):** İlk büyük yön mumu; ikinci mum ilk mumun %50 düzeltmesini koruyup ilk kapanışı geçmez ve fitili %61,8 ötesine gitmez. Alt zaman dilimindeki gövdesi kadar veya daha uzun ters fitilli mumun yönündeki ekstremumu kırılınca giriş; stop %50'nin karşı yanında; hedef 2–3 stop mesafesi. Short tam simetri. Kaynak W1/D1, D1/H4 ve H4/H1 çiftlerini sayar. S. 19'daki “alt dilim sinyali, ikinci üst dilim mumunun içinde ve koşullar sağlandıktan sonra” ifadesi nedensel olarak çelişir: üst mumun *kapanış* koşulu, içindeki alt mumlar yaşanırken bilinemez. Aşağıdaki sürüm, sinyali **ikinci üst mum kapandıktan sonraki** üst mumda arar; bu kaynak sonucunun bire bir tekrarı değildir.
- **Kapalı mum ön kayıt:** EURUSD/GBPUSD/USDJPY FX; H4 kurulum/H1 tetik, tek ortak saat dilimi. H4 boğa ilk mum `close>open`, aralığı `≥1,5×ATR14_H4[t−1]`, gövde/aralık `≥0,65` ise “büyük”; bu eşikler **bizim**. Mum `L,H,C` kapanışında dondurulur. İzleyen tek tamamlanmış H4 mum için `close2>(H+L)/2`, `close2≤C`, `low2≥H−0,618(H−L)` şartları. Shortta `close2<(H+L)/2`, `close2≥C`, `high2≤L+0,618(H−L)` şartları. İkinci mumun ilk mumun high/low sınırını hiç geçmemesi ayrı hassasiyet koludur; ana kurala dahil edilmez. H4 mum kapanınca kurulum bilinir; koşul bozulursa sinyal yok. Oran hesabında long %61,8 seviyesi `H−0,618 range`, short `L+0,618 range`.
- **Alt dilim/giriş:** İkinci H4 kapanışından sonraki **ilk dört tamamlanmış H1** içinde long için `close>open`, alt fitil `min(open,close)−low≥abs(close−open)` ve `low` ilk mumun %61,8 seviyesinin altına inmemiş olsun; short simetrisi. Sıfır gövdeli doji geçersiz. İlk uygun H1 mumunun yüksek/düşük seviyesi tetik olarak dondurulur. İzleyen en çok dört H1 içinde ilk `close>trigger_high` (short `close<trigger_low`) kapanışında sinyal; sonraki ilk uygulanabilir M1 ask/bid ile giriş. H1 geri tepme mumu yalnız **ikinci H4 kapanışından sonra** kabul edilir. Bu süre pencereleri ve kapanış kırılımı bizim test tanımımızdır.
- **Risk/çıkış:** Long stop ilk büyük H4 mumun `%50` düzeyinin `0,1×ATR14_H4` altı, short üstü; girişe göre doğru tarafta değilse işlem yok. Hedef `entry+2,5R` / `entry−2,5R`; 12 H4 mum süre çıkışı. En çok özsermayenin %0,25'i risk, aynı paritede tek pozisyon, lot aşağı yuvarlanır. Spread, komisyon, kayma, FX swap, gap ve stop/hedef aynı M1 barda belirsizse stop önceliği dahil. 2R ve 3R yalnız ayrı ön kayıtlı duyarlılık kolları; sonuçtan sonra en iyisini seçme yok.
- **Ayrıştırma:** [JI128A](../batch_128/STRATEGIES.md) tek mum %50 fitil reddi ve aynı ilk büyük mumdan düz %50 limit giriş kontrolü ile **aynı parite/dönem/maliyet** altında karşılaştır. İkinci H4 teyidi, %61,8 fitil sınırı, alt H1 geri tepme ve tetik kırılımının her birinin ayrı ablation sonucu, sinyal kaybı, net R, maksimum düşüş, örneklem dışı ve işlem sayısı raporlansın. Kaynağın “yüksek başarı olasılığı” ölçülmüş veri değildir.

**Parti sonucu:** 3 kitap, 144 sayfa, 1 yeni aday. Toplam **495 tamamlanmış ayrı kitap, 21.860 sayfa, 396 doğrulanmamış strateji adayı**.
