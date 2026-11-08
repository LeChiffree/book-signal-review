# Kitap okuma 154 — kanal dibinde sıkışma kırılımı

Üç ayrı PDF'nin **50 + 46 + 8 = 104 sayfası** baştan sona incelendi. **Yeni bağımsız araştırma adayı: 1.** Bu bir kârlılık bulgusu değildir; backtest, paper test ve emir yapılmadı. Sayfalar PDF sayfasıdır.

## 1. Forex Swing Trading — Abraham Robert C.

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 17/Baskı 17/Forex Swing Trading - Abraham Robert C. (50 sayfa) - @eseckal.pdf>) · [tam metin](01_forex_swing_abraham.txt)

**Tam okuma:** s. 1–10 giriş ve swing işlem özellikleri; 11–20 destek/direnç, kırılım ve geri çekilme; 21–26 trend kanalı ve kanal dibindeki sıkışma; 27–33 yutan mum, çekiç ve kayan yıldız; 34–38 MA5/13 ve geri çekilme; 39–47 baş-omuz, çift/üçlü tepe/dip; 48–50 kapanış/tanıtım. S. 24–25 üç dip ve üç tepeyle kanal çizip, yükselen kanalın **alt kenarı yakınındaki birkaç günlük konsolidasyonun en yüksek seviyesinin aşılmasını** long tetikleyici olarak ayırır. S. 22 alt/üst kenarı hedef yönünde kullanır. Diğer destek/direnç, MA ve mum/formasyon bölümleri önceki [kanal](../batch_044/STRATEGIES.md), [mum](../batch_050/STRATEGIES.md) ve [dönüş](../batch_070/STRATEGIES.md) aileleriyle örtüşür.

### AR154A — Yükselen kanal alt kenarında kısa sıkışma ve üst kırılım

- **Kaynak çekirdeği (s. 22–25):** Yükselen kanalın alt kenarına yakın düz/yatay fiyatlar birkaç gün sürer; fiyat sıkışmanın en yüksek düzeyini kırınca alış aranır. Kaynak kanal teması toleransını, sıkışma süresini, stopu ve uygulanacak çıkışı sayısallaştırmaz. Aşağıdaki geometrik tanım bizim araştırma vekilimizdir, elle çizilen kanalın bire bir kopyası değildir.
- **Veri ve kanal (bizim ön kayıt):** EURUSD ve GBPUSD D1, New York 17:00 kapanışlı beş işlem günlük bar; tatil/erken kapanış takvimi point-in-time. Her pivot dip/tepe solda ve sağda **2'şer tam kapanmış D1** ile teyit edilir; sinyal gününde yalnız teyit anı geçmiş pivotlar görülebilir. Son 40 D1 içindeki en son üç teyitli pivot dip `L1<L2<L3` fiyatça yükselsin ve aralarında en az 3 D1 olsun. Diplerin bar indislerine doğrusal en küçük kare çizgisi `B(i)` uydur; eğim `>0`, üç dibin çizgiye mutlak uzaklıklarının her biri `≤0,25×ATR14_D1` olsun. Aynı 40 günlük pencerede en az iki teyitli pivot tepe bulunsun; `U(i)=B(i)+median(high_pivot−B(pivot_index))` paralel üst sınır; kanal genişliği sinyal anında `≥2ATR14`. Kanal/pivotlar yalnız t kapanışına kadar bilinen bilgiyle yeniden hesaplanır; geçmiş sinyal yeniden yazılmaz.
- **Sıkışma ve sinyal (bizim):** Son **3–6 kapanmış D1** bar için aday pencereleri kısa olandan uzuna sırayla dene ve ilk geçerliyi kullan. Bu barlarda min(low) `B(t)±0,25ATR14` içinde olsun; hiçbiri `B(i)−0,1ATR14` altında kapanmasın; tüm pencerenin `max(high)−min(low)≤1,5ATR14`; pencerenin kapanış regresyon eğimi mutlak `≤0,1ATR14/bar`. t barı kapandığında `close[t]>max(high[t−n:t−1])+0,05ATR14` ve `close[t]>open[t]` ise long. Geçmiş pencere t'yi içermez, kanal t kapanışında teyitli pivotlarla sabittir. Aynı kanal dip seti ve sıkışma için tek sinyal; alt çizgi altı kapanışta olay sıfırlanır. `n`, toleranslar ve ATR katsayıları kaynağın değil, ön kaydın parçasıdır.
- **İcra/risk/çıkış:** t kapanışı sonrası ilk uygulanabilir M1 ask ile giriş. İlk stop `min(low[t−n:t],B(t))−0,1ATR14`; hedef sinyal anında **dondurulmuş** `U(t)`; hedef girişin üzerinde ve tüm ücret/spread/kayma sonrası uzaklık `>1R` değilse işlem yok. Hedef/stop veya kapanmış D1'de `close<B(i)` sonrası ilk M1; en geç 10 D1 bar çıkış. İşlem başı özsermayenin %0,25'i, çift başına tek pozisyon; spot FX spread/komisyon/swap ve haber boşluğu dahil; aynı M1'de stop/hedef sırası bilinmiyorsa stop önce. Üst sınır veya 10 gün kaynakta kesin çıkış değildir, bizim test şartımızdır.
- **Fark ve karşılaştırma:** [C44 kanal kenarından hemen dönüş](../batch_044/STRATEGIES.md), yalın sıkışma üst kırılımı ve yalnız kanal dibi teması kollarıyla aynı kanal/evren/maliyetlerde olay eşleşmesi ve net R ölçülsün. Adayın ayırıcı olayı, alt kenar yakınında **sıkışma tamamlandıktan sonra** sıkışma yüksek düzeyinin kapanışla aşılmasıdır. Kanal çizim parametreleri sonuçlara göre geriye dönük seçilmesin; ayrılmış dış örneklemde sınansın.

## 2. Günlük Alım Satım — Anthony Smith

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 19/Baskı 19/Günlük Alım Satım - Para Kazanmanın ve Başarıya Ulaşmanın Gizli Stratejileri (Orijinal) - Anthony Smith (46 sayfa) - @eseckal.pdf>) · [tam metin](02_day_trading_anthony.txt)

**Tam okuma:** s. 1–6 kapak, önsöz; 7–13 gün içi/swing/pozisyon ticareti, piyasa tanıtımı; 14–19 hisse seçimi, ön seans ve izleme listesi; 20–25 eski platform/aracı tanıtımları; 26–28 psikoloji; 29–36 plan, günlük, stop ve limit anlatımı; 37–42 penny stock; 43–46 aracı kurum ve kapanış.

**Karar:** Başlık “gizli stratejiler” dese de yönlü, ölçülebilir bir fiyat olayı ile giriş ve çıkış birlikte verilmez. S. 35'te limit emrini açık işlem sayısını sınırlayan bir emir gibi anlatması teknik olarak hatalıdır; s. 8'de vadeli sözleşmenin kârının mutlaka teslim gününde oluşacağını iddia eder. S. 37–41'de düşük likiditeli penny stock için toplu alıp hızla elden çıkarma önerisi, maliyet ve dolum riski belirsizken test edilebilir üstünlük değildir. Yeni bağımsız aday yok.

## 3. Teknik Analiz ve Dow Teorisi — Mustafa Küçükakarsu

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 22/Baskı 22/Teknik Analiz ve Dow Teorisi - Mustafa Küçükakarsu (8 sayfa) - @eseckal.pdf>) · [tam metin](03_dow_mustafa.txt) · [sekiz sayfanın görsel denetimi](dow_contact.jpg)

**Tam okuma:** s. 1–2 kapak/teknik analiz; 3–5 görsel ağırlıklı simetrik üçgen ve yukarı kırılım örneği; 6–7 Dow'un fiyat, trend, gösterge/hacim teyidi ve trendin devamı ilkeleri; 8 çoklu gösterge grafiği. Metin s. 6 “6 ana kural” der fakat beş madde listeler; s. 7 aynı listeyi “5 ana kural” diye tekrarlar. Üçgen şekli [önceki üçgen adaylarıyla](../batch_003/STRATEGIES.md) aynı olaydır; göstergelerin eşiği, giriş/stop/çıkış yok. Yeni aday yok.

**Parti sonucu:** Üç yeni kitap, 104 sayfa ve **1 yeni aday**. Toplam aday sayısı 388 oldu.
