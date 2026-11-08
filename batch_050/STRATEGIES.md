# Kitap okuma 050 — Inside bar, yutan mum ve aralık kırılımı

**Kapsam:** 15 + 31 + 54 = **100 PDF sayfası**. Üç PDF'nin tüm sayfaları numaralı, sıralı metne çıkarıldı; görsel ağırlıklı *Inside Bar* kitabında s. 3, 7, 9, 13–15 ayrıca görsel denetlendi. Atıflar PDF sayfasıdır. Kaynak fikri ile **bizim** kripto/kapalı mum test sözleşmesi ayrı tutuldu. Backtest, paper test ve emir yapılmadı.

## 1. Colibri Trader — Inside Bar

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Inside Bar (15 sayfa) - @eseckal.pdf>) · [Tam metin](01_inside_bar.txt)

**Kaynak:** İkinci barın tamamı ilk barın high–low aralığında kalır (s. 3). Çizimler inside barı destekte boğa dönüşü, dirençte ayı dönüşü (s. 7–8) ve trend içinde devam sinyali (s. 9–12) olarak gösterir. s. 13'te long için inside bar yakınından giriş, ana bar altında stop ve üst dirençte olası hedef yerleşimi görseldir; net fiyat formülü verilmez. s. 14–15 çizimleri **Hikkake** için ilk kırılmanın ters yöne dönmesini ve inside bar çizgisinin sonradan teyit geçilmesini gösterir. Çizimden tek başına getiri veya evrensel başarı oranı çıkarılamaz. Kitap çoğunlukla görseldir; alternatif inside bar varyantları s. 4–6'da sistematik bir seçim kuralı vermez.

### IB50 — Trend içi ana mum aralığının kapanışla kırılması

- **Bizim şekil ve bağlam:** H1 gerçek OHLC; `high[t]<high[t−1]` ve `low[t]>low[t−1]` tam kapsanan inside bar. Eşit sınır ayrı hassasiyet kolu. Ana mum `t−1` seviyeleri inside bar kapanışında dondurulur. Son tam H4 `close>EMA50_H4` ve EMA50 artıyorsa yalnız long, düşüşte simetrik short. Kaynağın çizimsel “trend” kavramının bu EMA vekili **bizim** seçimimizdir.
- **Sinyal:** Inside kapanışından sonraki en çok 3 H1 barda ilk `close>motherHigh` long veya `close<motherLow` short; fiyat yalnız fitille aşarsa sinyal yok. Ters yöne H1 kapanışı, kurulumun süresini bitirir; aynı inside bar iki işlem üretmez. Sonraki uygulanabilir 1m fiyatından giriş. Long stop `motherLow−0.1 ATR14_H1`, short `motherHigh+0.1 ATR`; 2R hedef veya 12 H1 bar süre. 0.1 ATR, 3 ve 12 bar **bizim** seçimlerimiz.
- **Hikkake ayrı kol:** Boğa için inside kapanışından sonraki ilk 2 H1 barda `low<motherLow` ve `close<motherLow` yanlış aşağı kırılımı; sonraki en çok 3 H1 kapanışından ilki `close>insideHigh` olursa long. Ayı simetrik: ana high üstünde kapanış sonra inside low altında kapanış. Stop yanlış kırılma ekstremi `±0.1 ATR`; 2R/12 H1. Bu, s. 14–15 teyit çizgisinin **bizim** açık yorumudur; çizim stop/süre eşiğini vermez. Yanlış kırılma barında eski sinyal üretilmez.
- **Karşılaştırma:** Çıplak inside bar, H4 trend kapılı inside bar ve Hikkake ayrı kolları; önceki inside bar/kanal kırılımı adaylarıyla aynı olay örtüşmesi. Destek/direnç dönüşü s. 7–8 ayrıca noktasal seviye yöntemi kararlaştırılmadan test adayına zorla eklenmez.

## 2. Timon Weller — The Engulfing Trader

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/The Engulfing Trader - Timon Weller (31 sayfa) - @eseckal.pdf>) · [Tam metin](02_engulfing_weller.txt)

**Kaynak:** Yazar günlük/haftalık çizgi grafiğinde en az iki güçlü temasla yatay destek/direnç belirleyip orada yutan mum arar (s. 4–8). Tam gövde yutma ile kısmi gövde/yüksek veya düşük yutma varyantlarını birlikte gösterir (s. 9–11). Kırılan desteğin dirence, direncin desteğe dönüşebileceğini anlatır (s. 12). Giriş sinyal mumu **kapandıktan** sonra ekstrem üzeri/altı bekleyen emir; ideal olarak ertesi günlük mumda tetiklenme, alternatif %50 geri çekilme veya fitil aşımıdır (s. 14–17). Kaynak iki parçalı işlem, ilk parçada 1R hedef, ikinci parçada karşıt yutan mum/sonraki yapıya kadar devam ve opsiyonel başabaş önerir (s. 18–22). s. 6'daki “%70 üzeri sıçrama” ve s. 16'daki %50 geri çekilme sıklığı bağımsız doğrulanmış sonuç kabul edilmez; dış örneklemde ayrıca ölçülür. Kaynaktaki 9–15 pip ve işlem başı %2 sermaye Forex örneği, kriptoya aynen aktarılmaz.

### EW50 — Önceden teyitli düzeyde tam gövde yutan mum

- **Bizim yapı:** D1 gerçek kapanışlarıyla, 2 sol/2 sağ D1 sonrası teyitli pivot kapanışları; son 180 kapanmış D1 içinde aynı yönde en az iki pivot kapanışı `≤0.3 ATR14_D1` yakınlıkta ise seviye, son pivot **teyit edildiği anda** dondurulur. Aynı geçmişten seçilebilen çoklu seviyelerde son teyitli ve en yakın düzey tek olarak seçilir. `180`, `0.3 ATR` ve pivot tanımı, s. 4–5'teki elle çizilen “iki temas”ın **bizim** vekilidir; haftalık düzey ayrı kol olabilir.
- **Şekil ve olay:** Boğa için önceki D1 kırmızı `close[t−1]<open[t−1]`, sinyal D1 yeşil `close[t]>open[t]`, `open[t]≤close[t−1]`, `close[t]≥open[t−1]`; gövde tam yutulmalı. Sinyal mumunun gerçek `low`'u veya kapanışı önceden dondurulmuş desteğe `≤0.3 ATR` mesafede. Ayı için renk/yutma ve direnç simetrik. Kısmi yutma kaynakta kabul edilse de ölçüsü net olmadığından **ayrı** test kolu; ana kol yalnız tam gövde. İkinci mum kapanmadan aday sinyal değildir.
- **İcra/risk:** Sinyal D1 kapandıktan sonraki **tek D1 süresince** long `signalHigh+0.1 ATR14_D1` alım stopu, short `signalLow−0.1 ATR` satış stopu; sonraki 1m barlarda tetiklenme kontrolü. Giriş olmazsa iptal. Long stop `signalLow−0.1 ATR`, short `signalHigh+0.1 ATR`. Pozisyonun %50'si 1R'de kapanır; kalan %50 ilk ters **tam gövde yutma** D1 kapanışından sonra veya 10 D1 bar sürede çıkar. 1R sonrası kalan stopu ücret dahil başabaşa taşıma **ayrı kol**. Kaynak stopu yapıya/pip'e göre seçer; ATR ve 10 bar **bizim** kripto uyarlamamızdır.
- **Karşılaştırma:** Sadece yutma, sadece iki temaslı seviye, birleşim; önceki engulfing/destek direnç adaylarıyla sinyal örtüşmesi. Limitle %50 geri çekilme ayrı kolunda **tetiklenmeyen** aday işlem sayılmaz; fırsat kaybı ayrıca raporlanır. Kaynak örnekleri seçilmiş işlem grafikleridir.

## 3. John Connors — Koparma Ticareti

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Koparma Ticareti - John Connors (54 sayfa) - @eseckal.pdf>) · [Tam metin](03_breakout_connors.txt)

**Kaynak:** Önce iki sınırlı yatay fiyat dikdörtgeni tanımlanır (s. 12–16); giriş, aralık **dışında güçlü kapanan**, aralık barlarından büyük fakat aşırı büyük olmayan mumdur (s. 16–17, 19–25). Başarısız kırılmada fiyat aralığa dönmesi nedeniyle stop aralık genişliğinin %10–15'i **içine** konur (s. 30–32). En az 2R ilk hedef önerilir (s. 33–36), pozisyonun kalan yarısı için 2R sonrası başabaş ve EMA20 karşı tarafında bar kapanışında çıkış seçeneği anlatılır (s. 41–46). Üst zaman dilimindeki baskın trendle ters işlemi süzme fikri vardır (s. 47–49). Kitabın varsayımsal %40/%50 isabet simülasyonları (s. 36–40) gerçek kripto geri testi değildir.

### BC50 — Yatay kutudan ölçülü gövdeli kapanış kırılımı

- **Bizim kutu:** H1 gerçek OHLC'de sinyal barından **önceki 24 tamamlanmış H1** için `boxHigh=max(high)`, `boxLow=min(low)`, `width=boxHigh−boxLow`. Kutu içindeki en az 2 teyitli (2 sol/2 sağ) tepe `boxHigh−0.15×width` üstünde ve en az 2 dip `boxLow+0.15×width` altında; `width/median(ATR14_H1,24)` değeri `[1.5,6]` aralığında. Kutu sonda dondurulur; bunlar kitaptaki elle çizilen dikdörtgen için **bizim** kuralımızdır. Sağ pivot teyidi tamamlanmadıysa sayma. Sıfır genişlik/geçersiz ATR atla.
- **Kırılım:** Long `close>boxHigh+0.1 ATR14_H1`, short `close<boxLow−0.1 ATR`; sinyal mumunun gerçek gövdesi kutudaki önceki 24 mumun **en büyük gövdesinden büyük** ve `range≤2×` önceki 24 range medyanı; `close` kendi range'inin long üst %25 / short alt %25'inde. Gövde kuralı s. 19'daki örneğe, üst range sınırı s. 23'teki aşırı sıçramayı dışlamaya dayanır; 0.1 ATR, 2×, %25 **bizim** eşiklerimiz. Tek kutuda ilk geçerli kapanış; sonraki barlarda kutu yeniden kurularak aynı hareket için tekrar sinyal verme.
- **İcra/risk:** Kapanış sonrası ilk uygulanabilir 1m giriş. Long stop `boxHigh−0.125×width`, short `boxLow+0.125×width` (kaynak %10–15); stop girişin doğru tarafında ve toplam maliyetin iki katından geniş olmalı. Basit kol 2R hedef veya 48 H1 bar. Koşucu kol: 2R'de %50 kapat, kalanı maliyetleri karşılayan başabaş stop ve ilk H1 `close<EMA20_H1` (short `>EMA20`) sonrası sonraki 1m çıkış; 48 H1 azami süre. Stop/hedef aynı 1m'de kötümser öncelik. Üst tam H4 EMA50 yön filtresi ayrı ablation kolu.
- **Karşılaştırma:** Önceki range/donchian/ORB kırılım adaylarıyla aynı barlarda sinyal örtüşmesi; “ölçülü büyük gövde” ve aralığa 12.5% iç stopun ayrı katkısı. Hem yalın 2R hem koşucu kol maliyet/sermaye kullanımıyla kıyaslanır; kitap simülasyonu sonuç olarak tekrarlanmaz.

## Ortak test notu

Point-in-time veri ve varlık evreni, yalnız kapanmış bar, sonraki uygulanabilir 1m fiyatı, ücret/spread/kayma/funding, eksik bar, pozisyon çakışması ve zaman sıralı dış örneklem gereklidir. IB50'nin görsel teyit çizgisi ve EW50'nin elle çizilen düzeyi en önemli yorum riskleridir; açıkça tanımlanmayan varyantlar temel stratejiye gizlice eklenmemelidir. Bu partide kârlılık ölçülmedi.
