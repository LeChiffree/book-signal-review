# Filtre Laboratuvarı — Yöntem ve Kapsam

## Amaç

525 Binance USDT-M perpetual üzerinde, 120 benzersiz high/medium mekanik kuralı
14 rejim filtresiyle ayrı ayrı test etmek. Filtreler giriş anında uygulanır;
stop/hedef takibi yine 1m OHLC üzerindedir. Fee, slippage ve funding dahildir.

## Filtreler

| # | ID | Kural |
|---:|---|---|
| 0 | `btc_trend` | BTC kapanışı 200 günlük SMA üzerinde |
| 1 | `btc_mom` | BTC 30 günlük getirisi pozitif |
| 2 | `btc_calm` | BTC 20 günlük oynaklığı 1 yıllık medyanın altında |
| 3 | `fng_greed` | Fear & Greed endeksi >= 50 |
| 4 | `fng_fear` | Fear & Greed endeksi <= 25 |
| 5 | `liquidity` | 30 günlük dolar hacmi yatay kesit medyanının üzerinde |
| 6 | `breadth` | Sembollerin >= %50'si 50 günlük SMA üzerinde |
| 7 | `rel_strength` | Sembolün 30 günlük getirisi BTC'den güçlü |
| 8 | `symbol_trend` | Sembol kapanışı 200 günlük SMA üzerinde |
| 9 | `near_high` | Sembol 90 günlük zirvesinin >= %80'inde |
| 10 | `low_vol` | Sembol 20 günlük oynaklığı yatay kesit medyanının altında |
| 11 | `volume_surge` | Sinyal barı hacmi 20 barlık medyanın 1.5 katından fazla |
| 12 | `funding_pos` | Son funding oranı pozitif |
| 13 | `funding_neg` | Son funding oranı negatif |

Fear & Greed verisi `api.alternative.me/fng` üzerinden tarihsel olarak çekildi
(`filter_layer/data/fear_greed.csv`).

## Test edilen kapsam

- **525 sembol**
- **120 benzersiz kural** test edildi (1d: 65, 4h: 25, 1h: 24, 1w: 6); bunlardan **116'sı** işlem üretti
- **14 filtre + filtresiz baz** → 1.738 geçerli strateji × filtre satırı (işlem üretenler)
- Filtreler **tek tek** uygulanır; `fng_greed` ve `fng_fear` aynı anda doğru olamaz.
- 5m/15m filtre katmanına alınmadı: brüt kenar zaten negatif, 219M işlemde
  filtre durumlarının maliyeti karşılaması beklenmiyor. 5m/15m baz sonuçları
  ana raporda ayrı durur.

## Önemli yöntem notu

Her filtre için ayrı non-overlap durumu tutulur. Bir filtre bir işlemi kabul
etmezse o filtrenin sonraki sinyali bloke olmaz; bu nedenle filtreli sonuçlar
"aynı işlem listesinden sonradan seçme" değil, giriş filtresinin gerçek
simülasyonudur.

## Çıktılar

- `filter_layer/filter_dashboard.html` — interaktif dashboard
- `filter_layer/dashboard_data.json` — tüm strateji × filtre sonuçları
- `filter_layer/results/trades/*.parquet` — sembol bazında kabul edilmiş işlemler
- `filter_layer/data/daily_masks.parquet` — günlük rejim maskeleri
- `filter_layer/data/filter_defs.json` — filtre tanımları

## Dashboard

- Sol: **01 Timeframe → 02 Strateji → 03 Filtre → 04 görünüm**. Sağ üstte ayrıca filtre switch box vardır.
- Sağ: 17 interaktif ECharts grafiği:
  - iki $10/işlem kasa eğrisi (tüm dönem + 2025–2026)
  - iki günlük kâr/zarar histogramı (tüm + 25–26)
  - günlük işlem sayısı (tüm + 25–26)
  - yıllık, mevsimsel, çeyreklik kâr/zarar
  - aylık heatmap, hafta günü
  - kalma süresi histogramı
  - Long/Short
  - getiri–kalma scatter
  - filtre etkisi (ortalama + medyan)
- Fontlar: Inter + JetBrains Mono yerel woff2; grafik motoru yerel ECharts.
- Eleme: toplam işlem başı net **ve** 2026 işlem başı net aynı anda negatifse sonuç dışarıda bırakılır.
- Varsayılan sıralama **medyan sembol neti**; tabloda ortalama işlem başı net de görünür. "Sadece pozitif" varsayılan olarak açıktır.
