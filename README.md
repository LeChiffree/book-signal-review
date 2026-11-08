# Book Signal Review

Mechanical, fee-inclusive backtests of book-derived trading rules on Binance
USDT-M perpetual futures. The repository contains the strategy catalog, the
backtest engine, the 525-symbol results, the ECharts dashboard and the filter
laboratory.

## What is included

- `batch_001` … `batch_215` — extracted strategy sections and source notes.
- `backtest/bookbt.py` — data loaders, indicators, expression DSL, 1m execution,
  stop/target/time exits, fees, slippage and funding.
- `backtest/bookbt525.py` — 525-symbol data adapter.
- `backtest/run_all_525.py` — resumable 525-symbol runner.
- `backtest/aggregate.py` / `build_dashboard.py` / `build_report.py` — baseline
  525-symbol dashboard and report.
- `backtest/results_525/` — per-symbol summary and monthly parquet results.
- `backtest/filter_layer/` — 14-filter laboratory:
  - `filter_dashboard.html` — main ECharts dashboard
  - `dashboard_data.json` — full aggregated data (including daily series,
    hold-time buckets, cash curves and scatter samples)
  - `FILTER_REPORT.md` / `FILTER_LAYER.md`
  - `results/trades/` — filtered trade records per symbol
  - `data/` — daily regime masks and Fear & Greed history
  - `assets/` — local ECharts build and fonts

## Data policy

Raw candle data is **not** included. The scripts expect the local archive at:

```text
D:\1mDataBinance
  active_525\futures_bars\1h
  active_525\futures_bars\4h
  active_525\funding
  1m\<SYMBOL>\<SYMBOL>-1m-YYYY-MM.parquet
```

The `backtest/cache/` directory (1m/HTF caches) is intentionally git-ignored.
To use another root, change `DATA` in `bookbt.py` or set the path in the adapter.

## Reproduce

```powershell
cd backtest
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r ..\requirements.txt

# 525-symbol baseline
python -u run_all_525.py --workers 12

# Baseline dashboard
python -u aggregate_525.py
python -u build_dashboard.py
python -u build_report.py

# Filter laboratory (uses local candle archive)
python -u filter_layer\prepare_filters.py
python -u filter_layer\run_filters.py --workers 12
python -u filter_layer\aggregate_filters.py
python -u filter_layer\build_filter_dashboard_v2.py
python -u filter_layer\report_filters.py

# Serve the filter dashboard locally
cd filter_layer
python -m http.server 8000 --bind 0.0.0.0
```

Then open `http://127.0.0.1:8000/filter_dashboard.html` (or the machine's LAN IP).

## Method snapshot

- Signals are generated on completed strategy-timeframe bars.
- Entry is the first 1m open after the signal bar closes.
- Stops/targets are checked on 1m OHLC; if both touch in the same 1m bar, stop
  is assumed first.
- Signal/time exits occur at the next 1m open. One position per symbol/strategy.
- Taker fee 5 bps per side, slippage 2 bps per side, historical 8h funding.
- Weekly bars are resampled from daily; 1d from 1h; 5m/15m from 1m.
- Confidence is `high` / `medium` for tested rules; low-confidence mappings are
  listed but excluded from the main results.

## Important caveats

- These are mechanical proxies, not exact replications of discretionary rules.
- The broad 525-symbol universe is materially harsher than the earlier
  58-symbol liquid subset; results are universe-sensitive.
- The filter layer tests each of 14 filters separately (strategy × filter), not
  every 2^14 AND subset.
- 5m/15m rules are included in the baseline report but not in the filter matrix:
  their gross edge is already negative and the trade count is enormous.
- Past performance is not a guarantee of future returns.
