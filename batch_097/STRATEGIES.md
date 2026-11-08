# Kitap okuma 097 — seans VWAP ve gösterge teyidi

**Kapsam:** Daha önce tamamlanmamış üç PDF'nin **41 + 12 + 33 = 86 PDF sayfası** baştan sona okundu. Metinler sıralı olarak kaydedildi; kural ve grafik içeren 21 sayfa [görsel denetlendi](figure_contacts/). **Bir yeni strateji adayı** kaydedildi. Kaynak sayfaları PDF sayfalarıdır. Backtest, paper test ve emir yapılmadı.

## 1. Günlük Trading Stratejisi — Index Trader

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 18/Baskı 18/Günlük Trading Stratejisi - Türkçe ve İngilizce - Index Trader (41 sayfa) - @eseckal.pdf>) · [Tam metin](01_index_trader.txt)

**Sayfa haritası:** s. 1–21 Türkçe anlatım; s. 22–41 aynı yöntemin İngilizce tekrarı. VWAP tanımı/formülü s. 4–6/24–26, RSI(14) s. 9/29, ADX s. 10–11/30–31, M15 giriş kuralları s. 14–15/34–35, ATR(14) stop ve 2×ATR hedef s. 16–18/36–38, seçilmiş işlem grafikleri s. 19–21/39–41. İki dil **iki ayrı strateji sayılmaz**.

### IV97 — Seans VWAP yönünde RSI60/40 geçişi ve yükselen ADX

- **Kaynak çekirdeği:** Nifty futures 15 dakikada long: fiyat/VWAP üstü kapanış, RSI14'ün aşağıdan 60 üstüne geçmesi, ADX yükselmesi ve sinyal mumunun yüksek seviyesinden giriş; short için VWAP altı, RSI14'ün 40 altına geçmesi, yükselen ADX ve sinyal mumu dibi (s. 14–15, 34–35). Girişten 1×ATR14 stop ve 2×ATR14 hedef (s. 16–18, 36–38). ADX yön değil güç ölçer; kaynakta +DI/−DI koşulu yok. S. 18/38 short örneğinde `10300+23=10277` yazımı hem aritmetik hem stop yönü açısından hatalıdır; short stopu 10323 olmalıdır. Grafikler seçilmiştir, başarı kanıtı değildir.
- **Bizim nedensel M15 pilotumuz:** İşlem evreni baştan dondurulmuş, likit ve geçmiş üyeliği bilinen kripto perpetual sözleşmeleridir. Her UTC gün 00:00'da VWAP sıfırlanır; `VWAP[t]=Σ_UTC gün ((H+L+C)/3 × base_volume)/Σ_UTC gün(base_volume)`. Sıfır/eksik hacimde sinyal yok. `RSI14` ve `ADX14` Wilder RMA ile yalnız tamamlanmış M15 mumundan hesaplanır; en az 100 M15 ısınma barı. Long için `close[t]>VWAP[t]`, `RSI[t−1]≤60`, `RSI[t]>60`, `ADX[t]>ADX[t−1]`; short için `close[t]<VWAP[t]`, `RSI[t−1]≥40`, `RSI[t]<40`, yine ADX yükselişi. **UTC sıfırlaması ve kripto evreni bizim uyarlamamızdır**; Hindistan seansının mikro yapısı ile eşdeğer olduğu varsayılmaz.
- **Emir ve risk:** Sinyal M15 kapandıktan sonra alış stop `high[t]+tick` veya satış stop `low[t]−tick`; yalnız sonraki iki M15 mum süresince, ilk uygulanabilir M1 ask/bid ile dolabilir. Sinyal mumunun içinde işlem yok. Girişte `ATR14[t]` dondurulur; long stop `entry−ATR`, hedef `entry+2ATR`, short simetri. Aynı M1'de stop/hedef varsa stop önce; gap/kaymada gerçekleşebilir daha kötü fiyatı kullan. Dolmayan emir iptal; açık işlem 16 M15 bar veya UTC gün sonunda daha erken çıkışla kapanır. İki bar emir süresi, 16 bar süre çıkışı, tick tamponu ve günlük sıfırlama **bizim açık test seçimlerimizdir**. Bir sembolde aynı anda tek pozisyon; komisyon, spread, kayma ve funding net sonuçta dahil edilir.
- **Karşılaştırma:** VWAP tek başına, VWAP+RSI, VWAP+RSI+ADX ve önceki [VWAP/ADX adayları](../batch_043/STRATEGIES.md) aynı veri ve maliyetlerle karşılaştırılmalı. Sinyal örtüşmesi ve ek filtrelerin işlem sayısını/ne kadar net katkıyı değiştirdiği raporlanmadan bağımsız üstünlük iddia edilmez. Parametreleri sonuçlara bakarak seçme; ayrılmış dış örneklem kullan.

## 2. Ichımoku Hızlı Başlangıç Rehberi — Bob Joiner

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 18/Baskı 18/Ichımoku Hızlı Başlangıç Rehberi - Bob Joiner (12 sayfa) - @eseckal.pdf>) · [Tam metin](02_ichimoku_joiner.txt)

**Sayfa haritası:** s. 1–3 kapak/giriş; 4–6 Ichimoku çizgileri; 7 bulut ve ileri ötelenen Senkou A/B; 8 Tenkan/Kijun kesişimi; 9 Chikou; 10–11 bulut altındaki ayı kesişimi ve tarihsel fiyatla karşılaştırma örnekleri; 12 kapanış. İç kapakta yazar adı Robert C. Joiner yazıyor.

**Karar:** Tenkan/Kijun kesişimi, bulut konumu ve Chikou teyidi önceki [Ichimoku adaylarında](../batch_004/STRATEGIES.md) kayıtlı; kitap yeni bir giriş/stop/çıkış sistemi tanımlamıyor. S. 9 Chikou'yu bugünkü kapanışın **26 dönem ileri** izdüşümü diye tanımlar, ancak s. 10–11 geçmiş fiyat eğrisi ile kıyaslar. Bu zaman yönü tutarsızlığını aynen kodlamayacağız. Görünür bulut ve Chikou için grafikteki ileri/geri çizim yerini geçmişte elde bulunan veriyle karıştırmak lookahead üretir. Yeni strateji başlığı açılmadı.

## 3. Geçimini Sağlamak İçin Günlük Alım Satım — Leigh Vernon

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 18/Baskı 18/Geçimini Sağlamak İçin Günlük Alım Satım - Borsa Piyasasında Yön Bulmak İçin 5 Uzman Sistem - Leigh Vernon (Orijinal) (33 sayfa) - @eseckal.pdf>) · [Tam metin](03_five_systems_vernon.txt)

**Sayfa haritası:** s. 1–13 genel day trading ve süre stopu; 14–17 MA fiyat geçişi/geri çekilmesi; 18–19 MA15/50, SMA50/200 ve EMA50/100 çaprazları; 20–22 Turtle 20/55 gün kırılımı, 10/20 gün çıkışı, N tabanlı stop/piramitleme; 23–25 Williams %R ve ayrı bir SMA18 grafik örneği; 26–29 RSI20/80 ve 50 mum tepe/dibiyle karşı trend dönüşü; 30–33 psikoloji ve kapanış. Kapak OCR'da “9 Expert Systems” görünürken içindekiler ve son tanıtım “5 Expert Systems” der; yöntem sayısı içindekilere göre beştir.

**Karar ve tutarsızlıklar:** MA ve Turtle çekirdekleri [kanal kırılımı](../batch_003/STRATEGIES.md) ve mevcut MA ailesiyle tekrar. Turtle metni s. 21'de 20/55 gün giriş, 10/20 gün çıkış, 2N stop verir; özel bir yeni kural yok. Williams bölümünün s. 23 girişi SMA18 üzerindeki iki dip ve bar tepesi geçişini anlatır, s. 24–25 ise %R −80/−20 aşırılık sinyalini ayrı tarif eder; bunların zorunlu **birlikte** kullanılacağını söylemez. S. 24'te “stop alış fiyatının altında” mesafe vermediği için tam mekanik sistem değildir. S. 25'te hem aşırı alım üstüne hem altına geçiş için satış/alış denmesi yön bakımından belirsizdir. RSI bölümünün s. 27–29 50 mum ekstremumu, RSI≤20/≥80 ve sonraki mum kapanışı anlatımı, “ikinci low” ile “ilk low mumunun üstünde kapanış” sırasını netleştirmez; s. 28 stopu “mantıklı” 1–3 bar geriye koyar. Bu yön/olay belirsizliğini veri sonrası yorumlayarak yeni bağımsız sinyal saymıyoruz; mevcut [RSI aşırılık dönüşü](../batch_002/STRATEGIES.md) için kaynak notu olarak tutuldu. S. 22 getiri yüzdeleri denetlenebilir işlem kaydı ve maliyet içermiyor. Yeni başlık açılmadı.

**Sonraki adım:** IV97'yi önce veri yeterliliği, seans tanımı, M1 dolum ve geçmiş sembol evreni açısından denetle; sonra yalnız dış örneklem ve maliyetli backtest. Şimdilik sinyal veya kârlılık kanıtı yoktur.
