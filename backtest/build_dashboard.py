import os, json, html, math, collections

BT = r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest'
DATA = json.load(open(os.path.join(BT, 'dashboard_data.json'), encoding='utf-8'))


def dd_from_pnl(pnls):
    eq = 1.0; peak = 1.0; mdd = 0.0
    for p in pnls:
        eq *= (1.0 + p)
        peak = max(peak, eq)
        mdd = min(mdd, eq / peak - 1.0)
    return mdd


def pct(x, d=2):
    if x is None:
        return '—'
    return f'{x*100:,.{d}f}%'


def num(x):
    if x is None:
        return '—'
    return f'{int(x):,}'


def cnum(x):
    if x is None:
        return '—'
    x = float(x)
    if x >= 1e6:
        return f'{x/1e6:.1f}M'
    if x >= 1e3:
        return f'{x/1e3:.0f}k'
    return str(int(x))


def css_class_tf(tf):
    return {'5m': 'tf-5m', '15m': 'tf-15m', '1h': 'tf-1h', '4h': 'tf-4h', '1d': 'tf-1d', '1w': 'tf-1w'}.get(tf, '')


meta = DATA['meta']
tf_rows = DATA['tf']
specs = DATA['specs']
batches = DATA['batches']
bench = DATA['benchmark']
fams = DATA['families']

# key findings
best_tf = max(tf_rows, key=lambda r: r['median_net']) if tf_rows else None
worst_tf = min(tf_rows, key=lambda r: r['median_net']) if tf_rows else None
daily = next((r for r in tf_rows if r['tf'] == '1d'), best_tf)
weekly = next((r for r in tf_rows if r['tf'] == '1w'), None)
five = next((r for r in tf_rows if r['tf'] == '5m'), worst_tf)
pool = [s for s in specs if not s.get('is_duplicate')]
ranked = [s for s in pool if s['n'] >= 30 and s['symbols'] >= 5
          and s.get('median_symbol_net', -1) > 0 and s.get('pct_symbols_positive', 0) >= 0.5]
if not ranked:
    ranked = [s for s in pool if s['n'] >= 30 and s['symbols'] >= 5]
if not ranked:
    ranked = [s for s in pool if s['n'] >= 20] or pool
top = sorted(ranked, key=lambda s: s.get('median_symbol_net', -1), reverse=True)[:1]
top = top[0] if top else (specs[0] if specs else None)

# daily long/short flow
_dl = sum(s.get('long_n', 0) for s in specs if s['tf'] == '1d')
_ds = sum(s.get('short_n', 0) for s in specs if s['tf'] == '1d')
long_share = _dl / max(_dl + _ds, 1)

# top 5 for equity chart
top5 = sorted(ranked, key=lambda s: s.get('median_symbol_net', -1), reverse=True)[:5]

# equity points
def eq_points(s):
    pts = [['2022-08', 1.0]]
    for m, e in zip(s.get('monthly', []), s.get('monthly_equity', [])):
        pts.append([m, e])
    return pts


series_strat = []
colors = ['#4fd1c5', '#f6ad55', '#b794f4', '#68d391', '#fc8181']
for i, s in enumerate(top5):
    series_strat.append({'name': f"{s['sid']} · {s['tf']}", 'color': colors[i % len(colors)],
                         'points': eq_points(s), 'width': 2.2})
# benchmark
btc_pts = [['2022-08', 1.0]]
for m, p in zip(bench['btc_months'], bench['btc_pnl']):
    btc_pts.append([m, btc_pts[-1][1] * (1 + p)])
basket_pts = [['2022-08', 1.0]]
for m, p in zip(bench['basket_months'], bench['basket_pnl']):
    basket_pts.append([m, basket_pts[-1][1] * (1 + p)])
series_bench = [
    {'name': 'BTC buy & hold', 'color': '#8da2c0', 'points': btc_pts, 'width': 2.0, 'dash': '5 4'},
    {'name': 'EW crypto basket', 'color': '#b794f4', 'points': basket_pts, 'width': 2.0, 'dash': '3 4'},
]

# excluded reasons
all_specs = json.load(open(os.path.join(BT, 'specs_final.json'), encoding='utf-8'))
exc_reasons = collections.Counter()
for s in all_specs:
    if s.get('status') == 'excluded':
        exc_reasons[s.get('reason', 'Other')] += 1
# also low-confidence reasons are implied
exc_html = ''.join(
    f'<li><span>{html.escape(k)}</span><b>{v}</b></li>'
    for k, v in exc_reasons.most_common(10)
)

# tf table rows
tf_html = ''
for r in tf_rows:
    tf_html += f"""<tr>
      <td><span class="pill {css_class_tf(r['tf'])}">{r['tf']}</span></td>
      <td class="num">{num(r['specs'])}</td>
      <td class="num">{cnum(r['trades'])}</td>
      <td class="num {'pos' if r['avg_net']>0 else 'neg'}">{pct(r['avg_net'], 3)}</td>
      <td class="num {'pos' if r['median_symbol_net']>0 else 'neg'}">{pct(r['median_symbol_net'], 3)}</td>
      <td class="num">{pct(r['pct_symbols_positive'], 0)}</td>
      <td class="num {'pos' if r['median_portfolio']>0 else 'neg'}">{pct(r['median_portfolio'], 1)}</td>
      <td class="num">{pct(r['pct_positive'], 0)}</td>
    </tr>"""

fam_html = ''
for r in fams[:14]:
    fam_html += f"""<tr>
      <td>{html.escape(r['family'])}</td>
      <td class="num">{num(r['specs'])}</td>
      <td class="num">{num(r['trades'])}</td>
      <td class="num {'pos' if r['median_net']>0 else 'neg'}">{pct(r['median_net'], 3)}</td>
      <td class="num {'pos' if r['median_portfolio']>0 else 'neg'}">{pct(r['median_portfolio'], 1)}</td>
      <td class="num">{pct(r['pct_positive'], 0)}</td>
    </tr>"""

batch_counts = collections.Counter(b['status'] for b in batches)
seg = ''
labels = {'tested': ('Tested', '#4fd1c5'), 'low_only': ('Low confidence only', '#f6ad55'),
          'excluded_only': ('Excluded only', '#fc8181'), 'no_sections': ('No sections', '#3b4b68')}
for k in ['tested', 'low_only', 'excluded_only', 'no_sections']:
    v = batch_counts.get(k, 0)
    if v:
        seg += f'<div class="seg" style="width:{v/len(batches)*100:.2f}%;background:{labels[k][1]}" title="{labels[k][0]}: {v}"></div>'

# top strategy finding
if top:
    top_txt = (f"{top['sid']} ({top['tf']}, {top['family']}) · "
               f"{pct(top.get('median_symbol_net', 0), 2)} median symbol net, "
               f"{pct(top.get('pct_symbols_positive', 0), 0)} of symbols positive")
else:
    top_txt = '—'

edge_note = ('The average is carried by a minority of strong symbols.'
             if daily['avg_net'] > 0 else
             'The average is already negative after costs; the median symbol is weaker still.')
daily_title = ('Daily edge is thin and uneven'
               if daily['avg_net'] > 0 else
               'Daily edge disappears in the broad universe')

findings = f"""
<div class="finding">
  <div class="fk">01 · Horizon</div>
  <h3>Fees break the fast timeframes</h3>
  <p>The average 5m trade is <b>{pct(five['avg_gross'],3)} gross</b> before costs and <b>{pct(five['avg_net'],3)} net</b> after. The cost stack adds about <b>{pct(five['fee_drag'],3)}</b> per round trip — enough to turn a flat gross edge into a clear loss.</p>
  <div class="mini">5m: {five['specs']} specs · {num(five['trades'])} trades · only {pct(five['pct_symbols_positive'],0)} of symbol-spec pairs positive</div>
</div>
<div class="finding">
  <div class="fk">02 · Edge</div>
  <h3>{daily_title}</h3>
  <p>Daily specs average <b>{pct(daily['avg_net'],2)}</b> net per trade, but the median symbol earns <b>{pct(daily['median_symbol_net'],3)}</b>; <b>{pct(daily['pct_positive'],0)}</b> of specs are positive, only <b>{pct(daily['pct_symbols_positive'],0)}</b> of symbol-spec pairs. {edge_note}</p>
  <div class="mini">Median daily portfolio {pct(daily['median_portfolio'],1)} over 4 years · BTC {pct(bench['btc_return'],0)} · fee drag {pct(daily['fee_drag'],2)}/trade</div>
</div>
<div class="finding">
  <div class="fk">03 · Benchmark</div>
  <h3>Buy &amp; hold is a high bar</h3>
  <p>BTC returned <b>{pct(bench['btc_return'],0)}</b> and the equal-weight crypto basket <b>{pct(bench['basket_return'],0)}</b> from Aug 2022 to Aug 2026. Most mechanical proxies do not beat it after costs.</p>
  <div class="mini">Daily flow is {pct(long_share,0)} long; in a +{pct(bench['btc_return'],0)} BTC market, directional beta is part of the result.</div>
</div>
<div class="finding">
  <div class="fk">04 · Coverage</div>
  <h3>{meta['n_tested_batches']} of 215 batches survived the first screen</h3>
  <p><b>{meta['n_tested_specs']}</b> high/medium-confidence proxies (<b>{meta.get('n_unique_rules', meta['n_tested_specs'])}</b> unique rules) were tested. <b>{meta['n_low_batches']}</b> batches only contain low-confidence mappings, <b>{meta['n_excluded_batches']}</b> are excluded, and <b>{meta['n_no_sections']}</b> have no strategy sections.</p>
  <div class="mini">Top result: {html.escape(top_txt)}</div>
</div>
"""

HTML = r'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Book Strategy Lab · 215 batches × __N_SYMBOLS__ crypto futures</title>
<style>
:root{
  --bg:#080d18; --panel:#0f1728; --panel2:#131e33; --line:#22314d;
  --text:#e8eef9; --muted:#8da2c0; --dim:#637795;
  --accent:#4fd1c5; --amber:#f6ad55; --red:#fc8181; --green:#68d391; --purple:#b794f4;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{
  margin:0; color:var(--text); font-family:ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;
  background:
    radial-gradient(1100px 600px at 15% -10%, rgba(79,209,197,.12), transparent 55%),
    radial-gradient(900px 500px at 90% 0%, rgba(183,148,244,.10), transparent 55%),
    var(--bg);
  line-height:1.45;
}
.wrap{max-width:1420px;margin:0 auto;padding:26px 22px 70px}
header{display:flex;justify-content:space-between;gap:24px;align-items:flex-end;flex-wrap:wrap;margin:8px 0 22px}
.eyebrow{font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--accent);font-weight:700}
h1{font-size:clamp(26px,3.4vw,44px);line-height:1.08;margin:8px 0 6px;letter-spacing:-.02em}
h1 span{background:linear-gradient(90deg,#4fd1c5,#b794f4 60%,#f6ad55);-webkit-background-clip:text;background-clip:text;color:transparent}
.sub{color:var(--muted);max-width:760px;font-size:14px}
.stamp{font-size:12px;color:var(--dim);text-align:right}
.kpis{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px;margin:18px 0 20px}
.kpi{background:linear-gradient(180deg,rgba(255,255,255,.035),rgba(255,255,255,.01));border:1px solid var(--line);border-radius:14px;padding:14px 16px}
.kpi .v{font-size:26px;font-weight:750;letter-spacing:-.02em}
.kpi .l{font-size:11px;text-transform:uppercase;letter-spacing:.12em;color:var(--muted);margin-top:2px}
.kpi .s{font-size:12px;color:var(--dim);margin-top:6px}
.findings{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin:16px 0 18px}
.finding{background:linear-gradient(145deg,rgba(79,209,197,.08),rgba(255,255,255,.015) 45%);border:1px solid var(--line);border-radius:16px;padding:16px 18px}
.fk{font-size:10px;letter-spacing:.18em;color:var(--accent);font-weight:700;text-transform:uppercase}
.finding h3{margin:5px 0 6px;font-size:16px}
.finding p{margin:0;color:var(--muted);font-size:13px}
.finding b{color:var(--text)}
.mini{margin-top:10px;padding-top:9px;border-top:1px dashed var(--line);color:var(--dim);font-size:11px}
.tabs{display:flex;gap:6px;flex-wrap:wrap;border-bottom:1px solid var(--line);margin:8px 0 18px;position:sticky;top:0;background:rgba(8,13,24,.92);backdrop-filter:blur(10px);z-index:10;padding-top:8px}
.tab{appearance:none;border:0;background:transparent;color:var(--muted);padding:10px 13px;font:inherit;font-size:13px;font-weight:650;cursor:pointer;border-bottom:2px solid transparent}
.tab:hover{color:var(--text)}
.tab.active{color:var(--accent);border-bottom-color:var(--accent)}
.panel{display:none}
.panel.active{display:block}
.grid2{display:grid;grid-template-columns:1.12fr .88fr;gap:14px}
.card{background:linear-gradient(180deg,rgba(255,255,255,.035),rgba(255,255,255,.012));border:1px solid var(--line);border-radius:16px;padding:16px 16px 14px;min-width:0}
.card h2{font-size:15px;margin:0 0 4px;letter-spacing:-.01em}
.card .hint{color:var(--dim);font-size:11.5px;margin:0 0 10px}
.chart{width:100%;min-height:280px}
.chart svg{width:100%;height:auto;display:block}
.legend{display:flex;gap:14px;flex-wrap:wrap;font-size:11px;color:var(--muted);margin-top:8px}
.legend i{display:inline-block;width:9px;height:9px;border-radius:2px;margin-right:5px;vertical-align:middle}
table{width:100%;border-collapse:collapse;font-size:12px}
th,td{padding:8px 8px;border-bottom:1px solid rgba(34,49,77,.7);text-align:left;white-space:nowrap}
th{color:var(--dim);font-size:10px;text-transform:uppercase;letter-spacing:.1em;font-weight:700;position:sticky;top:0;background:#0e1626;cursor:pointer;z-index:2}
th:hover{color:var(--text)}
td.num,th.num{text-align:right;font-variant-numeric:tabular-nums}
tr.row{cursor:pointer}
tr.row:hover td{background:rgba(79,209,197,.055)}
.pos{color:var(--green)} .neg{color:var(--red)}
.pill{display:inline-block;padding:2px 7px;border-radius:999px;font-size:10px;font-weight:750;letter-spacing:.04em;border:1px solid transparent}
.tf-5m{background:rgba(252,129,129,.13);color:#feb2b2;border-color:rgba(252,129,129,.28)}
.tf-15m{background:rgba(246,173,85,.13);color:#fbd38d;border-color:rgba(246,173,85,.28)}
.tf-1h{background:rgba(236,201,75,.13);color:#fefcbf;border-color:rgba(236,201,75,.28)}
.tf-4h{background:rgba(104,211,145,.13);color:#c6f6d5;border-color:rgba(104,211,145,.28)}
.tf-1d{background:rgba(79,209,197,.13);color:#b2f5ea;border-color:rgba(79,209,197,.28)}
.tf-1w{background:rgba(183,148,244,.13);color:#e9d8fd;border-color:rgba(183,148,244,.28)}
.badge{display:inline-block;padding:2px 7px;border-radius:6px;font-size:10px;font-weight:700}
.b-tested{background:rgba(79,209,197,.14);color:#b2f5ea}
.b-low{background:rgba(246,173,85,.14);color:#fbd38d}
.b-exc{background:rgba(252,129,129,.14);color:#feb2b2}
.b-none{background:rgba(99,119,149,.14);color:#a0aec0}
.b-high{background:rgba(79,209,197,.14);color:#b2f5ea}
.b-medium{background:rgba(183,148,244,.14);color:#e9d8fd}
.controls{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin:4px 0 12px}
.controls input,.controls select{background:#0c1424;border:1px solid var(--line);color:var(--text);border-radius:9px;padding:8px 10px;font:inherit;font-size:12px;outline:none}
.controls input:focus,.controls select:focus{border-color:var(--accent)}
.controls input[type=search]{min-width:210px}
.controls .spacer{flex:1}
.btn{background:rgba(79,209,197,.12);border:1px solid rgba(79,209,197,.3);color:#b2f5ea;border-radius:9px;padding:8px 11px;font:inherit;font-size:12px;font-weight:650;cursor:pointer}
.btn:hover{background:rgba(79,209,197,.2)}
.tablewrap{max-height:620px;overflow:auto;border:1px solid var(--line);border-radius:12px}
.detail{margin-top:14px;display:none}
.detail.on{display:block}
.detail .rule{background:#0b1220;border:1px solid var(--line);border-radius:10px;padding:10px 12px;font-family:ui-monospace,SFMono-Regular,Consolas,monospace;font-size:11px;color:#a7f3d0;white-space:pre-wrap;overflow:auto}
.detail .summary{color:var(--muted);font-size:12px;margin:8px 0}
.detail .mets{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:8px;margin:10px 0}
.mets{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:8px}
.mets div{background:#0b1220;border:1px solid var(--line);border-radius:9px;padding:8px}
.mets b{display:block;font-size:15px}
.mets span{font-size:10px;color:var(--dim);text-transform:uppercase;letter-spacing:.08em}
.segbar{display:flex;height:12px;border-radius:999px;overflow:hidden;border:1px solid var(--line);background:#0c1424;margin:8px 0 12px}
.seg{height:100%}
.seglegend{display:flex;gap:14px;flex-wrap:wrap;font-size:11px;color:var(--muted);margin-bottom:8px}
.seglegend i{display:inline-block;width:8px;height:8px;border-radius:2px;margin-right:5px}
ul.reasons{list-style:none;padding:0;margin:0;display:grid;gap:7px}
ul.reasons li{display:flex;justify-content:space-between;gap:12px;font-size:12px;color:var(--muted);border-bottom:1px dashed rgba(34,49,77,.7);padding-bottom:6px}
ul.reasons b{color:var(--text)}
.method{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.method h3{font-size:13px;margin:0 0 6px}
.method p,.method li{color:var(--muted);font-size:12.3px}
.method code{background:#0b1220;border:1px solid var(--line);border-radius:5px;padding:1px 5px;color:#a7f3d0;font-size:11px}
.note{border-left:3px solid var(--amber);background:rgba(246,173,85,.07);padding:10px 12px;border-radius:0 8px 8px 0;color:#fbd38d;font-size:12px;margin:10px 0}
footer{margin-top:26px;color:var(--dim);font-size:11px;border-top:1px solid var(--line);padding-top:14px}
@media(max-width:1100px){.kpis{grid-template-columns:repeat(2,1fr)}.findings{grid-template-columns:1fr}.grid2{grid-template-columns:1fr}.method{grid-template-columns:1fr}}
@media(max-width:640px){.wrap{padding:16px 12px 50px}.kpis{grid-template-columns:1fr}.detail .mets{grid-template-columns:repeat(2,1fr)}.stamp{text-align:left}}
</style>
</head>
<body>
<div class="wrap">
<header>
  <div>
    <div class="eyebrow">Book signal review · first-pass mechanical backtest</div>
    <h1>215 batches. __N_SYMBOLS__ crypto futures. <span>One fee-inclusive test bed.</span></h1>
    <div class="sub">Every strategy section was mapped to a mechanical proxy, signalled on its own timeframe, and executed on 1-minute Binance USDT-M data with taker fees, slippage and historical funding. Signals use completed bars only; entries occur at the first 1m open after the signal bar closes.</div>
  </div>
  <div class="stamp">
    <div>Signal window</div><div><b>2022-08-01 → 2026-08-31</b></div>
    <div style="margin-top:6px">Execution data through 2026-10-18</div>
  </div>
</header>

<div class="kpis">
  <div class="kpi"><div class="v">__N_SPECS__</div><div class="l">mechanical proxies tested</div><div class="s">__N_UNIQUE__ unique engine rules · high + medium mappings</div></div>
  <div class="kpi"><div class="v">__N_BATCHES__ / 215</div><div class="l">batches covered</div><div class="s">__N_LOW__ low-confidence · __N_EXC__ excluded · __N_NONE__ no sections</div></div>
  <div class="kpi"><div class="v">__N_SYMBOLS__</div><div class="l">symbols</div><div class="s">Binance USDT-M perpetuals with 1m/1h/4h data</div></div>
  <div class="kpi"><div class="v">__N_TRADES__</div><div class="l">simulated trades</div><div class="s">fees 5 bps/side · slippage 2 bps/side · funding included</div></div>
</div>

<div class="findings">__FINDINGS__</div>

<div class="tabs">
  <button class="tab active" data-tab="overview">Overview</button>
  <button class="tab" data-tab="strategies">Strategy explorer</button>
  <button class="tab" data-tab="batches">Batch coverage</button>
  <button class="tab" data-tab="method">Method &amp; caveats</button>
</div>

<section class="panel active" id="panel-overview">
  <div class="grid2">
    <div class="card">
      <h2>Gross edge vs net edge by timeframe</h2>
      <p class="hint">Average per-trade return. The gap is the cost stack: 5 bps fee per side, 2 bps slippage per side, plus funding.</p>
      <div id="tfChart" class="chart"></div>
      <div class="legend"><span><i style="background:#4fd1c5"></i>gross</span><span><i style="background:#fc8181"></i>net</span></div>
      <div class="legend" id="tfNote" style="display:block"></div>
    </div>
    <div class="card">
      <h2>Where the edge survives</h2>
      <p class="hint">Share of tested proxies with positive average net per trade.</p>
      <div id="posChart" class="chart"></div>
    </div>
  </div>

  <div class="grid2" style="margin-top:14px;grid-template-columns:1fr 1fr">
    <div class="card">
      <h2>Top strategies · monthly equity (zoomed)</h2>
      <p class="hint">Equal-weight 1/__N_SYMBOLS__ capital per trade. The y-axis is auto-zoomed to the strategy range; benchmarks are on a separate chart.</p>
      <div id="equityChart" class="chart"></div>
      <div class="legend" id="eqLegend"></div>
    </div>
    <div class="card">
      <h2>Timeframe scorecard</h2>
      <p class="hint">All figures are fee-inclusive. “Portfolio” compounds monthly returns with 1/__N_SYMBOLS__ capital per trade.</p>
      <div class="tablewrap" style="max-height:360px">
        <table>
          <thead><tr><th>TF</th><th class="num">Specs</th><th class="num">Trades</th><th class="num">Avg net</th><th class="num">Med sym</th><th class="num">Sym +</th><th class="num">Med pf</th><th class="num">Specs +</th></tr></thead>
          <tbody>__TF_ROWS__</tbody>
        </table>
      </div>
      <p class="hint" style="margin-top:8px">Gross edge and cost drag are in the chart at left. The 1w row is a 7-spec small sample.</p>
    </div>
  </div>

  <div class="grid2" style="margin-top:14px">
    <div class="card">
      <h2>Benchmarks · fully invested</h2>
      <p class="hint">BTC and an equal-weight basket of the same __N_SYMBOLS__ symbols. The strategy curves above use idle cash and are not directly comparable.</p>
      <div id="benchChart" class="chart"></div>
      <div class="legend" id="benchLegend"></div>
      <div class="mets" style="grid-template-columns:repeat(4,minmax(0,1fr));margin-top:10px">
        <div><b class="pos">__BTC_RET__</b><span>BTC return</span></div>
        <div><b class="neg">__BTC_DD__</b><span>BTC max DD</span></div>
        <div><b class="pos">__BASKET_RET__</b><span>EW basket return</span></div>
        <div><b class="neg">__BASKET_DD__</b><span>EW basket max DD</span></div>
      </div>
    </div>
    <div class="card">
      <h2>Family leaders</h2>
      <p class="hint">Median per-trade net and median portfolio return by strategy family (families with at least 3 tested specs).</p>
      <div class="tablewrap" style="max-height:420px">
        <table>
          <thead><tr><th>Family</th><th class="num">Specs</th><th class="num">Trades</th><th class="num">Med. net</th><th class="num">Med. portfolio</th><th class="num">% positive</th></tr></thead>
          <tbody>__FAM_ROWS__</tbody>
        </table>
      </div>
    </div>
  </div>

  <div class="grid2" style="margin-top:14px">
    <div class="card">
      <h2>Coverage map</h2>
      <p class="hint">How the 215 batch folders were classified. The dashboard never silently drops a batch.</p>
      <div class="segbar">__SEG__</div>
      <div class="seglegend">
        <span><i style="background:#4fd1c5"></i>Tested: __N_BATCHES__</span>
        <span><i style="background:#f6ad55"></i>Low confidence only: __N_LOW__</span>
        <span><i style="background:#fc8181"></i>Excluded only: __N_EXC__</span>
        <span><i style="background:#3b4b68"></i>No sections: __N_NONE__</span>
      </div>
      <div class="note">Coverage is intentionally conservative. A section is only “tested” if a mechanical rule could be mapped with high or medium confidence. Complex discretionary patterns, non-crypto assets and pure exit/position variants are listed with reasons instead of being silently approximated.</div>
    </div>
    <div class="card">
      <h2>Excluded section reasons</h2>
      <p class="hint">The most common reasons a section was not turned into a mechanical test.</p>
      <ul class="reasons">__EXC_HTML__</ul>
      <div class="note" style="margin-top:14px">Low-confidence mappings are not in the main results. They are visible as “low confidence only” batch rows, with the section title and mapping status in the source catalog.</div>
    </div>
  </div>
</section>

<section class="panel" id="panel-strategies">
  <div class="card" style="margin-bottom:14px">
    <h2>Most consistent strategies</h2>
    <p class="hint">Top 15 by median symbol net, requiring at least 30 trades and 5 symbols. This ranking is deliberately resistant to a single new-listing outlier.</p>
    <div id="consChart" class="chart"></div>
  </div>
  <div class="card">
    <h2>Strategy explorer</h2>
    <p class="hint">Default ranking uses median symbol net — one vote per symbol — so a single new-listing outlier cannot dominate. Portfolio net uses 1/__N_SYMBOLS__ capital per trade. Click a row for the rule and monthly equity.</p>
    <div class="controls">
      <input id="q" type="search" placeholder="Search SID, batch, title…">
      <select id="tfFilter"><option value="">All timeframes</option></select>
      <select id="famFilter"><option value="">All families</option></select>
      <select id="confFilter"><option value="">All confidence</option><option>high</option><option>medium</option></select>
      <label style="font-size:11px;color:var(--muted)">Min trades <input id="minN" type="number" value="20" min="0" style="width:82px;margin-left:5px"></label>
      <label style="font-size:11px;color:var(--muted);display:flex;align-items:center;gap:5px"><input id="uniqOnly" type="checkbox" checked> Unique rules</label>
      <button class="btn" id="resetBtn">Reset</button>
      <a class="btn" href="strategy_metrics.csv" download>CSV</a>
      <span class="spacer"></span>
      <span id="count" style="font-size:11px;color:var(--dim)"></span>
    </div>
    <div class="tablewrap">
      <table id="specTable">
        <thead><tr>
          <th data-k="portfolio_net" class="num">Portfolio</th>
          <th data-k="avg_net" class="num">Avg net</th>
          <th data-k="median_symbol_net" class="num">Med. sym net</th>
          <th data-k="pct_symbols_positive" class="num">Sym +%</th>
          <th data-k="sid">SID</th>
          <th data-k="batch">Batch</th>
          <th data-k="title">Strategy</th>
          <th data-k="tf">TF</th>
          <th data-k="family">Family</th>
          <th data-k="rule_group_size" class="num">Rule</th>
          <th data-k="n" class="num">Trades</th>
          <th data-k="symbols" class="num">Syms</th>
          <th data-k="avg_gross" class="num">Avg gross</th>
          <th data-k="fee_drag" class="num">Cost drag</th>
          <th data-k="max_dd" class="num">Max DD</th>
          <th data-k="win_rate" class="num">Win</th>
          <th data-k="profit_factor" class="num">PF</th>
          <th data-k="confidence">Conf.</th>
        </tr></thead>
        <tbody></tbody>
      </table>
    </div>
    <div class="detail" id="detail">
      <h2 id="dTitle">—</h2>
      <div class="summary" id="dSummary"></div>
      <div class="rule" id="dRule"></div>
      <div class="mets" id="dMets"></div>
      <div class="legend" id="dYears"></div>
      <div id="dChart" class="chart"></div>
    </div>
  </div>
</section>

<section class="panel" id="panel-batches">
  <div class="card">
    <h2>Batch coverage · 001–215</h2>
    <p class="hint">Every batch folder is listed. Tested batches show the best high/medium-confidence strategy by median symbol net; the rest show why they were not tested.</p>
    <div class="controls">
      <select id="bStatus"><option value="">All statuses</option><option value="tested">Tested</option><option value="low_only">Low confidence only</option><option value="excluded_only">Excluded only</option><option value="no_sections">No sections</option></select>
      <input id="bq" type="search" placeholder="Search batch or strategy…">
      <span class="spacer"></span><span id="bcount" style="font-size:11px;color:var(--dim)"></span>
    </div>
    <div class="tablewrap" style="max-height:680px">
      <table id="batchTable">
        <thead><tr><th>Batch</th><th>Status</th><th class="num">Sections</th><th class="num">Tested</th><th class="num">Low</th><th class="num">Excluded</th><th>Best strategy</th><th>TF</th><th class="num">Portfolio</th><th class="num">Med. sym net</th><th class="num">Trades</th><th>Reason / note</th></tr></thead>
        <tbody></tbody>
      </table>
    </div>
  </div>
</section>

<section class="panel" id="panel-method">
  <div class="method">
    <div class="card">
      <h3>Data & execution</h3>
      <p>OHLCV data comes from <code>D:\1mDataBinance</code>. Higher timeframes are read from local Binance CSVs (<code>5m</code>, <code>15m</code>, <code>1h</code>, <code>4h</code>, <code>1d</code>); weekly bars are resampled from daily. Execution uses 1-minute OHLC, including mixed CSV/parquet months.</p>
      <ul>
        <li><b>Signal timing:</b> only completed strategy-TF bars. Entry at the first 1m open after the signal bar closes.</li>
        <li><b>Stops / targets:</b> checked on 1m OHLC. If stop and target touch in the same 1m bar, the stop is assumed first (conservative).</li>
        <li><b>Exit time / signal:</b> next 1m open after the exit bar closes.</li>
        <li><b>One position</b> per symbol per strategy. No pyramiding, no overlapping entries.</li>
        <li><b>Funding:</b> historical 8h funding from <code>151_M\binance_futures\funding</code>, charged to the position side.</li>
      </ul>
      <h3 style="margin-top:14px">Cost model</h3>
      <p>Binance USDT-M taker fee <code>0.0005</code> per side and slippage <code>0.0002</code> per side. A round trip costs roughly <b>14 bps</b> before funding. The dashboard reports both gross and net so the cost drag is visible.</p>
      <h3 style="margin-top:14px">Portfolio math</h3>
      <p>Each trade is sized at <code>1/__N_SYMBOLS__</code> of capital. Monthly PnL is summed across symbols and compounded. This is a conservative equal-weight deployment: idle symbols leave cash uninvested. Benchmarks are fully invested and are shown for context, not as a like-for-like comparison.</p>
    </div>
    <div class="card">
      <h3>Mapping confidence</h3>
      <ul>
        <li><b>High:</b> the section names an explicit indicator/pattern family and parameters could be parsed (e.g. MACD cross, RSI level, Donchian channel, Bollinger band).</li>
        <li><b>Medium:</b> the family is clear but the source leaves thresholds or filters implicit; a standard parameter set is used.</li>
        <li><b>Low:</b> only a loose keyword match; not included in the main results. These sections are listed as “low confidence only” at batch level.</li>
        <li><b>Excluded:</b> options, US equities, FX, Nifty, news/macro, portfolio/rotation, pure exit or position-sizing variants, and discretionary patterns (SMC, Elliott, harmonic, Wyckoff, TD sequential, divergence).</li>
        <li><b>Duplicate rules:</b> __N_SPECS__ source mappings collapse to <b>__N_UNIQUE__ unique engine rules</b>. The explorer marks duplicates with ×N and defaults to unique rules.</li>
      </ul>
      <h3 style="margin-top:14px">Known limitations</h3>
      <ul>
        <li>This is a <b>first-pass mechanical proxy</b>, not a claim of exact replication of every discretionary rule in the source book.</li>
        <li>Weekly signals are generated on weekly bars resampled from daily; stops and targets are checked on 1m after entry.</li>
        <li>Cross-sectional, breadth, pairs and portfolio-rotation rules are out of scope for a single-symbol engine.</li>
        <li>Symbol coverage is survivorship-biased: the __N_SYMBOLS__ symbols are those with 1m/1h/4h data in the local archive. 5m/15m and 1d signals are resampled from 1m/1h; new listings enter at their first available bar.</li>
        <li><b>Universe sensitivity:</b> an earlier 58-symbol liquid subset showed a positive daily median; broadening to the full active universe reverses that result. The 58-symbol finding was selection-driven and should not be generalized.</li>
        <li>Funding is applied at 8h boundaries; small timing differences versus exchange settlement are possible.</li>
        <li>New listings can produce extreme single-trade returns. The dashboard therefore ranks on median symbol net and reports symbol consistency; average net and portfolio return are shown but should be read with that caveat.</li>
        <li>All fills are taker fills. Maker execution, fee rebates or lower slippage would materially improve the fast timeframes; the fee stack is the dominant result for 5m/15m/1h.</li>
      </ul>
      <div class="note">Result files: <code>strategy_metrics.csv</code>, <code>dashboard_data.json</code>, and per-symbol parquet summaries under <code>results\summary</code> and <code>results\monthly</code>.</div>
    </div>
  </div>
</section>

<footer>
  Generated from 454 extracted strategy sections across 215 batch folders · __N_SPECS__ high/medium-confidence mechanical proxies · __N_SYMBOLS__ Binance USDT-M symbols · fee-inclusive, 1-minute execution.
</footer>
</div>

<script>
const DATA = __DATA__;
const fmtPct=(x,d=2)=>x==null?'—':(x*100).toFixed(d)+'%';
const fmtNum=(x)=>x==null?'—':Math.round(x).toLocaleString();
const esc=(s)=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const cleanTitle=(s)=>{const t=String(s.title??'');const p=String(s.sid??'');return t.startsWith(p)?t.slice(p.length).replace(/^\s*[—–-]\s*/,''):t;};
const tfColor={'5m':'#fc8181','15m':'#f6ad55','1h':'#ecc94b','4h':'#68d391','1d':'#4fd1c5','1w':'#b794f4'};
const confClass={'high':'b-high','medium':'b-medium'};

function svgEl(w,h){return `<svg viewBox="0 0 ${w} ${h}" role="img">`;}
function axisY(w,h,pad,min,max,ticks=5){
  let s='';
  for(let i=0;i<=ticks;i++){
    const v=min+(max-min)*i/ticks, y=pad.t+(max-v)/(max-min||1)*(h-pad.t-pad.b);
    s+=`<line x1="${pad.l}" y1="${y}" x2="${w-pad.r}" y2="${y}" stroke="#1c2942" stroke-width="1"/>`;
    s+=`<text x="${pad.l-8}" y="${y+4}" text-anchor="end" fill="#637795" font-size="10">${fmtPct(v,0)}</text>`;
  }
  return s;
}

function barGrouped(el, labels, series, opts={}){
  const w=780,h=300,pad={l:58,r:14,t:16,b:48};
  const all=series.flatMap(s=>s.values);
  let min=Math.min(0,...all), max=Math.max(0,...all);
  if(max===min){max=min+0.01;}
  const bw=(w-pad.l-pad.r)/labels.length;
  const gw=bw*0.72, sw=gw/series.length;
  let s=svgEl(w,h);
  s+=axisY(w,h,pad,min,max,5);
  labels.forEach((lab,i)=>{
    series.forEach((se,j)=>{
      const v=se.values[i];
      const y0=pad.t+(max-0)/(max-min)*(h-pad.t-pad.b);
      const y1=pad.t+(max-v)/(max-min)*(h-pad.t-pad.b);
      const x=pad.l+i*bw+(bw-gw)/2+j*sw;
      const yy=Math.min(y0,y1), hh=Math.max(1,Math.abs(y1-y0));
      s+=`<rect x="${x}" y="${yy}" width="${Math.max(2,sw-2)}" height="${hh}" rx="2" fill="${se.color}" opacity=".92"><title>${esc(lab)} · ${esc(se.name)}: ${fmtPct(v,3)}</title></rect>`;
    });
    s+=`<text x="${pad.l+i*bw+bw/2}" y="${h-pad.b+18}" text-anchor="middle" fill="#8da2c0" font-size="11">${esc(lab)}</text>`;
  });
  s+='</svg>';
  el.innerHTML=s;
}

function barH(el, rows, opts={}){
  const w=780, rh=24, pad={l:120,r:70,t:8,b:8};
  const h=Math.max(160,pad.t+pad.b+rows.length*rh);
  const maxV=Math.max(0.0001,...rows.map(r=>Math.abs(r.value)));
  let s=svgEl(w,h);
  s+=`<line x1="${pad.l}" y1="${pad.t}" x2="${pad.l}" y2="${h-pad.b}" stroke="#22314d"/>`;
  rows.forEach((r,i)=>{
    const y=pad.t+i*rh+4, bw=(w-pad.l-pad.r)*Math.abs(r.value)/maxV;
    const x=r.value>=0?pad.l:pad.l-bw;
    s+=`<rect x="${x}" y="${y}" width="${Math.max(1,bw)}" height="${rh-8}" rx="3" fill="${r.color||'#4fd1c5'}" opacity=".9"><title>${esc(r.label)}: ${fmtPct(r.value,1)}</title></rect>`;
    s+=`<text x="${pad.l-8}" y="${y+rh/2-1}" text-anchor="end" fill="#8da2c0" font-size="10.5">${esc(r.label)}</text>`;
    s+=`<text x="${w-pad.r+6}" y="${y+rh/2-1}" fill="${r.value>=0?'#68d391':'#fc8181'}" font-size="10.5">${fmtPct(r.value,1)}</text>`;
  });
  s+='</svg>';
  el.innerHTML=s;
}

function lineChart(el, series, opts={}){
  const w=820,h=330,pad={l:56,r:18,t:16,b:52};
  const labels=[...new Set(series.flatMap(s=>s.points.map(p=>p[0])))].sort();
  const allY=series.flatMap(s=>s.points.map(p=>p[1]));
  let min=Math.min(1,...allY), max=Math.max(1,...allY);
  const span=max-min||1; min=min-span*0.05; max=max+span*0.05;
  const x=(lab)=>pad.l+(labels.indexOf(lab)/(labels.length-1||1))*(w-pad.l-pad.r);
  const y=(v)=>pad.t+(max-v)/(max-min)*(h-pad.t-pad.b);
  let s=svgEl(w,h);
  // y grid
  for(let i=0;i<=4;i++){
    const v=min+(max-min)*i/4, yy=y(v);
    s+=`<line x1="${pad.l}" y1="${yy}" x2="${w-pad.r}" y2="${yy}" stroke="#1c2942"/>`;
    s+=`<text x="${pad.l-8}" y="${yy+4}" text-anchor="end" fill="#637795" font-size="10">${v.toFixed(2)}x</text>`;
  }
  // x labels every ~6 months
  labels.forEach((lab,i)=>{ if(i%6===0||(i===labels.length-1&&i%6>2)){
    s+=`<text x="${x(lab)}" y="${h-pad.b+18}" text-anchor="middle" fill="#637795" font-size="10">${lab}</text>`;
  }});
  series.forEach(se=>{
    const pts=se.points.filter(p=>labels.includes(p[0]));
    const d=pts.map((p,i)=>`${i?'L':'M'}${x(p[0]).toFixed(1)},${y(p[1]).toFixed(1)}`).join(' ');
    s+=`<path d="${d}" fill="none" stroke="${se.color}" stroke-width="${se.width||2}" stroke-linejoin="round" stroke-linecap="round" ${se.dash?`stroke-dasharray="${se.dash}"`:''} opacity=".95"><title>${esc(se.name)}</title></path>`;
    const last=pts[pts.length-1];
    if(last){s+=`<circle cx="${x(last[0])}" cy="${y(last[1])}" r="3" fill="${se.color}"/>`;}
  });
  s+='</svg>';
  el.innerHTML=s;
  const lg=document.getElementById(opts.legend||'eqLegend');
  if(lg){lg.innerHTML=series.map(se=>`<span><i style="background:${se.color}"></i>${esc(se.name)}</span>`).join('');}
}

function initOverview(){
  const tf=DATA.tf.filter(r=>r.tf!=='1w');
  barGrouped(document.getElementById('tfChart'), tf.map(r=>r.tf), [
    {name:'gross',color:'#4fd1c5',values:tf.map(r=>r.avg_gross)},
    {name:'net',color:'#fc8181',values:tf.map(r=>r.avg_net)}
  ]);
  const w=DATA.tf.find(r=>r.tf==='1w');
  const note=document.getElementById('tfNote');
  if(note) note.textContent=w?`1w omitted from the chart: ${w.specs} specs, ${fmtNum(w.trades)} trades, average net ${fmtPct(w.avg_net,2)}. See the scorecard.`:'';
  barH(document.getElementById('posChart'), DATA.tf.map(r=>({label:r.tf,value:r.pct_positive,color:tfColor[r.tf]||'#4fd1c5'})).reverse());
  lineChart(document.getElementById('equityChart'), SERIES_STRAT);
  lineChart(document.getElementById('benchChart'), SERIES_BENCH, {legend:'benchLegend'});
}

function drawConsChart(){
  const rows=DATA.specs.filter(s=>!s.is_duplicate&&s.n>=30&&s.symbols>=5).sort((a,b)=>b.median_symbol_net-a.median_symbol_net).slice(0,15);
  barH(document.getElementById('consChart'), rows.map(s=>({label:`${s.sid} · ${s.tf}`,value:s.median_symbol_net,color:tfColor[s.tf]})));
}

const SERIES_STRAT = __SERIES_STRAT__;
const SERIES_BENCH = __SERIES_BENCH__;

function showTab(name){
  document.querySelectorAll('.tab').forEach(b=>b.classList.toggle('active',b.dataset.tab===name));
  document.querySelectorAll('.panel').forEach(p=>p.classList.toggle('active',p.id==='panel-'+name));
}
document.querySelectorAll('.tab').forEach(b=>b.addEventListener('click',()=>showTab(b.dataset.tab)));

// spec explorer
const state={sort:'median_symbol_net',dir:-1};
function fillSelect(id,vals){const el=document.getElementById(id);vals.forEach(v=>{const o=document.createElement('option');o.value=v;o.textContent=v;el.appendChild(o);});}
fillSelect('tfFilter',[...new Set(DATA.specs.map(s=>s.tf))].sort());
fillSelect('famFilter',[...new Set(DATA.specs.map(s=>s.family))].sort());

function specRows(){
  const q=document.getElementById('q').value.toLowerCase();
  const tf=document.getElementById('tfFilter').value;
  const fam=document.getElementById('famFilter').value;
  const conf=document.getElementById('confFilter').value;
  const minN=+document.getElementById('minN').value||0;
  const uniq=document.getElementById('uniqOnly').checked;
  let rows=DATA.specs.filter(s=>
    (!tf||s.tf===tf)&&(!fam||s.family===fam)&&(!conf||s.confidence===conf)&&s.n>=minN&&
    (!uniq||!s.is_duplicate)&&
    (!q||[s.sid,s.batch,s.title,s.family,s.tf].join(' ').toLowerCase().includes(q))
  );
  const k=state.sort;
  rows.sort((a,b)=>{
    let av=a[k],bv=b[k];
    if(typeof av==='string'){av=av.toLowerCase();bv=(bv||'').toLowerCase();}
    return (av>bv?1:av<bv?-1:0)*state.dir;
  });
  return rows;
}

function renderSpecs(){
  const rows=specRows();
  document.getElementById('count').textContent=`${rows.length} strategies`;
  const tb=document.querySelector('#specTable tbody');
  tb.innerHTML=rows.map(s=>`<tr class="row" data-idx="${s.idx}">
    <td class="num ${s.portfolio_net>=0?'pos':'neg'}">${fmtPct(s.portfolio_net,1)}</td>
    <td class="num ${s.avg_net>=0?'pos':'neg'}">${fmtPct(s.avg_net,3)}</td>
    <td class="num ${s.median_symbol_net>=0?'pos':'neg'}" title="best symbol: ${esc(s.top_symbol||'')} · concentration ${fmtPct(s.concentration||0,0)}">${fmtPct(s.median_symbol_net,3)}</td>
    <td class="num">${fmtPct(s.pct_symbols_positive,0)}</td>
    <td><b>${esc(s.sid)}</b></td>
    <td>${esc(s.batch.replace('batch_',''))}</td>
    <td title="${esc(s.title)}" style="max-width:340px;overflow:hidden;text-overflow:ellipsis">${esc(cleanTitle(s))}</td>
    <td><span class="pill ${'tf-'+s.tf}">${s.tf}</span></td>
    <td>${esc(s.family)}</td>
    <td class="num" title="${s.rule_group_size>1?`same rule as ${esc(s.rule_group_lead)}`:''}">${s.rule_group_size>1?`×${s.rule_group_size}`:'1'}</td>
    <td class="num">${fmtNum(s.n)}</td>
    <td class="num">${s.symbols}</td>
    <td class="num">${fmtPct(s.avg_gross,3)}</td>
    <td class="num">${fmtPct(s.fee_drag,3)}</td>
    <td class="num neg">${fmtPct(s.max_dd,1)}</td>
    <td class="num">${fmtPct(s.win_rate,0)}</td>
    <td class="num">${s.profit_factor>=999?'∞':s.profit_factor.toFixed(2)}</td>
    <td><span class="badge ${confClass[s.confidence]||''}">${esc(s.confidence)}</span></td>
  </tr>`).join('');
  tb.querySelectorAll('tr').forEach(tr=>tr.addEventListener('click',()=>selectSpec(+tr.dataset.idx)));
}

function selectSpec(idx){
  const s=DATA.specs.find(x=>x.idx===idx); if(!s)return;
  const d=document.getElementById('detail'); d.classList.add('on');
  document.getElementById('dTitle').textContent=`${s.sid} — ${cleanTitle(s)}`;
  document.getElementById('dSummary').textContent=s.summary||'';
  document.getElementById('dRule').textContent=(s.rule_long?`LONG  ${s.rule_long}`:'')+(s.rule_short?`\nSHORT ${s.rule_short}`:'')+(s.rule_long||s.rule_short?'':'(no mechanical rule stored)');
  document.getElementById('dMets').innerHTML=[
    ['Trades',fmtNum(s.n)],['Symbols',s.symbols],['Avg net',fmtPct(s.avg_net,3)],
    ['Portfolio',fmtPct(s.portfolio_net,1)],['Max DD',fmtPct(s.max_dd,1)],['Win rate',fmtPct(s.win_rate,1)],
    ['Profit factor',s.profit_factor>=999?'∞':s.profit_factor.toFixed(2)],['Cost drag',fmtPct(s.fee_drag,3)],
    ['Long / Short',`${fmtNum(s.long_n)} / ${fmtNum(s.short_n)}`],['Long PnL sum',fmtPct(s.long_net,2)],
    ['Short PnL sum',fmtPct(s.short_net,2)],['Avg hold',`${(s.avg_hold_h||0).toFixed(1)}h`]
  ].map(([k,v])=>`<div><b>${v}</b><span>${k}</span></div>`).join('');
  const yrs=Object.entries(s.yearly||{}).map(([y,v])=>`<span>${y}: <b class="${v>=0?'pos':'neg'}">${fmtPct(v,1)}</b></span>`).join('');
  document.getElementById('dYears').innerHTML=yrs;
  const pts=[['2022-08',1.0],...s.monthly.map((m,i)=>[m,s.monthly_equity[i]])];
  lineChart(document.getElementById('dChart'),[{name:s.sid,color:'#4fd1c5',points:pts,width:2.4}]);
}

document.querySelectorAll('#specTable th').forEach(th=>{
  const k=th.dataset.k; if(!k)return;
  th.addEventListener('click',()=>{
    if(state.sort===k)state.dir*=-1; else {state.sort=k;state.dir=-1;}
    renderSpecs();
  });
});
['q','tfFilter','famFilter','confFilter','minN','uniqOnly'].forEach(id=>document.getElementById(id).addEventListener('input',renderSpecs));
document.getElementById('resetBtn').addEventListener('click',()=>{
  document.getElementById('q').value='';document.getElementById('tfFilter').value='';document.getElementById('famFilter').value='';
  document.getElementById('confFilter').value='';document.getElementById('minN').value=20;document.getElementById('uniqOnly').checked=true;state.sort='median_symbol_net';state.dir=-1;renderSpecs();
});

// batches
function renderBatches(){
  const st=document.getElementById('bStatus').value;
  const q=document.getElementById('bq').value.toLowerCase();
  let rows=DATA.batches.filter(b=>!st||b.status===st);
  if(q)rows=rows.filter(b=>(b.batch+' '+b.best_sid+' '+b.best_title+' '+(b.reasons||[]).join(' ')).toLowerCase().includes(q));
  document.getElementById('bcount').textContent=`${rows.length} batches`;
  const badge={tested:['b-tested','Tested'],low_only:['b-low','Low confidence only'],excluded_only:['b-exc','Excluded only'],no_sections:['b-none','No sections']};
  document.querySelector('#batchTable tbody').innerHTML=rows.map(b=>{
    const [cls,lab]=badge[b.status]||['b-none',b.status];
    const reason=(b.reasons&&b.reasons[0])|| (b.status==='low_only'?'Only low-confidence mechanical mappings.':b.status==='no_sections'?'No ### strategy sections in this batch.':'—');
    return `<tr>
      <td><b>${b.batch.replace('batch_','')}</b></td>
      <td><span class="badge ${cls}">${lab}</span></td>
      <td class="num">${b.sections}</td><td class="num">${b.tested}</td><td class="num">${b.low}</td><td class="num">${b.excluded}</td>
      <td title="${esc(b.best_title)}" style="max-width:330px;overflow:hidden;text-overflow:ellipsis">${b.best_sid?`<b>${esc(b.best_sid)}</b>${b.best_is_duplicate?` <span style="color:var(--amber)">→ ${esc(b.best_rule_lead)}</span>`:''} · ${esc(b.best_title)}`:'—'}</td>
      <td>${b.best_tf?`<span class="pill tf-${b.best_tf}">${b.best_tf}</span>`:'—'}</td>
      <td class="num ${b.best_portfolio_net>=0?'pos':'neg'}">${b.best_portfolio_net==null?'—':fmtPct(b.best_portfolio_net,1)}</td>
      <td class="num ${b.best_median_symbol_net>=0?'pos':'neg'}">${b.best_median_symbol_net==null?'—':fmtPct(b.best_median_symbol_net,2)}</td>
      <td class="num">${b.best_n||'—'}</td>
      <td style="max-width:360px;white-space:normal;color:var(--dim)">${esc(reason)}</td>
    </tr>`;
  }).join('');
}
document.getElementById('bStatus').addEventListener('change',renderBatches);
document.getElementById('bq').addEventListener('input',renderBatches);

initOverview();drawConsChart();renderSpecs();renderBatches();
</script>
</body>
</html>'''

n_trades_all = sum(s['n'] for s in specs)
HTML = (HTML
        .replace('__DATA__', json.dumps(DATA, ensure_ascii=False).replace('</', '<\\/'))
        .replace('__SERIES_STRAT__', json.dumps(series_strat, ensure_ascii=False))
        .replace('__SERIES_BENCH__', json.dumps(series_bench, ensure_ascii=False))
        .replace('__N_SPECS__', num(meta['n_tested_specs']))
        .replace('__N_UNIQUE__', str(meta.get('n_unique_rules', meta['n_tested_specs'])))
        .replace('__N_BATCHES__', str(meta['n_tested_batches']))
        .replace('__N_LOW__', str(meta['n_low_batches']))
        .replace('__N_EXC__', str(meta['n_excluded_batches']))
        .replace('__N_NONE__', str(meta['n_no_sections']))
        .replace('__N_SYMBOLS__', str(meta['n_symbols']))
        .replace('__N_TRADES__', (f'{n_trades_all / 1e6:.1f}M' if n_trades_all >= 1e6 else num(n_trades_all)))
        .replace('__FINDINGS__', findings)
        .replace('__TF_ROWS__', tf_html)
        .replace('__FAM_ROWS__', fam_html)
        .replace('__SEG__', seg)
        .replace('__BTC_RET__', pct(bench.get('btc_return', 0), 1))
        .replace('__BTC_DD__', pct(dd_from_pnl(bench.get('btc_pnl', [])), 1))
        .replace('__BASKET_RET__', pct(bench.get('basket_return', 0), 1))
        .replace('__BASKET_DD__', pct(dd_from_pnl(bench.get('basket_pnl', [])), 1))
        .replace('__EXC_HTML__', exc_html))

out = os.path.join(BT, 'dashboard.html')
open(out, 'w', encoding='utf-8').write(HTML)
print('wrote', out, len(HTML), 'bytes')
