# Kitap okuma 139 — Coppock döngüsü ve teyitli H4 pivot kırılımı

**Kapsam:** Üç ayrı PDF'nin **35 + 34 + 64 = 133 sayfası** baştan sona okundu. Sayfa numaraları PDF sayfasıdır. Backtest, paper test ve emir yapılmadı.

## 1. Bir Aylık Trade Bilgeliği Rehberi — Edward C. Turner

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 9/Baskı 9/1 Aylık Trade Bilgeliği Rehberi - Edward C. Turner (35 sayfa) - @eseckal.pdf>) · [Tam metin](01_turner_month.txt)

**Tam okuma:** S. 1–8 önsöz, işlem disiplini ve eğitim; s. 9 Hilbert sinüs dalgası; s. 10–18 psikoloji, swing/kanal ve demo; s. 19–26 risk/disiplin; s. 27 CCI; s. 28–32 işlem davranışı, Keltner(10–20, 1,5 ATR) ve MA79/EMA89; s. 33 aylık Coppock formülü ve giriş/çıkış; s. 34–35 eğitim ve Bollinger. S. 15'te **kurulum olmasa da öğlen gerçek işlem yap** önerisi araştırma veya risk kuralı olarak alınmaz. S. 33'teki geçmiş çöküş listesi seçilmiş gözlemlerdir, tam örneklem istatistiği değildir. Hilbert ve Keltner için bu kitap kesin kapanmış sinyal/stop vermez; önceki kanal ve osilatör aileleriyle örtüşür.

### EC139A — Aylık Coppock dip dönüşü ve çift tepe çıkışı

- **Kaynak:** S. 33, Coppock `WMA10(ROC14+ROC11)` aylık; sıfır altında çukurdan yukarı dönünce alım; arada sıfır altı olmadan iki tepe oluşturması pozisyonu kapama uyarısı. Kaynak esas olarak S&P 500 endeksi için anlatır. Formül ve yön kaynak, somut tepe tespiti ile risk sınırları bizim deney tanımımızdır.
- **Ön kayıt:** Likit, toplam getiri içeren endeks/ETF serisinde yalnız **tamamlanmış ay** kapanışlarıyla ROC14 ve ROC11 yüzde değişim, ardından 10 aylık ağırlıklı ortalama (en yeni aya 10, en eskiye 1 ağırlık). `C[t−1]<0`, `C[t−1]<C[t−2]` ve `C[t]>C[t−1]` ise t aylık kapanışında long olay. Bir açık pozisyon varken tekrar giriş yok. Çıkış için Coppock'ta `k=1` sağ/sol ayla ancak sonraki ay kapanınca teyitli iki yerel yüksek olsun; ikisi arasında Coppock hiç sıfır altına inmesin. İkinci tepe teyit kapanışında veya `C[t]<0` ilk kapanışında çık. Bu çift tepe algoritması bizim nesnelleştirmemizdir, kaynak sayısal tepe tanımı vermez.
- **Emir/risk:** Sinyalden sonraki ilk uygulanabilir işlem seansı açılışı; long stop, sinyal ayından önceki 6 tamamlanmış ayın en düşük low'u altında `0,1 ATR14_ay` (yoksa işlem yok); en çok 60 ay zaman çıkışı. Stop ve süre kaynağın kuralı değildir. Pozisyon boyutu stopa göre en çok %0,5 özsermaye riski, gapte gerçek açılış dolumu, ücret ve kayma dahil. Kriptoya aktarılırsa ayrı evren ve ayrı dış örneklem; kaynak performansı kripto kanıtı değildir.
- **Kıyas:** Aylık al-tut ve aylık MA10 rejimiyle aynı ETF/toplam getiri ve maliyet varsayımında karşılaştır; temettü, survivorship, 200 aylık warmup ve az işlem sayısını raporla. Aylık t tamamlanmadan Coppock değerini kullanma.

## 2. Yavaş ve İstikrarlı — Robert Glover

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 8/Baskı 8/Yavaş ve İstikrarlı - Robert Glover (34 sayfa) - @eseckal.pdf>) · [Tam metin](02_glover_slow.txt)

**Tam okuma:** S. 1–17 piyasa, demo/robot, stop ve spread; s. 18–25 USDJPY H4 dört sol/dört sağ pivot kırılımı, 2 pip giriş tamponu ve ayrı 10/15/20 pip stop/hedef; s. 26–29 Pazar/Cuma, haber fitili ve yuvarlak sayı engeli; s. 30–32 yeniden seçim ve örnek işlem sayıları; s. 33–34 kaynaklar. Dört sağ H4 barın kapanmasını bekleme kuralı pivotu **geriye boyamadan** test için belirleyicidir. Yazarın 189 işlemde günlere göre kazanma oranları (s. 27) yalnız kendi seçilmiş ve değişen örneklemidir; s. 31'de filtreler sonuçlara göre uyarlanmıştır, bu nedenle dış örneklem kanıtı değildir. Forex 2/10/15/20 pipleri kripto fiyatına aynen uygulanamaz.

### RG139A — H4 teyitli dört bar pivotunun tamponlu kırılımı

- **Kaynak:** H4 pivot high, hem önceki hem sonraki dört mumdan daha yüksek; low için ters. Pivot ucu +2 pip buy stop / −2 pip sell stop; 10, 15, 20 piplik ayrı stop/TP çiftleri (s. 20–24). Pazar/Cuma ve belirgin haber fitili elemesi (s. 26–29).
- **Bizim kripto test sözleşmesi:** H4 UTC mumunda merkez `p` high değeri `p−4…p−1` ve `p+1…p+4` high'larının hepsinden **katı büyük** olsun. Pivot ancak `p+4` kapanışında emre elverişli. Bu kapanıştan sonraki en çok 12 H4 bar geçerli buy stop `high[p]+0,1 ATR14_H4[p+4]`; short için simetri. ATR tamponu ve emir ömrü bizim ölçek uyarlamamızdır. Önceden bilinmeyen p+1…p+4 sırasında oluşmuş kırılım varsa aynı pivotu sonradan işlemeye çalışma.
- **Risk/çıkış:** Long stop, sabit `entry−1R` ve hedef `entry+1R`; `1R=max(0,5 ATR14_H4[p+4], entry−min(low[p−4:p+4]))` iki ayrı risk kolu olarak test edilsin, **en iyi sonucu sonradan seçme**. Short simetri. Hedef/stop, maliyet ve gerçek dolumla H4 içi M1 yolundan; aynı M1 mumundaki belirsiz sırada stop önce. Emir dolduktan en çok 12 H4 bar sonra zaman çıkışı. Risk en çok %0,5 özsermaye, ücret/kayma/funding dahil. 1R/ATR ve süre kripto uyarlamasıdır; kaynağın USDJPY pip stop/TP değerleri ayrıca gerçek FX verisi varsa birebir test edilebilir.
- **Kıyas:** [Mevcut pivot kırılımı ailesi](../batch_005/STRATEGIES.md) ile aynı H4 olay anahtarında karşılaştır. `k=4`, tampon ve Cuma/Pazar filtresinin ayrı katkısını ölç; kriptoda 7/24 olduğundan FX hafta sonu gerekçesi aynen geçerli sayılmaz.

## 3. Başarılı Hisse Senedi Ticareti — Nick Radge

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 9/Baskı 9/Başarılı Hisse Senedi Ticareti - Nick Radge (64 sayfa) - @eseckal.pdf>) · [Tam metin](03_radge_stock.txt)

**Tam okuma:** S. 1–20 beklenti, örneklem ve veri madenciliği; s. 21–31 sıkı/uzak stop, 1,5–2R'de başabaş, MA20–150 takip stopu ve kademeli ekleme; s. 32–40 düşük riskli üçgen/menzil giriş örneği ile frekans; s. 41–43 zihniyet; s. 44–55 sabit yüzdeli pozisyon boyutu, kayıp serisi, marj ve çeşitlendirme; s. 56 günlük aralık/fiyat “Bang for Buck” sıralaması; s. 57–64 sonuç ve iki stop simülasyonu tablosu. Bu kitap yeni yön tetikinden çok **mevcut kırılım adayları için yürütme varyantları** verir. Önceden sabitlenmiş dar stop ile geniş stop, MA takip stopu ve kademeli giriş ancak aynı ilk risk, ücret ve tüm stoplanan işlemler korunarak karşılaştırılmalı. S. 56'daki `200 günlük ortalama (high−low)/close` yalnız sermaye kısıtlı hisse portföyünde sıralama filtresidir; “beklenen günlük kâr” değildir, aşağı yön olasılığı ve işlem maliyeti yoktur. S. 22'de kâr faktörünü ters oranla tarif eder, s. 33'te doğru `brüt kâr/brüt zarar` kullanır; testte doğru tanım kullanılmalı. S. 27'de tek hisse/parametre tablosunun tüm piyasalara genellenmesi kanıt değildir. **Yeni bağımsız yön stratejisi sayılmadı.**

## Sonuç

**2 yeni araştırma adayı:** EC139A ve RG139A. Radge'nin risk/çıkış fikirleri mevcut adaylar için ayrı, önceden tanımlı deney kollarıdır.
