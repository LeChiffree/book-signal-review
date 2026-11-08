# Kitap okuma 121 — zayıf açılışın önceki kapanışı geri alması

**Kapsam:** Üç ayrı PDF'nin **25 + 29 + 27 = 81 sayfası** baştan sona tarandı. Atıflar PDF sayfasıdır. Backtest, paper test veya emir yapılmadı.

## 1. Colibri Trader — Price Action ile arz ve talep

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 7/Baskı 7/Price Action - Colibri Trader - Demsu (25 sayfa) - @eseckal.pdf>) · [Tam metin](01_colibri_price_action.txt)

**Tam okuma:** S. 1–9 arz/talep çizgisi ile bölgesinin ayrımı, impulsif mum ve küçük gövdeli kümeyle bölge seçimi, yuvarlak fiyat; s. 10–14 önceden seçilmiş bölgeye dönüşte mum teyidi ve D1/H4 zaman dilimi; s. 15–25 D1/H4/H1/M15 örnekleri, pin/yutan/inside teyidi ve yüksek zaman dilimiyle örtüşme. Metin tüm ticaret sisteminin verilmediğini s. 14'te açıkça söyler. Bölge sınırı, “güçlü” mum ve uygun retest uzaklığı nesnel eşik içermez. Arşivdeki arz/talep, seviye + mum ve çoklu zaman dilimi fikirleriyle aynı aile; **yeni bağımsız aday yok**. Büyük katılımcıların bu bölgelere emir koyduğu metinde kanıtlanmıyor.

## 2. Price Action Dinamikleri — RektProof notları

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 7/Baskı 7/Price Action Dinamikleri (29 sayfa) - @eseckal.pdf>) · [Tam metin](02_price_action_dynamics.txt)

**Tam okuma:** S. 1–3 kırıcı bölge; s. 4–7 aralık dışına sapma, yapı kırılımı, arz/talep retesti ve karşı aralık ucu hedefi; s. 8–9 birikim/süpürme/dağıtım; s. 10–15 kırık salınım ve ters dönüş; s. 16–20 üç dokunuş; s. 21–25 yapı ile arz/talep bağlamı; s. 26–29 yüksek zaman dilimi talebi ve disiplin. Grafik ağırlıklı sayfalar s. 7, 9, 14–15, 18–20, 27, 29'da ek nicel kural vermiyor. Süpürme + yapı kırılımı + retest, mevcut likidite/SFP ve order-block ailesiyle örtüşür; “kurumsal manipülasyon” nedenselliği varsayılmaz. S. 21 metnin öznel olduğunu belirtir. **Yeni bağımsız aday yok.**

## 3. Stephen W. Bigalow — Kazançlı Mum Giriş Çıkış Stratejileri

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 7/Baskı 7/Kazançlı Mum Giriş Çıkış Stratejileri (27 sayfa) - @eseckal.pdf>) · [Tam metin](03_candle_entries_exits.txt)

**Tam okuma:** S. 1–5 mum dönüşü ve stokastik bağlamı; s. 6–11 sinyal sonrasındaki açılış/gap; s. 12–15 güçlü/zayıf hisse ve endeks açılışına göre karar ağacı; s. 16–20 zayıf açılışta önceki kapanışın geri alınması, Harami/Doji; s. 21–27 çıkış ve yeniden giriş. S. 2, mum sinyallerinin başarı istatistiklerinin henüz toplanmadığını söylemesine rağmen %60–80 arası oranlar ileri sürer; bunlar doğrulanmış sonuç değildir. S. 16'da sinyalin ertesi günü önceki gövdenin yarısından aşağıda kapanırsa çıkış önerilir; bu yeni giriş değil, mevcut mum adaylarının çıkış ablation'ıdır.

### BG121A — Boğa dönüş sinyalinden sonra düşük açılışın kapanışı geri alması

- **Kaynak (PDF s. 7, 12–18):** Boğa mum dönüşünden sonraki seans önceki kapanıştan düşük açılırsa hemen almak yerine önceki günün kapanışında buy-stop kur; o düzey geri alınınca giriş. Bu, genel yutan/çekiç deseninden farklı bir **ertesi seans yürütme filtresi** olarak sınanır.
- **Kapalı mum ve emir sözleşmesi:** Likit, geçmişten seçilmiş ve delisted hisseleri içeren ABD hisse evreni; düzeltilmiş D1 OHLC sinyali, gerçek seans açılışı ve M1 uygulama verisi. Tamamlanmış D1 `t` boğa yutan (karşı renk gövdeyi tamamen kapsayan) veya çekiç (alt fitil ≥2 gövde, üst fitil ≤0,5 gövde) ise ertesi gün `t+1` açılışı `C[t]` altında ama `low[t]` üstündeyse `C[t]+1 tick` buy-stop konur. Yalnız `t+1` seansında dolabilir; ilk M1 açılışı seviyenin üzerindeyse fiyat atlaması gerçek kotasyonla işlenir, önceki fiyattan varsayımsal dolum yok. `t+1` kapanışına dek dolmazsa iptal. Sinyal öncesi düşüş bağlamı: `C[t-1] < SMA20[t-1]` (**bizim** nesnelleştirmemiz). Stop `low[t]-1 tick`, hedef 2R veya 10 seans sonunda çıkış; %0,5 özsermaye riski/işlem, tek pozisyon/hisse. Ücret, spread, kayma, açılış açık artırması ve kurumsal eylemler uygulanır. Stop mesafesi sıfır/negatifse işlem yok. Sinyal ve evren `t` kapanışında kilitlenir; `t+1` açılışına göre önceden seçim yapılmaz.
- **Ayrışma:** Aynı sinyaller için (i) tüm ertesi açılışlardan alım, (ii) düşük açılışta hemen alım, (iii) düşük açılışta önceki kapanışın geri alınması kolları; her kolun gerçekleşen işlem sayısı, unfilled oranı ve maliyet sonrası R dağılımı kıyaslanır. Endeks/vadeli işlem açılışını filtreleyen varyant yalnız nokta zamanlı veri mevcutsa eklenir. Seanslı hisse gap mantığı 7/24 kriptoya doğrudan taşınmaz.

## Sonuç

**1 yeni araştırma adayı:** BG121A. İki diğer kitap arşivdeki sinyal aileleri için bağlam ve teyit varyantları sağlar; doğrulanmış getiri sunmaz.
