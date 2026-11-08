# Kitap okuma 188 — başarısız kırılımın ikinci dönüşü ve üç kısıtlı boyutlandırma

Üç PDF'nin **513 sayfası** sayfa bazında metne çıkarılıp baştan sona tarandı; kural sayfaları ayrıca ayrıntılı okundu. **1 yeni doğrulanmamış işlem stratejisi adayı** ve **1 yeniden kullanılabilir risk kuralı** kaydedildi. Backtest, paper test ve emir yapılmadı. Sayfalar PDF sayfasıdır.

## 1. Airforexone — Gelişmiş Price Action Tekniği (364 sayfa)

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Gelişmiş Price Action Tekniği (364 sayfa) - @eseckal.pdf>) · [tam metin](01_advanced_price_action.txt)

**Tam okuma:** S. 1–37 FX/araç/grafik temelleri; 38–60 piyasa yapısı; 61–96 mum, seviye, MA ve trend çizgisi; 97–127 klasik formasyonlar; 128–151 Fibonacci; 152–183 mum formasyonları; 184–208 trend/geri çekilme ve birleşim; 209–235 risk/çıkış; 236–259 makro ve korelasyon; 260–293 arz-talep ve hacim profili; 294–319 tuzaklar; 320–364 süreç ve psikoloji. S. 185–206 kırılım, geri çekilme ve 0,618 birleşimi; s. 294–301 stop süpürmesi ve s. 313–319 çift tepe/dip tuzağı önceki aday aileleriyle örtüşür. S. 302–308'deki *Catch–Pain–Release* (CPR), merkez pivot aralığı CPR'siyle karıştırılmamalıdır. Kurumsal manipülasyon ve yüksek başarı anlatısı doğrulanmış neden/performans değildir.

### AFX188A — başarısız kırılım, uzaklaşma ve eski kırılım düzeyine ikinci retest

- **Kaynak (s. 302–308):** Konsolidasyon sınırı kırılır, fiyat geri dönüp kırılımı boşa çıkarır (*catch*), eski sınırdan uzaklaşıp ters tarafta zaman geçirir (*pain*), sonra ilk kırılım seviyesine yeniden çıkar ve tekrar reddedilir (*release*). Kaynak s. 304 kısa yönde stopu dönüş zirvesinin yaklaşık 15 pip üstüne, hedefi önceki düşük seviyelere koyar. Aşağıdaki pencere ve eşikler **bizim ön kayıt tanımımızdır**; kitabın kesin parametreleri değildir.
- **Veri/kurulum:** EURUSD gerçek H1 bid/ask OHLC ve tarihsel spread. Tamamlanmış son 12 H1'in `U=max(high)`, `L=min(low)` aralığı `≤2×ATR14_H1` ise konsolidasyon; aralık, kırılım mumu başlamadan önce dondurulur. Yalnız H1 kapanışında `close>U` yukarı kırılımı veya `close<L` aşağı kırılımı kaydet; aynı aralık için ilk kırılım. Aşağıdaki short tanımının long simetriğini de test et. Kırılım `close>U` sonrası en geç 3 tamamlanmış H1'de `close<U` olmalı (*catch*). Ardından en az 3 H1 kapanışı `U` altında ve bu evrede en az bir `low<L−0.5×ATR14` olmalı (*pain*). ATR yalnız kırılım öncesinde bilinen değerle sabitlenir.
- **Sinyal/icra:** Catch sonrasındaki en çok 24 H1'de fiyatın `U` düzeyini yeniden görmesi ve tamamlanan retest H1'inin `close<U` ve `close<open` olması short sinyali. Retest sayılan mum, pain için sayılan son mumdan sonra gelmeli; tek H1 içinde hem uzaklaşma hem retest sırası varsayılmaz. Sonraki ilk uygulanabilir bid'den short. Long için `L` altına kırılım/geri dönüş, `U+0.5ATR` üstüne uzaklaşma, `L` yeniden temas ve `close>L`, `close>open` simetrisi. Aynı konsolidasyon yalnız bir işlem üretir. Kaynağın öznel konsolidasyon/acı süresi bizim `12/3/24` H1 ve `0.5ATR` eşikleriyle mekanikleştirilmiştir.
- **Çıkış/risk:** Short stop `max(ilk kırılım high, retest high)+1 pip`, long stop karşı minimum `−1 pip`; hedef pain evresinin en düşük/yüksek seviyesi. Hedef doğru yönde en az `1R` değilse işlem yok. 24 H1 sonra zorunlu çıkış. İşlem başına özsermayenin en çok `%0,25`i stop riski; komisyon, spread, swap ve kayma dahil. Stop/target ve zaman sınırı kaynakta tam verilmediğinden test sözleşmesidir; kaynak 15 pip örneği ayrı duyarlılık kolu olabilir.
- **Ayırıcı sınama:** İlk başarısız kırılım kapanışında doğrudan giriş, ilk retest olmadan ters yön, standart range false breakout ve pain süresi `0/3/6` H1 kollarını aynı dönem ve maliyetlerle karşılaştır. Retest öncesi bilgiyle seviye dondurulmalı; sonra oluşan ekstremumları geriye dönük sınır seçmek için kullanma. İşlem sayısı, net R, maksimum düşüş ve dönem dışı stabilite raporlanmalı.

## 2. Harneet Singh Kharbanda — Bir Keşiş Gibi Trade Yap (74 sayfa)

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Bir Keşiş Gibi Trade Yap - Harneet Singh Kharbanda (74 sayfa) - @eseckal.pdf>) · [tam metin](02_trade_like_monk.txt)

**Tam okuma:** S. 1–13 açılış öyküsü/duygu; 14–28 plan, aşırı işlem ve günlük; 29–46 trader görüşmeleri ve Nifty 15m vaka anlatısı; 47–74 görüşmeler, disiplin ve kapanış. S. 37–44'teki Nifty örneği seçilmiş ve yorum ağırlıklıdır; evrensel eşik/çıkış kuralı vermez. S. 15'te giriş, çıkış ve büyüklüğü önceden yazma; s. 26–27'de günlük tutma yararlı süreç kurallarıdır, bağımsız kapalı mum sinyali değildir. **Yeni aday: 0.**

## 3. Tom Basso — Başarılı Yatırımcılar Pozisyonlarını Neden ve Nasıl Boyutlandırıyor (75 sayfa)

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Başarılı Yatırımcılar Pozisyonlarını Neden ve Nasıl Boyutlandırıyor - Tom Basso (75 sayfa) - @eseckal.pdf>) · [tam metin](03_position_sizing_basso.txt)

**Tam okuma:** S. 1–18 giriş, sistem ve ilk risk; 19–27 stop mesafesine göre risk büyüklüğü; 28–37 ATR ile volatilite sınırı; 38–43 sermaye/marj sınırı ve üçünün minimumu; 44–50 özsermaye/kontrat tablosu; 51–61 açık pozisyonun yeniden dengelenmesi; 62–69 portföy risk limiti; 70–75 sonuçlar. S. 25'teki kanal kırılımı yalnız örnek al/sat motorudur ve önceki Donchian ailesini tekrarlar. Kitap yeni bağımsız giriş sinyali vermez. **Yeni işlem adayı: 0.**

### BB188R — backtest/paper test için üç kısıtlı pozisyon büyüklüğü (strateji sayısına dahil değil)

- **Kaynak:** S. 19–21 stop riskine göre `equity×riskPayı / birimStopKaybı`; s. 29–32 ATR21 ve `equity×volPayı / birimATRDeğeri`; s. 38–41 sermaye/marj payı ve bu üç miktarın minimumu. S. 51–65 pozisyon açıkken risk/volatilite ve toplam portföy riskini yeniden ölçüp limiti aşınca azaltma. Kaynak yeni başlayan için `%0,5` tek pozisyon riskini, örnekte `%1` risk, `%0,75` volatilite, `%5` sermaye/marj kullanır; bunlar performans garantisi değildir.
- **Uygulama sözleşmesi:** Her aday stratejinin giriş sinyali kapandıktan sonra `q=floor(min(0.005E / (|entry−stop|×pointValue+estimatedCost), 0.005E / (ATR21_D1×pointValue), 0.05E / initialMarginPerUnit))`; spot hisse için üçüncü payda hisse giriş fiyatı. `E` karar anındaki özsermaye, ATR yalnız son kapanmış D1 verisi, marj o anda geçerli kontrat şartı. `q<1` ise işlem yok; stop emri garantili dolum sayılmaz. Kaynaktaki ATR güncelleme yazımı s. 31'de eksik/yanıltıcı göründüğünden testte standart `ATR_t=ATR_(t−1)+α(TR_t−ATR_(t−1))`, `α=2/22` açıkça sabitlenir. `%0,5` vol ve `%5` marj, bizim muhafazakâr ön kayıt seçimimizdir.
- **Ayırıcı sınama:** Her stratejide aynı sinyal/çıkışla yalnız stop riski büyüklüğüne karşı üçlü minimumu karşılaştır; net getiri, max drawdown, reddedilen emir sayısı ve sermaye kullanımını raporla. Birden çok açık pozisyonda stop kayıpları toplamı için ayrıca portföy tavanı koy; eş zamanlı gap ve korelasyon nedeniyle bu tavan gerçek kaybın üst sınırı değildir.

**Parti sonucu:** 3 PDF, **513 sayfa**, **1 yeni doğrulanmamış işlem adayı**; ayrıca 1 risk kuralı. Kümülatif **564 PDF, 30.809 sayfa, 429 işlem adayı**.
