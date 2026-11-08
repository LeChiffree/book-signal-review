# Kitap okuma 211 — işlem katı anlatısı, pivotlar ve gün içi sistem tasarımı

Üç daha önce tamamlanmamış PDF'nin **714 sayfası** sayfa bazında metne çıkarılıp tarandı; işlem kuralı bölümleri ayrıca incelendi. **Yeni, bağımsız kapalı mum stratejisi adayı: 0.** Backtest, paper test ve emir yapılmadı. Sayılar PDF sayfasıdır.

## 1. John Sussex — Birinci Gün - Trader (184 sayfa)

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 11/Baskı 11/Birinci Gün - Trader - John Sussex (184 sayfa) - @eseckal.pdf>) · [tam metin](01_sussex_first_day.txt)

**Tam tarama:** S. 1–9 içindekiler ve önsöz; 10–75 Chicago/Londra işlem katı ve kişiler; 76–131 1987 çöküşü, bayi hikâyeleri ve pozisyon hataları; 132–176 iş yaşamı ve sonraki dönem; 177–184 fotoğraflar/kapanış. Önsöz s. 7 kitabın yatırımcıya işlem sistemi öğretmek için yazılmadığını açıkça belirtir. Anlatı, işlem katı emir akışı, büyük pozisyon ve risk kültürü açısından tarihsel bağlam verir; ölçülebilir OHLCV olayı, kapanmış mum giriş tetikleyicisi, stop ve çıkıştan oluşan bir kural sunmaz. S. 177–183 ağırlıkla fotoğraf/altyazı olduğundan metin kısa. **Yeni aday: 0.**

## 2. Ashwani Gujral — Grafiklerle Trade Yaparak Nasıl Para Kazanılır (261 sayfa)

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 11/Baskı 11/Grafiklerle Trade Yaparak Nasıl Para Kazanılır - Ashwani Gujral (261 sayfa) - @eseckal.pdf>) · [tam metin](02_gujral_charts.txt)

**Tam tarama:** S. 1–34 piyasa, grafik ve trend temelleri; 35–68 mum boyutu/reddedilme ve açılış; 69–103 günlük/haftalık pivot ve CPR; 104–131 trend geri çekilmesi ve stop/çıkış; 132–160 değişen piyasa koşulları; 161–183 haber ve sektör; 184–205 tuzaklar; 206–224 çoklu kanıt/örnekler; 225–261 risk, disiplin ve kaynakça. S. 85–94'te dar CPR ve trend günü, geniş CPR ve dönüş; s. 90–94'te gün içi CPR desteği; s. 187–204'te aralık dışına sahte taşma, düzeltme bitişi ve trend bitişi olmak üzere üç tuzak türü anlatılır. **Tekrar denetimi:** Dar CPR/kırılım ve CPR'ye dönüş [012. partide](../batch_012/STRATEGIES.md) ayrı olaylar olarak kayıtlıdır. Geri çekilme [001. partide](../batch_001/STRATEGIES.md), yanlış kırılım ve tuzak [023. partide](../batch_023/STRATEGIES.md) temsil edilir. Hindistan hisse açılışı/gap ve Nifty/Bank Nifty sektör örnekleri, 7/24 kriptoda gerçek borsa açılışı varmış gibi kodlanamaz. Haber/“katalizör” s. 161–183 ve 206–224, ayrıca nokta zamanlı dış veri olmadan yalnız mumdan üretilemez. Bazı grafiklerde “dev mum” veya “iyi kapanış” için evrensel eşik yoktur; seçilmiş kazanan örneklerden eşik öğrenmek ileriye bakma yanlılığı yaratır. Mevcut CPR sözleşmesinde CPR genişliği kantilleri ve eşik duyarlılığı, bu kitap için uygun ablation'dır; yeni strateji sayılmadı. **Yeni aday: 0.**

## 3. Markus Heitkoetter — Günlük Trading için Tam Kapsamlı Kılavuz (269 sayfa)

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 11/Baskı 11/Günlük Trading için Tam Kapsamlı Kılavuz - Markus Heitkoetter (269 sayfa) - @eseckal.pdf>) · [tam metin](03_heitkoetter_day_trading.txt)

**Tam tarama:** S. 1–90 gün içi işlemin gerekleri ve piyasa seçimi; 91–153 grafik, trend çizgisi, MA, MACD, Williams %R, RSI ve BB; 154–174 giriş, stop, hedef ve zaman stopu; 175–193 performans ölçümü/optimizasyon; 194–239 plan, psikoloji ve günlük disiplin; 240–269 ekler, sözlük ve kaynakça. S. 142–152'de 14/20 MA kesişimi ve BB dışına taşmada karşıt yönde işlem örnekleri, mevcut [MA kesişimi](../batch_006/STRATEGIES.md) ve [BB dönüşü](../batch_010/STRATEGIES.md) aileleridir. S. 170 önceki gün high/low seviyesini hedef, s. 171–174 bar ekstremumuyla takip stopu ve “işlem grafiğinin üç barı” kadar **zaman stopu** önerir; bunlar ayrı giriş olayı değil, mevcut adaylara çıkış varyantıdır. Önceki gün hedefi için hedefin giriş anında doğru tarafta ve en az net 1R uzakta olduğu ayrıca denetlenmelidir. S. 175–193'te Monte Carlo, kâr/zarar raporu ve geniş parametre platosu anlatılır; örnek optimizasyon veya %70 kazanma oranı güncel ve maliyet sonrası bağımsız sonuç sayılmaz. Kripto pilotuna aktarılacak çıkış ablation'ı: mevcut adayların aynı sinyallerinde stop/hedef gelmezse 3 sinyal zaman dilimi barı sonunda zorunlu çıkış; maliyet ve aynı mum içi stop/target sırası sabit. Bu mevcut adayın yürütme karşılaştırmasıdır. **Yeni aday: 0.**

**Parti sonucu:** 3 PDF, **714 sayfa**, **0 yeni aday**. Kümülatif **633 PDF, 46.086 sayfa, 444 doğrulanmamış aday**.
