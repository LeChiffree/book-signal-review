# Kitap okuma 146 — İki mumluk orta nokta ile trend çıkışı

**Kapsam:** Üç ayrı PDF'nin **37 + 18 + 22 = 77 PDF sayfası** baştan sona incelendi. Falcon'un metin çıkarımında boş kalan [23. PDF sayfası](falcon_page23.png) ayrıca görsel kontrol edildi. Atıflar PDF sayfasıdır. Kaynaktan türetilen mekanik eşikler aşağıda açıkça **test varsayımı** olarak işaretlendi. Backtest, paper test ve emir yapılmadı.

## 1. Falcon Trading Teknik Analiz Kursu — Falcon Trading Guidance

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 5/Baskı 5/Falcon Trading Teknik Analiz Kursu (37 sayfa) - @eseckal.pdf>) · [Tam metin](01_falcon_course.txt)

**Tam okuma:** S. 1–6 giriş, psikoloji ve terimler; s. 7–12 “dürtüsel/düzeltici doğa” ve çoklu zaman dilimi trend çizimleri; s. 13–15 formasyon içinden riskli giriş ile kırılım sonrası giriş; s. 16–23 başa baş/yarı risk, yapı sonrası izleyen stop ve seçilmiş GBPUSD görseli; s. 24–27 kârda pozisyona ekleme; s. 28–30 EURJPY için 100 işlemlik yazarın kendi seçtiği geriye dönük istatistik; s. 31–36 günlük hedef çalışma sayfaları; s. 37 sonuç. Düzeltici hareketin sınırı, çizilen trend çizgisinin pivot seçimi ve “dürtüsel” hacim/aralık eşiği sabit verilmemiştir. S. 29'daki %81 isabet iddiasının işlem listesi, ücretler ve bağımsız dönem yoktur; bunu doğrulanmış sonuç saymayız. S. 20–21'deki başa baş/yarı risk uygulaması mevcut stop yönetimi varyantıdır; s. 24–27'de toplam açık risk üst sınırı portföy kontrolüdür. [Önceki bayrak/kırılım aileleri](../batch_016/STRATEGIES.md) yanında kaynakta yeni nesnel giriş tetikleyicisi yok. **Yeni aday: 0.**

## 2. Forex Trading Manifestosu — Maceo Jordan / Forex Jungle Guide

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 18/Baskı 18/Forex Trading Manifestosu (18 sayfa) - @eseckal.pdf>) · [Tam metin](02_forex_manifesto.txt)

**Tam okuma:** S. 1–6 psikoloji ve varsayımsal bileşik getiri tabloları; s. 7–8 arz/talep anlatısı; s. 9 ilk bar kapanışının kendi high–low orta noktası, sonraki barın önceki kapanış ve orta noktaya göre teyidi; s. 10–14 seans/haber zamanları ve haber sonrası 30/60 dakika ile 2/3/5 gün izlemesi; s. 15–16 hataları kaydetme; s. 17–18 kurs daveti. S. 4–5, 10–13'teki sabit aylık %6–22 senaryoları gerçekleşmiş performans değildir. S. 11'de büyük yatırımcıların “haber öncesi bilgi” kullandığı iddiası doğrulanmış veri değil; bu iddiadan sinyal kurulmadı. Haber fiyat boşluğu ve kayma, açıklama anı girişini ayrıca zorlaştırır.

### MJ146A — Trend pozisyonu için art arda iki zayıf orta nokta kapanışı

- **Kaynak çekirdeği:** Trend yönündeki bar kendi aralığının orta noktasında veya ötesinde kapanmazsa sonraki barı izle; sonraki kapanış da önceki kapanışın ve orta noktanın yön tarafında kalmazsa hareket sona erebilir (PDF s. 9). Bu **kesin satış emri değil**, mevcut pozisyon için uyarıdır. Aşağıdaki çıkış işlemi ve eşitlik durumları bizim test yorumumuzdur.
- **Kapanmış mum kuralı:** Ana deney EURUSD H4; önceden kayıtlı [LP145A girişleri](../batch_145/STRATEGIES.md) değişmeden kullanılır. Yalnız pozisyon açıldıktan **sonra tamamen oluşmuş** t ve t+1 H4 barları değerlendirilir. `mid[t]=(H[t]+L[t])/2`; sıfır aralıkta sinyal yok. Long uyarısı `C[t]≤mid[t]`; izleyen tamamlanmış bar t+1 için `C[t+1]≤C[t]` **ve** `C[t+1]≤mid[t]` ise çıkış sinyali. Short simetri: `C[t]≥mid[t]`, `C[t+1]≥C[t]` ve `C[t+1]≥mid[t]`. Aynı t+1 bar, bir sonraki ardışık çiftin ilk barı olabilir; yalnız ilk gerçekleşen çıkış kullanılır. Kaynağın “önceki orta nokta” sözü belirsizse bu sözleşme tek yorum olarak test öncesi sabittir; t+1'in kendi orta noktasını kullanmak ayrı duyarlılık koludur.
- **İcra/risk:** Sinyal t+1 H4 kapanınca sonraki ilk uygulanabilir bid/ask M1 kotasyonundan piyasa çıkışı. LP145A'nın ilk stopu, 2R hedefi, SMA100 ters kapanışı ve 60 H4 süre sınırı korunur; hangisi önce uygulanabilir zamana gelirse o çalışır. Stop/hedef mum içinde gerçekleşirse H4 kapanış uyarısı beklenmez. Spread, komisyon, swap ve kayma dahil; başlangıç pozisyon boyutu LP145A ile aynıdır. EURUSD likit seans/hafta sonu gapleri gerçek kotasyon zamanlarıyla işlenir.
- **Karşılaştırma/karar:** Aynı giriş işlemlerinde (1) LP145A temel çıkışı, (2) tek zayıf orta nokta mumunda çıkış, (3) bu iki bar teyidi; ücret sonrası getiri dağılımı, kârın erken kesilmesi, max drawdown ve stop sayısı kıyaslanır. Sonuçlar eşlenik işlem bazında ve tarihsel eğitim/dış örnek ayrımıyla raporlanmalı. Bu bir **çıkış modülü**dür, kendi başına long/short giriş sinyali değildir; ayrı kazanç iddiası yoktur.

## 3. Yapay Zeka ile Daha Akıllı Trading — Chris Miller

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 21/Baskı 21/Yapay Zeka ile Daha Akıllı Trading - Chris Miller (22 sayfa) - @eseckal.pdf>) · [Tam metin](03_ai_trading_miller.txt)

**Tam okuma:** S. 1–3 kapak/içindekiler; s. 4–13 yapay zekâ kullanımı ve risk kontrolü hakkındaki genel iddialar; s. 14–18 Deriv ve bir otomatik sinyal sağlayıcısının tanıtımı; s. 19–20 içerik pazarlaması/SEO; s. 21–22 sonuç/kaynakça. Model mimarisi, eğitim verisi, hedef değişken, zaman damgalı sinyal veya stop/çıkış formülü açıklanmadığından kapalı mumla yeniden üretilebilir sinyal yoktur. S. 5'teki %96 kayıp oranı kaynaksızdır; s. 11'de ensemble kullanmanın başarıyı artıracağı iddiası doğrulanmış dış örnek test değildir; s. 17 kullanıcı yorumları bağımsız kayıt değildir. Kitaptaki bağlantılı hizmet bu araştırmanın verisi veya test sistemi sayılmaz. **Yeni aday: 0.**

## Sonuç

**1 yeni araştırma adayı: MJ146A çıkış modülü.** Toplam **438 tamamlanmış ayrı kitap, 383 kayıtlı strateji adayı**. Adayın etkisi ancak eşlenik backtest ve sonra paper test ile görülebilir.
