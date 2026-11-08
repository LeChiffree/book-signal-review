# Kitap okuma 001 — ADX, Bollinger, 20 EMA

**Durum:** Üç PDF'nin sırasıyla 41, 37 ve 31 sayfasının tamamı okundu (toplam 109 PDF sayfası). Grafik/tablo içeren örnek sayfalar ayrıca görsel olarak kontrol edildi. Bu dosya işlem sonucu değil, daha sonra geri test edilecek kural sözleşmeleridir. Tüm sayfa numaraları PDF sayfasıdır; basılı sayfa numarası farklı olabilir.

## 1. ADX Göstergesi — Puneet Jain

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/ADX Göstergesi - Puneet Jain (41 sayfa) - @eseckal.pdf>)

Kitap ADX14/DMI14 kullanıyor (s. 3–4). ADX **yönü değil trend gücünü**, +DI/−DI yönü gösteriyor (s. 8–11). Altı konu var: düşük ADX filtresi, ADX ile kırılım, EMA20 geri çekilmesi, DMI hakimiyet değişimi ve ADX ayrışmasında çıkış (s. 41). Son ikisi kitapta yeterince mekanik tanımlanmadığı için ayrı araştırma adayı olarak tutuldu.

### A1 — Düşük ADX sonrası yönlü kırılım

- **Kaynak:** s. 17, 22–23; grafik s. 18.
- **Kitap kuralı:** ADX14 en az 10 bar boyunca 20 altında; fiyat formasyonu/konsolidasyon kırılır; ADX 20 üstüne çıkar; yükselişte +DI yeni tepe ve +DI>20 ile doğrulama.
- **Mekanik günlük aday:** `low_adx_run_10 = all(ADX14[t-10:t-1]<20)`; referans direnç `max(high[t-20:t-1])`; `close_t>direnç`, `ADX14_t>20`, `+DI_t>-DI_t`. +DI'nin son 20 bardaki tepesini kırması ayrı ek filtre olarak denenir. 20 bar kanal, kitapta tanımlanmayan formasyonun **bizim sabit yorumumuzdur**.
- **Özellikler:** düşük ADX dönem uzunluğu, ADX artışı, DMI farkı, kırılım/ATR mesafesi, önceki 20 bar kanal genişliği, hacim oranı.
- **Giriş/çıkış deney sözleşmesi:** günlük sinyal kapanınca ertesi yürütülebilir 1m açılışı; ATR stop, kanal içine geri kapanış ve H3D/H7D/H14D zaman çıkışı ayrı varyantlar. Kitaptaki “trend çizgisi altı stop” çizgi nesnelleştirilmeden uygulanmaz.

### A2 — Güçlü trendde EMA20 geri çekilmesi

- **Kaynak:** s. 27–28.
- **Kitap kuralı:** ADX14 başlangıçta 20 üstünde ve yükseliyor; fiyat EMA20'ye geri çekiliyor; önceki barın tepesinin üstüne alış emri; oluşan salınım dibi altında stop.
- **Mekanik günlük aday:** `ADX14[t-k]>20` ve o anda yükseliyor, `+DI>-DI`; son 1–5 kapalı barda `low<=EMA20` ve geri çekilme öncesi trend var; `close_t>high[t-1]` kapanış onayı. “EMA'ya ulaştı” için `low<=EMA20` ile `abs(low-EMA20)<=0.25*ATR` ayrı varyantlar; k ve eşik yalnız eğitimde seçilir.
- **Özellikler:** EMA20 yüzde ve ATR uzaklığı, ADX düşüş süresi, geri çekilme derinliği, son onay mumunun gövde/ATR oranı.
- **Çıkış:** onaylı salınım dibi veya ATR stop; trailing stop ve zaman çıkışı karşılaştırılır. Kitabın emir bazlı sürümüyle kapalı mum sürümü **aynı sinyal değildir**; ayrı backtest ID'leri gerekir.

### A3 — DMI hakimiyet değişimi ve ADX ayrışması

- **Kaynak:** s. 32–39.
- **Karar:** Kitap görsel örneklerle anlatıyor; pivotların teyit süresi, ayrışma eşiği ve çıkış zamanı net değil. İlk geri teste alınmaz. Önce nedensel pivot ve ADX tepe tanımı yazılıp olay sayısı ölçülsün.

## 2. Bollinger Bantları — Connors Research / Laurence Connors ve Cesar Alvarez

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 11/Baskı 11/Bollinger Bantları - İşe Yarayan Trading Stratejileri - Connors Research - Laurence Connors ve Cesar Alvarez (37 sayfa) - @eseckal.pdf>)

**Kritik formül:** Kitap standart BB(20,2) kullanmıyor. Bant `SMA5 ± 1×std5`, `%B=(close-lower)/(upper-lower)` (s. 5). Mevcut projedeki `bb_percent_b` bu parametrelerle yeniden hesaplanmadıkça kitap sinyali diye gösterilmemeli. Bant genişliği sıfırsa `%B=NaN`.

### B1 — Trend içinde çok günlük derin geri çekilme

- **Kaynak kuralı:** s. 8–9. Likit ABD hissesi, 100 günlük tarihsel volatilite >30, ADX10>30, close>SMA200, BB(5,1) `%B` değeri 2–4 gün boyunca 0.1/0/−0.1 altı. Ertesi gün, sinyal kapanışından %4/6/8/10 aşağı limit emir. `%B>1` kapanışında çıkış; s. 16–18'de `%B>0.5/0.75`, RSI2 ve SMA3/5 çıkışları da karşılaştırılmış.
- **Kripto için mekanik aday:** `close>SMA200`; BB(5,1) `%B<0` koşulu son 2 veya 4 kapalı günlük mumda; ADX10 ve 100 günlük gerçekleşen volatilite ayrı filtreler. Ertesi gün limit mesafesi sabit yüzde yerine `x×ATR/close` ile de denenir. Limit emrin 1m veride gerçekten dolması zorunlu; dolmayan sinyal işlem değildir.
- **Özellikler:** BB(5,1) `%B` seviyesi, alt eşik altında gün sayısı, bant genişliği, `close/SMA200−1`, ADX10, volatilite, limit mesafesi/ATR.
- **Çıkış:** `%B>1` ana kitap varyantı; `%B>0.5`, `%B>0.75`, RSI2 ve SMA3/5 ayrı ablation. Ek olarak projedeki maksimum tutma süresi ve risk stopu önceden sabitlenir. Kitap s. 28 stopların sonuçları düşürebileceğini iddia ediyor, fakat futures için risksiz/limitsiz pozisyon varsayımı yapılmaz.
- **Kanıt sınırı:** Kitabın hisse testleri 2001–2012 dönemi; en iyi varyasyonlar raporlanmış (s. 11–18, görsel tablo s. 12). **Kayma ve komisyon testte yok** (s. 28). Bu yüzdeler kripto için beklenti olarak alınmaz.

### B2 — Aynı sinyalin gün içi çıkışı

- **Kaynak:** s. 20–22. Önceki iki gün `%B<0.1`, ertesi gün derin limitten giriş ve aynı gün kapanışta çıkış.
- **Karar:** Mevcut ilk strateji birkaç günlük günlük karar hattı olduğu için ayrı **gün içi araştırma hattına ertelendi**. Giriş sonrası aynı gün çıkış için 1m yol ve maliyet modeli gerekir.

### B3 — Opsiyon uygulaması

- **Kaynak:** s. 23–26. Kitap hisse opsiyonuyla uygulama anlatır.
- **Karar:** Binance futures OHLCV araştırmasına uygun değil; strateji kataloğuna eklenmez.

## 3. 20 EMA Stratejisi — Jayesh Shah

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/20 EMA Stratejisi - Jayesh Shah (31 sayfa) - @eseckal.pdf>)

Kitap birkaç gün–2/3 hafta süren hisse işlemlerini hedefler (s. 2). Ana üç aşama: fiyatın EMA20 üstüne çıkıp pivot oluşturması; geri çekilmenin EMA20 altına düşmemesi; pivot tepesinin kırılması (s. 7–14). Seçilmiş örnek grafikler performans testi değildir.

### E1 — EMA20 destekli pivot kırılımı

- **Kaynak:** s. 7–16, 24, 28–30; görsel kurulum s. 12.
- **Mekanik günlük aday:** (1) en az N gün EMA20 altında kapanıştan sonra `close>EMA20`; (2) onaylı pivot tepe (sağdaki iki kapalı mum ile teyit, yalnız teyit anından itibaren kullanılabilir); (3) tepe sonrası geri çekilme sırasında `low>=EMA20` katı sürüm ve `close>=EMA20` gevşek sürüm; (4) `close_t>pivot_high` olayında sinyal. Kitap içindeki “EMA'yı hiç geçmesin” ifadesi fitili de dışlar; iki sürüm önceden ayrı kaydedilir.
- **Hacim:** kitap s. 24 kırılım gününde önceki bir ay ortalamasının en az 2 katı hacim kullanıyor. Kriptoda `quote_volume_t / mean(quote_volume[t-20:t-1]) >=2` ve sürekli hacim oranı; sabit 2 eşik ile eşiği olmayan sürüm ayrı test.
- **Özellikler:** pivot yaşı, geri çekilme süresi, minimum EMA20 mesafesi/ATR, kırılım mesafesi/ATR, kırılım mumunun kapanış konumu ve gövde/aralık oranı, quote hacim oranı.
- **Giriş:** kitap gün içi pivot ihlalinde alış diyor; ilk projede kapalı günlük mumdan sonra ilk yürütülebilir 1m açılışı kullanılır. Bu uyarlama kayma yaratabilir; iki sürüm ayrı tutulur.
- **İlk stop:** kitap kırılım mumunun dibinin altını öneriyor (s. 13, 17). Futures için fiyat tikine göre tampon ve risk bütçesi ayrıca tanımlanır. 1m yolunda stop/TP aynı barda görülürse stop önceliği.

### E2 — Çıkış varyantları (E1 girişine bağlanır)

- **Kaynak:** s. 17–24.
- **Varyantlar:** büyük kırmızı gövde, uzun üst fitil veya tepe dojisiyle çıkış; önceki mum dibi trailing stop; sabit yüzde stop/hedef; pozisyonun yarısını +%10–15'te satıp kalana başabaş stop.
- **Mekanik tanım gereği:** “büyük” mum `abs(close-open)/ATR`; uzun üst fitil `upper_wick/(high-low)`; doji `abs(close-open)/(high-low)`; “tepe” son N bar yüksek konumu. Eşikler kitapta nicel değil, eğitim kesiminde sabitlenmeli.
- **Önemli düzeltme:** “yarısını sattıktan sonra daima kâr” söylemi ücret, funding ve kayma sonrası garanti değildir. Maliyet ve kalan pozisyonun durdurulma fiyatı hesaba katılmalı.

## Üç kitabın ortak test sırası

1. İlk sade kontrol: günlük trend ve basit kanal kırılımı. Sonra A1, A2, B1, E1 aileleri ayrı ölçülür; A2 ile E1 farklı giriş mantığıdır.
2. B1 için yeni BB(5,1) özellikleri gerekir; mevcut BB sütunlarıyla karıştırılmaz. ADX10 ile ADX14 de ayrı tutulur.
3. Strateji başına long/flat, H3D/H7D/H14D ve ücret+kayma+funding dahil sonuç; geçmişte o anda açık olan sözleşme evreni. Aynı takvim dönemleri ortak fold'a atanır.
4. Kitap eşiği, çıkış ve filtre çeşitlerinin her biri ayrı denemedir. Fold içi seçim sonrası son holdout bir kez açılır. Kazanma oranı tek karar ölçütü değildir; işlem sayısı, maliyet sonrası beklenti, max drawdown ve rejim/simge tutarlılığı birlikte raporlanır.

**Henüz backtest veya paper test yapılmadı.** Bu partide strateji tanımları kaydedildi; bir sonraki kullanıcı devamında yeni üç kitap seçilecek.
