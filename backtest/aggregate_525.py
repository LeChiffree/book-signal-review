import os
import sys

BT = r'D:\Paper_ML_BSH\analysis\book_signal_review\backtest'
sys.path.insert(0, BT)
import bookbt525

bookbt525.install()
os.environ['BOOKBT_RESULTS'] = 'results_525'
os.environ['BOOKBT_N_SYMBOLS'] = '525'

import aggregate

aggregate.main()
