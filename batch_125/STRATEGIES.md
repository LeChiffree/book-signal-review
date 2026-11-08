# Kitap okuma 125 — çoklu zaman diliminde arz/talep dönüşü

**Kapsam:** Üç ayrı PDF'nin 21 + 21 + 22 = **64 PDF sayfası** baştan sona okundu. Sayfa numaraları PDF sayfasıdır. Bu dosya araştırma sözleşmesidir; backtest, paper test veya emir yapılmadı.

## 1. Trading Junkies — Mum Kalıpları

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 7/Baskı 7/Mum Kalıpları - Trading Junkies (21 sayfa) - @eseckal.pdf>) · [Tam metin](01_trading_junkies_candles.txt) · [Görsel sayfalar 1–12](candles_contact_1.png) · [Görsel sayfalar 13–21](candles_contact_2.png)

**Tam okuma:** S. 1 kapak; s. 2–3 marubozu; s. 4–5 dönen top/doji; s. 6–7 boğa/ayı yutma; s. 8–9 cımbız; s. 10–13 çekiç, asılı adam, ters çekiç, kayan yıldız; s. 14–19 sabah/akşam yıldızı, üç asker/karga, üç iç yukarı/aşağı; s. 20–21 harami. Metin katmanı çoğu sayfada yalnız başlığı taşıdığı için **21 sayfanın görseli de incelendi**. Kitap çizimlerle örnek veriyor; giriş, stop, çıkış, süre ve maliyet koşulu tanımlamıyor. Bütün formasyon aileleri önceki partilerde mevcut. Özellikle s. 3'te ayı marubozunun aynı anda “en yüksekten açılıp en yüksekten kapandığı” ve “en düşükten kapandığı” söylenmesi çeviri çelişkisidir; çizim ve OHLC tanımı esas alınmalı. **Yeni bağımsız aday yok.**

## 2. Johnathon — Swing Trading için Kesin Kılavuz

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 21/Baskı 21/Swing Trading için Kesin Kılavuz - Johnathon (21 sayfa) - @eseckal.pdf>) · [Tam metin](02_johnathon_swing.txt)

**Tam okuma:** S. 1–7 swing işlem ufku ve sabit parasal riskle farklı stop uzaklığına göre lot ayarı; s. 8–14 HH/HL trend, desteğe çekilme, iki bar dönüşü veya boğa yutma; s. 15–16 aralık üstünden sat/altından al ve ortadan kaçın; s. 17–20 günlük destek/direnç bağlamında H1 ayı yutma; s. 21 sonuç. D1 direnç + H1 yutma kurulumu önceki çoklu zaman dilimi destek/direnç adaylarıyla aynı ailede; bu kitap nesnel seviye genişliği, trend gücü ya da ek ayırt edici eşik vermiyor. “Yüksek olasılıklı” ifadesi ölçülmüş performans değil. **Yeni bağımsız aday yok.**

## 3. James Jecool King — Smart Money Concept / SMC Trading

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 25/Baskı 25/Smart Money Concept - SMC Trading - James Jecool King (22 sayfa) - @eseckal.pdf>) · [Tam metin](03_king_smc.txt)

**Tam okuma:** S. 1 kapak; s. 2–3 H4/M15 piyasa yapısı ve BOS sonrası geri çekilme; s. 4–5 kırılım öncesi son ters mumdan arz/talep, eşit tepe/dip likiditesi; s. 6–7 trend çizgisi ve “zayıf” swing hedefleri; s. 8–12 üst zaman dilimi alanı içinde düşük zaman dilimi CHoCH veya arz/talep dönüşümü; s. 13–18 V dönüşü, RSI ayrışması, iskonto/prim filtresi; s. 19–22 %0,5 giriş riski, 4R'de %20 kısmi çıkış, 10R'de kısmi çıkış ve seçilmiş örnekler. Çeviride `15M`/`1M` bazen “15 aylık”/“15 milyon” olarak aktarılmış; bunlar dakika grafikleridir. “Bankaların fiyatı ittiği” iddiası fiyat grafiğinden kanıtlanamaz. 8–25R örnekleri seçilmiş örneklerdir, beklenti kanıtı değildir.

### JK125A — H4 talep/arz temasında M15 likidite süpürmesi ve yapı dönüşü

- **Kaynak (PDF s. 2–5, 8–13, 19–22):** H4 yönü ve kırılım öncesi son ters mumdan alan; alan içinde likidite alımı sonrası M15 alt yapı kırılımı; talep/arz alanına yeniden testte giriş; bölgenin ötesine stop; giriş başına %0,5 risk. Metin fiyat düzeylerini ve “makul” geri çekilmeyi sayısallaştırmadığı için aşağıdaki eşikler **araştırma için bizim nesnelleştirmemizdir**.
- **Veri ve zaman:** EURUSD, GBPUSD, USDJPY; H4 ana bağlam, M15 sinyal, M1 emir yürütme. Yalnız kapanmış mumlar. H4 ve M15 pivotları iki **sonraki** mum kapanınca kesinleşir; henüz kesinleşmemiş pivot işaretlenmez. Alış için son iki kesinleşmiş H4 pivot tepesi/dibi yükselir. Son H4 yukarı BOS'u, kapanışın önceki kesinleşmiş H4 tepesini aşmasıdır. Bu BOS'tan önceki son düşüş H4 mumunun gövde ve fitili `[low,high]` tek bir **talep alanı** olarak dondurulur; ancak o mumdan BOS'a kadar en fazla 12 H4 bar vardır ve alan oluşturulurken BOS bilinmeden işlem yapılamaz. Alan BOS'dan sonraki en fazla 20 H4 bar geçerlidir ve ilk ziyarette kullanılır.
- **Alış tetikleyicisi:** M15 barı H4 talep alanına değdiğinde izleme başlar. Son 20 **tamamlanmış** M15 bardaki iki bar sağ/sol pivot düşüklerinden en az iki tanesi birbirine `<=0,1 ATR14_M15` yakınsa eşit dip kümesi vardır. Temas barı veya sonraki dört M15 barda `low` bu kümenin altına iner, fakat aynı M15 bar kapanışı kümenin üstüne dönerse “süpürme” sayılır. Sonraki en çok altı M15 barda kapanış, süpürme öncesi son kesinleşmiş M15 pivot tepesini aşarsa yükseliş CHoCH teyididir. Teyit barından sonra ilk M15 düşüş mumu kapanınca onun `[low,high]` aralığı talep dönüş alanı olarak dondurulur; izleyen sekiz M15 barda bu alana ilk dokunuşta M1 kotasyonuyla limit alış denenir. Dönüş alanı hiç oluşmazsa işlem yok. Satış simetrik: H4 düşüş yapısı, son yükseliş mumu arz alanı, eşit tepe üstü süpürme, M15 dip kırılımı ve ilk yükseliş mumuna yeniden test.
- **Risk/çıkış:** Stop süpürme ekstremi ile H4 alan ekstreminden daha uzakta olanın `0,1 ATR14_M15` dışındadır. Pozisyon miktarı stop mesafesine göre özsermayenin `%0,5` ilk riskiyle hesaplanır; maksimum bir işlem/çift. İlk risk `1R`; `4R` görüldüğünde %20 azalt, kalanını ilk sinyalde dondurulmuş yakın karşı H4 pivotuna kadar tut; hedef giriş yönünde ve `>4R` değilse işleme girme. 48 M15 bar sonra veya stop/kar hedefinde tüm kalan pozisyon çıkar. M1 fiyatı iki seviyeye aynı barda değerse önce stop varsay. Gerçek bid/ask, komisyon, kayma, swap ve hafta sonu boşluğu hesaba katılır. Açılmayan limit emri başarı sayılmaz.
- **Ön kayıtlı karşılaştırma:** Aynı H4 alan temasıyla fakat eşit dip/tepe süpürmesi **olmadan** giriş, ardından süpürme var ama M15 CHoCH yok kollarıyla karşılaştır. Önceki [arz/talep BOS/CHoCH](../batch_040/STRATEGIES.md) ve [ileri order block](../batch_058/STRATEGIES.md) adaylarına karşı aynı tarih, veri ve maliyetle ek değerini ölç. Ana hipotez, bu iki teyidin işlem sayısını azaltırken maliyet sonrası net R ve düşüş profilini iyileştirmesidir. Seçim yanlılığını önlemek için H4 alanlarını ve pivotları geçmiş barlara geriye dönük taşımak yasaktır.

## Sonuç

**1 yeni birleşik araştırma adayı:** JK125A. Mum atlası ve swing kılavuzu önceki strateji ailelerine yeni ayırt edici işlem kuralı eklemedi.
