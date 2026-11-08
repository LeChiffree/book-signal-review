# Kitap okuma 064 — ATR izleyen çıkış, MACD/RSI teyidi, hacimli seviye dönüşü

**Kapsam:** Üç PDF'nin gerçek **65 + 50 + 65 = 180 sayfası** sıralı metne çıkarılıp incelendi. Atıflar PDF sayfasıdır. Kaynakta verilmeyen eşikler ve icra kuralları **bizim test tanımımızdır**. Backtest, paper test ve emir yapılmadı.

## 1. David Jenyns — En İyi Trading Sistemleri

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/En İyi Trading Sistemleri - David Jenyns (65 sayfa) - @eseckal.pdf>) · [Tam metin](01_systems_jenyns.txt)

**Kaynak:** Yazar hazır bir tam giriş sistemi vermediğini açıkça söyler (s. 11, 19). s. 30'da Tom Basso/Van K. Tharp'tan aktarılan örnek: ATR'nin 10 günlük EMA'sının üç katı kadar ilk stop, kapanıştan yalnız lehe taşınan izleyen stop ve işlem başına %1 risk. Aktarılan geçmiş performansın veri, masraf ve yeniden üretim ayrıntıları kitapta yoktur; kaynak kârlılık kanıtı kabul edilmez. Beklenti hesabı ve R tanımı s. 36, 52; çıkışların önceden mekanik yazılması s. 40–41; test ve örneklem dışı gelecek sınırı s. 46–51.

### DJ64 — Mevcut girişler için 3×ATR-EMA10 yalnız lehe izleyen stop

- **Statü:** Bu bir **çıkış ve risk yönetimi koludur**, yeni bağımsız giriş sinyali değildir. Önceden kaydedilmiş, D1 kapalı mumla giriş veren CD61 veya MR60 gibi adayların **aynı giriş zamanları** üstünde test edilecek; giriş seçimini değiştirmeyecek.
- **Hesap:** D1 Wilder ATR14'ün EMA10'u `V[t]`; en az 100 D1 ısınma. Long girişinde `entry−3V[signal]`, short `entry+3V[signal]` ilk stop. Her **sonraki** D1 kapanışında long stop `max(previous_stop, close[t]−3V[t])`, short `min(previous_stop, close[t]+3V[t])`; gün içindeki barlar sonraki D1 kapanışına dek bir önceki stopu kullanır. ATR14 dönemi kaynakta belirtilmez, bizim seçimimizdir; stopun gerçek zamanlı ne zaman güncellendiği de bu test tanımıdır.
- **İcra/karşılaştırma:** Giriş ve stop dolumu 1m, ücret/spread/kayma/funding; aynı 1m belirsizliğinde aleyhte dolum. Stop yanlış tarafta veya maliyetin iki katından dar ise atla. Kaynakta hedef yok; çıkış kolu stop veya 90 D1 süreyle ölçülür. Aynı girişin sabit 2R ve kaynak stratejinin kendi çıkışıyla eşleştirilmiş net R, kuyruk kayıp, maksimum düşüş, elde tutma süresi kıyaslanır. Pozisyon boyutu girişte özsermayenin en çok %1'ini **ilk stop mesafesine** riske edecek; kaldıraç/pozisyon limiti uygulanır. Rastgele giriş anekdotu bir test sonucu olarak yeniden sunulmaz.

## 2. Jeff Drake — İndikatörlerle Kazanç Sağlamak

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/İndikatörlerle Kazanç Sağlamak - Jeff Drake (50 sayfa) - @eseckal.pdf>) · [Tam metin](02_indicators_drake.txt)

**Kaynak:** Hareketli ortalamaların konsolidasyonda yanlış kesişimleri (s. 11–12), MACD histogram sıfır geçişinin tek başına yalancı sinyalleri (s. 14–16). Örnek #3'te kısa vadeli teyit için **histogram sıfır çizgisi + RSI 50 çizgisi geçişi** beraber kullanılır ve örnek yatay piyasadır (s. 40–41). Diğer somut örnekler EMA21 ve yükselen ATR (s. 37–38), SMA21/55 kesişimi + Chaikin volatilitesi (s. 39–40) ve TRIX/MFI (s. 41–42). Seçilmiş grafik örnekleri başarı oranı sağlamaz.

### JD64 — Yatay rejimde MACD histogram ve RSI50 eşzamanlı geçişi

- **Rejim:** H4 kapanmış 30 barlık aralık `max(high)−min(low)≤4×ATR14_H4`, ADX14 `<20`; rejim ölçümü sinyal barından **önceki** 30 kapanmış H4 üstünde yapılır. Kaynağın nitel yatay ortamı için sayısal proxy bize aittir.
- **Sinyal:** H4 MACD(12,26,9) histogramı `h`, Wilder RSI14. Long: `h[t−1]≤0<h[t]` ve RSI14 `t−1≤50<t` **aynı tamamlanmış H4** barda; short tersi. Aynı bar zorunluluğu ana kol; ikinci göstergenin en çok üç H4 sonra teyit ettiği ayrı kol gecikme etkisini ölçer. En az 100 H4 ısınma. Çaprazlardan biri olmadan sırf gösterge değerinin aynı tarafta kalması yeni sinyal değildir.
- **İcra/risk:** Sinyal kapanışı sonrası ilk uygulanabilir 1m giriş. Long stop önceki 10 H4 low minimumu `−0,1×ATR`, short high maksimumu `+0,1×ATR`; 2R veya 18 H4 süre. Stop yanlış tarafta/maliyetten dar ise atla, aynı 1m stop önce. Histogram tek başına, RSI tek başına ve çift teyit kolları aynı piyasa/rejim/maliyet evreninde karşılaştırılır; MACD+RSI adaylarıyla olay çakışması raporlanır.

## 3. Ravi Agarwal — Teknik Analizi Anlamak ve Uygulamak

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Teknik Analizi Anlamak ve Uygulamak - Ravi Agarwal (65 sayfa) - @eseckal.pdf>) · [Tam metin](03_technical_agarwal.txt)

**Kaynak:** Bu bir başlangıç düzeyi proje raporu; baş-omuz, çift tepe/dip, trend ve destek/direnç kurallarını özetler (s. 30–45). Önceden iki kez direnç olan seviyenin kırıldıktan sonra desteğe dönüşü s. 43–44'te, hacmin güçlü fiyat hareketini teyidi s. 46–47'de. s. 57–65'teki 2009 Nifty raporları ileriye dönük performans örneklemi değildir. Anlatılan kalıplar önceki kitaplarla büyük ölçüde aynı; aşağıdaki aday yeni şekil değil **hacim koşulunun marjinal testi**dir.

### RA64 — Önceden iki kez sınanmış direncin hacimli kırılıp desteğe dönüşmesi

- **Seviye/olay:** TH63'ün iki teyitli H4 swing high ile dondurulan yatay direnç tanımını **aynen kullan**; böylece yeni bir pivot algoritması eklenmez. Kırılım H4 `close>level+0,1×ATR14` ve breakout barı base-volume `≥1,5×önceki20 H4 volume medyanı`; hacim medyanına breakout barı eklenmez. Sonraki en çok altı H4 içinde ilk `low≤level+0,1×ATR` ve `close>level` geri testi; short simetrik. Hacim eşiği bizim tanımımızdır.
- **İcra/risk:** TH63 ile aynı giriş, stop ve 2R/24 H4 süre kuralları; sinyal kapalı H4 sonrası ilk uygulanabilir 1m. Hacimli ve hacimsiz TH63 işlemleri eşlenerek hacim filtresinin net R, yanlış kırılım, işlem sayısı ve likidite dilimleri ölçülür. Hisse seansı ve rapordaki yuvarlak INR seviyeleri kriptoda ön koşul kabul edilmez.

## Ortak test sözleşmesi

Yalnız geçmişte kapanmış barlar, teyitli pivotlar ve dondurulmuş seviyeler kullanılacak. Sonraki uygulanabilir 1m dolumu, ücret, spread, kayma, perpetual funding, eksik veri ve çakışan pozisyon politikası dahil edilecek. Zaman sıralı ayrılmış doğrulamada işlem sayısı, net R, maksimum düşüş ve yalın taban çizgisi olmadan kârlılık iddiası kurulmaz.
