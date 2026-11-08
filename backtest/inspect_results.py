import pandas as pd, glob, os, json
p = r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest\results\summary'
dfs = []
for f in glob.glob(os.path.join(p, '*.parquet')):
    dfs.append(pd.read_parquet(f))
df = pd.concat(dfs, ignore_index=True)
print(df.shape)
print(df[['sid', 'tf', 'family', 'n', 'avg_net', 'portfolio_net', 'win_rate', 'max_dd', 'symbol']].sort_values('portfolio_net', ascending=False).head(25).to_string(index=False))
print('\nby trades')
print(df[['sid', 'tf', 'family', 'n', 'avg_net', 'portfolio_net', 'win_rate', 'symbol']].sort_values('n', ascending=False).head(15).to_string(index=False))
print('\nsummary stats')
print(df[['n', 'avg_net', 'portfolio_net', 'win_rate', 'max_dd']].describe().to_string())
print('\nby tf')
print(df.groupby('tf').agg(n=('n', 'sum'), avg=('avg_net', 'mean'), med=('portfolio_net', 'median'), syms=('symbol', 'nunique')).to_string())
