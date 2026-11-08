# Kitap okuma 109 — VWAP üstünde RSI55, düşük ADX

**Kapsam:** Üç özgün PDF'nin **15 + 12 + 10 = 37 sayfası** baştan sona okundu. Payapa s. 2–6 İngilizce ve s. 8–12 Türkçe aynı içerik; iki ayrı kaynak sayılmadı. Atıflar PDF sayfasıdır. Backtest, paper test veya emir yapılmadı.

## 1. Trading Kurulumları — Falcon FX

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 7/Baskı 7/Trading Kurulumları - Falcon FX (15 sayfa) - @eseckal.pdf>) · [Tam metin](01_falcon_fx.txt)

**Tam okuma:** S. 1–8 üçüncü kanal teması, H1 reddi, çift tepe/dip, iç içe kanal ve bayrak; s. 9–10 ilk dürtü sonrası M15/H1 bayrağı; s. 11–13 üç takdire bağlı yönetim tarzı; s. 14 risk/ödül kontrol listesi; s. 15 psikoloji. S. 2 6–8 H1, s. 10 6–8 M15 sıkı düzeltme sonrası 2–4 pip dışı emir gibi sayılar verir; fakat “ana yapı”, kanal sınırı, düzeltmenin başlangıcı, dürtü, ret mumu, bayrak ve işlem yönü tek anlamlı algoritma değildir. S. 14 en az 3R ve 15 pip stop talep eder ama hangi hedef/stop seviyesinin hangi kurulumda seçileceğini vermez. Mevcut bayrak/kanal/üç temas adaylarıyla örtüşür; sırf süre eşiklerini değiştirerek yeni bağımsız aday açılmadı. Sonradan çizilmiş kanalın geçmiş girişe taşınması lookahead olur.

## 2. Payapa Scalping Stratejisi — Blanco

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 9/Baskı 9/Payapa Scalping Stratejisi - Türkçe ve İngilizce (12 sayfa) - @eseckal.pdf>) · [Tam metin](02_payapa_scalp.txt)

**Tam okuma:** S. 1 kapak; s. 2–3 medyan fiyata uygulanmış EMA5/8/13/21/100/200 ve Stochastic(5,3,3); s. 4–6 M5/M15/H1/H4 “continuation trap”, stochastic kesişimi ve çıkış; s. 7 geçiş; s. 8–12 Türkçe tekrar. Çekirdeğin EMA dizilişi ve stokastik kesişimi önceki çok zaman dilimli EMA/stokastik adaylarına benzer. Kritik metin hatası: s. 3–6 “EMA'ların 10/50/90 seviyesinde olması” der, fakat EMA fiyat birimindedir; 10/50/90 yalnız stokastik osilatör seviyeleridir. Yakınlaştırmaya göre değişen “EMA'nın osilatör seviyesine ulaşması” matematiksel sinyal olamaz. Trend tuzağına bazen kaçınma (s. 4–5), bazen o yönde işleme girme (s. 6) öneriliyor; giriş ve çıkış yönü çelişiyor. Stop ve risk bütçesi de yok. Doğrulanmamış “asla zarar etmeme” iddiası işlem kuralı veya performans kanıtı değildir. Yeni aday açılmadı.

## 3. Gün İçi Trading Stratejisi — Stock Trader

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 26/Baskı 26/Gün İçi Trading Stratejisi - Gelişmiş Bir Gün İçi İşlem Yöntemini Öğren - Stock Trader - Orijinal (10 sayfa) - @eseckal.pdf>) · [Tam metin](03_intraday_stock_trader.txt)

**Tam okuma:** S. 1–4 kapak/giriş; s. 5 alım/satım/çıkış kuralları; s. 6–8 Pine kodu; s. 9 yazarın tek yıllık sonuç tablosu; s. 10 kapanış. Kaynak BankNifty futures 15m'dir. Kod `ta.vwap((high+low)/2)`, `ta.rsi(close,14)`, `ta.dmi(10,20)` ve `ADX<30` kullanır. Long `close>VWAP` + RSI14 **55'i yukarı keser**; short `close<VWAP` + RSI14 **35'i aşağı keser**. Kaynak s. 5 “15:00 sonrası” çıkar derken kod s. 6 `1445-1500` karesinin başlangıcını çıkış yapar; iki saati eşdeğer saymıyoruz. Kodun `islong/isshort` bayrağı VWAP çıkışında sıfırlanmıyor, yalnız karşı giriş veya gün sonunda; bu da aynı yönlü yeniden girişi farkında olmadan engelleyebilir. S. 9'daki 2020–2021 / “1 yıl”, %31,48 net kâr ve %6,29 drawdown yalnız yazar beyanıdır; veri, işlem listesi ve tarih aralığı yok.

### ST109A — M15 VWAP–RSI55/35 kesişimi, ADX<30

- **Kaynak (s. 5–8):** BankNifty futures 15m; seans içinde long `close>session VWAP`, `ADX(10,20)<30`, `RSI14[t−1]≤55<RSI14[t]`; short `close<VWAP`, `ADX<30`, `RSI14[t−1]≥35>RSI14[t]`. Pozisyon VWAP karşı tarafına kapanışta veya gün sonunda kapanır. VWAP girdi fiyatı `HL2` olup gerçekleşen bar hacmiyle ağırlanır.
- **Nesnel araştırma sürümü:** Borsanın tarihsel işlem takvimindeki BankNifty futures kontratlarını, vade ve roll kuralı önceden sabitlenmiş şekilde kullan. IST 09:15–14:30 arası **tamamlanmış** M15 barlarda VWAP seans açılışında sıfırlanır: `Σ[(high+low)/2 × volume]/Σvolume`; sıfır/eksik hacim sinyal yok. RSI14 Wilder; DMI +DI/−DI periyodu 10 ve ADX Wilder yumuşatma 20, yalnız bitmiş M15 verisi. En az 100 bar ısınma; VWAP her seans yeni. Sinyal kapandığında sonraki ilk uygulanabilir M1 bid/ask'te giriş; bir aktif pozisyon, aynı bar zıt sinyalde önce çıkış sonra yeni giriş ancak ayrı kol. Long `close<VWAP`, short `close>VWAP` ile sonraki M1 çıkış. Gün sonu için **kod kolu** IST 14:45 ilk M15 çıkış penceresi, **metin kolu** 15:00 ayrı karşılaştırma; sessizce birleştirme. S. 5–8 sert stop vermez; gerçek paper deneyi öncesi önceden sabit `1×ATR14_M15` stop ve pozisyon başına en çok %0,5 özsermaye riski **bizim emniyet/araştırma ekimizdir**, orijinal sonuç replikası değildir. Aynı M1 stop ve çıkış sırası belirsizse stop önce; spread, işlem ücreti, vergi, kayma ve futures roll etkisi dahil.
- **Ayrışma/test:** [97. partideki](../batch_097/STRATEGIES.md) Nifty VWAP+RSI60/40 **yükselen ADX** ve 1×ATR/2×ATR stratejisine karşı burada **ADX<30 yatay rejimi**, RSI55/35 ve VWAP/saate bağlı çıkış vardır. Aynı veri ve maliyetlerle VWAP tek başına, RSI tek başına, ADX<30 filtresiz ve ADX yükselen kollarını önceden kaydet; işlem çakışması ve maliyet sonrası net R raporla. Hindistan seansını UTC kripto gününe çevirmek orijinal kural değildir.

## Sonuç

**1 yeni aday:** ST109A. Diğer iki kitap okunup tekrar ve tanımsız koşullar gerekçeleriyle kaydedildi.
