import json, re, os, sys
sys.path.insert(0, r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest')
import families as F

ROOT = r'D:\Paper_ML_BSH\analysis\book_signal_review'
rows = json.load(open(os.path.join(ROOT, 'backtest', 'sections.json'), encoding='utf-8'))

EXCLUDE = [
    ('opsiyon', 'Opsiyon uygulaması; vadeli OHLCV ile test edilemez.'),
    ('option', 'Opsiyon uygulaması; vadeli OHLCV ile test edilemez.'),
    ('portföy', 'Portföy/kural karşılaştırması; tek enstrüman sinyali değil.'),
    ('pozisyon büyüklüğü', 'Pozisyon büyüklüğü kuralı; giriş sinyali değil.'),
    ('risk yönetimi', 'Risk yönetimi kuralı; giriş sinyali değil.'),
    ('filtre deneyi', 'Filtre/ablation deneyi; bağımsız giriş değil.'),
    ('özellik adayı', 'Özellik adayı; işlem sinyali değil.'),
    ('sinyal değil', 'Sinyal değil.'),
    ('strateji değil', 'Strateji değil.'),
    ('ertelendi', 'Yazar tarafından ertelenmiş / tanım eksik.'),
    ('alınmaz', 'Yazar ilk backteste almamış.'),
    ('eklenmez', 'Yazar kataloğa eklememiş.'),
    ('uygun değil', 'Kaynak kuralı kripto vadeli verisine uygun değil.'),
    ('veri koşullu', 'Gerekli veri (FX/seans/haber) yok.'),
    ('NFP', 'Haber verisi gerekli.'),
    ('FOMC', 'Haber verisi gerekli.'),
    ('SPY', 'ABD hisse/endeks verisi gerekli.'),
    ('QQQ', 'ABD hisse/endeks verisi gerekli.'),
    ('hisse evreni', 'ABD hisse evreni gerekli.'),
    ('delist', 'ABD hisse evreni gerekli.'),
    ('Nifty', 'Nifty vadeli verisi yok.'),
    ('BankNifty', 'Nifty vadeli verisi yok.'),
    ('Camarilla', 'Seans/pivot seviyeleri kripto 7/24 için uyarlanabilir; proxy test.'),
]
ASSET_HARD = ['SPY', 'QQQ', 'Nifty', 'BankNifty', 'NFP', 'FOMC', 'earnings', 'kazanç',
              'ABD hisse', 'delist', 'opsiyon', 'option']


def clean(s):
    return re.sub(r'\s+', ' ', s)


def get_tf(title, body):
    text = title + ' ' + body
    # explicit event timeframe patterns
    for pat in [r'(?:olay|sinyal|kapanış|tetik)[^.]{0,80}?\b(M1|M5|M15|M30|H1|H4|D1|W1)\b',
                r'\b(M1|M5|M15|M30|H1|H4|D1|W1)\b[^.]{0,40}?(?:kapanış|olay|sinyal)']:
        m = re.search(pat, text)
        if m:
            return {'M1': '1m', 'M5': '5m', 'M15': '15m', 'M30': '15m', 'H1': '1h',
                    'H4': '4h', 'D1': '1d', 'W1': '1d'}[m.group(1)]
    # most frequent
    counts = {k: len(re.findall(rf'\b{k}\b', text)) for k in ['M1', 'M5', 'M15', 'M30', 'H1', 'H4', 'D1', 'W1']}
    k = max(counts, key=counts.get)
    if counts[k] == 0:
        return '1d'
    return {'M1': '1m', 'M5': '5m', 'M15': '15m', 'M30': '15m', 'H1': '1h',
            'H4': '4h', 'D1': '1d', 'W1': '1d'}[k]


def nums_after(text, key, default=None):
    m = re.search(key + r'\s*[\(\[]?\s*(\d+)', text, re.I)
    return int(m.group(1)) if m else default


def two_periods(text, default=(20, 50)):
    pairs = re.findall(r'\b(?:EMA|SMA|LWMA|WMA|SMMA)\s*[\(\[]?\s*(\d+)\s*[\)\]]?\s*[/\-–]\s*(\d+)', text, re.I)
    if pairs:
        return int(pairs[0][0]), int(pairs[0][1])
    vals = [int(x) for x in re.findall(r'\b(?:EMA|SMA|LWMA|WMA|SMMA)\s*[\(\[]?\s*(\d+)\b', text, re.I)]
    vals = list(dict.fromkeys(vals))
    if len(vals) >= 2:
        return vals[0], vals[1]
    if len(vals) == 1:
        return vals[0], default[1]
    return default


def get_stop(text, default=2.0):
    m = re.search(r'(\d+(?:[.,]\d+)?)\s*(?:x|×)?\s*(?:ATR|atr)', text)
    if m:
        v = float(m.group(1).replace(',', '.'))
        if 0.2 <= v <= 8:
            return v
    return default


def get_time(text, tf, default=None):
    m = re.search(r'H(\d+)\s*D', text)
    if m:
        return int(m.group(1))
    m = re.search(r'(\d+)\s*(?:tam(?:amlanmış)?\s*)?(?:H1|H4|M15|M5|M1|bar)\b', text)
    if m:
        v = int(m.group(1))
        if 1 <= v <= 200:
            return v
    if default is not None:
        return default
    return {'1d': 14, '4h': 30, '1h': 48, '15m': 32, '5m': 48, '1m': 60}.get(tf, 14)


def family_for(title, body):
    t = (title + ' ' + body).lower()
    # explicit exclusions first
    for kw, reason in EXCLUDE:
        if kw.lower() in t:
            if kw in ('Camarilla',):
                continue
            return None, reason
    if any(k.lower() in t for k in ASSET_HARD):
        return None, 'Gerekli varlık/veri türü (hisse, endeks, haber, opsiyon) yok.'
    # title-first rules
    if 'supertrend' in t:
        return 'supertrend', None
    if 'ichimoku' in t or 'bulut' in t or 'tenkan' in t or 'kijun' in t:
        return ('ichimoku_tk' if ('tenkan' in t and 'kijun' in t and 'bulut' not in title.lower()) else 'ichimoku_cloud'), None
    if 'macd' in t:
        return ('macd_cross' if ('kesiş' in t or 'cross' in t or 'sinyal' in t) else 'macd_hist'), None
    if 'bollinger' in t or re.search(r'\bbb\b', t):
        if any(k in t for k in ['kırılım', 'breakout', 'sıkış', 'daral', 'açıl']):
            return 'bb_break', None
        return 'bb_reversion', None
    if 'keltner' in t:
        return 'keltner_rev', None
    if 'stokastik' in t or 'stochastic' in t or 'stoch' in t:
        return 'stoch', None
    if 'cci' in t:
        return 'cci_rev', None
    if 'rsi' in t:
        if any(k in t for k in ['ayrış', 'divergence']):
            return None, 'RSI ayrışması; nedensel pivot tanımı yok.'
        if any(k in t for k in ['60/40', '50 rejim', 'momentum', 'trend']):
            return 'rsi_momentum', None
        return 'rsi_reversion', None
    if 'vwap' in t:
        return ('vwap_break' if any(k in t for k in ['kırılım', 'break', 'üstü', 'geçiş']) else 'vwap_rev'), None
    if 'donchian' in t or ('kanal' in t and 'kırılım' in t):
        return 'donchian_break', None
    if any(k in t for k in ['çift dip', 'çift tepe', 'ikili dip', 'ikili tepe', 'double top', 'double bottom']):
        return 'double_pattern', None
    if 'fibonacci' in t or re.search(r'\bfib\b', t):
        return 'fib_retrace', None
    if any(k in t for k in ['yutan', 'engulf', 'çekiç', 'hammer', 'pin bar', 'doji', 'iç bar', 'inside bar', 'harami']):
        return 'candle_pattern', None
    if any(k in t for k in ['önceki gün', 'önceki hafta', 'seans', 'session', 'pivot', 'açılış aralığı']):
        return 'session_level', None
    if any(k in t for k in ['kutu', 'aralık', 'sıkış', 'range', 'konsolidasyon', 'dar bant']):
        return 'range_break', None
    if 'adx' in t:
        return ('donchian_break' if 'kırılım' in t else 'ma_pullback'), None
    if any(k in t for k in ['pivot', 'swing', 'yapı kırılım', 'fraktal']):
        return 'pivot_break', None
    if any(k in t for k in ['ema', 'sma', 'hareketli ortalama']):
        if any(k in t for k in ['kesiş', 'cross', 'çapraz']):
            return 'ma_cross', None
        return 'ma_pullback', None
    if any(k in t for k in ['momentum', 'roc', 'trend']):
        return 'ma_cross', None
    return None, 'Mekanik giriş kuralı otomatik eşleştirilemedi.'


def build_spec(i, r):
    title, body = r['title'], r['body']
    fam, reason = family_for(title, body)
    if fam is None:
        return {'idx': i, 'batch': r['batch'], 'sid': r['id'], 'title': title,
                'status': 'excluded', 'reason': reason}
    tf = get_tf(title, body)
    text = title + ' ' + body
    low = text.lower()
    long_only = ('yalnız long' in low or 'sadece al' in low or 'long-only' in low)
    short = ('short' in low or 'satış' in low or 'simetrik' in low)
    stop = get_stop(body)
    time = get_time(body, tf)
    fast, slow = two_periods(text, (20, 50))
    try:
        if fam == 'ma_cross':
            sp = F.ma_cross(i, tf, fast, slow, 200, 'ema', stop, time, True, long_only, short)
        elif fam == 'ma_pullback':
            sp = F.ma_pullback(i, tf, fast, slow, max(fast, 20), 5, stop, time, long_only, short)
        elif fam == 'donchian_break':
            n = nums_after(text, r'donchian', None) or nums_after(text, r'(\d+)\s*(?:gün|bar)', 20)
            sp = F.donchian_break(i, tf, n, 0, 0, 0, stop, time, long_only, short)
        elif fam == 'range_break':
            n = nums_after(text, r'(\d+)\s*(?:gün|bar)', 20)
            sp = F.range_break(i, tf, n, 4.0, 0, stop, time, long_only, short)
        elif fam == 'pivot_break':
            sp = F.pivot_break(i, tf, 2, 2, 20, stop, time, long_only, short)
        elif fam == 'bb_reversion':
            n = nums_after(text, r'bb', 20); k = 2.0
            m = re.search(r'bb\s*[\(\[]\s*\d+\s*[;,]\s*(\d+(?:[.,]\d+)?)', text, re.I)
            if m: k = float(m.group(1).replace(',', '.'))
            sp = F.bb_reversion(i, tf, n, k, 14, 30, 70, 0, stop, time, long_only, short)
        elif fam == 'bb_break':
            sp = F.bb_break(i, tf, 20, 2.0, 200, stop, time, long_only, short)
        elif fam == 'rsi_reversion':
            n = nums_after(text, r'rsi', 14)
            sp = F.rsi_reversion(i, tf, n, 30, 70, 50, 0, stop, time, long_only, short)
        elif fam == 'rsi_momentum':
            n = nums_after(text, r'rsi', 14)
            sp = F.rsi_momentum(i, tf, n, 50, stop, time, long_only, short)
        elif fam == 'macd_cross':
            sp = F.macd_cross(i, tf, 12, 26, 9, False, stop, time, long_only, short)
        elif fam == 'macd_hist':
            sp = F.macd_hist(i, tf, 12, 26, 9, stop, time, long_only, short)
        elif fam == 'stoch':
            sp = F.stoch(i, tf, 14, 3, 3, 20, 80, stop, time, long_only, short)
        elif fam == 'ichimoku_cloud':
            sp = F.ichimoku_cloud(i, tf, stop, time, long_only, short)
        elif fam == 'ichimoku_tk':
            sp = F.ichimoku_tk(i, tf, True, stop, time, long_only, short)
        elif fam == 'supertrend':
            sp = F.supertrend_flip(i, tf, 10, 3.0, stop, time, long_only, short)
        elif fam == 'keltner_rev':
            sp = F.keltner_rev(i, tf, 20, 1.5, 5, 30, 70, stop, time, long_only, short)
        elif fam == 'cci_rev':
            sp = F.cci_rev(i, tf, 20, -200, 200, 0, stop, time, long_only, short)
        elif fam == 'vwap_rev':
            sp = F.vwap_rev(i, tf, 2.0, stop, time, long_only, short)
        elif fam == 'vwap_break':
            sp = F.vwap_break(i, tf, stop, time, long_only, short)
        elif fam == 'double_pattern':
            sp = F.double_pattern(i, tf, 10, 0.5, stop, time, long_only, short)
        elif fam == 'fib_retrace':
            sp = F.fib_retrace(i, tf, 2, 0.5, 0.618, 200, stop, time, long_only, short)
        elif fam == 'candle_pattern':
            kind = 'engulf' if ('yutan' in low or 'engulf' in low) else ('inside' if ('iç bar' in low or 'inside' in low) else 'pin')
            sp = F.candle_pattern(i, tf, kind, 200 if 'trend' in low else 0, stop, time, long_only, short)
        elif fam == 'session_level':
            mode = 'failed' if any(k in low for k in ['başarısız', 'sahte', 'süpür', 'geri kapan']) else 'break'
            sp = F.session_level(i, tf, mode, stop, time, long_only, short)
        else:
            return {'idx': i, 'batch': r['batch'], 'sid': r['id'], 'title': title,
                    'status': 'excluded', 'reason': 'Bilinmeyen aile.'}
    except Exception as e:
        return {'idx': i, 'batch': r['batch'], 'sid': r['id'], 'title': title,
                'status': 'excluded', 'reason': f'Spec üretim hatası: {e}'}
    sp.update(batch=r['batch'], sid=r['id'], title=title, status='tested', family=fam,
              mapping='auto', confidence='medium', summary=clean(body)[:300])
    return sp


specs = [build_spec(i, r) for i, r in enumerate(rows)]
json.dump(specs, open(os.path.join(ROOT, 'backtest', 'specs_auto.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
from collections import Counter
print(Counter(s['status'] for s in specs))
print(Counter(s.get('family') for s in specs if s['status'] == 'tested'))
print(Counter(s.get('reason', '') for s in specs if s['status'] == 'excluded').most_common(15))
