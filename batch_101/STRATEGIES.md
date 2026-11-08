# Kitap okuma 101 — EMA34 dalga geri çekilmesi

**Kapsam:** Üç PDF'nin **19 + 34 + 42 = 95 sayfası** baştan sona okundu. Atıflar PDF sayfasıdır. Kaynak kuralı ile bizim sayısal uygulama kararlarımız ayrıdır. Backtest, paper test ve gerçek emir yapılmadı.

## 1. Basitleştirilmiş Forex — Alpha Balde

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 18/Baskı 18/Basitleştirilmiş Forex - Alpha Balde (19 sayfa) - @eseckal.pdf>) · [Tam metin](01_simple_forex_balde.txt)

**Tam okuma:** S. 1–5 tanıtım ve haber saatleri; s. 6–10 EMA34 yüksek/kapanış/düşük dalgası, Stochastic(5,3,3), MACD(6,13,5); s. 11–13 yön, geri çekilme, giriş, stop ve 2R hedef; s. 14–15 M5/M15 uygulaması; s. 16–19 sonuç ve kaynaklar. Dalga ve giriş grafiklerinin bulunduğu s. 7–13, 15 [görsel olarak](figure_contacts/) kontrol edildi. Haftada 200–300 pip iddiası doğrulanmış işlem serisi içermez.

### AB101 — EMA34 yüksek/düşük dalgasına geri çekilme ve yönüne dönüş

- **Kaynak kuralı (s. 7–13):** EMA34(high), EMA34(close), EMA34(low) kanalı. Fiyat dalganın üstündeyken yükseliş, altındayken düşüş; fiyat dalgaya geri girsin ve Stochastic(5,3,3) aşırı satıma yaklaşsın; MACD(6,13,5) sinyal çizgisi sıfırda veya üstünde olsun; ardından ilk yeniden dalga üstüne çıkan “yeşil” mumun kapanışında long. Stop yeni düşükten 2 FX pip aşağı, hedef 2R. Short simetrik kırmızı mumda. **Kaynak kusuru:** s. 12 short için de “stokastik 20/40 civarında aşırı alım” yazıyor; 20/40 aşırı alım değildir. Short testinde `%K≥60` bizim simetrik yorumumuzdur; özgün çelişki saklanır.
- **Nesnel kapalı mum sözleşmesi:** BTC/ETH M15; üç EMA34 ayrı high/close/low serilerinden, MACD çizgisi EMA6(close)−EMA13(close), sinyal EMA5(MACD), Stochastic full/slow(5,3,3) Wilder olmayan SMA hesabı. Long rejim, en az iki kapanmış M15 `close>EMA34(high)`; sonrasındaki en çok 10 barda `low≤EMA34(high)` ve `close≥EMA34(low)` ile dalgaya temas, temastaki `%K≤40`, `MACD_signal≥0`. Temastan sonraki en çok 5 kapanmış barda ilk `close>EMA34(high)` ve bir önceki kapanış `≤EMA34(high)` long tetik; tetikte MACD sinyal ≥0. Short rejim iki `close<EMA34(low)`, `high≥EMA34(low)`, `close≤EMA34(high)`, `%K≥60`, `MACD_signal≤0`, ardından ilk alt banda yeniden kapanış. Dalga içi temas, 2/10/5 bar pencereleri ve short osilatör eşiği **bizim test seçimimizdir**; yeşil/kırmızı rengin yeniden üretilebilir vekilidir. Karşı banda kapanış veya zaman dolması kurulumu iptal eder; kurulum başına tek giriş.
- **İcra ve risk:** Tetik kapanışı sonrası ilk uygulanabilir 1m giriş. Long stop kurulum-temas-tetik arasındaki gerçek minimum low `−max(tick,0.1 ATR14_M15)`; short maksimum high üstü. FX 2 pip kriptoya taşınmaz; ATR tamponu **bizim ölçekleme kararımızdır**. Giriş dolumundan 2R hedef, 32 M15 bar zaman çıkışı **bizim**. Stop aynı 1m hedefle çakışırsa stop önce; komisyon, spread, kayma uygulanır. Trend rejimi, dalga dönüşü ve stokastik/MACD filtrelerinin her biri ayrı ablation; önceki MACD+Stoch [TNT68](../batch_068/STRATEGIES.md) ve EMA geri çekilme adaylarıyla olay örtüşmesi ölçülür.

## 2. Forex Online — Eugenio Milani

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 18/Baskı 18/Forex Online - Eugenio Milani (34 sayfa) - @eseckal.pdf>) · [Tam metin](02_forex_online_milani.txt)

**Tam okuma:** S. 1–17 Forex yapısı, pariteler, spread/pip; s. 18–22 genel para ve risk yönetimi; s. 23–30 teknik/temel analiz ve gösterge türleri; s. 31–34 broker ve ürünler. Strateji diye anılan kısımlar eşik, zaman dilimi, sinyal, stop ve çıkış belirtmez. Yeni kapalı mum stratejisi çıkarılmadı. S. 16 “en güvenli piyasa” ve komisyonsuzluk; s. 26–27 şirket bilanço ölçütlerini Forex paritesi sinyali gibi anlatma, bu çalışma için kanıt veya kural değildir. Spread maliyetini kaydetme hatırlatması mevcut tüm test sözleşmelerine uygulanır.

## 3. Forex Trading — Owen Pagano

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 18/Baskı 18/Forex Trading - Owen Pagano (42 sayfa) - @eseckal.pdf>) · [Tam metin](03_forex_pagano.txt)

**Tam okuma:** S. 1–13 Forex, kaldıraç ve tanıtım; s. 14–16 genel teknik analiz; s. 17–24 psikoloji, otomatik sistem ve temel analiz; s. 25–30 osilatör/MA/PAR SAR tarifleri; s. 31–42 broker, maliyet ve genel sonuç. S. 29–30 SAR noktasına veya MA kesişimine giriş/çıkış önerisi hesap parametreleri ve stop belirtmez; aynı çekirdek önceki SAR/MA adaylarında mevcut. Yeni aday sayılmadı. Kitaptaki kârlılık ve düşük risk iddiaları işlem verisiyle desteklenmez; s. 32 spread, kayma ve gecelik maliyeti somut olarak anımsatır.
