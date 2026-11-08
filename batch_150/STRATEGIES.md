# Kitap okuma 150 — Dow, gövde–fitil çift dip/tepe ve kripto grafik temelleri

Üç ayrı kitap, toplam **77 PDF sayfası**, baştan sona incelendi. **Yeni araştırma adayı: 1.** Kaynak kuralı ile bizim ölçülebilir test parametrelerimiz ayrıdır. Backtest, paper test ve emir yapılmadı; kârlılık iddiası yoktur. Sayfalar PDF sayfasıdır.

## 1. Dow Teorisi — Michael Young

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 20/Baskı 20/Dow Teorisi - Michael Young (23 sayfa) - @eseckal.pdf>) · [tam metin](01_dow_young.txt) · [s. 20 görseli](dow_p20.png)

**Tam okuma:** s. 1–7 giriş/yasal/tanıtım; s. 8–12 Dow varsayımları; s. 13–17 birincil trend, daha yüksek tepe/dip, iki endeks teyidi, hacim, aralık ve ikincil hareket; s. 18–21 boğa/ayı aşamaları; s. 22–23 sonuç. Metin çıkmayan s. 20 görseli incelendi, yalnız birikim–ana hareket–aşırılık şeması.

**Karar:** Fiyat yapısı, hacimli trend teyidi ve aralık kırılımı önceki adaylarda var. s. 14'teki sanayi ve taşıma endeksi teyidi, BTC/ETH için aynı ekonomik ilişki değildir. “Hızla takip” süresi, trend pivotunun seçimi ve işlem çıkışı kaynaktan nesnel biçimde çıkmıyor. Yeni aday yok.

## 2. Alfa Crypto Ders Notları

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 22/Baskı 22/Alfa Crypto Ders Notları (27 sayfa) - @eseckal.pdf>) · [tam metin](02_alfa_crypto.txt) · [çift dip s. 3](alfa_p3.png) · [çift tepe s. 4](alfa_p4.png) · [trend devamı s. 23](alfa_p23.png)

**Tam okuma:** s. 1–2 kural ve örneklem uyarısı; s. 2–4 çift dip/tepe için ilk ekstremumun **gövde ucu ile fitil ucu arası** ikinci temas bölgesi ve yaklaşık 5–25 mum ara; s. 5–11 omuz–baş–omuz/tersi, gövde sınırı ve boyun kırılımı; s. 12–22 RSI'nin baş/tepe sırasında 70/30 aşırısı, kapanışla giriş, ATR marjı ve örnek stop/hedef; s. 23–27 EMA200 yönünde çift dip/tepe ve omuz–baş–omuz devamı, boyun kırılımı ve örnek 1,4R. s. 20–21 başarısız örnek de gösteriliyor. s. 3–4 ve 23'ün çizimleri görsel kontrol edildi.

**Ayırt edici kaynak fikri:** İkinci dip/tepe, ilk ekstremumun gövde–fitil aralığına dokunur; gövdesi ilk ekstremumun fitil sınırını aşarsa yapı geçersizdir (s. 3–4). Trend devamı için fiyat EMA200 tarafında kalır ve ara tepe/dip (boyun) kırılır (s. 23–25). Bu, [G1](../batch_003/STRATEGIES.md) ve [R35](../batch_035/STRATEGIES.md) çift dip/tepe adaylarının yalnız tepe/dip toleransıyla tanımlanan biçiminden farklı bir **ikinci temas geometrisi**. Yeni adayın değeri, aynı olay evrenindeki bu ek geometrinin ve EMA200 kapısının marjinal katkısıdır; çıplak çift dip ayrı yeniden sayılmaz.

### AC150 — EMA200 yönünde gövde–fitil bölgesi teyitli çift dip/tepe

- **Veri ve ısınma:** BTC/ETH için tek borsadan gerçek **4h OHLCV**, UTC sınırları, en az 250 tam 4h bar ısınma. EMA200 kapanış fiyatından, `ATR14` Wilder TR'den hesaplanır. Hacim filtreye girmez. M1 gerçek fiyat yolu yalnız yürütme/çıkış için kullanılır; farklı fiyat serilerinden dolum yapılmaz.
- **Long yapı:** İlk dip barı `i`, iki sol ve iki sağ **tam kapanmış** 4h barla teyitli pivot low (`low[i]` çevresindeki dört low'dan küçük; eşitlikte eski pivot öncelikli). İkinci dip adayı `j`, `5 ≤ j−i ≤ 25`, aynı sağ/sol teyitli pivot low ve arada başka teyitli dip yok. İlk dip gövde altı `B_i=min(open[i],close[i])`. İkinci dip **bölgeye değmeli**: `low[j] ≤ B_i` ve ikinci mumun gövde altı `B_j=min(open[j],close[j])` için `low[i] ≤ B_j ≤ B_i`; böylece fitil ilk dibi süpürebilir, fakat gövde ilk fitil dibinin altına taşamaz. Aradaki boyun `N=max(high[i+1..j−1])`; `N−max(low[i],low[j]) ≥ ATR14[j]` (**bizim** sığ W elememiz). `i..t` aralığındaki her kapanış kendi EMA200'ünün üstünde olmalı; s. 23'teki “EMA200 altında kapanış yapmama”yı böyle somutlaştırdık. `j+2` kapanmadan ikinci pivot veya boyun olayı yok.
- **Long tetik:** `j+2` teyidinden sonraki en çok 10 tam 4h barda ilk `close[t] > N + 0.1 ATR14[t−1]` ve `close[t−1] ≤ N + 0.1 ATR14[t−2]` (**kırılım tamponu/pencere bizim**). Bu ana kadar `close < low[i]` veya EMA200 altı kapanış olursa kurulum iptal. `t` mumunun içindeki high kırılımı işlem sayılmaz. Aynı iki dip yalnız bir kez kullanılır. Short: teyitli iki tepe, ilk tepenin gövde üstü `B_i=max(open[i],close[i])`, `high[j] ≥ B_i`, ikinci gövde üstü `B_i ≤ B_j ≤ high[i]`, aradaki boyun `N=min(low[i+1..j−1])`, bütün kapanışlar EMA200 altında; ilk `close[t] < N−0.1 ATR` sonrası short. Eşzamanlı çelişkili kurulumda işlem yok.
- **Yürütme/risk:** Sinyal 4h kapanışından sonraki ilk uygulanabilir M1 açılışında, ücret ve kaymayla giriş. Long stop `min(low[i],low[j])−0.1 ATR14[t]`; short `max(high[i],high[j])+0.1 ATR14[t]`. Hedef **1,4R** (kaynak s. 15, 24–25'teki örnek; başarı oranı kanıtı değil). En çok **42 adet 4h bar** sonra süre çıkışı (**bizim**). Stop yanlış tarafta, hedef maliyeti karşılamıyor veya M1 veri boşluğu varsa atla. Aynı M1 barda stop ve hedef görülürse stop önce; funding, ücret, kayma ve başarısız dolum açıkça kaydedilir. Pozisyon büyüklüğü önceden sabit portföy risk tavanına göre hesaplanır, stop gerçekleşmesinin kesin fiyat garantisi olduğu varsayılmaz.
- **Ablation/eşdeğerlik:** Aynı iki pivot ve aynı 4h karar saatinde [R35](../batch_035/STRATEGIES.md) çıplak çift dip/tepe, yalnız gövde–fitil bölgesi, yalnız EMA200 ve ikisi birlikte karşılaştırılır; her kolda işlem sayısı, olay çakışması, net R, uzun/kısa ve rejim dağılımı raporlanır. 5–25 mum penceresi s. 3'te **kesin kural değil, öneri** olarak geçer; 4h kullanımı ve ATR tamponları bizim sabitlememizdir. Parametreler dış örneklem görülmeden dondurulmalı. EMA200 veya bu bölge mevcut özellik matrisinde eşdeğerse tekrar sütun açılmaz.

**Ertelenenler:** s. 6–19 omuz–baş–omuz “termination zone”u ile RSI aşırısı, önceki baş/omuz ve RSI adaylarının çoklu filtresi. Omuz/baş pivotlarının tek anlamlı seçim algoritması ve kaynakta çelişmeyen stop noktası olmadan ayrı aday sayılmadı. Kaynağın seçilmiş kazanç yüzdeleri bağımsız performans verisi değildir.

## 3. Kripto Para Grafikleri

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 8/Baskı 8/Kripto Para Grafikleri (27 sayfa) - @eseckal.pdf>) · [tam metin](03_crypto_charts.txt)

**Tam okuma:** s. 1–5 mum/doji/çekiç ve çift dip; s. 6–15 çift tepe, üçgen, baş/omuz, dikdörtgen, bayrak ve takoz; s. 15–24 MA/MACD/RSI/CCI/Bollinger/momentum/stokastik/hacim/SAR; s. 24–27 Fibonacci geri çekilme, fan ve zaman bölgeleri.

**Karar:** Formasyonların ve indikatörlerin standart anlatımı önceki adaylarla örtüşüyor. s. 22'de %K/%D duyarlılık tarifi karışmış; s. 23 hacim çubuğu rengi gerçek agresör yönü kanıtı değil; s. 24 SAR adım büyüklüğünün fiyat noktasını hangi yönde yaklaştırdığı anlatımı güvenilir uygulanabilir formül yerine geçmiyor. Fibonacci fan/zaman bölgeleri için pivot ve tetik nesnel verilmemiş. Yeni aday yok.

## Birikim

Bu parti sonunda **450 kitap, 150 rapor, 19.921 PDF sayfası ve 384 ayrı strateji adayı** kayıtlıdır. Adayların test edilmesi daha sonraki aşamadır.
