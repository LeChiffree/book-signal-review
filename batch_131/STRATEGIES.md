# Kitap okuma 131 — getiri eğrisi ve ölüm kesişimi

**Kapsam:** Üç ayrı PDF'nin **25 + 25 + 28 = 78 PDF sayfası** okundu. Sayfa numaraları PDF sayfasıdır. Grafik ağırlıklı ilk kitabın bütün sayfaları ayrıca görsel incelendi. Bunlar araştırma adaylarıdır; backtest veya paper test henüz yapılmadı.

## 1. Takas Edilebilir Order Blocklar

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 6/Baskı 6/Takas Edilebilir Order Blocklar (25 sayfa) - @eseckal.pdf>) · [Tam metin](01_tradable_order_blocks.txt) · [Görsel s. 1–9](ob_contact_1.png) · [Görsel s. 10–18](ob_contact_2.png) · [Görsel s. 19–25](ob_contact_3.png)

**Tam okuma:** S. 1–4 OB, dengesizlik, yapı kırılması, SSR/flip alanı ve sekiz nitelik; s. 5–20 çizilmiş destek/direnç, yapı kırılması, 2× itki, karşı bloğun aşılması ve SSR örnekleri; s. 21 zaman dilimi tablosu; s. 22–25 2× itki ve 3R örnekleri. Kitap OB sonrası dengesizliğin en az **blok genişliğinin 2 katı**, hedefe açık alanın en az **3R** olmasını önerir (s. 4, 12, 22–25). Bunlar [mevcut OB/BOS ilk retest](../batch_058/STRATEGIES.md) adayına önceden belirlenmiş **filtre kolu** olarak eklenebilir: yalnız kırılım mumu kapandığında bilinen fiyatlarla blok yüksekliği, itki ve o anda görülen karşı bölge mesafesi ölçülür; ilk retestten önce yeniden çizim yapılmaz. Kitap “iki onay seçin” der; tüm sekiz niteliği zorunlu saymak kaynak kuralı değildir. OB seçimi, SSR ve “karşı bloğun çıkarılması” tam mekanik tanımlanmadığından bağımsız strateji sayılmadı. Görseldeki seçilmiş başarılı örnekler başarı oranı kanıtı değildir.

## 2. Wyckoff Eğitimi — Rise Precision

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 7/Baskı 7/Wyckoff Eğitimi - Rise Precision (25 sayfa) - @eseckal.pdf>) · [Tam metin](02_wyckoff_rise_precision.txt)

**Tam okuma:** S. 1–7 tarihçe, beş adım ve üç yasa; s. 8–13 birikim, spring, SOS ve LPS; s. 14–18 dağıtım, UTAD, SOW ve LPSY; s. 19–25 yeniden birikim ve evre kontrol çizelgeleri. Kaynak, spring dönüşünden sonra **daha düşük hacimli test** ve SOS ardından **azalan hacimli geri çekilme** önerir (s. 9, 12–13, 22); dağıtımda bunun tersini anlatır (s. 15, 17–18, 25). Bu olaylar [önceki Wyckoff](../batch_075/STRATEGIES.md), [spring/SFP](../batch_117/STRATEGIES.md) ve hacim testleriyle örtüşür. Sayfalardaki “faz C/D” etiketi tamamlanmış geleceği görmeden kesinleştirilemez; belirli bir geçmiş pencerede seviye, test süresi ve hacim eşiği tanımlanmamıştır. Bunları ayrı aday diye yeniden saymadık. P&F yatay sayımı için kutu ve dönüş ayarları da verilmedi.

## 3. Çökme Sinyali — Tim Morris

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 25/Baskı 25/Çökme Sinyali - Borsa Çöküşünü Öngören Tek Sinyal - Tim Morris (28 sayfa) - @eseckal.pdf>) · [Tam metin](03_morris_crash_signal.txt)

**Tam okuma:** S. 1–9 kapak, risk ve tarihsel çöküş örnekleri; s. 10–19 ABD 10 yıl eksi 2 yıl Hazine getiri farkının negatife dönüşü ve örnek tarihleri; s. 20–22 inversiyonda nakde geçiş, ardından SPY günlük SMA50'nin SMA200 altına kesilmesiyle RWM/TZA üzerinden kısa taraf; s. 23–24 SMA50'nin yeniden SMA200 üstüne kesilmesiyle SPY'ye geri dönüş; s. 25–28 platform tanıtımı ve kapanış. Kitabın “yanlış sinyal yok”, 6 ay–2 yıl içinde çöküş ve kesişimle hareketin neredeyse tamamının alınacağı iddiaları seçilmiş tarihsel örneklere dayanır; güvenilir performans kanıtı değildir. ABD resesyonu ile borsa çöküşü aynı olay değildir. Kaldıraçlı TZA'nın günlük yeniden dengelemesi uzun tutuşta endeksin basit 3× ters getirisi olamaz; ana aday yalnız kaldıraçsız karşılaştırmadır.

### TM131A — 10Y–2Y inversiyonu sonrası SPY ölüm kesişimiyle risk rejimi

- **Kaynak (PDF s. 10–13, 19–24):** 10Y−2Y getiri farkı sıfırın altına düşünce uzun piyasa maruziyetini kapat; açığa satış için ayrıca günlük SPY SMA50'nin SMA200 altına kesilmesini bekle; altın kesişimde yeniden uzun ol. İnversiyon anında hemen short açmak kitabın önerisi değildir.
- **Nedensel deney sözleşmesi:** ABD Hazine 2Y/10Y günlük resmi gözlemi yayımlandığı **gerçek saatten sonra** kullanılabilir; gecikme belirsizse bir sonraki ABD işlem gününden itibaren geçerli say. `spread = 10Y−2Y`; önceki yayımlanmış gözlem `>=0`, yeni gözlem `<0` ise alarmı etkinleştir. SPY SMA'ları sadece tam kapanmış günlük barlarla hesapla. Alarmda SPY uzununu sonraki işlem seansında kapatıp nakde geç; alarm açıkken SMA50 `>=` SMA200 durumundan `<` durumuna ilk geçişte sonraki seans açılışında SPY short veya kaldıraçsız RWM long kolunu başlat. SMA50 yeniden `>` SMA200 kesince short/RWM'yi kapatıp sonraki seans SPY long'a dön ve alarmı sıfırla. Önceden aktif ölüm kesişimi varsa inversiyon sonrasında yeni bir kesişim bekle; bu seçimin etkisini ayrı duyarlılık kolunda ölç. Kesişimden önce ters ETF alınmaz. Başlangıçta SPY long; ilk 200 kapanış tamamlanana kadar kesişim yok.
- **Risk ve karşılaştırma:** Ana uygulamada SPY long ↔ nakit ↔ RWM long, aynı anda tek pozisyon; SPY short ve kaldıraçsız Russell 2000 ters ETF farklı dayanak riskleri taşıdığından ayrı kollar. Açılış boşlukları, fon gideri, dağıtımlar, borç alma maliyeti (doğrudan short kolu), alış-satış farkı ve temettü dahil toplam getiri kullanılmalı. İnversiyonun tek başına nakit filtresi, yalnız SMA50/200 kesişimi, SPY al-tut ve eşit riskli koruma koluyla aynı dönem karşılaştır. Önceden tanımlı ana ölçü maliyet sonrası toplam getiri, maksimum düşüş ve kaçırılan boğa piyasası getirisi; çöküş olaylarının sayısı az olduğu için rejim bazında belirsizlik ayrıca raporlanır. Kaynaktaki “6 ay–2 yıl” bir işlem çıkış saati olarak kullanılmaz.

## Sonuç

**1 yeni araştırma adayı:** TM131A. OB'nin 2×/3R niteliği mevcut OB adayına filtre olarak; Wyckoff olayları mevcut adaylarla örtüşen tekrarlar olarak kaydedildi.
