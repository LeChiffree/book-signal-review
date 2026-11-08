# Kitap okuma 011 — G7 haftalık yön, karar noktaları, pozisyon büyüklüğü

**Kapsam:** Üç PDF'nin **49 + 53 + 63 = 165 PDF sayfası** sayfa sırasıyla işlendi. Sayfa numaraları PDF sayfasıdır. Birinci kaynak Forex, ikinci Nifty vadeli işlemleri, üçüncü Forex/rulet bahis benzetmeleri üzerine; kripto sonuçları veya güvenilir kâr oranları olarak yorumlanmaz. Karar anında bilinemeyecek fiyat, pivot, haber veya hesap istatistiği testte kullanılmayacak. Bu partide backtest/paper emir yok.

## 1. Forex Science — G7 Forex Sistemi

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 9/Baskı 9/G7 Forex Sistemi - Forex Science (49 sayfa) - @eseckal.pdf>)

Sistem kapalı haftalık mumdan gelecek haftanın yönünü seçer; H1 grafikte 200 SMA, 100/200 Bollinger ve yavaş Stoch(14,7,3) ile geri çekilme arar, ters mum kapanınca girer (s. 11–18, 26–35). Stop ters mumun dışı, hedef en az 2R (s. 42). Haftalık görüşü bozan önceki haftanın karşı ucu ±10 pip **pozisyonu otomatik ters çeviren stop değildir** (s. 25). 10 haftalık SMA isteğe bağlı bağlamdır (s. 16, 48). S. 19–24'te `higher high veya higher low`, `lower high veya lower low` esnek tarifleri aynı dış haftada iki yöne de işaret edebilir. Kaynak BB standart sapma katsayısını ve “200 SMA'ya yakın” mesafesini vermez. Forex NFP/seans/pip kuralları (s. 48–49) kriptoya aynen aktarılmaz; performans ve haftalık pip iddiaları doğrulanmış örneklem sayılmaz.

### G7a — Önceki tam haftanın yönünde H1 aşırılık ve ters mum

- **Haftalık karar:** UTC pazartesi 00:00 sınırında son **tamamlanmış** 7 günlük haftanın `high/low` değerleri önceki tam hafta ile karşılaştırılır. Bazda `high[w]>high[w-1] && low[w]>low[w-1]` long; her ikisi küçükse short; dış haftalar ve karışık haftalar **nötr**. Bu, kitabın esnek kuralının çakışmasız **bizim sıkı sürümüdür**. Ayrı ablation: yükseklerin birinin daha yüksek olması boğa, düşüklerin birinin daha düşük olması ayı; ikisi birden olursa işlem yok. Haftalık spike mum dönüşleri (s. 21, 24) ayrı etiket, baz değil. İptal düzeyi: long için son haftanın low'u `-0.1 ATR14_weekly`; short için high `+0.1 ATR`. Tampon Forex 10 pip yerine bizim ölçek seçimimiz. Haftanın herhangi bir H1 barında düzey görülürse o haftanın yeni girişleri iptal; mevcut pozisyonun stopu bundan ayrı.
- **H1 kurulum:** Önceki haftanın long yönünde son kapanmış H1 için `StochK14_7_3[t]<20`; `low[t]<=BB100_lower[t]` **veya** `low[t]<=BB200_lower[t]` **veya** `abs(low[t]-SMA200[t])<=0.1 ATR14_H1[t-1]`. Short üst bant, `K>80`, SMA simetrisi. `BB(n,2)` ve `0.1 ATR` kaynakta yok; önceden dondurulmuş uyarlama. Stoch hesap türü `(14,7,3)` yavaş K/D olarak açıkça sabitlenmeli. BB ile SMA temasları tek olayda etiketlenir.
- **Tetik:** Kurulumdan sonra en çok üç kapanmış H1 içinde ilk boğa yutan mum veya alt fitili `>=2×gövde`, kapanışı üst yarıda olan pin mum; short simetri. Kaynak yutan/çekiç/doji/cımbız gibi birçok şekle izin verir (s. 33–35), `3 bar`, fitil ve kapanış eşikleri bizim daraltmamız. Tetik mum kapanışından sonraki ilk 1m giriş. Stop tetik mumunun dibi `-0.1 ATR14_H1[t-1]`, hedef `2R`; Forex'in 20–60 pip stop kapısı (s. 42) aktarılmaz, `stop_distance/ATR` raporlanır.
- **Ablation:** Haftalık yön, Stoch, BB/SMA temas ve ters mumun her biri baz üstüne eklenir. Giriş üç adımın sonuncusu kapanmadan üretilemez. Haftalık SMA10 ve kitap s. 31'deki elle çizilmiş Fibonacci/trend çizgisi isteğe bağlıdır; öznel çizimi özgün kural diye kodlama. H1 kohortunu günlük adaylara doğrudan havuzlama.

## 2. Smart Trader — Karar Noktaları

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 9/Baskı 9/Karar Noktaları - Smart Trader (53 sayfa) - @eseckal.pdf>)

İlk bölüm yatırım, beklenti ve yöntem (s. 5–24); işlem çekirdeği s. 25–43. “Karar noktası” (DP) olarak önceki günün high/low/close, gün açılışı, teyitli swing, yuvarlak fiyat ve aralık sınırı kullanılır (s. 26–29). DP civarında **TST/FTC** (seviyeye yaklaşır ama ilerleyemez), **BPB** (kırılım ve geri çekilmede seviyenin tutulması), **BOF** (kırılım başarısızlığı) ayrımı yapılır (s. 36–40). Bir sonraki karar noktasına kadar boşluk veya *first trouble area* (FTA) hesaplama fikri s. 35, 42'de önemlidir. İki veya daha fazla barın ilk mumun aralığı içinde kaldığı “Master Candle” ve aralık kırılımı s. 43'te açıkça tarif edilir. Kaynak Nifty 3m takdirî sistem; birebir mekanik kural ve sayısal tolerans yok. “Diğer traderların stopları” açıklaması OHLCV ile gözlenmiş emir akışı değildir. Aralıkta kalma %70 iddiası (s. 33) test edilmiş oran sayılmaz.

### DP11a — Önceki gün yüksek/düşük karar noktasında başarısız kırılım

- **Kaynak davranışı:** BOF, seviyenin dışına çıkıp içeride kalamamak; ters yöne ve bir sonraki DP'ye hareket fikri (s. 36, 40). TST/FTC seviyeye varmadan dönüş olduğundan aynı olay değildir.
- **Bizim kapalı H1 olay:** Her UTC gün başlangıcında `PDH/PDL/PDclose` son **tam günlük** bardan dondurulur. Long için `low_H1[t]<PDL-0.1 ATR14_H1[t-1] && close_H1[t]>PDL`; short için `high_H1[t]>PDH+0.1 ATR && close_H1[t]<PDH`. `0.1 ATR` bizim tolerans; tek bar BOF çeşidi. En çok iki bar dışarıda kapanıp sonra içeri dönen çeşidi ayrı. Olay kapandıktan sonraki ilk 1m giriş; stop dışarı taşan ekstremum `±0.1 ATR`, ilk hedef `PDclose`, sonraki hedef karşı DP; 1R/2R ve 6/12/24 H1 bar zaman çıkışı ayrı. Hedef risk oranı işlem anında hesaplanır; FTA `<=1R` ise filtreli varyant işlem dışı.
- **Çakışma:** Batch 005 S1 ve batch 006 F1 failed-low reddi ile aynı bar olabilir. DP seviyesi ve pivot seviyesi etiketleri tek işlem üzerinde birlikte tutulur; bağımsız üç strateji kazancı sayılmaz.

### DP11b — Önceki gün sınırının kırılım sonrası ilk retesti

- **Kaynak davranışı:** BPB, kırılan DP'nin yeni destek/direnç olarak tutulması; kaynak s. 39'da geri çekilme swing high kırılımında giriş ve DP/swing altında stop seçenekleri verir.
- **Bizim H1 olay:** Son tam gün `PDH` üstünde H1 `close[t]>PDH+0.1 ATR` ile kırılım; sonraki en çok 12 H1 içinde ilk `low<=PDH+0.25 ATR` ve `close>PDH` retest barı. Teyit için bu barın tepesinin **sonraki H1 kapanışında** aşılması veya retest barının kendisinin boğa kapanışı iki ayrı sürüm. Emir ancak teyit kapanışı sonrası ilk 1m; stop dondurulmuş PDH `-0.1 ATR` veya retest dibi ayrı. Short PDL simetri. `12 bar`, `0.25 ATR`, teyit seçimi bizim nesnelleştirmemiz. Karşı DP/2R ve 6/12/24 H1 çıkışı.
- **Kontrol:** Doğrudan PDH/PDL kırılımı bazına karşı retest bekleme, başarısız dolum ve daha iyi/kaçan fiyat oranları; batch 005 S2/O1/D1 ile çakışma.

### DP11c — Master mumun en az iki iç bardan sonra kırılması

- **Kaynak:** İki veya daha fazla ardışık barın yüksek/düşükleri ilk “ana mum” sınırları içinde; ana mum üst/alt sınır kırılınca yönlü giriş, stop karşı uç (s. 43).
- **Bizim H1 tarama:** Ana mum m kapanışında sınırlar `H/L`; `m+1` ve `m+2` kapalı barlarda `high<H && low>L` (eşitlikte yok). m+2 kapanışında bir sonraki H1 için iki yönlü OCO stop emirleri `H+1 tick`, `L-1 tick`; karşı uç başlangıç stop. Emir yalnız bir H1 geçerli; aynı 1m içinde iki uç görülürse sıralama belirsiz olarak işaretle. Ana mum gövde/aralık ve PDH/PDL yakınlığı **etiket** olarak eklenir; kaynak bunları tek başına sinyal saymama uyarısı yapar. 1R/2R ve 6/12/24 H1 çıkışları bizim test ufukları. Önceki NR4/NR7 ve inside-bar aileleriyle ek katkı ölçülecek.

**Ertelenen:** Yuvarlak sayı DP'si, farklı fiyat ölçeklerinde basamak seçimine bağlı; önce tick/psikolojik yuvarlama sözleşmesi gerekir. TST/FTC için “DP'den önce durma” toleransı ve başarısız devam süresi sayısal değil; BOF/BPB sonucu gelmeden keyfî ek kural üretilmez.

## 3. Roulette Trader — Forex Trading Risk Yönetimi Sistemleri

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 9/Baskı 9/Forex Trading Risk Yönetimi Sistemleri - Roulette Trader (63 sayfa) - @eseckal.pdf>)

Kitap **işlem yönü için mekanik OHLCV sinyali sunmuyor**; verilen robotların sinyal kodu/verisi yok. Ana konu işlem büyüklüğünün son kazanç/kayıp dizisine göre değişmesi. Kayıp sonrası ikiye katlayan Martingale'in riskini s. 11–14'te kabul ediyor. “Ardışık kazanç” yöntemi: birim sayısı 1'den başlar, her kârdan sonra +1, ilk kayıptan veya seçili çevrim hedefine ulaşınca 1'e döner (s. 14–18). “Kümülatif kazanç”: kâr sonrası +1, zarar sonrası -1, minimum 1, çevrim hedefinde sıfırlama (s. 19–21); farklı kâr/zarar büyüklükleri için oranlama s. 51'de anlatılır. Düşük başlangıç lotu “flat-line” (s. 46–48); ayrıca kayıp sonrası artıran negatif ilerleme (s. 52–54) önerilir. Karşıt yönde aynı varlık işlemlerini iki ayrı strateji gibi birlikte kârlı gösteren örnek (s. 29–31) bağımsız alpha kanıtı değildir. S. 35'te çevrim içi açık kâr zirvesinden düşüşü drawdown'a katmama önerisi, gerçek hesap riski raporlaması için **uygun değildir**.

### R11 — İşlem boyutu kuralı karşılaştırması; sinyal değil

- **Girdi:** Önceden dondurulmuş bir sinyal adayının, maliyet sonrası ve zaman sıralı işlem R dizisi. Önce sabit `risk_per_trade` ve sabit pozisyon tavanı baz. Alternatif olarak `units[t]` yalnız `t-1`e kadar sonuçlarla: ardışık `min(max_units,1+consecutive_wins)`; kümülatif `clip(units[t-1]+sign(net_R[t-1]),1,max_units)`. Kaynak birim artışını tarif eder; `max_units` ve risk tavanını **biz** belirlemeliyiz. Tek pozisyon riski ve toplam açık portföy riski tavanını geçecek emir küçültülür veya alınmaz. Kayıp sonrası artırma/Martingale kaynakta geçse de ilk uygulamaya alınmaz; olası zarar kuyruğu çok büyüktür.
- **Doğrulama:** Aynı sinyal sırası ve aynı dolum/maliyetler üzerinde sabit risk bazına göre nihai net getiri **ile birlikte** gerçek peak-to-trough equity drawdown, beklenen kısafall/ES, en kötü seri, margin/funding, tasfiye ve risk tavanı ihlalini raporla. Artan büyüklüğün “alpha” yarattığı söylenmez: gelecek işlem sonucunun geçmiş büyüklükten bağımsız olduğu sıfır/negatif beklentili bir sinyalde ölçekleme net beklentiyi kendiliğinden pozitif yapmaz; ücretler daha da azaltır. Karşıt yönleri aynı anda açma da brüt fiyat riskini çoğunlukla netlerken iki yönde maliyet doğurur. Çevrim içi kârlar özkaynak/riske dahildir; yalnız başlangıç sermayesinin altını drawdown sayma hatası yapılmaz.
- **Durum:** Kullanılabilir bir sinyal stratejisi çıkarılmadı. Bu kitap ilerideki backtest için pozisyon büyüklüğü ve risk raporlaması **deney tasarımı** sağlıyor. Kaynaktaki robot getirileri ve küçük sermayeyi hızlı büyütme örnekleri bağımsız doğrulanmadı.

## Ortak uygulama kararı

1. **Öncelik:** DP11c (açık master mum kuralı) ve DP11a/DP11b aynı PDH/PDL olay evreninde; ardından G7a çok zaman dilimi filtresinin ek katkısı. R11, ancak pozitif/negatif sinyal sonucu ve OOS yürütme netleşince risk deneyi.
2. Karar için yalnız kapanmış UTC 1w/1d/H1 barlar; emir sonraki yürütülebilir 1m. PDH/PDL, haftalık sınır, Master mum ve pivotlar olaydan önce dondurulacak. Giriş, iptal, dolmama, ücret/spread/kayma, funding, net R ve çakışan kurulumlar saklanacak.
3. Çoklu deneme ve rejim/dış örneklem ayrımı olmadan başarı iddiası yok. Bu partide backtest, paper test veya canlı emir yapılmadı.
