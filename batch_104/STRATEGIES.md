# Kitap okuma 104 — üç döviz çiftli EMA10 sepeti

**Kapsam:** Üç özgün PDF'nin **24 + 50 + 19 = 93 sayfası** baştan sona okundu. Atıflar PDF sayfasıdır. Bu turda backtest, paper test veya emir yapılmadı. Aşağıdaki aday araştırma hipotezidir; kaynakta verilen kazanç iddiaları doğrulanmış performans değildir.

## 1. Gavin Holmes Scalp Stratejisi

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 3/Baskı 3/Gavin Holmes Scalp Stratejisi (24 sayfa) - @eseckal.pdf>) · [Tam metin](01_gavin_holmes_scalp.txt)

**Tam okuma:** S. 1–5 ürün ve sistem tanıtımı; s. 6–11 SMART Center Pro/SuperScalp tarayıcısı ve zaman dilimi uyumu; s. 12–14 yüksek hacim bölgesine düşük hacimli dönüş; s. 15–16 çıkış/risk; s. 17–24 VSA açıklamaları ve tanıtım. M1–M5'te tarayıcının kendi sinyali ile sonraki bar yön teyidi anlatılıyor (s. 4–10), fakat tarayıcı ve VSA işaretlerinin hesaplama koşulları verilmemiş. S. 16 kesin stop kuralı sağlamıyor. Düşük hacimli dönüş önceki VSA adaylarıyla örtüşüyor. Bu nedenle kitap adına mekanik sinyal uydurup yeni aday saymadık. Forex tick hacmi, merkezi gerçekleşmiş hacim değildir.

## 2. Madam Lim Trading Sistemi — World Class Trading Stars

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 3/Baskı 3/Madam Lim Trading Sistemi - World Class Trading Stars (50 sayfa) - @eseckal.pdf>) · [Tam metin](02_madam_lim.txt)

**Tam okuma:** S. 1–12 giriş, özgeçmiş ve özet; s. 13–15 sepet girişi/çıkışı; s. 16–20 korelasyon ve EMA; s. 21–26 risk; s. 27–30 grafik ayarı; s. 31–39 short kuralları ve örnekler; s. 40–47 long kuralları ve örnekler; s. 48–50 yorum ve ağırlık değişikliği. Ana kaynak koşulu açık: EURUSD, GBPUSD, USDCHF H4 kapanışlarının en az ikisi EMA10'un aynı tarafında ise **üç çiftin tamamında aynı yönde** işlem; lot oranı sırasıyla %30/%20/%50; toplam sepet kârı %5–10 veya toplam zarar %20 ya da tüm çiftlerde ters EMA kapanışıyla toplu çıkış (s. 31–32, 40–41). S. 18 ve 26 korelasyon/hedge açıklamaları kendi içinde farklı USD maruziyeti taşıyor: üç çifte aynı yönde girildiğinde USDCHF negatif korelasyonu diğerlerini kısmen dengeler ama sabit lotlar eşit USD riski yaratmaz. Hedge garantisi yoktur; 2011 korelasyonları güncel kabul edilmez.

### ML104A — EMA10 çoğunluk oyu ve üç çiftli sepet

- **Kaynak (s. 14–15, 29, 31–32, 40–41):** H4 kapanış EMA10'a göre üç enstrümanın en az ikisinde üstteyse tüm üçünde long, en az ikisinde alttaysa tüm üçünde short. Ağırlıklar EURUSD 0,30; GBPUSD 0,20; USDCHF 0,50 **lot oranıdır**. Toplu pozisyon kapatılır. EMA10 yakınında yatay seyir ve “çok uzakta” istisnaları (s. 32, 41) nicel eşik içermez; temel adayın parçası değildir.
- **Nesnel araştırma sürümü:** Üç senkronize, bitmiş H4 barın `close_t > EMA10_t` sayısı en az iki ise long; `close_t < EMA10_t` sayısı en az iki ise short. Eşitlik varsa sinyal yok. Açık sepet yokken yön yeni oluştuğunda sonraki uygulanabilir bid/ask kotasyonunda üç bacak birlikte açılır; yinelenen yönde yeniden giriş için üç bacağın da kapandıktan sonra oylama yönünün en az bir H4 bar sıfırlanması gerekir (**bizim anti-churn koşulumuz**). Kaynaktaki 0,30/0,20/0,50 lot oranı FX kontrat, pip değeri ve USD maruziyetine göre normalize edilmeden salt portföy ağırlığı sayılmaz. Önce kaynak lot oranı ayrı senaryo; ikinci senaryo eşit USD delta veya eşit ATR riskli bacaklar **bizim ablation'ımızdır**.
- **Çıkış/risk:** Kaynaktaki toplu net sepet PnL'si giriş özsermayesinin +%5, +%10 ve −%20'sine eriştiğinde ayrı kollar; üç H4 bar da ters EMA tarafında kapanırsa sonraki uygulanabilir kotasyonda toplu kapat. %20 zarar sınırı araştırma için aşırı büyük; birincil güvenli araştırma kolunda maksimum sepet özsermaye kaybını **bizim** %1 ile sınırla ve kaynak kolunu yalnız karşılaştırma olarak raporla. Aynı bar içinde kâr ve zarar eşiği vurulursa düşük zaman dilimi kotasyonla sıra belirle; çözülmezse zarar önce. 20 H4 bar azami tutma **bizim**. Spread, komisyon, swap/finansman ve üç bacak eşzamanlı olmayan dolumlar dahil. Sadece geçmişten hesaplanan korelasyonla USD hedge varsayımını ayrıca denetle.
- **Ayrışma/test:** Tek enstrüman EMA10 filtresinden farkı, üç senkronize çifti çoğunluk oyu ve ters korelasyonlu üçüncü bacağı beraber kullanmasıdır. Abla­syon: iki benzer USD çifti, USDCHF'siz sepet, her biri tek başına, oylama ve ağırlık varyantları. Portföy USD delta ve gerçekleşen risk ölçülmeden “korunma” veya pozitif beklenti iddiası yapılamaz. Walk-forward dönemde rejim/korelasyon kırılması, gecikme ve maliyet sonrası net getiri incelenecek.

## 3. Trendline Trading Stratejisi — Day and Night Forex

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 7/Baskı 7/Trendline Trading Stratejisi - Day and Night Forex (19 sayfa) - @eseckal.pdf>) · [Tam metin](03_trendline_day_night.txt)

**Tam okuma:** S. 1–4 iki pivottan trend çizgisi ve üçüncü/dördüncü temas girişi; s. 5–8 kapanışla kırılım, çizgi geçerliliği ve eğim; s. 9–10 yatay destek/direnç birleşimi; s. 11–14 yapı değişimi ve trend; s. 15–17 çoklu zaman dilimi, stop ve risk; s. 18 varyasyonlar; s. 19 özet ve dönüş mumu kataloğu. İki pivotun teyit gecikmesi, çizgiye temas toleransı, “belirgin” pivot, uygun eğim, yedi dönüş mumunun tam koşulları ve toplu çıkış nesnel verilmemiş. Daha önce [80. parti](../batch_080/STRATEGIES.md) iki/üç temas ve kapanışla kırılımı, diğer partiler trend çizgisi retestini kaydetti. Bu kitap yeni bağımsız aday eklemedi. İleride çizgi algılama hipotezi kurulursa bu **bizim algoritmamız** olarak ve gecikmeli pivot teyidiyle denenmeli; geçmiş grafiğe çizilen çizgi doğrudan canlı sinyal kabul edilmemeli.

## Sonuç

Bu üç kitaptan **1 yeni strateji adayı** kaydedildi: ML104A. Gavin Holmes için kritik sinyal kodu kapalı, Trendline kitabındaki tema ve çizgi kuralları mevcut adaylarla çakışıyor. Backtest ve paper test sonraki aşamada.
