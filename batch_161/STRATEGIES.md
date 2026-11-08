# Kitap okuma 161 — üç mum sonrası ters kırılım, giriş ve RSI aşırılığı

Üç ayrı PDF'nin **57 + 47 + 42 = 146 sayfası** sırasıyla incelendi. Sayfa atıfları PDF sayfasıdır. **Yeni bağımsız strateji adayı: 1.** Backtest, paper test ve emir yapılmadı.

## 1. Price Action — Raoul Hunter

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 18/Baskı 18/Price Action - Raoul Hunter (57 sayfa) - @eseckal.pdf>) · [tam metin](01_price_action_hunter.txt)

**Tarama:** s. 1–9 giriş/bağlam; 10–17 pin, dış ve iç mum; 18–30 klasik Japon mumları; 31–32 yalın fiyat hareketi ters dönüşü; 33–40 baş omuz, çift/üçlü tepe; 41–47 harmonik kalıplar; 48–53 kupa kulp, elmas ve seviye+mum; 54–57 sonuç. Pin mum için en az 3:1 fitil/gövde (s. 13), iç mumda ana mumun kırılması (s. 16–17) ve boyun çizgisi/kulp kırılımı (s. 35–49) önceki aday ailelerindedir. Harmoniklerde pivotların "önemli" olması ve CD çizgisinin çizimi nesnel verilmemiştir; 42. sayfadaki zaman oranı ifadesi de çeviride muğlak.

### RH161A — Üç aynı yönlü mum ardından karşı yöne önceki uç kırılımı

- **Kaynak:** s. 31–32. Aynı yönde **en az üç mum**, arada ters renk varsa sayım sıfırlanır. Yükselişte kapanış bir önceki mumun *low* seviyesinin altına inince short; düşüşte önceki *high* üstüne kapanınca long. Kâr için yeni yönünde art arda üç mumdan sonra çıkış veya karşı yöndeki eşdeğer tetikleyicide zorunlu çıkış anlatılır. s. 31'deki örnekte doji ile bir sonraki düşük kırılımı vardır. Bu, [26. partinin üç mum devam](../batch_026/STRATEGIES.md) adayından yön ve tetik bakımından ayrılır; [12. partinin 4–5 mum + EMA8](../batch_012/STRATEGIES.md) kuralının da aynı olay olmadığı ayrıca karşılaştırılacaktır.
- **Ön kayıtlı sinyal:** BTCUSDT/ETHUSDT spot D1 UTC. Short için t−3,t−2,t−1 mumlarının her birinde `close>open`; t kapanışında `close_t<low_{t-1}`. Long için üç `close<open` ve `close_t>high_{t-1}`. t mumu üçlü sayımın dışında ve t kapanana kadar sinyal yok. Doji (`close=open`) sayımı sıfırlar. Dört veya daha fazla aynı renkli mum varsa yalnız ilk uygun ters kırılım sayılır; örtüşen pencerelerden çoğaltılmış işlem yok. Kaynağın "en az üç" ve reset kuralı korunur; sayımı bu şekilde sabitleme test sözleşmesidir.
- **İcra/risk:** t kapanışından sonraki ilk uygulanabilir 1m açılışı. Long stop `min(low_{t-3:t})−0,1 ATR14_D1(t)`, short stop `max(high_{t-3:t})+0,1 ATR14_D1(t)`; ATR tamponu kaynağa değil bize aittir. İşlem başına %0,25 özsermaye riski, kaldıraçsız. Giriş sonrası **üç ardışık kapalı D1** pozisyon yönünde (`close>open` long / `<open` short) olunca sonraki ilk 1m çıkış; araya ters/doji girince kâr sayımı sıfırlanır. Ters yönde RH161A sinyali gelirse sonraki ilk 1m'de kapat, aynı anda otomatik ters açma yok. 10 D1'dan sonra süre çıkışı bizim kuralımız. Stop intraday uygulanır; 1m veri yoksa işlem doldurulmaz. Aynı 1m'de iki çıkış koşulu varsa stop önce. Başlangıçta 20 tam D1 ve ATR14 geçmişi yoksa sinyal yok.
- **Değerlendirme:** Aynı dönem ve masraf modeliyle yalın önceki low/high ters kapanışını, 2/3/4 mum ön koşulunu, batch012 ve batch026 olaylarını karşılaştır. Ücret/kayma sonrası net R, medyan R, işlem sayısı, maksimum düşüş, yön/sembol ve dönem dışı sonuçlar raporlanır. Kaynak örnek grafikleri bağımsız başarı kanıtı değildir.

## 2. İşleme Giriş Noktasının Belirlenmesi — Momoh SO

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 20/Baskı 20/İşleme Giriş Noktasının Belirlenmesi - Momoh SO (47 sayfa) - @eseckal.pdf>) · [tam metin](02_entry_momoh.txt)

**Tarama:** s. 1–18 trend, formasyon ve çift tepe/dip; 19–28 destek/talep bölgesinde boğa teyidi; 29–36 direnç/arz bölgesinde ayı teyidi; 37–47 emir, örnek ve kapanış. s. 19–22 ve 29–31 farklı formasyonları alternatif olarak verir, fakat hangisinin seçileceğini ya da destek bölgesinin sayısal sınırını belirlemez. Çift tepe/dip boyun kırılımı, destek/dirençte ters mum ve kırılım sonrası geri test mevcut ailelerle örtüşür. s. 45'teki seçilmiş işlem ve ödeme örnekleri genellenebilir istatistik değildir. **Yeni bağımsız aday yok.**

## 3. Fiyat Aşırı Alım ve Aşırı Satım Sinyali — Momoh SO

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 20/Baskı 20/Fiyat Aşırı Alım ve Aşırı Satım Sinyali - Momoh SO (42 sayfa) - @eseckal.pdf>) · [tam metin](03_extremes_momoh.txt)

**Tarama:** s. 1–13 giriş/fiyat davranışı; 14–16 RSI 30/50/70; 17–28 aşırı alım ve seçilmiş kısa örnekler; 29–38 aşırı satım ve seçilmiş uzun örnekler; 39–42 diğer kitap reklamları. s. 19'da 30 altından tekrar üstüne long, s. 31–32'de 70 üstünden tekrar altına short, [57. partideki RSI sistemiyle](../batch_057/STRATEGIES.md) aynıdır. "MA çizgisi" ifadesi RSI eğrisini mi RSI üzerine hesaplanmış ayrı bir ortalamayı mı anlattığı net değildir; ayrıca 50 ve 30/70 geçişlerinin sıralaması çelişkili. s. 14'teki %75 doğruluk ve s. 38'deki garanti iddiaları bağımsız kayıtla desteklenmez. **Yeni bağımsız aday yok.**

**Parti sonucu:** 3 kitap, 146 sayfa, 1 yeni aday. Birikmiş toplam **392 doğrulanmamış strateji adayı**.
