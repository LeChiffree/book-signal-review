# Kitap okuma 039 — hacim teyidi ve para akışı

**Kapsam:** 10 + 35 + 83 = **128 PDF sayfası**. Her sayfanın sıralı metni kaydedildi; hacim yöntemi, örnekleri ve sonuç kısımları sayfa sayfa incelendi. Shah s. 18, Milton s. 28 ve s. 60 görsel olarak da kontrol edildi. Atıflar PDF sayfasıdır. Kaynakta olmayan sayılar **bizim deney seçimimizdir**. Backtest, paper test ve emir yok.

## 1. Chaikin Para Akışı Göstergesi

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 11/Baskı 11/Chaikin Para Akışı Göstergesi (10 sayfa) - @eseckal.pdf>) · [Tam metin](01_chaikin_money_flow.txt)

**Kaynak:** `MFM=((close−low)−(high−close))/(high−low)`, `MFV=MFM×volume`, `CMF20=sum(MFV,20)/sum(volume,20)` (s. 1). Sıfırın üstü/altı baskı yönünü gösterir; sıfırda sık ileri geri geçişe karşı **+0,05/−0,05** tampon önerilir (s. 3–5). CMF, günün kendi aralığındaki kapanışı ölçer; önceki kapanışa göre gap ve fiyat değişimini ölçmez (s. 6–7). S. 9–10'da CMF sıfırı ve RSI14 50'yi aynı yönde kesen hisse taraması örneği vardır; taramanın gün kapanışına dayandırılması gerektiğini açıkça söyler. Kaynak CMF'nin tek başına kullanılmamasını belirtir (s. 8). Hisse fiyatı/dolar hacmi eşikleri kriptoya taşınmaz.

### C39 — CMF tamponunu mevcut D1 kırılıma ekleme

- **Bizim hesap:** Tam UTC D1 barları. `high=low` ise o barın MFM'si 0; `sum(volume,20)=0` ise CMF tanımsız ve sinyal yok. Hacim, seçilen borsanın **gerçek gerçekleşmiş taban varlık hacmi**; sentetik veya borsalar arası birleşmiş seri kullanılmaz. `CMF20[t−1]<=0.05 && CMF20[t]>0.05` long teyidi, `>=−0.05 && <−0.05` short teyidi. Kaynaktaki eşikler korunur; eksik payda davranışı bizim güvenlik kuralımızdır.
- **Deney:** Önceden tanımlı 20-D1 en yüksek/en düşük kapanış kırılımı ile aynı `t` gününde CMF geçişi; ikinci kol `CMF20[t]>0.05` durum filtresi, üçüncü kol CMF filtresiz. Giriş `t` kapanışından sonraki ilk uygulanabilir 1m, stop 2 ATR14_D1, hedef 2R veya 10 D1 bar sonra çıkış; bu icra/risk kuralları bizim ortak deney çerçevemizdir. RSI14 50 eşzamanlı kesişimi ayrı filtre kolu, ana kurala otomatik eklenmez.
- **Risk:** Fiyat düşerken pozitif CMF görülebilir; s. 6–7 bu hesaplama özelliğini anlatır. CMF'yi “gerçek para girişi” ya da tek başına kârlı sinyal diye yorumlama. Aynı kırılım olaylarında mevcut hacim/RSI filtreleriyle örtüşme sayılmalı.

## 2. Jayesh Shah — Volume Trading

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 26/Baskı 26/Volume Trading - Jayesh Shah (35 sayfa) - @eseckal.pdf>) · [Tam metin](02_volume_trading_shah.txt) · [Giriş kuralları s. 18](shah_p18.png)

**Kaynak:** Direnç veya 52 haftalık yüksek kırılımında hacim, son ayın ortalama günlük hacminin **iki katından fazla** olmalı (s. 10–11, 18). Kırılım mumu aralık tepesine yakın güçlü kapanmalı; doji ve düşüş mumu elenir (s. 14, 18–20). S. 18 açık uzun kuralı: gün 1 yeni 52 hafta yüksek, güçlü kapanış, hacim >2× önceki ay ortalaması; gün 2 önceki günün yüksek üstünden al. S. 20–21 gün kapanmadan girmeme, ertesi gün ilk 15 dakikada fiyatın yüksek üstünde kalmasını bekleme ve başlangıç stopunu gün 1 düşük altında tutma. S. 15–16 yutma/delme/çekiç dönüş mumlarında hacmin önceki günden fazla olmasını ister. S. 26–29 tek gün yerine birkaç gün/hafta süren yüksek hacim anlatılır. Hisse örneklerindeki olağanüstü getiriler, kripto sonucu değildir. “Tüm kopuşların %70'i başarısız” (s. 10) için yöntem verilmemiştir.

### S39 — 52 haftalık zirve + >2× hacim + ertesi gün yüksek teyidi

- **Bizim D1 tanım:** Kripto 7/24 olduğu için 52 hafta = önceki **364 tamamlanmış UTC D1** bar; `high[t]>max(high[t−364:t−1])` ve `close[t]>max(high[t−364:t−1])`. Hacim `volume[t]>2×mean(volume[t−30:t−1])`; kapanış mumun aralık tepesinden en çok %20 aşağıda, `close>open`, gövde aralığın en az %50'si. 30 gün ve son %20/%50 eşikleri bizim sayısallaştırmamız; 2× ve 52 hafta kaynaktan. Sıfır aralıklı mum ve eksik geçmiş geçersiz.
- **İcra:** Gün `t` tamamlandıktan sonra sonraki UTC gününün **ilk 15 tamamlanmış 1m mumu** boyunca her kapanışın `high[t]` üstünde kalması şartı. 15. kapanıştan sonraki ilk uygulanabilir 1m fiyatıyla long; ilk 15 dakikada koşul yoksa o gün için işlem yok. Bu, kaynağın ertesi gün güçlü fiyatı bekleme fikrinin bizim kesinleştirmemizdir; hisse piyasasındaki açılış gap'i kriptoda aynı değildir. Stop `low[t]−0.1 ATR14_D1`; stop mesafesi maliyetin iki katından küçükse veya aşırı büyükse (`>4 ATR`) geçersiz. 3R veya 20 D1 bar sonra çıkış; kaynak kârı trendle taşısa da kesin hedef/süre vermez.
- **Karşılaştırma:** Aynı 364-gün kırılımları için >2× hacim / >1× hacim / hacimsiz, gün `t` sonrası hemen giriş / 15 dakika teyidi. Hacim filtresinin seçilim etkisini işlem sayısı ve maliyetle birlikte ölç. Hisse “52 hafta” fikri kripto için varsayımsal transferdir.

## 3. George Milton — Hacim Fiyat Analizi

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 19/Baskı 19/Hacim Fiyat Analizi - Nasıl Yapılacağına Dair Nihai Yeni Başlayanlar Rehberi - George Milton (83 sayfa) - @eseckal.pdf>) · [Tam metin](03_volume_price_milton.txt) · [Ord dalgası s. 28](milton_p28.png) · [MFI karşılaştırması s. 60](milton_p60.png)

**Kaynak:** Kitap risk, teknik analiz, hacim göstergeleri ve grafik örneklerini derler. Hacim dalgası, aynı yönde **en az üç yüksek hacimli** mumdan oluşur; kısa hacim ortalaması olarak `EMA(EMA(volume,3),3)` veya `EMA(volume,5)` önerilir (s. 23–25). Tim Ord yönteminde bir dalganın hacim ortalaması, dalga hacimleri toplamı / mum sayısıdır; itişten sonraki düzeltme dalgası hacminin yaklaşık **%50 düşmesi**, itiş tepesinin üstünde kapanış ve kırılım mumunda eski tepe mumuna benzer hacim long örneği (s. 26–29). S. 28 görseli 20→10 Ord hacimli geri çekilme ve yeniden kırılımı gösterir. S. 48'de dirençteki önceki hacme göre kırılım hacminin **≥%10 yüksek**, zayıf/sahte kırılımda **≥%10 düşük** olmasını anlatır. S. 57–60 MFI20 merkez çizgisi ve MFI14'ün 20 dönem ortalamasıyla 30 gün kırılım filtresi; verilen FDAX 2004–2016 sonuçları bu örneğin kendi piyasası/yöntemiyle sınırlı, kripto performans kanıtı değil. S. 72–82 fiyat-hacim ayrışması ve aşırı hacimde olası tükenme; her artış otomatik devam sinyali değildir. Kitaptaki dalga başlangıcı/bitişi ve pivot seçimi tam mekanik değil.

### M39 — İtiş dalgası sonrası düşük hacimli düzeltme ve yüksek üstü kapanış

- **Bizim D1 dalga üretimi:** Yalnız 3-sol/3-sağ **onaylanmış** D1 pivot low/high ile ardışık `L→H` yukarı dalgası kur; `H` ancak üç sağ D1 mum kapandığında bilinir. İtişte en az 3 yükselen kapanış ve bunların hacimleri önceki kapanmış barın `EMA(volume,5)` üstünde olsun. `V_up=sum(volume[L:H])/bar_count(L:H)`. H onayından sonra ilk teyitli düşen düzeltme dalgası `H→R`, `R` onayında `V_down` aynı formülle. `V_down<=0.5 V_up` ve düzeltme derinliği itiş yüksekliğinin %23–50'si. Ardından ilk `close[t]>high[H]+0.1 ATR14_D1[t−1]` long; kırılım hacmi `volume[t]>=volume[H]`. Short simetrik yalnız veri buna izin veriyorsa ayrı kol. Yüzde 50 Ord kıstası kaynaktan; pivot 3/3, aralık, EMA eşiği, %23–50 bandı ve ATR tamponu bizim belirginleştirmemizdir.
- **İcra/risk:** `t` kapanışı sonrası ilk uygulanabilir 1m giriş; stop `low[R]−0.1 ATR`, 2R hedef veya 20 D1 bar zaman çıkışı. Stop girişin altı ve maliyetin en az iki katı uzaklıkta olmalı. Dalga `H/R` pivotu onaylanmadan eski barlara sinyal yazma. Kaynak dalga yaklaşımı çok öznel olduğu için önce olay sayısı ve parametre duyarlılığı ölçülmeli.
- **Alternatif filtre:** S. 48 hacim kıstası için mevcut 20-D1 direnç kırılımında `volume[t]>=1.1×volume[son teyitli direnç pivotu]` ile `<=0.9×` kollarını kıyasla; “başarılı/sahte” etiketini yalnız sonradan gözlemle. S. 60 MFI14>kendi SMA20 filtresi aynı olayların ayrı ablation'ı; FDAX sonuç yüzdelerini kriptoya projekte etme.

## Ortak test notu

Önce **S39** (kaynakta net 2× ve giriş sekansı), sonra **C39** (net formül ve ±0,05), ardından **M39** (dalga seçimi duyarlı). Her aday önce mevcut breakout, hacim, OBV/MFI ve destek/direnç aileleriyle olay bazında karşılaştırılmalı. Point-in-time evren ve borsa hacmi, kapanış sonrası uygulanabilir fiyat, ücret/spread/kayma/funding, aynı bardaki stop-hedef sırası ve zaman sıralı dış örneklem olmadan performans hükmü yoktur.
