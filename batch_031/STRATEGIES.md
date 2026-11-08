# Kitap okuma 031 — DeMark sayımları, EMA kesişimleri, RSI 80/20 ayrışması

**Kapsam:** 183 + 19 + 18 = **220 PDF sayfası**. Sayfa sıralı tam metinler bu klasördedir. Atıflar **PDF sayfası**dır. Kaynak kural ile bizim kripto deneyi ayrı tutulur. Backtest/paper test/emir yapılmadı.

## 1. Jason Perl — DeMark Göstergesi

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/DeMark Göstergesi - Jason Perl (183 sayfa) - @eseckal.pdf>) · [Tam metin](01_demark_perl.txt)

Kitap TD Sequential ve TD Combo (s. 3–68), TD D-Wave (s. 69–90), nesnel TD çizgileri (s. 91–102), retracement (s. 103–114), trend faktörü (s. 115–124), REI (s. 125–143), hareketli ortalamalar (s. 144–150), projeksiyon/kanallar (s. 151–162) ve kısa vadeli formasyonları (s. 163–178) işler. Çeviri/OCR bazı formülleri bozuyor; özellikle s. 152'deki aralık projeksiyonu ve s. 128 sonrası REI hesaplaması bu metinden sessizce kodlanmamalı. Bu partide açık sayım kurallarını öne aldım; diğer aileler incelenecek fikirlerdir.

### D31a — Mükemmelleşmiş TD 9 kurulumunun TDST yakınında dönüşü

- **Kaynak:** Alış kurulumunun ilk barı `close[t]<close[t-4]` düşüş fiyat dönüşünü takip eder; **dokuz ardışık** barın her kapanışı dört bar önceki kapanıştan düşüktür; koşul bozulursa sayım sıfırlanır (s. 3–5). Satış simetrik (s. 5–6). Alış 8 veya 9. barın en düşüğü, 6 ve 7. bar düşüklerinin en küçüğüne `<=` ise mükemmelleşir (s. 12); satış için yükseklerin `>=` karşılığı (s. 15–16). Perl, bütün dokuzları işlem yapmaz: mükemmellik, kurulumda TDST destek/direnç ötesine **kapanış olmaması**, 9. kapanışının bu seviyeye yakınlığı ister (s. 13–18). Alış stopu kurulumdaki en düşük **true low** barının true range'i kadar altı; satış stopu en yüksek **true high** barının true range'i kadar üstü. Karşı TDST seviyesine mesafe riskten büyük olmalı (s. 15, 18). TDST, son tamamlanan kurulumun uç true fiyatlarıyla tanımlanır (s. 7–10).
- **Bizim D1 olay sözleşmesi:** UTC D1 kapanışından sonra sayım durumu güncellenir; ilk bar için bir önceki dört bar karşılaştırmasının işaret değiştirmesi ve 1–9 kesintisiz koşulu zorunlu. `true_low=min(low, önceki close)`, `true_high=max(high, önceki close)`, `TR=true_high-true_low`. 9. barda mükemmellik ve **o sinyalden önce kapanmış son karşıt TDST** kontrolü; kaynakta sayısal olmayan “yakınlık” eğitimde `|close9−TDST|/ATR14_D1` eşiğiyle sabitlenir. TDST henüz mevcut değilse sinyal yok. Sonraki ilk 1m'de giriş, kaynak true-range stopu, karşı TDST hedefi yalnız net mesafe >1R ise; azami H7D bizim güvenlik sonlandırmamız. Sonradan oluşan mükemmelliği 9. bara geri yazma; ancak oluştuğu gündeki ayrı olay olarak ele al. Long/short simetrik.
- **Karşılaştırma:** Sıradan dokuz sayımı, mükemmelleşmiş dokuz ve TDST filtresi aynı olay havuzunda; dokuz bar sonrası dönüş etkisini RSI/MA mean reversion'a karşı ölç. Düşüş trendinin sürmesi halinde stop riski önemlidir.

### D31b — TD Sequential 9→13 tükenme ve gecikmiş onay

- **Kaynak:** Dokuzluk kurulumdan **sonra veya 9. barda** geri sayım başlayabilir. Alış için `close[t]<=low[t-2]` nitelikli barlar **ardışık olmak zorunda değildir**; 13 nitelikli bar gerekir (s. 18–20). 13. alış barının `low13<=close(count8)` ek koşulu sağlanmazsa 13 ertelenir (s. 20–21); satış `close[t]>=high[t-2]`, `high13>=close(count8)` simetriği (s. 33–34). Gelişen geri sayımı karşıt kurulum ve TDST koşulları silebilir; yeni kurulumların geri dönüşümü ek kurallar taşır (s. 22–24, 35–37). Agresif giriş 13. bar kapanışı; tutucu alış `close[t]>close[t-4]` ilk teyit kapanışı, satış `<` (s. 25, 38). Alış riski sayımın **bütün barları**, numarasızlar dahil, arasındaki en düşük true low barının true range'i kadar altı; satış simetrik (s. 27–28, 40). Tepki için 12 bar tartışılır (s. 29, 41).
- **Bizim araştırma sözleşmesi:** Önce yalnız **tek aktif kurulum**, karşıt 9 oluşunca sayımı iptal, 13 nitelikli bar ve ek 8. bar koşulu; sayımın başından 13'e kadar bütün kapanmış barlar stop hesaplamasına dahil. Daha karmaşık 1,618 aralık/18 bar geri dönüşüm kuralları ayrı sürüm olarak kodlanıp doğrulanmadan “tam TD Sequential” denmez. İlk 13 sinyalinde ertesi ilk 1m giriş; stop yukarıdaki kaynak formül; hedef 2R veya ilk ters dokuz/12 D1 sonlandırması **bizim** çıkış seçimi. Tutucu teyit kolu yalnız 13'ten **sonraki** kapanışlarda çalışır, giriş sonraki ilk 1m; teyit yoksa belirlenmiş 12 bar sonunda iptal. Aynı M1 mumunda stop önce. Sayım durum makinesi için elle etiketlenmiş s. 19–21 ve 33–34 şekilleriyle birim karşılaştırması gerekir.
- **Önemli ayrım:** TD Combo, kurulum 9 tamamlanınca geri sayımını kurulumun **1. barından geriye dönük** hesaplar ve ek dört koşul kullanır (s. 61–63). Sequential ile aynı sinyal olarak birleştirilemez; bu turda kod sözleşmesine alınmadı.

### D31c — TD Differential iki barlık baskı filtresi

- **Kaynak:** `alış baskısı = close−true_low`, `satış baskısı = true_high−close`; yukarı ok için ardışık iki düşen kapanış, son bar alış baskısı öncekinden yüksek ve satış baskısı öncekinden düşük (s. 163). Bir sonraki barda yüksek veya kapanış artışı beklenir; beklenti doğrulanmış sonuç değildir.
- **Bizim D1 filtre deneyi:** Son kapanmış bar `t` ve `t−1` ile tam formülü uygula; tek başına işlem değil, D31a/D31b dönüş girişlerinde filtreli/filtersiz sonuç. Sonraki barın `high[t+1]` bilgisi sinyalde kullanılmaz. Kısa yön simetrisi kitap bölümünün ilerleyen kurallarıyla ayrıca teyit edilmeden kodlanmaz.

## 2. Soulz — EMA'ların Gücü

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 6/Baskı 6/EMA_ların Gücü - Soulz (19 sayfa) - @eseckal.pdf>) · [Tam metin](02_ema_power_soulz.txt)

Kitap günlük EMA13/21 ve EMA50/200, M15 EMA13/34, haftalık EMA50, H4 EMA200 önerir (s. 6–12). EMA200 retestinde “confluence” örnekleri (s. 13–15) nesnel ek filtre/stop vermiyor; örnek yüzde kazançlar kanıt değil. Fiyatın EMA etrafında gidip gelmesinde kenarda beklemeyi söyler (s. 16).

### E31a — M15 EMA13/34 kapanış kesişimi, HTF filtresiyle

- **Kaynak:** M15 EMA13 ve EMA34 kesişimi bir işlem fikri; MACD gibi teyitler önerilir, fakat tamamlanmış kesişimi beklemeye vurgu yapar (s. 9, 17–18). Stop ve hedefin nesnel fiyat düzeyi verilmez; 2–3R örneği s. 18'dedir.
- **Bizim deney:** Tam kapanmış M15 `EMA13[t]>EMA34[t]` ve önceki bar `<=` long; short simetrik. Ertesi ilk 1m'de giriş. Önceden tamamlanmış H4 `close>EMA200` yön filtresi ve filtresiz kol; `ATR14_M15` temelli stop, 2R hedef, azami 24 M15 bar; parametreler eğitim döneminde sabitlenir. EMA/MACD çaprazlarının birbirinin türevi olabileceği için önceki EMA/MACD adaylarıyla **sinyal eşdeğerliği** raporlanır; yeni bağımsız alfa varsayılmaz.

### E31b — Haftalık EMA50 rejim filtresi

- **Kaynak:** Tam haftalık fiyat EMA50 üstünde alış, altında satış (s. 10); günlük EMA13/21 trend bilgisi (s. 11), H4 EMA200 destek/direnç (s. 12).
- **Bizim filtre:** Yalnız son **tamamlanmış UTC haftası** `close_week>EMA50_week` ise long adaylarına izin; tersi short. Açık haftanın değeri kullanılmaz. Mevcut D1 trend/breakout sinyal havuzuna filtre uygula, filtreli/filtersiz net sonuç ve dışlanan işlem sayısını karşılaştır. Tek başına yeni emir üretmez.

## 3. RSI 80-20 Trading Stratejisi

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 7/Baskı 7/RSI 80-20 Trading Stratejisi (18 sayfa) - @eseckal.pdf>) · [Tam metin](03_rsi_80_20.txt)

### R31 — 50 bar ekstremumu + RSI8 ayrışması + ilk barın kapanışını kırma

- **Kaynak:** RSI periyodu 8, eşikler 20/80 (s. 2–3). İlk dip son 50 barın en düşüğü ve RSI≤20; sonra **daha düşük fiyat dibi ama daha yüksek RSI** için ikinci barın kapanışı beklenir (s. 3–7). Long tetik, fiyatın ilk dip **mumunun üzerinde kapanması**; short için ilk tepe mumunun altında kapanması (s. 8, 13–17). “Mumun üzerinde/altında” ifadesi kapanış mı high/low sınırı mı olduğu bakımından belirsizdir. Stop önceki destek/direnç altı/üstü; en az yaklaşık 1:3 kâr/risk tavsiyesi, fakat “1–3 zaman periyodu geriye” ifadesi de belirsiz (s. 8–9). Örnekler M15/H1/H4; özel EFC gösterge reklamı hesap kuralı değildir.
- **Bizim H4 ilk deney:** İlk `A` barında `low[A] < min(low[A−49:A−1])` ve Wilder RSI8 kapanışta `<=20`. Sonraki en çok 20 **kapanmış** H4 bar içinde ilk `B` için `low[B]<low[A]` ve `RSI8[B]>RSI8[A]`; B de kapanmalı. B'den sonraki ilk 20 kapanmış H4 bar içinde `close[t]>close[A]` tetik; giriş sonraki ilk 1m. Short: `high[A]>max(high[A−49:A−1])`, RSI8≥80, `high[B]>high[A]`, `RSI8[B]<RSI8[A]`, sonra `close[t]<close[A]`. B ve tetik pencereleri **bizim** seçimi; aynı A'ya çoklu B yok; teyitten önce yeni A gelirse eski adayı iptal et. Long stop `min(low[A],low[B])−0.1*ATR14_H4`, short simetrik; 3R hedef veya 10 H4 bar süresi. Stop, 0.1 ATR ve süre bizim somutlaştırmamızdır. Yalnız `close[A]` kırılır, ilk barın high/low seviyesi tetik diye değiştirilmez.
- **Karşılaştırma:** İlk mumun `close[A]` kırılması ana sözleşme, `high[A]`/`low[A]` kırılması daha katı alternatif olarak aynı olaylarda ölçülür; ikisi de kaynak belirsizliğinin yorumudur. 50 bar ekstremumu yalnız, RSI eşikli ekstremum, ayrışma, kapanış teyidi sıralı ablation; mevcut RSI divergence adaylarıyla eşdeğerlik kontrolü. İlk dipten ikinci dibe bekleme süresi ve kaçırılmış/iptal olmuş olaylar raporlanır. PDF'nin geri dönüş iddiası test edilmemiştir.

## Öncelik ve uygulama sınırları

R31, üç aşamalı açık tetik nedeniyle öncelikli H4 adaydır. D31a ve D31b, state machine doğrulaması ve TDST/geri dönüşüm yorumları netleştikten sonra denenir; özellikle D31b'nin basitleştirilmiş sürümü tam ticari DeMark algoritması diye etiketlenmez. E31 adayları mevcut MA sinyallerine karşı ancak ek değer gösterirse saklanır. Tüm adaylar point-in-time evren, kapanmış mum, sonraki uygulanabilir fiyat, ücret/spread/kayma/funding ve zaman sıralı dış örneklemle değerlendirilecektir.
