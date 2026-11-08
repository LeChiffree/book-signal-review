# Kitap okuma 036 — kutu kırılımı ve destek/direnç

**Kapsam:** 54 + 12 + 22 = **88 PDF sayfası**. Üç PDF'nin tamamı sayfa sıralı metne çıkarıldı; metinsiz kritik grafiklerden Connors s. 18 ve Gerçek Destek ve Direnç s. 6 ayrıca görsel incelendi. Sayfa numaraları PDF sayfasıdır. Aşağıdaki sayısal kurallar kaynakta yoksa açıkça **bizim deney tanımımız** olarak belirtilir. Backtest, paper test veya emir yapılmadı.

## 1. John Connors — Koparma Ticareti

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Koparma Ticareti - John Connors (54 sayfa) - @eseckal.pdf>) · [Tam metin](01_breakout_connors.txt) · [Grafik s. 18](connors_p18.png)

**Kaynak:** Önce yatay fiyat kutusunun üst ve alt sınırını saptar (s. 12–15). Güçlü mumun kutu **dışında kapanması** gerekir; gövdesi kutu içi mumlardan büyük ve kapanış yönlü uca yakın olmalı, aşırı uç büyüklükteki kopuş kovalanmamalıdır (s. 16–25). S. 18 grafiği alt sınırın altındaki güçlü düşüş mumunu gösterir. Marjinal çıkış ve kutuya geri dönüş zayıf/yanlış kopuştur (s. 25–28). Stopu kırılan sınıra göre eski kutunun %10–15 içine koyar (s. 30); asgari hedef 2R (s. 33). Pozisyonun yarısını 2R'de kapatıp kalanı başabaş stop ve EMA20 karşı kapanışı veya gün sonuna dek taşıma örneği vardır (s. 41–46). Üst zaman dilimi trendi yön filtresi olarak önerilir (s. 47–49). Kutunun tam seçimi, 'güçlü/aşırı' gövdenin kesin eşiği ve işlem maliyetleri verilmez.

### C36 — Güçlü kapanışlı kutu kırılımı

- **Bizim D1 deney:** Sinyal günü `t` açılmadan bilinen `U=max(high[t−20:t−1])`, `L=min(low[t−20:t−1])`; `W=U−L`. Son 20 tamamlanmış barda üst ve alt kenara `0.15 ATR14[t−1]` içinde en az ikişer dokunuş ve `W<=4 ATR14[t−1]` şartı. `close[t]>U+0.1 ATR14[t−1]` long, alt sınır için simetri. Kırılım gövdesi son 20 gövdenin maksimumundan büyük, fakat aynı kümenin medyanının 3 katından küçük; kapanış mum aralığının yönlü son %20'sinde. Bu pencere, dokunuş, ATR ve gövde eşikleri **bizim** test hipotezimizdir. Mum tam kapanmadan sinyal yok.
- **İcra/risk:** Sonraki ilk uygulanabilir 1m fiyatıyla giriş. Long stop `U−0.10W`, short stop `L+0.10W`; giriş ile stop arasındaki fark pozitif ve toplam maliyetin en az 2 katı olmalı. 2R'de yarısını çıkar; kalanın stopunu gerçekleşen girişe taşı ve D1 EMA20'nin karşı tarafında ilk kapanışta veya 10 D1 bar sonra çıkar. Tek hedef 2R ve üst zaman dilimi EMA yön filtresi ayrı kollar. Kaynağın %10–15 stop bandının %10 ucunu seçtik; günlük 10 bar azami süre, maliyet tabanı ve EMA'nın mekanik uygulaması bize aittir.
- **Öncelik:** Batch034 N34 ve batch035 S35 ile aynı breakout olayları üzerinde eşleştir; ek katkıyı yalnız güçlü gövde/kapanış ve kutu içi stop farkından ölç. Çok katı gövde koşulu sinyal sayısını azaltabilir; başarısız/az örnek sonucu da kaydet.

## 2. Gerçek Destek ve Direnç

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 10/Baskı 10/Gerçek Destek ve Direnç (12 sayfa) - @eseckal.pdf>) · [Tam metin](02_true_support_resistance.txt) · [Grafik s. 6](true_sr_p6.png)

**Kaynak:** Tekrarlı dönüşlerde yatay seviyeler yerine eğimli destek/direnç doğruları (TRSL) çizer (s. 1–3); doğruların kesişmesi ve daralma olası tepki/kopuş alanları olarak anlatılır (s. 5–7). S. 6'daki iki grafik bazı tepkilerin kesişimden **önce** veya boşlukla olduğunu gösterir; kesişim tam zamanlı sinyal değildir. Kırılan desteğin direnç olarak tekrar test edilmesi (s. 9–10) ve kanal dışına çıkış (s. 11) fikirleri var. Pivot seçimi, dokunuş toleransı, çizginin geçerlilik süresi ve çıkış kesin değildir; bu nedenle kaynaktan tekil, hazır bir işlem algoritması çıkmıyor.

### T36 — Teyitli eğimli seviyenin kırılım ve retest adayı

- **Bizim H4 deney:** Pivot ancak solunda ve sağında 3'er **tam kapanmış** H4 mum varsa onaylanır. Son 60 tamamlanmış H4 içinde iki teyitli pivot high üst doğruyu, iki teyitli pivot low alt doğruyu kurar; doğru uçları onay zamanına kadar sabitlenir. İki sınır arasındaki öngörülen uzaklık önceki 10 barda azalıyorsa ve bugün pozitifse daralma sayılır. `close[t]` üst doğrunun `0.1 ATR14_H4[t−1]` üzerinde kapanırsa, sonraki 5 H4 içinde ilk üst sınıra geri dokunup tekrar üstünde kapanan mum long; alt yön simetrik. Stop karşı sınır veya 1 ATR (hangisi yakınsa fakat maliyet tabanını karşılıyorsa); 2R hedef veya 20 H4 bar zaman çıkışı. **Tüm** rakamlar ve retest teyidi bizim operasyonelleştirmemizdir.
- **Çekince:** Çizgiler grafikte geriye bakarak seçilirse yanıltıcı sonuç doğar. Retest yoksa işlem yok; s. 6'daki kesişim resmi tek başına ileriye dönük tahmin sağlamaz. Önce batch035 üçgen/kırılım ve daha önceki trend çizgisi sinyalleriyle olay eşdeğerliğini kontrol et; bağımsız strateji olarak önceliği düşük.

## 3. Investija — Destek ve Dirençler

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Destek ve Dirençler - Investija (22 sayfa) - @eseckal.pdf>) · [Tam metin](03_support_resistance_investija.txt)

**Kaynak:** Yazar piyasanın trend mi yatay mı olduğunu tek zaman dilimindeki destek/direnç çizgileriyle değerlendirir (s. 3–10); zıt renkli ardışık mumların dönüş noktalarına çizgi yerleştirir, fitil geçişini değil **saat kapanışını** kırılım sayar (s. 8–9). Önce yönü, stop konumunu ve en az **1:2** risk/ödülü belirleyip ancak uygun fiyatta girer (s. 17–19). Yatay USD/CHF örneğinde önceki yön yukarı olduğu için alt sınır yakınında alış, üst sınır yakınında çıkış düşünür (s. 18); trend örneğinde kırılan direncin yeniden destek olmasını bekler (s. 19). Çıkış önceki direnç/destekte ve yaklaşık 1.5–2R üstünde olmalıdır (s. 21–22). S. 14–16'daki zihinsel stop ve s. 22'de zararlı pozisyonu tutma anlatımı güvenilir, mekanik risk kontrolü değildir; aday kurala alınmadı. S. 19 örneğinde sayılar/çeviri tutarsız görünüyor; tekil fiyatları kural yapmıyoruz.

### I36 — Önceki trend yönünde bant kenarı, 2R filtresi

- **Bizim H4 deney:** Son 40 **tam kapanmış** H4 barın `U=max(high)`, `L=min(low)` sınırlarına `0.2 ATR14_H4` yakın en az ikişer temas; `U−L` 2–6 ATR arasında. Önceki 60 H4 barın `EMA20>EMA50` eğilimi long yönünü, tersi short yönünü seçer. Long için `low[t]<=L+0.2 ATR` ve `close[t]>L+0.2 ATR` olduğunda sonraki ilk 1m giriş; stop `L−0.2 ATR`, hedef `U−0.2 ATR`. Girişte net olası ödül/risk en az 2 ise işlem al; 20 H4 bar sonunda çık. Short simetrik. Pencere, temas, ATR, EMA ve süre **bizim** tanımlarımız; kaynak mekanik eşik vermez.
- **Ayrı karşılaştırma:** Kırılan `U` üstünde H4 kapanışından sonraki ilk retest `close>U` ise long düşüncesi s. 19'dan gelir; test edilirse sabit stop `U−0.2 ATR`, önceden bilinen sonraki direnç hedefi ve girişte ≥2R şartı gerektirir. Sonraki direnç bilinemiyorsa hedef uydurup sinyal kaydetme. Önce mevcut bant sekmesi ve kırılım-retest kayıtlarıyla örtüşmeyi ölç.

## Test sırası ve ortak kontrol

Önce **C36**'yı mevcut kutu kırılımı tabanına karşı, sonra **I36**'yı mevcut bant sekmesi tabanına karşı değerlendir; **T36** çizgi seçim duyarlılığı yüzünden araştırma önceliğinde geride. Point-in-time varlık evreni, kapanış sonrası uygulanabilir fiyat, komisyon/spread/kayma/funding, aynı bardaki stop-hedef sırası ve zaman sıralı dış örneklem zorunlu. Bunlar henüz test edilmemiş hipotezlerdir; kaynaklardaki grafik örnekleri getiri kanıtı değildir.
