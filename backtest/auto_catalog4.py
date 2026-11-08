import json, re, os, sys
sys.path.insert(0, r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest')
import families as F

ROOT = r'D:\Paper_ML_BSH\analysis\book_signal_review'
rows = json.load(open(os.path.join(ROOT, 'backtest', 'sections.json'), encoding='utf-8'))

# Titles/heads that make a section non-testable with our data or out of scope.
TITLE_BLOCK = [
    (r'opsiyon|\boption\b', 'Opsiyon uygulaması; vadeli OHLCV ile test edilemez.'),
    (r'portföy|rotasyon|sepet|göreli güç|relative strength|endeks|sektör|breadth|genişlik',
     'Portföy/kesitsel kural; tek enstrüman girişi değil.'),
    (r'pozisyon büyüklüğü|pozisyon yönetimi|risk yönetimi|risk karşı|kaldıraç',
     'Pozisyon/risk kuralı; giriş sinyali değil.'),
    (r'filtre deneyi|ablation|karşılaştırma|test sırası|özellik adayı',
     'Ablasyon/karşılaştırma; bağımsız giriş değil.'),
    (r'sinyal değil|strateji değil|karar:|ertelenen|ertelenen/tekrar|özet',
     'Başlık bağımsız strateji değil.'),
    (r'çıkış varyant|çıkış rejimi|exit|runner|iz süren|trailing|hedef varyant',
     'Çıkış/pozisyon varyantı; bağımsız giriş kuralı değil.'),
    (r'\bSPY\b|\bQQQ\b|Nifty|BankNifty|ABD hisse|hisse evreni|delist|\bFX\b|EURUSD|GBPUSD|USDJPY',
     'Gerekli varlık/veri türü yok (hisse/FX/endeks).'),
    (r'\bNFP\b|\bFOMC\b|earnings|kazanç açıklama|haber verisi|makro',
     'Haber/makro verisi gerekli.'),
    (r'\bSMC\b|order block|order-block|FVG|fair value gap|Elliott|dalga sayım|harmonic|XABCD|Wyckoff|TD Sequential|TD9|TD 9',
     'Tanımı öznel/çok parçalı; otomatik proxy güvenilir değil.'),
    (r'ayrışma|divergence', 'Ayrışma/sapma tanımı nedensel pivot gerektiriyor; otomatik proxy güvenilir değil.'),
    (r'boşluk|gap', 'Kripto 7/24 verisinde anlamlı seans boşluğu yok.'),
]

# Explicit indicator families. These get higher confidence.
EXPLICIT_FAMILIES = {
    'supertrend', 'ichimoku', 'fib_retrace', 'vwap', 'macd', 'smma_channel',
    'bb', 'keltner_rev', 'stoch', 'cci_rev', 'double_pattern', 'nr_break',
    'td_setup', 'ha_reversal', 'ma_cross', 'rsi', 'adx', 'donchian_break',
    'cpr_break'
}

TITLE_RULES = [
    (r'supertrend', 'supertrend'),
    (r'ichimoku|bulut|tenkan|kijun', 'ichimoku'),
    (r'fibonacci|\bfib\b|altın bölge|altin bolge', 'fib_retrace'),
    (r'vwap', 'vwap'),
    (r'macd', 'macd'),
    (r'histogram', 'macd'),
    (r'smma', 'smma_channel'),
    (r'bollinger|\bbb\b', 'bb'),
    (r'keltner', 'keltner_rev'),
    (r'stokastik|stochastic|\bstoch\b', 'stoch'),
    (r'williams\s*%?r', 'williams_rev'),
    (r'\bcci\b', 'cci_rev'),
    (r'çift dip|çift tepe|ikili dip|ikili tepe|double top|double bottom|üçlü dip|üçlü tepe|baş-omuz|omuz-baş', 'double_pattern'),
    (r'nr\s*4|nr\s*7|nr4|nr7', 'nr_break'),
    (r'heikin|ha dönüş|ha renk', 'ha_reversal'),
    (r'cpr', 'cpr_break'),
    (r'yutan|engulf|çekiç|hammer|pin bar|doji|iç bar|inside bar|harami|kayan yıldız|shooting star|marubozu|fitil|reddedilme|ters mum', 'candle_pattern'),
    (r'kesiş|cross|çapraz|geçiş', 'ma_cross'),
    (r'\brsi\b', 'rsi'),
    (r'adx', 'adx'),
    (r'donchian|dışına taşma|dışına çıkma|kanal|channel', 'donchian_break'),
    (r'pivot seviye|önceki gün|önceki hafta|seans|session|gün yüksek|gün düşük|hafta yüksek|hafta düşük|açılış aralığı|açılış aralı',
     'session_level'),
    (r'kutu|dar aralık|sıkışma|sıkış|range|konsolidasyon|dar bant|üçgen|bayrak|flama|triangle|flag|pennant', 'range_break'),
    (r'pivot|swing|fraktal|yapı kırılım|destek|direnç|seviye|trend çizgisi|trendline', 'pivot_break'),
    (r'geri çekilme|pullback|toparlanma|tepki', 'ma_pullback'),
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


def tf_from_text(title, body):
    tfs = list(re.finditer(r'\b(M1|M5|M15|M30|H1|H4|D1|W1)\b', title))
    if tfs:
        first = tfs[0]
        after = title[first.end():first.end() + 18].lower()
        if len(tfs) > 1 and any(k in after for k in ['rejim', 'filtre']):
            k = tfs[1].group(1)
        else:
            k = first.group(1)
    else:
        m = re.search(r'(?:olay|sinyal|kapanış|tetik|giriş)[^.]{0,100}?\b(M1|M5|M15|M30|H1|H4|D1|W1)\b', body)
        if m:
            k = m.group(1)
        else:
            found2 = re.findall(r'\b(M1|M5|M15|M30|H1|H4|D1|W1)\b', title + ' ' + body[:400])
            if not found2:
                return '1d'
            k = max(set(found2), key=found2.count)
    if 'haftalık' in title.lower() and 'W1' not in title:
        return '1w'
    return {'M1': '5m', 'M5': '5m', 'M15': '15m', 'M30': '15m', 'H1': '1h',
            'H4': '4h', 'D1': '1d', 'W1': '1w'}[k]


def n_bars(desc, body, default=20):
    m = re.search(r'(\d+)\s*(?:bar|gün|gun|günlük)', desc + ' ' + body[:260], re.I)
    if m:
        v = int(m.group(1))
        if 3 <= v <= 200:
            return v
    return default


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
        if 2 <= v <= 10:
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
    tl = title.lower()
    head = body[:240].lower()
    for pat, reason in TITLE_BLOCK:
        if re.search(pat, tl, re.I):
            return {'idx': i, 'batch': r['batch'], 'sid': r['id'], 'title': title,
                    'status': 'excluded', 'reason': reason}
    # explicit exclusions stated at the top of the body
    for kw, reason in [('geri teste alınmaz', 'Yazar ilk backteste almamış.'),
                       ('ilk backtestte ertelenir', 'Yazar tarafından ertelenmiş.'),
                       ('kataloğa eklenmez', 'Yazar kataloğa eklememiş.'),
                       ('uygun değil', 'Kaynak kuralı kripto vadeli verisine uygun değil.'),
                       ('veri koşullu', 'Gerekli veri yok.')]:
        if kw in head:
            return {'idx': i, 'batch': r['batch'], 'sid': r['id'], 'title': title,
                    'status': 'excluded', 'reason': reason}
    fam = pick_family(title, body)
    if fam is None:
        return {'idx': i, 'batch': r['batch'], 'sid': r['id'], 'title': title,
                'status': 'excluded', 'reason': 'Mekanik giriş kuralı otomatik eşleştirilemedi.'}
    tf = tf_from_text(title, body)
    desc = desc_of(title)
    stop = get_stop(body)
    time = get_time(body, tf)
    fast, slow = two_periods(desc + ' ' + body, (20, 50))
    long_only = any(k in tl for k in ['yalnız long', 'sadece al', 'long-only', 'yükseliş trendi'])
    short_only = any(k in tl for k in ['short', 'aşırı alım', 'düşüş trendi']) and 'simetrik' not in tl
    both = ('short' in (title + body).lower() or 'satış' in (title + body).lower() or
            'simetrik' in (title + body).lower())
    short = both and not long_only
    if long_only:
        short = False
    try:
        if fam == 'ma_cross':
            sp = F.ma_cross(i, tf, fast, slow, 200, 'ema', stop, time, True, long_only, short)
        elif fam == 'ma_pullback':
            sp = F.ma_pullback(i, tf, fast, slow, fast, 5, stop, time, long_only, short)
        elif fam == 'donchian_break':
            sp = F.donchian_break(i, tf, n_bars(desc, body), 0, 0, 0, stop, time, long_only, short)
        elif fam == 'range_break':
            sp = F.range_break(i, tf, n_bars(desc, body), 4.0, 0, stop, time, long_only, short)
        elif fam == 'pivot_break':
            sp = F.pivot_break(i, tf, 2, 2, min(fast, 50), stop, time, long_only, short)
        elif fam == 'bb':
            n, k = bb_params(desc + ' ' + body)
            if any(k2 in tl for k2 in ['kırılım', 'breakout', 'sıkış', 'daral', 'açıl', 'bant dışı']):
                sp = F.bb_break(i, tf, n, k, 200, stop, time, long_only, short)
            else:
                rn = rsi_period(desc + ' ' + body, 14)
                sp = F.bb_reversion(i, tf, n, k, rn, 30, 70, 0, stop, time, long_only, short)
        elif fam == 'rsi':
            n = rsi_period(desc + ' ' + body)
            if n <= 3:
                # RSI(2) continuation: long while overbought, short while oversold
                L = f'rsi(close,{n})>90'
                Sh = f'rsi(close,{n})<10'
                sp = F.S(i, tf, L, Sh, stop=stop, time=time,
                         exit_long=f'rsi(close,{n})<50', exit_short=f'rsi(close,{n})>50')
            elif any(k2 in tl for k2 in ['60/40', '50 rejim', 'momentum', 'trend', '50 üstü', '50 üzeri', 'geri çekilme', 'toparlanma', 'pullback']):
                sp = F.rsi_momentum(i, tf, n, 50, stop, time, long_only, short)
            else:
                sp = F.rsi_reversion(i, tf, n, 30, 70, 50, 0, stop, time, long_only, short)
        elif fam == 'macd':
            if 'histogram' in tl or 'sıfır geçiş' in tl or 'zero' in tl:
                sp = F.macd_hist(i, tf, 12, 26, 9, stop, time, long_only, short)
            else:
                sp = F.macd_cross(i, tf, 12, 26, 9, False, stop, time, long_only, short)
        elif fam == 'stoch':
            sp = F.stoch(i, tf, 14, 3, 3, 20, 80, stop, time, long_only, short)
        elif fam == 'ichimoku':
            if 'tenkan' in tl and 'kijun' in tl and 'bulut kırılım' not in tl:
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
            if any(k2 in tl for k2 in ['kırılım', 'break', 'üstü', 'geçiş']):
                sp = F.vwap_break(i, tf, stop, time, long_only, short)
            else:
                sp = F.vwap_rev(i, tf, 2.0, stop, time, long_only, short)
        elif fam == 'double_pattern':
            sp = F.double_pattern(i, tf, 10, 0.5, stop, time, long_only, short)
        elif fam == 'fib_retrace':
            sp = F.fib_retrace(i, tf, 2, 0.5, 0.618, 200, stop, time, long_only, short)
        elif fam == 'candle_pattern':
            kind = 'engulf' if ('yutan' in tl or 'engulf' in tl) else ('inside' if ('iç bar' in tl or 'inside' in tl) else 'pin')
            sp = F.candle_pattern(i, tf, kind, 200 if 'trend' in tl else 0, stop, time, long_only, short)
        elif fam == 'session_level':
            mode = 'failed' if any(k2 in tl for k2 in ['başarısız', 'sahte', 'süpür', 'geri kapan', 'tuzak']) else 'break'
            sp = F.session_level(i, tf, mode, stop, time, long_only, short)
        elif fam == 'adx':
            sp = F.adx_break(i, tf, n_bars(desc, body), 20, stop, time, long_only, short)
        elif fam == 'nr_break':
            n = 7 if 'nr7' in tl or 'nr 7' in tl else 4
            sp = F.nr_break(i, tf, n, stop, time, long_only, short)
        elif fam == 'smma_channel':
            sp = F.smma_channel(i, tf, 55, 55, 5, stop, time, long_only, short)
        elif fam == 'ha_reversal':
            sp = F.ha_reversal(i, tf, stop, time, long_only, short)
        elif fam == 'td_setup':
            sp = F.td_setup(i, tf, 9, stop, time, long_only, short)
        elif fam == 'cpr_break':
            sp = F.cpr_break(i, tf, stop, time, long_only, short)
        elif fam == 'williams_rev':
            L = '(ref(williams_r(high,low,close,14),1)<-80)&(williams_r(high,low,close,14)>-80)'
            Sh = '(ref(williams_r(high,low,close,14),1)>-20)&(williams_r(high,low,close,14)<-20)'
            sp = F.S(i, tf, L, Sh, stop=stop, time=time)
        else:
            raise ValueError(f'unknown {fam}')
    except Exception as e:
        return {'idx': i, 'batch': r['batch'], 'sid': r['id'], 'title': title,
                'status': 'excluded', 'reason': f'Spec üretim hatası: {e}'}
    # direction override
    if short_only:
        sp['entry_long'] = None
        sp['direction'] = 'short'
    quality = 'high' if fam in EXPLICIT_FAMILIES else 'medium'
    if fam in ('range_break', 'ma_pullback', 'pivot_break', 'session_level', 'candle_pattern') and not re.search(r'\d', desc):
        quality = 'low'
    sp.update(batch=r['batch'], sid=r['id'], title=title, status='tested', family=fam,
              mapping='auto', confidence=quality, summary=re.sub(r'\s+', ' ', body)[:280],
              params=dict(tf=tf, fast=fast, slow=slow, stop=stop, time=time))
    return sp


specs = [make(i, r) for i, r in enumerate(rows)]
json.dump(specs, open(os.path.join(ROOT, 'backtest', 'specs_final.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
from collections import Counter
print(Counter(s['status'] for s in specs))
print(Counter(s.get('confidence') for s in specs if s['status'] == 'tested'))
print(Counter(s.get('family') for s in specs if s['status'] == 'tested'))
