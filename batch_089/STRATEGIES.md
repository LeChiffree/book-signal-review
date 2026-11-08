# Kitap okuma 089 — başlangıç derlemeleri ve Forex işlem kuralları

**Kapsam:** Daha önce okunmamış üç PDF'nin **83 + 31 + 21 = 135 sayfası** baştan sona okundu. Önemli kural sayfaları [görsel olarak incelendi](figure_contacts/). Sayfa numaraları PDF sayfalarıdır. Bu partide **yeni bağımsız strateji adayı yok**; önceki adaylara uygulanabilecek risk denetimi notları var. Backtest, paper test ve emir yapılmadı.

## 1. Başlangıç Seviyesi Günlük Trading 2020 — George Livermore

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 12/Baskı 12/Başlangıç Seviyesi Günlük Trading 2020 - George Livermore (83 sayfa) - @eseckal.pdf>) · [Tam metin](01_day_trading_2020.txt)

**Sayfa haritası:** s. 1–21 günlük işlem, platformlar ve maliyet; 22–32 opsiyonların genel tanıtımı; 33–46 giriş/çıkış, breakout, pivot, 20/60/100 MA; 47–58 disiplin ve risk; 59–70 gösterge sözlüğü; 71–83 yaygın hatalar ve sonuç. S. 35, 40, 43, 45, 57 görsel denetlendi.

**Tekrar kararı:** S. 45'te hızlı MA20'nin yavaş MA60'ı kesmesi ve fiyatın MA100 tarafında kalması, [006. partide](../batch_006/STRATEGIES.md) kaydedilmiş 20/60/100 strateji ailesinin aynısı. S. 40–42 hacimli destek/direnç kırılımı ve momentum, önceki breakout/volume adaylarını tekrarlıyor. S. 35'te iki dakikalık üçgenin ilk iki saat içinde kırılması örneği, mevcut günlük karar sözleşmesinde önceden seçilmiş D1 sinyali olmadan yürütülemez; sınır/pivot teyidi de belirtilmiyor. S. 43 merkezi pivot formülünde `/3` düşmüş; bu metni kod için güvenilir formül kaynağı saymıyoruz. S. 22–32 opsiyon işlemleri, OHLCV spot/perpetual test sözleşmesinde opsiyon primi, vade ve IV verisi olmadan değerlendirilemez.

**Araştırmaya katkı:** S. 33, 39, 44–46, 57–58 girişten önce stop, hedef, pozisyon büyüklüğü ve maliyet belirleme gerektiğini vurgular. Bu maddeler mevcut strateji sözleşmesinin doğrulama kontrolüdür; sinyal veya kanıtlanmış getiri sayılmaz. Kaynakta farklı bölüm ve piyasaların karıştığı, s. 43 pivot tanımının aritmetik eksik olduğu görüldüğünden örnek başarı iddialarına güvenilmez.

## 2. Yeni Başlayanlar İçin Basitleştirilmiş Forex Trading — Marlon Green

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 10/Baskı 10/Yeni Başlayanlar İçin Basitleştirilmiş Forex Trading - Marlon Green (31 sayfa) - @eseckal.pdf>) · [Tam metin](02_simple_forex.txt)

**Sayfa haritası:** s. 1–9 önsöz ve FX tanımı; 10–16 sistem/platform seçimi; 17–19 genel “strateji türleri”; 20–23 sinyal sağlayıcısı seçimi; 24–26 döviz çiftleri/analiz; 27–31 otomatik işlem yazılımı. S. 17–18 görsel denetlendi.

**Karar:** Kitap trend, hareketli ortalama kesişimi, destek/direnç ve grafik tanımadan söz eder (s. 12, 17–19, 24–25), fakat hiçbirinde hesaplanabilir giriş eşiği, dönem, stop ve çıkış sırası vermez. Dört “strateji” sınıfı (temel, basit, karmaşık, gelişmiş) işlem algoritması değil eğitim düzeyidir. Yeni strateji açılmadı. S. 21–22'deki sinyal hizmeti ücreti ve demo değerlendirme önerileri, üçüncü taraf performansının maliyet sonrası ve tarih damgalı doğrulanması için araştırma kontrolü olarak not edildi.

## 3. Forex Trading Kuralları — Lever70

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 10/Baskı 10/Forex Trading Kuralları - Lever70 (Forex Factory) (21 sayfa) - @eseckal.pdf>) · [Tam metin](03_forex_rules.txt)

**Sayfa haritası:** s. 1–4 amaç ve kural listesi; 5–11 günlük hedef/stop/pozisyon büyüklüğü; 12–15 sinyal uyumu, seans, likidite, haber; 16–19 broker, kaldıraç, kayıp serisi ve rejim; 20–21 okuma listesi. S. 5, 9, 11–12, 17 görsel denetlendi.

**Uygulanabilir risk deneyi, yeni sinyal değil:** Kaynak s. 17, iki ardışık kayıptan sonra işlem yapmayı bırakmayı önerir. Mevcut backtest adaylarının üstünde ayrı portföy/risk kolu olarak ön kayıt yapılabilir: UTC gününde iki **gerçekleşmiş net** kayıp arka arkaya görülünce o günün kalan yeni girişlerini kapat; açık pozisyonların stop/hedef yönetimini sürdür; sonraki UTC gününde sayaç sıfırlansın. Kâr veya sıfır net sonuç seriyi sıfırlar. Bu sıfırlama ve gün sınırı **bizim** kesinleştirmemiz; kaynak mola süresi vermez. Ana strateji sinyallerini değiştirmeden, yalnız reddedilen sinyal sayısı, işlem sayısı, net getiri, azami düşüş ve maliyeti ölç. S. 18 rejim sınıflama önerisi önceki adayların trend/yatay filtreleriyle örtüşür.

**Riskli iddialar:** S. 5 “her günü kârla bitir” işlem sonucu olarak garanti edilemez; s. 9'daki her gün 5 pip kazanarak bileşik büyüme hesabı kayıp günlerini ve işlem maliyetlerini dışlar, ampirik beklenti değildir. S. 5–6 ve 9'da %5 işlem riski önerisi mevcut proje risk sınırını yükseltmek için gerekçe sayılmaz. S. 11'de broker stopunu gerçek çıkış noktasından 20 pip uzağa bırakma önerisi öngörülen maksimum kaybı bozabilir; kabul edilmez. FX seans/pip/haber kuralları (s. 13–16) 24/7 kripto piyasasına saat ve ölçek değişmeden taşınmaz. Bunların hiçbiri yeni bağımsız giriş stratejisi sayılmadı.
