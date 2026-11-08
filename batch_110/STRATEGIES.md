# Kitap okuma 110 — iki kademeli Fibonacci geri çekilmesi

**Kapsam:** Üç özgün PDF'nin **14 + 10 + 19 = 43 sayfası** baştan sona okundu. Thomas Wood PDF'sinde s. 1–13 metin katmanı boş olduğu için [s. 1–7](wood_1_7.jpg), [s. 8–14](wood_8_14.jpg) ve [özellikle 11–13](wood_page_11.jpg) görsel incelendi. Atıflar PDF sayfasıdır. Backtest, paper test veya emir yapılmadı.

## 1. Haftalık Gelir İçin Basit Kurulumlar — Thomas Wood

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 26/Baskı 26/Haftalık Gelir İçin Basit Kurulumlar - Thomas Wood - Orijinal (14 sayfa) - @eseckal.pdf>) · [Çıkarılan metin](01_weekly_wood.txt) · [Görseller 1–7](wood_1_7.jpg) · [Görseller 8–14](wood_8_14.jpg)

**Tam görsel okuma:** S. 1–3 kapak ve içindekiler, s. 4–6 psikoloji, s. 7–9 momentum osilatörüyle fiyat ayrışması, s. 9–10 yatay pivot kırılımıyla trend dönüşü, s. 11–12 Kicker mum boşluğu, s. 12–13 momentum kırılımı/sıkışma, s. 14 tanıtım. S. 11'de yükseliş Kicker'ı önceki mum gövdesinin tamamen üstünde açılıp kapanan, önceki trende zıt renkli mum; düşüşü ters. Yazar özellikle 4h+ grafik ve yalnız düzenli RTH seansı kullanan vadeli veri önerir. Bu çekirdek [3. partideki C3](../batch_003/STRATEGIES.md) açılış boşluğu gerektiren Kicker ailesinin aynısıdır; yeni aday sayılmadı. Kicker'ı 24/7 kripto mumlarına gap atarak taşımak farklı hipotez olur. S. 7–10 ayrışma ve yatay yapı kırılımı, s. 12–13 sıkışma kırılımı da arşivdeki ailelerle örtüşür. Başarı ve gelir örnekleri bağımsız performans kanıtı değildir.

## 2. Çift Vuruş Fibonacci Stratejisi — J Crawford

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 2/Baskı 2/Çift Vuruş Fibonacci Stratejisi - J Crawford (10 sayfa) - @eseckal.pdf>) · [Tam metin](02_double_fib_crawford.txt)

**Tam okuma:** S. 1–3 giriş/Fibonacci; s. 4–6 CL vadeli işlemde %50 ve %61,8 düzeylerine yarımşar giriş, %78,6 stop; s. 7–10 USDCAD D1 ikinci örnek ve sonuç. S. 5 rakamları: 49,83 ile 49,79 giriş, ikisi dolarsa 49,81 ortalama, 49,70 stop. S. 8'de USDCAD iki limit, s. 10'da ikinci limitin **altı seans sonra** dolduğu anlatılır; belirsiz emir ömrünü tek mum varsayamayız. Kaynak fiyatın yükseliş swing'inin hangi gecikmeli algoritmayla seçileceğini ve kâr çıkışını kesin vermez. %50/%61,8 düzeylerinin özel olasılık iddiası gösterilmiş istatistik değildir.

### JC110A — %50/%61,8 yarım pozisyon girişleri ve %78,6 ortak stop

- **Kaynak (s. 4–6, 8–10):** Önceki yükseliş dip `L`→tepe `H` hareketinde `F50=H−0,5(H−L)`, `F618=H−0,618(H−L)`, `F786=H−0,786(H−L)`. Her iki düzeyde hedef pozisyonun yarısı için long limit; iki dolumda maliyet öncesi ortalama fiyat `0,5 F50+0,5 F618`; ortak stop F786. Kaynak belirgin olarak **parça parça dolumu** ve ikinci parçanın günler sonra gelmesini içerir. Düşüş salınımındaki kısa taraf simetrisi **bizim araştırma genişletmemizdir**, kaynak örnekleri yalnız long.
- **Nesnel kapalı mum sürümü:** CL vadeli 5m ve USDCAD D1 iki ayrı kaynak pazarı. Pivot `L`, iki sol ve iki sağ tamamlanmış barda daha düşük low ile teyit edilir; sonrasında `H`, aynı 2+2 sağ teyidiyle ilk daha yüksek high. İki pivot da ancak sağ teyit barı kapandığında bilinir; `H>L`, hareket en az `2×ATR14` değilse sinyal yok (**bizim** filtre). İkinci pivot teyit tarihinde fiyat F50'nin altına inmişse geçmişe limit doldurma yapılmaz, o kurulum atlanır. Sonraki uygulanabilir M1/quote akışında iki 0,5 büyüklükte limit bırak. İlk dolumdan önce tek bacağın potansiyel kaybı, ikinci dolum dahil en kötü toplam risk 0,5% hesap özsermayesini aşmayacak büyüklükte olsun. İlk dolumdan sonra ikinci limit en çok 6 tam işlem seansı aktif (**bizim**, örnekteki altı gün üst sınır değildir); dolmazsa iptal, ilk bacak açık kalır. Her iki bacak için F786 stop, fiyat düzeyi yönüne uygun tick ve maliyet düzeltmesi. İlk dolumdan sonra F786 görülürse diğer limit de iptal. Hedef her dolmuş bacak için eski `H` testi, ardından toplam sepetin kapanışı; hedef kaynakta yok, **bizim**. En çok 10 seans tutma **bizim**. Stop/hedef aynı M1 içinde belirsizse stop önce; limit dolmayan kurulumlar dahil, spread, ücret, kayma ve CL roll/USDCAD hafta boşluğu raporlanır.
- **Ayrışma/test:** [22. partideki](../batch_022/STRATEGIES.md) tek %50 limit ve [42. partideki](../batch_042/STRATEGIES.md) %61,8 teyitli tek girişten farklı bilgi, **iki kademenin dolum/pozisyon riski yoludur**. Aynı teyitli swing evreninde %50 tek, %61,8 tek ve iki kademeli kolların dolma oranı, koşullu getiri, toplam risk ve maliyet sonrası net R'si karşılaştırılacak. Veri üzerinde sonradan “en güzel” swing'i seçmek veya pozisyonu iki dolum gerçekleşmiş gibi tüm kurulumlara yazmak yasak.

## 3. Forex — Investing People / Valeriano

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 18/Baskı 18/Forex - Investing People - Valeriano (19 sayfa) - @eseckal.pdf>) · [Tam metin](03_forex_valeriano.txt)

**Tam okuma:** S. 1–6 tanıtım ve risk; s. 7–9 mekanik/takdire bağlı ayrımı; s. 10–15 SwingFX günlük trend başlangıcı “JOT”, çift dip/tepe ve grafik; s. 16–19 seminer/tanıtım. Giriş “mum formasyonu high/low kırılımı”, stop “formasyon veya swing dışı”, hedef “istatistiksel sistem” olarak geçer ama bu sistemin hesabı, JOT'un kesin mum tanımı, pivot teyidi ve zaman sınırı kitapta yok. Çift dip/tepe ve trend başlangıcı kırılımı önceki adaylarla örtüşür. Yeni aday sayılmadı. S. 8'de 10.000 test işlemiyle ileri test başarısızlığının yalnız %1 olacağı iddiası, örneklem/bağımsızlık ve model seçimi bilgisi olmadan geçerli istatistik sonucu değildir.

## Sonuç

**1 yeni aday:** JC110A. Wood ve Valeriano fikirleri okunup mevcut adaylara eşlendi.
