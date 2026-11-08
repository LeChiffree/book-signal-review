# Kitap okuma 111 — üçgen sonrası 1-2-3 Fibonacci kırılımı

**Kapsam:** Üç ayrı PDF'nin **20 + 26 + 29 = 75 sayfası** baştan sona incelendi. FX Goat PDF'sinin metin katmanı bozuk kodlandığından [s. 1–10](fx_goat_1_10.jpg), [s. 11–20](fx_goat_11_20.jpg) ve [s. 21–29](fx_goat_21_29.jpg) görsel okundu. Atıflar PDF sayfasıdır. Backtest, paper test ve emir yapılmadı.

## 1. Forex Bermuda Trading Stratejisi — Michel Selim

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 8/Baskı 8/Forex Bermuda Trading Stratejisi - Michel Selim (20 sayfa) - @eseckal.pdf>) · [Tam metin](01_bermuda_selim.txt)

**Tam okuma:** S. 1–3 kapak ve risk; s. 4–6 yakınsayan üçgen ve kırılım, tercihen H1/H4; s. 7–8 Fibonacci ile 1-2-3 dönüşünün tanıtımı; s. 9–13 birleşik kurulum, 0 noktası=1, 100 noktası=2, 3 noktası %23,6/%38,2/%50/%61,8 geri çekilmede, giriş 100 kırılımında, stop 3 dışı, uzatma hedefleri %161,8/%261,8/%423,6; s. 14–17 geriye dönük EURUSD örnekleri; s. 18–20 risk yönetimi. Kaynağın üçgen, pivot ve Fibonacci seviyesine yakınlık için kesin algoritması yoktur; aşağıdaki operasyonel eşikler araştırma tanımıdır. Kitabın yüksek başarı/genellik iddiaları ölçülmüş sonuç değildir.

### MS111A — Üçgen kırılımı sonrası 1-2-3 geri çekilmesi ve 100 düzeyi yeniden kırılımı

- **Kaynak (s. 4–6, 9–13, 17):** Üçgen içinden yönlü çıkıştan sonra 1-2-3 yapısı beklenir; 1→2 salınımının geri çekilmesinde 3, belirtilen Fibonacci düzeylerinden birine denk gelirse 2'nin yeniden geçilişinde girilir. Stop 3 dışına; uzatma hedefleri %161,8, %261,8, %423,6'ya konur. Kaynak önceki ana trendi şart koşmaz.
- **Kapalı mum deney sözleşmesi:** Başlangıç evreni EURUSD H1, ayrı duyarlılık kolu H4. Yalnız sağında iki kapanmış mum bulunan 2-sol/2-sağ pivotlar kullanılacak. Son 80 mumda art arda alçalan iki pivot tepe ile yükselen iki pivot dip bulunacak; iki doğrunun gelecekte kesişmesi ve pivotlar arasındaki kapanışların çizgiler içinde olması şartı bizim üçgen tanımımızdır. İlk dış kapanış yönü kırılımdır. Long için kırılım sonrasında teyitli 1=dip, 2=tepe, 3=daha yüksek dip sıralaması; short için simetri. 3'ün `|2−1|` içindeki geri çekilmesi 0,236/0,382/0,500/0,618 düzeylerinden birine **±0,03** mesafedeyse uygun (**bizim toleransımız**). 3 sağ teyidi geldiğinde 2 zaten yeniden kırılmışsa sinyal atlanır. Sonraki mumlarda 2'nin ötesinde kapanış giriş sinyali; izleyen mum açılışında, spread/kayma ile uygulanır. Stop 3 dışına 1 pip; ilk hedef 1→2 yönünde 1,618 uzatma; 2,618/4,236 yalnız ayrı deney kolları. Stop ve hedef aynı bar içindeyse düşük zaman çözünürlüğü yoksa stop önce. 3 teyidinden sonra 20 mumda giriş yoksa iptal; girişten sonra 40 mumda çıkış yoksa piyasa çıkışı. Bir kurulum için tek işlem ve 0,5% özsermaye risk tavanı (**bizim**). Her sinyalde pivotların teyit zamanı, üçgen çizgileri, Fibonacci mesafesi, spread, maliyet sonrası R saklanacak.
- **Özgün hipotez:** Arşivde tek başına üçgen kırılımı, 1-2-3 kırılımı ve Fibonacci geri çekilmesi aileleri var; burada üçgen *önkoşulunun* 1-2-3+Fibonacci kurulumunun ileriye dönük sonucunu değiştirip değiştirmediği sınanır. Aynı 1-2-3 kuralını üçgen filtresi olmadan çalıştırıp işlem sayısı, seçilim, maliyet sonrası beklenti ve farklı piyasa dönemleri karşılaştırılacak. Pivot ve çizgi çiziminde gelecekteki mumlar kullanılmayacak.

## 2. AK47 Scalping Stratejisi — Siya Vezi

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 9/Baskı 9/AK47 Scalping Stratejisi - Türkçe ve İngilizce - Siya Vezi (26 sayfa) - @eseckal.pdf>) · [Tam metin](02_ak47_vezi.txt)

**Tam okuma:** S. 1–6 giriş/tanıtım; s. 7–11 M15 ve H1'de yakın veya önceki gün yüksek/düşüğüne üç itki-geri çekilme “vektörü” ile geliş, düzey testinde dönüş yönünde giriş; s. 12 fitil yorumları, 30 pip ters hareketle çıkış ve kanıtsız Asya seansı %80 iddiası; s. 13 boş/bitiş. S. 14–26 aynı içeriğin İngilizce tekrarından oluşur. “Vektör”, düzeyin seçimi ve “hemen testte giriş” nesnel kapalı mum kurallarıyla verilmemiştir; önceki gün düzeyi reddi ve çoklu salınım dönüşü arşiv adaylarıyla örtüşür. **Yeni bağımsız aday yok.** 80–100 pip örnek kazanç performans kanıtı değildir.

## 3. Nasdaq Trading Stratejisi — FX Goat

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 7/Baskı 7/Nasdaq Trading Stratejisi - FX Goat (Orijinal) (29 sayfa) - @eseckal.pdf>) · [Bozuk metin katmanı](03_nasdaq_fx_goat.txt) · [Görsel 1–10](fx_goat_1_10.jpg) · [Görsel 11–20](fx_goat_11_20.jpg) · [Görsel 21–29](fx_goat_21_29.jpg)

**Tam görsel okuma:** S. 1–3 Nasdaq tanıtımı, üç başlık (V, Z, destek/direnç) ve M15+ önerisi; s. 4–6 önceki gün tepe/dip civarında V dönüşü ve retest; s. 7–8 ters V/Z anlatımı ve seçilmiş örnekler; s. 9–12 önceki gün düzeyinin testi, retest ve stop; s. 13–19 fitilli dönüş mumu, doji, destek/direnç çizimi ve örnekler; s. 20–27 kanal/üçgen kırılımı ve retest örnekleri; s. 28–29 iletişim. “V/Z” bacakları ile destek/direnç seçimi kesin algoritma, emir ömrü ve hedef vermiyor. Önceki gün yüksek/düşük reddi, mum fitili teyidi ve üçgen retesti mevcut aday ailelerine denk geliyor. **Yeni bağımsız aday yok.** S. 3'teki 1:500 kaldıraç ve örnek bakiyeyi araştırma kuralına taşımıyoruz.

## Sonuç

**1 yeni araştırma adayı:** MS111A. İki diğer kitap mevcut fikirleri destekleyen kaynak olarak kaydedildi. Bu aday henüz doğrulanmış strateji değildir.
