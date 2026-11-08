import sys, json
sys.path.insert(0, r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest')
import bookbt as bt
import pandas as pd

specs = json.load(open(r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest\specs_final.json', encoding='utf-8'))
s = [x for x in specs if x.get('sid') == 'A1'][0]
print(repr(s['entry_long']))
d = bt.prepare_symbol('BTCUSDT', tfs=('1d',), load_minute=False)
df = d['tf']['1d']
print(type(df['close']), df.shape)
from bookbt import BASE_CTX, eval_expr, highest, ref, adx, _s
ctx = dict(BASE_CTX)
for c in ['open','high','low','close','volume']:
    ctx[c] = df[c]
ctx['adx14'] = adx(df['high'], df['low'], df['close'])[0]
print('adx type', type(ctx['adx14']))
print('highest type', type(highest(df['high'], 10)))
print('ref type', type(ref(highest(df['high'], 10), 1)))
print('bool series type', type(ctx['adx14'] > 20))
a = ref(highest(df['high'], 10), 1)
b = ctx['adx14'] > 20
print('a type', type(a), 'b type', type(b))
try:
    c = a & b
    print('a&b ok', type(c))
except Exception as e:
    print('a&b err', repr(e))
try:
    out = eval(s['entry_long'], {'__builtins__': {}}, ctx)
    print('eval ok', type(out))
except Exception as e:
    print('eval err', repr(e))
