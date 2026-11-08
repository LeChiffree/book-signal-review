# Kitap okuma 186 — SMA50 ve ATR3 ile çift eşikli H1 yön değişimi

Üç yeni PDF'nin **357 sayfası** metne çıkarılıp sayfa bazında baştan sona tarandı; kural sayfaları ayrıca ayrıntılı okundu. **1 yeni doğrulanmamış strateji adayı** kaydedildi. Backtest, paper test ve emir yapılmadı. Sayfalar PDF sayfasıdır.

## 1. Jim Berg ve John Atkinson — Online Trading ve Yatırımın 10 Sırrı (88 sayfa)

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 10/Baskı 10/Online Trading ve Yatırımın 10 Sırrı - Jim Berg ve John Atkinson (88 sayfa) - @eseckal.pdf>) · [tam metin](01_ten_secrets_berg.txt)

**Tam okuma:** S. 1–8 kapak/içindekiler/giriş; 9–17 2008 ayı piyasası ve zamanlama; 18–25 “kanıt ağırlığı” ve seçilmiş hisseler; 26–31 kriz portföyü; 32–40 işlem planı; 41–48 risk/pozisyon büyüklüğü; 49–56 portföy ve stop psikolojisi; 57–62 trailing stop örnekleri; 63–69 trend/volatilite ve seçilmiş hisse örnekleri; 70–83 bültenin notional işlem günlüğü; 84–88 kapanış/tanıtım. S. 20'deki “B-Sekiz-Kanıt”, s. 66–68'deki özel “JB Mavi Çubuk Volatilitesi14” ve “Güvenli Başlangıç Hisseleri” için hesap formülü/veri zamanlaması verilmez. S. 61–62'deki kâr alıcı ve ardışık iki trailing stop altı kapanış yalnız mevcut çıkış ailelerinin varyantıdır. S. 71'deki `%78,9` başlık seçilmiş bülten/notional sonuçlarıdır, bağımsız dış örneklem performansı değildir. **Yeni bağımsız aday: 0.**

## 2. Rakesh Bansal — Karlı Kısa Vadeli Trading Stratejileri (193 sayfa)

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 11/Baskı 11/Karlı Kısa Vadeli Trading Stratejileri - Rakesh Bansal (193 sayfa) - @eseckal.pdf>) · [tam metin](02_short_term_bansal.txt)

**Tam okuma:** S. 1–24 ön bilgi/grafik/trend; 25–40 HH/HL ve LH/LL trend stratejileri; 41–47 destek/direnç; 48–68 trend çizgisi; 69–146 klasik formasyonlar, üçgen, dikdörtgen, bayrak/flama; 147–150 gerçek seans gap'leri; 151–157 Fibonacci geri çekilmesi; 158–181 RSI/MACD ayrışma, MA ve ATR; 182–189 mekanik sistem, SMA±ATR ve HHV/LLV; 190–193 algoritmik işlem/kapanış. Trend, klasik formasyon, ayrışma ve Fibonacci kuralları önceki aday ailelerini yineler. S. 188–189 HHV/LLV 7–28 bar karşı eşik dönüşü önceki [Donchian](../batch_130/STRATEGIES.md) ailesinin H1 pencere varyantıdır. S. 183–184'teki “iyi gün içi sistem günde 6–10 sinyal verir”, kazanan işlem sayısı kaybedenden fazla olmalı ve s. 189'daki yıllık `%40` iddiası evrensel performans koşulu değildir; kâr/zarar büyüklüğü ve maliyetler belirleyicidir.

### RB186A — H1 SMA50 ± ATR3 kapanışla yönlü durum makinesi

- **Kaynak (s. 185–188):** H1 fiyat `SMA50+ATR3` üstünde kapanınca long; `SMA50−ATR3` altında kapanınca short. Karşı bant altında/üstünde kapanış önceki yönü kapatır ve yeni yönü açar. Kaynak SMA için 20–50, ATR için 3–7 periyot denemeyi söyler; s. 188'deki örnek `SMA50, ATR3` ve 60 dakikalık Nifty vadeli grafiğidir. Sonradan en kârlı parametreyi seçip aynı örneklemde doğrulanmış ilan etmeyeceğiz.
- **Veri/hesap:** Tarihsel Nifty vadeli işlemlerinde gerçek sözleşme H1 bid/ask OHLC, sözleşme/roll takvimi ve işlem saatleri. Tam kapanmış H1 `t` için `M_t=SMA50(close)`, `A_t=WilderATR3(high,low,önceki close)`, `U_t=M_t+A_t`, `D_t=M_t−A_t`. `C_t>U_t` yukarı olay, `C_t<D_t` aşağı olay; eşitlik sinyal değil. `M,A` t kapanınca bilinir, sinyalin aynı H1 açılışında işlem yok. Önceki durum long ise tekrar long olayında ekleme yapılmaz; short olayında ters çevir. İşlem seansı dışındaki eksik H1 için sahte bar üretme.
- **İcra/risk/çıkış:** Teyit H1 kapanışından sonra ilk uygulanabilir kotasyonda long ask/short bid. İlk koruyucu acil stop long için `entry−2×ATR14_H1(t)`, short için `entry+2×ATR14_H1(t)`; özsermayenin en çok `%0,25`i stop riski, aynı anda tek sözleşme yönü. Karşı bant kapanışında sonraki kotasyonda mevcut pozisyonu kapatıp, yeni risk sınırı uygunsa tersini aç. Karşı sinyal gelmezse en geç 10 işlem seansı sonunda çık. `2×ATR14` acil stopu, 10 seans ve risk payı **bizim test sözleşmemizdir**; kaynak s. 187 karşı bant çıkışını verir. Gap, margin, roll, komisyon, genişleyen spread ve kayma dahil; stop seviyesi garantili dolum sayılmaz.
- **Ayırıcı sınama:** Aynı H1 verisiyle çıplak SMA50 kapanış geçişi, EMA/SMA+ATR Keltner **kırılımı**, [130. parti](../batch_130/STRATEGIES.md) Donchian karşı eşik dönüşü ve yalnız tek yön trend kuralı. Sinyal örtüşmesi, işlem sıklığı, whipsaw maliyeti, net R, maksimum düşüş ve dönem dışı pencere testleri raporlanmalı. `20/50 SMA × 3/7 ATR` ızgarası keşif alanıdır; nihai parametre yalnız eğitim döneminde seçilir. Kaynak örneğindeki “en iyi saatlik” ifadesi genellenmiş kanıt değildir.

## 3. Rankia — Teknik Analiz Rehberi (76 sayfa)

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 11/Baskı 11/Teknik Analiz Rehberi - Rankia (76 sayfa) - @eseckal.pdf>) · [tam metin](03_ta_rankia.txt)

**Tam okuma:** S. 1–15 tanım, grafik ölçeği ve zaman dilimleri; 16–34 trend, Dow, seviye, çizgi ve gap; 35–48 devam formasyonları; 49–60 çift/üçlü tepe-dip, OBO, V ve yuvarlak dönüş; 61–68 Elliott; 69–76 Fibonacci ve kapanış. Kitap eğitim rehberidir. Dikdörtgen/üçgen/bayrak kırılımı ve ölçüm hedefleri (s. 35–48), çift tepe/dip boyun kırılımı (s. 49–57), gap ve Fibonacci (s. 33–34, 69–75) önceki kayıtlarda var. Elliott etiketinin s. 63'te açıkça belirtildiği gibi geriye dönük değişebilmesi, teyitsiz canlı kural üretmeyi engeller. Tekrardan kaçınarak **yeni bağımsız aday: 0**.

**Parti sonucu:** 3 PDF, **357 sayfa**, **1 yeni doğrulanmamış aday**. Kümülatif **558 PDF, 29.913 sayfa, 426 aday**.
