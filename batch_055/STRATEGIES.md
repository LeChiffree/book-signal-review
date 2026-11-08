# Kitap okuma 055 — Zaman pencereli likidite, kanal retesti, taze arz/talep

**Kapsam:** 9 + 19 + 74 = **102 PDF sayfası**. Üç PDF'nin tüm sayfaları numaralı sırayla metne çıkarıldı. Atıflar PDF sayfasıdır. Kaynağın yoruma açık terimleri ile aşağıdaki **bizim ölçülebilir test vekillerimiz** ayrıdır. Backtest, paper test veya emir uygulanmadı.

## 1. Zaman ve Fiyat Teorisi

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Zaman ve Fiyat Teorisi (9 sayfa) - @eseckal.pdf>) · [Tam metin](01_time_price_theory.txt)

**Kaynak:** Günlük 20/40/60 gün, H1 için üç gün ve M1/M5 için üç H4 mum geriye bakma penceresi verilir; dış likidite eski high/low, iç likidite aralık içindeki dengesizlik olarak ayrılır (s. 5). PO3 birikim/manipülasyon/dağılım olarak çerçevelenir (s. 6). Manipülasyon ekstremi ve yapı değişimi arasındaki ayağa 0–1 Fibonacci bağlayıp 1, 1,5, 2, 2,5, 4 uzantılarını hedef alanları diye verir (s. 7). H1 üç günlük ve D1 20/40 günlük seçilmiş örnekler vardır (s. 8–9). “IPDA algoritması” ve ileriye hedef dili piyasanın o seviyelere gideceğinin kanıtı değildir; kaynak net giriş, stop ve doğrulanmış sonuç sunmaz.

### TP55 — Önceki üç gün ekstrem süpürmesi sonrası H1 yapı değişimi ve uzantı hedefi

- **Sabit olay:** Her H1 kapanışında yalnız **önceki 72 tamamlanmış H1** mumun high/low'unu hesapla (24 saatlik kripto günlerinde üç gün); mevcut mum bu pencereye girmez. Long için mevcut H1 `low<önceki72Low−0,1×ATR14_H1` ve `close>önceki72Low`; short simetri. Bu mumun ekstremi manipülasyon ekstremi olarak dondurulur. Kaynağın üç günlük bakışının ve PO3 manipülasyonunun bizim kodlanabilir vekilidir.
- **MSS:** Süpürmeden sonraki en çok 12 H1 mumda long için, süpürme öncesinde **2 sol/2 sağ barla teyit edilmiş** en yeni H1 swing high üstünde kapanan ilk H1; short için swing low altında ilk kapanış. Swing teyidi sweep öncesi gerçekleşmiş olmalı. Önce MSS'ye ters yeni ekstrem olursa kurulumu iptal et. Pencere ve pivot seçimi bizim varsayımımızdır.
- **İcra/hedef:** MSS H1 kapanışından sonraki ilk uygulanabilir 1m giriş. Long stop sweep low `−0,1×ATR14_H1`, short sweep high `+0,1×ATR`. `R=|giriş−stop|` pozitif ve maliyetin en az iki katı olmalı. Temel kol 2R, uzantı kolu için sweep ekstreminden MSS mumunun **kapanışına** kadar mesafe `L` dondurulur; long hedef `MSS close+1×L`, `1,5×L`, `2×L` ayrı kollar; short simetri. Hedef girişin doğru tarafında değilse kolu atla. Kaynağın 2,5/4 uzantılarını ancak yeterli örneklemle, önceden kilitlenmiş hassasiyet olarak incele. 24 H1 bar süre; aynı 1m stop/hedefte stop önce.
- **Karşılaştırma:** Önceki likidite süpürmesi/MSS adaylarıyla aynı olayları eşleştir. Üç günlük pencerenin ve uzantı hedefinin standart 2R karşısındaki marjinal katkısı asıl sorudur. Grafik üzerinde sonradan seçilmiş manipülasyon ayağı kullanma.

## 2. Louisos Alexander — Trend Çizgisi Analizinin Gücünden Yararlanın

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Trend Çizgisi Analizinin Gücünden Yararlanın - Louisos Alexander (19 sayfa) - @eseckal.pdf>) · [Tam metin](02_trendline_power.txt)

**Kaynak:** Çizgi için en az iki tepe/dip, uzun zaman dilimine öncelik, fitil delmesini kapanış kırılmasından ayırma (s. 4–6). Kırılan çizgiye retest ve rol değişimi ana işlem fikridir (s. 6–7). Paralel çizgili kanalın dışına kapanış ve geri test sonrasında yaklaşık **kanal genişliği** kadar hedef önerilir (s. 7–8). Çift dip/tepe için kırılma kapanışı ve retest (s. 11–12), bayrak direği hedefi (s. 13), üçgen türleri (s. 15) ve sahte kırılma uyarısı (s. 19) vardır. Basılı grafikteki “45 derece” (s. 5) eksen ölçeği değişince fiyat kuralı değildir; kullanılmaz.

### TL55 — Teyitli paralel kanal kırılımı, retest ve kanal genişliği hedefi

- **Kanal kurulumu:** H4'te 2-sol/2-sağ kapanmış barla teyit edilen iki yükselen swing low (long için) veya iki düşen swing high (short için); 4–40 H4 bar aralıklı. İki noktadan alt/üst ana çizgi oluştur. Aynı arada teyitli karşı swinglerden en az biriyle ana çizgiye paralel ikinci çizgi geçir; karşı tarafın en dış **önceden teyitli** pivotundan geçen çizgiyi kanal sınırı olarak dondur. Genişlik iki çizginin fiyat farkı ve en az `1×ATR14_H4` olmalı. Yeni pivotlarla geçmiş çizgiyi yeniden uydurma. Bu kanal seçimi bizim nesnelleştirmemizdir.
- **Kırılım:** Long yükselen kanalın **üst** çizgisi üzerinde H4 `close>line+0,1×ATR`, short alçalan kanalın **alt** çizgisi altında simetrik. Fitil geçişi yeterli değildir (kaynak s. 5). İlk kapanıştan sonra en çok 8 H4 mumda kırılan çizgiye `0,1×ATR` toleransla ilk temas ve aynı mumda veya sonraki en çok 2 H4 mumda doğru tarafta yönlü kapanış. Retest gerçekleşmeden sinyal yok.
- **İcra/risk:** Retest teyidi kapanışından sonraki ilk uygulanabilir 1m giriş. Long stop retest ile teyit arasındaki gözlenmiş low `−0,1×ATR`; short simetri. Kaynak hedefi kırılım anında dondurulan kanal genişliğini `breakout_line+width` (short `−width`) olarak uygula; hedef girişin doğru tarafında ve riskin en az 1,5 katı uzaklıkta değilse atla. Ayrı standart 2R hedef kolu; 24 H4 bar süre. Aynı 1m stop/hedefte stop önce.
- **Karşılaştırma:** Batch053 FD53 ve diğer çizgi retestleriyle örtüşme; paralel kanal genişliği hedefinin sabit 2R'ye göre net etkisi. Kanalın seçili grafiğe sonradan uydurulması en büyük veri sızıntısı riskidir.

## 3. Jode Lebin — Profesyoneller Gibi Trade Yapın

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Profesyoneller Gibi Trade Yapın - Jode Lebin (74 sayfa) - @eseckal.pdf>) · [Tam metin](03_trade_like_pros.txt)

**Kaynak:** Arz/talep yapıları RBD, DBR, RBR ve DBD olarak ayrılır (s. 29–32). Bölgenin bazı 1–6 mumluk; arz için üst fitil ile alt gövde, talep için üst gövde ile alt fitil sınırı kullanılır (s. 33–38). Büyük zaman dilimi konum, orta zaman dilimi trend, küçük zaman dilimi giriş için ayrılır (s. 40–45). Bölgeye limit giriş, karşı sınırda stop, karşıt bölge veya 3R hedef örneklenir (s. 47, 52–53, 62). İlk geri dönüşten önce bölge “taze”, sonraki retestlerde tüketilmiş sayılır (s. 54–55); zaman dilimleri arası çakışma (s. 59–60) ve bazdaki uzun fitil/doji uyarısı (s. 64–66) ek filtrelerdir. Kitabın “olasılık çok yüksek/sıfır” ifadeleri ölçülmüş oran değildir.

### PL55 — H4 taze arz/talep bölgesine ilk dönüş; D1 konum ve trend filtresi

- **Bölge:** H4 OHLC'de 1–6 barlık baz: her baz mumunun `|close−open| ≤ 0,5×ATR14_H4`; baz içi toplam high-low `≤1,5×ATR`. Bazı izleyen ilk iki tamamlanmış H4 bar toplamda baz aralığının en az `1,5` katı yönde uzaklaşır ve ikinci bar baz üstünde/altında kapanır; yukarı çıkış talep, aşağı arz. Bölge ikinci ayrılış barı kapanınca **ilk kez** bilinir. Talep üst sınırı baz gövdelerinin max üstü, alt sınır baz low min; arz üst sınır baz high max, alt sınır baz gövdelerinin min altı. Baz/impuls eşikleri bizim objektif vekilimizdir.
- **Konum ve filtre:** Son kapanmış D1'den önceki 20 tamamlanmış D1 mumun high/low aralığını dondur. Long yalnız fiyat bu aralığın alt yarısında ve D1 EMA20 son kapanışta önceki D1 EMA20'den yüksek; short üst yarı ve EMA20 düşüyor. D1 konum ve EMA trendi kitabın çoklu zaman dilimi yaklaşımının bizim ölçülebilir vekilidir. Temel kol filtre olmadan, ikinci kol bu filtreyle çalıştırılmalı; kaynağın görsel “eğri” ve trendiyle özdeş kabul edilmez.
- **Giriş ve çıkış:** Oluşumdan sonra en çok 20 H4 bar içinde bölgeye **ilk** geri dönüşte, long için talep üst sınırına, short için arz alt sınırına limit emir; emir yalnız bölge oluşumu bilindikten sonra yerleştirilmiş sayılır. 1m fiyat gerçekten limite ulaşmazsa dolum yok; boşluk üzerinden bedelsiz dolum varsayma. Long stop bölge altı `−0,1×ATR14_H4`, short bölge üstü `+0,1×ATR`. Dondurulmuş 3R hedef ve 20 H4 bar süre. Karşıt önceden bilinen bölge 3R'den önceyse atla. Aynı 1m stop/hedefte stop önce. Bir bölge ilk temasından sonra sonuç ne olursa olsun tüketilmiş olur.
- **Karşılaştırma:** Önceki arz/talep/OB adaylarıyla aynı olayları eşleştir. “Taze” ilk temas, 1–6 mum baz ve D1 filtrelerinin her birinin ek katkısını ayrı ölç; 3R'yi kaynak performans vaadi olarak yorumlama.

## Ortak test notu

Sinyal anında bilinmeyen pivot, gün high/low, kanal sınırı veya gelecekteki karşıt bölge kullanılmaz. Önceden sabit sembol/veri dönemi, geçmişten geleceğe ayrılmış doğrulama, gerçek 1m uygulanabilir dolum, ücret, spread, kayma, perpetual funding, eksik bar ve çakışan pozisyon politikası gerekir. Net R, örneklem büyüklüğü, maksimum düşüş, alt dönemler, parametre hassasiyeti ve yalın taban çizgileri raporlanmadan stratejilerin kârlı olduğu söylenemez.
