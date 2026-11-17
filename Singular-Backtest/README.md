# Singular-Backtest — Book Signal Review

Bu klasör, Book Signal Review deposundaki kural laboratuvarının **tekil işlem**
(Singular-Backtest) varyantını üretir. Normal sonuçlara (`backtest/filter_layer/`)
hiçbir şekilde dokunulmaz; tüm çıktılar bu klasörde tutulur.

## Kural

Seçilen kapsamda **aynı coinde aynı anda en fazla bir açık işlem** bulunabilir.
Önceki işlem kapanmadan gelen yeni giriş sinyali bloke edilir. Aynı giriş anında
öncelik: kısa zaman dilimi (1h > 4h > 1d > 1w), sonra long > short, sonra `sid`.

## Neden varsayılan kapsam `family`?

Book motoru her kural (`sid`) için filtre başına zaten tek pozisyon tutar ve
filtre akışları birbirinden bağımsız ilerler. Bu nedenle **tek kural düzeyinde
tekil kural, normal sonuçla birebir aynıdır** (`--scope=spec` bir no-op'tur).
Anlamlı tekillik, aynı kural ailesinin farklı kuralları ve zaman dilimleri aynı
coinde üst üste pozisyon açtığında ortaya çıkar.

| Kapsam | Anlam | Bloke oranı (baseline) |
|---|---|---|
| `family` (varsayılan) | Aynı kural ailesi, tüm spec ve TF'ler birlikte | ~%49 |
| `portfolio` | Tüm Book portföyü, coin başına tek işlem | ~%95 |
| `spec` | Tek kural (`sid`) | %0 (motor zaten tekil) |

## Sonuçlar (varsayılan `family`, 525 sembol)

| Metrik | Normal | Singular | Fark |
|---|---|---|---|
| İşlem | 12.390.388 | 6.296.608 | −6.093.780 (%49,18 bloke) |
| Ortalama getiri | −0,1686% | −0,1620% | +0,0066 puan |
| Kasa (10$ sabit) | −208.953$ | −101.997$ | +106.956$ |

Kasa farkı büyük ölçüde işlem sayısının yarıya inmesinden gelir; işlem başına
ortalama getiri neredeyse aynı kalır. Bloke edilen işlemler ortalamada normal
portföyle benzer kalitededir, ancak sayı yarıya indiği için toplam zarar da
yaklaşık yarıya iner.

## Dosyalar

- `run_singular.py` — tek geçişli üretici (parquet → JSON/CSV).
- `verify_singular.py` — bağımsız doğrulama (kapsama, bloke muhasebesi, parquet
  sayımları, örnek kapsam kabul sayıları, toplam formülleri).
- `results/singular_results.json` — dashboard için tam payload.
- `results/singular_rows.csv` — 1.738 satır (spec × filtre) normal/singular.
- `results/singular_coins.csv` — spec × coin kırılımı (baseline).
- `results/run_manifest.json`, `run.log`, `verify.log`.

## Kullanım

```bash
python Singular-Backtest/run_singular.py
python Singular-Backtest/run_singular.py --scope=portfolio
python Singular-Backtest/run_singular.py --scope=spec --symbols=20   # hızlı test
python Singular-Backtest/verify_singular.py
```

Normal metrikler `backtest/filter_layer/dashboard_data.json` sonuçlarından
birebir alınır; singular metrikler `results/trades/*.parquet` işlem
kayıtlarından yeniden hesaplanır. `retAll` = işlem başına ortalama net × 100,
`kasaAll` = toplam net × 10$'dır. Tekil işlemlerde kâr/zarar günleri çıkış
gününe göre sayılır.
