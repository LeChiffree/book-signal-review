# Kitap okuma 136 — H4 EMA yeniden test ve iki mumluk ters işlem

**Kapsam:** Üç ayrı PDF'nin **3 + 38 + 37 = 78 sayfası** baştan sona okundu. PDF sayfa numaraları kullanılır. Backtest, paper test ve emir yapılmadı.

## 1. H4 Zaman Diliminde 200 ve 50 EMA ile Strateji Oluşturma

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 9/Baskı 9/H4 Zaman Diliminde 200 ve 50 EMA ile Strateji Oluşturma (3 sayfa) - @eseckal.pdf>) · [Tam metin](01_h4_ema200_50.txt)

**Tam okuma:** S. 1 H4 EMA50/EMA200 rejimi ve ilk tepe/dip; s. 2 tepe/dip kırılımı, yeni ekstremum, eski seviyeye yeniden testte limit emir ve 1,5 kat hedef; s. 3 stop, 1R'de başabaş/kısmi kâr ve kaçan emir. Özellikle **ilk ekstremum kırıldıktan sonra yeni ekstremum oluşmasını bekleyip eski kırılan seviyeye dönüşte giriş** sırası, salt EMA kesişiminden farklıdır. “Yakın zamanda” kesişim ve “en görünür” salınım kaynakta sayısal değildir. S. 2'de short örneğinin hedef rakamlarından biri yazım hatalıdır; türetilen mesafe kullanılmalı. S. 3'ün “en az 1:2” iddiası, hedef 1,5×ilk salınım mesafesi olsa da stop ara swing'e konduğu için her olayda matematiksel olarak garanti değildir.

### H136A — EMA50/200 rejiminde kırılan ekstremumun ikinci dönüşü

- **Kaynak kural:** H4 EMA50/EMA200 yönü, eski tepe/dip kırılımı, yeni ekstremumdan sonra eski seviyede limit giriş; stop yakın görünür karşı salınım; hedef ilk salınım mesafesinin 1,5 katı (s. 1–3).
- **Bizim ön kayıt tanımı:** H4 kapanışında EMA50>EMA200 ve kesişim son 30 H4 barda teyit edilmişse long rejim (short ters). Kesişim penceresi bizim parametremiz. `k=2` sol ve sağ barlı, yalnız sağ iki bar kapandıktan sonra bilinen pivot high `P` ve takip eden teyitli pivot low `L` seç. `close[t]>P` ilk kırılım olsun. Sonraki en çok 12 H4 barda `high>P+0,1 ATR14_H4[t]` yeni yüksek oluşturup bar kapansın. O anda `P,L` ve `1,5×(P−L)` hedef mesafesi dondurulur. Sonraki en çok 12 H4 barda `P` seviyesinde buy limit beklet; shortta pivot low kırılımı ve sell limit simetrik. P'ye dönüş olmazsa işlem yok. ATR tamponları, pivot genişliği ve pencereler bizim test varsayımlarımızdır.
- **Risk/çıkış:** Long stop `L−0,1 ATR14_H4` (girişten önce sabit), hedef `P+1,5×(P−L)`; short simetri. Stop yanlış tarafta, hedef girişten en az 1R uzakta değilse veya maliyet sonrası alan yetersizse işlem yok. Limit dolumu ve aynı 1m mumdaki stop/hedef sırası gerçek bid/ask, ücret ve kaymayla; belirsiz sırada stop önceliğiyle çözülür. En çok 42 H4 bar sonra çıkış bizim zaman sınırımız. 1R'de başabaş/kısmi kapama s. 3'teki ayrı varyant, temel adayda kullanılmaz.
- **Kıyas:** Basit H4 EMA50/200 yönlü kırılım ve [mevcut EMA rejim adayları](../batch_031/STRATEGIES.md) ile ortak olay ve eşit risk bütçesinde karşılaştır. Limitin dolmama oranını ve seçilim etkisini raporla. Seçilmiş kaynaktaki grafik getiri kanıtı değildir.

## 2. Currency Grail — Benim Gizli Kayıpsız Forex Scalping Sistemim

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 9/Baskı 9/Currency Grail - Benim Gizli Kayıpsız Forex Scalping Sistemim - Türkçe ve İngilizce (38 sayfa) - @eseckal.pdf>) · [Tam metin](02_currency_grail.txt)

**Tam okuma:** S. 1–3 tanıtım; s. 4–7 iki yükselen barla short ve zaman dilimine göre sabit pip hedef; s. 8 stopsuz bekleme; s. 9–12 iki düşen barla long ve kaçınılacak mumlar; s. 13–19 uygulama notları; s. 20–38 aynı 19 sayfanın İngilizce aslı. Kaynakta “2. bar daha büyük” ile ikinci barın high–close/close–low farkının “önemli ölçüde” daha büyük olması nesnel eşik değildir. Üçüncü bar açılışında ters yönde giriş yapılır. Kaynak hiçbir stop kullanmaz; “kayıpsız” ifadesi, zarar realize edilmeden bekleme ve seçilmiş örneklerden çıkarılmış doğrulanmamış iddiadır. S. 18/37 Bitcoin için **test etmediğini** belirtir. Sabit 1/2/5/20 pip hedefler (s. 7/26), spread ve ücret hesaba katılmadan kârlılık göstermez.

### CG136A — İki genişleyen mumun ters yönlü kısa vadeli tepkisi

- **Kaynak kural:** Short için ikinci bar birinciden daha yüksek high ve low yapar; ikinci bar daha büyük ve üst fitili daha uzundur; sonraki bar açılışında short (s. 4–7/23–26). Long için ikinci bar daha düşük high ve low, daha büyük aralık ve alt fitil (s. 9–10/28–29). Kaynak ikinci bar ucu ötesinde opsiyonel stop örneği verir (s. 8/27).
- **Bizim ön kayıt tanımı:** Likit kripto çiftlerinde H1 kapalı `t−1,t` barları: short `high[t]>high[t−1]`, `low[t]>low[t−1]`, `range[t]≥1,25×range[t−1]`, `high[t]−close[t]≥1,5×(high[t−1]−close[t−1])`, `high[t]−close[t]≥0,25×range[t]`. Longda düşük high/low, `close[t]−low[t]` için simetri. Sıfır fitilli ilk bar da aralık şartıyla değerlendirilsin; sıfır aralıklı bar atılsın. `1,25`, `1,5`, `%25` kaynak sayısı değil, “daha büyük/önemli” sözlerini ölçülebilir yapan bizim eşiklerimizdir. `t` tam kapandıktan sonraki ilk işlem yapılabilir 1m açılışında ters yönde giriş.
- **Risk/çıkış:** Short stop `high[t]+0,1 ATR14_H1[t−1]`, long stop `low[t]−0,1 ATR`; hedef 1R, en çok 3 H1 bar. Hedef/stop/zaman sınırı bizim güvenli test sözleşmemizdir; **kaynağın stopsuz sisteminin aynısı değildir**. Forex 5 pip hedefi kriptoya aktarılmaz. Bid/ask, ücret, kayma, likidite, aynı 1m bardaki stop önceliği ve karşıt sinyalde tek pozisyon sınırı dahil. İşlem başına sabit %0,5 özsermaye riskini aşma.
- **Kıyas:** Rastgele yön değil, aynı iki bar koşullarında trend yönünde giriş ve yalnız üst/alt fitil reddi adaylarıyla eşit işlem maliyetinde kıyasla. Özellikle pozitif brüt getirinin spread sonrası kaybolup kaybolmadığını ölç. Kaynaktaki “sıfır kayıp” iddiasını hipotez kabul etme.

## 3. Kolaylaştırılmış Elliott Dalgaları — Acrotec

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 9/Baskı 9/Kolaylaştırılmış Elliott Dalgaları - Acrotec (Orijinal) (37 sayfa) - @eseckal.pdf>) · [Tam metin](03_elliott_acrotec.txt)

**Tam okuma:** S. 1–5 teori; s. 6–10 dalga 2/3/4 sayım kuralları; s. 11–17 uzama, çapraz üçgen ve başarısız beşinci dalga; s. 18–24 zigzag, flat, irregular, yatay üçgen ve birleşimler; s. 25–35 Elliott kanalı çizimleri; s. 36–37 kaynakça. Kitap dalga pivotlarını hangi kapanmış fiyatlarla ve hangi anda sabitleyeceğini, girişi, stopu ve çıkışı belirtmez. Üçüncü dalganın en kısa olmaması gibi kurallar **beşinci dalga tamamlanmadan** sınanamaz; bunu erken giriş koşulu saymak ileri bilgi olur. Başarısız beşinci dalga s. 16–17'de anlatılır fakat sayım geriye dönük yeniden etiketlenebilir. Bu metinden bağımsız kapalı mum stratejisi çıkarılmadı. **Yeni aday yok.**

## Sonuç

**2 yeni araştırma adayı:** H136A ve CG136A. İkisi de yalnız ön kayıtlı backtest hipotezidir; doğrulanmış getiri değildir.
