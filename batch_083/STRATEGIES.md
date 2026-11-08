# Kitap okuma 083 — Londra mikro sistemi, Bollinger dönüşü ve kanal çıkışı

**Kapsam:** Üç PDF'nin gerçek **80 + 113 + 61 = 254 sayfası** sayfa sırasıyla okundu; strateji ve grafik sayfaları [görsel olarak](figure_contacts/) kontrol edildi. Atıflar PDF sayfa numarasıdır. Bu dosyada iki yeni **araştırma başlığı** vardır: biri yönlü giriş adayı, diğeri mevcut girişler üzerinde çıkış deneyi. Hiçbir kitap örneği bağımsız backtest sayılmadı; backtest, paper test ve emir yapılmadı.

## 1. Kazançlı Günlük Trading Stratejisi — Caroline Ayuk

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 12/Baskı 12/Kazançlı Günlük Trading Stratejisi - Caroline Ayuk (80 sayfa) - @eseckal.pdf>) · [Tam metin](01_ayuk_daily.txt)

**Sayfa haritası:** S. 1–29 psikoloji, FX temeli ve tanıtım; s. 30–38 M15 grafik, Londra seansı kutuları, OsMA ve fraktal; s. 39–47 LWMA 8/10 (10 LWMA için `shift=1`), OsMA(12,26,9), giriş koşulları; s. 48–53 alım/satım kontrol listesi, 20 pip stop/hedef; s. 54–63 yalnız seçilmiş günlük örnekler; s. 63–68 isteğe bağlı stop taşıma ve hesap riski; s. 69–80 uygulama, günlük ve sonuç. Grafik ekranları s. 31–36, 42, 48–52, 56 ve 61'de ayrıca incelendi.

**Kaynak kuralı ve karar:** Londra civarında M15 kapanmış mumun 10 LWMA'nın doğru tarafında açılıp kapanması, 8 LWMA yönü, OsMA işareti ve önceden oluşmuş karşı fraktal stopu ile sonraki M15 başında giriş tarif ediliyor (s. 39–53). 10 LWMA'nın bir bar **ileri çizdirilmesi** grafik görünümü ve veri hizalaması için ayrıca tanım ister; mevcut mumla ileri kaymış seri karıştırılamaz. 20 pip hedef, 20 pipten fazla stopu kısma, GBP/USD ve CET/Londra zamanları FX'e özgüdür. Bu sistemin sinyali günlük karar **sonrasında yeni oluşacak M15** mumundan gelir; günlük kapanışta gerçekleşmiş gibi kaydetmek veri sızdırır. Bu yüzden mevcut çok günlü strateji havuzuna yeni başlık eklenmedi. Ayrı intraday araştırmada gerçek kapanmış M15, doğru kaydırılmış LWMA, sonraki uygulanabilir M1 dolumu, FX oturum saatinin tarihsel DST eşlemesi ve 1% işlem riskiyle yeniden kodlanabilir. S. 54–63'teki başarılı günler seçilmiş örneklerdir.

## 2. Basit Forex Trading Formülleri — Billy Williams

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 10/Baskı 10/Basit Forex Trading Formülleri - Billy Williams (113 sayfa) - @eseckal.pdf>) · [Tam metin](02_williams_formulas.txt)

**Sayfa haritası:** S. 1–43 FX işleyişi, kaldıraç, temel göstergeler; s. 44–55 mum formasyonları, baş-omuz, çift tepe/dip, BB/MACD, flama/bayrak ve Ichimoku; s. 56–91 risk, emir, yönetilen sistem ve dolandırıcılık; s. 92–101 haber, pivot, boşluk, M5 EMA20/MACD ve NFP iç mum; s. 102–106 çoklu gösterge, korelasyon ve `Turn Trade`; s. 107–110 COT, açık faiz ve FX carry; s. 111–113 genel planlama. Grafikler s. 44–55, 94, 97–98, 103, 105–106'da kontrol edildi.

**Ayıklama:** S. 94'teki dünkü H/L/C pivot formülleri önceki pivot çalışmalarını tekrar eder. M5 EMA20+MACD (s. 97–98), NFP sonrası M15 iç mum (s. 100–101) günlük çok günlü sözleşmeye uygun giriş değildir. Carry ve COT (s. 107–110) spot FX faiz oranı ve haftalık gecikmeli vadeli veri ister; kripto perpetual funding ile aynı ölçü değildir. S. 102–103'teki çoklu gösterge hizalanması net birleşik eşik ve çıkış vermez. Kaynakta bazı sayısal ve piyasa açıklamaları tutarsız olduğundan performans öncülü kabul edilmedi.

### BW83A — D1 SMA20 yönünde H1 Bollinger 2σ/3σ aşırılığından dönüş

- **Kaynak:** Günlük `SMA20` trend yönünü, saatlik Bollinger 2 ve 3 standart sapma uzaklığı geri çekilmeyi belirler; long için fiyat günlük SMA20 üstünde, H1 alt 3σ–2σ alanını test ettikten sonra geri kapanış; short simetrik (s. 105–106). Kaynak 2σ/3σ bantlarının **ortalama penceresini belirtmez**, H1 giriş ve çıkış cümleleri kısmen birbiriyle çelişir. `İlk hedef = riskin %50'si` ifadesi ile stopu bu seviyeye taşıma anlatımı da eksiktir. Bu nedenle aşağıdaki kural doğrudan kaynak getirisi iddiası değildir.
- **Bizim ön kayıt:** Günlük UTC `t` kapanışında yalnız tamamlanmış D1'de `close_t>SMA20_D1[t]` long rejimi (short için `<`). Aynı karar anından önce kapanmış son **altı H1** içinde en az bir `low <= lowerBB(20,3)`, ardından son kapanmış H1 `close > lowerBB(20,2)` ve bir önceki H1 kapanışı `<=lowerBB(20,2)` ise long olay. Short üst bantta simetrik. BB(20) dönemi ve altı H1 bakış penceresi **bizim** sabit seçimimiz; bantlar her H1'in o ana kadarki kapanışlarından hesaplanır. D1 kararından **sonraki ilk uygulanabilir M1** açılışında dolum; aynı anda iki yön oluşursa işlem yok, bir olaydan tek işlem.
- **Risk/çıkış:** Long stop `min(son 6 H1 low)−0,1×ATR14_D[t]`, short simetrik; stop mesafesi pozitif değilse atla. 1R/2R hedef ve en çok 3 gün zaman çıkışı ayrı deney kolları; hepsi **bizim**. Tam ücret, kayma, funding ve aynı M1'de stop önce. Mevcut [Bollinger geri dönüş ve trend filtreleri](../batch_011/STRATEGIES.md) ile aynı olay günlerinde karşılaştır; 3σ dokunuşunun 2σ tek başına girişe katkısını ayrı ölç.

## 3. Açığa Çıkan Trading Sırları — ChartSecret.com

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 10/Baskı 10/Açığa Çıkan Trading Sırları (61 sayfa) - @eseckal.pdf>) · [Tam metin](03_trading_secrets.txt)

**Sayfa haritası:** S. 1–18 piyasa, destek/direnç ve risk temeli; s. 19–27 ilk retest ve iki mumluk teyit; s. 28–37 yükselen/düşen kanal kırılımı ve retest; s. 38–42 asimetrik üçgen; s. 43–53 genişleyen megafon ve bant geri dönüşü; s. 54–58 sabit pip ile 4 HiLo takip stopu; s. 59–61 işlem günlüğü/tanıtım. S. 21–22, 28–31, 38–42, 44–51 ve 57 grafikleri ayrıca kontrol edildi.

**Ayıklama:** İlk kanal/üçgen/megafon kırılımı ve retesti önceki [kanal ve kırılım adayları](../batch_022/STRATEGIES.md) ile çakışır. Kaynak, `ilk retest`i sayısal mesafe ve azami süre ile kesinleştirmez; grafiklerde gözle seçilen sınırlar tek başına güvenilir yeni sinyal sayılmadı. Bunun yerine kaynakta açıkça tanımlanan çıkış karşılaştırması saklandı.

### CS83A — Kâr bölgesinde etkinleşen dört mum HiLo takip stopu

- **Kaynak:** Long için son dört **tamamlanmış mumun** en düşük seviyesinin 1 pip altı, short için en yüksek seviyesinin 1 pip üstü; yalnız stop seviyesi girişin kârlı tarafına geçtiyse hareket ettir (s. 56–58). Kaynak her yeni mumda güncelleme gösterir. FX pip miktarı kripto tick'ine bire bir çevrilmez.
- **Bizim karşılaştırma:** Önceden kayıtlı kanal kırılımı + ilk retest işlemlerinin **aynı girişlerini** kullan. D1 kararında veya H4 kapanışında, long için `candidate=min(low_H4[t−3:t])−1 tick` ve `candidate>entry+estimated_exit_cost` ise `stop_new=max(stop_old,candidate)`; short için `candidate=max(high_H4[t−3:t])+1 tick` ve `candidate<entry−estimated_exit_cost` ise `stop_new=min(stop_old,candidate)`. Yalnız dört **kapanmış H4** barı; mevcut H4'ün gelecekteki ekstremi kullanılmaz. Stop açılışta hazır emir olarak sonraki uygulanabilir M1'e taşınır. Başlangıç koruyucu stop, 2R sabit hedef ve 7 gün azami süre kontrol kolunda aynı kalır. HiLo çıkışının etkisini sabit 2R/ATR takip stopuyla eş giriş kohortunda kıyasla; kazanan işlemlerden ibaret geriye dönük örneklem seçme.

## Ortak doğrulama

Yeni sayısal eşikler ve kripto uyarlamaları kaynak bilgisi değil, **bizim test hipotezimizdir**. Çok günlü adaylar [sözleşmedeki](../../../research_v2/24_MULTIDAY_STRATEGY_CONTRACT.md) UTC D1 karar, son bitmiş H1/H4/D1, sonraki uygulanabilir M1, point-in-time evren, veri boşluğu ve maliyet kurallarına tabidir. Dört mum takip stopu yönlü alfa adayı değil, çıkış modülü olduğu için toplam başlık sayısını okurken bu ayrım korunmalı.
