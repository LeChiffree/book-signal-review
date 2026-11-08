# Kitap okuma 164 — formasyon çizelgesi, fiyat yapısı ve Japon mumları

Üç ayrı PDF'nin **33 + 48 + 50 = 131 sayfası** incelendi. İlk PDF'de metin katmanı yalnız filigran içerdiği için 33 sayfanın tamamı [görsel dizin 1](chart_patterns_contact_1.jpg), [2](chart_patterns_contact_2.jpg), [3](chart_patterns_contact_3.jpg) ile görsel olarak okundu. Atıflar PDF sayfasıdır. **Yeni bağımsız araştırma adayı: 1.** Backtest/paper test/emir yapılmadı.

## 1. Grafik Kalıpları — Chart Patterns Cheat Sheet

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 17/Baskı 17/Grafik Kalıpları (33 sayfa) - Orijinal - @eseckal.pdf>) · [çıkarılan metin](01_chart_patterns.txt)

**Görsel tarama:** s. 1–3 kapak ve genel dizin; 4–16 çift tepe/dip, omuz-baş-omuz, yükselen/düşen takoz ve seçilmiş grafikler; 17–33 bayrak, flama, yükselen/düşen üçgen ve dikdörtgenler. Formasyonların kapanmış mumla nasıl tamamlandığı, pivot genişliği, işlem süresi, stop ve hedef birlikte sayısal verilmez. Aynı aileler [3.](../batch_003/STRATEGIES.md), [16.](../batch_016/STRATEGIES.md) ve [72. partide](../batch_072/STRATEGIES.md) var. **Yeni bağımsız aday yok.**

## 2. Price Action — Daniel Stones

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 19/Baskı 19/Price Action - Daniel Stones (48 sayfa) - @eseckal.pdf>) · [tam metin](02_price_action_stones.txt)

**Tarama:** s. 1–15 klasik formasyonlar ve kırılım/retest; 16–24 çoklu zaman dilimi, HH/HL ve M15/M5 örnekleri; 25–34 tepe/dip ve iki ardışık yüksek/düşük barla salınım teyidi; 35–45 yapı değişimi, seviye ve SMA200 bağlamı; 46–48 28 FX çifti üzerinden para birimi gücü ızgarası. S. 30–33'teki pivot tanımı sonraki barlar oluşmadan bilinemez; s. 33–34'te aşırı büyük barların geriye dönük göz ardı edilmesi veya döngünün sıfırlanması kaynakta sayısal eşiksizdir. Klasik formasyon, çoklu zaman dilimi ve SMA200 konuları önceki adaylarla örtüşür. S. 46–48'deki **çiftler arası +1/−1/0 oy toplamı** farklı bir seçim kuralıdır; giriş/çıkış kaynağın parçası olmadığından aşağıda araştırma varsayımı olarak ayrı yazıldı.

### DS164A — 28 FX çiftinden güçlü/zayıf para birimi sıralaması

- **Kaynak kural:** Günlük grafikte son iki teyitli tepe ve dip yükseliyorsa baz para birimine +1, karşı para birimine −1; ikisi de düşüyorsa ters işaret; karışık yapıysa iki para birimine 0 yaz. Sekiz majör para biriminin 28 farklı çifti için oyları topla; en yüksek puanlıyı en düşük puanlıya karşı seç (s. 46–48). S. 47'de CAD +6, NZD −5 örneğiyle NZDCAD short izleniyor. Bu **seçim filtresidir**, kitap tam stop/çıkış vermez.
- **Veri/ön kayıt:** USD, EUR, GBP, JPY, CHF, CAD, AUD, NZD'nin 28 tekil çaprazı için aynı New York 17:00 kapanışına hizalanmış, tarihsel bid/ask D1 OHLC gerekir. Sadece işlem gününde mevcut pariteler; herhangi bir çift eksikse o gün sinyal yok. Önceden sabit kanonik kotasyon yönü seçilir; ters kotasyonlar fiyatlar çevrilerek, bid/ask tarafı da doğru terslenerek normalleştirilir. Sonradan seçilmiş piyasa/çift dönemi kullanılmaz. En az 60 tam ortak D1 bar ısınma.
- **Pivot/puan:** Kaynağın iki yüksek/düşük bar teyidini ileriye bakmadan uygulamak için her paritede aday dip, kendisinden sonra ve aday dip altına inmeden oluşan *iki* yeni daha yüksek high olayı tamamlanınca teyit edilir; aday tepe için iki yeni daha düşük low simetrik. Bu olaylar en çok 10 D1 barda tamamlanmazsa aday düşer. Aynı yönde devam eden bar yeni olay sayılmaz; her olay önceki kırılan high/low'u aşmalı. Eşitlik teyit sayılmaz. Son iki teyitli tepe ve dipten HH+HL için +1/−1, LH+LL için −1/+1, diğerinde 0. Bu kesin olay ve 10 bar sınırı **bizim mekanik uyarlamamızdır**; sonuç pivot genişliği duyarlılığıyla raporlanır. Puan her ortak D1 kapanışında yeniden hesaplanır; gelecekte teyit olan pivot geçmiş günün puanını değiştirmez.
- **Giriş/çıkış:** En yüksek ve en düşük puan tekil olmalı, fark ≥6 ve seçilen paritenin kendi D1 yapısı güçlüden zayıfa yönde olmalı. Bu eşik ve giriş **bizim test sözleşmemizdir**. Aynı sinyalin ertesi uygulanabilir FX açılışında güçlü para birimi long/zayıf short yönünde tek pozisyon. Stop `1,5×ATR14_D1`, hedef `3×ATR14_D1`; puan farkı <3 olursa sonraki açılışta, aksi halde en çok 20 D1 bar sonra çık. Bir seferde tek portföy pozisyonu; beraberlik veya spread/maliyet verisi yoksa işlem yok.
- **Risk/test:** Giriş anındaki özsermayenin en çok %0,25'i stop riski, birim lot aşağı yuvarlanır. Gerçekçi FX spreadi, komisyon, kayma, overnight swap ve hafta sonu gap'i dahil. Aynı fiyat/kapanış verisiyle **seçilen çiftte basit D1 trend takibi**, puan eşiği 0/6/10 ve top-bottom seçim olmadan tüm çiftlerde trend sinyali karşılaştırılır. Olay sayısı, net R, maksimum düşüş, para birimi yoğunluğu, veri eksikliği, eşzamanlı çapraz korelasyonu ve dönem dışı sonuçlar raporlanır. Tarihsel 28 çift ve maliyet verisi olmadan kripto OHLCV üzerinde eşdeğer diye sınanmaz.

## 3. Japon Mum Grafik Teknikleri — James Abbott

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 19/Baskı 19/Japon Mum Grafik Teknikleri - James Abbott (50 sayfa) - @eseckal.pdf>) · [tam metin](03_candles_abbott.txt)

**Tarama:** s. 1–12 giriş, Dow trendi ve seviye; 13–17 çekiç, yutan, harami ve mumlar; 18–25 çift tepe/dip, sahte kırılım, genişleyen formasyon ve Fibonacci; 26–29 Bollinger bandı ve sıkışma; 30–33 stokastik, RSI ve ayrışma; 34–38 MA kullanımı; 39–43 risk; 44–50 psikoloji ve kaynakça. S. 19 çift tepe boyun kırılımı→retest→ayı mumu, s. 27 BB trend yönünde bant temasında mum teyidi ve s. 29 BB sıkışma kırılımı önceki adaylarla aynı olay aileleri. S. 31'de stokastik %K/%D formülleri kendi arasında tutarsız; platform göstergesi yerine harfi harfine kodlanamaz. S. 24'teki piyasaların %70 yatay/%30 trend olduğu iddiası doğrulanmış bir sabit değildir. **Yeni bağımsız aday yok.**

**Parti sonucu:** 3 kitap, 131 sayfa, 1 yeni aday. Toplam **492 tamamlanmış ayrı kitap, 21.716 sayfa, 395 doğrulanmamış strateji adayı**.
