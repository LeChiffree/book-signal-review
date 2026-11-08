import os, sys, json, time, argparse, glob
from concurrent.futures import ProcessPoolExecutor, as_completed
import numpy as np
import pandas as pd

BT = r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest'
sys.path.insert(0, BT)
import bookbt as bt
import bookbt525

bookbt525.install()

SPECS_PATH = os.path.join(BT, 'specs_final.json')
OUT = os.path.join(BT, 'results_525')
CONF = ('high', 'medium')
ALLOC_N = 525


def load_specs(tfs):
    specs = json.load(open(SPECS_PATH, encoding='utf-8'))
    specs = [s for s in specs if s.get('status') == 'tested' and s.get('confidence') in CONF]
    keep = set(tfs)
    if '1d' in keep:
        keep.add('1w')
    return [s for s in specs if s['tf'] in keep]


def metrics(trades, alloc):
    if not trades:
        return None
    nets = np.array([t['net'] for t in trades], dtype=float)
    nets = nets[np.isfinite(nets)]
    if len(nets) == 0:
        return None
    eq = np.cumprod(1.0 + nets * alloc)
    peak = np.maximum.accumulate(eq)
    dd = float((eq / peak - 1.0).min()) if len(eq) else 0.0
    pos = nets[nets > 0]
    neg = nets[nets < 0]
    gp = float(pos.sum()) if len(pos) else 0.0
    gl = float(-neg.sum()) if len(neg) else 0.0
    sd = float(nets.std(ddof=1)) if len(nets) > 1 else 0.0
    first = min(t['entry_time'] for t in trades)
    last = max(t['exit_time'] for t in trades)
    years = max((last - first) / (365.25 * 24 * 3600 * 1000), 1 / 365.25)
    sharpe = float(nets.mean() / sd * np.sqrt(len(nets) / years)) if sd > 0 else 0.0
    return dict(
        n=len(nets),
        win_rate=float((nets > 0).mean()),
        avg_net=float(nets.mean()),
        median_net=float(np.median(nets)),
        total_net=float(nets.sum()),
        portfolio_net=float(eq[-1] - 1.0),
        max_dd=dd,
        profit_factor=float(gp / gl) if gl > 0 else (float('inf') if gp > 0 else 0.0),
        gross_profit=gp,
        gross_loss=gl,
        fee_sum=float(sum(t.get('fee', 0.0) for t in trades)),
        funding_sum=float(sum(t.get('funding', 0.0) for t in trades)),
        avg_hold_h=float(np.mean([(t['exit_time'] - t['entry_time']) / 3_600_000 for t in trades])),
        long_n=int(sum(1 for t in trades if t['side'] == 1)),
        short_n=int(sum(1 for t in trades if t['side'] == -1)),
        long_net=float(sum(t['net'] for t in trades if t['side'] == 1)),
        short_net=float(sum(t['net'] for t in trades if t['side'] == -1)),
        sharpe=sharpe,
        first_entry=int(first),
        last_exit=int(last),
        years=float(years),
    )


def one_symbol(args):
    sym, specs, tfs = args
    t0 = time.time()
    d = bt.prepare_symbol(sym, tfs=tfs, load_minute=True)
    if not d.get('m1'):
        return sym, 0, 'no 1m data', time.time() - t0
    summaries = []
    monthlies = []
    errors = []
    for s in specs:
        try:
            trades = bt.run_strategy(s, d)
            if trades and isinstance(trades[0], dict) and 'error' in trades[0]:
                errors.append({'idx': s['idx'], 'sid': s['sid'], 'error': str(trades[0]['error'])})
                continue
            trades = [t for t in trades if 'net' in t]
            if not trades:
                continue
            m = metrics(trades, 1.0 / ALLOC_N)
            base = {'idx': s['idx'], 'sid': s['sid'], 'batch': s['batch'], 'title': s['title'],
                    'family': s['family'], 'tf': s['tf'], 'confidence': s['confidence'],
                    'symbol': sym}
            base.update(m)
            summaries.append(base)
            ts = pd.to_datetime([t['exit_time'] for t in trades], unit='ms', utc=True)
            nets = np.array([t['net'] for t in trades], dtype=float)
            mm = pd.DataFrame({'month': ts.strftime('%Y-%m'), 'pnl': nets / ALLOC_N,
                               'pnl_simple': nets, 'n': 1})
            mm = mm.groupby('month', as_index=False).sum()
            mm['idx'] = s['idx']; mm['symbol'] = sym
            monthlies.append(mm)
        except Exception as e:
            errors.append({'idx': s['idx'], 'sid': s['sid'], 'error': repr(e)})
    sdf = pd.DataFrame(summaries)
    mdf = pd.concat(monthlies, ignore_index=True) if monthlies else pd.DataFrame()
    os.makedirs(os.path.join(OUT, 'summary'), exist_ok=True)
    os.makedirs(os.path.join(OUT, 'monthly'), exist_ok=True)
    os.makedirs(os.path.join(OUT, 'errors'), exist_ok=True)
    if not sdf.empty:
        sdf.to_parquet(os.path.join(OUT, 'summary', f'{sym}.parquet'), index=False)
    if not mdf.empty:
        mdf.to_parquet(os.path.join(OUT, 'monthly', f'{sym}.parquet'), index=False)
    if errors:
        json.dump(errors, open(os.path.join(OUT, 'errors', f'{sym}.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    return sym, len(sdf), f'{len(errors)} errors', time.time() - t0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--limit', type=int, default=0)
    ap.add_argument('--workers', type=int, default=6)
    ap.add_argument('--symbols', type=str, default='')
    ap.add_argument('--tfs', type=str, default='5m,15m,1h,4h,1d')
    ap.add_argument('--force', action='store_true')
    args = ap.parse_args()
    tfs = tuple(t for t in args.tfs.split(',') if t)
    specs = load_specs(tfs)
    syms = bt.symbols()
    if args.symbols:
        keep = set(args.symbols.split(','))
        syms = [s for s in syms if s in keep]
    if not args.force:
        done = {os.path.basename(p)[:-8] for p in glob.glob(os.path.join(OUT, 'summary', '*.parquet'))}
        syms = [s for s in syms if s not in done]
    if args.limit:
        syms = syms[:args.limit]
    os.makedirs(OUT, exist_ok=True)
    print(f'symbols={len(syms)} specs={len(specs)} tfs={tfs} workers={args.workers}', flush=True)
    tasks = [(s, specs, tfs) for s in syms]
    t0 = time.time()
    with ProcessPoolExecutor(max_workers=args.workers) as ex:
        futs = {ex.submit(one_symbol, t): t[0] for t in tasks}
        for i, f in enumerate(as_completed(futs), 1):
            sym = futs[f]
            try:
                r = f.result()
                print(f'[{i}/{len(syms)}] {r[0]} rows={r[1]} {r[2]} {r[3]:.1f}s total={time.time()-t0:.0f}s', flush=True)
            except Exception as e:
                print(f'[{i}/{len(syms)}] {sym} FAILED {e!r}', flush=True)
    print('done', round(time.time() - t0, 1), flush=True)


if __name__ == '__main__':
    main()
