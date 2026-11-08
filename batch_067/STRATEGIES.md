# Kitap okuma 067 — Dirençte karşı mum, çift dip geri testi, ilk 9/30 geri çekilmesi

**Kapsam:** Üç PDF'nin gerçek **69 + 66 + 47 = 182 sayfası** sıralı metne çıkarılıp incelendi. Atıflar PDF sayfasıdır. Kaynakta eksik sayısal eşikler **bizim test tanımımızdır**. Backtest, paper test ve emir yapılmadı.

## 1. Forex Profit Farm — Forex Sihirli Mum Çubukları

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Forex Sihirli Mum Çubukları - Forex Profit Farm (69 sayfa) - @eseckal.pdf>) · [Tam metin](01_magic_candles.txt)

**Kaynak:** İki kez gözlenen S/R seviyesine yeniden yaklaşınca küçük boğa mumundan sonra daha büyük ayı mumunun dirençte dönüş uyarısı olması s. 31–35'te. Yutan mum s. 35–36, sabah/akşam yıldızı s. 37–40, EMA200'ün S/R bağlamı s. 63–64'te. Mum kapanmadan işlem kararı verilmemesi s. 65–66'da açıkça söylenir. Yazarın yıldızlar için kişisel `%65+` doğruluk ifadesi (s. 40) örneklem ve maliyet bilgisi içermez; sonuç kabul edilmez. Diğer pek çok kalıp önceki kitaplarda var.

### FP67 — Teyitli dirençte küçük boğa mumunu izleyen büyük ayı mum

- **Seviye:** H4'te 3 sol/3 sağ barla teyitli iki swing high, fark `≤0,2×ATR14_H4`; ikincisinin teyit kapanışında direnç iki high ortalaması olarak dondurulur. Long simetri için iki swing low talep seviyesi. Bunlar kitabın çizimle seçtiği seviyeyi kodlanabilir kılan bizim eşiklerimizdir.
- **Sinyal:** Dirence yeniden temas eden kapanmış H4 boğa mumunun gövdesi önceki 20 H4 gövde medyanından küçük olsun; sonraki **tam H4 mum** ayı, gövdesi ilk gövdenin `≥1,5` katı ve `close<first.open` olsun. İkinci mumun high'ı dirençten `≤0,2×ATR` uzaklıkta olmalı. İlk mum sonradan yeni S/R pivotu diye seçilmez. Long için destek üzerinde küçük ayı ardından büyük boğa simetriği. Gövde/tolerans bizim ölçümümüzdür.
- **İcra/risk:** İkinci mum kapanışı sonrası ilk uygulanabilir 1m short; stop `max(level,first.high,second.high)+0,1×ATR`, long tersi. 2R veya 18 H4 süre. Stop yanlış tarafta/maliyetten dar ise atla; aynı 1m stop önce. Aynı iki mum desenini S/R filtresiz ve yalnız yutan gövde tanımıyla kıyasla; önceki engulfing ve MB65 S/R kuyruğu adaylarıyla çakışma ve ek katkı raporla.

## 2. Trading Technicals — Teknik Analiz: Trading Sanatı

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Teknik Analiz - Trading Sanatı - Trading Technicals (Orijinal) (66 sayfa) - @eseckal.pdf>) · [Tam metin](02_technical_art.txt)

**Kaynak:** İngilizce görsel katalog; mum ve formasyonların çoğu önceki kitaplarla aynı (s. 5–33, 43–62). Kaynak s. 53'te üçlü dip için kırılım sonrası genellikle geri test olmadığını, s. 54'te **çift dipte boyun çizgisi kırılımından sonra geri test ve sıçrama beklendiğini** açıkça ayırır. İki swing noktasıyla S/R çizimi s. 44–45. Bu “genellikle” ifadeleri veriyle gösterilmiş oranlar değildir. VWAP için seans içi ilk üst kapanış fikri s. 39'da, fakat 7/24 kriptoda seans çıpası keyfidir; bu partide öncelik verilmez.

### TT67 — Çift dip boyun kırılımından sonra ilk geri test

- **Şekil:** H4'te 3 sol/3 sağ tamamlanmış barla teyitli iki swing low `L1,L2`, fark `≤0,25×ATR14_H4`, araları 6–40 H4. Aradaki teyitli high boyun `N`; `N−max(L1,L2)≥1×ATR`. İkinci dip ancak üç sağ bar kapandığında kullanılabilir. Boyun ve dip aralığı o anda dondurulur. Kaynakta olmayan tolerans/pencere bizimdir.
- **Tetik:** İkinci dip teyidinden en çok 16 H4 sonra ilk `close>N+0,1×ATR` kırılımı. Sonraki en çok altı tam H4 mumda `low≤N+0,1×ATR` ve `close>N` ilk boyun geri testi; kapanış sonrası ilk uygulanabilir 1m long. Geri test mumundan önce `close<min(L1,L2)` yapı iptal. Short için çift tepe simetrisi kaynak bölümündeki genel dönüş kalıbından türetilmiş kol, ana kaynak fikri long çift diptir.
- **Risk/karşılaştırma:** Stop `min(L1,L2)−0,1×ATR`; hedef `N+(N−min(L1,L2))` ölçülü hareket veya 30 H4 süre. Hedef girişten yukarıda değil/ödül-risk `<1` ise atla; stop yanlış tarafta/maliyetten dar ise atla. Aynı 1m stop önce. Kırılımda hemen giriş ve geri test bekleyen kolları, ayrıca üçlü dip kırılımıyla geri test sıklığını karşılaştır; önceki çift dip/SR flip adaylarıyla olay örtüşmesi raporla.

## 3. Galen Woods — Düşünen Trader

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Düşünen Trader - Galen Woods (47 sayfa) - @eseckal.pdf>) · [Tam metin](03_thinking_trader.txt)

**Kaynak:** Kitap çoğunlukla işlem sıklığı, öğrenme, risk ve seçicilik üzerinedir. Somut örnek: **yeni 9/30 kesişiminden sonraki ilk geri çekilme**, stop sinyal mumunun bir tick ötesi, hedef önceki trend ekstremi, seviyeleri değiştirmeme (s. 13–16). Belirli işlem saatlerini geçmiş veriyle seçmenin bir örneği s. 24–27'de; aynı örneklemde seçip performansı yine aynı örneklemde raporlamak ileriye dönük kanıt değildir. Dar doji aralığı, trende aykırı kapanış, hedefe kadar engel S/R ve aşırı geniş sinyal mumundan kaçınma önerileri s. 37–40'ta. Kitap 9/30 ortalamalarının türünü bu PDF'de açıklamaz.

### GW67 — Yeni 9/30 kesişiminden sonra yalnız ilk geri çekilme

- **Trend:** H1 kapanmış mumlarda EMA9 ve SMA30 **bizim ortalama türü seçimi**. Long için `EMA9[t−1]≤SMA30[t−1]`, `EMA9[t]>SMA30[t]` ilk kesişim; short simetrik. Kaynağın 9/30 adı dönemleri verir, türleri burada vermediği için bu sürüm kesin kaynak reproduksiyonu değildir. En az 100 H1 ısınma.
- **İlk geri çekilme:** Kesişim kapanışından sonraki en çok 12 H1 içinde fiyatın ilk `low≤EMA9` ve `close>SMA30` H1 barı long sinyal; short `high≥EMA9` ve `close<SMA30`. Öncesindeki herhangi bir EMA9 teması varsa sonraki bar yeni “ilk” sayılmaz. Kesişimden sonra SMA30'un tersine kapanış veya karşı kesişim olursa yapı iptal. Önceki trend high hedefi, sinyal anına kadar görülen `max(high)`; short low simetriği. On iki bar penceresi ve tam sinyal tanımı bizimdir.
- **Risk/icra:** Sinyal kapanışı sonrası ilk uygulanabilir 1m giriş. Long stop sinyal low `−1 tick`, short high `+1 tick`; hedef sinyalden önce gözlenmiş trend high/low. Hedef girişin lehe tarafında değil veya ilk ödül/risk `<1` ise atla. 12 H1 süre sınırı bizim; stop/hedef dondurulur, elle kaydırılmaz; aynı 1m stop önce. Tüm geri çekilmeler ve yalnız ilk geri çekilme, ayrıca EMA9/SMA30 ile EMA9/EMA30 varyantları karşılaştırılır. İşlem saati filtresi ancak **iç eğitim döneminde seçilip** dış test döneminde sabitlenirse ayrı hipotez olur; s. 24–27 yüzdeleri taşınmaz.

## Ortak test sözleşmesi

Üç aday da yalnız kapanmış mum, o ana dek teyitli pivot ve önceden dondurulmuş seviye kullanır. Giriş/çıkışta uygulanabilir 1m fiyat, ücret, spread, kayma, perpetual funding, eksik veri ve çakışan pozisyon politikası gerekir. Zaman sıralı ayrılmış doğrulamada işlem sayısı, net R, maksimum düşüş ve yalın taban çizgisi olmadan kârlılık iddiası kurulmaz.
