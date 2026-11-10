import os

ROOT = r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest\filter_layer'

HTML = r'''<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" href="data:,">
<title>Filtre Laboratuvarı · 525 sembol</title>
<script src="assets/echarts.min.js"></script>
<style>
@font-face{font-family:'Inter';src:url('assets/fonts/inter-400.woff2') format('woff2');font-weight:400;font-style:normal;font-display:swap}
@font-face{font-family:'Inter';src:url('assets/fonts/inter-600.woff2') format('woff2');font-weight:600;font-style:normal;font-display:swap}
@font-face{font-family:'Inter';src:url('assets/fonts/inter-700.woff2') format('woff2');font-weight:700;font-style:normal;font-display:swap}
@font-face{font-family:'JetBrains Mono';src:url('assets/fonts/jetbrains-400.woff2') format('woff2');font-weight:400;font-style:normal;font-display:swap}
@font-face{font-family:'JetBrains Mono';src:url('assets/fonts/jetbrains-600.woff2') format('woff2');font-weight:600;font-style:normal;font-display:swap}
:root{
  --bg:#09111c;--panel:#101d2b;--panel2:#142334;--line:#26384a;
  --text:#e8f0f4;--muted:#91a6b6;--dim:#64798b;
  --accent:#6caaff;--green:#46d49a;--red:#ff6f7d;--amber:#f2c674;--purple:#b794f4;
}
*{box-sizing:border-box}
html,body{margin:0;background:var(--bg);color:var(--text);font-family:Inter,"Segoe UI",Arial,sans-serif;line-height:1.5}
body{background:var(--bg);font-size:14px}
.app{display:grid;grid-template-columns:275px minmax(0,1fr);min-height:100vh}
aside{border-right:1px solid var(--line);background:#0e1927;padding:24px 18px 44px;position:sticky;top:0;height:100vh;overflow:auto}
.brand{font-size:11px;letter-spacing:2px;text-transform:uppercase;color:var(--accent);font-weight:800}
h1{font-size:25px;line-height:1.08;margin:8px 0 6px;letter-spacing:-.5px;font-weight:700}
.sub{font-size:12px;color:var(--muted);margin:0 0 22px;line-height:1.5}
.step{padding:0;border:0;background:transparent;margin:21px 0}
.step.active{border:0;background:transparent}
.stepno{font-size:11px;letter-spacing:2px;color:var(--accent);font-weight:800;margin-bottom:6px;text-transform:uppercase}
.step label{display:block;color:#b8cad5;font-size:12px;font-weight:650;margin-bottom:7px}
select,input[type=text],input[type=number]{width:100%;background:#172738;border:1px solid #34475a;color:var(--text);border-radius:9px;padding:10px 11px;font:inherit;font-size:12px;outline:none}
select:focus,input:focus{border-color:var(--accent)}
.filters{display:flex;flex-direction:column;gap:2px;max-height:390px;overflow:auto;padding-right:2px}
.fbtn{appearance:none;border:1px solid transparent;background:transparent;color:var(--muted);text-align:left;border-radius:7px;padding:7px 6px;cursor:pointer;font:inherit;font-size:11.5px;display:grid;grid-template-columns:1fr auto;gap:5px}
.fbtn:hover{background:#1b3043;color:var(--text)}
.fbtn.active{background:#1b3952;border-color:#376282;color:var(--accent)}
.fbtn b{font-weight:600;color:var(--text);display:block;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.fbtn small{color:var(--muted);font-size:10px;display:block;margin-top:1px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.fcount{font-variant-numeric:tabular-nums;color:var(--muted);font-size:10px;align-self:center}
.toggles{display:flex;flex-direction:column;gap:7px;margin-top:4px}
.toggle{display:flex;align-items:center;justify-content:space-between;color:#c5d5df;font-size:11px;cursor:pointer}
.toggle input{width:auto;accent-color:var(--accent)}
.side-note{border-top:1px solid var(--line);margin-top:18px;padding-top:17px;color:var(--muted);font-size:12px;line-height:1.6}
main{padding:26px 30px 50px;min-width:0;max-width:1800px}
.top{display:flex;justify-content:space-between;gap:18px;align-items:flex-start;flex-wrap:wrap;margin-bottom:16px}
.top h2{font-size:25px;line-height:1.08;margin:0;letter-spacing:-.5px;font-weight:700}
.top p{color:var(--muted);font-size:14px;margin:6px 0 0;max-width:900px}
.crumb{font-size:11px;letter-spacing:2px;text-transform:uppercase;color:var(--accent);font-weight:800;margin-bottom:6px}
.switchbox{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:12px 14px;min-width:280px}
.switchbox label{display:block;color:#b8cad5;font-size:11px;font-weight:650;margin-bottom:6px}
.kpis{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px;margin:18px 0 12px}
.daykpis{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin:0 0 18px}
.daycard{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:14px 17px;display:flex;align-items:center;justify-content:space-between;gap:12px}
.daycard .dk{font-size:12px;color:var(--muted);font-weight:650}
.daycard .dv{font-size:26px;font-weight:750;letter-spacing:-.5px;font-variant-numeric:tabular-nums;display:flex;gap:6px;align-items:baseline}
.daycard .dv .sep{color:var(--muted);font-size:17px;font-weight:400}
.daycard .ds{font-size:11px;color:var(--muted);margin-top:2px}
.kpi{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:16px 18px;min-width:0}
.kpi .v{font-size:26px;font-weight:750;letter-spacing:-.5px;font-variant-numeric:tabular-nums;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.kpi .l{font-size:12px;color:var(--muted);margin-top:3px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.section{margin:25px 0}
.section-head{display:flex;justify-content:space-between;align-items:flex-end;margin:0 0 13px}
.section-head h3{font-size:16px;margin:0;letter-spacing:-.01em;font-weight:700}
.section-head span{font-size:12px;color:var(--muted)}
.grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:13px}
.grid3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:13px}
.card{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:18px;min-width:0}
.card h4{font-size:14px;margin:0 0 3px;font-weight:650;letter-spacing:-.01em}
.card .hint{font-size:11px;color:var(--muted);margin:0 0 7px;min-height:13px}
.period-split{display:grid;grid-template-columns:1fr 1fr;gap:13px}
.period-panel{border:1px solid var(--line);border-radius:14px;padding:18px;background:var(--panel);min-width:0}
.period-panel.now{border-color:#376282;background:var(--panel2)}
.period-head{display:flex;justify-content:space-between;align-items:flex-end;gap:8px;margin-bottom:12px}
.period-head h3{font-size:16px;margin:0;letter-spacing:-.02em;font-weight:700}
.period-head span{font-size:11px;color:var(--muted)}
.period-metrics{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:7px;margin-bottom:12px}
.pm{background:#122131;border:1px solid #223449;border-radius:8px;padding:8px 9px;min-width:0}
.pm .v{font-size:14px;font-weight:700;font-variant-numeric:tabular-nums;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.pm .l{font-size:9.5px;color:var(--muted);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;margin-top:1px}
.period-panel .chart{height:220px}
.period-panel .chart.tiny{height:180px}
.period-panel .subhead{font-size:10px;color:var(--muted);text-transform:uppercase;letter-spacing:.08em;margin:12px 0 4px}
.chart{width:100%;height:340px}
.chart.tall{height:400px}
.chart.short{height:260px}
.wide{grid-column:1/-1}
.pos{color:var(--green)}.neg{color:var(--red)}.amber{color:var(--amber)}
.badge{display:inline-block;padding:2px 7px;border-radius:7px;font-size:10px;border:1px solid var(--line);color:var(--muted)}
.tablewrap{max-height:590px;overflow:auto;border:1px solid var(--line);border-radius:9px}
table{width:100%;border-collapse:collapse;font-size:12px}
th,td{padding:9px;border-bottom:1px solid #223449;text-align:left;white-space:nowrap}
th{color:#a9c0cf;font-size:11px;position:sticky;top:0;background:#192b3d;z-index:2;cursor:pointer;text-align:right}
th:first-child,td:first-child{text-align:left}
tr.rowline{cursor:pointer}tr.rowline:hover{background:#1a3042}tr.sel{background:#1b3952}
td.num,th.num{text-align:right;font-variant-numeric:tabular-nums}
.toolbar{display:flex;gap:11px;align-items:center;flex-wrap:wrap;margin:4px 0 12px;color:var(--muted);font-size:12px}
.toolbar label{display:flex;align-items:center;gap:5px}
.toolbar input[type=checkbox]{appearance:none;width:15px;height:15px;border:1px solid #3c5670;border-radius:4px;background:#122131;cursor:pointer;position:relative;margin:0}
.toolbar input[type=checkbox]:checked{background:var(--accent);border-color:var(--accent)}
.toolbar input[type=checkbox]:checked::after{content:'✓';position:absolute;inset:0;color:#09111c;font-size:11px;font-weight:800;display:flex;align-items:center;justify-content:center}
.tabs{display:flex;gap:6px;border-bottom:1px solid var(--line);margin:0 0 20px;position:sticky;top:0;z-index:20;background:var(--bg);padding-top:8px}
.tabbtn{appearance:none;background:transparent;border:0;border-bottom:2px solid transparent;border-radius:0;color:var(--muted);padding:11px 15px;font:inherit;font-size:13px;font-weight:650;cursor:pointer}
.tabbtn:hover{background:transparent;color:var(--text)}
.tabbtn.active{color:var(--accent);border-bottom-color:var(--accent);background:transparent}
.tabcount{font-size:11px;color:var(--muted);margin-left:7px;font-weight:500}
.tabpane[hidden]{display:none}
.scanwrap{max-height:calc(100vh - 300px)}
.scanwrap table{font-size:12px}
.scanwrap td,.scanwrap th{padding:8px 10px}
.scorebar{height:5px;border-radius:3px;background:#223449;overflow:hidden;margin-top:4px;width:74px;margin-left:auto}
.scorebar i{display:block;height:100%}
.mini{font-size:10px;color:var(--muted);margin-top:2px;max-width:190px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.scorekey{font-size:11.5px;color:var(--muted);line-height:1.75}
.scorekey b{color:var(--text);font-weight:650}
th.sortasc::after{content:' ▲';color:var(--accent)}
th.sortdesc::after{content:' ▼';color:var(--accent)}
.thwrap{display:flex;align-items:center;justify-content:space-between;gap:6px;width:100%}
th:first-child .thwrap{justify-content:flex-start}
.fcaret{border:1px solid transparent;background:transparent;color:var(--muted);cursor:pointer;padding:2px 5px;border-radius:5px;font-size:10px;line-height:1;opacity:.5;margin-left:auto}
.fcaret:hover{opacity:1;background:#24405a;color:var(--text);border-color:#376282}
th.filtered .fcaret{opacity:1;color:var(--accent);border-color:#376282;background:#1b3952}
#colMenu{position:fixed;z-index:80;background:var(--panel2);border:1px solid #376282;border-radius:12px;padding:12px;min-width:258px;max-width:320px;box-shadow:0 18px 44px rgba(0,0,0,.55);display:none;font-size:12px}
.cm-head{display:flex;justify-content:space-between;align-items:baseline;gap:8px;font-weight:700;margin-bottom:9px}
.cm-sub{font-size:10px;color:var(--muted);font-weight:500}
.cm-sort{display:flex;gap:6px;margin:0 0 9px}
.cm-sort button{flex:1;padding:6px 8px;font-size:11px;background:#16283a;border:1px solid #2d4459;color:var(--text);border-radius:7px}
.cm-sort button:hover{background:#24405a}
.cm-list{max-height:230px;overflow:auto;border:1px solid var(--line);border-radius:8px;margin:7px 0;background:#0f1c29}
.cm-item{display:grid;grid-template-columns:auto 1fr auto;gap:7px;align-items:center;padding:5px 8px;cursor:pointer;color:var(--text)}
.cm-item:hover{background:#1b3043}
.cm-item input{accent-color:var(--accent);margin:0}
.cm-item span{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.cm-item b{font-weight:500;color:var(--muted);font-size:10px}
.cm-all{display:flex;align-items:center;gap:7px;color:var(--muted);font-size:11.5px;margin:6px 0 0;cursor:pointer}
.cm-all input{accent-color:var(--accent);margin:0}
.cm-row{display:grid;grid-template-columns:64px 1fr;gap:8px;align-items:center;margin:7px 0}
.cm-row label{color:var(--muted);font-size:11.5px}
.cm-note{font-size:10.5px;color:var(--muted);margin:8px 0 0}
.cm-actions{display:flex;gap:7px;margin-top:10px}
.cm-actions button{flex:1;padding:7px 9px;font-size:11.5px}
.cm-none{color:var(--muted);font-size:11px;padding:9px}
#scanClearCols{background:#1b3952;border:1px solid #376282;color:var(--text);font-size:11.5px;padding:6px 10px;border-radius:8px}
.rule{font-family:'JetBrains Mono',monospace;font-size:10px;color:#b8c7dd;background:#09111c;border:1px solid var(--line);border-radius:8px;padding:10px;white-space:pre-wrap;overflow:auto;max-height:140px}
.empty{display:flex;align-items:center;justify-content:center;height:100%;min-height:180px;color:var(--muted);font-size:12px}
.loading{position:fixed;inset:0;background:#09111c;display:flex;align-items:center;justify-content:center;z-index:50;color:var(--accent);font-size:18px}
.note{font-size:12px;color:var(--muted);border-top:1px solid var(--line);padding-top:10px;margin-top:14px;line-height:1.6}
button{background:#1b3952;border:1px solid #376282;color:var(--text);border-radius:8px;padding:8px 11px;cursor:pointer;font:inherit;font-size:12px}
button:hover{background:#245071}
.footer{font-size:12px;color:var(--muted);margin-top:20px;line-height:1.7}
@media(max-width:1300px){.kpis{grid-template-columns:repeat(4,1fr)}.grid3{grid-template-columns:repeat(2,1fr)}}
@media(max-width:1000px){.app{grid-template-columns:1fr}aside{position:relative;height:auto}.grid,.grid3,.period-split{grid-template-columns:1fr}.kpis{grid-template-columns:repeat(2,1fr)}.daykpis{grid-template-columns:1fr}.period-metrics{grid-template-columns:repeat(2,1fr)}}
</style>
</head>
<body>
<div class="loading" id="loading">Veri yükleniyor…</div>
<div class="app">
<aside>
  <div class="brand">Book Signal Review</div>
  <h1>Filtre Laboratuvarı</h1>
  <div class="sub">525 sembol · 14 rejim filtresi · 1m execution</div>

  <div class="step">
    <div class="stepno">01 · ZAMAN DİLİMİ</div>
    <label>Timeframe filtresi</label>
    <select id="tfFilter">
      <option value="">Tümü</option>
      <option value="1d">1d</option>
      <option value="4h">4h</option>
      <option value="1h">1h</option>
      <option value="1w">1w</option>
    </select>
  </div>

  <div class="step">
    <div class="stepno">02 · STRATEJİ</div>
    <label>Strateji seç</label>
    <select id="strategySel"></select>
    <input type="text" id="strategySearch" placeholder="SID / aile ara…" style="margin-top:6px">
  </div>

  <div class="step active">
    <div class="stepno">03 · FİLTRE</div>
    <div class="filters" id="filterList"></div>
  </div>

  <div class="step">
    <div class="stepno">04 · GÖRÜNÜM</div>
    <div class="toggles">
      <label class="toggle">Sadece pozitif <input type="checkbox" id="positiveOnly" checked></label>
      <label class="toggle">Bazı göster <input type="checkbox" id="showBase" checked></label>
      <label class="toggle">Min işlem <input type="number" id="minN" value="20" min="0" step="10" style="width:64px"></label>
    </div>
  </div>

  <div class="side-note">
    Yeşil/kırmızı günlük bar aynı günün pozitif ve negatif realized PnL'ini birlikte gösterir.
    Filtreler tek tek uygulanır; sonuçlar fee + slippage + funding dahildir.
  </div>
</aside>

<main>
  <nav class="tabs">
    <button class="tabbtn active" data-tab="overview">Genel bakış</button>
    <button class="tabbtn" data-tab="scan">Strateji taraması<span class="tabcount" id="scanTabCount"></span></button>
  </nav>

  <div id="tab-overview" class="tabpane">
  <div class="top">
    <div>
      <div class="crumb" id="crumb">Strateji seç</div>
      <h2 id="title">—</h2>
      <p id="subtitle"></p>
    </div>
    <div class="switchbox">
      <label>Uygulanacak filtre (switch)</label>
      <select id="filterSwitch"></select>
    </div>
  </div>

  <div class="kpis" id="kpis"></div>
  <div class="daykpis" id="daykpis"></div>

  <div class="section">
    <div class="section-head"><h3>Filtre etkisi</h3><span>Seçili stratejide 14 filtrenin etkisi</span></div>
    <div class="grid">
      <div class="card"><h4>Ortalama işlem başı net</h4><p class="hint">Seçili strateji · filtre bazında</p><div class="chart" id="filterAvg"></div></div>
      <div class="card"><h4>Medyan sembol neti</h4><p class="hint">Tek bir sembolün baskın olmasını engeller</p><div class="chart" id="filterMedian"></div></div>
      <div class="card wide"><h4>Filtre heatmap’i</h4><p class="hint">Mevcut 14 filtre · en fazla 20 strateji · ortalama net</p><div class="chart tall" id="filterHeatmap"></div></div>
      <div class="card"><h4>Filtre özeti</h4><p class="hint">Pozitif sonuç sayısı, ortalama net, medyan sembol neti</p><div id="filterStats"></div></div>
      <div class="card"><h4>Kapsam notu</h4><p class="hint">Veriyle doğrudan hesaplanamayan alanlar</p><div class="note" style="border:0;padding:0;margin:0">5m SL/TP sırası, çıkış nedeni dağılımı ve ortalama R, mevcut trade export’unda stop mesafesi/çıkış nedeni tutulmadığı için bu sürümde yok. 56 filtre değil, çalışılmış 14 filtre var.</div></div>
    </div>
  </div>

  <div class="section">
    <div class="section-head"><h3>Dönem karşılaştırması</h3><span>Sol: tüm yıllar · Sağ: yalnızca 2026</span></div>
    <div class="period-split">
      <section class="period-panel">
        <div class="period-head"><h3>TÜM YILLAR</h3><span id="allPeriodMeta"></span></div>
        <div class="period-metrics" id="allMetrics"></div>
        <div class="subhead">Günlük kâr / zarar</div><div class="chart" id="allDaily"></div>
        <div class="subhead">Günlük işlem sayısı</div><div class="chart tiny" id="allCount"></div>
        <div class="subhead">Haftalık kâr / zarar</div><div class="chart tiny" id="allWeekly"></div>
        <div class="subhead">Aylık kâr / zarar</div><div class="chart tiny" id="allMonthly"></div>
        <div class="subhead">Mevsimsel kâr / zarar</div><div class="chart tiny" id="allSeason"></div>
        <div class="subhead">$10 / işlem kasa eğrisi</div><div class="chart tiny" id="allCash"></div>
      </section>
      <section class="period-panel now">
        <div class="period-head"><h3>2026</h3><span id="y26PeriodMeta"></span></div>
        <div class="period-metrics" id="y26Metrics"></div>
        <div class="subhead">Günlük kâr / zarar</div><div class="chart" id="y26Daily"></div>
        <div class="subhead">Günlük işlem sayısı</div><div class="chart tiny" id="y26Count"></div>
        <div class="subhead">Haftalık kâr / zarar</div><div class="chart tiny" id="y26Weekly"></div>
        <div class="subhead">Aylık kâr / zarar</div><div class="chart tiny" id="y26Monthly"></div>
        <div class="subhead">Mevsimsel kâr / zarar</div><div class="chart tiny" id="y26Season"></div>
        <div class="subhead">$10 / işlem kasa eğrisi</div><div class="chart tiny" id="y26Cash"></div>
      </section>
    </div>
  </div>

  <div class="section">
    <div class="section-head"><h3>Coin bazında net</h3><span>En aktif 40 sembol · tüm yıllar</span></div>
    <div class="card"><div class="chart" id="allCoins"></div></div>
  </div>

  <div class="section">
    <div class="section-head"><h3>Portföy ve risk</h3><span>1/525 hesap · tüm yıllar</span></div>
    <div class="grid">
      <div class="card"><h4>Kümülatif net özsermaye</h4><p class="hint">Günlük netlerin bileşiği</p><div class="chart" id="equity"></div></div>
      <div class="card"><h4>Drawdown</h4><p class="hint">Önceki zirveye uzaklık</p><div class="chart" id="drawdown"></div></div>
      <div class="card wide"><h4>Hareketli 30 / 90 / 365 günlük net getiri</h4><p class="hint">Günlük netin kayan toplamı; 1/525 hesap</p><div class="chart short" id="rolling"></div></div>
    </div>
  </div>

  <div class="section">
    <div class="section-head"><h3>Dönemsel analiz</h3><span>Yıl · mevsim · çeyrek · ay · hafta günü · kalma süresi</span></div>
    <div class="grid3">
      <div class="card"><h4>Yıllık kâr / zarar</h4><p class="hint">Yeşil yukarı, kırmızı aşağı</p><div class="chart" id="yearly"></div></div>
      <div class="card"><h4>Mevsimsel kâr / zarar</h4><p class="hint">Aynı bar üzerinde kâr ve zarar</p><div class="chart" id="seasonal"></div></div>
      <div class="card"><h4>Çeyreklik kâr / zarar</h4><p class="hint">Q1–Q4</p><div class="chart" id="quarterly"></div></div>
      <div class="card"><h4>Aylık heatmap</h4><p class="hint">Yıl × ay net PnL</p><div class="chart" id="monthHeat"></div></div>
      <div class="card"><h4>Hafta günü</h4><p class="hint">Pzt–Paz kâr / zarar</p><div class="chart" id="weekday"></div></div>
      <div class="card"><h4>İşlemde kalma süresi</h4><p class="hint">&lt;1s … 4h+ işlem sayısı</p><div class="chart" id="hold"></div></div>
      <div class="card"><h4>Kalma süresine göre kâr / zarar</h4><p class="hint">Her süre aralığında brüt kâr ve zarar</p><div class="chart" id="holdPnl"></div></div>
    </div>
  </div>

  <div class="section">
    <div class="section-head"><h3>Trade analizi</h3><span>Long / Short ve getiri–kalma ilişkisi</span></div>
    <div class="grid">
      <div class="card"><h4>Long vs Short</h4><p class="hint">Toplam hesap PnL ve işlem sayısı</p><div class="chart" id="longShort"></div></div>
      <div class="card"><h4>Getiri vs kalma süresi</h4><p class="hint">Her nokta bir işlem; x gün, y getiri</p><div class="chart" id="scatter"></div></div>
    </div>
  </div>

  <div class="section">
    <div class="section-head"><h3>Seçili kural</h3><span id="ruleMeta"></span></div>
    <div class="card"><div class="rule" id="ruleBox">—</div></div>
  </div>

  </div><!-- /tab-overview -->

  <div id="tab-scan" class="tabpane" hidden>
    <div class="top">
      <div>
        <div class="crumb">Sıralanabilir tarama</div>
        <h2>Strateji × filtre × timeframe</h2>
        <p>Her satır tek bir kombinasyon. Sütun başlığına tıkla: artan / azalan sırala. Satıra tıkla: stratejiyi genel bakışta aç.</p>
      </div>
      <div class="switchbox">
        <label>Puan nasıl hesaplanır (0–100)</label>
        <div class="scorekey">
          <b>P2</b> net/işlem (tüm yıllar) · min→0, max→33.3<br>
          <b>P4</b> kârlı işlem ort. süresi (saat) · ters: min→33.3, max→0<br>
          <b>P5</b> kârlı / zararlı oranı · min→0, max→33.3<br>
          <b>Puan</b> = P2 + P4 + P5
        </div>
      </div>
    </div>

    <div class="toolbar">
      <input type="text" id="scanSearch" placeholder="SID / filtre / TF ara…" style="max-width:260px">
      <label>Min işlem <input type="number" id="scanMinN" value="0" min="0" step="10" style="width:78px"></label>
      <label class="toggle" style="color:var(--muted)"><input type="checkbox" id="scanPositive"> sadece pozitif</label>
      <label class="toggle" style="color:var(--muted)"><input type="checkbox" id="scanBase" checked> filtresiz baz dahil</label>
      <span id="scanHint"></span>
      <button id="scanClearCols" style="display:none">Sütun filtrelerini temizle (<span id="scanColCount">0</span>)</button>
    </div>
    <div class="tablewrap scanwrap"><table id="scanTable"><thead></thead><tbody></tbody></table></div>
  </div>
  <div id="colMenu"></div>

  <div class="note">
    274 high/medium source mapping → 120 benzersiz kural (116'sı işlem üretti; 1d/4h/1h/1w).
    5m/15m filtre katmanına alınmadı: brüt kenar zaten negatif; 219M işlemde filtre maliyeti karşılamıyor.
    “Tüm kombinasyonlar” = her strateji × her filtre (tek tek); 14 filtrenin 2^14 alt kümesi değildir.
    Sonuçlar fee, slippage ve funding dahildir; geçmiş performans gelecek getiriyi garanti etmez.
  </div>
  <div class="footer">Filtre Laboratuvarı · 525 Binance USDT-M perpetual · 1m execution · yerel ECharts</div>
</main>
    274 high/medium source mapping → 120 benzersiz kural (116'sı işlem üretti; 1d/4h/1h/1w).
    5m/15m filtre katmanına alınmadı: brüt kenar zaten negatif; 219M işlemde filtre maliyeti karşılamıyor.
    “Tüm kombinasyonlar” = her strateji × her filtre (tek tek); 14 filtrenin 2^14 alt kümesi değildir.
    Sonuçlar fee, slippage ve funding dahildir; geçmiş performans gelecek getiriyi garanti etmez.
  </div>
  <div class="footer">Filtre Laboratuvarı · 525 Binance USDT-M perpetual · 1m execution · yerel ECharts</div>
</main>
</div>

<script>
let DATA=null;
const state={idx:null,filter:'baseline',tf:'',positiveOnly:true,showBase:true,minN:20,tableSort:'median_symbol_net',tableDir:-1};
const charts={};
const PAL={green:'#46d49a',red:'#ff6f7d',accent:'#6caaff',amber:'#f2c674',purple:'#b794f4',dim:'#64798b',line:'#26384a',text:'#e8f0f4'};
const fmtPct=(x,d=2)=>x==null||!isFinite(x)?'—':(x*100).toFixed(d)+'%';
const fmtNum=(x)=>x==null?'—':Math.round(x).toLocaleString('en-US');
const esc=(s)=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const dayDate=(d)=>new Date(d*86400000);
const dayStr=(d)=>dayDate(d).toISOString().slice(0,10);
const DAY=86400000;
const FROM26=Date.UTC(2025,0,1)/DAY;
const TO26=Date.UTC(2026,11,31)/DAY;
const FROM2026=Date.UTC(2026,0,1)/DAY;
const TO2026=Date.UTC(2026,11,31)/DAY;
const rkey=(idx,fid)=>`${idx}|${fid}`;

function chart(id){
  if(!charts[id]) charts[id]=echarts.init(document.getElementById(id),null,{renderer:'canvas'});
  return charts[id];
}
function setChart(id,opt){
  const c=chart(id);
  c.setOption(opt,true);
}
function baseText(){return {fontFamily:'Inter',color:PAL.text};}
function grid(pad){return {left:pad??54,right:18,top:18,bottom:32,containLabel:true};}
function axisCat(data,extra={}){return Object.assign({type:'category',data:data,axisLine:{lineStyle:{color:PAL.line}},axisLabel:{color:PAL.dim,fontSize:9},axisTick:{show:false}},extra);}
function axisVal(extra={}){return Object.assign({type:'value',axisLine:{show:false},axisLabel:{color:PAL.dim,fontSize:9},splitLine:{lineStyle:{color:'rgba(34,49,77,.55)'}}},extra);}
function tooltip(extra={}){return Object.assign({trigger:'axis',backgroundColor:'#101d2b',borderColor:PAL.line,textStyle:{color:PAL.text,fontFamily:'Inter',fontSize:10},axisPointer:{type:'shadow'}},extra);}
function emptyOpt(msg){return {title:{text:msg,left:'center',top:'middle',textStyle:{color:PAL.dim,fontSize:11,fontWeight:400}},xAxis:{show:false},yAxis:{show:false},series:[]};}

function strategyList(){return DATA.specs.filter(s=>!state.tf||s.tf===state.tf);}
function specByIdx(idx){return DATA.specs.find(s=>s.idx===idx)||null;}
function resultFor(idx,fid){return DATA.results.find(r=>r.idx===idx&&r.filter_key===fid)||null;}
function baselineFor(idx){return resultFor(idx,'baseline');}
function selectedResult(){return resultFor(state.idx,state.filter)||baselineFor(state.idx);}
function filterDefs(){return [{id:'baseline',label:'Filtresiz baz',label_tr:'Filtresiz baz',bit:null},...DATA.filters];}
function filterLabel(fid){const f=filterDefs().find(x=>x.id===fid);return f?f.label_tr:fid;}

function initSelectors(){
  const tf=document.getElementById('tfFilter');
  tf.value=state.tf;
  tf.addEventListener('change',()=>{state.tf=tf.value;buildStrategyOptions();});
  document.getElementById('strategySearch').addEventListener('input',buildStrategyOptions);
  document.getElementById('strategySel').addEventListener('change',e=>{state.idx=+e.target.value;if(!resultFor(state.idx,state.filter))state.filter='baseline';renderAll();});
  document.getElementById('filterSwitch').addEventListener('change',e=>{state.filter=e.target.value;renderAll();});
}
function buildStrategyOptions(){
  const q=document.getElementById('strategySearch').value.toLowerCase();
  const opts=strategyList().filter(s=>(!q||`${s.sid} ${s.title} ${s.family} ${s.tf}`.toLowerCase().includes(q)));
  const sel=document.getElementById('strategySel');
  const current=state.idx;
  sel.innerHTML=opts.map(s=>`<option value="${s.idx}">${esc(s.sid)} · ${esc(s.tf)} · ${esc(s.family)}</option>`).join('');
  if(opts.length){
    if(!opts.some(s=>s.idx===current)) state.idx=opts[0].idx;
    sel.value=String(state.idx);
  }
  if(!resultFor(state.idx,state.filter)) state.filter='baseline';
  renderAll();
}

function renderFilterList(){
  const el=document.getElementById('filterList');
  el.innerHTML=filterDefs().map(f=>{
    const st=DATA.filter_stats.find(x=>x.id===f.id)||{};
    return `<button class="fbtn ${state.filter===f.id?'active':''}" data-fid="${esc(f.id)}"><span><b>${esc(f.label_tr)}</b><small>${esc(f.label)}</small></span><span class="fcount">${f.id==='baseline'?'baz':`${st.n_positive||0}/${st.n_results||0}`}</span></button>`;
  }).join('');
  el.querySelectorAll('button').forEach(b=>b.addEventListener('click',()=>{state.filter=b.dataset.fid;renderAll();}));
}
function syncSwitch(){
  const sel=document.getElementById('filterSwitch');
  sel.innerHTML=filterDefs().map(f=>`<option value="${f.id}">${esc(f.label_tr)}</option>`).join('');
  sel.value=state.filter;
}
function renderHeader(r){
  const s=specByIdx(state.idx)||{};
  document.getElementById('title').textContent=s.sid?`${s.sid} · ${s.title.replace(s.sid,'').replace(/^[\s—–-]+/,'')}`:'Strateji seç';
  document.getElementById('crumb').textContent=`${s.tf||''} · ${s.family||''} · ${r?filterLabel(r.filter_key):''}`;
  document.getElementById('subtitle').textContent=r?`${fmtNum(r.n)} işlem · ${r.symbols} sembol · ${fmtPct(r.avg_net,3)} ortalama net · 2026 ${fmtPct(r.ret_2026,2)} · portföy ${fmtPct(r.portfolio_net,2)}`:'Bu kombinasyon için veri yok.';
}
function dayStats(r, from=null, to=null){
  let green=0,red=0,flat=0;
  (r?.daily||[]).forEach(x=>{
    if(from!=null&&x[0]<from)return;
    if(to!=null&&x[0]>to)return;
    if(x[4]>0)green++; else if(x[4]<0)red++; else flat++;
  });
  return {green,red,flat};
}
function renderDayKpis(r){
  const t=dayStats(r), y=dayStats(r,FROM2026,TO2026);
  const card=(label,a)=>`<div class="daycard"><div><div class="dk">${label}</div><div class="ds">${a.flat?`${a.flat} yatay gün · `:''}günlük net PnL</div></div><div class="dv"><span class="pos">${a.green}</span><span class="sep">/</span><span class="neg">${a.red}</span></div></div>`;
  document.getElementById('daykpis').innerHTML=card('Kârlı / zararlı gün · Tüm dönem',t)+card('Kârlı / zararlı gün · 2026',y);
}
function renderKpis(r){
  const k=[
    ['İşlem',fmtNum(r?.n)],['Ort. net',fmtPct(r?.avg_net,3)],['2026 net',fmtPct(r?.ret_2026,2)],
    ['Med. sembol',fmtPct(r?.median_symbol_net,2)],['Portföy',fmtPct(r?.portfolio_net,2)],
    ['Kazanma',fmtPct(r?.win_rate,1)],['PF',r?.profit_factor>=999?'∞':(r?.profit_factor!=null?r.profit_factor.toFixed(2):'—')],
    ['Maks DD',fmtPct(r?.max_dd,1)]
  ];
  document.getElementById('kpis').innerHTML=k.map(([l,v])=>{
    const neg=String(v).startsWith('-');
    return `<div class="kpi"><div class="v ${neg?'neg':(l==='Ort. net'||l==='2026 net'?'pos':'')}">${v}</div><div class="l">${l}</div></div>`;
  }).join('');
}
function renderRule(r){
  const s=specByIdx(state.idx)||{};
  document.getElementById('ruleMeta').textContent=`${s.batch||''} · ${s.tf||''} · ${s.family||''} · ${s.confidence||''}`;
  document.getElementById('ruleBox').textContent=(s.rule_long?`LONG\n${s.rule_long}\n\n`:'')+(s.rule_short?`SHORT\n${s.rule_short}\n\n`:'')+(r?`Filtre: ${filterLabel(r.filter_key)} · ${fmtNum(r.n)} işlem`:'');
}

function dailyAccount(r){return r.daily.map(x=>[x[0],x[1],x[2]/DATA.meta.alloc_n,x[3]/DATA.meta.alloc_n,x[4]/DATA.meta.alloc_n]);}
function dailySlice(r,from=null,to=null){let d=r.daily;if(from!=null)d=d.filter(x=>x[0]>=from);if(to!=null)d=d.filter(x=>x[0]<=to);return d;}
function dateLabels(d){return d.map(x=>dayStr(x[0]));}
function barPnlOption(d, title){
  if(!d.length)return emptyOpt('Bu dönemde işlem yok');
  const dates=dateLabels(d), pos=d.map(x=>x[2]), neg=d.map(x=>x[3]);
  return {
    textStyle:baseText(),
    grid:grid(52),
    tooltip:tooltip({formatter:p=>{const i=p[0].dataIndex,x=d[i];return `${dates[i]}<br/>Kâr: ${fmtPct(x[2],3)}<br/>Zarar: ${fmtPct(x[3],3)}<br/>Net: ${fmtPct(x[4],3)}<br/>İşlem: ${x[1]}`}}),
    xAxis:axisCat(dates,{axisLabel:{color:PAL.dim,fontSize:8,formatter:v=>v.slice(2,7)}}),
    yAxis:axisVal({axisLabel:{color:PAL.dim,fontSize:8,formatter:v=>fmtPct(v,1)}}),
    dataZoom:[{type:'inside'},{type:'slider',height:12,bottom:2,borderColor:PAL.line,fillerColor:'rgba(108,170,255,.12)',textStyle:{color:PAL.dim,fontSize:8}}],
    series:[
      {name:'Kâr',type:'bar',data:pos,barGap:'-100%',barWidth:'68%',itemStyle:{color:PAL.green,borderRadius:[2,2,0,0]}},
      {name:'Zarar',type:'bar',data:neg,barGap:'-100%',barWidth:'68%',itemStyle:{color:PAL.red,borderRadius:[0,0,2,2]}}
    ]
  };
}
function countOption(d){
  if(!d.length)return emptyOpt('Bu dönemde işlem yok');
  const dates=dateLabels(d);
  return {textStyle:baseText(),grid:grid(43),tooltip:tooltip(),xAxis:axisCat(dates,{axisLabel:{color:PAL.dim,fontSize:8,formatter:v=>v.slice(2,7)}}),
    yAxis:axisVal(),dataZoom:[{type:'inside'}],
    series:[{name:'İşlem',type:'bar',data:d.map(x=>x[1]),barWidth:'62%',itemStyle:{color:PAL.accent,opacity:.75,borderRadius:[2,2,0,0]}}]};
}
function cashOption(d, fromLabel){
  if(!d.length)return emptyOpt('Bu dönemde işlem yok');
  let cash=0; const pts=[];
  pts.push([dayDate(d[0][0]-1),0]);
  d.forEach(x=>{cash += x[4]*10; pts.push([dayDate(x[0]),cash]);});
  return {textStyle:baseText(),grid:grid(58),tooltip:{trigger:'axis',backgroundColor:'#101d2b',borderColor:PAL.line,textStyle:{color:PAL.text,fontFamily:'JetBrains Mono',fontSize:10},formatter:p=>`${p[0].axisValueLabel||''}<br/>Kasa: $${p[0].value[1].toFixed(2)}`},
    xAxis:{type:'time',axisLine:{lineStyle:{color:PAL.line}},axisLabel:{color:PAL.dim,fontSize:8}},
    yAxis:axisVal({axisLabel:{color:PAL.dim,fontSize:8,formatter:v=>'$'+Number(v).toFixed(0)}}),
    series:[{name:'Kasa',type:'line',data:pts,showSymbol:false,lineStyle:{color:PAL.accent,width:2},areaStyle:{color:new echarts.graphic.LinearGradient(0,0,0,1,[{offset:0,color:'rgba(108,170,255,.28)'},{offset:1,color:'rgba(108,170,255,.01)'}])}}]};
}
function equityOption(d){
  if(!d.length)return emptyOpt('Bu dönemde işlem yok');
  let eq=1;const pts=[[dayDate(d[0][0]-1),1]];
  d.forEach(x=>{eq*=1+x[4]/DATA.meta.alloc_n;pts.push([dayDate(x[0]),eq]);});
  return {textStyle:baseText(),grid:grid(54),tooltip:{trigger:'axis',backgroundColor:'#101d2b',borderColor:PAL.line,textStyle:{color:PAL.text,fontFamily:'JetBrains Mono',fontSize:10},formatter:p=>`${p[0].axisValueLabel||''}<br/>Equity: ${p[0].value[1].toFixed(4)}x`},
    xAxis:{type:'time',axisLine:{lineStyle:{color:PAL.line}},axisLabel:{color:PAL.dim,fontSize:8}},
    yAxis:axisVal({axisLabel:{color:PAL.dim,fontSize:8,formatter:v=>Number(v).toFixed(2)+'x'}}),
    series:[{name:'Equity',type:'line',data:pts,showSymbol:false,lineStyle:{color:PAL.purple,width:2},areaStyle:{color:'rgba(196,181,253,.08)'}}]};
}
function aggregateBy(d, fn){
  const m=new Map();
  d.forEach(x=>{const k=fn(dayDate(x[0]));if(!m.has(k))m.set(k,[0,0,0,0]);const a=m.get(k);a[0]+=x[1];a[1]+=x[2];a[2]+=x[3];a[3]+=x[4];});
  return m;
}
function divergingOption(d, fn, order, title){
  const m=aggregateBy(d,fn);
  const cats=order.filter(k=>m.has(k)); if(!cats.length)return emptyOpt('Veri yok');
  const pos=cats.map(k=>m.get(k)[1]),neg=cats.map(k=>m.get(k)[2]);
  return {textStyle:baseText(),grid:grid(46),tooltip:tooltip({formatter:p=>{const i=p[0].dataIndex,a=m.get(cats[i]);return `${cats[i]}<br/>Kâr: ${fmtPct(a[1],2)}<br/>Zarar: ${fmtPct(a[2],2)}<br/>Net: ${fmtPct(a[3],2)}<br/>İşlem: ${a[0]}`}}),
    xAxis:axisCat(cats,{axisLabel:{color:PAL.dim,fontSize:9,rotate:0}}),yAxis:axisVal({axisLabel:{color:PAL.dim,fontSize:8,formatter:v=>fmtPct(v,1)}}),
    series:[{name:'Kâr',type:'bar',data:pos,barGap:'-100%',barWidth:'56%',itemStyle:{color:PAL.green,borderRadius:[2,2,0,0]}},{name:'Zarar',type:'bar',data:neg,barGap:'-100%',barWidth:'56%',itemStyle:{color:PAL.red,borderRadius:[0,0,2,2]}}]};
}
function yearlyOption(d){return divergingOption(d,x=>String(x.getUTCFullYear()),['2022','2023','2024','2025','2026'],'Yıllık');}
function seasonOption(d){const order=['İlkbahar','Yaz','Sonbahar','Kış'];const fn=x=>{const m=x.getUTCMonth()+1;return m<=2?'Kış':m<=5?'İlkbahar':m<=8?'Yaz':'Sonbahar';};return divergingOption(d,fn,order,'Mevsim');}
function quarterOption(d){return divergingOption(d,x=>'Q'+(Math.floor(x.getUTCMonth()/3)+1),['Q1','Q2','Q3','Q4'],'Çeyrek');}
function weekdayOption(d){const order=['Pzt','Sal','Çar','Per','Cum','Cmt','Paz'];const fn=x=>{const w=x.getUTCDay();return order[(w+6)%7];};return divergingOption(d,fn,order,'Hafta');}
function monthHeatOption(d){
  if(!d.length)return emptyOpt('Veri yok');
  const m=new Map();
  d.forEach(x=>{const dt=dayDate(x[0]);const y=dt.getUTCFullYear(),mo=dt.getUTCMonth()+1;const k=`${y}-${mo}`;m.set(k,(m.get(k)||0)+x[4]);});
  const years=[...new Set([...m.keys()].map(k=>+k.split('-')[0]))].sort();
  const data=[];let mx=0;
  years.forEach((y,yi)=>{for(let mo=1;mo<=12;mo++){const v=m.get(`${y}-${mo}`)||0;mx=Math.max(mx,Math.abs(v));data.push([mo-1,yi,v]);}});
  return {textStyle:baseText(),grid:{left:44,right:12,top:12,bottom:26,containLabel:true},tooltip:{position:'top',backgroundColor:'#101d2b',borderColor:PAL.line,textStyle:{color:PAL.text,fontSize:10},formatter:p=>`${years[p.value[1]]}-${String(p.value[0]+1).padStart(2,'0')}<br/>${fmtPct(p.value[2],2)}`},
    xAxis:{type:'category',data:['Oca','Şub','Mar','Nis','May','Haz','Tem','Ağu','Eyl','Eki','Kas','Ara'],axisLabel:{color:PAL.dim,fontSize:8},axisLine:{lineStyle:{color:PAL.line}}},
    yAxis:{type:'category',data:years.map(String),axisLabel:{color:PAL.dim,fontSize:8},axisLine:{lineStyle:{color:PAL.line}}},
    visualMap:{min:-Math.max(mx,.0001),max:Math.max(mx,.0001),calculable:false,orient:'horizontal',left:'center',bottom:0,itemWidth:8,itemHeight:70,textStyle:{color:PAL.dim,fontSize:8},inRange:{color:['#ff6f7d','#142334','#46d49a']}},
    series:[{type:'heatmap',data:data,itemStyle:{borderColor:'#101d2b',borderWidth:1},emphasis:{itemStyle:{shadowBlur:8,shadowColor:'rgba(0,0,0,.5)'}}}]};
}
function holdOption(r){
  const is8=!!(r.hold8&&r.hold8.length);const h=(is8?r.hold8:r.hold_hist)||[];if(!h.length)return emptyOpt('Veri yok');
  const labels=(is8?(DATA.meta.hold_labels_v2||DATA.meta.hold_labels):DATA.meta.hold_labels||[]).slice(0,h.length);
  return {textStyle:baseText(),grid:grid(40),tooltip:tooltip({formatter:p=>{const i=p[0].dataIndex,a=h[i];return `${labels[i]}<br/>İşlem: ${a[0]}<br/>Kâr: ${fmtPct(a[1],2)}<br/>Zarar: ${fmtPct(a[2],2)}<br/>Net: ${fmtPct(a[3],2)}`}}),
    xAxis:axisCat(labels,{axisLabel:{color:PAL.dim,fontSize:8,rotate:24}}),yAxis:axisVal(),
    series:[{type:'bar',data:h.map(x=>x[0]),barWidth:'62%',itemStyle:{color:PAL.amber,borderRadius:[2,2,0,0]}}]};
}
function periodStats(r, is2026){
  if(!r) return null;
  if(is2026){
    const y=r.y2026||{};
    if(y.n) return {n:y.n, wins:y.wins, losses:y.losses, flat:y.flat,
      avg:r.ret_2026, hold:y.avg_hold_days, gross:y.pos||0, loss:y.neg||0, net:y.net||0};
    const d=dailySlice(r,FROM2026,TO2026);
    const n=d.reduce((a,x)=>a+x[1],0);
    const gross=d.reduce((a,x)=>a+x[2],0), loss=d.reduce((a,x)=>a+x[3],0), net=d.reduce((a,x)=>a+x[4],0);
    return {n, wins:null, losses:null, flat:null, avg:r.ret_2026, hold:null, gross, loss, net};
  }
  const n=r.n||0;
  const wins=(r.wins_total!=null&&r.wins_total>0)?r.wins_total:Math.round((r.win_rate||0)*n);
  return {n, wins, losses:r.losses_total??Math.max(0,n-wins), flat:r.flat_total??0,
    avg:r.avg_net, hold:r.avg_hold_days, gross:r.pos_sum||0, loss:r.neg_sum||0, net:r.total_net||0};
}
function renderPeriodMetrics(r){
  const all=periodStats(r,false), y=periodStats(r,true);
  const box=(id,s,metaId,label)=>{
    const el=document.getElementById(id); if(!s||!s.n){el.innerHTML='<div class="empty">Bu dönemde işlem yok.</div>';return;}
    const cells=[
      ['İşlem',fmtNum(s.n)],['Kârlı',s.wins==null?'—':fmtNum(s.wins)],
      ['Zararlı / başabaş',s.wins==null?'—':fmtNum((s.losses||0)+(s.flat||0))],
      ['Ort. net',fmtPct(s.avg,3)],['Ort. kalma',s.hold==null?'—':`${s.hold.toFixed(2)}g`],
      ['Brüt kâr (toplam)',fmtPct(s.gross,1)],['Brüt zarar (toplam)',fmtPct(s.loss,1)],['Net (toplam)',fmtPct(s.net,1)]
    ];
    el.innerHTML=cells.map(([l,v])=>`<div class="pm"><div class="v ${String(v).startsWith('-')?'neg':(l==='Kârlı'||l==='Ort. net'||l==='Net'?'pos':'')}">${v}</div><div class="l">${l}</div></div>`).join('');
    const m=document.getElementById(metaId); if(m) m.textContent=`${fmtNum(s.n)} işlem · ${label}`;
  };
  box('allMetrics',all,'allPeriodMeta','2022-08 → 2026-08');
  box('y26Metrics',y,'y26PeriodMeta','2026 takvimi');
}
function weeklyKey(day){const d=dayDate(day);const dow=(d.getUTCDay()+6)%7;return day-dow;}
function aggKeys(d, fn){
  const m=new Map();
  d.forEach(x=>{const k=fn(x[0]);if(!m.has(k))m.set(k,[0,0,0,0]);const a=m.get(k);a[0]+=x[1];a[1]+=x[2];a[2]+=x[3];a[3]+=x[4];});
  return m;
}
function barsFromMap(m, keys, labelFn){
  const cats=keys.filter(k=>m.has(k)); if(!cats.length)return emptyOpt('Veri yok');
  const pos=cats.map(k=>m.get(k)[1]),neg=cats.map(k=>m.get(k)[2]);
  return {textStyle:baseText(),grid:grid(42),tooltip:tooltip({formatter:p=>{const i=p[0].dataIndex,a=m.get(cats[i]);return `${labelFn(cats[i])}<br/>Kâr: ${fmtPct(a[1],2)}<br/>Zarar: ${fmtPct(a[2],2)}<br/>Net: ${fmtPct(a[3],2)}<br/>İşlem: ${a[0]}`}}),
    xAxis:axisCat(cats.map(labelFn),{axisLabel:{color:PAL.dim,fontSize:8,rotate:24}}),yAxis:axisVal({axisLabel:{color:PAL.dim,fontSize:8,formatter:v=>fmtPct(v,1)}}),
    series:[{type:'bar',data:pos,barGap:'-100%',barWidth:'62%',itemStyle:{color:PAL.green}},{type:'bar',data:neg,barGap:'-100%',barWidth:'62%',itemStyle:{color:PAL.red}}]};
}
function weeklyOption(d){
  if(!d.length)return emptyOpt('Veri yok');
  const m=aggKeys(d,weeklyKey);const keys=[...m.keys()].sort((a,b)=>a-b);
  return barsFromMap(m,keys,k=>dayStr(k).slice(2,10));
}
function monthlyOption(d){
  if(!d.length)return emptyOpt('Veri yok');
  const m=aggKeys(d,day=>{const x=dayDate(day);return Date.UTC(x.getUTCFullYear(),x.getUTCMonth(),1)/DAY;});
  const keys=[...m.keys()].sort((a,b)=>a-b);
  return barsFromMap(m,keys,k=>dayStr(k).slice(0,7));
}
function coinOption(r){
  const rows=(r.symbols_top||[]).slice().sort((a,b)=>b.net-a.net);
  if(!rows.length)return emptyOpt('Coin kırılımı hazırlanıyor');
  const cats=rows.map(x=>x.symbol), vals=rows.map(x=>x.net/DATA.meta.alloc_n);
  return {textStyle:baseText(),grid:{left:76,right:18,top:8,bottom:20,containLabel:true},tooltip:tooltip({formatter:p=>{const x=rows[p[0].dataIndex];return `${x.symbol}<br/>Net: ${fmtPct(x.net/DATA.meta.alloc_n,2)}<br/>İşlem: ${x.n}`}}),
    xAxis:axisVal({axisLabel:{color:PAL.dim,fontSize:8,formatter:v=>fmtPct(v,1)}}),yAxis:axisCat(cats,{axisLabel:{color:PAL.dim,fontSize:8}}),
    series:[{type:'bar',data:vals.map((v,i)=>({value:v,itemStyle:{color:v>=0?PAL.green:PAL.red}})),barHeight:'55%'}]};
}
function drawdownOption(d){
  if(!d.length)return emptyOpt('Veri yok');
  let eq=1,peak=1;const pts=[[dayDate(d[0][0]-1),0]];
  d.forEach(x=>{eq*=1+x[4]/DATA.meta.alloc_n;peak=Math.max(peak,eq);pts.push([dayDate(x[0]),(eq/peak-1)*100]);});
  return {textStyle:baseText(),grid:grid(52),tooltip:{trigger:'axis',backgroundColor:'#101d2b',borderColor:PAL.line,textStyle:{color:PAL.text,fontSize:10},formatter:p=>`${p[0].axisValueLabel||''}<br/>DD: ${Number(p[0].value[1]).toFixed(2)}%`},
    xAxis:{type:'time',axisLabel:{color:PAL.dim,fontSize:8},axisLine:{lineStyle:{color:PAL.line}}},yAxis:axisVal({axisLabel:{color:PAL.dim,fontSize:8,formatter:v=>v.toFixed(0)+'%'}}),
    series:[{type:'line',data:pts,showSymbol:false,lineStyle:{color:PAL.red,width:1.6},areaStyle:{color:'rgba(251,113,133,.18)'}}]};
}
function rollingOption(d){
  if(!d.length)return emptyOpt('Veri yok');
  const net=d.map(x=>x[4]/DATA.meta.alloc_n);
  const roll=(w)=>net.map((_,i)=>net.slice(Math.max(0,i-w+1),i+1).reduce((a,b)=>a+b,0));
  const x=d.map(z=>dayDate(z[0]));
  const mk=(w,color)=>({name:`${w}g`,type:'line',showSymbol:false,data:x.map((xx,i)=>[xx,roll(w)[i]*100]),lineStyle:{color,width:1.7}});
  return {textStyle:baseText(),grid:grid(52),legend:{top:0,textStyle:{color:PAL.muted,fontSize:9}},
    tooltip:{trigger:'axis',backgroundColor:'#101d2b',borderColor:PAL.line,textStyle:{color:PAL.text,fontSize:10},valueFormatter:v=>Number(v).toFixed(2)+'%'},
    xAxis:{type:'time',axisLabel:{color:PAL.dim,fontSize:8},axisLine:{lineStyle:{color:PAL.line}}},yAxis:axisVal({axisLabel:{color:PAL.dim,fontSize:8,formatter:v=>Number(v).toFixed(0)+'%'}}),
    series:[mk(30,PAL.accent),mk(90,PAL.amber),mk(365,PAL.purple)]};
}
function filterHeatmapOption(){
  const specs=DATA.specs.slice().sort((a,b)=>(b.idx||0)-(a.idx||0)).slice(0,20);
  const filters=filterDefs().filter(f=>f.id!=='baseline');
  const data=[];let mx=0;
  specs.forEach((s,yi)=>filters.forEach((f,xi)=>{const r=resultFor(s.idx,f.id);const v=r?r.total_net/DATA.meta.alloc_n:0;mx=Math.max(mx,Math.abs(v));data.push([xi,yi,v]);}));
  if(!data.some(d=>d[2]!==0))return emptyOpt('Filtre verisi yok');
  return {textStyle:baseText(),grid:{left:62,right:12,top:8,bottom:65,containLabel:true},tooltip:{position:'top',backgroundColor:'#101d2b',borderColor:PAL.line,textStyle:{color:PAL.text,fontSize:10},formatter:p=>`${filters[p.value[0]].label_tr}<br/>${specs[p.value[1]].sid}: ${fmtPct(p.value[2],2)} (1/525 hesap)`},
    xAxis:{type:'category',data:filters.map(f=>f.label_tr),axisLabel:{color:PAL.dim,fontSize:7,rotate:45},axisLine:{lineStyle:{color:PAL.line}}},
    yAxis:{type:'category',data:specs.map(s=>s.sid),axisLabel:{color:PAL.dim,fontSize:8},axisLine:{lineStyle:{color:PAL.line}}},
    visualMap:{min:-Math.max(mx,.0001),max:Math.max(mx,.0001),orient:'horizontal',left:'center',bottom:0,itemWidth:8,itemHeight:60,textStyle:{color:PAL.dim,fontSize:8},inRange:{color:['#ff6f7d','#142334','#46d49a']}},
    series:[{type:'heatmap',data:data,itemStyle:{borderColor:'#101d2b',borderWidth:1}}]};
}
function renderFilterStats(){
  const el=document.getElementById('filterStats'); if(!el)return;
  el.innerHTML='<div class="tablewrap" style="max-height:300px"><table><thead><tr><th>Filtre</th><th class="num">Pozitif</th><th class="num">Kazanma</th><th class="num">Ort. net</th><th class="num">Med. sembol</th><th class="num">İşlem</th></tr></thead><tbody>'+
    DATA.filters.map(f=>{const rr=DATA.results.filter(r=>r.filter_key===f.id);const k=rr.filter(r=>r.kept);const n=rr.reduce((a,x)=>a+x.n,0);const wins=rr.reduce((a,x)=>a+(x.win_rate||0)*x.n,0);const avg=k.length?k.reduce((a,x)=>a+x.avg_net,0)/k.length:null;const med=k.length?k.reduce((a,x)=>a+x.median_symbol_net,0)/k.length:null;return `<tr><td>${esc(f.label_tr)}</td><td class="num">${k.length}/${rr.length}</td><td class="num">${fmtPct(n?wins/n:0,1)}</td><td class="num ${avg>=0?'pos':'neg'}">${fmtPct(avg,2)}</td><td class="num ${med>=0?'pos':'neg'}">${fmtPct(med,2)}</td><td class="num">${fmtNum(n)}</td></tr>`;}).join('')+
    '</tbody></table></div>';
}
function holdPnlOption(r){
  const is8=!!(r.hold8&&r.hold8.length);const h=(is8?r.hold8:r.hold_hist)||[];if(!h.length)return emptyOpt('Veri yok');
  const labels=(is8?(DATA.meta.hold_labels_v2||DATA.meta.hold_labels):DATA.meta.hold_labels||[]).slice(0,h.length);
  return {textStyle:baseText(),grid:grid(42),tooltip:tooltip({formatter:p=>{const i=p[0].dataIndex,a=h[i];return `${labels[i]}<br/>Kâr: ${fmtPct(a[1],2)}<br/>Zarar: ${fmtPct(a[2],2)}<br/>Net: ${fmtPct(a[3],2)}`}}),
    xAxis:axisCat(labels,{axisLabel:{color:PAL.dim,fontSize:8,rotate:24}}),yAxis:axisVal({axisLabel:{color:PAL.dim,fontSize:8,formatter:v=>fmtPct(v,1)}}),
    series:[{name:'Kâr',type:'bar',data:h.map(x=>x[1]),barGap:'-100%',barWidth:'58%',itemStyle:{color:PAL.green}},{name:'Zarar',type:'bar',data:h.map(x=>x[2]),barGap:'-100%',barWidth:'58%',itemStyle:{color:PAL.red}}]};
}
function longShortOption(r){
  const L=r.long||[0,0,0,0,0],S=r.short||[0,0,0,0,0];
  const vals=[L[1]/DATA.meta.alloc_n,S[1]/DATA.meta.alloc_n];
  return {textStyle:baseText(),grid:grid(48),tooltip:tooltip({formatter:p=>{const a=[L,S][p[0].dataIndex];return `${p[0].name}<br/>İşlem: ${a[0]}<br/>Toplam: ${fmtPct(a[1]/DATA.meta.alloc_n,2)}<br/>Kazanma: ${fmtPct(a[0]?a[4]/a[0]:0,1)}`}}),
    xAxis:axisCat(['Long','Short']),yAxis:axisVal({axisLabel:{color:PAL.dim,fontSize:8,formatter:v=>fmtPct(v,1)}}),
    series:[{type:'bar',data:vals.map((v,i)=>({value:v,itemStyle:{color:i===0?PAL.green:PAL.red}})),barWidth:'42%'}]};
}
function scatterOption(r){
  const pts=r.scatter||[];if(!pts.length)return emptyOpt('Veri yok');
  const data=pts.map(p=>[Math.min(p[0],95),p[1]*100]);
  return {textStyle:baseText(),grid:grid(52),tooltip:{trigger:'item',backgroundColor:'#101d2b',borderColor:PAL.line,textStyle:{color:PAL.text,fontSize:10},formatter:p=>`Kalma: ${p.value[0].toFixed(1)} gün<br/>Getiri: ${p.value[1].toFixed(2)}%`},
    xAxis:axisVal({name:'gün',nameTextStyle:{color:PAL.dim,fontSize:9},axisLabel:{color:PAL.dim,fontSize:8}}),yAxis:axisVal({axisLabel:{color:PAL.dim,fontSize:8,formatter:v=>v.toFixed(0)+'%'}}),
    series:[{type:'scatter',data:data,symbolSize:4,itemStyle:{color:p=>p.value[1]>=0?'rgba(52,211,153,.55)':'rgba(251,113,133,.55)'},emphasis:{itemStyle:{color:PAL.accent}}}]};
}
function filterImpactOption(metric){
  const rows=filterDefs().map(f=>({f,r:resultFor(state.idx,f.id)})).filter(x=>x.r);
  const cats=rows.map(x=>x.f.label_tr), data=rows.map(x=>x.r[metric]);
  return {textStyle:baseText(),grid:grid(100),tooltip:tooltip({formatter:p=>{const x=rows[p[0].dataIndex].r;return `${cats[p[0].dataIndex]}<br/>${metric==='avg_net'?'Ort. net':'Med. sembol'}: ${fmtPct(x[metric],3)}<br/>İşlem: ${x.n}`}}),
    xAxis:axisVal({axisLabel:{color:PAL.dim,fontSize:8,formatter:v=>fmtPct(v,2)}}),yAxis:axisCat(cats,{axisLabel:{color:PAL.dim,fontSize:8,width:92,overflow:'truncate'}}),
    series:[{type:'bar',data:data.map((v,i)=>({value:v,itemStyle:{color:rows[i].f.id==='baseline'?PAL.amber:(v>=0?PAL.green:PAL.red)}})),barWidth:'60%',label:{show:true,position:'right',color:PAL.muted,fontSize:8,formatter:p=>fmtPct(p.value,2)}}]};
}
function renderCharts(r){
  if(!r)return;
  const d=r.daily||[];
  const da=dailyAccount(r);
  const d26=dailySlice(r,FROM2026,TO2026);
  const da26=d26.map(x=>[x[0],x[1],x[2]/DATA.meta.alloc_n,x[3]/DATA.meta.alloc_n,x[4]/DATA.meta.alloc_n]);
  renderPeriodMetrics(r);

  setChart('allDaily',barPnlOption(da));
  setChart('allCount',countOption(d));
  setChart('allWeekly',weeklyOption(da));
  setChart('allMonthly',monthlyOption(da));
  setChart('allSeason',seasonOption(da));
  setChart('allCash',cashOption(d));
  setChart('allCoins',coinOption(r));

  setChart('y26Daily',barPnlOption(da26));
  setChart('y26Count',countOption(d26));
  setChart('y26Weekly',weeklyOption(da26));
  setChart('y26Monthly',monthlyOption(da26));
  setChart('y26Season',seasonOption(da26));
  setChart('y26Cash',cashOption(d26));

  setChart('equity',equityOption(d));
  setChart('drawdown',drawdownOption(d));
  setChart('rolling',rollingOption(d));
  setChart('yearly',yearlyOption(da));
  setChart('seasonal',seasonOption(da));
  setChart('quarterly',quarterOption(da));
  setChart('monthHeat',monthHeatOption(da));
  setChart('weekday',weekdayOption(da));
  setChart('hold',holdOption(r));
  setChart('holdPnl',holdPnlOption(r));
  setChart('longShort',longShortOption(r));
  setChart('scatter',scatterOption(r));
  setChart('filterAvg',filterImpactOption('avg_net'));
  setChart('filterMedian',filterImpactOption('median_symbol_net'));
  setChart('filterHeatmap',filterHeatmapOption());
  renderFilterStats();
}
const scanState={sort:'_score',dir:-1};
function computeScores(){
  if(DATA.meta._scored)return;
  const rs=DATA.results;
  const p2=rs.map(r=>r.n?r.total_net/r.n:null);
  const p4=rs.map(r=>r.win_hold_h==null?null:r.win_hold_h);
  const p5=rs.map(r=>r.losses_total?(r.wins_total||0)/r.losses_total:null);
  const mm=(arr)=>{
    const v=arr.filter(x=>x!=null&&isFinite(x));
    return v.length?{min:Math.min(...v),max:Math.max(...v)}:{min:0,max:0};
  };
  const m2=mm(p2),m4=mm(p4),m5=mm(p5);
  const sc=(x,m,inv)=>{
    if(x==null||!isFinite(x))return 0;
    if(m.max===m.min)return 16.65;
    const t=(x-m.min)/(m.max-m.min);
    return 33.3*(inv?1-t:t);
  };
  rs.forEach((r,i)=>{
    r._p2=sc(p2[i],m2,false);
    r._p4=sc(p4[i],m4,true);
    r._p5=sc(p5[i],m5,false);
    r._score=r._p2+r._p4+r._p5;
    r._ratio=r.losses_total?(r.wins_total||0)/r.losses_total:null;
    r._avg26=(r.y2026&&r.y2026.n)?r.y2026.net/r.y2026.n:null;
  });
  DATA.meta._scored=1;
  DATA.meta._scoreRange={p2:m2,p4:m4,p5:m5};
}
const scanFilters={};
function scanFilterActive(c){
  const f=scanFilters[c.k];
  if(!f)return false;
  return c.kind==='text'?f.size>0:(f.min!=null||f.max!=null);
}
function scanFilterCount(){return scanCols.filter(scanFilterActive).length;}
function passesScanFilters(r){
  for(const c of scanCols){
    if(!scanFilterActive(c))continue;
    const f=scanFilters[c.k];
    if(c.kind==='text'){
      if(!f.has(String(r[c.k]??'')))return false;
    }else{
      const v=c.get(r);
      if(v==null||!isFinite(v))return false;
      if(f.min!=null&&v<f.min)return false;
      if(f.max!=null&&v>f.max)return false;
    }
  }
  return true;
}
function scanRows(){
  const q=(document.getElementById('scanSearch').value||'').toLowerCase();
  const minN=+document.getElementById('scanMinN').value||0;
  const pos=document.getElementById('scanPositive').checked;
  const base=document.getElementById('scanBase').checked;
  const rows=DATA.results.filter(r=>{
    if(!base&&r.filter_key==='baseline')return false;
    if(pos&&!r.kept)return false;
    if(r.n<minN)return false;
    if(q&&!(`${r.sid} ${r.title} ${r.tf} ${r.family} ${r.filter_key} ${r.filter_label_tr}`.toLowerCase().includes(q)))return false;
    return passesScanFilters(r);
  });
  const k=scanState.sort,dir=scanState.dir;
  rows.sort((a,b)=>{
    let av=a[k],bv=b[k];
    if(typeof av==='string'||typeof bv==='string'){
      av=(av==null?'':String(av)).toLowerCase();bv=(bv==null?'':String(bv)).toLowerCase();
      if(av===bv)return b.n-a.n;
      return (av>bv?1:-1)*dir;
    }
    if(av==null&&bv==null)return b.n-a.n;
    if(av==null)return 1;
    if(bv==null)return -1;
    if(av===bv)return b.n-a.n;
    return (av>bv?1:-1)*dir;
  });
  return rows;
}
const scanCols=[
  {k:'sid',label:'Strateji',kind:'text'},
  {k:'tf',label:'TF',kind:'text'},
  {k:'filter_label_tr',label:'Filtre',kind:'text'},
  {k:'n',label:'İşlem',kind:'num',step:10,get:r=>r.n,fmt:v=>fmtNum(v)},
  {k:'avg_net',label:'Net/işlem (tüm)',kind:'num',step:.1,unit:'%',get:r=>r.avg_net*100,fmt:v=>v.toFixed(2)+'%'},
  {k:'_avg26',label:'Net/işlem 2026',kind:'num',step:.1,unit:'%',get:r=>r._avg26==null?null:r._avg26*100,fmt:v=>v.toFixed(2)+'%'},
  {k:'win_hold_h',label:'Kârlı ort. süre (sa)',kind:'num',step:1,unit:'sa',get:r=>r.win_hold_h,fmt:v=>v.toFixed(1)+' sa'},
  {k:'_ratio',label:'Kârlı / zararlı',kind:'num',step:.05,get:r=>r._ratio,fmt:v=>v.toFixed(2)},
  {k:'_score',label:'Puan',kind:'num',step:1,unit:'puan',get:r=>r._score,fmt:v=>v.toFixed(1)},
  {k:'total_net',label:'Toplam net',kind:'num',step:1,unit:'%',get:r=>r.total_net*100,fmt:v=>v.toFixed(1)+'%'}
];
let cmKey=null;
function closeColMenu(){
  const m=document.getElementById('colMenu');
  if(m){m.style.display='none';m.innerHTML='';}
  cmKey=null;
}
function openColMenu(k,anchor){
  const col=scanCols.find(c=>c.k===k);if(!col)return;
  const m=document.getElementById('colMenu');
  if(cmKey===k&&m.style.display==='block'){closeColMenu();return;}
  cmKey=k;
  const f=scanFilters[k];
  let html=`<div class="cm-head">${esc(col.label)}<span class="cm-sub">${col.kind==='text'?'değer seç':'aralık'}</span></div>
    <div class="cm-sort"><button data-dir="asc">↑ Artan</button><button data-dir="desc">↓ Azalan</button></div>`;
  if(col.kind==='text'){
    const vals=Array.from(new Set(DATA.results.map(r=>String(r[k]??'')))).sort((a,b)=>a.localeCompare(b,'tr'));
    const counts=new Map();
    DATA.results.forEach(r=>{const v=String(r[k]??'');counts.set(v,(counts.get(v)||0)+1);});
    const sel=f?new Set(vals.filter(v=>f.has(v))):new Set(vals);
    html+=`<input type="text" id="cmSearch" placeholder="Ara…" autocomplete="off">
      <label class="cm-all"><input type="checkbox" id="cmAll"> Tümünü seç</label>
      <div class="cm-list" id="cmList"></div>
      <div class="cm-actions"><button id="cmApply">Uygula</button><button id="cmClear">Temizle</button></div>`;
    m.innerHTML=html;
    const list=m.querySelector('#cmList');
    const allBox=m.querySelector('#cmAll');
    const paint=(q='')=>{
      const shown=vals.filter(v=>!q||v.toLowerCase().includes(q));
      list.innerHTML=shown.map(v=>`<label class="cm-item"><input type="checkbox" data-v="${esc(v)}" ${sel.has(v)?'checked':''}><span>${esc(v)||'(boş)'}</span><b>${fmtNum(counts.get(v)||0)}</b></label>`).join('')||'<div class="cm-none">Eşleşme yok</div>';
      allBox.checked=vals.every(v=>sel.has(v));
    };
    paint();
    m.querySelector('#cmSearch').addEventListener('input',e=>paint(e.target.value.toLowerCase()));
    allBox.addEventListener('change',()=>{vals.forEach(v=>allBox.checked?sel.add(v):sel.delete(v));paint(m.querySelector('#cmSearch').value.toLowerCase());});
    list.addEventListener('change',e=>{
      const cb=e.target.closest('input[data-v]');if(!cb)return;
      const v=cb.dataset.v;cb.checked?sel.add(v):sel.delete(v);
      allBox.checked=vals.every(x=>sel.has(x));
    });
    m.querySelector('#cmApply').addEventListener('click',()=>{
      if(sel.size===0||sel.size===vals.length)delete scanFilters[k];
      else scanFilters[k]={size:sel.size,has:v=>sel.has(v)};
      closeColMenu();renderScan();
    });
    m.querySelector('#cmClear').addEventListener('click',()=>{
      delete scanFilters[k];closeColMenu();renderScan();
    });
  }else{
    const all=DATA.results.map(col.get).filter(v=>v!=null&&isFinite(v));
    const lo=Math.min(...all),hi=Math.max(...all);
    html+=`<div class="cm-row"><label>En az</label><input type="number" id="cmMin" step="${col.step||'any'}" value="${f&&f.min!=null?f.min:''}" placeholder="${col.fmt(lo)}"></div>
      <div class="cm-row"><label>En çok</label><input type="number" id="cmMax" step="${col.step||'any'}" value="${f&&f.max!=null?f.max:''}" placeholder="${col.fmt(hi)}"></div>
      <div class="cm-note">Veri aralığı: ${col.fmt(lo)} – ${col.fmt(hi)}${col.unit?' ('+col.unit+')':''}</div>
      <div class="cm-actions"><button id="cmApply">Uygula</button><button id="cmClear">Temizle</button></div>`;
    m.innerHTML=html;
    const apply=()=>{
      const mn=m.querySelector('#cmMin').value,max=m.querySelector('#cmMax').value;
      let min=mn===''?null:+mn,maxv=max===''?null:+max;
      if(min!=null&&!isFinite(min))min=null;
      if(maxv!=null&&!isFinite(maxv))maxv=null;
      if(min==null&&maxv==null)delete scanFilters[k];
      else scanFilters[k]={min,max:maxv};
      closeColMenu();renderScan();
    };
    m.querySelector('#cmApply').addEventListener('click',apply);
    m.querySelectorAll('#cmMin,#cmMax').forEach(inp=>inp.addEventListener('keydown',e=>{if(e.key==='Enter')apply();}));
    m.querySelector('#cmClear').addEventListener('click',()=>{delete scanFilters[k];closeColMenu();renderScan();});
  }
  m.style.display='block';
  const r=anchor.getBoundingClientRect();
  const w=m.offsetWidth,h=m.offsetHeight;
  m.style.left=Math.max(8,Math.min(r.left,r.right-w,window.innerWidth-w-10))+'px';
  let top=r.bottom+6;
  if(top+h>window.innerHeight-8)top=Math.max(8,r.top-h-6);
  m.style.top=top+'px';
  m.querySelectorAll('.cm-sort button').forEach(btn=>btn.addEventListener('click',()=>{
    scanState.sort=k;scanState.dir=btn.dataset.dir==='asc'?1:-1;
    closeColMenu();renderScan();
  }));
}
function renderScan(){
  if(!DATA)return;
  computeScores();
  const rows=scanRows();
  const nf=scanFilterCount();
  document.getElementById('scanHint').textContent=`${fmtNum(rows.length)} / ${fmtNum(DATA.results.length)} kombinasyon${nf?` · ${nf} sütun filtresi`:''}`;
  const clearBtn=document.getElementById('scanClearCols');
  clearBtn.style.display=nf?'inline-block':'none';
  document.getElementById('scanColCount').textContent=nf;
  document.querySelector('#scanTable thead').innerHTML='<tr>'+scanCols.map(c=>{
    const cls=scanState.sort===c.k?(scanState.dir>0?'sortasc':'sortdesc'):'';
    const num=c.kind==='text'?'':'num';
    const act=scanFilterActive(c)?'filtered':'';
    return `<th data-k="${c.k}" class="${num} ${cls} ${act}"><span class="thwrap"><span>${c.label}</span><button class="fcaret" data-k="${c.k}" title="Filtrele">▾</button></span></th>`;
  }).join('')+'</tr>';
  document.querySelector('#scanTable tbody').innerHTML=rows.map(r=>{
    const sc=r._score||0;
    const scc=sc>=66?'var(--green)':sc>=40?'var(--amber)':'var(--red)';
    const ratio=r._ratio==null?'—':`${r.wins_total} / ${r.losses_total} - ${r._ratio.toFixed(2)}`;
    return `<tr class="rowline" data-idx="${r.idx}" data-f="${esc(r.filter_key)}" title="${esc(r.sid+' · '+r.title)}">
      <td><b>${esc(r.sid)}</b><div class="mini">${esc(r.family||'')}</div></td>
      <td><span class="badge">${esc(r.tf)}</span></td>
      <td>${esc(r.filter_label_tr)}</td>
      <td class="num">${fmtNum(r.n)}</td>
      <td class="num ${r.avg_net>=0?'pos':'neg'}">${fmtPct(r.avg_net,3)}</td>
      <td class="num ${r._avg26==null?'':(r._avg26>=0?'pos':'neg')}">${r._avg26==null?'—':fmtPct(r._avg26,3)}</td>
      <td class="num">${r.win_hold_h==null?'—':r.win_hold_h.toFixed(1)+' sa'}</td>
      <td class="num">${ratio}</td>
      <td class="num" title="P2 ${r._p2.toFixed(1)} · P4 ${r._p4.toFixed(1)} · P5 ${r._p5.toFixed(1)}"><b>${sc.toFixed(1)}</b><div class="scorebar"><i style="width:${Math.max(0,Math.min(100,sc))}%;background:${scc}"></i></div></td>
      <td class="num ${r.total_net>=0?'pos':'neg'}">${fmtPct(r.total_net,1)}</td></tr>`;
  }).join('');
  document.querySelectorAll('#scanTable tbody tr').forEach(tr=>tr.addEventListener('click',()=>{
    state.idx=+tr.dataset.idx;state.filter=tr.dataset.f;
    const sp=specByIdx(state.idx);if(sp){state.tf=sp.tf;document.getElementById('tfFilter').value=sp.tf;}
    buildStrategyOptions();
    activateTab('overview');
  }));
  document.querySelectorAll('#scanTable th').forEach(th=>th.addEventListener('click',()=>{
    const k=th.dataset.k;if(!k)return;
    scanState.dir=scanState.sort===k?-scanState.dir:-1;
    scanState.sort=k;renderScan();
  }));
  document.querySelectorAll('#scanTable .fcaret').forEach(btn=>btn.addEventListener('click',e=>{
    e.stopPropagation();openColMenu(btn.dataset.k,btn);
  }));
}
function activateTab(name){
  closeColMenu();
  document.querySelectorAll('.tabbtn').forEach(b=>b.classList.toggle('active',b.dataset.tab===name));
  document.getElementById('tab-overview').hidden=name!=='overview';
  document.getElementById('tab-scan').hidden=name!=='scan';
  if(name==='overview'){
    requestAnimationFrame(()=>Object.values(charts).forEach(c=>{try{c.resize();}catch(e){}}));
  }else{
    renderScan();
  }
}
function renderAll(){
  if(!DATA)return;
  const r=selectedResult();
  syncSwitch();renderFilterList();renderHeader(r);renderKpis(r);renderDayKpis(r);renderCharts(r);renderRule(r);
}
function init(){
  document.getElementById('loading').style.display='none';
  initSelectors();
  buildStrategyOptions();
  const best=DATA.results.filter(r=>r.kept&&r.n>=50&&r.median_symbol_net>0).sort((a,b)=>b.median_symbol_net-a.median_symbol_net)[0]
    ||DATA.results.filter(r=>r.kept).sort((a,b)=>b.median_symbol_net-a.median_symbol_net)[0]||DATA.results[0];
  state.idx=best.idx;state.filter=best.filter_key;state.tf=best.tf;
  document.getElementById('tfFilter').value=state.tf;
  buildStrategyOptions();
  document.getElementById('strategySel').value=String(state.idx);
  renderAll();
  computeScores();
  document.getElementById('scanTabCount').textContent=fmtNum(DATA.results.length);
}
document.querySelectorAll('.tabbtn').forEach(b=>b.addEventListener('click',()=>activateTab(b.dataset.tab)));
document.getElementById('scanClearCols').addEventListener('click',()=>{
  Object.keys(scanFilters).forEach(k=>delete scanFilters[k]);
  closeColMenu();renderScan();
});
document.addEventListener('click',e=>{
  if(e.target.closest('#colMenu')||e.target.closest('.fcaret'))return;
  closeColMenu();
});
document.addEventListener('keydown',e=>{if(e.key==='Escape')closeColMenu();});
window.addEventListener('scroll',e=>{
  if(e.target&&e.target.closest&&e.target.closest('#colMenu'))return;
  closeColMenu();
},true);
['scanSearch','scanMinN','scanPositive','scanBase'].forEach(id=>{
  const el=document.getElementById(id);
  const go=()=>{if(!document.getElementById('tab-scan').hidden)renderScan();};
  el.addEventListener('input',go);el.addEventListener('change',go);
});
fetch('dashboard_data.json').then(r=>r.json()).then(d=>{DATA=d;init();}).catch(e=>{
  document.getElementById('loading').textContent='dashboard_data.json yüklenemedi. Yerel sunucudan aç: http://127.0.0.1:8000/ · '+e;
});
window.addEventListener('resize',()=>Object.values(charts).forEach(c=>c.resize()));
</script>
</body>
</html>'''

out = os.path.join(ROOT, 'filter_dashboard.html')
open(out, 'w', encoding='utf-8').write(HTML)
print('wrote', out, len(HTML), 'bytes')
