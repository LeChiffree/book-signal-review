# Kitap okuma 107 — hisse tarayıcısı ve fix verisi denetimi

**Kapsam:** Üç özgün PDF'nin **20 + 18 + 16 = 54 sayfası** baştan sona okundu. Atıflar PDF sayfasıdır. Bu turda backtest, paper test veya emir yapılmadı. Kitaplardaki kâr ve kurumsal niyet iddiaları doğrulanmış veri değildir.

## 1. Forex Trading Şifresi — Alberto Sassetti

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 28/Baskı 28/Forex Trading Şifresi - Alberto Sassetti (20 sayfa) - @eseckal.pdf>) · [Tam metin](01_forex_code_sassetti.txt)

**Tam okuma:** S. 1–4 tanıtım ve Londra kapanışı; s. 5–7 BFix/CME fix öncesi yön ve sonrası geri dönüş; s. 8–9 CME vadeli, COT aşırılığı; s. 10 spread fikri; s. 11 haber öncüleri; s. 12–14 kurumsal çoklu vade anlatısı; s. 15–20 bağlantılar/yazar. S. 5–7'de 10:00 CT = 16:00 GMT eşitliği yıl boyu geçerli değildir; CT yaz saati değişir. Daha önemlisi 15:50'de “beklenen fix fiyatı”nın nasıl hesaplandığı, o anda gerçekten yayımlanıp yayımlanmadığı ve spot/futures dönüşümü açıklanmaz. Aynı gün 16:00 fix'i 15:50 işlemine girdi yapmak bilgi sızıntısı olur. [106. partideki](../batch_106/STRATEGIES.md) LS106A yalnız yayımlanmış *önceki* fix'i kullanır; bu metin aynı veri ailesini tekrarlar. COT s. 8 “non-commercial artışıyla long” derken s. 9 %70–80 long/kısa aşırılığında tersine dönüş önerir; yayın gecikmesi, oran paydası, giriş/stop/çıkış belirtilmez. COT ve faiz/haber adayları [28. partide](../batch_028/STRATEGIES.md) ayrı veri gereksinimiyle zaten ayrılmıştı. Yeni bağımsız aday açılmadı. Fix, emir akışı ve “garantili likidite” iddiaları fiyat kaydından kanıtlanamaz.

## 2. Swing Trading için Hisse Tarama Aracı — Abhishek Jain

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 25/Baskı 25/Swing Trading için Hisse Tarama Aracı - Abhishek Jain (18 sayfa) - @eseckal.pdf>) · [Tam metin](02_swing_screener_jain.txt)

**Tam okuma:** S. 1–7 tanıtım, psikoloji, D1 grafik; s. 8–13 tarayıcı; s. 14–15 yön/giriş/stopun tarayıcıdan **çıkmadığı** uyarısı; s. 16–18 sermaye ve örnek kâr hesabı. Tarayıcı kuralları açıkça s. 8–13: günlük hisse hacmi >500.000 adet, önceki 10 gün ortalaması >500.000, 30 gün ortalaması >250.000, göreli hacim >1,5, piyasa değeri >₹10 milyar, bir ay içinde kazanç duyurusu ve ATR >₹10. Ancak göreli hacmin karşılaştırma penceresi, ATR periyodu, kazanç ilanının ilk yayın tarihi belirtilmez. S. 14 açıkça **işlem yönünü belirlemez** ve s. 15 giriş/çıkış vermez. Bu bir strateji adayı değil, likit/oynak hisse *evren filtresi* taslağıdır.

**İleride evren deneyi için sözleşme (bizim tamamlayıcı tanımlarımız):** Hindistan hisse piyasasında tarihsel hayatta olan ve o tarihte işlem gören tüm hisseler, survivorship-free; her D1 kapanışında hacim `V_t>500k`, `mean(V[t-9:t])>500k`, `mean(V[t-29:t])>250k`; RVOL `V_t/mean(V[t-20:t-1])>1.5`; t anındaki geçmiş piyasa değeri >₹10bn; Wilder ATR14_D1 >₹10. Kazanç takvimi yalnız t öncesi yayımlanmış ve t+30 takvim günü içinde kesinleşmiş tarihse ayrı filtre; düzeltme/iptal vintajı korunur. Önceki eşiklerin birlikteliği yalnız aynı D1 kapanışında bilinebilir, giriş en erken sonraki seans. Bu filtre mevcut yönlü sinyallerin evren seçimi ablation'ıdır; tek başına al/sat emri değildir. 20 gün RVOL, ATR14 ve kazanç takvimi davranışı **bizim** seçimlerimizdir. S. 16–17'deki %20 sermaye tahsisi ve ayrılan sermayenin %2 riski toplam sermayenin %0,4'üdür; kazanma oranı varsayımı gelecekteki performans kanıtı değildir.

## 3. Price Action Trading Stratejileri — Matthew Robert

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 19/Baskı 19/Price Action Trading Stratejileri - Matthew Robert (16 sayfa) - @eseckal.pdf>) · [Tam metin](03_price_action_robert.txt)

**Tam okuma:** S. 1–4 fiyat hareketi tanımları; s. 5–6 trend/kanal; s. 7–8 MACD/RSI/ADX ve trend; s. 9–10 birikim/dağıtım ile kırılım sonrası kapanış; s. 11–14 destek/direnç, fiyat dalgası ve “emilim” yorumu; s. 15–16 mum fitilleri ve trend çizgisi + yatay kırılım. S. 10 kırılımda kapanış veya sonraki gün teyidi tavsiye eder, fakat kırılacak seviyenin ve çıkışın kesin tanımı yok. S. 16 trend çizgisi kırılımına yatay yeni high/low teyidi ekler; pivot/çizgi tespiti tanımsız ve önceki trend çizgisi, yapı kırılımı adaylarıyla örtüşüyor. S. 9'daki destek/direnç rolleri bazı cümlelerde ters yazılmış; s. 15 broker saatinin H4/D1 mumlarını etkileyebileceğini kabul ederken “etkisi yoktur” demesi de güvenilir bir varsayım değildir. Mevcut arşivde kapalı mum, geçmişten teyitli pivot ve grafik saati şartları zaten vardır. Yeni bağımsız aday sayılmadı.

## Sonuç

**0 yeni strateji adayı.** Üç kitap tamamen incelendi; Jain filtresi gelecekteki hisse evreni testi için kaydedildi, diğer fikirler mevcut adaylarla veya veri sızıntısı riskiyle eşleşti.
