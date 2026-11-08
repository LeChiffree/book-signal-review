# Kitap okuma 087 — gösterge sözlüğü ve günlük sinyal derlemeleri

**Kapsam:** Daha önce tamamlanmamış üç PDF'nin **25 + 61 + 70 = 156 sayfası** okundu. Kural ve örnek sayfalarından seçilen 13 sayfa görsel olarak [incelendi](figure_contacts/). Sayfa numaraları PDF sayfalarıdır. Bu kayıt strateji ön kaydıdır; backtest, paper test ve emir yapılmadı. Kaynakların başarı yüzdeleri ölçülmüş performans kabul edilmez.

## 1. En İyi 25 İndikatör — Frank Luther

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 20/Baskı 20/En İyi 25 İndikatör - Frank Luther (25 sayfa) - @eseckal.pdf>) · [Tam metin](01_indicators.txt)

**Sayfa haritası:** s. 1–9 momentum ve trend göstergeleri; 10–13 ortalamalar, Supertrend, SAR; 14–21 hacim göstergeleri; 22–25 VWAP, bantlar, Donchian, ATR ve piyasa genişliği. S. 13, 23–24 görsel incelendi.

**Karar:** Bu kitap tek tek göstergeleri tanıtıyor; tam giriş, zarar durdurma ve çıkış kuralı veren yeni bir işlem kurulumu yok. RSI, MACD, ADX, OBV, MFI, VWAP, Bollinger ve Donchian önceki adaylarda zaten kullanılıyor. S. 24–25'teki 50/150/200 günlük ortalama üstündeki sembol yüzdesi ve advance/decline oranı, geçmişe dönük evren üyeliği korunursa piyasa rejimi özelliği olarak araştırılabilir; tek başına yeni strateji sayılmadı. S. 23 Donchian açıklaması ortalama temelli gibi görünüyor; kodlamada gerçek yüksek/düşük kanal tanımı kullanılmalı. SAR yönünü anlatan s. 13 metni de güvenilir bir bağımsız kural oluşturmuyor.

## 2. Al ve Sat Günlük Trading Sinyalleri — 2022 Baskısı

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 3/Baskı 3/Al ve Sat Günlük Trading Sinyalleri - 2022 Baskısı (61 sayfa) - @eseckal.pdf>) · [Tam metin](02_daily_signals.txt)

**Sayfa haritası:** s. 1–13 RSI varyantları; 14–26 Bollinger ve RSI üstüne Bollinger; 27–47 topluluk betikleri; 48–61 HMA, SSL, VWMA, Trend Magic, PMax, EMA500 ve Gauss kanalı. S. 21, 23, 52–53 görsel incelendi.

### VW87 — VWMA10/21 kapanış kesişimi

- **Kaynak:** Hızlı VWMA10, yavaş VWMA21'i yukarı kesince alış; aşağı kesince satış (s. 52–53). Kaynak stop, hedef, zaman aşımı, hacim türü veya işlem frekansı belirtmiyor. “Daha doğru” iddiasını kanıt olarak almıyoruz.
- **Bizim nedensel olay:** UTC D1 kapanmış mumlarda `VWMA_n[t] = Σ_{i=t-n+1}^{t}(close[i]×volume[i]) / Σ volume[i]`. Birincil hacim alanı veri sözleşmesindeki base hacim; quote hacim ayrı ön kayıtlı duyarlılık kolu. Sıfır toplam hacim ve eksik 21 günlük geçmişte sinyal yok. Long `VWMA10[t-1]≤VWMA21[t-1]` ve `VWMA10[t]>VWMA21[t]`; short tersi. Tekrarlayan aynı yön sinyali yok, eşitlikte pozisyon değiştirme yok.
- **İcra/risk:** Kapanıştan sonraki ilk uygulanabilir 1m açılışında giriş. `ATR14_D1[t]` ile 2 ATR başlangıç stopu, 2R hedef; karşıt VWMA kesişiminden sonraki ilk 1m veya en geç 14 gün sonunda çıkış. Stop/hedef/süre ve D1 ölçeği **bizim** seçimlerimiz. Stop yanlış tarafta, 1m fiyat veya maliyet alanı eksikse işlem yok. 1m içindeki eşzamanlı stop/hedef temasında stop önceliği; ücret, kayma ve funding dahil.
- **Örtüşme/karşılaştırma:** [VWMA20 eğimli kırılım](../batch_034/STRATEGIES.md) farklı olaydır; aynı karar günleri üzerinde VWMA10/21 ile SMA10/21 ve EMA10/21 kesişimi karşılaştırılmalı. VWMA üstünlüğü ayrıca hacim alanı ve yüksek hacimli tek bar etkisine duyarlılıkla sınanmalı.

**Tekrar/eksik tanım:** RSI2 ve fiyat Bollinger dönüşleri önceki kayıtlardaki parametrik varyantlar; RSI serisi üstüne Bollinger [086. parti](../batch_086/STRATEGIES.md) ile örtüşür. S. 27–47, 54–61'deki topluluk betiklerinin tam kodu/sürümü ve yeniden boyama davranışı bu PDF'de verilmediği için özgün gösterge çıktıları adına yeni test stratejisi kaydedilmedi.

## 3. Yüksek Kazanç Oranlı Günlük Trading Kurulumları — Marcel Robbinson

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 4/Baskı 4/Yüksek Kazanç Oranlı Günlük Trading Kurulumları - Marcel Robbinson (70 sayfa) - @eseckal.pdf>) · [Tam metin](03_robbinson.txt)

**Sayfa haritası:** s. 1–14 giriş ve ADX/özel filtre; 15–42 topluluk göstergeleri; 43–70 yedi birleşik kurulum. S. 52–55, 60, 63 görsel incelendi.

**Tekrar kararı:** S. 52–55'te `MFI21`/`SMA18(MFI)` kesişimi, HMA65 ve SMA200 yön filtresiyle tanımlanıyor; bu **aynı kombinasyon** [024. parti](../batch_024/STRATEGIES.md) s. 73–74 notunda önceden kaydedilmiş. Farklı kitap/yazar etiketini bağımsız strateji diye saymıyoruz. Buradaki sayfalar uzun girişte MFI kesişiminin 50 altındayken, kısa girişte 50 üstündeyken olmasını ekliyor; ileride kod/sürüm doğrulaması yapılırsa önceki adayın 50 rejimi varyantına işlenmeli. Özel HMA mum rengi ve MFI çizgi rengi kaynak betik olmadan bire bir tekrarlanamaz.

**Ertelenenler:** S. 45–51 ve 56–70'te UT Bot, HalfTrend, B/C Filter, Reversal Finder, CM Pivot Bands ve KDJ birleşimleri özel topluluk kodlarına bağlı. Kaynak kodu, sürüm, bar kapanışında değişmeme ve parametreler doğrulanmadan bunların grafikteki oklarını ölçülebilir sinyal sanmıyoruz. S. 63–66 BB + RSI5 + ADX<25 çekirdeği [014. parti](../batch_014/STRATEGIES.md) ile zaten örtüşüyor. S. 60 Williams %R −80 bölgesini “aşırı alım” diye adlandırıyor; bu standart osilatör yönüyle çelişir. Performans yüzdeleri örneklem, maliyet ve bağımsız doğrulama içermiyor.
