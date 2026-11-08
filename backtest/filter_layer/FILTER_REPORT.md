# Filtre Laboratuvarı — 525 Sembol Raporu

**Kapsam:** 525 sembol · 120 benzersiz kural test edildi (116’sı işlem üretti; 1d/4h/1h/1w) · 14 filtre · 1738 strateji × filtre sonucu

**Maliyet:** 5 bps taker/side, 2 bps slippage/side, tarihsel 8s funding. Sinyal stratejinin kendi timeframe’inde; giriş/stop/hedef 1m OHLC’de.

## Özet

- Pozitif ortalama işlem başı getiri (toplam veya 2026): **645 / 1738** sonuç.
- En az 50 işlem, 15 sembol ve pozitif medyan sembol neti koşulunu geçen: **119** sonuç.
- Eleme: yalnızca **hem toplam hem 2026 takvimi** işlem başı neti negatif olan sonuçlar dışarıda bırakıldı.
- Filtresiz bazı en az 30 işlem olan 114 stratejiden **92** tanesinde en az bir filtre bazdan daha iyi ortalama net üretti.
- 5m/15m filtre katmanına alınmadı; brüt kenar zaten negatif ve 219M işlemde filtre maliyeti karşılamıyor.

## Filtre bazında pozitiflik

| Filtre | Test | Pozitif | Pozitif medyan ort. | İşlem |
|---|---|---|---|---|
| BTC 200g SMA üzerinde | 116 | 69 | -0.11% | 6412141 |
| BTC 30g getirisi pozitif | 116 | 44 | 0.26% | 6881723 |
| BTC oynaklığı 1y medyanın altında | 116 | 56 | 0.05% | 6932675 |
| Korku/Açgözlülük >= 50 | 116 | 53 | -0.07% | 5506401 |
| Korku/Açgözlülük <= 25 | 116 | 38 | 0.13% | 3278930 |
| Likidite medyanın üzerinde | 116 | 40 | 0.05% | 6141963 |
| Piyasa genişliği >= %50 | 116 | 38 | 0.09% | 3676957 |
| Sembol 30g getirisi BTC’den güçlü | 116 | 28 | -0.67% | 4087878 |
| Sembol 200g SMA üzerinde | 116 | 30 | 0.01% | 2937368 |
| Sembol 90g zirvesinin %80’inde | 116 | 48 | 0.15% | 3204038 |
| Sembol oynaklığı medyanın altında | 116 | 43 | 0.05% | 6270668 |
| Hacim 20 barlık medyanın 1.5 katı | 115 | 55 | 0.05% | 5942853 |
| Son funding pozitif | 116 | 33 | 0.03% | 10198642 |
| Son funding negatif | 115 | 39 | 0.13% | 2703827 |

## En güçlü sonuçlar (medyan sembol neti)

| SID | TF | Filtre | İşlem | Sembol | Ort. net | 2026 | Med. sembol | PF | Portföy |
|---|---|---|---|---|---|---|---|---|---|
| BW83A | 1d | Sembol 200g SMA üzerinde | 248 | 177 | 1.28% | 1.34% | 5.87% | 1.16 | 0.6% |
| BW83A | 1d | Sembol 30g getirisi BTC’den güçlü | 412 | 271 | 0.53% | 0.79% | 3.94% | 1.06 | 0.4% |
| BW83A | 1d | Sembol 90g zirvesinin %80’inde | 252 | 189 | 0.68% | 0.98% | 3.51% | 1.10 | 0.3% |
| P3 | 1d | Sembol 200g SMA üzerinde | 146 | 112 | 3.26% | 8.41% | 3.46% | 1.76 | 0.9% |
| M33 | 1w | Sembol 200g SMA üzerinde | 1196 | 297 | 5.60% | 6.27% | 3.33% | 1.55 | 13.4% |
| P2 | 1d | BTC 30g getirisi pozitif | 1406 | 430 | 2.92% | 2.95% | 2.59% | 1.48 | 8.0% |
| P3 | 1d | Son funding negatif | 561 | 257 | 2.39% | -1.17% | 2.44% | 1.58 | 2.6% |
| I2 | 1d | BTC 200g SMA üzerinde | 3775 | 428 | 2.32% | 7.18% | 2.05% | 1.37 | 17.6% |
| DH86 | 1d | Korku/Açgözlülük <= 25 | 1368 | 453 | 1.60% | 1.56% | 2.03% | 1.26 | 4.2% |
| P2 | 1d | Son funding negatif | 1542 | 365 | 2.80% | 2.17% | 1.98% | 1.56 | 8.5% |
| DH86 | 1d | Son funding negatif | 914 | 332 | 1.25% | 0.64% | 1.89% | 1.20 | 2.2% |
| DH86 | 1d | Likidite medyanın üzerinde | 1385 | 342 | 0.70% | 0.75% | 1.88% | 1.10 | 1.8% |
| I2 | 1d | Korku/Açgözlülük >= 50 | 3195 | 413 | 2.10% | 7.37% | 1.79% | 1.32 | 13.1% |
| B29b | 1d | Korku/Açgözlülük <= 25 | 600 | 309 | 1.59% | 1.79% | 1.75% | 1.26 | 1.8% |
| P3 | 1d | Hacim 20 barlık medyanın 1.5 katı | 818 | 368 | 2.55% | 0.05% | 1.68% | 1.55 | 4.0% |
| FM91A | 1d | Son funding negatif | 1546 | 392 | 1.15% | -0.93% | 1.66% | 1.20 | 3.4% |
| KD181A | 1d | Sembol oynaklığı medyanın altında | 663 | 215 | 2.36% | 23.52% | 1.63% | 1.23 | 3.0% |
| I2 | 1d | BTC 30g getirisi pozitif | 4278 | 506 | 1.50% | 2.38% | 1.59% | 1.22 | 12.4% |
| BW83A | 1d | Son funding negatif | 498 | 265 | 0.75% | -0.12% | 1.48% | 1.16 | 0.7% |
| BW83A | 1d | Likidite medyanın üzerinde | 476 | 222 | 0.92% | 1.63% | 1.43% | 1.17 | 0.8% |

## Yöntem notu

- Her filtre ayrı bir giriş koşulu olarak, kendi non-overlap durumuyla simüle edildi; filtrelenmiş işlemler sonradan seçilmedi.
- Filtreler tek tek test edildi. “Tüm kombinasyonlar” burada **strateji × filtre** kombinasyonlarıdır; 14 filtrenin tüm 2^14 alt kümesi değildir.
- `fng_greed` ve `fng_fear` aynı anda doğru olamaz; bu nedenle 14 filtrenin AND’i tanımsızdır.
- Eleme kuralı: toplam işlem başı net **ve** 2026 takvimi işlem başı net aynı anda negatifse sonuç dışarıda bırakılır.
- 5m/15m baz sonuçları ana raporda ayrıca durur; bu filtre laboratuvarı 1d/4h/1h/1w kuralarına odaklanır.

## Dosyalar

- `filter_dashboard.html` — interaktif dashboard
- `dashboard_data.json` — tüm sonuçlar ve günlük seriler
- `strategy_filter_metrics.csv` — tablo
- `results/trades/*.parquet` — kabul edilmiş işlemler
