# Kitap okuma 058 — Sıkışma, kaynak OB ve destek/direnç mumu

**Kapsam:** 65 + 58 + 54 = **177 PDF sayfası**. Üç PDF'nin tüm sayfaları sıralı metne çıkarıldı; atıflar PDF sayfasıdır. Aşağıdaki kesin eşikler, kaynakta açıkça verilmedikleri yerde **bizim test vekilimizdir**. Backtest, paper test ve emir yapılmadı.

## 1. Frank Luther — Arz ve Talep Ticareti

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Arz ve Talep Ticareti - Frank Luther (65 sayfa) - @eseckal.pdf>) · [Tam metin](01_supply_demand_luther.txt)

**Kaynak:** Keskin hareketin çıktığı kısa yatay baz arz/talep alanıdır (s. 24–28); üst/alt fitil veya fitil-gövde karma sınırları tarif edilir (s. 26). İlk geri dönüşün taze bölge olduğu, çıplak dokunuş ile fiyat hareketi teyidi arasında giriş seçimi bulunduğu söylenir (s. 20–21, 28). Karşı bölgeye kadar ödül alanı kontrol edilir (s. 30). Son bölümde, daha yüksek zaman dilimi bölgesine yaklaşırken küçük zaman dilimi tepkilerinin giderek sıkışması/“compression” anlatılır, ama şekillerin çoğu görsel ve kural niteliktedir (s. 47–64). “Bankacıların” varlığına ya da sıkışmanın başarı oranına ilişkin işlem verisi sunulmaz. Bölge fikri batch055 PL55 ile büyük ölçüde örtüşür; bu kitaptan ayrı sınanacak ek fikir **yaklaşma biçimi**dir.

### FL58 — Taze H4 arz/talep bölgesine sıkışarak yaklaşma filtresi

- **Dondurulmuş bölge:** Batch055 PL55'in H4, 1–6 bar baz + kuvvetli ayrılış + ilk dönüş bölge tanımını aynen kullan; tanımı bu kitap için optimize etme. H4 bölge oluştuğu ikinci ayrılış mumu kapandığında kayıt açılır. Bu kitaptaki fitil/gövde kenarları PL55 ile uyumludur (s. 26). Bölge en çok 20 H4 bar geçerli ve ilk temas sonrası tüketilir.
- **Sıkışma, bizim ölçüm:** Bölgeye ilk temastan **önceki** son 6 tamamlanmış M15 bar içinde, arz bölgesine yaklaşan long yönlü fiyat için en az iki teyitli (1 sol/1 sağ) higher low ve son 3 M15'in ortalama true range'i önceki 3 M15'in ortalamasından küçük olmalı; talep bölgesine yaklaşan düşüş için iki lower high ve aynı range daralması. Son yaklaşma M15 kapanışında fiyat ile yakın bölge sınırı mesafesi `≤1×ATR14_M15` olmalı; ilk temas olayı bu kapanıştan **sonraki** barlarda aranır. Sıkışma daha sonra oluşursa geriye dönük filtreleme yapılmaz. Bu nicel tanım kaynağın çizimlerinden türetilmiş hipotezdir.
- **Giriş/risk:** Temas sonrası ilk tamamlanmış M15 mum arz için bölge yakın sınırının altında, talep için üstünde kapanırsa sonraki ilk uygulanabilir 1m giriş. Stop arz üst fitil sınırı `+0,1×ATR14_H4`, talep altı `−0,1×ATR`; 2R veya 12 H4 bar süre. Stop yanlış tarafta ya da maliyetin iki katından dar ise atla; aynı 1m stop/hedefte stop önce.
- **Karşılaştırma:** Aynı PL55 taze bölge olaylarını sıkışmalı/sıkışmasız gruplara ayır; ayrıca yalnız ilk temas ve teyitli girişin dolum/net R farkı. Sıkışma tanımını sonuçlara bakarak değiştirme.

## 2. James Jecool King — Gelişmiş Order Block Kılavuzu

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Gelişmiş Order Block Kılavuzu - James Jecool King (58 sayfa) - @eseckal.pdf>) · [Tam metin](02_advanced_ob_king.txt)

**Kaynak:** “Kaynak OB”, önceki gün/hafta/ay high-low veya ADR ekstremi yakınındaki dönüş mumu olarak tarif edilir; bullish için dipte down-close mumun high üstüne sonraki geçiş, bearish için tepedeki up-close mumun low altına geçiş teyidi kullanılır (s. 5–7, 11). Fiyatın bloğa geri gelişini bekleme ve karşı ekstrem ötesi stop vardır (s. 7–8, 11–12). H1 OB içinde M15 alt bölgeye daraltmanın stop ve RR'yi iyileştirebileceği görsel örneklenir (s. 13–21). Sonraki derleme bölümünde 1–6 mum baz, taze bölge, kuvvetli ayrılış ve puanlama bulunur (s. 26–30, 51–55); bunlar batch055 PL55 ve FL58 ile aynı hipotez ailesidir. “Kurumsal emir” ve örneklerdeki 5–11R sonuçlarının emir defteriyle doğrulaması yoktur.

### JK58 — Önceki gün ekstremindeki H1 kaynak OB ve M15 daraltma

- **Bağlam/OB:** UTC D1 son tamamlanmış high/low dondur. H1 long için sinyalden önceki en çok 4 tamamlanmış H1 içinde, önceki D1 low'a `≤0,25×ATR14_H1` mesafede low yapan **son down-close H1** mum; bearish için önceki D1 high yakınında son up-close H1. Seçilen mumun high/low'u H1 OB aralığı. OB ancak sonraki tamamlanmış H1 `close>OB high` (short `<OB low`) olduğunda teyitli; bu kapanıştan önce bölgeye limit yazılmaz. “Yakın”, 4 bar ve kapanış şartı bizim nesnelleştirmemiz; kaynak s. 6/11 high/low geçişi der.
- **Alt zaman dilimi kolu:** H1 OB'yi oluşturan dört tamamlanmış M15 mumu içinde long için son down-close M15, short için son up-close M15 seç; yoksa daraltma kolu işlem yapmaz. M15 alt bölge H1 bölgesinin içinde kalmalı ve genişliği H1 bölge genişliğinin en çok %60'ı olmalı. Bölge H1 teyit kapanışında **önceki M15 veriden** dondurulur; retest sırasında yeni M15 seçip daraltma yok. Temel kol tam H1 OB, ikinci kol bu önceden sabit M15 bölgedir.
- **Dolum/risk:** Teyitten sonraki 12 H1 içinde ilk geri dönüşte long için OB'nin üst sınırına, short için alt sınırına limit; 1m işlem seviyesi görülmezse dolum yok. Long stop seçili bölgenin low `−0,1×ATR14_H1`, short high `+0,1×ATR`; ayrıca **H1 orijinal ekstremi stop** kolunu ayrı değerlendir ki daraltmanın yapay olarak stop patlatma etkisi görülsün. Hedef 2R veya 24 H1 bar; aynı 1m stop/hedefte stop önce, yanlış tarafta/maliyetten dar stop atlanır. İlk testten sonra OB tüketilir.
- **Karşılaştırma:** PL55 ve önceki OB adaylarıyla olay örtüşmesi. M15 daraltma yüzünden kaçan dolumlar, stop oranı ve net R birlikte raporlanmalı; yalnız kazanmış örneklerin RR'sini kıyaslama.

## 3. Matt Anderson — Kazançlı Mum Kalıpları

[PDF](<D:/Paper_ML_BSH/Drive_PDF/PDFler/Baskı 1/Baskı 1/Kazançlı Mum Kalıpları - Matt Anderson (54 sayfa) - @eseckal.pdf>) · [Tam metin](03_candles_anderson.txt)

**Kaynak:** Çekiçte alt fitil en az 2×gövde ve önce düşüş (s. 8–10), kayan yıldızda üst fitil 2×gövde ve önce yükseliş (s. 14–16), marubozuda uzun gövde/kısa fitil (s. 25–28), yutanda karşı renkli iki gövdenin kapsanması (s. 29–31) anlatılır. Yükselen/düşen üç yöntem formasyonunda uzun yön mumu, onun aralığında üç küçük karşı/yatay mum, ardından yönlü kapanış vardır (s. 37–40). Giriş bağlamı destek/direnç, stop formasyon ekstremi ve en az 1,5R ödül (s. 42–49). Beş mumlu devam formasyonu, önceki tek/çift mum destek tepkisi adaylarından farklı test edilebilir fikir; “yüksek kazanma oranı” başlığı veri kanıtı değildir.

### MA58 — EMA yönünde beş mumlu üç yöntem devamı

- **Yön/ilk mum:** H4 gerçek OHLC. Long için ilk mum öncesinde son kapanmış H4 `EMA20>EMA50` ve her iki EMA son 3 H4 boyunca yükseliyor; short simetri. İlk mum long yeşil, gövdesi `≥1,2×ATR14_H4` ve aralığın en az %70'i gövde; short kırmızı. EMA ve ATR eşiği bizim trend/“uzun mum” vekilidir.
- **Konsolidasyon ve teyit:** İlk mumdan sonra **tam üç** tamamlanmış H4 mumun high/low'u ilk mum aralığının içinde kalır; her gövde `≤0,5×ilk gövde`. Sonraki beşinci H4 mum long `close>ilk mum high` ve yeşil, short `close<ilk mum low` ve kırmızı. Beşinci mum kapanmadan sinyal yok; kaynak son mumun ilk kapanış üstüne çıkmasını asgari sayar (s. 38), ilk **high/low** kırılımı bizim daha sıkı versiyonumuzdur. Üçten fazla orta mum için ayrı kol gerekebilir, ana kurala sonradan dahil etme.
- **İcra/risk:** Beşinci H4 kapanışından sonraki ilk uygulanabilir 1m giriş. Long stop orta üç mumun gözlenmiş min low'u `−0,1×ATR14_H4`; short max high `+0,1×ATR`; stop ilk mum ekstremi içinden geçiyorsa o mumun ekstremiyle daha geniş stop seçimi ayrı kol. 1,5R kaynak çıkış oranı, 2R ayrı kol; 12 H4 bar süre. Stop yanlış tarafta/maliyetin iki katından dar ise atla; aynı 1m stop/hedefte stop önce.
- **Karşılaştırma:** Önceki bayrak/inside-bar ve EMA devam adaylarıyla aynı sinyal anlarında olay örtüşmesi. Beş mum yapısının yalnız büyük yön mumu + EMA filtresine ek katkısını ölç.

## Ortak test notu

Önceden sabit varlık evreni, zaman sıralı ayrılmış değerlendirme, kapanmış mum/teyitli pivot, sonraki uygulanabilir 1m dolum, ücret/spread/kayma/funding ve eksik bar politikası gerekir. Çakışan pozisyonlar için tek kural belirle. Net R, işlem sayısı, dolum oranı, maksimum düşüş, alt dönemler ve basit taban çizgisi olmadan kârlılık yorumu yapılmaz.
