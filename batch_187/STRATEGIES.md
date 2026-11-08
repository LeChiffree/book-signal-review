# Kitap okuma 187 — bakir POC ve 20/20 ertesi gün geri dönüşü

Üç PDF'nin **383 sayfası** sayfa bazında metne çıkarılıp baştan sona tarandı; işlem kuralları kaynak sayfalarında ayrıntılı kontrol edildi. **2 yeni, henüz doğrulanmamış strateji adayı** kaydedildi. Backtest, paper test ve emir yapılmadı. Sayfa numaraları PDF sayfasıdır.

## 1. Michael Jardine — Günde Sadece 1 Trade (181 sayfa)

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 11/Baskı 11/Günde Sadece 1 Trade - Michael Jardine (181 sayfa) - @eseckal.pdf>) · [tam metin](01_one_trade_jardine.txt)

**Tam okuma:** S. 1–30 POC, bakir POC ve Jardine aralığı; 31–68 profil/seviye kullanımı ve gün içi örnekler; 69–82 iki stokastik ve giriş tetikleri; 83–122 Keltner, işlem örnekleri ve çıkış; 123–181 uygulama, risk ve kapanış. Kitabın tek başına stokastik kesişimi ve Keltner çıkışı önceki ailelerin varyantlarıdır. Ayırıcı yeni unsur, sonraki işlemlerde hiç dokunulmamış geçmiş seans POC'sinin gün başında seçilip ilk temasta dönüş aranmasıdır (özellikle s. 46–51, 103–106).

### MJ187A — bakir seans POC'sinin ilk yeniden temasında dönüş

- **Kaynak:** S. 10–15 ve 46–51 POC/bakir POC; s. 72–78 yavaş `81,9,9`, hızlı `9,3,3` stokastik ve 20/80 hizalanması; s. 103–106 açılışta Keltner dışı VPC, ilk temas ve tetik; s. 117–119 karşı Keltner kenarında çıkış. Kaynak 50-range/tick grafik ve S&P E-mini kullanır. Aşağıdaki M1 kapanış, profil ve risk kesinleştirmeleri **bizim test sözleşmemizdir**.
- **Veri/kurulum:** ES vadeli gerçek kontrat işlem tikleri (fiyat, miktar, zaman), RTH seans takvimi, kontrat rolleri ve uygulanabilir bid/ask. Tamamlanan her RTH seansı için işlem hacmini fiyat tikine göre topla; en yüksek tekil fiyatı POC kabul et, eşit maksimumda o günü dışla. Bir POC, ilgili seans bitiminden bugünkü açılışa kadar hiçbir gerçek işlem tikinde o fiyattan işlem görmediyse bakirdir; gece seansı da kontrol edilir. Açılışta son 20 RTH seansının bakir POC'lerinden fiyata en yakın alt ve üst seviyeyi sabitle. Keltner `EMA20(M1 close) ± 1.5×WilderATR20(M1)`, açılış öncesi son kapanmış M1'den hesaplanır; yalnız kanal dışındaki seviye geçerli. 20 seans sınırı ve Keltner parametreleri kaynakta sabit değildir, ön kayıt varsayımıdır.
- **Sinyal/icra:** Seans içindeki ilk POC temasından önce yaklaşım yönü belirlenir: aşağıdan gelen temasta short, yukarıdan gelende long. Temastan sonraki en çok 5 tamamlanmış M1 mumunda, ilgili yönde hızlı `9,3,3` stokastik `%K/%D` kesişimi, iki stokastiğin de short için `>80`, long için `<20` olması ve M1 kapanışının POC'nin beklenen dönüş tarafında bulunması gerekir. Sinyal mumundan **sonraki** ilk kotasyonda short bid/long ask; aynı POC gün içinde tekrar kullanılmaz. İki stokastiğin eş zamanlı koşulu s. 78'den alınmıştır; `5 M1` zaman penceresi ve M1'ye uyarlama bizim seçimimizdir. Aynı mum içi sıralamayı OHLC'den varsayma.
- **Çıkış/risk:** Girişteki karşı Keltner kenarı ilk hedef; ilk hedefte tamamını kapat. İlk temas-sonrası ekstremumun 1 tik ötesi koruyucu stop; hedef stopa göre doğru tarafta ve en az `1R` değilse işlem yok. Her işlemde özsermayenin en çok `%0,25`i riske edilir, seans sonunda açık pozisyon kapatılır. Hedef, stop ve giriş tikleri sıralaması gerçek tick/bid-ask akışıyla simüle edilir; komisyon, slippage ve kontrat rolleri dahil. Tamamını ilk hedefte kapatma, `1R` filtresi ve risk oranı bizim test sözleşmemizdir.
- **Ayırıcı sınama:** Aynı veriyle dokunulmuş POC, önceki gün hacim POC'si, seans VWAP'ı ve VPC filtresiz stokastik dönüşü karşılaştır. İlk temas sonrası sinyal oranı, net R, maliyet duyarlılığı ve yıllara göre dış örneklem raporla. İşlem tikleri yoksa bakirlik ve POC eşdeğer biçimde sınanamaz; M1 OHLC ile yaklaşık sonucu doğrulanmış sayma.

## 2. Edward Day — Gelişmiş Forex Trading (120 sayfa)

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 12/Baskı 12/Gelişmiş Forex Trading - Edward Day (120 sayfa) - @eseckal.pdf>) · [tam metin](02_advanced_forex_day.txt)

**Tam okuma:** S. 1–24 FX piyasası/araçlar; 25–46 fiyat hareketi, aralık ve trend; 47–64 trend, destek/direnç; 65–76 USDJPY H4/H1 örnek incelemesi; 77–86 carry ve makro; 87–116 günlük, risk, psikoloji; 117–120 kapanış/tanıtım. S. 35'te merkezi FX emir akışı/hacmi gözlenemeyeceğini belirtir; s. 66–76 örneği öznel seviye ve bağlam yorumlarına dayanır. Nesnel yeni giriş/çıkış kuralı ve önceki adaylardan bağımsız aile çıkmadı. **Yeni aday: 0.**

## 3. Arthur H. Ullrich — S&P 500 Endeksinde Günlük Trading (82 sayfa)

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 16/Baskı 16/S&P 500 Endeksinde Günlük Trading - Arthur H. Ullrich (82 sayfa) - @eseckal.pdf>) · [tam metin](03_sp500_intraday_ullrich.txt)

**Tam okuma:** S. 1–20 gün içi yaklaşım ve göstergeler; 21–22 20/20 kuralları; 23–30 gap, yutan mum, ADX/EMA ve dört kapanış kırılımı; 31–64 grafik örnekleri/gün içi uygulama; 65–82 risk, notlar ve kapanış. 20/20 yöntemi kaynakta Connors ve Raschke'nin *Street Smarts* kitabına atfedilir; özgün yazarlık iddiası yoktur. S. 23 gap dolumu yüzde iddiaları örnekleme ve dönem dışı doğrulama olmadan başarı olasılığı kabul edilmez. Gap/ADX/EMA/dört bar kırılımı önceki kayıtları tekrarlar.

### AU187A — 20/20 referans gününün ertesi seansında uç seviye süpürüp geri dönüş

- **Kaynak (s. 21–22):** Günlük referans bar bir uçtaki `%20` aralıkta açılır ve karşı uçtaki `%20` aralıkta kapanır. Ertesi seans referans ekstremumu `5–15` tik aşılır, sonra aynı seviyeye dönülür; yazar `10` tik seçer. Alış için üstte açılış/altta kapanış ve ertesi gün düşük seviyeyi süpürme; satış için tersi. Kaynak seviye geri dönüşünde limit emir tarif eder. Aşağıdaki kapanmış M1 teyidi ve çıkışlar bizim test uyarlamamızdır.
- **Veri/kurulum:** ES vadeli kontratın gerçek RTH D1 ve M1 barları, tik büyüklüğü, RTH takvimi ve bid/ask. Referans gününde `R=H−L>0`; long kurulumunda `O≥H−0.2R` ve `C≤L+0.2R`; short kurulumunda `O≤L+0.2R` ve `C≥H−0.2R`. Yalnız **bir sonraki** RTH seansına taşınır. Uzun için gün içi fiyat `L−10 tik` veya aşağısını, kısa için `H+10 tik` veya üstünü görmeli. Süpürmenin M1 içinde geri dönüşle sıralaması bilinmiyorsa, süpürmeyi tamamlanmış önceki M1 ile doğrula.
- **Sinyal/icra:** Süpürme tamamlandıktan sonra ilk tamamlanmış M1 mumunun long için `close>L`, short için `close<H` olması gerekir; o mumun kapanışından **sonraki** ilk uygulanabilir kotasyonda gir. Gün başına tek işlem, referans gününden iki gün sonra kurulum düşer. Kapanışla teyit, kaynak limit girişinden farklıdır; kaynak kuralıyla ayrı varyant olarak raporlanmalı.
- **Çıkış/risk:** Stop süpürme ekstremumunun 1 tik ötesi; hedef `2R`, seans bitiminde zorunlu çıkış. Stop mesafesi sıfır/negatifse sinyal yok. Stop riski özsermayenin en çok `%0,25`i; gap, komisyon, spread ve kayma dahil. `2R`, zaman çıkışı ve risk payı kaynak iddiası değil, bizim ön kayıt seçimimizdir. Hedef/stop aynı M1 mumunda görünürse tik sırası gerekir; yoksa en aleyhte sıra kullanılır.
- **Ayırıcı sınama:** Genel önceki gün yüksek/düşük false breakout, 20/20 referans filtresiz süpürme, `5/10/15` tik hassasiyeti ve kaynak limit giriş varyantını karşılaştır. Yıl, volatilite ve kontrat rejimi bazında olay sayısı, net R ve maliyet duyarlılığı raporlanmalı.

**Parti sonucu:** 3 PDF, **383 sayfa**, **2 yeni doğrulanmamış aday**. Kümülatif **561 PDF, 30.296 sayfa, 428 aday**.
