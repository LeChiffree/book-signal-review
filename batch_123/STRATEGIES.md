# Kitap okuma 123 — önceki günün bir ucunu aşıp karşı ucunu kırmak

**Kapsam:** Üç ayrı PDF'nin **43 + 28 + 37 = 108 sayfası** baştan sona okundu. Sayfa atıfları PDF sayfasıdır. Backtest, paper test ve emir yapılmadı.

## 1. Alpesh Pansheriya — Kanıtlanmış 8 Price Action Stratejisi

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 20/Baskı 20/Kanıtlanmış 8 Price Action Stratejisi - Alpesh Pansheriya (43 sayfa) - @eseckal.pdf>) · [Tam metin](01_eight_price_action.txt)

**Tam okuma:** S. 1–8 trend/aralık, destek/direnç ve klasik dönüşler; s. 9–12 mumlar, bayraklar ve üçgenler; s. 13–17 yükselen/alçalan salınım, MA ve geri çekilme; s. 18–22 çift tepe/dip ile baş-omuz; s. 23–26 kırılım/retest ve sahte kırılım; s. 27–30 aralık sınırından işlem; s. 31–34 trend çizgisi ve seviye çakışması; s. 35–43 risk, psikoloji ve özet. Başlıktaki “kanıtlanmış” sözüne rağmen yöntem bazında işlem listesi, örneklem ve masraf hesabı yok. Sekiz başlık, arşivdeki mum, pivot, MA geri çekilmesi, rol değiştiren seviye, SFP, aralık ve çizgi ailesini yeniden anlatıyor; bağımsız yeni aday sayılmadı. S. 9'da `close` açıklamasının açılış diye çevrilmesi bar verisinde uygulanmamalı.

## 2. Tyler Aaron — Price Action Trading

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 19/Baskı 19/Price Action Trading - Tyler Aaron (28 sayfa) - @eseckal.pdf>) · [Tam metin](02_tyler_price_action.txt)

**Tam okuma:** S. 1–10 büyük zaman diliminden küçük zaman dilimine trend hiyerarşisi; s. 11–15 H4/H1/M15 ile stokastik ve doji örneği; s. 16–19 H1 trendi/M15 BB daralması ve D1/H4 MA kısa örneği; s. 20–24 işlem stiline göre zaman dilimi seçimi; s. 25–28 üç zaman dilimi kuralı. S. 15'te seçilmiş örneğin “400 pip kazanırdı” ifadesi canlı uygulanabilir sonuç değildir. Göstergelerin bar kapanışında hangi sırayla doğrulandığı ve çıkış sözleşmesi verilmez. Çoklu zaman dilimi filtresi ve BB kırılımı önceki adaylarda var; **yeni bağımsız aday yok**. Daha büyük barı kapanmadan küçük bar kararına dahil etmek görünüm yanlılığı yaratır; ilerideki varyantlarda son *tamamlanmış* H4/D1 kullanılmalıdır.

## 3. Thomas Carter — Forex Trend Takip Stratejileri

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 8/Baskı 8/Forex Trend Takip Stratejileri - Thomas Carter (37 sayfa) - @eseckal.pdf>) · [Tam metin](03_carter_trend_follow.txt)

**Tam okuma:** S. 1–4 giriş; s. 5–19 strateji 1–10: EMA/SAR, MACD, stokastik, RSI, ADX/DMI ve DPO kesişimleri; s. 20 önceki gün uçlarını ters sırayla geçme; s. 21–30 CCI/RSI3 ile EMA trendi ve EMA geri çekilmesi; s. 31–36 SAR ile Schaff trend döngüsü ve diğer kesişimler; s. 37 kapanış. Çoğu strateji önceki gösterge/kesişim ailesinin periyot, pip hedefi veya filtre varyantıdır. S. 23'te RSI3+stokastik fikri [086. partide](../batch_086/STRATEGIES.md) de saptanmıştır. S. 33'te Schaff göstergesinin özgül formülü/sürümü belirtilmez; `-10...110` ölçeği uygulamaya özel olabilir. S. 18–19 DPO'nun grafiklerde merkezlenmesi gelecekteki veriyi kullanabilir; yeniden boyamayan tanım olmadan sinyal sayılmaz. S. 5'te SAR parametre sırası belirsizdir. Kitapta strateji bazında doğrulanmış performans yoktur.

### TC123A — Düşük ADX ortamında önceki günün bir ucunu aşıp karşı ucu kırmak

- **Kaynak (PDF s. 20, strateji 11):** `ADX14<35` iken önce önceki gün dip seviyesinin en az 15 pip altına inme, ardından önceki gün tepesinin 15 pip üstünde buy-stop; short için önce önceki günün tepesinin 15 pip üstüne çıkma, sonra dip seviyesinin 15 pip altında sell-stop. Girişten en çok 30 pip stop, 60 pip hedef. Kaynak bu iki olayın aynı gün olup olmayacağını belirtmez; aşağıdaki sabit süre **bizim** uygulama kuralımızdır.
- **Kapalı mum ve emir sözleşmesi:** EURUSD, GBPUSD, USDJPY, USDCHF, USDCAD, AUDUSD ve NZDUSD; FX broker'ın New York 17:00 günlük mum sınırı ve H1 karar barları. Her FX günü başlamadan önce **tamamlanmış önceki günün** `H_prev,L_prev` düzeylerini dondur. Long hazırlığı: bugünün tamamlanan ilk H1 barında `low <= L_prev−15 pip` ve `ADX14(H1)<35`; hazırlık ancak bu H1 kapanışında bilinir. Sonraki H1'den başlayarak aynı FX günü bitene dek `H_prev+15 pip` buy-stop açık tut; short simetri (`high >= H_prev+15 pip`, sonra `L_prev−15 pip` sell-stop). Gün sonuna dek dolmazsa iptal. İki yön aynı gün hazırlanırsa o günü atla (**bizim** çakışma kuralımız). İlk fill gerçek bid/ask üzerinden; atlamalı açılışta önceden bilinen stop fiyatından ideal dolum yazma. Başlangıç stopu fill'den 30 pip karşı yönde, hedef 60 pip; aynı gün NY 17:00 çıkışı **bizim** süre sınırımız. En çok 1 işlem/çift/gün, %0,5 özsermaye riski, komisyon, spread, kayma ve hafta sonu gapleri dahil. Aynı M1'de stop/hedef sırası çözülemezse kötümser stop önce.
- **Ayrışma:** [Önceki gün sınırında süpürme ve karşı sınır hedefi](../batch_040/STRATEGIES.md) ile bu adayın **karşı sınırın ötesine 15 pip kırılımı** farklı olaydır. Aynı FX döneminde ADX<35 filtresiz, yalnız karşı sınır breakout ve 15 pip yerine 0/30 pip tampon kolları önceden sabitlenerek kıyaslanır. ADX rejimi veya çift uçlu gün seçiminin katkısı, gerçekleşen ve iptal edilen emir sayısıyla birlikte ölçülür. Geçmiş gün sınırlarını gün sonunda yeniden kurma veya gün içindeki son ekstremi kullanma yasaktır.

## Sonuç

**1 yeni araştırma adayı:** TC123A. Kaynakta tarif edilen diğer gösterge ve fiyat hareketi kuralları önceki kayıtların varyantlarıdır; hiçbirinin getirisi bu taramayla doğrulanmadı.
