# Kitap okuma 132 — üç kitap, bir portföy adayı

**Kapsam:** Üç ayrı PDF'nin **13 + 44 + 41 = 98 sayfası** baştan sona incelendi. İlk PDF'nin metin katmanı boş olduğundan 13 sayfasının tamamı görsel okundu. İlk seçilen *VWAP Trading Stratejisiyle Kolay Para* kitabı, [43. partideki kitabın](../batch_043/STRATEGIES.md) farklı baskısı olduğu için kitap sayılmadı; yerine *Trading Uzmanlığı* seçildi. Backtest, paper test ve emir yapılmadı. Sayfalar PDF sayfasıdır.

## 1. Trading Uzmanlığı — Million Moves Presents

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 25/Baskı 25/Trading Uzmanlığı - Million Moves Presents (13 sayfa) - @eseckal.pdf>) · [Sayfa dökümü](01_trading_mastery.txt) · [Görsel s. 1–9](trading_contact_1.png) · [Görsel s. 10–13](trading_contact_2.png)

**Tam okuma:** S. 1 kapak; s. 2 formülü açıklanmayan ücretli gösterge tanıtımı; s. 3–4 mum ve dönüş şekilleri; s. 5 seviye retesti, mum teyidi; s. 6 osilatör uyumsuzluğu; s. 7 arz/talep; s. 8–9 kırılım ve retest formasyon çizelgesi; s. 10 Fibonacci düzeltme; s. 11 piyasa evreleri ve 200 MA; s. 12 risk/ödül tablosu; s. 13 korelasyon örnekleri. Bunların çoğu mevcut mum, destek/direnç, Fibonacci, formasyon ve uyumsuzluk adaylarıyla örtüşür. Özel göstergenin kodu/kuralı, osilatörün türü ve objektif seviye çizimi yok. Forex çiftleri arasındaki korelasyonlar zaman içinde sabit bir al/sat kuralı değildir. **Yeni aday yok.**

## 2. M ve W Nihai Gün İçi Trading Stratejisi — James Jecool King

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 25/Baskı 25/M ve W Nihai Gün İçi Trading Stratejisi - James Jecool King (44 sayfa) - @eseckal.pdf>) · [Tam metin](02_mw_king.txt)

**Tam okuma:** S. 1–12 M/W'nin iki ayağı, ikinci tepe daha düşük veya ikinci dip daha yüksek ve boyun çizgisi kırılımı; s. 13–24 destek/direnç, fitil, en az mumun üçte ikisi kuyruk olan pin bar ve M15 örnekleri; s. 25–31 bayrak kırılımı; s. 32–36 flama kapanış kırılımı, karşı çizgi stopu ve direk boyu hedefi; s. 37–39 kama; s. 40–44 pozisyon ve risk açıklamaları. İkinci ayakta giriş (s. 11–12, 14) ile ancak boyun çizgisi tamamlandıktan sonra giriş (s. 18) **ayrı zamanlı** kurallardır; bu seçimi tek işlem gibi geriye dönük birleştirmemek gerekir. M/W ve bayrak/flama/kama çekirdeği önceki [çift tepe/dip](../batch_045/STRATEGIES.md) ve [grafik formasyonu](../batch_003/STRATEGIES.md) adaylarıyla örtüşür. İkinci ayağın alçak/yüksek seçimi teyitli pivotların sağ barları tamamlanmadan bilinmez; kaynak pivot genişliği, bölge toleransı, çizgi çizimi ve stop tamponunu sabitlemez. “Her zaman aynı lot” ile sabit yüzde risk ifadeleri birbiriyle çelişir; bunlar test için risk ölçütü alınmaz. **Yeni bağımsız aday yok.**

## 3. Ayarla ve Unut — Tim Morris

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 25/Baskı 25/Ayarla ve Unut - Yıllık Ortalama _11_in Üzerinde Getiri Sağlayan Düşük Riskli Bir ETF Yatırım Stratejisi - Tim Morris (41 sayfa) - @eseckal.pdf>) · [Tam metin](03_set_forget_morris.txt)

**Tam okuma:** S. 1–10 giriş, varlık ve performans tanımları; s. 11–20 reklam, hisse, uzun vadeli tahvil ve altın hissesi gerekçesi; s. 21–25 portföy ağırlıkları; s. 26–28 faiz riskleri; s. 29–30 çeyreklik yeniden dengeleme ve temettü; s. 31–41 sonuç ve başka kitap reklamları. Kaynak geçmiş simülasyonda **VFINX/VUSTX/RGLD** kullanır (s. 14, 17, 19–23), bugünkü uygulama için **VOO/VGLT/RGLD/FNV** önerir (s. 23–25). İki evrenin geçmiş performansı aynı sayı değildir. S. 5'te önceki baskıda temettülerin iki kez sayıldığı hatası itiraf edilir. 1990–2020 için verilen %11,56 CAGR, −%12,89 maksimum düşüş ve −%4,03 en kötü yıl, yazarın seçilmiş dönem ve vekil fon iddialarıdır; yeni ETF sepetinin teyitli sonucu değildir. RGLD için kitabın verdiği −%98,04 düşüş (s. 20) “düşük risk” başlığıyla karıştırılmamalıdır. Faiz yükselişi uzun vadeli tahvil fonunu ciddi etkileyebilir (s. 26–28). Temettü getirisi garanti değildir.

### TM132A — 60/35/2,5/2,5 çeyreklik sabit ağırlık portföyü

- **Kaynak (PDF s. 22–25, 29–30):** VGLT `%60`, VOO `%35`, RGLD `%2,5`, FNV `%2,5`; Ocak, Nisan, Temmuz, Ekim başında hedef ağırlıklara dön. Dağıtımları yeniden yatır. Bu kısa vadeli işlem sinyali değil, sistematik **varlık dağılımı stratejisidir**; ayrı araştırma sınıfında tutulur.
- **Nedensel sözleşme:** Dört varlığın da gerçekten işlem gördüğü ilk ortak tarihten itibaren günlük toplam getiri verisini kullan. Her çeyreğin ilk ABD işlem gününde, önceki kapanışta bilinen portföy değeriyle hedef dolar ağırlıklarını hesapla; emirleri ilk uygulanabilir açılış kotasyonundan icra et. İcra fiyatı farklıysa gerçekleşen ağırlıkları kaydet; önceki çeyreği hedef ağırlığa geriye dönük sabitleme. Temettü/dağıtımların ex-date ve pay date farkı gerçek nakit akışıyla; bölünmeler, kapanışlar ve gider oranları fiyat serisinde doğru işlenir. Aradaki günlerde yalnız dağıtım nedeniyle nakit oluşursa sonraki çeyrek yeniden dengelemesine kadar nakitte tut; otomatik DRIP ayrı karşılaştırma kolu. Tüm seriler USD, sağkalım yanlılığı olmadan ve varlığın kote olduğu tarihten önce sentetik getiri eklenmeden.
- **Risk ve karşılaştırma:** Kaldıraç/short yok; toplam ağırlık `%100`; komisyon, alış-satış farkı, kayma, vergi varsayımı ve nakit faizi ayrı açıkla. Ana karşılaştırmalar aynı canlı evrende VOO al-tut, VOO/VGLT `60/40`, aynı dört varlıkla `55/40/2,5/2,5`, yeniden dengelemesiz al-tut ve yıllık dengeleme. CAGR, yıl bazlı getiriler, maksimum düşüş, en kötü ay/yıl, oynaklık, Sortino, faiz şoku dönemleri ve hisse/tahvil korelasyonunun birlikte yükseldiği dönemler raporlanır. VFINX/VUSTX/RGLD ile 1990–2020 vekil replikası istenirse **ayrı** deneydir; FNV/ETF tarihçesini taklit etmez. Hedef ağırlıklar kitabın in-sample seçimi olduğundan sonuç dış örneklem ve değişik başlangıç tarihleriyle sınanmalı.

## Sonuç

**1 yeni aday:** TM132A, varlık dağılımı sınıfında. İşlem formasyonu/indikatör sınıfına yeni aday eklenmedi.
