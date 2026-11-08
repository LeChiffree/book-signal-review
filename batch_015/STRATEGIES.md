# Kitap okuma 015 — Önceki gün kırılımı, üç vektör retesti, 123 dönüşü

**Kapsam:** Üç PDF'nin **18 + 26 + 93 = 137 PDF sayfası** işlendi. PDF sayfa numaraları kullanılır. AK47 dosyasının s. 15–25 bölümü s. 2–12'nin İngilizce karşılığıdır; iki ayrı kitap veya bağımsız kanıt değildir. Aşağıdaki stratejiler ileride test için hipotezdir. Bu partide backtest, paper test veya emir yok.

## 1. Karl Dittmann — 100 Pips Kur ve Unut Stratejisi

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 8/Baskı 8/100 Pips Kur ve Unut Stratejisi - Karl Dittmann (18 sayfa) - @eseckal.pdf>)

Kaynak USD/JPY için **18:00 EST–18:00 EST** önceki 24 saatlik H/L'yi alır (s. 10–11), `H+7 pip` buy stop ve `L-7 pip` sell stop koyar; her yön üç eşit emir: hedef 15, 35, 50 pip, ortak 25 pip stop (s. 12–13). Dolmayan emirler sonraki 18:00'den önce iptal, karşı yöndeki emirlerin ilk tetikte iptali isteğe bağlı (s. 13, 15). Önceki aralık `>150 pip` ise işlem yok (s. 17). Metin “limit emir” diyor; seviyenin dışında kırılım bekleyen emirler **stop giriş** olarak modellenmeli. “100 pip” üç emrin pip sonuçlarını topluyor; eşit toplam sermaye/riskte tek pozisyonun 100 pip hareketi değildir. S. 16'daki “çok nadiren” tam stop örneği için sıklık verisi yok.

### D15 — Tam gün yüksek/düşük dışına stop emirleri

- **Nedensel seviye:** Kriptoda her UTC 00:00 anında son tam günün `H,L` değerleri sabitlenir. Kaynak saati FX Asya seansına aittir; UTC gün sınırı **bizim** uyarlamamızdır. Baz aday: long stop `H+0.1 ATR14_D1[t-1]`, short stop `L-0.1 ATR`; `0.1 ATR` ve `range/ATR14_D1<=2` eşiği sabit pip/150 pip yerine bizim ölçek seçimimiz. Kaynağı birebir FX test etmek istersek EST saat tanımı ve yaz saati ayrıca kesinleştirilmeli.
- **Emir ve risk:** İki yön OCO; bir yön 1m içinde tetiklenince diğer yön iptal. Üç eşit alt pozisyonun **toplam** stop riski tek işlem risk tavanına sığar. Stop mesafesi `0.35 ATR14_D1`; hedefler stop mesafesinin `0.6R,1.4R,2R` katı, kaynak 15:35:50 hedeflerinin 25 pip stopa oranıdır. Yani toplam işlem hedefe kadar giderse alt pozisyonların kârı ortalama `1.33R`, kaynakta iddia edilen “100 pip” şeklinde raporlanmaz. Emirler ertesi UTC 00:00'da yenilenir/iptal. Açık pozisyonların gün sınırında kapatılması ve stop/hedefe kadar taşınması **ayrı** deneyler; kaynak bekleyen emir iptalini söyler, açık pozisyonu açıkça kapatmaz. Aynı 1m mumda iki yön görülürse sıralama belirsiz işaretlenir. PDH/PDL kırılım ailesiyle olayları çift sayma.

## 2. Siya Vezi — AK47 Scalping Stratejisi

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 9/Baskı 9/AK47 Scalping Stratejisi - Türkçe ve İngilizce - Siya Vezi (26 sayfa) - @eseckal.pdf>)

M15'te son dip/tepe, H1'de ayrıca önceki gün dip/tepe izlenir (İngilizce s. 20–24). Geçerli seviye için dipten önce aşağı, tepe öncesi yukarı **üç “vektör”/itki ve düzeltme** istenir; seviyenin testinde hemen ters işlem (s. 21–24). Destek/direnç veya arz/talep yapısıyla ikinci teyit tavsiye edilir (s. 20). “Vektör” için algoritma, seviyeye ne kadar yakınlık ve test mumunun kapanışı kaynakta tanımlı değil. Asya seansında %80 reddedilme, 80–100 pip hareket ve 30 pip azami ters hareket (s. 25) örneklemli istatistik değildir, kriptoya taşınmaz. Kaynağın **anında dokunuşta giriş** fikri kapalı mum sinyaliyle birebir aynı değildir.

### A15 — Üç teyitli swing sonrası ilk seviye reddi

- **Bizim M15 nesnelleştirmemiz:** Fraktal dip, solda/sağda ikişer tamamlanmış M15 barının low'undan düşük ve ancak sağdaki ikinci bar kapandıktan sonra bilinir. Son 48 M15 içinde en az üç **teyitli** daha düşük swing low ve aralarında teyitli düzeltici swing high varsa düşüş vektörleri hazır; tepe/short simetrik. `48 bar`, fraktal genişliği ve üç swing eşlemesi bizim algoritmamız; kaynak “üç vektör”ü sayısal anlatmaz. Alternatif H1 kohortunda PDH/PDL son tam UTC günden alınır.
- **Sinyal:** Önceden bilinen son fraktal low/PDL için ilk M15 `low<=level+0.1 ATR14_M15[t-1] && close>level && close>open` long; high/PDH için ters. Giriş ancak bu bar kapandıktan sonraki ilk 1m, stop reddeden mumun ekstremumu `±1 tick`, 2R hedef ve 4/8/16 M15 zaman çıkışı. `0.1 ATR`, kapanış teyidi ve çıkışlar bizim temkinli uyarlamamız. Kaynağın anında test emri ayrıca ancak seviyenin önceden dondurulduğu limit emir simülasyonuyla ayrı incelenebilir; iki yöntemin dolum ve risk farkı raporlanır. Batch 005 swing ve batch 011 PDH/PDL reddi ile aynı olaylara bağlanır.

## 3. Cam White derlemesi — 6 Basit Forex Trading Stratejisi

[Kaynak PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 8/Baskı 8/6 Basit Forex Trading Stratejisi - Cam White (93 sayfa) - @eseckal.pdf>)

Derleme farklı yazarların bölümlerini içerir (içindekiler s. 4). İşlem bakımından: Jody Samuels'ın **123 dönüş/devam** kuralı (s. 27–31); Cecil Robles'ın üst zaman dilimi EMA50 + Williams %R geri çekilmesi (s. 40–49); Casey Stubbs'ın stop/hedef konumlandırma yaklaşımı (s. 56–59); Sterling Suhr'ın önceki dönüm noktası etrafında kırılma/teyit/geri çekilme kuralı (s. 66–70); hacim ve özel yazılım tanıtımı (s. 76–84); Londra açılışı ve **Nadex ikili opsiyon** bağlamı (s. 86–92). S. 40/54/89/92 başarı yüzdeleri denetlenmiş performans sayılmaz. Banka “manipülasyonu” OHLCV ile gözlenmiş niyet değildir.

### F15a — 123 dönüşünde ikinci noktanın kırılması

- **Kaynak:** Zirvede nokta 1 yeni high, nokta 2 sonraki dip, nokta 3 daha düşük tepe; 2 altına kırılınca short; stop 3 veya daha geniş 1, hedef 2–3 mesafesi kadar izdüşüm. Dip için simetri (s. 27–30). 3 noktasının 1–2 hareketinin en az %50'sini geri alması ve 1–3 arasında 10–20 bar tercih, kesin zorunlu değil (s. 28–29). Trend devamı aynı 123 yapısının başka bağlamı (s. 30–31).
- **Bizim H1 sözleşmesi:** Fraktal pivotlar `left=2,right=2` kapalı H1 barlarıyla **teyit tarihinden itibaren** kullanılır. Short için en son teyitli `P1=high`, sonra `P2=low`, sonra `P3=high` ve `P3<P1`; P1–P3 10–20 H1 bar, `(P3-P2)/(P1-P2)>=0.5`. P3 teyidinden sonra ilk `close<P2-1 tick` short; long tam simetri. `10–20` ve %50 baz filtresi kaynaktaki tercihleri zorunlu hale getiren **bizim varyantımız**; filtresiz 123 karşılaştırması yapılır. Sonraki 1m giriş, stop P3 `+1 tick` veya P1 `+1 tick` ayrı; hedef girişten `abs(P3-P2)` uzaklıkta veya 2R. Kırılım öncesi P3 geleceği kullanılmaz. Önceki M/W ve swing dönüş adaylarıyla olay örtüşmesi saklanır.

### F15b — Üst zaman dilimi EMA50 yönünde Williams %R geri dönüşü

- **Kaynak:** Üst grafikte EMA50 son yaklaşık 10 barın eğimi yönü belirler (s. 43–44). Alt grafikte fiyat EMA50'nin karşı tarafına kapanır, Williams %R long için `-80` altına girip tekrar üstüne çıktığında sinyal; sinyal mumunun high'ı üstünde buy stop; yakın teyitli swing dibinin altında stop (s. 44–47). 2R lehte hareketten sonra SMA5 altında **iki kapanış** ve bu iki mumun low'u kırılmasıyla izleyen çıkış örneği (s. 48–49). Williams %R periyodu metin/görselde teyit edilmeden kaynak parametresi sayılamaz.
- **Bizim H4/D1 varyant:** Yalnız son kapanmış D1 `EMA50[t]>EMA50[t-10]` long; H4'te daha önce `close<EMA50_H4`, ardından `%R14[t-1]<-80 && %R14[t]>=-80`. `14` bizim standartlaştırmamız. H4 sinyal high `+1 tick` buy stop bir sonraki H4 geçerli; stop son teyitli H4 swing low `-1 tick`; short tam simetri `%R` -20 eşiğiyle. 2R sabit hedef baz; ayrıca 2R görülünce SMA5 altında/üstünde iki **tam H4 kapanış** sonrası sonraki bar kırılımı ile çıkış varyantı. D1 trend bilgisi olay anında kapanmış olmalı. S. 43 “Günlük ve H4” deyip “1 saatlik işlem” de dediği için zaman dilimi karışıklığı var; bu H4 seçimi bizim tutarlı sürümümüz.

**Diğer fikirler:** Sterling Suhr'ın üç mumlu seviye reddi s. 68–70, batch 011 DP11a ve batch 013 A13 ile çok yakın. Metinde “Adım #2” ayrıntısı PDF'de eksik görünüyor; tam kaynak dizisi gibi kodlanmaz. Nadex Londra saatleri, haber takvimi, USD endeksi, opsiyon kullanım fiyatı/son vade kuralı (s. 89–92) 24/7 spot/perp kripto OHLCV ile eşdeğer değildir. Hacim bölümü özel Phoenix göstergesi olmadan doğrulanabilir giriş vermiyor.

## Test notu

Öncelik F15a/F15b ve D15'in mevcut kırılım stratejilerine ek değerini ölçmek; A15 çok öznel “vektör” nedeniyle daha düşük güvenli. Tüm adaylarda UTC kapanış, dondurulmuş seviye, 1m yürütme, ücret/spread/kayma/funding, stop–hedef çakışması, dolmayan stop emirleri, dış örneklem ve aynı işlem çakışması kaydedilmeli. Üç kaynakta geçen getiri/başarı yüzdelerinden beklenen kâr çıkarılmaz.
