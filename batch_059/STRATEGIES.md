# Kitap okuma 059 — Kama süpürmesi, maliyet filtresi, EMA21 retesti

**Kapsam:** 48 + 57 + 68 = **173 PDF sayfası**. Üç PDF'nin tüm sayfaları sıralı metne çıkarıldı; atıflar PDF sayfasıdır. “Altın Teknik” bu partiden çıkarıldı: 64 sayfalık PDF'nin metin katmanı yalnız filigran veriyor, dolayısıyla görsel/OCR incelemesi yapılana kadar **okunmuş sayılmadı**. Aşağıdaki sayısal eşikler kaynakta yoksa **bizim test vekilimizdir**. Backtest, paper test ve emir yapılmadı.

## 1. Dylan Forexia — Üstün Trader Olmanın Yolu

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Üstün Trader Olmanın Yolu - Forexia (48 sayfa) - @eseckal.pdf>) · [Tam metin](01_superior_trader.txt)

**Kaynak:** Asya sıkışması/Londra kırılımı/NY geri alımı olarak günlük seans şeması (s. 27–28); hafta başındaki eğilimin Çarşamba/Perşembe tersine dönebileceği hipotezi (s. 33–36). İmza işlem, M15 kama kırılımının önceden var olan gün/hafta high-low'a doğru gidip seviyeyi süpürmesi, sonra kırılımın tersine giriş olarak anlatılır (s. 37–39, 43–47). Forex pip bazlı 30/50/100 hedef ve çoklu ekleme kaynak uygulamasıdır (s. 46); kriptoda taşınmaz. Kitabın medya/kurum/piyasa kontrolüne ilişkin geniş iddiaları (s. 2–26) veri sunmadığı için fiyat sinyalinin nedeni veya kârlılık kanıtı sayılmaz. PO3 ve sahte kırılım adaylarıyla belirgin örtüşme vardır.

### FX59 — M15 kama kırılımının önceki gün ekstremi süpürmesi ve ters kapanışı

- **Kama:** M15'te 2 sol/2 sağ kapanmış barla teyitli son iki lower high ve son iki higher low (short/long için aynı sıkışma). Tepelerden inen üst ve diplerden çıkan alt çizgi, iki pivot teyit edilince dondurulur; son pivotlar arası 4–40 M15 bar ve çizgiler ileriye doğru birleşmeli. Sonradan yeni pivotla çizgi değiştirme. Bu, kaynağın görsel kama tanımının bizim ölçülebilir hali.
- **Süpürme ve yön:** UTC'de önceki **tamamlanmış** gün high/low'unu gün başında dondur. Long için ilk tamamlanmış M15 mum alt kama çizgisinin altında **kapanır**, fitili önceki gün low'unun `0,1×ATR14_M15` altına iner ve kapanışı tekrar önceki gün low'unun üstündedir; short üst çizgi/önceki gün high simetrik. Mum hem kama kırılımı hem likidite süpürmesi taşımalı; bu kaynağın olay sırasının bizim sıkı versiyonudur. Seçili seans kolunda yalnız `America/New_York` 07:00–11:00 yerel saat sinyali; tüm saatler ana kol, çünkü kaynak 15m ve NY çevresi der ama kesin giriş saati vermez.
- **İcra/risk:** Mum kapanışından sonraki ilk uygulanabilir 1m giriş. Long stop sweep low `−0,1×ATR`, short high `+0,1×ATR`; 2R ve 3R ayrı hedef kolları veya 24 M15 bar süre. Stop yanlış tarafta ya da maliyetin iki katından dar ise atla. Aynı 1m stop/hedefte stop önce; tek sinyal/gün/sembol, ekleme yok. Haftanın gününü veri alt grubu olarak raporla; “Çarşamba dönüşü”nü doğrulanmış kural sayma.
- **Karşılaştırma:** Batch054 PQ54, batch057 BM57 ve önceki sweep/FVG adaylarıyla aynı olaylarda çakışma. Kamanın ilave koşulunun yalın önceki gün ekstrem süpürmesine göre işlem sayısı/net R etkisini ölç.

## 2. Christopher Lee — Forex Rüyası

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Forex Rüyası - Christopher Lee (57 sayfa) - @eseckal.pdf>) · [Tam metin](02_forex_dream.txt)

**Kaynak:** Kitap somut al/sat tetikleyicisi vermekten çok perakende işlem maliyeti, kısa vade/orta vade seçimi ve eğitim pazarlaması eleştirisidir. Spreadin tek işlemde küçük görünmesine rağmen sık işlemde toplam getiriyi aşındırabileceği örneği (s. 24–27), örnek işlem maliyeti/uygulanabilirlik tartışması (s. 50–55) ve H4/D1 orta vadeye yönelimi (s. 52–56) vardır. 150 pip günlük sınır, broker teşvikleri ve “profesyonellerle rekabet” genellemeleri kaynaktaki görüşlerdir; bunları piyasa gerçeği olarak doğrulanmış sayma. İşlem kuralı uydurulmaz.

### CL59 — Strateji değil: maliyet/işlem ufku geçiş ölçütü

- **Neden strateji değil:** Kitapta belirli giriş fiyatı, stop, hedef, gösterge veya mum formasyonu yok. Bu nedenle kendi başına backtest sinyali veya paper emir oluşturulmaz; `research_guardrail` olarak saklanır.
- **Nesnel karar sözleşmesi:** Mevcut her aday için, önceden sabit spread+komisyon+kayma+funding altında işlem başına brüt ve net R, ortalama maliyet/R, yıllık devir, maksimum düşüş ve net kâr dağılımını H1-altı ile H4/D1 ufuklarında raporla. Aynı giriş mantığı birden fazla zaman diliminde gerçekten tanımlanabiliyorsa parametreleri önceden sabitleyerek ayrı versiyonları karşılaştır; olmayan H4/D1 sinyali kitap adına icat etme. Net sonucun maliyet varsayımlarına duyarlılığını 0,5×/1×/2× maliyet senaryosuyla test et. Seçim yalnız ayrılmış doğrulama döneminden sonra, gelecekteki veriyle yeniden ayar yapmadan yapılır.
- **Kayda değer sonuç:** Frekansı azaltmak otomatik olarak daha kârlı değildir; kitabın pratik katkısı, maliyetin küçük hedefli adayları nasıl bozduğunu ölçmeyi zorunlu kılmasıdır.

## 3. Price Action El Kitabı

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Price Action El Kitabı (68 sayfa) - @eseckal.pdf>) · [Tam metin](03_price_action_handbook.txt)

**Kaynak:** EMA21 trend ve geri çekilme destek çizgisi olarak kullanılır, fakat dokunuş otomatik alım değildir; ters mum teyidi istenir (s. 13–15). Kırılım sonrası **ilk** retestte yeni trend yönüne giriş (s. 20), fraktalın iki sağ/iki sol mumla ve beşinci mum kapanınca teyidi (s. 21), önceki seviye/arz-talep ve yapı uyumu (s. 22) anlatılır. Stop için swing/fraktal/EMA/ATR, trailing için önceki mum veya EMA, hedef için önceki ekstrem/karşı bölge listelenir (s. 18–19). Uzun fitilden sonra 1–5 gün takip hareketi gerektiği uyarısı vardır (s. 34–35). Bölümlerin önemli kısmı hisse/BankNifty ve görsel örnek; tek başına “EMA21 iyi çalışır” ifadesi performans kanıtı değildir.

### PA59 — H4 fraktal kırılımı sonrası ilk EMA21 retesti ve dönüş mumu

- **Yapı/kırılım:** H4 gerçek mumlar. Swing high/low 2 sol/2 sağ tamamlanmış barla teyitli; fraktal fiyatı yalnız sağdaki ikinci bar kapandığında erişilebilir. Long yalnız `EMA21_H4` yükseliyorsa ve son H4 close EMA üstündeyse; ilk `close>önceden teyitli swingHigh+0,1×ATR14_H4`. Short simetri. Kırılım kapanışında fraktal seviye, EMA ve ATR dondurulur; aynı swing için sonraki kırılımları atla.
- **İlk geri çekilme ve mum:** Sonraki en çok 8 H4 içinde ilk bar `low≤EMA21_H4+0,1×ATR` ve `low≤kırılan swingHigh+0,25×ATR`; short high karşılığı. EMA o bar kapanınca hesaplanır; şartı değerlendirirken yalnız **önceki kapanmış H4 EMA** seviyesini kullan, bugünkü EMA ile bar içinde limit doldurma yok. Temas barı veya sonraki en çok 2 kapanmış H4 bar içinde long için boğa yutan gövde ya da alt fitili en az 2×gövde olan ve EMA üstünde kapanan pin; short simetri. İlk uygun kapanış sinyal, sonraki ilk uygulanabilir 1m giriş. Bu pencereler ve mum ölçüleri bizim sabit yorumumuzdur.
- **Risk/çıkış:** Long stop temas–teyit arası gözlenmiş low `−0,1×ATR14_H4`, short simetri; 2R veya 18 H4 bar süre. Ayrı çıkış kolunda trailing stop her yeni H4 kapanışında önceki **tamamlanmış** H4 low/high'a yalnız lehe taşınır. Stop yanlış tarafta ya da maliyetin iki katından dar ise atla; aynı 1m stop/hedefte stop önce.
- **Karşılaştırma:** Batch053 FD53 ve diğer trend çizgisi/EMA retest adaylarıyla sinyal örtüşmesi. EMA21 ile **ilk** fraktal kırılım retesti kombinasyonunun, sadece fraktal kırılımı veya sadece EMA21 dokunuşuna göre marjinal katkısını ölç.

## Ortak test notu

Varlık evreni, tarih aralığı ve eşikler önceden sabitlenmeli. Kapanmış mum ve point-in-time fraktal, sonraki uygulanabilir 1m dolum, ücret/spread/kayma ve perpetual funding, eksik bar ve çakışan pozisyon politikası gerekir. Zaman sıralı ayrılmış doğrulama, net R, işlem sayısı, maksimum düşüş, maliyet duyarlılığı ve yalın taban çizgisi olmadan kârlılık iddiası yoktur.
