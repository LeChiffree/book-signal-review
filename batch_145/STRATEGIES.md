# Kitap okuma 145 — SMA50/100 dönüşü ve ilk geri çekilme

**Kapsam:** Üç ayrı PDF'nin **44 + 6 + 45 = 95 PDF sayfası** baştan sona okundu. Atıflar PDF sayfasıdır. Kaynakta verilmeyen kesin pencereler ve maliyet/risk eşikleri aşağıda **bizim test varsayımlarımız** olarak belirtilir. Backtest, paper test ve emir yapılmadı.

## 1. ICT Order Block Trading — Derek Salvon

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 19/Baskı 19/ICT Order Block Trading - Derek Salvon (44 sayfa) - @eseckal.pdf>) · [Tam metin](01_ict_ob_salvon.txt)

**Tam okuma:** S. 1–7 Bollinger M5 scalp anlatımı; s. 8–18 OB tanımı, HTF bölge ve LTF ret; s. 19–25 emir akışı ile haftalık yön/H4 OB, Fibonacci %50 ve 1:1 risk/ödül; s. 26–34 üç mum FVG, seans/likidite süpürmesi ve FVG dönüşü; s. 35–40 kill zone saatleri ve DST; s. 41–44 Fibonacci/OTE. Bollinger bantlarında yön tersine dönmesi, [mevcut BB adayları](../batch_001/STRATEGIES.md) ile çakışır. Haftalık yön + iskontolu OB %50 geri gelişi, [mevcut OB/FVG ailesinin](../batch_005/STRATEGIES.md) filtre ve uygulama varyantıdır. FVG s. 26–34 aynı süpürme→FVG dizisidir. S. 3–6'da destek ve “üst bantta long” anlatımı kendi içinde tutarsız; seçilmiş işlemler performans kanıtı değildir. S. 18/22'deki 1–5 ve 10–15 pip stop tamponları aynı stratejiye farklı verilir. S. 19 DOM verisi fiyat mumundan kurumsal emir görüldüğünü kanıtlamaz. S. 39'da Londra kapanış saatleri kendi içinde farklıdır; seansları uygulanabilir takvimle ayrıca doğrulamak gerekir. **Yeni aday: 0.**

## 2. İndikatörleri Birleştirerek Geliştireceğin Güçlü Stratejilerle… — Long Pham

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 20/Baskı 20/İndikatörleri Birleştirerek Geliştireceğin Güçlü Stratejilerle _80_e Varan Kazanç Elde Et - Long Pham (6 sayfa) - @eseckal.pdf>) · [Tam metin](02_indicators_pham.txt)

**Tam okuma:** S. 1 kapak; s. 2–3 H4/D1 orta trend, SMA100 yön ve önceki swing tepe/dip kırılması; s. 3–4 SMA50/SMA100 kesişimi ve SMA50'ye ilk geri çekilme, eski dip/tepe stopu; s. 5 destek/direnç ve SMA100 izleyen stop, seçilmiş 2014–2015 EURUSD örneği; s. 6 ZigZag(12,5,3) çizimi ve boşluk yorumu. Başlıktaki “%80” ve seçilmiş tek işlem sonucu bağımsız başarı kanıtı değildir. ZigZag'ın son noktası yeniden çizilebildiğinden sinyal için **kullanılmayacak**; teyitli pivot gerekir.

### LP145A — SMA100 ve eski swing kırıldıktan sonra SMA50/100 kesişimi ile SMA50 ilk retesti

- **Kaynak çekirdeği:** H4 veya D1 EURUSD'de fiyat SMA100 tarafına geçip eski swing tepe/dibi kırar; SMA50 de SMA100'ü aynı yöne keser; fiyat SMA50'ye çekilip ana trend yönüne dönerse giriş (PDF s. 3–4). Kaynak trend içinde SMA100'e dönüşte eklemeyi ayrı bir fırsat sayar (s. 4), fakat yeni pozisyon ana sinyaline karıştırılmadı. Son swing karşı tarafı stop, sonraki direnç/destek veya SMA100'e göre izleyen stop s. 4–5.
- **Veri ve kapanış sinyali:** Ana pazar EURUSD spot H4; broker zaman damgası ve haftalık açılış/kapanış takvimi sabit, alış/satış kotasyonları gerekli. SMA50/100 kapanış üzerinden, en az 120 kapanmış H4 bar. Pivot high/low, merkez barın iki önce ve iki sonraki barın high/low'unu aşmasıyla tanımlanır ve yalnız **iki sağ bar kapanınca** bilinir. Long kurulum başlangıcı t'de `C[t]>SMA100[t]`, `C[t]>son teyitli pivotHigh` ve `SMA50[t]>SMA100[t]` iken `SMA50` kesişimi t veya önceki en çok 5 barda aşağıdan yukarı olmuş olsun; kurulumdan önce kullanılan pivot high kesinleşmiş olmalıdır. Short simetrik. Bu beş bar ve pivot yarıçapı bizim sabit seçimimizdir; kaynak aynı anda yakınlaşmayı anlatır, sayısal pencere vermez.
- **İlk retest/giriş:** Kurulumdan sonraki ilk en çok 12 H4 barda long `low≤SMA50[t]` ve aynı bar `close>SMA50[t]`; short `high≥SMA50[t]` ve `close<SMA50[t]`. Bu retest mumu kapanmadan giriş yok. Kurulumla retest arasında SMA50/100 sırası veya SMA100 yön tarafı kapanışla bozulursa iptal. İlk retest dışındaki temaslar aynı kurulumda yeni işlem üretmez. Sonraki ilk uygulanabilir ask/bid kotasyonundan long/short. H4 bar içi stop/target sırası için M1 kotasyon, yoksa ihtiyatlı stop önce senaryosu gerekir. Retest eşiği ve 12 bar penceresi bizim uygulanabilir yorumumuzdur.
- **Risk/çıkış:** Long stop, sinyalden **önce teyit edilmiş** son pivot low altına `0,1×ATR14_H4`; short son pivot high üstüne aynı tampon. Stop girişin doğru tarafında değilse işlem yok; kurulumdan sonra teyit edilecek dip stop için geçmişe taşınmaz. Hedef sabit 2R; H4 kapanışı SMA100'ün ters tarafına geçerse sonraki kotasyonda çık; en geç 60 H4 barda süre çıkışı. Kaynak yakın direnç/destek hedefi ve SMA100 stopu anlatır, 2R/60 bar/ATR tamponu bizim ön kayıtlı alternatifimizdir. Başlangıçta en çok %0,25 hesap sermayesi riski, kaldıraçsız eşdeğer miktar; spread, komisyon, rollover ve kayma dahil.
- **Karşılaştırma:** Aynı EURUSD/H4 dönemlerinde çıplak SMA50/100 kesişimi, yalnız SMA100+teyitli pivot kırılımı ve SMA50 retesti olmadan kesişim+fiyat kırılımı. Ayırt edici hipotez **üç olayın sırası ve ilk SMA50 geri çekilmesi**dir; önceki MA geri çekilmesi ve [EMA50/100](../batch_025/STRATEGIES.md) adaylarına karşı sinyal örtüşmesi ile net katkı ölçülmeli. Parametreler eğitim dışı döneme bakılarak seçilmez; farklı broker kotasyonları ve dönemler ayrı raporlanır. Henüz hiçbir sonuç ölçülmedi.

## 3. Forex Trading: Dinamik Bir Pazarda Başarı İçin Stratejiler ve Taktikler — Kyle W. James

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 26/Baskı 26/Forex Trading - Dinamik Bir Pazarda Başarı İçin Stratejiler ve Taktikler - Kyle W. James (45 sayfa) - @eseckal.pdf>) · [Tam metin](03_forex_james.txt)

**Tam okuma:** S. 1–10 Forex/merkez bankası/terimler; s. 11–18 plan ve hedefler; s. 19–24 stop, boyut ve psikoloji; s. 25–29 destek/direnç, MA, RSI, Fibonacci, Gann ve diğer araçların adları; s. 30–35 makro veri; s. 36–45 psikoloji ve genel sonuç. Somut gösterge periyodu + giriş + çıkış birlikteliği vermez. S. 6 faiz artışının dövizi daha az cazip kılacağı, s. 7 daha cazip kılacağı yazıldığı için kendi içinde çelişir; makro anlatıdan otomatik yön kuralı alınamaz. S. 21'de yüksek risk/ödül oranının “daha fazla risk gerektirmesi” de oran tanımından çıkmaz. İşlem planı ve veri zamanı yönetimi faydalı uygulama notlarıdır; yeni kapalı mum sinyali değildir. **Yeni aday: 0.**

## Sonuç

**1 yeni araştırma adayı: LP145A.** Toplam **435 tamamlanmış ayrı kitap ve 382 kayıtlı strateji adayı**. Bu, ileri test için bir hipotezdir; kârlılık sonucumuz yoktur.
