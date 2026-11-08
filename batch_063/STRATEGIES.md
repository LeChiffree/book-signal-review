# Kitap okuma 063 — Taze bölge, EMA geri çekilmesi, çoklu seviye testi

**Kapsam:** Üç PDF'nin gerçek **95 + 50 + 52 = 197 sayfası** sıralı metne çıkarılıp incelendi. Atıflar PDF sayfasıdır. Sayısal bölge/tolerans/eşik ve süreler kaynakta yoksa **bizim backtest tanımımızdır**. Backtest, paper test ve emir yapılmadı.

## 1. Samibegood / A. Riskiyanto — Arz ve Talep Analizi

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Arz ve Talep Analizi - Samibegood - A. Riskiyanto (95 sayfa) - @eseckal.pdf>) · [Tam metin](01_supply_demand_samibegood.txt)

**Kaynak:** Dar dengelenme alanı, alan dışına **kapanışla** güçlü çıkış ve ilk geri ziyaret talep/arz fikrinin çekirdeği (s. 6, 11, 13–14). D1 bölgeye dönüşte M15/M5 ters mumla giriş, bölgenin ötesinde stop ve sonraki karşı bölge veya en az 2:1 hedef (s. 16–19). İlk geri çekilme, geniş kâr alanı, hızlı uzaklaşma ve hiç test edilmemiş “taze” bölge tercihleri (s. 32–33). Kitap kripto borsasındaki gerçek bekleyen emirleri gözlemlemez; bölge etiketini OHLCV vekili olarak kullanıyoruz.

### SR63 — Güçlü çıkışla oluşan taze talep/arz bölgesinin ilk yeniden testi

- **Bölge üretimi:** UTC D1'de 4–12 tam barlık taban; tüm gövde uçları arasındaki aralık `≤1,5×ATR14_D1`, tabanın en yüksek gövde üstü ve en düşük gövde altı sınırdır. Tabanın ardından ilk tam D1 `close>zone.high+0,5×ATR` ve gövde `≥1×ATR` ise talep, aşağı simetri arz. Bölge ve çıkış mumu o kapanışta dondurulur. Bu sayısal taban ve güçlü çıkış ölçüleri bize aittir. Çıkış mumunun high/low'u bölgeye eklenmez.
- **Tazelik/tetik:** Çıkış kapanışından itibaren en çok 30 D1 içinde bölgeye ilk temas; arada H1 high/low herhangi bir temas varsa artık “taze” sayılmaz. İlk temas H1 kapanışıyla bilindikten sonra en çok dört tam H1 bar içinde long için ilk boğa H1 `close>open` ve `close>high[t−1]` (short ters) teyidi. Daha önce stop sınırı ihlal edilmişse iptal. Böylece kaynağın gün içi erken ters mum fikri kapalı mumla ölçülür; kaynağın kapanış beklemeden giriş önerisi ayrı gerçek zamanlı veri olmadan ana test değildir.
- **İcra/risk:** Teyit kapanışından sonraki ilk uygulanabilir 1m giriş. Long stop `zone.low−0,1×ATR14_H1`, short `zone.high+0,1×ATR`; karşıt önceden dondurulmuş bölge 2R'den yakınsa atla. 2R veya 48 H1 süre çıkışı. Stop yanlış tarafta/maliyetten dar ise atla, aynı 1m stop önce. Bölge sayıları ve teyit barı seçimi için duyarlılık; taze/ikinci temas ve güçlü/zayıf çıkış ayrı kollar. Batch058 FL58 ve önceki arz/talep adaylarıyla olay örtüşmesi ölçülür.

## 2. Thomas Carter — Forex 20 Trend Takip Sistemi

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Forex 20 Trend Takip Sistemi - Thomas Carter (50 sayfa) - @eseckal.pdf>) · [Tam metin](02_forex20_carter.txt)

**Kaynak:** Kitap 20 kısa forex reçetesi derler (s. 8–48). #16: EMA7 EMA21 üstünde ve EMA21 yükselen/yatay iken fiyat iki ortalama üstünde; geri çekilme EMA'ların arasına, ardından EMA21'e dokunuş; son mum high+1 pip üstünde alış; short simetri, stop son swing ve 2R hedef (s. 39–40). #8'de EMA4/11 kesişimi ADX13>22 ve yönlü DI filtresiyle (s. 22); #13'te SMA150 yönü, RSI3 aşırılığı ve stochastic kesişimi (s. 33). Pip bazlı diğer reçeteler kriptoya doğrudan taşınmaz.

### TC63 — EMA7/21 trendinde EMA21 temasından sonra son high/low kırılımı

- **Trend/geri çekilme:** H4 kapalı barlarında EMA7>EMA21, `EMA21[t]>EMA21[t−3]`, son üç kapanışın en az ikisi iki EMA üstünde iken long rejimi; short ters. İlk `low≤EMA21` barı temas olur; temas barı öncesinde önceki beş H4 kapanış en az bir kez EMA7 üstünde bulunmalı. Temas anındaki EMA21 kullanılır, çizgi sonraki barlarla geriye kaydırılmaz. Beş/üç bar koşulları ve H4 seçimi bizim test tanımımızdır.
- **Emir:** Temas mumu kapandıktan sonra `touch.high+1 tick` long stop girişi sonraki dört H4 boyunca canlı; her yeni tamamlanmış bar high'ı referans fiyatı yeniden yazmaz. Short `touch.low−1 tick`. 1m veride emir seviyesi ilk geçildiğinde, spread/kayma ile dolum; limit yoksa geçen ama doldurulamayan olasılığı ayrıca raporla. Temas sonrası fiyat EMA21'in karşısında iki H4 kapanış yaparsa ya da dört H4 biterse emri iptal et.
- **Risk/karşılaştırma:** Stop, temas öncesinde 3 sol/3 sağ barla **zaten teyitli** son swing low/high ile temas mumunun low/high'ının daha uzak olanı ±0,1 ATR tampon; stop yanlış tarafta/maliyetten dar ise atla. 2R hedef, en çok 30 H4 süre ve aynı 1m stop önce. Önceki EMA pullback adaylarıyla aynı veri/masraf altında EMA21 teması ve tetik emrinin ek katkısı; kriptoda 1 pip yerine işlem yapılan sembolün tick'i kullanılır.

## 3. Toni Hansen — Pazarı: Destek ve Direnci Anlamak

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Toni Hansen_in Pazarı - Destek ve Direnci Anlamak (52 sayfa) - @eseckal.pdf>) · [Tam metin](03_support_resistance_hansen.txt)

**Kaynak:** Kitap fiyat seviyesi, önceki zirve/dip, sıkışma, boşluk, trend kanalı, eşit hareket ve MA destek/dirençlerini inceler (s. 4–37). Sıkışma bölgesinin ortası güçlüdür (s. 14–15); tekrarlanan testler sınırı aşındırabilir (s. 10, 44–45). Kırılmadan sonra eski desteğin direnç olarak geri testi anlatılır (s. 46). Destek/direncin tek başına işlem vaadi olmadığı, yaklaşım hızı ve hacmin de dikkate alınacağı vurgulanır (s. 23, 48). “Üçüncü test” sayısı örnek anlatımdır, evrensel başarı kanıtı değildir.

### TH63 — İki testten sonra yatay seviye kırılımı ve ilk geri testi

- **Seviye:** H4'te 3 sol/3 sağ kapanmış barla teyitli iki swing high, farkı `≤0,2×ATR14_H4`, araları 5–40 H4. İkinci pivot teyidinde direnç `mean(high1,high2)` olarak dondurulur. Aradaki en az bir kapanış seviyenin `≥0,5×ATR` altında olmalı; short için iki swing low ve üstte ara kapanış. Pivotlar sonraki veriye göre yeniden yerleştirilmez. Tolerans/pencere bizim tanımımızdır.
- **Kırılma/geri test:** İkinci pivot teyidinden sonra en çok 20 H4 içinde ilk `close>resistance+0,1×ATR` long kırılımı. Sonraki en çok altı H4 bar içinde ilk `low≤resistance+0,1×ATR` ve `close>resistance` geri testi; short ters. Tetik geri test mumunun kapanışı sonrası ilk uygulanabilir 1m. Test kapanışından önceki yüksekler kırılım seçimini değiştirmez. Geri test hiç yoksa işlem yok.
- **Risk/karşılaştırma:** Long stop `min(retest.low,level−0,5×ATR)−0,1×ATR`, short simetriği; 2R veya 24 H4 süre. Yanlış taraftaki/dar stopu atla, aynı 1m stop önce. Tek dokunuşlu seviye ve geri testsiz kırılım kollarıyla net R, işlem sayısı, yanlış kırılım oranı; önceki S/R flip adaylarıyla çakışma. Hisse seansı ve gap örnekleri kriptoya mekanik olarak taşınmaz.

## Ortak test sözleşmesi

Üç adayda da yalnız kapanmış bar, o ana kadar teyitli pivot ve dondurulmuş seviye kullanılır. Sonraki uygulanabilir 1m fiyat, ücret, spread, kayma, perpetual funding, eksik veri ve çakışan pozisyon politikası açıkça modellenir. Zaman sıralı ayrılmış doğrulamada işlem sayısı, net R, maksimum düşüş ve yalın taban çizgisi olmadan kârlılık iddiası kurulmaz.
