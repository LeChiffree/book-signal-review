import os, json

BT = r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest'
ROOT = os.path.join(BT, 'filter_layer')
DATA = json.load(open(os.path.join(ROOT, 'dashboard_data.json'), encoding='utf-8'))

HTML = r'''<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Filtre Laboratuvarı · 525 sembol</title>
<style>
:root{
  --bg:#070c16; --panel:#0d1627; --panel2:#111e33; --line:#22314d;
  --text:#e9eff9; --muted:#8da2c0; --dim:#637795;
  --accent:#5eead4; --green:#34d399; --red:#fb7185; --amber:#fbbf24; --purple:#c4b5fd;
}
*{box-sizing:border-box}
html,body{margin:0;background:var(--bg);color:var(--text);font-family:ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;line-height:1.4}
body{background:
 radial-gradient(1100px 600px at 15% -10%, rgba(94,234,212,.11), transparent 55%),
 radial-gradient(900px 500px at 95% 0%, rgba(196,181,253,.09), transparent 55%),var(--bg)}
.app{display:grid;grid-template-columns:320px minmax(0,1fr);min-height:100vh}
aside{border-right:1px solid var(--line);background:rgba(9,15,27,.82);padding:18px 14px 40px;position:sticky;top:0;height:100vh;overflow:auto}
.brand{font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:var(--accent);font-weight:800}
h1{font-size:22px;line-height:1.08;margin:8px 0 4px;letter-spacing:-.02em}
.sub{font-size:11px;color:var(--dim);margin-bottom:14px}
.search{width:100%;background:#0a1322;border:1px solid var(--line);color:var(--text);border-radius:9px;padding:8px 10px;font:inherit;font-size:12px;margin-bottom:10px}
.filters{display:flex;flex-direction:column;gap:5px}
.fbtn{appearance:none;border:1px solid transparent;background:transparent;color:var(--muted);text-align:left;border-radius:9px;padding:7px 8px;cursor:pointer;font:inherit;font-size:11.5px;display:grid;grid-template-columns:1fr auto;gap:6px}
.fbtn:hover{background:rgba(255,255,255,.035);color:var(--text)}
.fbtn.active{background:rgba(94,234,212,.09);border-color:rgba(94,234,212,.35);color:var(--accent)}
.fbtn b{font-weight:700;color:var(--text)}
.fbtn small{color:var(--dim);font-size:10px;display:block;margin-top:1px}
.fcount{font-variant-numeric:tabular-nums;color:var(--dim);font-size:10px;align-self:center}
.sidehead{font-size:10px;text-transform:uppercase;letter-spacing:.12em;color:var(--dim);margin:14px 0 6px;font-weight:700}
.side-note{border-top:1px dashed var(--line);margin-top:14px;padding-top:10px;color:var(--dim);font-size:10px}
main{padding:22px 24px 50px;min-width:0}
.top{display:flex;justify-content:space-between;gap:18px;align-items:flex-end;flex-wrap:wrap;margin-bottom:14px}
.top h2{font-size:25px;margin:0;letter-spacing:-.02em}
.top p{color:var(--muted);font-size:12px;margin:5px 0 0;max-width:730px}
.select{background:#0a1322;border:1px solid var(--line);color:var(--text);border-radius:9px;padding:9px 10px;font:inherit;font-size:12px;min-width:300px}
.kpis{display:grid;grid-template-columns:repeat(7,minmax(0,1fr));gap:9px;margin:14px 0}
.kpi{background:linear-gradient(180deg,rgba(255,255,255,.04),rgba(255,255,255,.012));border:1px solid var(--line);border-radius:12px;padding:11px 12px}
.kpi .v{font-size:20px;font-weight:800;letter-spacing:-.02em;font-variant-numeric:tabular-nums}
.kpi .l{font-size:9px;text-transform:uppercase;letter-spacing:.12em;color:var(--dim);margin-top:2px}
.grid{display:grid;grid-template-columns:1.35fr .95fr;gap:12px}
.card{background:linear-gradient(180deg,rgba(255,255,255,.035),rgba(255,255,255,.01));border:1px solid var(--line);border-radius:15px;padding:14px 15px;min-width:0}
.card h3{font-size:13px;margin:0 0 3px}
.card .hint{font-size:10.5px;color:var(--dim);margin:0 0 8px}
.chart{width:100%;height:auto;display:block}
.wide{grid-column:1/-1}
.row{display:flex;gap:8px;align-items:center;flex-wrap:wrap}
.badge{display:inline-block;padding:2px 7px;border-radius:999px;font-size:10px;border:1px solid var(--line);color:var(--muted)}
.pos{color:var(--green)} .neg{color:var(--red)} .amber{color:var(--amber)}
table{width:100%;border-collapse:collapse;font-size:11px}
th,td{padding:6px 7px;border-bottom:1px solid rgba(34,49,77,.7);text-align:left;white-space:nowrap}
th{color:var(--dim);font-size:9px;text-transform:uppercase;letter-spacing:.09em;position:sticky;top:0;background:#0c1525;z-index:2;cursor:pointer}
tr.rowline{cursor:pointer} tr.rowline:hover{background:rgba(94,234,212,.05)}
tr.sel{background:rgba(94,234,212,.09)}
td.num,th.num{text-align:right;font-variant-numeric:tabular-nums}
.tablewrap{max-height:420px;overflow:auto;border:1px solid rgba(34,49,77,.5);border-radius:10px}
.toolbar{display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin:8px 0 10px}
.toolbar label{font-size:11px;color:var(--muted)}
.rule{font-family:ui-monospace,SFMono-Regular,Consolas,monospace;font-size:10.5px;color:#b8c7dd;background:#08111f;border:1px solid var(--line);border-radius:8px;padding:9px;white-space:pre-wrap;overflow:auto;max-height:140px}
.note{font-size:10.5px;color:var(--dim);border-top:1px dashed var(--line);padding-top:8px;margin-top:10px}
.empty{color:var(--dim);font-size:12px;padding:20px}
@media(max-width:1100px){.app{grid-template-columns:1fr}aside{position:relative;height:auto}.kpis{grid-template-columns:repeat(3,1fr)}.grid{grid-template-columns:1fr}.wide{grid-column:auto}}
</style>
</head>
<body>
<div class="app">
<aside>
  <div class="brand">Book Signal Review</div>
  <h1>Filtre Laboratuvarı</h1>
  <div class="sub">525 sembol · 14 rejim filtresi · 1m execution</div>
  <input class="search" id="strategySearch" placeholder="Strateji / SID ara…">
  <div class="sidehead">Filtreler</div>
  <div class="filters" id="filterList"></div>
  <div class="sidehead">Görünüm</div>
  <label class="fbtn" style="cursor:pointer"><span><b>Sadece pozitif</b><small>Ortalama işlem başı net &gt; 0</small></span><input type="checkbox" id="positiveOnly" checked style="width:auto"></label>
  <label class="fbtn" style="cursor:pointer"><span><b>Bazı göster</b><small>Filtresiz karşılaştırma</small></span><input type="checkbox" id="showBase" checked style="width:auto"></label>
  <div class="side-note">
    Her filtre tek tek uygulanır. Yeşil/kırmızı günlük bar, aynı günün pozitif ve negatif realized PnL'ini birlikte gösterir.
  </div>
</aside>
<main>
  <div class="top">
    <div>
      <h2 id="title">Strateji seç</h2>
      <p id="subtitle">Soldan filtre, sağdan strateji seç. Tüm sonuçlar fee, slippage ve funding dahildir.</p>
    </div>
    <select class="select" id="strategySel"></select>
  </div>
  <div class="kpis" id="kpis"></div>
  <div class="grid">
    <section class="card wide">
      <h3>Günlük realized PnL — aynı gün kâr ve zarar tek barda</h3>
      <p class="hint" id="dailyHint">Pozitif segment yeşil, negatif segment kırmızı; sıfır çizgisi aynı günü temsil eder.</p>
      <div id="dailyPnl"></div>
    </section>
    <section class="card">
      <h3>Günlük işlem sayısı</h3>
      <p class="hint">Seçili strateji + filtre; çıkış gününe göre.</p>
      <div id="dailyCount"></div>
    </section>
    <section class="card">
      <h3>Kümülatif equity</h3>
      <p class="hint">1/525 eşit ağırlık, günlük netlerin bileşiği.</p>
      <div id="equity"></div>
    </section>
    <section class="card">
      <h3>Filtre sıralaması</h3>
      <p class="hint">Seçili stratejide ortalama işlem başı net.</p>
      <div id="filterRank"></div>
    </section>
    <section class="card">
      <h3>Seçili kural</h3>
      <p class="hint" id="ruleMeta"></p>
      <div class="rule" id="ruleBox">—</div>
    </section>
    <section class="card wide">
      <h3>Tüm strateji × filtre kombinasyonları</h3>
      <div class="toolbar"><label>Min işlem <input id="minN" type="number" value="20" min="0" step="10" style="width:64px;background:#0a1322;border:1px solid var(--line);color:var(--text);border-radius:6px;padding:3px 5px"></label><span class="hint" id="tableHint"></span></div>
      <div class="tablewrap"><table id="resultTable"><thead></thead><tbody></tbody></table></div>
    </section>
  </div>
  <div class="note">
    274 high/medium source mapping → 120 benzersiz kural (1d/4h/1h/1w), bunlardan 116’sı işlem üretti. 5m/15m filtre katmanına alınmadı: brüt kenar zaten negatif ve 219M işlemde filtre durumları maliyetin altında kalıyor. Filtreler tek tek; “tüm strateji × filtre” kombinasyonları listelenir.
  </div>
</main>
</div>
<script>
const DATA = __DATA__;
const F = DATA.filters;
const FILTERS = [{id:'baseline', key:'baseline', label:'Filtresiz baz', label_tr:'Filtresiz baz', bit:null}, ...F];
const SPECS = DATA.specs;
const state = {idx:null, filter:'baseline', positiveOnly:true, showBase:true, sort:'median_symbol_net', dir:-1, minN:20};
const fmtPct=(x,d=2)=>x==null||!isFinite(x)?'—':(x*100).toFixed(d)+'%';
const fmtNum=(x)=>x==null?'—':Math.round(x).toLocaleString('en-US');
const esc=(s)=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const dayStr=(d)=>{const x=new Date(d*86400000);return x.toISOString().slice(0,10);};
const rkey=(idx,fid)=>`${idx}|${fid}`;
const resMap=new Map(); DATA.results.forEach(r=>resMap.set(rkey(r.idx,r.filter_key),r));
const baseMap=new Map(); DATA.results.forEach(r=>{if(r.filter_key==='baseline')baseMap.set(r.idx,r);});

function specByIdx(idx){return SPECS.find(s=>s.idx===idx)||null;}
function resultFor(idx,fid){return resMap.get(rkey(idx,fid))||null;}
function defaultResult(){
  let kept=DATA.results.filter(r=>r.kept && r.n>=100 && r.symbols>=20 && r.median_symbol_net>0);
  if(!kept.length) kept=DATA.results.filter(r=>r.kept && r.n>=30);
  if(!kept.length) kept=DATA.results.filter(r=>r.kept);
  kept.sort((a,b)=>b.median_symbol_net-a.median_symbol_net);
  return kept[0]||DATA.results[0];
}
function renderTitle(){
  const s=specByIdx(state.idx);
  document.getElementById('title').textContent=s?`${s.sid} · ${s.title.replace(s.sid,'').replace(/^[\s—–-]+/,'')}`:'Strateji seç';
  document.getElementById('strategySel').value=String(state.idx);
}
function sortResults(rows){
  const k=state.sort, d=state.dir;
  return rows.sort((a,b)=>{let av=a[k],bv=b[k];
    if(typeof av==='string'){av=(av||'').toLowerCase();bv=(bv||'').toLowerCase();}
    return (av>bv?1:av<bv?-1:0)*d;});
}
function filteredResults(){
  let rows=DATA.results.filter(r=>{
    if(!state.showBase && r.filter_key==='baseline')return false;
    if(state.positiveOnly && !r.kept)return false;
    if(r.n < state.minN)return false;
    return true;
  });
  const q=document.getElementById('strategySearch').value.toLowerCase();
  if(q) rows=rows.filter(r=>(r.sid+' '+r.title+' '+r.tf+' '+r.family+' '+r.filter_key+' '+r.filter_label_tr).toLowerCase().includes(q));
  return sortResults(rows);
}
function renderFilters(){
  const el=document.getElementById('filterList');
  el.innerHTML=FILTERS.map(f=>{
    const st=(DATA.filter_stats.find(x=>x.id===f.id)||{});
    const active=state.filter===f.id?' active':'';
    const right=f.id==='baseline'?`<span class="fcount">baz</span>`:`<span class="fcount">${st.n_positive||0}/${st.n_results||0}</span>`;
    return `<button class="fbtn${active}" data-fid="${esc(f.id)}"><span><b>${esc(f.label_tr)}</b><small>${esc(f.label)}</small></span>${right}</button>`;
  }).join('');
  el.querySelectorAll('button').forEach(b=>b.addEventListener('click',()=>{state.filter=b.dataset.fid;renderAll();}));
}
function resultForSelected(){
  let r=resultFor(state.idx,state.filter);
  if(!r) r=baseMap.get(state.idx);
  return r;
}
function renderKpis(r){
  const s=specByIdx(state.idx)||{};
  const k=[
    ['İşlem',fmtNum(r?.n)],['Ort. net',fmtPct(r?.avg_net,3)],['Toplam (işlem)',fmtPct(r?.total_net,1)],
    ['Portföy',fmtPct(r?.portfolio_net,1)],['Kazanma',fmtPct(r?.win_rate,1)],
    ['PF',r?.profit_factor>=999?'∞':(r?.profit_factor!=null?r.profit_factor.toFixed(2):'—')],
    ['Maks DD',fmtPct(r?.max_dd,1)]
  ];
  document.getElementById('kpis').innerHTML=k.map(([l,v])=>`<div class="kpi"><div class="v ${String(v).startsWith('-')?'neg':(l==='Ort. net'?'pos':'')}">${v}</div><div class="l">${l}</div></div>`).join('');
  document.getElementById('subtitle').textContent=r?`${s.tf||''} · ${s.family||''} · ${r.filter_label_tr} · ${r.symbols||0} sembol · ${fmtPct(r.portfolio_net,1)} portföy`:'Bu kombinasyon için işlem yok.';
}
function svgOpen(w,h){return `<svg class="chart" viewBox="0 0 ${w} ${h}" role="img">`;}
function drawDailyPnl(r){
  const el=document.getElementById('dailyPnl');
  if(!r||!r.daily||!r.daily.length){el.innerHTML='<div class="empty">Pozitif sonuç yok; başka filtre seç.</div>';return;}
  const w=1180,h=340,pad={l:64,r:18,t:22,b:44};
  const d=r.daily; const alloc=DATA.meta.alloc_n||525;
  const vals=d.flatMap(x=>[x[2]/alloc,x[3]/alloc]); let mx=Math.max(0,...vals.map(Math.abs),0.0001);
  const bw=(w-pad.l-pad.r)/Math.max(d.length,1);
  const y0=pad.t+(h-pad.t-pad.b)/2;
  let s=svgOpen(w,h);
  for(let i=0;i<=4;i++){const y=pad.t+(h-pad.t-pad.b)*i/4; const v=mx-(2*mx)*i/4; s+=`<line x1="${pad.l}" y1="${y}" x2="${w-pad.r}" y2="${y}" stroke="#1b2942"/><text x="${pad.l-8}" y="${y+4}" text-anchor="end" fill="#637795" font-size="10">${fmtPct(v,1)}</text>`;}
  s+=`<line x1="${pad.l}" y1="${y0}" x2="${w-pad.r}" y2="${y0}" stroke="#3b4b68"/>`;
  const step=Math.max(1,Math.ceil(d.length/8));
  d.forEach((x,i)=>{
    const px=pad.l+i*bw+1, bwid=Math.max(1,bw-2); const pos=x[2]/alloc,neg=x[3]/alloc;
    const yp=pad.t+(h-pad.t-pad.b)*(mx-pos)/(2*mx), hp=y0-yp;
    const yn=pad.t+(h-pad.t-pad.b)*(mx-neg)/(2*mx), hn=yn-y0;
    if(pos>0) s+=`<rect x="${px}" y="${yp}" width="${bwid}" height="${Math.max(1,hp)}" fill="#34d399" opacity=".9"><title>${dayStr(x[0])} · +${fmtPct(pos,3)} · ${x[1]} işlem</title></rect>`;
    if(neg<0) s+=`<rect x="${px}" y="${y0}" width="${bwid}" height="${Math.max(1,hn)}" fill="#fb7185" opacity=".9"><title>${dayStr(x[0])} · ${fmtPct(neg,3)} · ${x[1]} işlem</title></rect>`;
    if(i%step===0) s+=`<text x="${px+bwid/2}" y="${h-pad.b+16}" text-anchor="middle" fill="#8da2c0" font-size="9">${dayStr(x[0]).slice(2,7)}</text>`;
  });
  s+='</svg>'; el.innerHTML=s;
  document.getElementById('dailyHint').textContent=`${d.length} gün · aynı gün pozitif ve negatif realized PnL tek barda · hesap toplamı ${fmtPct(r.portfolio_net,1)} (1/${alloc})`;
}
function drawCount(r){
  const el=document.getElementById('dailyCount');
  if(!r||!r.daily||!r.daily.length){el.innerHTML='<div class="empty">Veri yok.</div>';return;}
  const w=560,h=250,pad={l:45,r:10,t:14,b:35}; const d=r.daily; const mx=Math.max(1,...d.map(x=>x[1]));
  let s=svgOpen(w,h); const bw=(w-pad.l-pad.r)/Math.max(d.length,1);
  s+=`<line x1="${pad.l}" y1="${h-pad.b}" x2="${w-pad.r}" y2="${h-pad.b}" stroke="#22314d"/>`;
  d.forEach((x,i)=>{const bh=(h-pad.t-pad.b)*x[1]/mx; s+=`<rect x="${pad.l+i*bw+1}" y="${h-pad.b-bh}" width="${Math.max(1,bw-2)}" height="${Math.max(1,bh)}" fill="#5eead4" opacity=".75"><title>${dayStr(x[0])}: ${x[1]} işlem</title></rect>`;});
  s+=`<text x="${pad.l}" y="${h-8}" fill="#637795" font-size="9">${dayStr(d[0][0])}</text><text x="${w-pad.r}" y="${h-8}" text-anchor="end" fill="#637795" font-size="9">${dayStr(d[d.length-1][0])}</text>`;
  s+='</svg>'; el.innerHTML=s;
}
function drawEquity(r){
  const el=document.getElementById('equity');
  if(!r||!r.daily||!r.daily.length){el.innerHTML='<div class="empty">Veri yok.</div>';return;}
  const w=560,h=250,pad={l:48,r:10,t:14,b:35}; let eq=1; const pts=[[0,1]];
  r.daily.forEach((x,i)=>{eq*=1+x[4]/DATA.meta.alloc_n; pts.push([i,eq]);});
  const mn=Math.min(...pts.map(p=>p[1]),1), mx=Math.max(...pts.map(p=>p[1]),1);
  const X=i=>pad.l+i/(pts.length-1||1)*(w-pad.l-pad.r), Y=v=>pad.t+(h-pad.t-pad.b)*(mx-v)/(mx-mn||1);
  let s=svgOpen(w,h); [0,.5,1].forEach(t=>{const y=pad.t+(h-pad.t-pad.b)*t; s+=`<line x1="${pad.l}" y1="${y}" x2="${w-pad.r}" y2="${y}" stroke="#1b2942"/><text x="${pad.l-8}" y="${y+4}" text-anchor="end" fill="#637795" font-size="9">${(mx-(mx-mn)*t).toFixed(2)}x</text>`;});
  s+=`<polyline fill="none" stroke="#5eead4" stroke-width="2.2" points="${pts.map(p=>`${X(p[0])},${Y(p[1])}`).join(' ')}"/>`;
  s+=`<text x="${pad.l}" y="${h-8}" fill="#637795" font-size="9">${dayStr(r.daily[0][0])}</text><text x="${w-pad.r}" y="${h-8}" text-anchor="end" fill="#637795" font-size="9">${dayStr(r.daily[r.daily.length-1][0])}</text>`;
  s+='</svg>'; el.innerHTML=s;
}
function drawRank(){
  const el=document.getElementById('filterRank');
  const rows=FILTERS.map(f=>{const r=resultFor(state.idx,f.id); return r?{f,r}:null;}).filter(Boolean).sort((a,b)=>b.r.avg_net-a.r.avg_net);
  if(!rows.length){el.innerHTML='<div class="empty">Filtre sonucu yok.</div>';return;}
  const w=560,rh=22,h=Math.max(120,rows.length*rh+24),pad={l:150,r:60,t:8,b:8};
  const mx=Math.max(0.001,...rows.map(x=>Math.abs(x.r.avg_net)));
  let s=svgOpen(w,h); s+=`<line x1="${pad.l}" y1="${pad.t}" x2="${pad.l}" y2="${h-pad.b}" stroke="#22314d"/>`;
  rows.forEach((x,i)=>{const y=pad.t+i*rh+4, len=(w-pad.l-pad.r)*Math.abs(x.r.avg_net)/mx; const pos=x.r.avg_net>=0; const xx=pos?pad.l:pad.l-len;
    s+=`<rect x="${xx}" y="${y}" width="${Math.max(1,len)}" height="${rh-7}" rx="2" fill="${pos?'#34d399':'#fb7185'}" opacity=".88"><title>${esc(x.f.label_tr)}: ${fmtPct(x.r.avg_net,3)} · n=${x.r.n}</title></rect>`;
    s+=`<text x="${pad.l-6}" y="${y+rh/2}" text-anchor="end" fill="#8da2c0" font-size="9">${esc(x.f.label_tr.slice(0,24))}</text>`;
    s+=`<text x="${w-pad.r}" y="${y+rh/2}" text-anchor="end" fill="${pos?'#34d399':'#fb7185'}" font-size="9">${fmtPct(x.r.avg_net,2)}</text>`;});
  s+='</svg>'; el.innerHTML=s;
}
function renderTable(){
  const rows=filteredResults();
  document.getElementById('tableHint').textContent=`${rows.length} kombinasyon · ${state.positiveOnly?'pozitif ortalama net':'tümü'} · tabloya tıkla`;
  const cols=[['sid','SID'],['tf','TF'],['filter_label_tr','Filtre'],['n','İşlem'],['avg_net','Ort. net'],['median_symbol_net','Med. sembol'],['total_net','Toplam'],['win_rate','Kazanma'],['profit_factor','PF'],['symbols','Sembol'],['portfolio_net','Portföy']];
  document.querySelector('#resultTable thead').innerHTML='<tr>'+cols.map(([k,l])=>`<th data-k="${k}" class="${k==='sid'||k==='tf'||k==='filter_label_tr'?'':'num'}">${l}</th>`).join('')+'</tr>';
  document.querySelector('#resultTable tbody').innerHTML=rows.map(r=>`<tr class="rowline ${r.idx===state.idx&&r.filter_key===state.filter?'sel':''}" data-idx="${r.idx}" data-f="${esc(r.filter_key)}">
    <td><b>${esc(r.sid)}</b></td><td><span class="badge">${esc(r.tf)}</span></td><td>${esc(r.filter_label_tr)}</td>
    <td class="num">${fmtNum(r.n)}</td><td class="num ${r.avg_net>=0?'pos':'neg'}">${fmtPct(r.avg_net,3)}</td>
    <td class="num ${r.median_symbol_net>=0?'pos':'neg'}">${fmtPct(r.median_symbol_net,3)}</td>
    <td class="num ${r.total_net>=0?'pos':'neg'}">${fmtPct(r.total_net,1)}</td><td class="num">${fmtPct(r.win_rate,1)}</td>
    <td class="num">${r.profit_factor>=999?'∞':(r.profit_factor??'—')}</td><td class="num">${r.symbols}</td>
    <td class="num ${r.portfolio_net>=0?'pos':'neg'}">${fmtPct(r.portfolio_net,1)}</td></tr>`).join('');
  document.querySelectorAll('#resultTable tbody tr').forEach(tr=>tr.addEventListener('click',()=>{state.idx=+tr.dataset.idx; state.filter=tr.dataset.f; document.getElementById('strategySel').value=String(state.idx); renderAll();}));
  document.querySelectorAll('#resultTable th').forEach(th=>th.addEventListener('click',()=>{const k=th.dataset.k; if(!k)return; state.dir=state.sort===k?-state.dir:-1; state.sort=k; renderTable();}));
}
function renderRule(r){
  const s=specByIdx(state.idx)||{};
  document.getElementById('ruleMeta').textContent=`${s.batch||''} · ${s.family||''} · ${s.confidence||''} · ${r?fmtNum(r.n)+' işlem':'—'}`;
  const txt=(s.rule_long?`LONG  ${s.rule_long}\n`:'')+(s.rule_short?`SHORT ${s.rule_short}\n`:'')+(r?`\nFiltre: ${r.filter_label_tr}`:'');
  document.getElementById('ruleBox').textContent=txt||'Kural metni yok.';
}
function renderAll(){
  renderTitle();
  renderFilters();
  const r=resultForSelected();
  renderKpis(r); drawDailyPnl(r); drawCount(r); drawEquity(r); drawRank(); renderTable(); renderRule(r);
}
function init(){
  const opts=SPECS.slice().sort((a,b)=>(a.batch+a.sid).localeCompare(b.batch+b.sid));
  document.getElementById('strategySel').innerHTML=opts.map(s=>`<option value="${s.idx}">${esc(s.sid)} · ${esc(s.tf)} · ${esc(s.family)} — ${esc(s.title.replace(s.sid,'').replace(/^[\s—–-]+/,''))}</option>`).join('');
  document.getElementById('strategySel').addEventListener('change',e=>{state.idx=+e.target.value; if(!resultFor(state.idx,state.filter)) state.filter='baseline'; renderAll();});
  document.getElementById('strategySearch').addEventListener('input',()=>{renderTable();});
  document.getElementById('positiveOnly').addEventListener('change',e=>{state.positiveOnly=e.target.checked;renderTable();});
  document.getElementById('showBase').addEventListener('change',e=>{state.showBase=e.target.checked;renderTable();});
  document.getElementById('minN').addEventListener('input',e=>{state.minN=+e.target.value||0;renderTable();});
  const d=defaultResult()||DATA.results[0];
  state.idx=d.idx; state.filter=d.filter_key;
  document.getElementById('strategySel').value=String(d.idx);
  renderAll();
}
init();
</script>
</body>
</html>'''

HTML = HTML.replace('__DATA__', json.dumps(DATA, ensure_ascii=False).replace('</', '<\\/'))
out = os.path.join(ROOT, 'filter_dashboard.html')
open(out, 'w', encoding='utf-8').write(HTML)
print('wrote', out, len(HTML), 'bytes')
