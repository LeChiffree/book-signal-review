# Kitap okuma 163 — büyük hareketler, momentum hisseleri ve çoklu zaman dilimi

Üç ayrı PDF'nin **58 + 59 + 58 = 175 sayfası** sırayla tarandı. Atıflar PDF sayfasıdır. **Yeni bağımsız araştırma adayı: 1.** Backtest, paper test ve emir yapılmadı.

## 1. Büyük Piyasa Hareketlerini Nasıl Yakalayabilirsiniz — L.R. Thomas

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 16/Baskı 16/Büyük Piyasa Hareketlerini Nasıl Yakalayabilirsiniz - L.R. Thomas (58 sayfa) - @eseckal.pdf>) · [tam metin](01_big_moves_thomas.txt)

**Tarama:** s. 1–6 trend ve pozisyon büyütme; 7–43 aylık/haftalık seviye, trend çizgisi ve kanal üstünden H4/günlük girişle seçilmiş örnekler; 44–49 gün içi kanal ve MA3/MA10 momentumu; 50–58 H1 parabolik dönüş ve M5 destek/direnç kırılması. S. 46'daki fiyatın MA3'ü aşarken MA10'a değmemesi tek başına giriş/çıkış değildir. S. 52'deki “dikey hareket”, yanal bölüm, ikinci taraf, s. 56–57'deki uygun bağlam ve elle çizilen seviye nesnel eşiklerle tanımlanmıyor. Kanal kırılması/retesti, çoklu zaman dilimi ve trend dönüşü mevcut adaylarla örtüşür. **Yeni bağımsız aday yok.**

## 2. Yüksek İvmeli Hisselerde İşlem Yapmayı Öğrenin — Matthew R. Kratter

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 19/Baskı 19/Yüksek İvmeli Hisselerde İşlem Yapmayı Öğrenin - Matthew R. Kratter (59 sayfa) - @eseckal.pdf>) · [tam metin](02_momentum_stocks_kratter.txt)

**Tarama:** s. 1–10 şirketlerin yıllık gelir büyümesiyle izleme listesi; 11–18 SMA50/SMA200 giriş, %15 stop, ters kesişim veya %300 fiyat artışında çıkış ve pozisyon boyu; 19–44 seçilmiş tarihsel hisse örnekleri; 45–53 açığa satış ve ödünç maliyeti; 54–59 sonuç. Kitap s. 12'de ortalamayı basit kapanış ortalaması olarak tarif ediyor; bu **EMA değil SMA**. S. 9–10 yıllık gelir büyümesi >%20, üç yıllık ortalama tercihen >%20. S. 11'de SMA50 yukarı kesişimi ve fiyatın SMA50 üstünde olması birlikte gerekiyor; s. 14–15'te üç alternatif çıkış var. S. 15'teki %90 stop oranına rağmen pozitif ortalama beklenti hesabı, işlem dağılımı ve maliyet olmadan sonuç değildir. S. 17'de 77,82 adedin 80'e yuvarlanması önceden belirlenen %2 riski aşar; aşağı yuvarlanmalı. Hisse evreni ve yayın zamanı bilinmeyen finansal verilerle yapılan geriye dönük tarama ileriye bakma yanlılığı yaratır.

### MK163A — Gelir büyümesi seçimiyle SMA50/200 momentum takibi

- **Kaynak kural:** Yıllık gelir büyümesi >%20 olan hisseyi izle (s. 9–10). Günlük SMA50, SMA200'ü aşağıdan yukarı keser ve kapanış SMA50 üstündeyse ertesi seans açılışında al (s. 11–12). Alış fiyatının %15 altındaki stop, SMA50'nin SMA200 altına geçmesi sonrası ertesi açılış veya girişten %300 yükselişte tam çıkıştan ilk gerçekleşenini uygula (s. 14–15). Short sürümünü kaynak yeni başlayanlara önermiyor (s. 53); bu aday yalnız long.
- **Ön kayıtlı evren/veri:** Likit ABD adi hisseleri, o tarihte listede olan ve sonradan delist olmuş hisseler dahil. Tarihsel bölünme/temettü, seans açılışları, işlem maliyeti ve *yayınlandığı anın zaman damgasıyla* şirket gelirleri gerekir. Sinyal günü kapanışına dek yayımlanmış son yıllık raporda yıllık net satış büyümesi >%20 ise evrene girer; negatif veya eksik önceki yıl gelirinde sinyal yok. Sektör/“yeni teknoloji” öznel sınıflaması kullanılmaz. Üç yıllık >%20 büyüme filtresi yalnız ayrı duyarlılık kolu; kaynak bunu zorunlu demiyor. Bu veri yoksa **aday test edilmez**; bugünkü hisse listesini geriye taşımak veya BTC/ETH OHLCV'ye gelir vekili eklemek yasaktır.
- **Sinyal/icra:** En az 200 tamamlanmış D1 seans sonrası `SMA50[t-1]≤SMA200[t-1]`, `SMA50[t]>SMA200[t]`, `close[t]>SMA50[t]` ve bilinen gelir koşulu birlikte. Bir sonraki düzenli seansın uygulanabilir açılışında alış; açılış yoksa atla. Alıştan sonra `entry×0,85` sabit stop, `entry×4` limit hedef; ilk ters SMA kesişimi `SMA50[t]<SMA200[t]` kapanınca sonraki açılışta çık. Aynı seanstaki stop/hedef çakışmasında stop önce; gap açılışında gerçekleşebilir fiyat ve kayma kullan. Aynı hissede tek pozisyon; çıkıştan sonra yeni yukarı kesişim bekle.
- **Risk ve kıyas:** Pozisyon adedi `floor(0,005×equity/(entry-stop))`, ayrıca giriş tutarı en çok özsermayenin %10'u; bu iki sınır **bizim araştırma seçimimizdir**, kaynak s. 16–18'de örnek %1–2 hesap riski verir. Komisyon, spread, kayma, corporate action ve delist getirileri dahil. Aynı evren/dönemde gelir filtresiz SMA50/200 ve gelir filtresi olan fakat basit momentum kontrolüyle karşılaştır; işlem sayısı, net R, düşüş, maruziyet, sektörel kümelenme, veri eksikliği ve dönem dışı sonuçlar raporlansın. Kaynağın Apple/Cisco/Crocs örnekleri ileri performans kanıtı değildir. Bu aday **hisse verisi sağlanana dek kripto backtest/paper kuyruğuna girmez**.

## 3. Forex İçin Gelişmiş Teknik Analiz — Wayne Walker

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 16/Baskı 16/Forex İçin Gelişmiş Teknik Analiz - Wayne Walker (58 sayfa) - @eseckal.pdf>) · [tam metin](03_advanced_forex_walker.txt)

**Tarama:** s. 1–15 trend, destek/direnç ve hareketli ortalamalar; 16–18 MACD; 19–25 Fibonacci; 26–35 mum/grafik örüntüleri; 36–44 trend, sinyal ve zamanlama grafikleri; 45–51 piyasalar arası/temel bağlam; 52–58 psikoloji ve sonuç. S. 42–43 örneğinde W1 yükseliş bağlamı, D1 CCI'nin −100'ü yukarı kesmesi ve H1'in aynı yöndeki CCI sinyali var. Ancak W1 “yükseliş trendi”, H1'in “yaklaşık aynı zamanda” sinyal vermesi ve çıkış/stop sayısal değil. CCI −100 geri geçişi [138. partide](../batch_138/STRATEGIES.md), üst zaman dilimi rejimi ve alt zaman dilimi teyidi de mevcut aday ailelerinde bulunuyor. Bu kitap yeni olay sırası veya ölçülebilir eşik vermediği için **yeni bağımsız aday yok**; üçlü dilim teyidi mevcut CCI adayına ileride ablation olabilir.

**Parti sonucu:** 3 kitap, 175 sayfa, 1 yeni aday. Toplam **489 tamamlanmış ayrı kitap, 21.585 sayfa, 394 doğrulanmamış strateji adayı**.
