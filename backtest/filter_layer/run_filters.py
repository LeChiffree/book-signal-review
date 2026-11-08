import os, sys, json, time, argparse, glob, hashlib, collections
from concurrent.futures import ProcessPoolExecutor, as_completed
import numpy as np
import pandas as pd

BT = r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest'
sys.path.insert(0, BT)
import bookbt525

bookbt525.install()
import bookbt as bt
from filter_layer.engine import build_bar_masks, run_filtered

OUT = os.path.join(BT, 'filter_layer', 'results')
DATA = os.path.join(BT, 'filter_layer', 'data')
CONF = ('high', 'medium')
TFS = ('1h', '4h', '1d')
TARGET_TFS = {'1h', '4h', '1d', '1w'}

_DAILY = None


def load_daily_masks():
    global _DAILY
    if _DAILY is None:
        d = pd.read_parquet(os.path.join(DATA, 'daily_masks.parquet'))
        d['ts'] = d['ts'].astype('int64')
        _DAILY = {k: g[['ts', 'mask']].sort_values('ts').reset_index(drop=True)
                  for k, g in d.groupby('symbol', sort=False)}
    return _DAILY


def _key(s):
    k = lambda x: '' if x is None else str(x)
    return hashlib.md5(f"{s['tf']}|{s['family']}|{k(s.get('entry_long'))}|{k(s.get('entry_short'))}|{k(s.get('stop'))}|{k(s.get('time'))}".encode()).hexdigest()


def unique_specs():
    specs = json.load(open(os.path.join(BT, 'specs_final.json'), encoding='utf-8'))
    tested = [s for s in specs if s.get('status') == 'tested' and s.get('confidence') in CONF
              and s.get('tf') in TARGET_TFS]
    groups = collections.defaultdict(list)
    for s in tested:
        groups[_key(s)].append(s)
    leads = []
    for g in groups.values():
        leads.append(min(g, key=lambda x: (x['batch'], x['sid'])))
    leads.sort(key=lambda s: (s['batch'], s['sid']))
    return leads


def one_symbol(sym):
    t0 = time.time()
    dm = load_daily_masks()
    daily = dm.get(sym)
    d = bt.prepare_symbol(sym, tfs=TFS, load_minute=True)
    if not d.get('m1'):
        return sym, 0, 'no 1m', time.time() - t0
    specs = unique_specs()
    mask_cache = {}
    rows = []
    errors = []
    for s in specs:
        tf = s['tf']
        if tf not in d['tf']:
            continue
        if tf not in mask_cache:
            mask_cache[tf] = build_bar_masks(d, d['tf'][tf], daily)
        try:
            trades = run_filtered(s, d, mask_cache[tf])
            if trades and isinstance(trades[0], dict) and 'error' in trades[0]:
                errors.append({'idx': s['idx'], 'sid': s['sid'], 'error': str(trades[0]['error'])})
                continue
            rows.extend(trades)
        except Exception as e:
            errors.append({'idx': s['idx'], 'sid': s['sid'], 'error': repr(e)})
    df = pd.DataFrame(rows)
    os.makedirs(os.path.join(OUT, 'trades'), exist_ok=True)
    os.makedirs(os.path.join(OUT, 'errors'), exist_ok=True)
    if not df.empty:
        df.to_parquet(os.path.join(OUT, 'trades', f'{sym}.parquet'), index=False)
    else:
        pd.DataFrame(columns=['idx', 'sid', 'tf', 'symbol', 'side', 'entry_time', 'exit_time',
                              'net', 'gross', 'accepted_mask', 'cond_mask']).to_parquet(
            os.path.join(OUT, 'trades', f'{sym}.parquet'), index=False)
    if errors:
        json.dump(errors, open(os.path.join(OUT, 'errors', f'{sym}.json'), 'w', encoding='utf-8'),
                  ensure_ascii=False, indent=1)
    return sym, len(df), f'{len(errors)} errors', time.time() - t0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--workers', type=int, default=12)
    ap.add_argument('--symbols', type=str, default='')
    ap.add_argument('--limit', type=int, default=0)
    ap.add_argument('--force', action='store_true')
    args = ap.parse_args()
    syms = bt.symbols()
    if args.symbols:
        keep = set(args.symbols.split(','))
        syms = [s for s in syms if s in keep]
    if not args.force:
        done = {os.path.basename(p)[:-8] for p in glob.glob(os.path.join(OUT, 'trades', '*.parquet'))}
        syms = [s for s in syms if s not in done]
    if args.limit:
        syms = syms[:args.limit]
    print(f'symbols={len(syms)} unique_specs={len(unique_specs())} workers={args.workers}', flush=True)
    t0 = time.time()
    with ProcessPoolExecutor(max_workers=args.workers) as ex:
        futs = {ex.submit(one_symbol, s): s for s in syms}
        for i, f in enumerate(as_completed(futs), 1):
            sym = futs[f]
            try:
                r = f.result()
                print(f'[{i}/{len(syms)}] {r[0]} trades={r[1]} {r[2]} {r[3]:.1f}s total={time.time()-t0:.0f}s', flush=True)
            except Exception as e:
                print(f'[{i}/{len(syms)}] {sym} FAILED {e!r}', flush=True)
    print('done', round(time.time() - t0, 1), flush=True)


if __name__ == '__main__':
    main()
