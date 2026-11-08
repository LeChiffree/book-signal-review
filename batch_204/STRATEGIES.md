# Kitap okuma 204 — SRDC, Minervini VCP ve Phantom

Üç daha önce tamamlanmamış PDF'nin **551 sayfası** sayfa bazında metne çıkarılıp tarandı; işlem kuralı geçen sayfalar ayrıntılı incelendi. **Yeni, henüz doğrulanmamış strateji adayı: 1.** Backtest, paper test veya emir yapılmadı. Aşağıdaki sayılar PDF sayfasıdır.

## 1. OrangeRoshan — SRDC 1 (124 sayfa)

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 10/Baskı 10/OrangeRoshan Paylaşımları - SRDC 1 - MatiasFX - Türkçe ve İngilizce (124 sayfa) - @eseckal.pdf>) · [tam metin](01_orange_roshan_srdc.txt)

**Tarama:** S. 1–62 Türkçe forum derlemesi, s. 63–124 aynı mesajların İngilizce aslı. Çekirdek bir önceki günün high/low sınırına iki yönlü emir, küçük pip hedefi ve sonradan eklenmiş M15 teyidi (s. 10–12, 119–123). Gelişmiş kuralda sınırı delen M15 mumunun kapanması, sonraki M15 mumunun bütünüyle sınır dışında oluşması ve ancak sonraki açılışta giriş istenir (s. 121, 123). Bu, [önceki gün uç kırılımı](../batch_029/STRATEGIES.md) adayına iki mum teyidi ve gecikme filtresidir; aynı seviye ve yön olayı için yeni bağımsız aday sayılmadı. Metinde stop yok/çok uzak stop (s. 12), 25 pip stop (s. 119) ve GBPUSD/EURUSD için 50 pip stop (s. 120) çelişir. 5 pip hedefin spread sonrası sonuç verdiği iddiası geçerli performans kanıtı değildir. M15 teyidi, mevcut ailenin maliyetli deneyinde önceden dondurulmuş varyant olarak karşılaştırılabilir. **Yeni aday: 0.**

## 2. Mark Minervini — Borsa Sihirbazı Gibi Trade Yapın (317 sayfa)

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 11/Baskı 11/Borsa Sihirbazı Gibi Trade Yapın - Mark Minervini (317 sayfa) - @eseckal.pdf>) · [tam metin](02_minervini_stock_wizard.txt)

**Tarama:** S. 1–68 yaklaşım, hisse seçimi ve risk; s. 69–90 piyasa aşamaları; s. 91–199 temel/teknik seçimi ve giriş hazırlığı; s. 200–231 VCP, hacim ve pivot; s. 232–317 çıkış, risk, örnekler ve ekler. Aşama 2 için fiyatın SMA150 ve SMA200 üstünde, SMA150'nin SMA200 üstünde ve SMA200'ün yükseliyor olması açıkça verilir (s. 74–75). VCP'de tipik olarak 2–4 ardışık düzeltmenin yaklaşık yarıya inen derinlikleri (s. 200–203), tabanın sonunda çok düşük hacim ve pivot kırılımında genişleyen hacim (s. 204–205, 225–226, 231) anlatılır. Kaynak, tek bir %10–15 yatay kutuyu gerçek ardışık daralmadan ayırır (s. 201–202, 231). Bu yüzden genel dar kutu/Donchian kırılımından farklı bir **sekans koşulu** test edilebilir. Grafik örnekleri seçilmiştir; anlatılan getiriler dış örneklem kanıtı değildir.

### MIN204A — Teyitli ardışık daralma ve hacim kuruması sonrası pivot kırılımı

- **Evren/veri:** D1 düzeltilmiş OHLCV; tarihsel olarak işlem gören ve sonradan silinen hisseler dahil nokta zamanlı hisse evreni. Split/temettü düzeltmeleri, işlem durması ve delist tarihi işleme uygun biçimde saklanır. Yalnız D1 kapanışında bilinen veri; yürütme için sonraki seans açık/ilk M1, spread ve hacim gerekir.
- **Trend:** `C_t>SMA150_t>SMA200_t`, `SMA200_t>SMA200_(t−20)`, `C_t>SMA50_t`. İlk üç öğe kaynak s. 74–75; 20 günlük eğim penceresi ve SMA50 filtresi bizim ön kayıt parametremizdir.
- **Formasyon:** Son 20–100 tamamlanmış D1 barında dönüş noktaları, solda 2 ve sağda 2 tamamlanmış barı aşan high/low olarak **sağdaki ikinci bar kapandığında** teyit edilir. Alternatif teyitli tepe–dip dizisinde 2–4 düzeltme bulunmalı. Her düzeltme derinliği `d_i=(tepe_i−dip_i)/tepe_i`; `0.35≤d_(i+1)/d_i≤0.65`, ilk `d_1≤0.35`, son `d_last≤0.08`. Son dipten sonra teyitli son tepe/pivot olmalı; bütün pivotlar sinyalden önce teyitli kalmalı. Çakışan örüntülerde en yakın tarihli son pivot, eşitlikte kısa taban seçilir. 20–100 gün, fraktal genişliği ve yüzdelik bantlar kaynağın kesin kuralları değil, bizim sınanacak nesnelleştirmemizdir.
- **Hacim/tetik:** Son daralmanın hacim medyanı, ilk daralmanın hacim medyanının `≤0.7`si. İlk kez `C_t>son teyitli tepe` ve `V_t≥1.2×median(V_(t−50):V_(t−1))` olduğunda long sinyal. Son daralma dibi sinyal mumundan önce belirlenmiş olmalı. 0.7 ve 1.2 eşikleri bizimdir; kaynağın yönü son aşamada azalan, kırılımda artan hacimdir. İlk kırılım mumu dışında tekrar sinyal yok; yeni baz ancak mevcut sinyal kapanıp yeni dönüş dizisi oluşunca aranır.
- **Yürütme/risk/çıkış:** Sinyal kapanışından sonraki seans açılışında piyasa alış; açılış pivot üstünde en çok `%2` gap yapmışsa doldur, aksi halde pas. Stop `son daralma dibi−0.1×ATR14_t`; stop mesafesi girişin `%15`ini aşarsa pas. Sabit ilk sermaye riski `%0.25`, tek hisse `%10` özsermaye ve eşzamanlı toplam açık risk `%1` üst sınırı. Kâr hedefi `3R`; önce stop/3R, ayrıca `C<SMA50` kapanışını izleyen açılışta veya 40. seans açılışında çık. Gap, halt ve aynı dakika stop/hedef sırası yürütme verisiyle; belirsizlikte olumsuz dolum. Bunların tümü bizim test sözleşmemiz, kitabın sabit vaatleri değil.
- **Ayırıcı test:** Aynı evren/tarih/giriş/stop/çıkış ve maliyette son 20 gün high kırılımı, genel 10–15% kutu kırılımı, yalnız hacim filtresini kaldırma ve ardışık daralma koşulunu kaldırma kolları. Önceki kayıtlarla özellikle [genel daralma](../batch_130/STRATEGIES.md) ve [hacimli tepe kırılımı](../batch_039/STRATEGIES.md) karşılaştırılacak. Parametreler öğrenme döneminde sabitlenecek; tarihsel evren, endeks üyeliği, maliyet, delist, sinyal sayısı, dolmayan emir, net R, maksimum düşüş ve dönemlere ayrılmış dış örneklem raporlanacak. Tekil seçilmiş grafikler başarı sayılmaz.

## 3. Art Simpson — Phantom'un Hediyesi (110 sayfa)

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 10/Baskı 10/Phantom_un Hediyesi (110 sayfa) - @eseckal.pdf>) · [tam metin](03_phantom_gift.txt)

**Tarama:** S. 1–13 hazırlık ve işlem psikolojisi; 14–19 kural 1, pozisyonu doğru kabul etmeyip piyasanın kanıtlamasını isteme ve yanlışsa küçültme; 20–25 kural 2, yalnız kanıtlanmış kazanan pozisyona ekleme; 26–78 örnek ve uygulama tartışmaları; 79–110 sermaye koruma, rapor dönemleri ve sonuç. “Kanıt” için tekrarlanabilir fiyat eşiği, zaman penceresi ve başlangıç giriş sinyali verilmez (özellikle s. 16–18, 20–25). Bunlar mevcut giriş adaylarının pozisyon yönetimi için ayrı araştırma katmanı olabilir; keyfi bir kârlı pozisyona ekleme eşiği icat edilerek yeni giriş stratejisi sayılmadı. **Yeni aday: 0.**

**Parti sonucu:** 3 PDF, **551 sayfa**, **1 yeni doğrulanmamış aday**. Kümülatif **612 PDF, 41.358 sayfa, 441 doğrulanmamış aday**.
