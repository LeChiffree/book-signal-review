# Book Signal Review — 525 Sembol Backtest Özeti

**Kapsam:** 215 batch, 454 strateji bölümü, 274 high/medium mekanik proxy (166 benzersiz kural), 525 Binance USDT-M perpetual.

**Dönem:** sinyaller 2022-08-01 → 2026-08-31; 1m execution 2026-10-18'e kadar.

**Maliyet:** Binance USDT-M taker 5 bps/side, slippage 2 bps/side, tarihsel 8s funding dahil. Sinyal stratejinin kendi timeframe'inde; giriş, stop ve hedef takibi 1m OHLC'de.

## Ana sonuç

| TF | Spec | İşlem | Ort. net | Medyan sembol net | Semboller + | Medyan portföy |
|---|---:|---:|---:|---:|---:|---:|
| 5m | 41 | 178.1M | -0.144% | -0.144% | 1% | -100.0% |
| 15m | 18 | 20.3M | -0.161% | -0.160% | 5% | -96.6% |
| 1h | 37 | 15.3M | -0.167% | -0.178% | 18% | -63.8% |
| 4h | 46 | 3.8M | -0.099% | -0.219% | 36% | -16.3% |
| 1d | 119 | 1.6M | -0.221% | -0.680% | 39% | -7.2% |
| 1w | 7 | 19.2k | -4.860% | -7.179% | 36% | -4.9% |

- **Hiçbir timeframe geniş evrende pozitif medyan üretmiyor.** 5m/15m/1h maliyet nedeniyle net negatif; 4h ve 1d'de de medyan sembol negatif.
- **Benchmark:** BTC +237.7%; 525 sembollük eşit ağırlıklı sepet -42.5%.
- **En iyi medyan sembol netleri:** BW83A +1.20% (1d), P2 +0.91% (1d), DH86 +0.60% (1d), I2 +0.58% (1d), I16a +0.13% (4h). Ancak 166 benzersiz kuraldan yalnızca 8'i pozitif medyan üretiyor; bu genel bir edge değil.

## Kritik bulgu: evren seçimi

58 sembollük likit alt kümede 1d sonucu pozitifti:

- 58 sembol: ort. net **+0.82%**, medyan sembol **+0.079%**, medyan portföy **+11.6%**
- 525 sembol: ort. net **-0.22%**, medyan sembol **-0.680%**, medyan portföy **-7.2%**

Aynı kurallar, aynı maliyetler; fark yalnızca evren. 58 sembollük sonuç seçilmiş likit coinlere bağlıydı ve geniş evrene genellenemiyor.

## Dosyalar

- `dashboard.html` — interaktif dashboard
- `REPORT.md` — İngilizce detaylı rapor
- `strategy_metrics.csv` — strateji metrikleri
- `dashboard_data.json` — dashboard verisi
- `results_525/summary/*.parquet` — sembol × strateji özetleri
- `results_525/monthly/*.parquet` — aylık PnL
- `final_overview.png`, `final_strategies.png`, `final_batches.png`, `final_method.png` — ekran görüntüleri

## Uyarılar

- Bu, kitaptaki her disiplinli kuralın birebir replikasyonu değil; high/medium confidence mekanik proxy'lerdir. 59 bölüm kapsam dışı, 121 düşük güvenli eşleme ana sonuçlara alınmadı.
- Yeni listingler ve düşük likidite aşırı işlem getirileri üretebilir; sıralama medyan sembol netine göre yapıldı.
- Taker fill varsayıldı. Maker/rebate veya daha düşük slippage hızlı timeframe'leri iyileştirebilir; mevcut sonuçlarda maliyet baskın.
