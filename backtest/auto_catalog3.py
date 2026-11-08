import json, re, os, sys
sys.path.insert(0, r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest')
import families as F

ROOT = r'D:\Paper_ML_BSH\analysis\book_signal_review'
rows = json.load(open(os.path.join(ROOT, 'backtest', 'sections.json'), encoding='utf-8'))

HARD_EXCLUDE = [
    ('opsiyon', 'Opsiyon uygulaması; vadeli OHLCV ile test edilemez.'),
    ('option', 'Opsiyon uygulaması; vadeli OHLCV ile test edilemez.'),
    ('portföy', 'Portföy/rotasyon kuralı; tek enstrüman girişi değil.'),
    ('rotasyon', 'Portföy/rotasyon kuralı; tek enstrüman girişi değil.'),
    ('sepet', 'Sepet/portföy kuralı; tek enstrüman girişi değil.'),
    ('pozisyon büyüklüğü', 'Pozisyon büyüklüğü kuralı; giriş sinyali değil.'),
    ('pozisyon yönetimi', 'Pozisyon yönetimi kuralı; giriş sinyali değil.'),
    ('risk yönetimi', 'Risk yönetimi kuralı; giriş sinyali değil.'),
    ('risk karşı', 'Risk karşı örneği; işlem stratejisi değil.'),
    ('filtre deneyi', 'Filtre/ablation deneyi; bağımsız giriş değil.'),
    ('ablation', 'Ablation/karşılaştırma; bağımsız giriş değil.'),
    ('özellik adayı', 'Özellik adayı; işlem sinyali değil.'),
    ('sinyal değil', 'Sinyal değil.'),
    ('strateji değil', 'Strateji değil.'),
    ('ertelendi', 'Yazar tarafından ertelenmiş / tanım eksik.'),
    ('ertelenen', 'Yazar tarafından ertelenmiş / tanım eksik.'),
    ('alınmaz', 'Yazar ilk backteste almamış.'),
    ('eklenmez', 'Yazar kataloğa eklememiş.'),
    ('uygun değil', 'Kaynak kuralı kripto vadeli verisine uygun değil.'),
    ('veri koşullu', 'Gerekli veri (FX/seans/haber) yok.'),
    ('NFP', 'Haber verisi gerekli.'),
    ('FOMC', 'Haber verisi gerekli.'),
    ('SPY', 'ABD hisse/endeks verisi gerekli.'),
    ('QQQ', 'ABD hisse/endeks verisi gerekli.'),
    ('Nifty', 'Nifty vadeli verisi yok.'),
    ('BankNifty', 'Nifty vadeli verisi yok.'),
    ('earnings', 'Kazanç/haber verisi gerekli.'),
    ('kazanç açıklama', 'Kazanç/haber verisi gerekli.'),
    ('delist', 'ABD hisse evreni gerekli.'),
    ('hisse evreni', 'ABD hisse evreni gerekli.'),
    ('ABD hisse', 'ABD hisse evreni gerekli.'),
    ('karar:', 'Karar/özet başlığı; bağımsız strateji değil.'),
    ('ertelenen/tekrar', 'Erteleme notu; bağımsız strateji değil.'),
    ('test sırası', 'Test sırası/planı; bağımsız strateji değil.'),
    ('karşılaştırma', 'Karşılaştırma/ablasyon; bağımsız giriş değil.'),
]

ASSET_HARD = ['SPY', 'QQQ', 'Nifty', 'BankNifty', 'NFP', 'FOMC', 'earnings',
              'ABD hisse', 'delist', 'opsiyon', 'option']

TITLE_RULES = [
    (r'supertrend', 'supertrend'),
    (r'ichimoku|bulut|tenkan|kijun', 'ichimoku'),
    (r'fibonacci|\bfib\b|altın bölge|altin bolge', 'fib_retrace'),
    (r'vwap', 'vwap'),
    (r'macd', 'macd'),
    (r'smma', 'smma_channel'),
    (r'bollinger|\bbb\b', 'bb'),
    (r'keltner', 'keltner_rev'),
    (r'stokastik|stochastic|\bstoch\b', 'stoch'),
    (r'williams\s*%?r', 'smma_channel'),
    (r'\bcci\b', 'cci_rev'),
    (r'çift dip|çift tepe|ikili dip|ikili tepe|double top|double bottom|üçlü dip|üçlü tepe|baş-omuz|omuz-baş', 'double_pattern'),
    (r'nr\s*4|nr\s*7|nr4|nr7', 'nr_break'),
    (r'td\s*9|td\s*13|td sequential|td dizisi', 'td_setup'),
    (r'heikin|ha dönüş|ha renk', 'ha_reversal'),
    (r'yutan|engulf|çekiç|hammer|pin bar|doji|iç bar|inside bar|harami|kayan yıldız|shooting star|marubozu|fitil|reddedilme|ters mum', 'candle_pattern'),
    (r'kesiş|cross|çapraz', 'ma_cross'),
    (r'\brsi\b', 'rsi'),
    (r'adx', 'adx'),
    (r'donchian|dışına taşma|dışına çıkma|kanal|channel', 'donchian_break'),
    (r'cpr', 'cpr_break'),
    (r'pivot seviye|önceki gün|önceki hafta|seans|session|gün yüksek|gün düşük|hafta yüksek|hafta düşük|açılış aralığı|açılış aralı', 'session_level'),
    (r'kutu|dar aralık|sıkışma|sıkış|range|konsolidasyon|dar bant|üçgen|bayrak|flama|triangle|flag|pennant', 'range_break'),
    (r'pivot|swing|fraktal|yapı kırılım|destek|direnç|seviye|trend çizgisi|trendline', 'pivot_break'),
    (r'ema|sma|hareketli ortalama|\bma\d', 'ma_pullback'),
    (r'momentum|roc|trend', 'ma_cross'),
]

BODY_RULES = [
    (r'supertrend', 'supertrend'),
    (r'ichimoku|bulut|tenkan|kijun', 'ichimoku'),
    (r'macd', 'macd'),
    (r'bollinger|\bbb\b', 'bb'),
    (r'keltner', 'keltner_rev'),
    (r'stokastik|stochastic|stoch', 'stoch'),
    (r'cci', 'cci_rev'),
    (r'rsi', 'rsi'),
    (r'adx', 'adx'),
    (r'donchian|kanal kırılımı', 'donchian_break'),
    (r'çift dip|çift tepe|double top|double bottom', 'double_pattern'),
    (r'yutan|engulf|çekiç|hammer|pin bar|doji|iç bar|inside', 'candle_pattern'),
    (r'önceki gün|önceki hafta|seans|session|cpr|pivot seviye', 'session_level'),
    (r'kutu|aralık|sıkış|range|konsolidasyon|üçgen|bayrak|flama', 'range_break'),
    (r'pivot|swing|fraktal|yapı kırılım', 'pivot_break'),
    (r'kesiş|cross|çapraz', 'ma_cross'),
    (r'ema|sma|hareketli ortalama', 'ma_pullback'),
]


def desc_of(title):
    return title.split('—')[-1].strip()


def first_int(text, default=None, lo=1, hi=500):
    m = re.search(r'\b(\d+)\b', text)
    if m:
        v = int(m.group(1))
        if lo <= v <= hi:
            return v
    return default


def tf_from_text(title, body):
    found = re.findall(r'\b(M1|M5|M15|M30|H1|H4|D1|W1)\b', title)
    if found:
        k = found[-1]
    else:
        m = re.search(r'(?:olay|sinyal|kapanış|tetik|giriş)[^.]{0,100}?\b(M1|M5|M15|M30|H1|H4|D1|W1)\b', body)
        if m:
            k = m.group(1)
        else:
            found2 = re.findall(r'\b(M1|M5|M15|M30|H1|H4|D1|W1)\b', title + ' ' + body[:400])
            if not found2:
                return '1d'
            k = max(set(found2), key=found2.count)
    return {'M1': '5m', 'M5': '5m', 'M15': '15m', 'M30': '15m', 'H1': '1h',
            'H4': '4h', 'D1': '1d', 'W1': '1w'}[k]


def two_periods(text, default=(20, 50)):
    pairs = re.findall(r'\b(?:EMA|SMA|LWMA|WMA|SMMA)\s*[\(\[]?\s*(\d+)\s*[\)\]]?\s*[/\-–]\s*(\d+)', text, re.I)
    if pairs:
        a, b = int(pairs[0][0]), int(pairs[0][1])
    else:
        vals = [int(x) for x in re.findall(r'\b(?:EMA|SMA|LWMA|WMA|SMMA)\s*[\(\[]?\s*(\d+)\b', text, re.I)]
        vals = list(dict.fromkeys(vals))
        if len(vals) >= 2:
            a, b = vals[0], vals[1]
        elif len(vals) == 1:
            a, b = vals[0], default[1]
        else:
            return default
    return min(a, b), max(a, b)


def rsi_period(text, default=14):
    m = re.search(r'RSI\s*[\(\[]\s*(\d{1,2})\s*[\)\]]', text, re.I)
    if m:
        v = int(m.group(1))
        if 2 <= v <= 50:
            return v
    m = re.search(r'RSI\s*(\d{1,2})(?!\s*/)', text, re.I)
    if m:
        v = int(m.group(1))
        if 2 <= v <= 50:
            return v
    return default


def bb_params(text):
    m = re.search(r'BB\s*[\(\[]\s*(\d{1,3})\s*[;,\s]\s*(\d+(?:[.,]\d+)?)', text, re.I)
    if m:
        return int(m.group(1)), float(m.group(2).replace(',', '.'))
    return 20, 2.0


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
    return {'1d': 14, '1w': 12, '4h': 30, '1h': 48, '15m': 32, '5m': 48}.get(tf, 14)


def pick_family(title, body):
    tl = title.lower()
    for pat, fam in TITLE_RULES:
        if re.search(pat, tl):
            return fam
    bl = body.lower()
    for pat, fam in BODY_RULES:
        if re.search(pat, bl):
            return fam
    return None


def make(i, r):
    title, body = r['title'], r['body']
    low = (title + ' ' + body).lower()
    tl = title.lower()
    head = body[:220].lower()
    for kw, reason in HARD_EXCLUDE:
        k = kw.lower()
        if k in tl:
            return {'idx': i, 'batch': r['batch'], 'sid': r['id'], 'title': title,
                    'status': 'excluded', 'reason': reason}
        # body notes only count near the start, where the author states the decision
        if k in head and k in ('alınmaz', 'ertelendi', 'ertelenen', 'eklenmez',
                               'uygun değil', 'veri koşullu', 'sinyal değil',
                               'strateji değil', 'karar:'):
            return {'idx': i, 'batch': r['batch'], 'sid': r['id'], 'title': title,
                    'status': 'excluded', 'reason': reason}
    for kw in ASSET_HARD:
        k = kw.lower()
        if k in tl or k in head:
            return {'idx': i, 'batch': r['batch'], 'sid': r['id'], 'title': title,
                    'status': 'excluded', 'reason': f'Gerekli varlık/veri türü yok: {kw}.'}
    if ('çıkış' in title.lower() or 'exit' in title.lower()) and ('giriş' not in title.lower()):
        return {'idx': i, 'batch': r['batch'], 'sid': r['id'], 'title': title,
                'status': 'excluded', 'reason': 'Çıkış/pozisyon varyantı; bağımsız giriş kuralı değil.'}
    fam = pick_family(title, body)
    if fam is None:
        return {'idx': i, 'batch': r['batch'], 'sid': r['id'], 'title': title,
                'status': 'excluded', 'reason': 'Mekanik giriş kuralı otomatik eşleştirilemedi.'}
    tf = tf_from_text(title, body)
    desc = desc_of(title)
    stop = get_stop(body)
    time = get_time(body, tf)
    fast, slow = two_periods(desc + ' ' + body, (20, 50))
    long_only = ('yalnız long' in low or 'sadece al' in low or 'long-only' in low)
    short = ('short' in low or 'satış' in low or 'simetrik' in low)
    try:
        if fam == 'ma_cross':
            sp = F.ma_cross(i, tf, fast, slow, 200, 'ema', stop, time, True, long_only, short)
        elif fam == 'ma_pullback':
            sp = F.ma_pullback(i, tf, fast, slow, fast, 5, stop, time, long_only, short)
        elif fam == 'donchian_break':
            n = first_int(desc, None, 3, 200) or first_int(body[:200], 20, 3, 200)
            sp = F.donchian_break(i, tf, n, 0, 0, 0, stop, time, long_only, short)
        elif fam == 'range_break':
            n = first_int(desc, None, 3, 200) or first_int(body[:200], 20, 3, 200)
            sp = F.range_break(i, tf, n, 4.0, 0, stop, time, long_only, short)
        elif fam == 'pivot_break':
            sp = F.pivot_break(i, tf, 2, 2, min(fast, 50), stop, time, long_only, short)
        elif fam == 'bb':
            n, k = bb_params(desc + ' ' + body)
            if any(k2 in low for k2 in ['kırılım', 'breakout', 'sıkış', 'daral', 'açıl', 'bant dışı']):
                sp = F.bb_break(i, tf, n, k, 200, stop, time, long_only, short)
            else:
                sp = F.bb_reversion(i, tf, n, k, 14, 30, 70, 0, stop, time, long_only, short)
        elif fam == 'rsi':
            n = rsi_period(desc + ' ' + body)
            if any(k2 in low for k2 in ['60/40', '50 rejim', 'momentum', 'trend', '50 üstü', '50 üzeri']):
                sp = F.rsi_momentum(i, tf, n, 50, stop, time, long_only, short)
            else:
                sp = F.rsi_reversion(i, tf, n, 30, 70, 50, 0, stop, time, long_only, short)
        elif fam == 'macd':
            if 'histogram' in low or 'sıfır geçiş' in low or 'zero' in low:
                sp = F.macd_hist(i, tf, 12, 26, 9, stop, time, long_only, short)
            else:
                sp = F.macd_cross(i, tf, 12, 26, 9, False, stop, time, long_only, short)
        elif fam == 'stoch':
            sp = F.stoch(i, tf, 14, 3, 3, 20, 80, stop, time, long_only, short)
        elif fam == 'ichimoku':
            if 'tenkan' in low and 'kijun' in low and 'bulut kırılım' not in low:
                sp = F.ichimoku_tk(i, tf, True, stop, time, long_only, short)
            else:
                sp = F.ichimoku_cloud(i, tf, stop, time, long_only, short)
        elif fam == 'supertrend':
            sp = F.supertrend_flip(i, tf, 10, 3.0, stop, time, long_only, short)
        elif fam == 'keltner_rev':
            sp = F.keltner_rev(i, tf, 20, 1.5, 5, 30, 70, stop, time, long_only, short)
        elif fam == 'cci_rev':
            sp = F.cci_rev(i, tf, 20, -200, 200, 0, stop, time, long_only, short)
        elif fam == 'vwap':
            if any(k2 in low for k2 in ['kırılım', 'break', 'üstü', 'geçiş']):
                sp = F.vwap_break(i, tf, stop, time, long_only, short)
            else:
                sp = F.vwap_rev(i, tf, 2.0, stop, time, long_only, short)
        elif fam == 'double_pattern':
            sp = F.double_pattern(i, tf, 10, 0.5, stop, time, long_only, short)
        elif fam == 'fib_retrace':
            sp = F.fib_retrace(i, tf, 2, 0.5, 0.618, 200, stop, time, long_only, short)
        elif fam == 'candle_pattern':
            kind = 'engulf' if ('yutan' in low or 'engulf' in low) else ('inside' if ('iç bar' in low or 'inside' in low) else 'pin')
            sp = F.candle_pattern(i, tf, kind, 200 if 'trend' in low else 0, stop, time, long_only, short)
        elif fam == 'session_level':
            mode = 'failed' if any(k2 in low for k2 in ['başarısız', 'sahte', 'süpür', 'geri kapan', 'tuzak']) else 'break'
            sp = F.session_level(i, tf, mode, stop, time, long_only, short)
        elif fam == 'adx':
            sp = F.donchian_break(i, tf, 20, 0, 20, 0, stop, time, long_only, short)
        elif fam == 'nr_break':
            n = 7 if 'nr7' in low or 'nr 7' in low else 4
            sp = F.nr_break(i, tf, n, stop, time, long_only, short)
        elif fam == 'smma_channel':
            sp = F.smma_channel(i, tf, 55, 55, 5, stop, time, long_only, short)
        elif fam == 'ha_reversal':
            sp = F.ha_reversal(i, tf, stop, time, long_only, short)
        elif fam == 'td_setup':
            sp = F.td_setup(i, tf, 9, stop, time, long_only, short)
        elif fam == 'cpr_break':
            sp = F.cpr_break(i, tf, stop, time, long_only, short)
        else:
            raise ValueError(f'unknown {fam}')
    except Exception as e:
        return {'idx': i, 'batch': r['batch'], 'sid': r['id'], 'title': title,
                'status': 'excluded', 'reason': f'Spec üretim hatası: {e}'}
    sp.update(batch=r['batch'], sid=r['id'], title=title, status='tested', family=fam,
              mapping='auto', confidence='medium', summary=re.sub(r'\s+', ' ', body)[:280],
              params=dict(tf=tf, fast=fast, slow=slow, stop=stop, time=time))
    return sp


specs = [make(i, r) for i, r in enumerate(rows)]
for s in specs:
    if s['idx'] in (47, 114, 134):
        s['status'] = 'excluded'
        s['reason'] = 'Başlık bağımsız strateji değil (erteleme/karar/özet).'
json.dump(specs, open(os.path.join(ROOT, 'backtest', 'specs_auto3.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
from collections import Counter
print(Counter(s['status'] for s in specs))
print(Counter(s.get('family') for s in specs if s['status'] == 'tested'))
