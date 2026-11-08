# Kitap okuma 124 — düzeltmenin iki katı dürtüyle teyitli trend dönüşü

**Kapsam:** Üç ayrı PDF'nin **37 + 25 + 46 = 108 sayfası** baştan sona okundu. Atıflar PDF sayfasıdır. Backtest, paper test ve emir yapılmadı.

## 1. Andy Crowder — 3 Basit Opsiyon Stratejisi

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 4/Baskı 4/3 Basit Opsiyon Stratejisi - Andy Crowder (37 sayfa) - @eseckal.pdf>) · [Tam metin](01_crowder_options.txt)

**Tam okuma:** S. 1–7 opsiyon temeli; s. 8–10 RSI2/3/5/14 uç değerleri ile özel, açıklanmayan modelin giriş bağlamı; s. 11–14 boğa put/ayı call kredi spreadleri; s. 15–20 nötr RSI ile IV sırası ve demir kondor, haftalık opsiyon; s. 21–32 nakit teminatlı put ve seçilmiş ETF/hisse örnekleri; s. 33–37 covered call ve put–call döngüsü. S. 9 özel modelin tüm ayrıntıları verilmediğini söyler. S. 25–29'daki put örneklerinde 22,50×100=2.250 iken 2.150 olarak yazılması, “marjın %20'si = riskin tamamı” yorumu ve s. 32'de 85×100 için yanlış tutar gibi aritmetik/risk hataları vardır. %80 OTM olasılığı, %80 kârlı işlem olasılığı veya pozitif beklenti demek değildir; derin zarar, tahsis, komisyon, kotasyon genişliği ve temettü/erken kullanım hesaba katılmalıdır. Opsiyon fiyatı, vade, IV, bid/ask ve tahsis OHLC mumlarından üretilemez. Bu nedenle kullanıcının **kapalı mumla üretilebilir** strateji kütüğüne bu kitaptan aday eklenmedi. Ayrı opsiyon veri hattı kurulduğunda spread/put/covered call için bağımsız araştırma dosyası açılabilir.

## 2. IntroBooks — Günlük Trading

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 12/Baskı 12/Günlük Trading - Intro Books - Learning is Easy (25 sayfa) - @eseckal.pdf>) · [Tam metin](02_intro_day_trading.txt)

**Tam okuma:** S. 1–8 gün içi ticaret ve kaldıraç; s. 9–16 piyasa/ECN tarihi; s. 17–20 trend, karşı trend, aralık, scalping, haber ve fiyat hareketi kategorileri; s. 21–23 komisyon, spread ve eski düzenleme açıklamaları; s. 24–25 sonuç/yayınevi. S. 17–20 kategoriler için giriş eşiği, sinyal barı, stop veya çıkış süresi verilmez; önceki trend ve aralık ailelerine yeni uygulanabilir kural eklenmedi. “Limit emirle spread kazanma” fikri sıra derinliği ve dolum olasılığı olmadan OHLC'de test edilemez. S. 23'teki hukuk ve hesap koşulları tarihsel bağlamdır, güncel kural olarak kullanılmaz. **Yeni aday yok.**

## 3. Laurentiu Damir — Price Action Trends

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 16/Baskı 16/Price Action Trends - Laurentiu Damir (46 sayfa) - @eseckal.pdf>) · [Tam metin](03_damir_trends.txt)

**Tam okuma:** S. 1–10 HH/HL veya LH/LL trendi, ters yönde düzeltmenin son dürtüyü geçmemesi; s. 11–24 yeni salınım çiftini ancak düzeltmenin yaklaşık **iki katı** büyüklüğündeki devam dürtüsüyle teyit etme; s. 25–30 benzer ölçekli dalga seçimi; s. 31–36 önceki teyitli LH/HL geçişi, küçük düzeltme ve yeniden kırılımla trend dönüşü; s. 37–39 H1 girişini kapanmış H4 trendiyle aynı yöne süzme, stopu yeni teyitli HL/LH ardında takip etme; s. 40–46 seçilmiş işlem çizimleri ve kapanış. S. 30 seçimin kesin bilim olmadığını açıkça belirtir. S. 3'teki “yüzlerce/binlerce pip” ve s. 37'deki %80–90 piyasada kalma beklentisi istatistiksel kanıt değildir. Bu kitabın ayırıcı araştırma sorusu, **düzeltme boyutuna göre iki kat devam dürtüsüyle salınım teyidi**nin standart pivot teyidine katkısıdır.

### LD124A — İki kat dürtüyle teyitli salınım sonrası H1 trend dönüşü

- **Kaynak (PDF s. 10–16, 25–33, 36–39):** Potansiyel pivotu yalnız fiyat yeni yönde yeterince güçlü devam ettikten sonra onayla; devam dürtüsü önceki düzeltmenin yaklaşık iki katı olmalı. Son geçerli LH/HL aşılınca yeni yönde küçük düzeltmenin ardından yeniden kırılımda giriş; H4 trendi aynı yönde; stop son düzeltme ekstreminde ve yeni teyitli salınımlarla izlenir.
- **Kapalı mum sözleşmesi:** Likit majör FX çiftleri EURUSD, GBPUSD, USDJPY, USDCHF, USDCAD, AUDUSD, NZDUSD; H1 sinyal ve yalnız **son kapanmış** H4 bağlamı. Her zaman anında `k=2` sağ barla kesinleşmiş H1 pivot yüksek/düşükleri kullan. Boğa yönü için son düşüşteki ilk kesinleşmiş dip `L0`, onu izleyen düzeltme tepesi `LH`, sonra yeni dip `LL` olsun; `Q=LH−L0` düzeltme, `D=LH−LL` devam dürtüsüdür. `LL<L0`, `D>=2Q` ve üç pivot da kendi teyit barından önce kullanılmıyorsa eski düşüş salınımı onaylanır. Sonraki H1 kapanışı teyitli `LH` üstüne çıkar ve en çok 8 H1 içinde en az bir aşağı düzeltme barı (`close<open`) oluşur; onun ardından ilk H1 kapanışı bu yeni düzeltme öncesindeki tepenin üstüne geçerse long sinyal. H4 filtresi: son tamamlanmış H4 kapanışı `SMA50_H4` üstünde ve son iki teyitli H4 pivot dibi yükselen. Short bütün fiyat ilişkilerinin simetriği. `k=2`, 8 bar, H4 SMA50 ve fiyatın kapanışla kırılması **bizim** nesnelleştirmemizdir; kaynak bunları sayıyla vermez. Sinyal H1 kapanınca sonraki ilk uygulanabilir M1'de giriş; stop yeni küçük düzeltmenin ekstremi dışına `0,1 ATR14_H1`; başlangıç riskine göre %0,5 özsermaye pozisyonu. Her yeni **kapanışta teyit edilmiş** HL/LH ile stop yalnız lehe güncellenir; 48 H1 sonra veya stopta çıkış. Tek açık işlem/çift. Gerçek bid/ask, komisyon, kayma ve hafta sonu boşlukları dahil; aynı M1 stop/hedef belirsizliğinde kötümser sıra.
- **Ayrışma:** Aynı trend dönüşü için `D>=2Q` koşulsuz kol, sıradan iki sağ bar pivotu ve [3MS yapı teyidi](../batch_018/STRATEGIES.md) ile aynı dönem/maliyet altında karşılaştır. İki kat dürtü filtresinin işlem sayısını düşürürken maliyet sonrası net R'yi iyileştirip iyileştirmediği asıl hipotezdir. H4 filtresini ayrı kaldırma kolunda ölç. Pivot uçlarını gelecekteki fiyatla yeniden etiketleyip eski barlara sinyal taşımak yasaktır.

## Sonuç

**1 yeni araştırma adayı:** LD124A. Opsiyon kitabının stratejileri ayrıca gerçek opsiyon veri hattı gerektirir; sonuçları kâr garantisi değildir.
