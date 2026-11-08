# Book Signal Review — Backtest Engine

Mechanical, fee-inclusive backtests of the strategy sections extracted from
`batch_001` … `batch_215` of the book-signal review.

## What is here

| File | Purpose |
|---|---|
| `specs_final.json` | 454 extracted sections → tested/excluded specs with family, timeframe, confidence and expressions |
| `bookbt.py` | Data loaders, indicators, expression DSL, 1m execution, fees, funding and metrics |
| `families.py` | Strategy archetypes used by the catalog |
| `auto_catalog4.py` | Classifies sections and emits `specs_final.json` |
| `run_all.py` | Parallel 58-symbol runner; writes per-symbol summaries |
| `run_all_525.py` | Parallel 525-symbol runner using `bookbt525.py`; writes `results_525/` |
| `bookbt525.py` | 525-symbol data adapter: 1h/4h parquet, 1d from 1h, 5m/15m from 1m, 525 funding |
| `aggregate.py` | Aggregates per-symbol summaries into `dashboard_data.json` / `strategy_metrics.csv` |
| `aggregate_525.py` | Runs the 525-symbol aggregation with the correct 1/525 allocation |
| `build_dashboard.py` | Generates the self-contained `dashboard.html` |
| `build_report.py` | Generates `REPORT.md` |
| `cache_htf.py` | One-time cache for the 58-symbol higher-timeframe CSVs |
| `results_525/` | 525-symbol per-symbol summary and monthly parquet files |
| `dashboard.html` | Final interactive dashboard |
| `REPORT.md` | Written summary of findings and caveats |

## Method in one paragraph

Signals are generated only on completed strategy-timeframe bars. Entry is the
first 1m open after the signal bar closes. Stops and targets are checked on 1m
OHLC; if both are touched in the same 1m bar, the stop is assumed first. Time
and signal exits occur at the next 1m open. One position per symbol per
strategy. Costs are Binance USDT-M taker fee **5 bps per side**, slippage
**2 bps per side**, plus historical 8h funding. The test window is
**2022-08-01 → 2026-08-31** for signals; 1m execution data extends to
**2026-10-18**.

## Reproduce

```powershell
cd D:\Paper_ML_BSH\analysis\book_signal_review\backtest

# 1. Build the catalog (only needed if sections/classification changed)
python -u auto_catalog4.py

# 2. One-time higher-timeframe cache
python -u cache_htf.py

# 3. Run all 525 symbols; resumes by skipping symbols with a summary file
python -u run_all_525.py --workers 12

# 4. Aggregate and build outputs (1/525 allocation)
python -u aggregate_525.py
python -u build_dashboard.py
python -u build_report.py
```

`run_all_525.py` is resumable: a symbol is skipped when
`results_525/summary/<SYMBOL>.parquet` already exists. Use `--force` to overwrite.
Use `--symbols BTCUSDT,ETHUSDT` or `--tfs 1d` for a quick check.

## Reading the results

- **Avg net** is the mean return per trade after fees, slippage and funding.
- **Median symbol net** gives each symbol one vote and is the default ranking
  metric; it resists a single new-listing outlier.
- **Portfolio** allocates 1/525 of capital to each trade and compounds monthly.
  It is a conservative equal-weight deployment; idle symbols leave cash
  uninvested.
- **Confidence** is the mapping confidence (`high` / `medium`). Low-confidence
  mappings are excluded from the main results and listed at batch level.
- **Unique rules:** 274 source mappings collapse to 166 unique engine rules.
  Duplicates share identical expressions and parameters; the explorer marks
  them with ×N and defaults to unique rules.
- **Gross vs net** isolates the cost stack. The gap is roughly 10–13 bps per
  round trip plus funding.

## Caveats

This is a first-pass mechanical proxy, not an exact replication of every
discretionary book rule. Complex patterns (SMC, Elliott, harmonic, Wyckoff,
TD sequential, divergence), non-crypto assets, options/FX and pure
exit/position-sizing variants are excluded with reasons. New listings can
produce extreme trades; rankings use median symbol net and symbol consistency.
See `REPORT.md` and the dashboard’s **Method & caveats** tab for details.
