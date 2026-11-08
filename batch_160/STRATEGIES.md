# Kitap okuma 160 — SMC, fiyat hareketi ve order block

Üç ayrı PDF'nin **16 + 20 + 25 = 61 sayfası** incelendi. Sayfa atıfları PDF sayfasıdır. **Yeni bağımsız strateji adayı: 0.** Backtest, paper test veya emir yapılmadı.

**Kopya kontrolü:** İlk seçilen Kartik K'nin 23 sayfalık VWAP/PVWAP PDF'si [43. partideki](../batch_043/STRATEGIES.md) kitabın aynı içerikli baskısıdır; üç ayrı kitap koşuluna dahil edilmedi. Yerine Morrison kitabı okundu.

## 1. Akıllı Para Konseptinde Ustalaşma — David E. Morrison

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 17/Baskı 17/Akıllı Para Konseptinde Ustalaşma - Forex Piyasasının Ayrıntılı Analizi - David E. Morrison (16 sayfa) - @eseckal.pdf>) · [tam metin](01_smart_money_morrison.txt)

**Tam tarama:** s. 1–4 SMC terimleri, CHOCH/BOS ve FVG; 5–7 piyasa yapısı/trend/yatay bölge; 8–9 emir akışı; 10–11 order block ve likidite; 12–14 piyasa likiditesi; 15–16 risk yönetimi.

**Karar:** s. 10 son ters mumdan OB ve dönüşte stopu OB dibi altına koyma fikri mevcut [OB/SMC adaylarıyla](../batch_005/STRATEGIES.md) örtüşür. s. 8–9 gerçek emir akışı için emir defteri/işlem akışı gerekir; kapalı OHLCV mumları bundan kurumsal emrin varlığını ispatlamaz. s. 11'de likidite toplama sonrasındaki yön tanımı da tek ve tutarlı tetik/çıkış sözleşmesi vermez. **Yeni aday yok.**

## 2. Price Action Kursu

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 6/Baskı 6/Price Action Kursu (20 sayfa) - @eseckal.pdf>) · [tam metin](02_price_action_course.txt)

**Tam tarama:** s. 1–4 fiyat hareketi ve risk; 5–8 piyasa/limit emirleri, daralma/genişleme; 9–13 yatay ve diyagonal seviyeler; 14–16 destekten sekme ve direnç kırılımı; 17–20 hacim ve çoklu zaman dilimi.

**Karar:** s. 15 destek yakınındaki daralma/uzun alt fitil ardından kapanışta long ve dip altı stop, önceki fitil/ret adayı ailesidir. s. 16 bölge dışına kapanışla kırılım, sınır veya sinyal mum dibi stopu, mevcut [kırılım ailesiyle](../batch_002/STRATEGIES.md) aynıdır. s. 17 yüksek hacim teyidi ve s. 18–19 üst zaman dilimi filtresi bu ailelerin ablation değişkenleri olarak değerlendirilebilir. DOM ekranındaki emirler (s. 5–8) geriye dönük OHLCV'de yoktur. **Yeni aday yok.**

## 3. Order Block — Mete Kaplan

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 6/Baskı 6/Order Block - Mete Kaplan (25 sayfa) - @eseckal.pdf>) · [tam metin](03_order_block_kaplan.txt)

**Tam tarama:** s. 1–6 son ters mum ve yapı kırılımı; 7–10 bölge çizimi ve rastgele engulfing elemesi; 11–18 kalite etkenleri (hızlı genişleme, yavaş geri geliş, önemli seviye, ilk test); 19–22 OB ortası, mum teyidi veya alt zaman dilimi MSB ile üç giriş türü; 23–25 kapanış ve uyarı.

**Karar:** s. 7 bölge çiziminde sabit kural olmadığını açıkça söyler; s. 16 ilk test ve s. 18 hızlı genişleme/yavaş dönüş, [mevcut OB ilk temas/mitigation ailesi](../batch_129/STRATEGIES.md) için filtre adaylarıdır. s. 20 OB gövde ortasından limit, mum dibi stop, 2–3R hedef; [önceki OB %50 uygulamalarıyla](../batch_054/STRATEGIES.md) örtüşür. s. 21 mum teyidi ve s. 22 alt zaman dilimi MSB de mevcut yapı kırılımı teyidinin varyantlarıdır. Nesnel sınama için pivotun sağ mumla kesinleşmesi, OB mumu, kırılım kapanışı, ilk geri test ve limit dolumu olay zamanında sabitlenmelidir; aksi halde geriye dönük seçilim olur. **Yeni bağımsız aday yok.**

**Parti sonucu:** 3 kitap, 61 sayfa, **0 yeni aday**. Birikmiş toplam **391 doğrulanmamış strateji adayı**.
