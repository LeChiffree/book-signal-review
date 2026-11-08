# Book Signal Review — Mechanical Backtest Report

**Scope:** 215 batch folders · 454 extracted strategy sections · 274 high/medium-confidence mechanical proxies (166 unique engine rules) · 525 Binance USDT-M perpetuals

**Window:** signals 2022-08-01 → 2026-08-31; 1-minute execution data through 2026-10-18.

**Costs:** Binance USDT-M taker fee 5 bps per side, slippage 2 bps per side, historical 8h funding included. One position per symbol per strategy.

---

## Executive summary

- **145 of 215 batches** produced at least one high/medium-confidence mechanical test. 23 batches contain only low-confidence mappings, 14 are excluded, and 33 have no strategy sections.
- **Fast timeframes are dominated by costs.** The average 5m trade is -0.044% gross and -0.144% net; the round-trip cost stack is 0.100%. Only 1% of symbol-spec pairs are positive.
- **4h has the best average net per trade** (-0.10%), but the broad-universe edge is thin and uneven: daily average net -0.22%, median symbol net -0.680%, 21% of daily specs positive, 39% of symbol-spec pairs positive. The 4h shelf averages -0.099% net with a -0.219% median symbol; the 1w shelf is a small 7-spec sample with -4.86% average net.
- **Buy & hold is a high bar.** BTC returned 238% and the equal-weight crypto basket -42% over the window. The median daily portfolio is -7.2%; most mechanical proxies do not beat the benchmark after costs.
- **Best robust proxies in the broad universe:** BW83A (1d, bb, median symbol 1.20%), P2 (1d, rsi, median symbol 0.91%), DH86 (1d, bb, median symbol 0.60%), I2 (1d, ichimoku, median symbol 0.58%), I16a (4h, ichimoku, median symbol 0.13%).

---

## Timeframe scorecard

All figures are fee-inclusive. “Portfolio” compounds monthly returns with 1/525 capital per trade; “median symbol net” gives each symbol one vote and resists single-listing outliers.

| TF | Specs | Trades | Avg gross | Avg net | Cost drag | Med. symbol net | Symbols + | Med. portfolio | Specs + |
|---|---|---|---|---|---|---|---|---|---|
| 5m | 41 | 178,101,415 | -0.044% | -0.144% | 0.100% | -0.144% | 1% | -100.0% | 0% |
| 15m | 18 | 20,259,558 | -0.062% | -0.161% | 0.099% | -0.160% | 5% | -96.6% | 0% |
| 1h | 37 | 15,275,869 | -0.071% | -0.167% | 0.096% | -0.178% | 18% | -63.8% | 0% |
| 4h | 46 | 3,786,022 | -0.016% | -0.099% | 0.083% | -0.219% | 36% | -16.3% | 13% |
| 1d | 119 | 1,626,138 | -0.164% | -0.221% | 0.058% | -0.680% | 39% | -7.2% | 21% |
| 1w | 7 | 19,180 | -4.240% | -4.860% | 0.621% | -7.179% | 36% | -4.9% | 29% |

## Universe sensitivity

- Earlier 58-symbol liquid subset: daily average net 0.82%, median symbol net 0.079%, median portfolio 11.6%.
- Current 525-symbol active universe: daily average net -0.22%, median symbol net -0.680%, median portfolio -7.2%.
- The sign reversal is a universe-selection result, not a parameter tweak: the 58-symbol set was concentrated in liquid majors, while the broad set includes many new and low-liquidity listings.

---

## Most consistent strategies

Filter: at least 30 trades, at least 5 symbols, positive median symbol net and at least half of symbols positive. Sorted by median symbol net.

| SID | Batch | Strategy | TF | Family | Trades | Symbols | Avg net | Med. symbol net | Symbols + | Portfolio | Max DD | Win | PF | Conf. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BW83A | 083 | BW83A — D1 SMA20 yönünde H1 Bollinger 2σ/3σ aşırılığından dönüş | 1d | bb | 1,259 | 429 | 0.62% | 1.20% | 57% | 1.5% | -1.3% | 53% | 1.12 | high |
| P2 | 002 | P2 — Kırılım emri tetiklenmeden önce iptal | 1d | rsi | 4,681 | 495 | 1.24% | 0.91% | 57% | 11.3% | -3.7% | 49% | 1.20 | high |
| DH86 | 086 | DH86 — RSI14 üzerinde Bollinger zarfından yeniden içeri giriş | 1d | bb | 3,359 | 492 | 0.61% | 0.60% | 54% | 3.8% | -2.3% | 53% | 1.09 | high |
| I2 | 004 | I2 — Bulut rejiminde Tenkan/Kijun ve fiyat/Kijun kesişimleri | 1d | ichimoku | 7,952 | 511 | 0.69% | 0.58% | 55% | 9.7% | -7.5% | 46% | 1.10 | high |
| I16a | 016 | I16a — H4 Tenkan/Kijun kesişimi | 4h | ichimoku | 47,828 | 520 | 0.22% | 0.13% | 55% | 20.8% | -7.2% | 43% | 1.08 | high |
| RT152A | 152 | RT152A — EMA12/35 çaprazı, CMF sıfır teyidi ve ilk EMA12 retesti | 4h | ma_cross | 35,166 | 518 | 0.30% | 0.07% | 52% | 19.2% | -13.8% | 27% | 1.08 | high |
| VW87 | 087 | VW87 — VWMA10/21 kapanış kesişimi | 1d | ma_cross | 5,765 | 467 | -0.35% | 0.03% | 50% | -4.8% | -15.7% | 42% | 0.95 | high |
| P3 | 002 | P3 — “Hızlanmazsa azalt” ve iki aşamalı çıkış | 1d | cci_rev | 1,766 | 442 | 1.11% | 0.03% | 50% | 3.7% | -1.8% | 52% | 1.21 | high |

---

## Best batches

| Batch | SID | Strategy | TF | Med. symbol net | Symbols + | Portfolio | Trades |
|---|---|---|---|---|---|---|---|
| 083 | BW83A | BW83A — D1 SMA20 yönünde H1 Bollinger 2σ/3σ aşırılığından dönüş | 1d | 1.20% | 57% | 1.5% | 1259 |
| 002 | P2 | P2 — Kırılım emri tetiklenmeden önce iptal | 1d | 0.91% | 57% | 11.3% | 4681 |
| 086 | DH86 | DH86 — RSI14 üzerinde Bollinger zarfından yeniden içeri giriş | 1d | 0.60% | 54% | 3.8% | 3359 |
| 004 | I2 | I2 — Bulut rejiminde Tenkan/Kijun ve fiyat/Kijun kesişimleri | 1d | 0.58% | 55% | 9.7% | 7952 |
| 016 | I16a | I16a — H4 Tenkan/Kijun kesişimi | 4h | 0.13% | 55% | 20.8% | 47828 |
| 152 | RT152A | RT152A — EMA12/35 çaprazı, CMF sıfır teyidi ve ilk EMA12 retesti | 4h | 0.07% | 52% | 19.2% | 35166 |
| 087 | VW87 | VW87 — VWMA10/21 kapanış kesişimi | 1d | 0.03% | 50% | -4.8% | 5765 |

---

## Coverage and exclusions

- Tested batches: **145**
- Low-confidence only: **23**
- Excluded only: **14**
- No strategy sections: **33**
- Tested proxies: **274**; unique engine rules: **166**; with at least one trade: **268**
- Excluded sections: **59**

Per-batch status and the exact reason for each exclusion are in the dashboard’s **Batch coverage** tab and in `dashboard_data.json`.

---

## Method

- Signals are generated only on completed strategy-timeframe bars. Entry is the first 1m open after the signal bar closes.
- Stops and targets are checked on 1m OHLC. If stop and target are both touched in the same 1m bar, the stop is assumed first (conservative).
- Time and signal exits occur at the next 1m open. One position per symbol per strategy; no pyramiding or overlapping entries.
- Fees: 5 bps per side; slippage: 2 bps per side; funding: historical 8h rates charged to the position side.
- 1h/4h bars come from the local parquet archive; 5m/15m are resampled from 1m, 1d is resampled from 1h, and weekly bars from daily. Signals cover 2022-08 through 2026-08; 1m execution data extends through 2026-10-18.
- Portfolio return allocates 1/525 of capital to each trade and compounds monthly. It is a conservative equal-weight deployment; idle symbols leave cash uninvested. It is therefore not directly comparable to a fully invested buy-and-hold benchmark.

## Caveats

- This is a **first-pass mechanical proxy**, not an exact replication of discretionary book rules. Mapping confidence is shown per strategy (`high`, `medium`, `low`); low-confidence mappings are excluded from the main results.
- New listings can produce extreme single-trade returns. Rankings use median symbol net and symbol consistency; average net and portfolio return are shown with that caveat.
- The universe is the 525-symbol active USDT-M set in the local archive; symbols enter at their first available bar, so survivorship/listing bias remains.
- Cross-sectional, breadth, pairs, portfolio-rotation and options/FX/US-equity strategies are out of scope for this single-symbol engine.
- Taker fills are assumed. Maker execution, rebates or lower slippage would materially improve the fast timeframes.

## Files

- `dashboard.html` — interactive dashboard (self-contained).
- `strategy_metrics.csv` — per-strategy metrics.
- `dashboard_data.json` — full data used by the dashboard.
- `results_525/summary/*.parquet` — per-symbol, per-strategy metrics.
- `results_525/monthly/*.parquet` — per-symbol monthly PnL.
- `results_525/errors/*.json` — per-symbol expression errors, if any.
