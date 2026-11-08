# Kitap okuma 195 — açılış aralığı, VSA ve piyasalar arası tahmin

Üç farklı PDF'nin **523 sayfası** sayfa bazında metne çıkarılıp baştan sona tarandı; giriş/çıkış kısımları ayrıca okundu. **Yeni bağımsız, nesnel kapalı mum işlem stratejisi adayı: 0.** Backtest, paper test ve emir yapılmadı. Sayfalar PDF sayfasıdır.

## 1. Michael Parness — Trend Ticareti Sanatı (230 sayfa)

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Trend Ticareti Sanatı - Michael Parness (230 sayfa) - @eseckal.pdf>) · [tam metin](01_trend_parness.txt)

**Tam okuma:** S. 1–14 yaklaşım ve risk; 15–30 kırılım ve 09:30–10:00 aralığı; 31–89 zaman dilimi, güçlü hisseler ve opsiyonlar; 90–134 açılış boşluğu ve 10:00 kuralı; 135–171 teknik gap giriş/çıkışları; 172–219 haber ve trend; 220–230 psikoloji ve son. S. 16–18 ve 129: New York 09:30–10:00 yüksek/düşük sınırının 10:00 sonrası aşılması, **açılış aralığı kırılımı**dır. S. 18'de aralık genişliği ilk hedef ve yaklaşık 1:1 risk/ödül örneğidir; önceki [açılış aralığı adayları](../batch_060/STRATEGIES.md) ile aynı aile. S. 90–105 büyük açılış boşluğunu ters yönde oynama; s. 137–149 ilk M5 çubuğu/çekiçle giriş, daha önceki [gap + ilk mum adayı](../batch_098/STRATEGIES.md) ile örtüşür. Kitapta “büyük” gap ve haber kalitesine sabit eşik yoktur; seçilmiş grafiklerden sonuç genellenmez. **Yeni aday: 0.**

**İlerideki test notu:** Önceki ORB testinde Parness varyantı ancak ayrı bir ablation kolu olabilir: 09:30–10:00 `America/New_York` RTH aralığı, 10:00 sonrasındaki ilk **kapanmış** M5 sınır geçişi, sonraki uygulanabilir M1 açılışı; stop karşı aralık ucu ve ilk hedef aralık genişliği. Buradaki M5 kapanış teyidi bizim gecikmeli uygulama seçimimizdir; kaynak intrabar geçişi de işlemeyi anlatır. Aynı günkü gerçek gap var/yok alt grupları, tarihi spread ve işlem maliyetiyle ayrı raporlanmalı. 24/7 kripto UTC gün sınırı bu seansın eşdeğeri değildir.

## 2. Gavin Holmes — Smart Money Gölgesinde Trading (189 sayfa)

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 10/Baskı 10/Smart Money Gölgesinde Trading - Gavin Holmes (189 sayfa) - @eseckal.pdf>) · [tam metin](02_smart_money_holmes.txt)

**Tam okuma:** S. 1–54 VSA arka planı ve örnekler; 55–90 hacim-yayılım/zayıflık; 91–119 sarsıntı, düşük hacimli test ve güç; 120–149 işlem planı ve psikoloji; 150–189 söyleşi ve son. S. 79–80'de arka planda zayıflık ardından düşük hacimli “Talep Yok” barı, s. 93–97'de düşük hacimli dar düşüş barı ve sonraki yükseliş teyidi, mevcut [VSA düşük hacimli teyit adayı](../batch_102/STRATEGIES.md) ile aynı olay ailesidir. S. 90'daki 500 barlık yeni dip ve s. 96'daki yaklaşık 50 bar arka plan okuması öznel “akıllı para” yorumu için bağlamdır; tek başına yeni giriş/çıkış makinesi değildir. S. 110 üç zaman diliminde trend ve düşük hacimli test ister, fakat “belirgin güç”ün sayısal eşiği yoktur. OHLCV kurum kimliğini veya manipülasyon niyetini kanıtlamaz. **Yeni aday: 0.**

**İlerideki test notu:** [LK102](../batch_102/STRATEGIES.md) üzerinde 500 tamamlanmış bar yeni düşük/yüksek ve 50 bar arka planı, veri yetiyorsa önceden kaydedilmiş filtre kolları olarak denenebilir. Yeni filtreler seçim sonrası kazanan grafiklerden ayarlanmaz; forex tick volume ile borsa işlem hacmi karıştırılmaz.

## 3. Louis B. Mendelsohn — Teknik Analiz ile Trendi Tahmin Etmek (104 sayfa)

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 10/Baskı 10/Teknik Analiz ile Trendi Tahmin Etmek - Louis B. Mendelsohn (104 sayfa) - @eseckal.pdf>) · [tam metin](03_trend_mendelsohn.txt)

**Tam okuma:** S. 1–44 piyasa bağlantıları; 45–58 MA gecikmesi ve tahmin yaklaşımı; 59–79 VantagePoint tahminleri ve gösterge örnekleri; 80–89 sinir ağları; 90–104 ekler/son. S. 56–57 ilgili piyasa girdilerini, s. 59–75 tahmini MA/tepe/dip ve Neural Index sinyallerini tanıtır. Tahminleri üreten modelin tam özellikleri, eğitim verisi, ağırlıkları ve tarihsel **o gün üretilmiş** tahmin serisi verilmez; bugünden geçmişe yeniden üretilen tahminler ileriye bakış riski taşır. S. 63'te tahmini MA ile gerçek MA kesişimi, tahmini seri olmadan yalnız geçmiş mumlardan hesaplanamaz. S. 61'deki doğruluk yüzdeleri bağımsız test kanıtı değildir. S. 85 aşırı eğitime karşı bağımsız test gereğini açıklar. Mevcut kapalı mum sözleşmesine uygulanabilir yeni sinyal yoktur. **Yeni aday: 0.**

**Parti sonucu:** 3 PDF, **523 sayfa**, **0 yeni aday**. Kümülatif **585 PDF, 34.731 sayfa, 434 doğrulanmamış aday**.
