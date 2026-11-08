# Kitap okuma 042 — Ichimoku, MACD trend çizgisi ve Fibonacci altın bölge

**Kapsam:** 55 + 23 + 34 = **112 PDF sayfası**. Üç PDF'nin tüm sayfaları sırayla metne aktarıldı; Fibonacci'nin metin çıkmayan s. 30–33 sayfaları görsel incelendi. Atıflar PDF sayfasıdır. Kaynak kuralları ile bizim kripto için ölçülebilir test önerilerimiz ayrıdır. Backtest, paper test ve emir yapılmadı.

## 1. Gabor Kovacs — Yeni Başlayanlar İçin Ichimoku

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Yeni Başlayanlar İçin Ichimoku - Gabor Kovacs (55 sayfa) - @eseckal.pdf>) · [Tam metin](01_ichimoku_kovacs.txt)

**Kaynak:** Tenkan 9, Kijun 26, Senkou B 52, Chikou 26 bar geriye, bulut 26 bar ileri çizilir (s. 7–9). Fiyatın bulut dışında olması, Tenkan/Kijun sırası, Chikou'nun fiyat/Kijun/bulut konumu ve gelecek bulut rengi dört asgari kontroldür (s. 18, 26–28). Güçlü Tenkan/Kijun kesişimi long için bulut üstünde, short için bulut altındadır (s. 17, 22). Alternatif girişte fiyat bulut dışında **kapanmalı** ve Chikou aynı yönü doğrulamalıdır; Chikou bulutta kaldığında giriş ertelenir (s. 23–24, 52–53). M15 girişten önce H1 ve H4'te dört kontrolün aynı yönü göstermesi önerilir (s. 27–28). Stop karşı bulut kenarı ve tampon veya son swing; fiyatın Kijun'u ters geçmesi çıkış seçeneklerindendir (s. 25, 54). Kitap bulut kalınlığına nitel önem verir fakat sayısal eşik vermez (s. 11).

### I42 — H4/H1 onaylı M15 bulut çıkışı

- **Bizim zaman hizası:** Her zaman diliminde yalnız tamamlanmış barlardan `Tenkan[t]=(HH9+LL9)/2`, `Kijun[t]=(HH26+LL26)/2`, `Araw[t]=(Tenkan[t]+Kijun[t])/2`, `Braw[t]=(HH52+LL52)/2`. `t` konumundaki bulut `Araw[t−26],Braw[t−26]`; geleceğe çizilen `Araw[t],Braw[t]` yalnız bulutun gelecekteki rengini değerlendirmek içindir. Chikou `close[t]` değerinin `t−26` üzerinde çizilmesidir: long için `close[t]` o tarihteki fiyat, Kijun ve o tarihe çizilmiş bulutun üstünde olmalı. Bunların tamamı `t` kapanışında bilinir; geçmişe çizilen Chikou geçmişte sinyal oluşmuş gibi sayılmaz. Her dilimde en az 104 bar ısınma.
- **Filtre ve olay:** M15 `t` kapanışında `close[t−1]` bulutun içinde/altında ve `close[t]` bulut üst kenarının üzerinde olsun. M15'te Tenkan>Kijun, Chikou doğrulaması ve `Araw[t]>Braw[t]` sağlansın. Aynı anda bilinen son **tam kapanmış** H1 ve H4 barlarında fiyat bulut üstü, Tenkan>Kijun, Chikou fiyat/Kijun/geçmiş bulut üstü ve gelecekteki bulut yükseliş renkli olsun. Short tüm eşitsizliklerin tersi. Bulut içi fiyat veya Chikou varsa işlem yok. H1/H4 kapanmamış barları kullanma.
- **İcra/risk:** M15 kapanışını izleyen ilk uygulanabilir 1m fiyatından giriş. Long ilk stop sinyal anındaki M15 bulut alt kenarı `−0.1 ATR14_M15`, short karşı simetri; stop girişin yanlış tarafındaysa veya beklenen işlem maliyetinin iki katından yakınsa işlem yok. M15 kapanışı Kijun'u ters geçtiğinde sonraki uygulanabilir 1m'de çık; ayrıca stop ve 32 M15 bar süre sınırı. ATR tamponu, ısınma ve süre **bizim** test seçimlerimizdir.
- **Karşılaştırma:** Aynı bulut kırılımını H1/H4 filtresiz, yalnız H1 filtreli ve Chikou filtresiz dene. Batch004 çok zamanlı Ichimoku ve batch041 I41 Kijun kesişimi ile olay ve getiri örtüşmesini ölç; I42 bağımsız yeni gösterge ailesi değildir. Bulut kalınlığını sonradan optimize edilmiş eşik olarak ekleme.

## 2. MACD Trend Takip Stratejisi

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 7/Baskı 7/MACD Trend Takip Stratejisi (23 sayfa) - @eseckal.pdf>) · [Tam metin](02_macd_trend.txt)

**Kaynak:** Varsayılan MACD ayarı ve tercihen H4/D1 anlatılır (s. 2, 7–8). Long örneğinde MACD çizgisinin önce yüksek tepe, sonra daha alçak tepe yapması ve bunlara fiyat tepesinin eşlik etmesi istenir; iki MACD tepesi birleştirilip çizgi yukarı kırılınca giriş yapılır (s. 10–15). Başlıkta “satış kuralları” yazmasına karşın s. 15–19 metni ve stop tarifi **long örneğini** anlatır; short tersidir. MACD sinyal çizgisi kesişimi tek başına yeterli sayılmaz; s. 15 kesişimle trend çizgisi kırılmasının birlikteliğini belirsiz ifade eder. Stop son fiyat swing dibinin 5–10 pip altı, çıkış ters MACD/sinyal kesişiminin **bar kapanışıyla** teyididir (s. 16, 18–19). Forex pipi kriptoya birebir taşınamaz.

### M42 — Onaylı MACD tepe çizgisi kırılımı

- **Bizim gösterge/pivot tanımı:** H4 kapanışlarında `MACD=EMA12(close)−EMA26(close)`, `signal=EMA9(MACD)`. MACD yerel tepesi ancak sağındaki 2 H4 bar kapandıktan sonra onaylanır; solda da 2 bar daha düşük MACD gerekir. Sırasıyla yüksek tepe ve alçak tepe oluşsun; eşlik eden fiyat tepeleri ilgili ±2 bar penceresinde onaylı olsun. Eşit değerlerde pivot yok. En az 200 bar ısınma. Bu 2+2 ve eşleşme penceresi **bizim** tanımımızdır.
- **Olay:** İkinci tepe **onaylandıktan sonraki** barlar için iki MACD pivotundan geçen azalan doğruyu ileri uzat. İlk `MACD[t−1]≤line[t−1]` ve `MACD[t]>line[t]` kapanışında, ayrıca `MACD[t]>signal[t]`, long sinyali ver. Doğru çizgisini her yeni pivota göre geçmişe dönük yeniden çizme. Short için iki MACD dibiyle yükselen doğru, sonra aşağı kırılım ve `MACD<signal`. Sinyal çizgisi koşulunu temel kola koymak s. 15'in temkinli yorumu; yalnız çizgi kırılımı ayrı ablation.
- **İcra/risk:** Takip eden ilk uygulanabilir 1m fiyatı. Stop long için sinyal anında **onaylı son fiyat swing dibi** `−0.1 ATR14_H4`, short için tepe `+0.1 ATR`; yanlış tarafta veya fazla dar stopta işlem yok. Ters MACD/sinyal kesişimi H4 kapanışında oluşursa sonraki 1m'de çık; stop ve 30 H4 bar zaman sınırı. ATR tamponu/süre bizim, son swing stopu ve ters kesişim kaynakta.
- **Karşılaştırma:** Yalnız MACD/sinyal kesişimi, yalnız çizgi kırılımı ve birleşim; batch024 MACD trend filtresiyle aynı olay evreninde kıyas. MACD pivotlarının sağ bar teyidi atlanırsa geçmişten bakarak seçilmiş tepeyle lookahead olur.

## 3. Fibonacci Golden Zone Trading Stratejisi

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 6/Baskı 6/Fibonacci Golden Zone Trading Stratejisi (34 sayfa) - @eseckal.pdf>) · [Tam metin](03_fibonacci_golden_zone.txt) · [Özet kural görseli s. 32](fib_visual-32.png)

**Kaynak:** Swing high/low iki sol ve iki sağ komşu mumla tanımlanır (s. 6); yükselişte dip→tepe, düşüşte tepe→dip Fib çizilir (s. 7). Altın bölge %38,2–61,8; varsayılan giriş %61,8 testinin ardından ana trend yönünde kapanıştır, H1 tercih edilir (s. 9, 13–17). Stop %100 düzeltme yani önceki karşı swing ötesi, hedef önceki trend swing ekstremi ötesidir (s. 18–20). Tescilli Golden Zone Dashboard çoğu zaman diliminde yönü teyit eder ve tersine dönerse erken çıkış önerilir (s. 10–11, 15–16, 20, 22; görsel s. 32). Gösterge algoritması verilmediği için panel sinyali **birebir yeniden üretilemez**. S. 26–27 tüm zaman dilimleri güçlü uyumluyken %50 giriş istisnası var; bunu temel kuralla karıştırmıyoruz. S. 30 ve 32 yalnız örnek görsel/özet kural, s. 31 ve 33 boş sayfadır.

### F42 — Onaylı swing ve %61,8 retest

- **Bizim noktasal yapı:** H1'de 2 sol/2 sağ barla teyitli pivotlar kullan. Son tamamlanmış yükselen impuls için eski teyitli dip `L`, sonraki teyitli tepe `H` ve onay anından sonra `H` üstünde yeni tepe oluşmamış olsun. Long `fib618=H−0.618(H−L)`, altın bölge `[H−0.618R,H−0.382R]`. Düşüş impulsu için son teyitli tepe `H`, sonraki dip `L`, short `fib618=L+0.618(H−L)`. Pivot ancak iki sağ bar kapanınca bilinir; yeni impuls seçimini ileri tarihe göre düzeltme.
- **Trend/panel vekili:** Kaynağın yüksek tepe/yüksek dip veya düşük tepe/düşük dip tarifini, H1'de son iki teyitli pivot çiftinin yönüyle sabitle. Panel algoritması bilinmediğinden **ayrı** ablation olarak bilinen son tam kapanmış H4 ve D1'de aynı pivot trend yönü koşulunu dene; buna kaynak panelinin eşdeğeri deme.
- **Olay:** İmpuls onayından sonra ilk H1 barında long `low[t]≤fib618` ve `close[t]>fib618`, short `high[t]≥fib618` ve `close[t]<fib618`; bar kapanışından önce bölgeye temas ve geri dönüş bilinmez. Test öncesi ilgili impulsun %100 seviyesinin ötesinde H1 kapanışı olmuşsa kurulum iptal. Kaynak %61,8 testini ister; kısa süreli gölge taşmasını tolere edip etmeme ayrı hassasiyet kolu.
- **İcra/risk:** Sonraki ilk uygulanabilir 1m giriş. Long stop `L−0.1 ATR14_H1`, short `H+0.1 ATR`; kaynak %100 ötesi, ATR tamponu bizim. Hedef long önceki `H+0.1 ATR`, short `L−0.1 ATR`; ayrıca 48 H1 bar süre ve stop. Hedef/stop aynı 1m içinde görünürse kötümser sıra varsayımı. Stop yanlış tarafta veya hedef net maliyetten sonra pozitif değilse işlem yok. Tescilli panel ters sinyali olmadan erken çıkış uygulanamaz; H4/D1 vekilinin tersine dönmesi ayrı deney.
- **Karşılaştırma:** 38,2–61,8 bölgesinde herhangi bir temas, yalnız %61,8 retest, panel vekiliyle ve vekilsiz; önceki Fibonacci/pullback adaylarıyla ortak işlem tarihlerini ve koşullu getiriyi karşılaştır. Seçilmiş geçmiş grafik örnekleri başarı kanıtı değildir.

## Ortak değerlendirme sırası

I42 için Chikou/bulut hizası, M42 için pivotun sağ bar onayı, F42 için swing teyidi ve tescilli panel eksikliği ilk teknik kapılardır. Her adayı sabit point-in-time varlık evreni, tam mum kapanışı sonrası giriş, ücret/spread/kayma/funding, aynı bardaki stop/hedef sırası ve zaman sıralı dış örneklemle test etmek gerekir. Bu parti yalnız okunmuş ve test taslağına kaydedilmiştir; hiçbir adayın kârlılığı gösterilmemiştir.
