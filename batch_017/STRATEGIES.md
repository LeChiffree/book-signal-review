# Kitap okuma 017 — H4 sahte kırılım, haftalık rotasyon, günlük aşırılık

**Kapsam:** Üç PDF'nin **108 + 23 + 153 = 284 PDF sayfası** işlendi. Referanslar PDF sayfasıdır. “30 Dakikalık Hisse Senedi Traderi” **M30 grafiği değil**, günde yaklaşık 30 dakika çalışma fikridir. Kaynak örnekleri ile bizim kriptoya çevirdiğimiz test kuralları ayrı yazıldı. Bu partide backtest, paper test veya emir yapılmadı.

## 1. Heikin Ashi Trader — 4 Saatlik Grafik Kullanarak Swing Trading

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 14/Baskı 14/4 Saatlik Grafik Kullanarak Swing Trading - Heikin Ashi Trader (108 sayfa) - @eseckal.pdf>)

PDF üç bölüm içeriyor: H4 swing kurulumları (s. 4–36), **sahte kırılım/fakeout** (s. 37–66) ve stop yönetimi (s. 67–108). Destek/direnç, çift dip/tepe, çoklu temas sonrası kırılım ve bayraklar ilk bölümün örnekleri (s. 18–28). Ana sınanabilir katkı, dar aralıktaki seviyenin dışına çıkıp tekrar içine dönen fiyatı ters yönde işlemektir (s. 39–40, 47–48). Kaynak en az iki seviye teması, sahte mum ekstremumu ötesi stop, karşı aralık sınırı hedef ve en az 2R fırsat ister (s. 47–48). “Büyük oyuncu stop avı” yorumu OHLCV ile doğrulanmış emir akışı değildir. H4'te **altı mum/24 saat** sonra hâlâ kârda olmayan pozisyonun riskini azaltma fikri s. 83–85; kesin otomatik emir kuralı verilmez. Heikin Ashi görsel mumları gerçek fiyatın H/L'siyle karıştırılmamalı: emir, stop ve dolum ham OHLC/1m üzerinden.

### H17 — Önceden belirli H4 aralığında başarısız sınır kırılımı

- **Bizim aralık tanımı:** Son 16 tamamlanmış H4 mumun `R=max(high), S=min(low)`. `R-S <=4 ATR14_H4[t-1]` ve her sınırın `0.2 ATR` çevresinde en az iki ayrı H4 temasının bulunması; sınırlar olay mumu başlamadan dondurulur. `16`, `4 ATR` ve `0.2 ATR` bizim nesnelleştirmemiz, kaynak yalnız yatay dar aralık ve en az iki temas der. Aynı mum iki sınırı aşarsa bazda işlem yok.
- **Tetik:** Short `high[t]>R+0.1 ATR14_H4[t-1] && close[t]<R`, long `low[t]<S-0.1 ATR && close[t]>S`; mum gövdesi `<=0.5×(high-low)` ve kırılım tarafı fitil `>=gövde` daraltılmış varyant. Tetik **H4 kapandıktan** sonraki ilk 1m giriş. Stop sahte mum ekstremumu `±1 tick`; karşı aralık sınırı ilk hedef, girişte net potansiyel `<2R` ise kaynak filtresine göre işlem yok. 2R sabit hedef ayrıca. Bu olay batch 011 DP11a ve önceki false-break adaylarıyla aynı işlem olabilir; **çift kâr** sayılmaz. Heikin Ashi renk değişimi ayrı filtre ablation; ham OHLC'den türetilmiş HA kapanmış H4 mumunda hesaplanır.
- **Zaman/risk varyantı:** Altı H4 kapanışından sonra fiyat girişe göre kârda değilse pozisyonu tamamen kapatma veya yarıya indirme ayrı deney. Kaynak yalnız azaltmayı düşün der; `6 bar` örnek verir, tam çıkış bizim algoritmamız. Stop maliyete çekilmişse ücret/kayma sonrası sıfır P&L varsayılmaz.

## 2. 15 Dakikalık Turbo Forex Trading Kursu

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 18/Baskı 18/15 Dakikalık Turbo Forex Trading Kursu (23 sayfa) - @eseckal.pdf>)

Kitap kısa Forex tanıtımı, seans açıklaması, 2011 haberine dayanan tek **sonradan seçilmiş** işlem örneği, platform/kopya işlem reklamları içeriyor (s. 2–21). Adındaki “15 dakika”, **M15 grafik ve kesin tetik** anlamına gelmiyor. S. 8'de Euro haberi sonrası açılan kısa pozisyon için nesnel haber skoru, giriş anı, stop/iptal yok; s. 9 ve 19–23'te kopyalanacak trader seçimi için veriye bağlanabilir kriter yok. S. 11 çoklu zaman dilimi eğilim kontrolü söylüyor ama sayısal kural vermiyor. S. 7'deki stop kullanılırsa kaybın yatırılan tutarı asla aşmayacağı ifadesi kaldıraç/kayma koşullarında genel güvence değildir. **Bu kaynaktan bağımsız, kapalı mumla üretilebilir yeni işlem stratejisi çıkarılmadı.** Çoklu zaman dilimi kontrolü batch 011 G7 ve batch 015 F15b gibi sistemlerde zaten temsil ediliyor. Kitabı sırf üçlü sayısını doldurmak için uydurma M15 sinyaliyle kodlamıyoruz.

## 3. Laurens Bensdorp — 30 Dakikalık Hisse Senedi Traderi

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 16/Baskı 16/30 Dakikalık Hisse Senedi Traderi - Finansal Özgürlük İçin Stresiz Trading Stratejisi - Laurens Bensdorp (153 sayfa) - @eseckal.pdf>)

Kitap girişten çok **evren, sıralama, çıkış ve sermaye tahsisi** sözleşmesini ayrıntılandırıyor (s. 68–82). Üç mekanik çekirdek: S&P 500 içinden haftalık momentum rotasyonu (s. 83–86), sert düşmüş hisselerin günlük mean reversion long'u (s. 99–104), hızlı yükselmiş hisselerin kısa versiyonu (s. 114–116). Kaynak hayatta kalan hisseleri seçmeme ve listeden çıkanları da veri evrenine alma gereğini açıkça söylüyor (s. 84, 100). ABD hisse evreni, SPY rejimi, piyasa açılışı/hafta sonu ve sert gap riski kriptoya birebir geçmez. Kaynağın raporlanan getiri/Sharpe/CAGR'si kitap içi backtesttir; veri ve kod olmadan bağımsız doğrulama sayılmaz.

### B17a — Haftalık momentum rotasyonu

- **Kaynak:** SPY `close > 0.98×SMA200` rejiminde, 3 günlük RSI `<50` olan S&P 500 hisseleri arasından **200 günlük ROC** en yüksek ilk 10'u seçer; cuma kapanışından sonraki ilk piyasa açılışında alır. Her hafta ilk 10 dışına düşeni değiştirir; stop yok veya isteğe bağlı %20 (s. 84–86). 10 eşit sermaye dilimi. Bu bir **portföy stratejisi**, tek coin işareti değil.
- **Bizim kripto D1/W1 sözleşmesi:** Her UTC pazar 23:59 günlük/haftalık kapanıştan sonra, yalnız o anda işlem görülebilen ve son 20 tam günde önceden belirli işlem hacmi eşiğini karşılayan coinler. Rejim BTC `close >=0.98×SMA200_D1`; seçim her coin `RSI3_D1<50`, `ROC200_D1=(close[t]/close[t-200]-1)`, ilk 10. Karar sonrası ilk 1m giriş/çıkış; haftalık aynı anda eşit hedef nominal ağırlık, her hafta ilk 10 dışına düşeni çıkar. Borsaya yeni giren coin 200 günlük geçmiş tamamlamadan aday değil, delisted coinleri veri setinden silme. Kaynak SPY yerine BTC, cuma yerine UTC pazar **bizim** uyarlamamız. Stopsuz bazın açık riskini raporla; %20 stop ayrı, işlem büyüklüğü ve portfolio drawdown/margin/funding sınırları konmadan paper'a geçme. Batch 013 L13c göreli güç filtresiyle örtüşme ve turnover ölçülür.

### B17b — Günlük aşırı satımda ek düşüşe limit alım

- **Kaynak:** `close>SMA150_D1`, `ADX7>45`, `ATR10/close>4%`, `RSI3<30`; en düşük RSI'lı en çok 10 hisse. Ertesi gün önceki kapanışın **%4 altında buy limit**. Dolum sonrası `2.5×ATR10` stop, `>=3%` kârda ertesi açılışta çıkış veya 4 gün sonunda zaman çıkışı (s. 99–104). Kaynak dolum gününde **stop koymuyor** (s. 103); bu yoğun gap riskine sebep olabilir. %2 hesap riski ve %10 nominal pozisyon tavanı anlatılır (s. 100–101).
- **Bizim kripto D1 uygulaması:** UTC gün `t` kapanınca filtreler, `t+1` gününe `limit=0.96×close[t]`; 24 saat dolmazsa iptal. **Dolum anında** `stop=fill-2.5 ATR10_D1[t]` koruyucu emir; fiyat `<=0` üretiyorsa aday atlanır. Pozisyon boyu `min(risk_budget/stop_distance,0.10 equity/fill)`; kaynak ilk gün stopsuz olsa da bu bizim paper öncesi risk uyarlamamız, sonuçlar ayrı raporlanmalı. Hedef `fill×1.03`; ilk 1m temasında kâr alma baz, kaynağın ertesi piyasa açılışı davranışıyla eşdeğer değil. Dört tam UTC gün sonra kapanış çıkışı. Kaynak filtreleri USD hisse fiyat ölçeğinden gelir; kriptoya geçerliliği test edilmeden varsayılmaz. Batch 006 RSI pullback/mean reversion ile aynı olaylar etiketlenir.

### B17c — Günlük aşırı alım sonrası kısa

- **Kaynak:** `ADX7>50`, `ATR10/close>5%`, son iki gün yükseliş mumu, `RSI3>85`; en yüksek RSI'lı en çok 10 hisse. Ertesi açılıştan önce önceki kapanış fiyatına short limit; dolum sonrası `2.5 ATR10` stop, `>=4%` kârda ertesi açılışta çıkış veya iki gün zaman çıkışı (s. 114–116). SMA filtresi **yok**. Kaynak ilk gün stop kullanmıyor.
- **Bizim D1 sürüm:** Önceki tam UTC gün kapanışından sonra kaynak göstergeleriyle short limit `close[t]` bir sonraki UTC gün geçerli. Fiyat zaten limitin üstündeyse ilk 1m uygulanabilir fiyatıyla dolum; limit emir koşulu ve maker/taker maliyeti açıkça raporlanır. Dolumda `stop=fill+2.5 ATR10_D1[t]`, `target=fill×0.96`; en geç iki tam UTC gün sonunda çıkış. Tek coin toplam riski, %10 nominal tavan, borrow/funding ve tasfiye modeli zorunlu. Spotta short açılabiliyormuş varsayma; uygun perp evreni ayrı. Uzun B17b ile portföyde eşzamanlı açık risk birleştirilir.

## Test kararı

H17 önceki failed-break kurallarıyla örtüşme deneyi; B17a gerçek portföy ve evren bakımından ayrı pilot; B17b/c yüksek oynaklık ve limit dolumu etkisi nedeniyle yalnız maliyet/gap modeliyle değerlendirilir. Tümünde kapanmış veriler, 1m dolum, sabit ön seçim evreni, delisting, ücret, spread/kayma, funding, net R ve dış örneklem gerekir. M15 Turbo'dan yeni sinyal yok.
