# Kitap okuma 115 — Fibonacci, order block ve mum dönüşleri

**Kapsam:** Üç ayrı PDF'nin **21 + 20 + 21 = 62 sayfası** baştan sona okundu. Atıflar PDF sayfasıdır. Bu partide yeni bağımsız aday yok; backtest, paper test ve emir yapılmadı.

## 1. Fibonacci Trading Hakkında Her Şey — Bill Poulos

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 8/Baskı 8/Fibonacci Trading Hakkında Her Şey - Bill Poulos (21 sayfa) - @eseckal.pdf>) · [Tam metin](01_fibonacci_poulos.txt)

**Tam okuma:** S. 1–2 giriş ve Fibonacci oranları; s. 3–4 %23,6/%38,2/%50/%61,8/%76,4 geri çekilme, uzatma düzeyleri ve pivotun iki sol/iki sağ düşük-yüksek barla tanımı; s. 5–12 geçmişe dönük geri çekilme örnekleri, başarısız örnek ve hangi seviyenin tutacağının bilinmemesi; s. 13–20 üç pivotla uzatma hedefleri, erken/geç hedef seçimi; s. 21 Fibonacci'nin tek başına giriş veya çıkış için yeterli olmadığı uyarısı. Kaynak özellikle iki seçim sorununu kabul eder: hangi salınım başlangıcı ve hangi geri çekilme/uzatma düzeyi. S. 3–4'teki 2+2 pivot teyidi mevcut sözleşmelerin veri sızıntısız pivot üretimine ek kaynak desteğidir; [110. partideki kademeli Fibonacci](../batch_110/STRATEGIES.md) ve diğer Fibonacci adaylarından ayrışan tekil emir, stop ve yönetim kuralı vermediği için **yeni aday yok**. S. 2'de Fibonacci'nin dönemine ilişkin çeviri/tarih hatası strateji kanıtı değildir.

## 2. BTMM + ICT Sniper Giriş — Omoemu Festus

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 7/Baskı 7/BTMM + ICT Sniper Giriş - Omoemu Festus (20 sayfa) - @eseckal.pdf>) · [Tam metin](02_btmm_festus.txt)

**Tam okuma:** S. 1–3 risk ve “piyasa yapıcı” anlatısı; s. 4–5 önceki gün/hafta/ay yüksek-düşük çevresinde M15 M/W dönüşü, H4 bağlamı, TDI ve EMA listesi; s. 6–8 zirveye doğru itiş öncesindeki son mumun “order block” sayılması ve bu mumun sonradan kırılıp kapanması, opsiyonel retest; s. 9–12 işaretli grafikler; s. 13–19 M15/H4 teyit listeleri, çeyrek noktaları ve TDI uyumsuzluğu; s. 20 sonuç. Kaynak birbiriyle zorunlu/alternatif teyitleri ayırmıyor, TDI formülü ve eşikleri, M/W pivot teyidi, çeyrek nokta ölçeği, emir ömrü, stop ve hedef vermiyor. “Son itişten önceki son mum” geriye dönük seçilirse lookahead doğurur. Kırılan blok/retest ve önceki gün düzeyi etrafındaki dönüş [5. partideki order block](../batch_005/STRATEGIES.md), sonraki arz-talep ve SFP adaylarına denk düşer. Bu metinden keyfi göstergeler ekleyerek yeni mekanik strateji türetmedik. **Yeni aday yok.** S. 3–4'teki kurumsal niyet ve stop kümeleri yalnız fiyat mumundan kanıtlanmaz.

## 3. Swing Trading — Cafe Du Forex

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 21/Baskı 21/Swing Trading - Cafe Du Forex (21 sayfa) - @eseckal.pdf>) · [Tam metin](03_swing_cafe_du_forex.txt)

**Tam okuma:** Dosya adı “Swing Trading” olsa da içerik Fransızca kaynaktan çevrilmiş **Japon mumları** rehberidir. S. 1–5 kapak/içindekiler, OHLC ve fitiller; s. 6–12 delici çizgi, yutan mum, harami/harami çaprazı, sabah yıldızı ve iki boşluklu terk edilmiş bebek; s. 13–19 kara bulut, ayı yutma/harami, akşam yıldızı, terk edilmiş bebek, küçük gövdeli tepe ve seçilmiş hisse örnekleri; s. 20–21 kurum tanıtımı/telif. Kaynakta s. 8'de boğa yutan ilk mumun rengini açıklayan satır grafikle/sonraki cümleyle tutarsızdır; formasyonun kesin tanımı için yalnız bu çeviriye dayanılmamalı. Mum aileleri [26. partideki mum kataloğu](../batch_026/STRATEGIES.md) ve diğer teyitli dönüş adaylarında var. Terk edilmiş bebek **gerçek seans boşluğu** gerektirir; kesintisiz kripto mumlarında boşluk şartı kaldırılıp aynı aday diye sayılamaz. “Ağır zirveler” için dışbükey küçük gövdeler ve gap yönü anlatılır ancak bar sayısı, eğrilik eşiği, stop ve hedef yok. Seçilmiş hisse örnekleri genel kazanma oranını kanıtlamaz. **Yeni aday yok.**

## Sonuç

**0 yeni aday.** Üç kitap mevcut kayıtların kapsamını ve sınırlamalarını açıklayan kaynaklar olarak işlendi.
