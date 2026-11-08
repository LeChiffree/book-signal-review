# PDF kitaplarından işlem sinyali adayları

## Kapsam ve karar ölçütü

Bu inceleme `Drive_PDF/PDFler` içindeki PDF'leri dosya bazında envantere alır; `all_pdf_screening.csv` her PDF için ayrı satırdır. **3.236 PDF'nin tamamı** dosya adı ve ilk üç PDF sayfasının metni açısından tarandı: 663.661 toplam sayfa, 9.704 örneklenen sayfa. 3.217 dosyada örnek metin okunabildi; 19 dosyanın ilk sayfalarında metin yok veya görüntü tabanlıydı. Okuma hatası veren dosya olmadı. Konu işaretleri bir kitabın tüm içeriği tarandığı anlamına gelmez. Bu **tam kitap okuması değildir**. Aşağıdaki yedi ana kaynak kitabın ilgili bölümleri ayrıca sayfa bazında okunmuştur. Dört eksik PDF `Drive_PDF/README.md` içinde listelidir.

İlk taramadaki konu izleri: hareketli ortalama 157 PDF, hacim/akış 179, ATR/volatilite 150, RSI/stokastik 132, Bollinger/Keltner 91, MACD 87, mum formasyonu 88, grafik formasyonu 82, kırılım/Donchian 64, ADX/DMI 29. Sayımlar birbirini dışlamaz; yalnız dosya adı veya ilk üç sayfada görülen terimlerdir.

Ekli kullanıcı notunun öncelikleri: yalnız karar anında bilinen kapalı mumlar; OHLCV'den üretilebilen nesnel tanımlar; formasyon olayı yanında geometri, yaş ve bağlam; her indikatöre kendi anlamına uygun dönüşüm; aynı özellikleri tekrar eklememe; maliyet sonrası, zaman sıralı test. Mevcut günlük strateji sözleşmesi `research_v2/24_MULTIDAY_STRATEGY_CONTRACT.md` ve mevcut 1.300 özelliklik BTC pilotu `research_v2/generated/multiday_btc_pilot/PILOT_REVIEW.md` ile karşılaştırıldı.

Buradaki maddeler **deney adaylarıdır**. Kitaptaki hisse senedi sonuçları kripto vadeli işlemlerine taşınmış bir performans kanıtı değildir.

## Öncelikli işlem kuralları

| Öncelik | Aday | Kapalı mumla hesaplanacak olay ve bağlam | Kaynak / not |
|---|---|---|---|
| 1 | **20 EMA geri çekilmesi + ADX/DMI** | `ADX14>20` ve yükseliyor; `+DI>-DI`; fiyat EMA20'ye geri geliyor, sonra önceki mum tepesini kırarak kapanıyor. EMA'ya yüzde/ATR uzaklığı ve ADX değişimi sürekli özellik olsun. Stop adayı: yalnız önceden onaylanmış salınım dibi veya ATR. | *ADX Göstergesi*, PDF s. 8, 27–28. Kitap emir tetikleyicisi kullanıyor; ilk günlük model için kapalı mum uyarlaması ayrı hipotezdir. |
| 2 | **Konsolidasyon kırılımı + göreli hacim** | `close_t > max(high[t-20:t-1])`; aynı anda `quote_volume_t / median(quote_volume[t-20:t-1])` ve `close_location_t`. Kırılım mesafesi ATR ile ölçeklensin. Düşük hacimli kırılım ayrı negatif örnek olarak tutulsun. | *Hacim Fiyat Analizi*, Anna Coulling, PDF s. 174–176; *20 EMA Stratejisi*, PDF s. 11–13, 24. Kaynakta hacimle doğrulanan kırılım anlatılıyor; 20 bar ve hacim eşiği deney parametresidir. |
| 3 | **Bollinger %B ile trend içi aşırı geri çekilme** | `close>SMA200`, `ADX10` ve BB(5,1) `%B` birlikte gözlensin; `%B<0.1` gibi derin geri çekilme olayı, gün sayısı, bant genişliği ve SMA uzaklığı ayrı alanlar olsun. Giriş/çıkış kuralları yalnız geçmişte sabitlenen limit ve `%B` dönüşü ile test edilsin. | *Bollinger Bantları – İşe Yarayan Trading Stratejileri*, Connors/Alvarez, PDF s. 5, 8–9. Kitaptaki $5, hisse hacmi ve %4–10 limitleri kriptoya aynen alınmamalı. |
| 4 | **Bullish engulfing + bağlam** | İkinci kapalı mumda olay; gövde oranı, alt/üst fitil, önceki 20 bar dibiyle uzaklık ve haftalık trend bağlamı. Yalın formasyon ve bağlamlı formasyon ayrı test edilmeli. | *Mum Formasyonları İçin Dürüst Bir Rehber*, Llewelyn James, PDF s. 43–48. Kitapta çıplak sinyal zayıf; çeşitli filtreler de çoğu zaman katkı sağlamamış. Kitabın bir hisse senedi testinde sonraki gün düşükten giriş, tepe kırılımı onayından daha iyi çıkmış; bu sonuç genellenemez. |
| 5 | **Hammer + önceki sert düşüş** | Alt fitil/gövde `>2`, üst fitil/aralık `<0.1`, önceki mum negatif ve gövdesi/aralığı `>0.5`; olaydan önceki dip ve RSI(2) bağlamı ayrı alanlar. Olayın ertesi mumunda oluşan koşul asla önceki karar satırına yazılmasın. | Aynı Llewelyn James kitabı, PDF s. 72–76. Kitaptaki optimize stop/hedef oranları ve hisse sonuçları yalnız deney girdisidir. |
| 6 | **MACD histogramı + DMI yönü** | `hist=(EMA12-EMA26)-EMA9(MACD)`; histogram/ATR seviyesi, 1 ve 5 mum değişimi, sıfır/sinyal kesişimi; `+DI>-DI` ile yön uyumu. Çıplak kesişim ve yön filtresi ayrı ablation. | *MACD Uzmanlığı*, Lalit Mohanty, PDF s. 8–10; *ADX Göstergesi*, PDF s. 8. MACD'nin fiyat birimi ATR ile normalize edilir. |
| 7 | **EMA20 üstü pivot kırılımı + hacim** | Önceki doğrulanmış pivot tepe oluşsun; geri çekilme boyunca kapanış EMA20 altına düşmesin; tepe üzerinde kapanış ve göreli hacim artışı. Pivot, yalnız geçmiş mumlarla onaylanmalı. | *20 EMA Stratejisi*, PDF s. 11–13, 24, 29–30. Kitaptaki hisse örnekleri seçilmiş görsellerdir, backtest sonucu değildir. |

**1. parti netleştirmesi:** Connors/Alvarez kitabındaki `%B`, **BB(5,1)** ile hesaplanıyor. Pilotun `bb_percent_b` sütunu aynı parametrelerle üretilmediği sürece kitap stratejisi için kullanılamaz. Tam kural [1. parti kaydında](batch_001/STRATEGIES.md).

### İkinci tur hipotezleri

- **Bollinger–Keltner sıkışma çıkışı + hacim:** Mevcut özellik matrisinde `bb_inside_kc` ve `bb_kc_squeeze_end` zaten var. Sıkışma sonrası yön, hacim ve kırılım mesafesi etkileşiminin ek katkısı test edilebilir. Bu fikir mevcut proje taslağından gelir; yukarıdaki kitaplardan doğrulanmış bir performans bulgusu değildir.
- **Kırılım başarısızlığı / retest:** Önceki aralık üzerinde kapanıştan sonra `k` gün içinde aralığa geri dönüşü ayrı olay say. Kırılımla aynı gün gelecek retest bilgisi kullanılmaz.
- **RSI bölgesi ve değişimi:** RSI 30/70 tek başına emir değildir; seviye, puan değişimi ve son 50 bar konumu, trend rejimiyle birlikte değerlendirilsin. RSI 0–100 ölçeğinde tutulmalı; EMA gibi yüzde fiyat farkına dönüştürülmemeli.

## Mevcut projeye bağlama

- Günlük karar satırı `(symbol, decision_time)` kalsın. Haftalık, 4h ve 1h bağlamı yalnız kapanmış veriyle bağlansın. 1m yol yalnız giriş/çıkış ve maliyet için kullanılsın.
- Mevcut pilotta ADX/DMI, Bollinger, Keltner, Supertrend ve birçok mum olayının sütunları zaten var. Yeni kitap bulguları öncelikle **olay seçimi ve ablation planı** üretir; 1.300 özelliği körlemesine büyütmez.
- İlk test paketi: yalnız günlük temel; ardından günlük+haftalık; sonra +4h özeti. Her pakette yukarıdaki olayların sürekli ölçülerine göre katkı bakılsın.
- Her aday için giriş, stop, hedef ve süre önceden sabitlensin; H3D/H7D/H14D ufukları ayrı değerlendirilsin. Ücret, kayma ve tarihsel funding sonuçtan düşülsün. Aynı 1m barda stop ve hedef birlikte görülürse projedeki konservatif stop önceliği uygulansın.
- Zaman sıralı walk-forward, 14 günlük örtüşen etiketler için purge/embargo, sembol/takvim ortak fold ve son dönem tek seferlik holdout kullanılsın. Kitapta görülen eşikler yalnız eğitim bölgesinde ayarlansın.
- *Kanıta Dayalı Teknik Analiz*, David Aronson, PDF s. 27–28 ve 454: long ağırlıklı bir kuralın genel yükselişten gelen getirisi öngörü gücü sanılabilir; daha karmaşık kurallar eğitimde iyileşirken testte bozulabilir. Bu nedenle buy-and-hold / basit trend kuralı karşılaştırması ve ablation zorunlu.

## İlk eleme

1. **Doğrudan işlem sinyali olarak ertele:** Pilot geçmişinde hiç görünmeyen rising/falling three methods, günlük/haftalık dragonfly–gravestone doji ve 4h morning star tanımları. Önce formasyon tanımını ve çok pariteli olay sıklığını doğrula.
2. **Doğrudan aktarma:** Hisseye özgü dolar fiyatı, pay adedi hacmi, borsa açılış boşluğu ve hisse endeksi `SPY` filtresi. Kripto OHLCV ve point-in-time piyasa bağlamı ile yeniden tanımlanabilir.
3. **Veri olmadan kullanma:** Emir defteri, tasfiye, açık pozisyon/funding kaynaklı işlem sinyalleri. Tarihsel ve karar anına uygun veri sağlanırsa ayrı deney olur.
4. **Öznel çizimleri otomatik sinyal sayma:** Wyckoff/Elliott/Wolfe, teyitsiz pivot ve elle seçilen üçgen/bayraklar. Önce mekanik olay tanımı ve olay sıklığı gerekir.

## Sınırlamalar

- Envanterdeki her PDF için satır vardır; ilk üç sayfanın taranması kitap içindeki bütün stratejileri bulma garantisi vermez. Ayrıntılı sayfa okuması yalnız yukarıda adı geçen kaynaklarda yapıldı. Görüntü tabanlı PDF'ler OCR gerektirir.
- Kitap performans rakamları karşılaştırılabilir kripto futures backtest'i değildir. Burada yeni model, kârlılık backtest'i veya paper işlem çalıştırılmadı.
- *Mum Formasyonları İçin Dürüst Bir Rehber* PDF s. 48'de, önceki paragrafta en iyi denilen hedef/stop ile “final rules” içinde yazılan değerler tutarsız. Parametreler kaynak doğrulanmadan aktarılmamalı.

## Okunan ana kaynaklar

- [ADX Göstergesi — Puneet Jain](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/ADX Göstergesi - Puneet Jain (41 sayfa) - @eseckal.pdf>) (PDF s. 8, 27–28)
- [20 EMA Stratejisi — Jayesh Shah](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/20 EMA Stratejisi - Jayesh Shah (31 sayfa) - @eseckal.pdf>) (PDF s. 11–13, 24, 29–30)
- [Bollinger Bantları — Connors ve Alvarez](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 11/Baskı 11/Bollinger Bantları - İşe Yarayan Trading Stratejileri - Connors Research - Laurence Connors ve Cesar Alvarez (37 sayfa) - @eseckal.pdf>) (PDF s. 8–9)
- [Mum Formasyonları İçin Dürüst Bir Rehber — Llewelyn James](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 19/Baskı 19/Mum Formasyonları İçin Dürüst Bir Rehber - Hedefe Yönelik Trading - Llewelyn James - Orijinal (176 sayfa) - @eseckal.pdf>) (PDF s. 43–48, 72–76, 173)
- [Hacim Fiyat Analizi — Anna Coulling](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 12/Baskı 12/Hacim Fiyat Analizi - Bu Kitabı Okuyan Piyasaları Okur - Anna Coulling (272 sayfa) - @eseckal.pdf>) (PDF s. 174–176)
- [MACD Uzmanlığı — Lalit Mohanty](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 18/Baskı 18/MACD Uzmanlığı - Lalit Mohanty (37 sayfa) - @eseckal.pdf>) (PDF s. 8–10)
- [Kanıta Dayalı Teknik Analiz — David R. Aronson](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 11/Baskı 11/Kanıta Dayalı Teknik Analiz - David R. Aronson (470 sayfa) - @eseckal.pdf>) (PDF s. 27–28, 454)
