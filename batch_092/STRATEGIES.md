# Kitap okuma 092 — stop süpürmesi ve belirsiz çoklu gösterge sistemi

**Kapsam:** Önceden tamamlanmamış üç PDF'nin **14 + 26 + 46 = 86 sayfası** baştan sona okundu. Grafik ve kritik kural sayfalarından 13'ü [görsel kontrol edildi](figure_contacts/). Sayfalar PDF numarasıdır. **Yeni bağımsız, uygulanabilir strateji adayı yok.** Backtest, paper test ve emir yapılmadı.

## 1. Forex Trading İşlemlerinde Stop Avlama Stratejisi — David Odoh

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 17/Baskı 17/Forex Trading İşlemlerinde Stop Avlama Stratejisi - David Odoh (14 sayfa) - @eseckal.pdf>) · [Tam metin](01_stop_hunting.txt)

**Sayfa haritası:** s. 1–2 giriş/üç likidite türü; 3–6 üç kez dokunulan trend çizgisinin fitil aşımı; 6–10 destek/direnç ve eşit tepe/dip süpürmesi, sonradan yapı kırılımı; 11–14 H1 fitili içinde M15 arz bölgesi çizimleri. S. 4, 8, 10, 13 görsel denetlendi.

**Karar:** Kaynak s. 2 trend çizgisi, destek/direnç ve eşit tepe/dip çevresini “likidite” olarak adlandırır. S. 5–10 bu seviyelerin fitille aşılması ve geri dönüşü, sonra BOS anlatır. Bu çekirdek [017. partide](../batch_017/STRATEGIES.md) aralık sahte kırılımı, [040. partide](../batch_040/STRATEGIES.md) teyitli pivot süpürmesi, [070. partide](../batch_070/STRATEGIES.md) SFP ve diğer likidite süpürmesi adaylarıyla örtüşür. S. 11–13 H1 fitili/M15 emir bloğu retesti de önceki [049. parti](../batch_049/STRATEGIES.md) arz/talep ve [078. parti](../batch_078/STRATEGIES.md) tekrarıdır. Bu PDF sabit pivot algoritması, eşitlik toleransı, giriş/stop/çıkış/süre vermez. Yeni başlık açılmadı. Grafik OHLC'si emir defterindeki gerçek stop kümelerini veya kasıtlı kurumsal manipülasyonu kanıtlamaz.

**İleride karşılaştırma notu:** Var olan süpürme adaylarında “önceden teyitli çift tepe/dip” filtresi var/yok ve BOS teyidi var/yok ablation yapılabilir; eşitlik için ATR toleransı, pivotun sağdan teyidi, sinyalin kapanmış mumda oluşması ve ilk uygun M1 icrası önceden dondurulmalıdır. Bu not yeni bağımsız sinyal veya kaynak parametresi değildir.

## 2. Adım Adım Kazanan Trader için Forex İşlem Stratejileri — Donald Stanberry

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 15/Baskı 15/Adım Adım Kazanan Trader için Forex İşlem Stratejileri - Donald Stanberry (26 sayfa) - @eseckal.pdf>) · [Tam metin](02_step_by_step.txt)

**Sayfa haritası:** s. 1–5 önsöz/içindekiler; 6–8 Forex temel ve aracı seçimi; 9–11 robot tanıtımı; 12–16 çevrimiçi işlem ve eğitim kursu; 17–18 çizgi/çubuk/mum grafik tanımı; 19–20 ücretli sinyal hizmeti; 21–23 gün içi Forex'in genel özellikleri; 24–26 evden çalışma ve yazar. S. 15, 19 görsel denetlendi.

**Karar:** Başlık “stratejiler” dese de s. 14–16'da anılan yedi “Thinslice” kuralının hiçbiri kitapta açıklanmıyor; bir kursun vaadi olarak kalıyor. S. 17–18 OHLC ve grafik türleri, s. 19–20 sinyal hizmetleri, s. 21–23 piyasa türü ve risk anlatımı işlem eşiği, stop ve çıkış sırası sağlamıyor. Yeni aday yok. Satıcı yorumları, robot güveni ve kolay kazanç ifadeleri doğrulanmış işlem performansı değildir. S. 2 sağlık feragati ve s. 24 Forex'te hafta sonu işlem yapılabileceği ima edilen pasaj, metnin güvenilirliğini ayrıca zayıflatır.

## 3. Yeni Forex Piyasası Trading Sistemi — Emegha Emmanuel

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 15/Baskı 15/Yeni Forex Piyasası Trading Sistemi - Emegha Emmanuel (46 sayfa) - @eseckal.pdf>) · [Tam metin](03_new_forex_system.txt)

**Sayfa haritası:** s. 1–4 önsöz/platform; 5–12 fiyat-zaman-hacim ve çoklu zaman dilimi; 13–19 fiyat, hacim, göstergeler ve rejim; 20–23 “simülatör” bileşenleri; 24–26 MACD, stokastik, SMA, BB ve mum girişleri; 27–30 harmonik/Elliott/Fibonacci; 31–38 çoklu zaman dilimi ve genel giriş/çıkış; 39–43 özet ve örnek grafik; 44–46 ek/haber takvimi. S. 23–26, 38, 42–43 ve şekiller görsel denetlendi.

**Kaynak fikir:** S. 23–26'da BB alt/üst delişi, dönüş mumu, MACD ekstremum/sinyal kesişimi, stokastik 30/70 kesişimi ve SMA yönü; s. 31–32 D1/H4 üst bağlamı ve M5 girişini; s. 38, 42–43 bütün göstergelerin aynı yöne hizalanmasını önerir. Ancak MACD/sto/BB/SMA hesap periyotları, eşzamanlılık penceresi, çizilen destek/direncin teyidi, harmonik/Elliott pivotu, stop, hedef ve iptal koşulu yoktur. S. 38 long için düşen trend dibinde destek/Fibonacci; short için yükselen trend tepesinde direnç/Fibonacci gibi öznel seçime döner. Bu haliyle kapalı mumda tekrar üretilebilir bir emir sözleşmesi değildir. Mevcut MACD+stokastik+BB ve çoklu zaman dilimi adaylarıyla da örtüşür; yeni başlık açılmadı.

**Doğruluk notları:** S. 24 MACD histogramının sıfır altında olmasını yükseliş trendi olarak anlatır; aynı sayfadaki sıfır-altı kesişimden long ifadesi ve standart MACD işareti arasında uyumsuzluk vardır. S. 25 short SMA kesişimi sonrası yanlışlıkla “long pozisyon” der ve BB için “%0,2 standart sapma” yazar; açık varsayılan bant katsayısı değildir. S. 15–19 harmonik/Elliott/Fibonacci şekillerini piyasa **hacminin** doğrudan ölçüsü gibi sunar, fakat bu şekiller işlem miktarını ölçmez. S. 40 Forex için “haftada 7 gün” iddiası önceki seans tanımlarıyla tutarsızdır. S. 45–46 tarih/saatli ekonomik takvim ve faiz yönü anlatımı bugünkü işlem kuralı veya kripto takvimi olarak kullanılmaz.

**Araştırma sınırı:** Bu üç kitaptan mevcut strateji sayısını artırmak için parametresiz öneriler türetilmedi. Önceki adayların ileriki testlerinde kapalı D1/H4/H1/M15, sinyalden sonraki ilk M1 icrası, nokta-zaman evreni, maliyet/kayma/fonlama ve aynı M1'de stop önce sırası korunur. Bu partide yeni başlıksız kayıt, kitapların tamamlandığı anlamına gelir; kârlı bir sonuç bulunduğu anlamına gelmez.
