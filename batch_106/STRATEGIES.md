# Kitap okuma 106 — BFix seviye kırılımı

**Kapsam:** Üç PDF'nin **20 + 20 + 20 = 60 sayfası** baştan sona incelendi. Bressert belgesi ağırlıkla görüntü olduğundan [1–10](bressert_contact_1_10.jpg) ve [11–20](bressert_contact_11_20.jpg) sayfalarının görsel montajı üzerinden ayrıca okundu. Atıflar PDF sayfasıdır. Backtest, paper test veya emir yapılmadı.

## 1. Londra Oturumu Forex Trading Sırları — Alberto Sassetti

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 20/Baskı 20/Londra Oturumu Forex Trading Sırları - Alberto Sassetti (20 sayfa) - @eseckal.pdf>) · [Tam metin](01_london_sassetti.txt)

**Tam okuma:** S. 1–4 tanıtım; s. 5–7 faiz farkı/LIBOR tarihi; s. 8–10 spot/vadeli ayrımı; s. 11–12 BFix tanımı; s. 13–16 M15 EMA/RSI ve BFix kırılımı; s. 17–20 0,0025 EURUSD grid örneği. S. 11 Londra 17:00, yine aynı sayfa 16:00 fix der; s. 14 de 16:00–17:00 civarı der. Bu belirsizlik gerçek BFix ürününün **yayın zamanı ve vintajı** ile çözülmeli. Aynı günün henüz yayınlanmamış BFix değeri daha erken bara taşınamaz. S. 13 EMA9/21+RSI14 anlatımı RSI'nın giriş filtresini açık bağlamaz; s. 14–15 ikinci, tek EMA9 ve RSI(30,70) ile BFix kuralı daha açık. S. 17–20 grid kuralı kendi içinde bazen 25 pip hedef, bazen 50 pip hedef ve belirsiz trend filtresi verir; [105. partideki](../batch_105/STRATEGIES.md) grid risk incelemesiyle birlikte, yeni bağımsız sinyal sayılmadı. S. 19'daki yuvarlak fiyatların kurumsal emir yoğunluğu iddiası gösterilmiş piyasa verisi değildir.

### LS106A — Önceden yayınlanmış BFix düzeyiyle M15 EMA9/RSI14 kırılımı

- **Kaynak (s. 11–12, 14–16):** GBPUSD M15'te fiyat EMA9 üstünde ve `30<RSI14<70` iken Londra BFix referansı üstü long; altında ve EMA9 altındayken short. 5–10 pip hedef, 5–7 pip stop; haber dönemlerinden kaçınma. Bu kitapta BFix yayını ve tam fix saati tutarsız olduğundan aşağıdaki geçmiş gün sürümü **bizim güvenli zamanlama uyarlamamızdır**, kaynağın bire bir kopyası değildir.
- **Nesnel araştırma sürümü:** Yetkili BFix GBPUSD fiyatı, ürün kimliği, fix zamanı, yayın zamanı ve sonradan revizyon bilgisiyle nokta-zaman tablosunda tutulur. Her M15 kararında yalnız `published_at ≤ bar_close` olan **en yeni önceki Londra iş günü** fix'i kullan; aynı gün henüz yayınlanmadıysa önceki gün seviyesini kullan. Bu alanlar yoksa test edilmez. GBPUSD M15 kapanmış bar `close_t>EMA9_t`, `30<RSI14_t<70`, `close[t-1]≤BFix_ref` ve `close_t>BFix_ref` ise long; short simetri. Sadece ilk kesişim, aynı gün aynı yönde en çok bir işlem. Sonraki ilk uygulanabilir M1 ask/bid ile giriş; 7 pip stop, 10 pip hedef kaynak aralığının önceden sabit uçları. 5/5 ve 7/10 pip kombinasyonları ayrı duyarlılık kolları. En çok dört M15 bar süre **bizim**; aynı M1 içinde sıra belirsizse stop önce. Londra saat dilimi/DST ve gerçek takvim kullan; veri gecikmesi, spread, komisyon, slippage ve fix lisans/erişimi kaydedilir. Haber filtresi ancak tarihsel yayımlanma zamanı güvenilir takvimle ayrıca test edilir.
- **Karşılaştırma:** Aynı EMA9/RSI M15 kesişiminde BFix seviyesi yerine önceki gün Londra saatindeki spot kapanışı ve önceki gün high/low gibi erişilebilir düzeylerle, ayrıca BFix filtresiz modelle karşılaştır. BFix alfa varsayımı yok; veri yoksa bu aday *bekleyen araştırma*, sentetik fix kullanılmaz. FX özel düzey BTC/ETH'ye doğrudan taşınmaz.

## 2. Düşük Riskli Swing Trading için Gün İçi Zamanlama — Walter Bressert

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 21/Baskı 21/Düşük Riskli Swing Trading için Gün İçi Zamanlama - Walter Bressert - Orijinal (20 sayfa) - @eseckal.pdf>) · [Çıkarılan metin](02_swing_bressert.txt) · [Görsel s. 1–10](bressert_contact_1_10.jpg) · [Görsel s. 11–20](bressert_contact_11_20.jpg)

**Tam okuma/görsel denetim:** S. 1 kapak, s. 2–3 sunum ve haftalık döngü; s. 4–6 20 haftalık/20 günlük döngü, 5–6 barlık osilatör ve buy/sell dönüşleri; s. 7–9 günlük yönü gün içine taşıma; s. 10–13 4×72 dakika / 18 bar ve 54 dakika / 18 bar örnekleri, döngü içi döngüler; s. 14–15 kombinasyon ve giriş zamanlaması; s. 16–19 el çizimleri; s. 20 kapanış. PDF'nin çoğunun metin katmanı yalnız sayfa numarası içeriyor; bu nedenle metin çıkarımı tek başına okuma kanıtı değildir. Grafikler geriye dönük işaretli döngü tepeleri/dipleri gösterir. “Oscillator”ın kesin formülü/periyodu, tepe/dip teyit gecikmesi, hangi döngünün ne zaman aktif olduğu, somut stop ve çıkış eksik. O an bilinmeyen 18 bar sonunu geçmiş sinyale atamadan mekanik kopya çıkarılamaz; yeni aday açılmadı. Döngü zamanlaması ileriye dönük ayrı araştırma fikri olarak not edildi.

## 3. Nasdaq Endeksi ile Tradingin Sırları — Muko Ruth

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 6/Baskı 6/Nasdaq Endeksi ile Tradingin Sırları (20 sayfa) - @eseckal.pdf>) · [Tam metin](03_nasdaq_secrets.txt)

**Tam okuma:** S. 1–6 Nasdaq100 ve etkenler; s. 7–8 CAT saatleri/haberler; s. 9–12 D1 yapı, M15 bölgeler, H1/H4 pin bar için trend-seviye-sinyal; s. 13–19 H1 order block çizimi, ilk kırılım ve tekrar test; s. 20 kapanış. Kaynak “açık trend”, “kolay tanınan seviye”, “güçlü çıkış” ve “başarılı retest” ölçülerini, pin bar oranlarını veya stop/hedefi kodlanabilir biçimde vermez. Pin bar/level ve order block retest çekirdeği önceki arşiv adaylarıyla örtüşüyor. Yeni bağımsız aday sayılmadı. S. 5'teki “%99,9 temeller belirler” iddiası ölçülmüş açıklayıcı güç değildir; ekonomik haber takvimi 24/7 kripto olayına doğrudan çevrilmez.

## Sonuç

**1 yeni araştırma adayı:** LS106A. BFix nokta-zaman verisi sağlanmadan uygulanmış sayılmayacak; Bressert ve Nasdaq kitapları okunup gerekçeleriyle kaydedildi.
