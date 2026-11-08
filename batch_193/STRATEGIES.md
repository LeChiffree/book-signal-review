# Kitap okuma 193 — trend riski ve işlem disiplini

Üç farklı PDF'nin **672 sayfası** sayfa bazında metne çıkarılıp baştan sona tarandı; kural ve risk bölümleri ayrıca ayrıntılı okundu. **Yeni bağımsız, nesnel kapalı mum işlem stratejisi adayı: 0.** Backtest, paper test ve emir yapılmadı. Sayfalar PDF sayfasıdır.

## 1. Alex Greyserman ve Kathryn M. Kaminski — Vadeli İşlemlerle Trend Takibi (391 sayfa)

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Vadeli İşlemlerle Trend Takibi - Alex Greyserman ve Kathryn M. Kaminski (391 sayfa) - @eseckal.pdf>) · [tam metin](01_futures_trend_greyserman.txt)

**Tam okuma:** S. 1–53 tarihçe ve trend takibi çerçevesi; 54–63 hareketli ortalama/kanal sinyali, güç ve risk büyüklüğü; 64–177 trend takip performansı ve portföy; 178–182 oynaklık tahmin penceresi; 183–265 stil, kayıp ve farklı piyasa ortamları; 266–276 stop temelli farklı trend endeksi; 277–391 faktörler, portföy, sonuçlar ve ekler.

S. 54–59 fiyatın hareketli ortalama veya önceki kanal sınırını aşması önceki MA/Donchian adaylarıyla aynı giriş ailesidir. S. 60–63 çoklu ufuk trend güçlerinin birleştirilip pozisyon büyüklüğüne uygulanması yeni bir giriş olayı değildir. S. 270–276'da takip eden stop vurulma sıklığıyla güncellenen yukarı/aşağı olasılıkları ve `S=P_yukarı−P_aşağı` büyüklüğü önerilir. Bu bölümün denklem OCR'ı bozulmuş; ilk sanal stopların kurulması ve günlük kapalı mumla intrabar stop tetikleme eşlemesi de net değildir. Bu nedenle kaynağı kesin bir işlem sözleşmesi gibi tamamlayıp yeni aday saymadık. **Yeni aday: 0.**

**Mevcut trend adayları için test varyantı:** S. 56–63, 270–273: sözleşme başına geçmiş fiyat değişimi standart sapması × puan değeriyle dolar riskini tahmin et; sinyal büyüklüğünü ayrılmış risk bütçesine uygula. S. 178–182: 20 günlük ve 250 günlük geçmiş oynaklık pencerelerini aynı girişlerle karşılaştır; ani oynaklık artışında geç uyarlama, maliyet, likidite, roll ve toplam portföy maruziyetini ölç. Pencere seçimi sadece geçmiş sonuçtan optimize edilmesin. Bu bir **risk/pozisyon boyutu ablation'ı**, yeni strateji değildir; [parti 184](../batch_184/STRATEGIES.md) ve [parti 188](../batch_188/STRATEGIES.md) ile örtüşür.

## 2. Tom Hougaard — En İyi Kaybeden Kazanır (250 sayfa)

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/En İyi Kaybeden Kazanır - Tom Hougaard (250 sayfa) - @eseckal.pdf>) · [tam metin](02_best_loser_hougaard.txt)

**Tam okuma:** S. 1–71 işlem yaklaşımı, kayıp ve kalıp arama; 72–119 algı ve işlem psikolojisi; 120–152 kazanan pozisyona ekleme, örnek işlemler ve risk; 153–200 alışkanlık, disiplin ve süreç; 201–250 davranış örnekleri ve sonuç.

S. 128'de kazanan pozisyona aynı veya daha küçük miktarda ekleme anlatılır. S. 141–142'de FTSE örneğinde 7.500'den 7.505'e ilerleyince ikinci birim eklenir ve stoplar yükseltilir; s. 150 eklemenin zararı da büyütebildiğini gösterir. Tekil örnek, yeniden üretilebilir genel giriş/ekleme eşiği ve çıkış kuralı vermez. Önceden kayıtlı trend girişlerinde ekleme yapılacaksa eşit ilk risk bütçesiyle ayrı kol ve eklemesiz kontrol olarak denenebilir; örnek işlemlerden kural uydurulmaz. S. 72'de formasyonları seçici görme riski, s. 200'de süreç takibi vurgulanır. **Yeni aday: 0.**

## 3. Norman Hallett — Traderlar İçin Mental Fitness (31 sayfa)

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Traderlar İçin Mental Fitness - Norman Hallett (31 sayfa) - @eseckal.pdf>) · [tam metin](03_mental_fitness_hallett.txt)

**Tam okuma:** S. 1–9 kaybı kişiselleştirme ve duygusal karar; 10–19 işlem ufku, sistem ve disiplin; 20–25 çalışma ortamı ve günlük; 26–31 öz değerlendirme ve kapanış. S. 5 ve 15 geçmiş testi görmenin plana bağlı kalmayı tek başına sağlamadığını; s. 20 ve 25 işlem ortamı ile günlük kaydını ele alır. Bunlar ileride paper testte kural dışı emir, kaçırılan sinyal ve günlüğe uyumu izlemek için kullanılabilir. Kapalı mum al/sat algoritması yoktur. **Yeni aday: 0.**

**Parti sonucu:** 3 PDF, **672 sayfa**, **0 yeni aday**. Kümülatif **579 PDF, 33.631 sayfa, 433 doğrulanmamış aday**.
