import json, os, re, collections
BT = r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest'
ROOT = r'D:\Paper_ML_BSH\analysis\book_signal_review'
specs = json.load(open(os.path.join(BT, 'specs_final.json'), encoding='utf-8'))
secs = json.load(open(os.path.join(BT, 'sections.json'), encoding='utf-8'))
batches = sorted(d for d in os.listdir(ROOT) if re.fullmatch(r'batch_\d{3}', d))
print('batches', len(batches), 'sections', len(secs))
by = collections.defaultdict(list)
for s in specs:
    by[s['batch']].append(s)
status = collections.Counter()
for b in batches:
    ss = by.get(b, [])
    tested = [s for s in ss if s['status'] == 'tested' and s.get('confidence') in ('high', 'medium')]
    low = [s for s in ss if s['status'] == 'tested' and s.get('confidence') == 'low']
    exc = [s for s in ss if s['status'] == 'excluded']
    if not ss:
        status['no_sections'] += 1
    elif tested:
        status['tested'] += 1
    elif low:
        status['low_only'] += 1
    elif exc:
        status['excluded_only'] += 1
print(status)
print('spec status', collections.Counter((s['status'], s.get('confidence')) for s in specs))
print('batches with sections but no specs', [b for b in batches if b not in by][:20])
