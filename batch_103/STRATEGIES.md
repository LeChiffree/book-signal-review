# Kitap okuma 103 — Donchian uç dönüşü ve eş dönem EMA/SMA geçişi

**Kapsam:** Üç özgün PDF'nin **26 + 18 + 20 = 64 sayfası** baştan sona okundu. Kural ve grafik sayfaları [görsel olarak](figure_contacts/) incelendi. Atıflar PDF sayfasıdır. Kaynak sonucu bağımsız backtest değildir; bu turda backtest, paper test veya emir yapılmadı.

## 1. EURUSD için 3 adet Günlük İşlem Stratejisi — Daniel G. G.

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 24/Baskı 24/EURUSD için 3 adet Günlük İşlem Stratejisi - Daniel G. G. (26 sayfa) - @eseckal.pdf>) · [Tam metin](01_eurusd_three_daniel.txt)

**Tam okuma:** S. 1–3 özet ve uyarı; s. 4–10 M30 Parabolic SAR; s. 11–17 H1 Donchian120 alt/üst uçları; s. 18–25 H1 EMA34/SMA34 kesişimi ve ATR4; s. 26 risk uyarısı. Kural/örnek/kod sayfaları 5–7, 9, 12–14, 16, 19, 21–22, 24 görsel kontrol edildi. S. 2, 5, 12, 19'daki 2023 getirileri tek bir tarih penceresinin yazar çıktısıdır; doğrulanmış veri, karşılaştırma veya gelecekteki getiri değildir. Pine kodu çevrilmiş ve değişken isimleri bozulmuş; metin kuralları esas alındı. S. 6 SAR(0,002;0,002;0,02), 80 pip stop/60 pip hedef ve ters sinyalde döndürme verir; bu esasen mevcut SAR dönüş ailesinin parametre/çıkış varyantıdır, yeni bağımsız aday sayılmadı. İlk uygulamada kaynak performansını yeniden üretme denetimi için ayrı benchmark olabilir.

### DG103A — Donchian120 karşı uç temasıyla dönüş

- **Kaynak (s. 11–16):** EUR/USD H1, Donchian periyodu 120, ofset 1. Alt banda temas biten mum sonrası long; üst banda temas sonrası short. Sabit 50 FX pip stop, 40 FX pip hedef; açık pozisyon varken yenisini açma. S. 16'daki sözde Pine kodu `request.security` ve değişken adları çeviride bozulmuş; doğru bant t−1'e kadar hesaplanan 120 tamamlanmış bar yüksek/düşüğüdür. Kâr/risk oranı 0,8'dir; yüksek kazanma iddiası net beklenti kanıtı değildir.
- **Nesnel araştırma sürümü:** Önce EUR/USD 1h bid/ask OHLC ile kaynak doğrulaması: `L_t=min(low[t−120:t−1])`, `U_t=max(high[t−120:t−1])`; kapanan t mumunda `low_t≤L_t` long veya `high_t≥U_t` short. Aynı mum iki banda dokunursa olay yok. Sinyal tamamlanınca sonraki uygulanabilir 1m dolum; EUR/USD için stop 50 pip, hedef 40 pip. BTC/ETH karşılaştırma kolunda stop `ATR14_1h` ve hedef `0,8×stop` **bizim fiyat ölçeklememizdir**, Forex pip kopyası değildir. Emir açılınca aynı yöndeki yeni sinyaller atlanır, zıt sinyalde sonraki 1m'de kapatıp tersine dönme kaynakta SAR için açık, Donchian'da açık değildir; Donchian bazında tersine dönme yok. En çok 48 adet 1h bar süre **bizim**. Aynı 1m stop/hedefte stop önce, maliyetler uygulanır. Önceki Donchian **kırılım** adayından yönü farklı; iki aile ve sıkışma/ADX rejimleri net R ile karşılaştırılır.

### DG103B — EMA34/SMA34 geçişi ve ATR4 hareket kapısı

- **Kaynak (s. 18–24):** EUR/USD H1; EMA34, SMA34'ü yukarı kesince long, aşağı kesince short, yalnız ATR4 `>0,0015` (15 pip). Stop ve hedef 20'şer pip. Kodu çevrilmiş ve satırları hatalı; kapanmış mumda kesişim yorumu metne uygundur. Bu, aynı dönemdeki EMA/SMA farkının işaret değişimiyle oluşan yeni bir olaydır, klasik farklı dönem MA kesişimiyle eşdeğer sanılmamalıdır.
- **Nesnel araştırma sürümü:** EUR/USD H1 tamamlanmış kapanışta `EMA34[t−1]≤SMA34[t−1]`, `EMA34[t]>SMA34[t]`, `Wilder ATR4[t]>0.0015` long; short simetri. Sonraki ilk uygulanabilir 1m dolum, gerçek dolumdan 20 pip stop ve 20 pip hedef. Aynı yönde işlem üst üste yok, zıt sinyal oluştuğunda mevcut pozisyonu sonraki 1m'de kapatıp yeni giriş yapılması ayrı kol; kaynak EMA/SMA bölümünde bunu belirtmez. BTC/ETH kolunda `ATR4/close>0.0015` rejim kapısı ve 1×ATR4 stop/hedef **bizim**. En çok 24 H1 süre **bizim**; aynı 1m stop önce. Filtreli/filtersiz, standart EMA/SMA ayrı dönemli kesişim ve basit momentum olayı ile maliyet sonrası fark ve işlem çakışması karşılaştırılır.

## 2. Kazançlı Hareketli Ortalama Trading Sistemi — Stephan Miller

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 25/Baskı 25/Kazançlı Hareketli Ortalama Trading Sistemi - Stephan Miller (18 sayfa) - @eseckal.pdf>) · [Tam metin](02_ma_miller.txt)

**Tam okuma:** S. 1–8 yapı yüksek/düşük açıklaması; s. 9–14 EMA55/89/144, 55–89 dinamik bölge; s. 15–17 yapı kırılımından sonra %38,2–61,8 Fibonacci geri çekilmesi, bölge, pin/çift dip/iki bar teyidi ve önceki swing hedefi; s. 18 sonuç. Görseller s. 10, 12, 15–17 incelendi. Talep/arz bölgesini hangi geçmiş barın nasıl oluşturduğu, pivot sağ teyidi, karmaşık düzeltme ve üst zaman dilimi koşulu nicel değildir. S. 17 short girişte “talep bölgesi” ve “satın alma limit”, short onayda çift dip yazması yön/çeviri hatasıdır. Bu haliyle tam sistemi sırf EMA parametresi değiştirerek yeni sinyal saymıyoruz. Gelecekte geçmişten teyitli pivot ve bölge tanımı belirlenirse EMA55/89+Fibonacci birleşimi, mevcut EMA geri çekilme adaylarının ablation'ı olabilir; o tanım **kaynağın değil bizim hipotezimiz** olacaktır.

## 3. Ultimate MACD Giriş Stratejisi — Richard Krugel

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 7/Baskı 7/Ultimate MACD Giriş Stratejisi - Richard Krugel (20 sayfa) - @eseckal.pdf>) · [Tam metin](03_macd_krugel.txt)

**Tam okuma:** S. 1–6 MACD(12,26,9); s. 7–9 fiyat/momentum ayrışması ve trendde erken sinyal uyarısı; s. 10–15 H4 trend, Fibonacci/geometri/düzeltme alanı, alt zaman diliminde histogram ayrışması ve dönüş barı örneği; s. 16–20 ücretli tam sisteme yönlendirme. Grafikler s. 8, 11, 13–14 incelendi. Pivot ve Fibonacci alanı nasıl sabitlenir, dönüş barı koşulu, stop, çıkış ve zaman sınırı verilmez; yazar s. 4 ve 17'de tam sistemi kitap dışına bırakır. Histogram ayrışması önceki MACD divergence adaylarıyla örtüşür; yeni bağımsız aday sayılmadı.

**Arşiv eşdeğerliği:** Bu turda ayrıca 23 sayfalık `VWAP Trading Stratejisiyle Kolay Para - Kartik K` tamamen okunup, [43. partideki aynı içerikli VWAP/PVWAP kitabıyla](../batch_043/STRATEGIES.md) eşleştirildi. Aynı s. 16–17 VWAP/PVWAP üstü/altı mum ve yüksek/düşük kırılım kuralı yeniden sayılmadı. [Çıkarılan metin](02_vwap_kartik.txt) denetim izi olarak kaldı.
