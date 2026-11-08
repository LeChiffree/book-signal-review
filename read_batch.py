import sys
from pathlib import Path
from pypdf import PdfReader

root = Path(r"D:\Paper_ML_BSH\Drive_PDF\PDFler")
batch = sys.argv[1] if len(sys.argv) > 1 else "001"
out = Path(r"D:\Paper_ML_BSH\analysis\book_signal_review") / f"batch_{batch}"
out.mkdir(parents=True, exist_ok=True)
books_by_batch = {
    "001": [
        ("ADX Göstergesi - Puneet Jain", "01_adx.txt"),
        ("Bollinger Bantları - İşe Yarayan Trading Stratejileri", "02_bollinger.txt"),
        ("20 EMA Stratejisi - Jayesh Shah", "03_ema20.txt"),
    ],
    "002": [
        ("MACD Uzmanlığı - Lalit Mohanty", "01_macd.txt"),
        ("RSI İndikatöründe Ustalaşmak - Lalit Mohanty", "02_rsi.txt"),
        ("Başarılı Koparma Ticareti - Sinisa Persic", "03_breakout.txt"),
    ],
    "003": [
        ("Mum Formasyonları İçin Dürüst Bir Rehber", "01_candles.txt"),
        ("Hacim Fiyat Analizi - Nasıl Yapılacağına Dair Nihai Yeni Başlayanlar", "02_volume.txt"),
        ("Grafik Formasyonları Uzmanlığı - Lalit Mohanty", "03_patterns.txt"),
    ],
    "004": [
        ("Ichimoku Sisteminin Kazançlı Sinyalleri ile Nasıl Trade Yapılır", "01_ichimoku.txt"),
        ("Gelişmiş Kripto Trading Stratejileri", "02_crypto.txt"),
        ("Kanıtlanmış Trading Stratejisi - Trend Trading", "03_trend.txt"),
    ],
    "005": [
        ("Swing Yüksekleri ve Swing Düşüklerini Kullanarak Pazarın", "01_swings.txt"),
        ("Arz ve Talep Bölgeleri - Fahmi Lamar", "02_supply_demand.txt"),
        ("Piyasa Yapısı ve Order Block Sanatında Ustalaşmak", "03_order_block.txt"),
    ],
    "006": [
        ("5 Adımlı Swing Trading Planı - Swing Trade Pro 2.0", "01_swing_plan.txt"),
        ("9 Kazançlı Trading Stratejisi - Roman Sadowski", "02_nine_strategies.txt"),
        ("RSI Swing Trading Stratejisi - TMP", "03_rsi_swing.txt"),
    ],
    "007": [
        ("5 SMA 5 RSI Forex Trading Stratejisi", "01_sma_rsi.txt"),
        ("Forex Momentum Stratejisi", "02_momentum.txt"),
        ("Gelişmiş Mum ve Ichimoku Stratejileri", "03_candle_ichimoku.txt"),
    ],
    "008": [
        ("RSI Pro Scalping Stratejisi", "01_rsi_pro_scalping.txt"),
        ("Forex Bounce Trading Stratejisi", "02_forex_bounce.txt"),
        ("Kazandıran Stratejiler - TradersGPS", "03_traders_gps.txt"),
    ],
    "009": [
        ("Golden Strateji - Russ Horn", "01_golden.txt"),
        ("H4 EMA5 GBP Stratejisi", "02_h4_ema5.txt"),
        ("Gelişmiş Sniper Trading Stratejisi", "03_sniper.txt"),
    ],
    "010": [
        ("Swing Trading Leandro Yöntemi", "01_leandro.txt"),
        ("Gann Trading Stratejisi - Trading Strategy Guides", "02_gann.txt"),
        ("Forex Scalping Stratejisi (28 sayfa)", "03_forex_scalping.txt"),
    ],
    "011": [
        ("G7 Forex Sistemi - Forex Science", "01_g7.txt"),
        ("Karar Noktaları - Smart Trader", "02_decision_points.txt"),
        ("Forex Trading Risk Yönetimi Sistemleri - Roulette Trader", "03_risk_systems.txt"),
    ],
    "012": [
        ("Mükemmel Trade Oluşturmak - Oli Hille", "01_perfect_trade.txt"),
        ("Pivotlarla Günlük Trading ve Price Action", "02_pivots_price_action.txt"),
        ("Günde 20 Pips Stratejisi", "03_twenty_pips.txt"),
    ],
    "013": [
        ("13 Swing Trading Stratejisi - Pankaj Ladha", "01_thirteen_swing.txt"),
        ("15 Price Action Stratejisi - Mr. Ankya", "02_fifteen_price_action.txt"),
        ("Basit Strateji - Güçlü Bir Günlük Alım Satım Stratejisi", "03_simple_strategy.txt"),
    ],
    "014": [
        ("3W Sistemi - Sumit Das", "01_three_w.txt"),
        ("BBMA Trading Stratejisi - John Ray", "02_bbma.txt"),
        ("Akıl Almaz Kazançlı Mekanik Günlük Trading Stratejileri", "03_mechanical_day_trading.txt"),
    ],
    "015": [
        ("100 Pips Kur ve Unut Stratejisi", "01_hundred_pips.txt"),
        ("AK47 Scalping Stratejisi", "02_ak47.txt"),
        ("6 Basit Forex Trading Stratejisi", "03_six_forex.txt"),
    ],
    "016": [
        ("Adım Adım Ichimoku - Fabio Monterrey Albizu", "01_ichimoku_step.txt"),
        ("ABCD Formasyonu - Sundeep Bilkhu", "02_abcd.txt"),
        ("Bayraklar ve Flamalar ile Trade - Vladimir Ribakov", "03_flags_pennants.txt"),
    ],
    "017": [
        ("4 Saatlik Grafik Kullanarak Swing Trading", "01_h4_heikin_ashi.txt"),
        ("15 Dakikalık Turbo Forex Trading Kursu", "02_m15_turbo.txt"),
        ("30 Dakikalık Hisse Senedi Traderi", "03_m30_stock_trader.txt"),
    ],
    "018": [
        ("90 Dakikada Sadeleştirilmiş Formasyon Trading Sırları", "01_pattern_secrets.txt"),
        ("Basitleştirilmiş Destek ve Direnç Analizi", "02_support_resistance.txt"),
        ("Basitleştirilmiş Price Action - Frank Miller", "03_price_action.txt"),
    ],
    "019": [
        ("Price Action Rehberi - Think Markets", "01_think_markets.txt"),
        ("Price Action Rehberi - Rayner Teo", "02_rayner_teo.txt"),
        ("Price Action Rehberi - Atanas Matov", "03_atanas_matov.txt"),
    ],
    "020": [
        ("Trendline Stratejisi - Kelvin Lee", "01_trendline_kelvin.txt"),
        ("Stoploss Stratejisi", "02_stoploss.txt"),
        ("Triple S Stratejisi", "03_triple_s.txt"),
    ],
    "021": [
        ("Price Action Scalping Stratejisi - Christopher", "01_christopher_scalping.txt"),
        ("Londra Koparma Stratejisi", "02_london_breakout.txt"),
        ("James16 Trading Stratejisi", "03_james16.txt"),
    ],
    "022": [
        ("Fibonacci Oranları Bir Yatırım Stratejisine Değer Katabilir Mi", "01_fibonacci_thesis.txt"),
        ("Trendline Stratejisi (114 sayfa)", "02_trendline_114.txt"),
        ("EMA14 ve EMA50 Scalping Stratejisi", "03_ema14_50.txt"),
    ],
    "023": [
        ("Forex - Price Action Rehberi", "01_forex_price_action.txt"),
        ("Price Action Scalping - Bob Volman", "02_volman_scalping.txt"),
        ("Hedging Stratejisi - John Carricaburu", "03_hedging.txt"),
    ],
    "024": [
        ("Kripto Para Alım Satımı ve Yatırımının Teknik Analizi - Osbert Ferguson", "01_crypto_ta_ferguson.txt"),
        ("Momentum Trade - Laurentiu Damir", "02_momentum_damir.txt"),
        ("Trend Traderinin El Kitabı - Güçlü Trend Ticareti - James Muranno", "03_trend_muranno.txt"),
    ],
    "025": [
        ("1 Dakikalık Forex Scalping Stratejisi - Trevor Candle", "01_m1_scalping_trevor.txt"),
        ("20 Trading Stratejisi (28 sayfa)", "02_twenty_strategies.txt"),
        ("100_den Fazla Alım Satım ve Yatırım Stratejisi", "03_hundred_strategies.txt"),
    ],
    "026": [
        ("14 Mum Kalıbı - P. Arul Pandi", "01_fourteen_candles.txt"),
        ("2023_te Etkili Swing Trading Stratejileri - Dennis Sharpe", "02_swing_sharpe.txt"),
        ("123 Grafik Formasyonu - Sunil Mangwani", "03_patterns_mangwani.txt"),
    ],
    "027": [
        ("17 Forex Trading Stratejisi - Thomas Carter", "01_seventeen_forex.txt"),
        ("20 Forex Stratejisi - Thomas Carter", "02_twenty_forex.txt"),
        ("2023 ICT Mentorship GEMS", "03_ict_gems.txt"),
    ],
    "028": [
        ("7 Kazandıran Strateji - Grace Cheng", "01_seven_winning_cheng.txt"),
        ("3 Swing Trading Örneği", "02_three_swing_examples.txt"),
        ("7 RSI Trade Stratejisi", "03_seven_rsi.txt"),
    ],
    "029": [
        ("30 Günde Piyasa Ustalığı - Jacob Bernstein", "01_market_mastery_bernstein.txt"),
        ("25 Trade Kuralı", "02_trade_rules.txt"),
        ("1 Saatte Profesyonel Bir Trader Gibi Forex Piyasasında Nasıl Trade Yapılır", "03_one_hour_forex.txt"),
    ],
    "030": [
        ("20 Dakikalık Trader Olmanın Yolları", "01_twenty_minute_trader.txt"),
        ("5 Dakikalık Scalp Stratejisi", "02_five_minute_scalp.txt"),
        ("15 Dakikada Forex Kursu", "03_fifteen_minute_forex.txt"),
    ],
    "031": [
        ("DeMark Göstergesi - Jason Perl", "01_demark_perl.txt"),
        ("EMA_ların Gücü - Soulz", "02_ema_power_soulz.txt"),
        ("RSI 80-20 Trading Stratejisi", "03_rsi_80_20.txt"),
    ],
    "032": [
        ("RSI İndikatörü +5 Sistem Trading Stratejisi", "01_rsi_five_systems.txt"),
        ("RSI Ölçeklendirme Stratejisi - Paul Dean", "02_rsi_scaling_dean.txt"),
        ("RSI Uyumsuzlukları - Empreror BTC", "03_rsi_divergence_emperor.txt"),
    ],
    "033": [
        ("ATR Uzmanlığı - Aaron Lee Johnson", "01_atr_mastery.txt"),
        ("Heiken Ashi ve Stokastik Göstergeyle Swing Trading", "02_heikin_stoch.txt"),
        ("Dual Momentum Trend Trading - Lee Tang", "03_dual_momentum.txt"),
    ],
    "034": [
        ("Darvas Box Trading - Jaynesh Kasliwal", "01_darvas_kasliwal.txt"),
        ("Breakout ve Pullback Trading Stratejileri - Michael Norman", "02_breakout_pullback_norman.txt"),
        ("VWAP Breakout Başarısızlığı Stratejisi - Varun Speak", "03_vwap_failed_breakout.txt"),
    ],
    "035": [
        ("Breakout Trading - Alton Swanson", "01_breakout_swanson.txt"),
        ("Trendin Tersine Dönüş Modelleri", "02_reversal_patterns.txt"),
        ("Destek ve Direnç Seviyesi Olarak TP ve SL Bulmak İçin Fibonacciyi Anlamak", "03_fibonacci_tp_sl.txt"),
    ],
    "036": [
        ("Koparma Ticareti - John Connors", "01_breakout_connors.txt"),
        ("Gerçek Destek ve Direnç (12 sayfa)", "02_true_support_resistance.txt"),
        ("Destek ve Dirençler - Investija", "03_support_resistance_investija.txt"),
    ],
    "037": [
        ("Breakout Trading Stratejisi - Mark K. White", "01_breakout_white.txt"),
        ("Destek ve Direnç Seviyelerinin Tespiti", "02_support_resistance_detection.txt"),
        ("Forex Piyasasında Konsolidasyon Breakout Sinyalleri", "03_consolidation_breakout.txt"),
    ],
    "038": [
        ("Trend Çizgileri - Albert Yang", "01_trendlines_yang.txt"),
        ("Destek Direnç Bölgeleriyle Günlük Trade - Laurentiu Damir", "02_zones_damir.txt"),
        ("Trend Kırılımı Strateji Rehberi", "03_trend_break_guide.txt"),
    ],
    "039": [
        ("Chaikin Para Akışı Göstergesi", "01_chaikin_money_flow.txt"),
        ("Volume Trading - Jayesh Shah", "02_volume_trading_shah.txt"),
        ("Hacim Fiyat Analizi - Nasıl Yapılacağına Dair Nihai", "03_volume_price_milton.txt"),
    ],
    "040": [
        ("Arz ve Talep - Saf Likidite Konsepti", "01_supply_demand_liquidity.txt"),
        ("Gelişmiş Likidite Tekniği - Elad Menda", "02_advanced_liquidity.txt"),
        ("Likidite - Trade with WorldBank", "03_liquidity_worldbank.txt"),
    ],
    "041": [
        ("Supertrend İndikatörü - Alpesh Pansheriya", "01_supertrend_pansheriya.txt"),
        ("Ichimoku Kazananları - Ahmed El Agouz", "02_ichimoku_winners.txt"),
        ("Bollinger Band Trading - Kazançlı Bir Trading Sistemi", "03_bollinger_wilson.txt"),
    ],
    "042": [
        ("Yeni Başlayanlar İçin Ichimoku - Gabor Kovacs", "01_ichimoku_kovacs.txt"),
        ("MACD Trend Takip Stratejisi (23 sayfa)", "02_macd_trend.txt"),
        ("Fibonacci Golden Zone Trading Stratejisi", "03_fibonacci_golden_zone.txt"),
    ],
    "043": [
        ("Kolay Para ile VWAP Trade Stratejisi", "01_vwap_easy_money.txt"),
        ("ADX İndikatörü - Learn Price Action", "02_adx_learn_price_action.txt"),
        ("Kazanan RSI Playbook - Hima Reddy", "03_rsi_playbook_reddy.txt"),
    ],
    "044": [
        ("Fibonacci Kanal Stratejisi - Trading Strategy Guides", "01_fibonacci_channel.txt"),
        ("Kanal Trading - Alton Swanson", "02_channel_swanson.txt"),
        ("RSI - Traderin Gizli Silahı - Erich Senft", "03_rsi_senft.txt"),
    ],
    "045": [
        ("VWAP Stratejisi - Terence V. Gronowski", "01_vwap_gronowski.txt"),
        ("Trende Karşı İşlem Yapmak - Heikin Ashi Trader", "02_countertrend_heikin_ashi.txt"),
        ("Heikin Ashi Trading Stratejisi - Roman Sadowski", "03_heikin_ashi_sadowski.txt"),
    ],
    "046": [
        ("Scalping Eğlencelidir - Heikin Ashi Trader", "01_scalping_fun.txt"),
        ("RSI - Göreceli Gün Endeksi - Alton Swanson", "02_rsi_swanson.txt"),
        ("Heikin Ashi Grafikleriyle Günlük Trade - Tim Haddock", "03_heikin_ashi_haddock_kapoor.txt"),
    ],
    "047": [
        ("Eğlenceli Scalping 2 - Heikin Ashi Trader", "01_scalping_fun_2.txt"),
        ("RSI - Alpesh Pansheriya", "02_rsi_pansheriya.txt"),
        ("Fibonacci Trend Çizgisi Strateji Rehberi", "03_fibonacci_trendline.txt"),
    ],
    "048": [
        ("RSI Sırları - Sudhir Dixit", "01_rsi_secrets_dixit.txt"),
        ("VWAP Uzmanlığı - Lalit Mohanty", "02_vwap_mastery_mohanty.txt"),
        ("Forex Momentum Stratejisi (23 sayfa)", "03_forex_momentum_23.txt"),
    ],
    "049": [
        ("Al ve Tut Stratejisini Yenen 5 Hareketli Ortalama Sinyali", "01_five_ma_signals.txt"),
        ("Akıllı Para Kavramıyla Price Action (41 sayfa)", "02_smc_price_action.txt"),
        ("Forex İçin Uygulamalı Pin Bar Trading", "03_pin_bar_thorpe.txt"),
    ],
    "050": [
        ("Inside Bar (15 sayfa)", "01_inside_bar.txt"),
        ("The Engulfing Trader - Timon Weller", "02_engulfing_weller.txt"),
        ("Koparma Ticareti - John Connors", "03_breakout_connors.txt"),
    ],
    "051": [
        ("Grafik Desenleriyle Strateji Oluşturma (58 sayfa)", "01_chart_pattern_strategy.txt"),
        ("Harmonik Desenler (10 sayfa)", "02_harmonic_patterns.txt"),
        ("Kokuşmuş İndikatörlere İhtiyacımız Yok - Kevin Baker", "03_no_indicators_baker.txt"),
    ],
    "052": [
        ("ICT Stratejisi (19 sayfa)", "01_ict_strategy.txt"),
        ("Mumların Dili (31 sayfa)", "02_language_of_candles.txt"),
        ("Hareketli Ortalamalarla Strateji Rehberi - John Person", "03_ma_strategy_person.txt"),
    ],
    "053": [
        ("GAP Trading - Jayesh Shah", "01_gap_trading_shah.txt"),
        ("Günde 50 Pips Stratejisi - Laurentiu Damir", "02_fifty_pips_damir.txt"),
        ("Teknik Analizde Ayak İzleri (11 sayfa)", "03_footprints.txt"),
    ],
    "054": [
        ("Günde 10 Pips Stratejisi - Haji Warithu", "01_ten_pips_warithu.txt"),
        ("Miracle Metot Trading Stratejisi (31 sayfa)", "02_miracle_method.txt"),
        ("Ticaret Sırları - Chame Quiroz", "03_trading_secrets_quiroz.txt"),
    ],
    "055": [
        ("Zaman ve Fiyat Teorisi (9 sayfa)", "01_time_price_theory.txt"),
        ("Trend Çizgisi Analizinin Gücünden Yararlanın", "02_trendline_power.txt"),
        ("Profesyoneller Gibi Trade Yapın - Jode Lebin", "03_trade_like_pros.txt"),
    ],
    "056": [
        ("Göreceli Güç Endeksi - Hima Reddy", "01_rsi_reddy.txt"),
        ("Forex Stratejisi - ST Kalıpları Trade Klavuzu", "02_st_patterns.txt"),
        ("Swing Trading - Piyasa Dalgalarında Sörf Yapmak", "03_swing_arps.txt"),
    ],
    "057": [
        ("Göreceli Güç Endeksi -RSI Göstergesi ile Ticaret", "01_rsi_trading.txt"),
        ("Elliott Dalga Prensibinin Temelleri", "02_elliott_foundations.txt"),
        ("Forex_te Bankaların Manipülasyonu", "03_bank_manipulation.txt"),
    ],
    "058": [
        ("Arz ve Talep Ticareti - Frank Luther", "01_supply_demand_luther.txt"),
        ("Gelişmiş Order Block Kılavuzu - James Jecool King", "02_advanced_ob_king.txt"),
        ("Kazançlı Mum Kalıpları - Matt Anderson", "03_candles_anderson.txt"),
    ],
    "059": [
        ("Üstün Trader Olmanın Yolu - Forexia", "01_superior_trader.txt"),
        ("Forex Rüyası - Christopher Lee", "02_forex_dream.txt"),
        ("Price Action El Kitabı (68 sayfa)", "03_price_action_handbook.txt"),
    ],
    "060": [
        ("H1 Stratejisi - Brian P.Anderson", "01_h1_anderson.txt"),
        ("Price Action Kalıpları - Ankya", "02_price_action_ankya.txt"),
        ("Swing Trading - Michael Roy", "03_swing_roy.txt"),
    ],
    "061": [
        ("Basitleştirilmiş Hareketli Ortalamalar - Clif Droke", "01_ma_droke.txt"),
        ("Basitleştirilmiş Mum Kalıpları - Christopher Lee", "02_candles_lee.txt"),
        ("Elliott Dalga Teorisi (43 sayfa)", "03_elliott_theory.txt"),
    ],
    "062": [
        ("En İyi Trend Çizgisi Yöntemleri - Patrick Mikula", "01_trendlines_mikula.txt"),
        ("Her Traderin Bilmesi Gereken 21 Mum - Dr. Melvin Pasternak", "02_candles_pasternak.txt"),
        ("MACD Göstergesinin Sırrı - Jayden Smith", "03_macd_smith.txt"),
    ],
    "063": [
        ("Arz ve Talep Analizi - Samibegood", "01_supply_demand_samibegood.txt"),
        ("Forex 20 Trend Takip Sistemi - Thomas Carter", "02_forex20_carter.txt"),
        ("Toni Hansen_in Pazarı - Destek ve Direnci Anlamak", "03_support_resistance_hansen.txt"),
    ],
    "064": [
        ("En İyi Trading Sistemleri - David Jenyns", "01_systems_jenyns.txt"),
        ("İndikatörlerle Kazanç Sağlamak - Jeff Drake", "02_indicators_drake.txt"),
        ("Teknik Analizi Anlamak ve Uygulamak - Ravi Agarwal", "03_technical_agarwal.txt"),
    ],
    "065": [
        ("Forex - Ayarla ve Unut Kazanç Sistemi - Mark Boardman", "01_set_forget_boardman.txt"),
        ("MACD Trend Takip Stratejisi - Trading Strategy Guides", "02_macd_trend_guides.txt"),
        ("Short-Term Trading Sırları (24 sayfa)", "03_short_term_secrets.txt"),
    ],
    "066": [
        ("Forex Grafik Desenleri - Eksiksiz Bir Kılavuz - Forex GDP", "01_patterns_gdp.txt"),
        ("Mum Çubuklarını Anlamak (48 sayfa)", "02_candles_understanding.txt"),
        ("EDGE Trading Sırları - Blue Edge Financial", "03_edge_secrets.txt"),
    ],
    "067": [
        ("Forex Sihirli Mum Çubukları - Forex Profit Farm", "01_magic_candles.txt"),
        ("Teknik Analiz - Trading Sanatı - Trading Technicals", "02_technical_art.txt"),
        ("Düşünen Trader - Galen Woods", "03_thinking_trader.txt"),
    ],
    "068": [
        ("Dinamit TNT Forex Sistemi (95 sayfa)", "01_tnt_forex.txt"),
        ("Kazandıran Forex Trading Sistemi - Axi Trader", "02_axi_system.txt"),
        ("Piyasa Yapıcı Tuzakları - Beat The Market Maker", "03_market_maker_traps.txt"),
    ],
    "069": [
        ("Craig Harris_in Forex Trading Metodolojisi", "01_craig_harris.txt"),
        ("Forex Broker Killer Edition - Kgopotso Mmutlane", "02_broker_killer.txt"),
        ("Para Sihirbazı - Mum Çubukları ile Farklı Bir Analiz Yöntemi", "03_para_sihirbazi.txt"),
    ],
    "070": [
        ("Bitcoin Günlük Alım Satım Stratejileri - Lawrence Keaton", "01_bitcoin_daily.txt"),
        ("En İyi Bitcoin ve Ethereum Trading Stratejisi - James Jecool King", "02_bitcoin_eth.txt"),
        ("Kripto Para Ticareti - Piyasaya Giriş, Çıkış ve Stop-Loss", "03_crypto_entry_exit.txt"),
    ],
    "071": [
        ("Algoritmik Trading Stratejileri - Scotty Ratford", "01_algorithmic_ratford.txt"),
        ("Ortalama Dönüşüne Dayalı Günlük Alım Satım Stratejisi Kitabı - Rob Teally", "02_mean_reversion_teally.txt"),
        ("Ayı Piyasası Trading Stratejileri - Matthew R. Kratter", "03_bear_market_kratter.txt"),
    ],
    "072": [
        ("Arz ve Talep Trading Stratejisi - Frank Edward", "01_supply_demand_edward.txt"),
        ("Düşük Risk Yüksek Kazanç Trading Stratejileri - Trading Pub", "02_low_risk_trading_pub.txt"),
        ("Fiyat Grafik Formasyonlarıyla Trading - Derek Salvon", "03_chart_patterns_salvon.txt"),
    ],
    "073": [
        ("Follow The Money (FTM) Stratejisi", "01_ftm.txt"),
        ("Forex Trading Sistemi - Sumo FX - Jaco Ferreira", "02_sumo_fx.txt"),
        ("En Başarılı 10 Price Action Modeli - Al Brooks", "03_al_brooks_patterns.txt"),
    ],
    "074": [
        ("Bir Tersine Dönüşün Ne Zaman Gerçekleşeceğini Nasıl Belirleyebilirim", "01_reversal_timing.txt"),
        ("MACD - Karthik Marar", "02_macd_marar.txt"),
        ("Trendline Trading Stratejisi - Rich Finegan", "03_trendline_finegan.txt"),
    ],
    "075": [
        ("Uyumsuzluklar - Alexander Elder", "01_divergence_elder.txt"),
        ("Wyckoff Yöntemi", "02_wyckoff.txt"),
        ("Forex Day Trading - Gavin Wallace", "03_day_trading_wallace.txt"),
    ],
    "076": [
        ("Short - Dr. Alexander Elder", "01_short_elder.txt"),
        ("Price Action - Elliot Baker", "02_price_action_baker.txt"),
        ("Order Block ve Fibonacci -  Bheki Mpanganeb", "03_ob_fib_mpanganeb.txt"),
    ],
    "077": [
        ("Spartan Trader Forex Sistemi - Nikos Mermigas", "01_spartan_mermigas.txt"),
        ("Price Action Kurulumları ve Örnekleri - Stoxxme", "02_stoxxme_setups.txt"),
        ("Yeni Başlayanlar İçin Grafik Okuma Teknikleri", "03_chart_reading.txt"),
    ],
    "078": [
        ("Trading Stratejileri - Simon Sikorski", "01_sikorski.txt"),
        ("Uyumsuzluklar - Oleg A. But", "02_oleg_divergence.txt"),
        ("Price Action - James Jecool King", "03_king_price_action.txt"),
    ],
    "079": [
        ("Price Action - Marcio Santos", "01_marcio_santos.txt"),
        ("Gap Trading (62 sayfa)", "02_gap_trading.txt"),
        ("Unicorn Avantajı - Furqan Malick", "03_unicorn_malick.txt"),
    ],
    "080": [
        ("Price Action - Market Masters Academy", "01_market_masters.txt"),
        ("Price Action Kursu - Junior Dias", "02_junior_dias.txt"),
        ("Supply and Demand Eğitim Kursu", "03_supply_demand_course.txt"),
    ],
    "081": [
        ("Price Action Stratejileri - Alpha FX", "01_alpha_fx.txt"),
        ("Supply and Demand Kılavuzu", "02_supply_demand_guide.txt"),
        ("Teknik Analiz Kursu - Rekt Proof", "03_rekt_proof.txt"),
    ],
    "082": [
        ("Düşük Riskli Ichimoku Stratejisi Rehberi - Karen Peloille", "01_ichimoku_peloille.txt"),
        ("Day Trade Forex Sistemi", "02_day_trade_forex.txt"),
        ("İşe Yarayan 5 Basit Trading Stratejisi - Jeff Swanson", "03_swanson_five.txt"),
    ],
    "083": [
        ("Kazançlı Günlük Trading Stratejisi - Caroline Ayuk", "01_ayuk_daily.txt"),
        ("Basit Forex Trading Formülleri - Billy Williams", "02_williams_formulas.txt"),
        ("Açığa Çıkan Trading Sırları", "03_trading_secrets.txt"),
    ],
    "084": [
        ("Basit Hareketli Ortalama (SMA) ve Bollinger Bantları Göstergelerinin Birlikte Kullanımıyla", "01_sma_bb.txt"),
        ("Gelişmiş RSI İndikatörü - Lalit Mohanty", "02_advanced_rsi.txt"),
        ("Harmonik Formasyonlar - Six000", "03_harmonic.txt"),
    ],
    "085": [
        ("En İyi 10 Forex Stratejisi - Authentic FX", "01_authentic_fx.txt"),
        ("Forex Trading Stratejileri - Edmund Loh", "02_edmund_loh.txt"),
        ("Günlük Trading Stratejilerinde İndikatörlerin Kullanımı - Lawrence Keaton", "03_keaton_indicators.txt"),
    ],
    "086": [
        ("Günlük Alım Satım Giriş ve Çıkışları - En İyi Günlük Alım Satım Girişi - David Harnett", "01_harnett.txt"),
        ("Forex Trading Stratejileri (53 sayfa)", "02_forex_strategies.txt"),
        ("Trend Trading Makaleleri (55 sayfa)", "03_trend_articles.txt"),
    ],
    "087": [
        ("En İyi 25 İndikatör - Frank Luther", "01_indicators.txt"),
        ("Al ve Sat Günlük Trading Sinyalleri - 2022 Baskısı", "02_daily_signals.txt"),
        ("Yüksek Kazanç Oranlı Günlük Trading Kurulumları - Marcel Robbinson", "03_robbinson.txt"),
    ],
    "088": [
        ("Uyumsuzluklarla Trading", "01_divergences.txt"),
        ("Forex Gizli Trading Modeli - Rich Finegan", "02_hidden_model.txt"),
        ("Coffee Grounds Trading Sistemi - P. K. Tournis", "03_coffee_grounds.txt"),
    ],
    "089": [
        ("Başlangıç Seviyesi Günlük Trading 2020 - George Livermore", "01_day_trading_2020.txt"),
        ("Yeni Başlayanlar İçin Basitleştirilmiş Forex Trading - Marlon Green", "02_simple_forex.txt"),
        ("Forex Trading Kuralları - Lever70", "03_forex_rules.txt"),
    ],
    "090": [
        ("Forex Trading 10 Altın Kural - Admiral Markets", "01_ten_forex_rules.txt"),
        ("Güniçi Trading ile Servet Oluşturmak - Maddy", "02_intraday_wealth.txt"),
        ("Kusursuz Günlük Trading - Ivan Cavric", "03_perfect_day_trading.txt"),
    ],
    "091": [
        ("Bollinger Band Trading - Kazançlı Bir Trading Sistemi Nasıl Oluşturulur - Glenn Wilson", "01_bollinger_wilson.txt"),
        ("Forex Trading Rehberi - 30 Dakikalık Günlük Trading Stratejisi - Jeremy Zindel", "02_m30_zindel.txt"),
        ("Günlük Forex Stratejisi - Güvenli ve Kazançlı Trading - Frq Mid", "03_forex_frq_mid.txt"),
    ],
    "092": [
        ("Forex Trading İşlemlerinde Stop Avlama Stratejisi - David Odoh", "01_stop_hunting.txt"),
        ("Adım Adım Kazanan Trader için Forex İşlem Stratejileri - Donald Stanberry", "02_step_by_step.txt"),
        ("Yeni Forex Piyasası Trading Sistemi - Emegha Emmanuel", "03_new_forex_system.txt"),
    ],
    "093": [
        ("Profesyonellerin Trading Sistemi - Eloy Villalon", "01_professional_system.txt"),
        ("Günde En Az 100 Dolar Kazanmak İçin En İyi Forex Trading Stratejileri - Brian Kendall", "02_hundred_dollars.txt"),
        ("Grafik Formasyonları ve Price Action Forex Trading - Mason Anderson", "03_patterns_price_action.txt"),
    ],
    "094": [
        ("Fiyat Kalıplarıyla Günlük Forex Trading - Laurentiu Damir", "01_price_patterns_damir.txt"),
        ("Günlük Trading - Giriş ve Çıkış Sistemleri 2023 - James Jecool King", "02_entries_exits_king.txt"),
        ("Vadeli İşlemler Trading Stratejileri - Wayne Walker", "03_futures_walker.txt"),
    ],
    "095": [
        ("Günde 40 Pips - Giorgio Strani", "01_forty_pips_strani.txt"),
        ("Kazandıran Forex Trading - Forex_te Kazanmak için Günde 10 Dakika - Giorgio Strani", "02_ten_minutes_strani.txt"),
        ("Forex Piyasasında Nasıl Scalp Yapılır - Binary Forex Brokers", "03_scalp_binary_forex.txt"),
    ],
    "096": [
        ("Borsada Kazanmak İçin Teknik Analiz Hakkındaki Gerçekler - Alvaro Cid", "01_technical_truths_cid.txt"),
        ("Döviz İşlemleri 2 - Heikin Ashi Trader", "02_fx_ha_trader.txt"),
        ("En İyi Teknik İndikatörler - Emily Dhruv", "03_indicators_dhruv.txt"),
    ],
    "097": [
        ("Günlük Trading Stratejisi - Türkçe ve İngilizce - Index Trader", "01_index_trader.txt"),
        ("Ichımoku Hızlı Başlangıç Rehberi - Bob Joiner", "02_ichimoku_joiner.txt"),
        ("Geçimini Sağlamak İçin Günlük Alım Satım - Borsa Piyasasında Yön Bulmak İçin 5 Uzman Sistem - Leigh Vernon", "03_five_systems_vernon.txt"),
    ],
    "098": [
        ("Biriktirme ve Dağıtım Kurulumları - Kesin Karlılık İçin Nihai İşlem Giriş Kurulumu - Momoh S.O.", "01_accumulation_momoh.txt"),
        ("Dürtüsel Satın Alma - Lalit Mohanty", "02_impulse_buying_mohanty.txt"),
        ("Day Trading - Rajiv LB Roy", "03_day_trading_roy.txt"),
    ],
    "099": [
        ("Kripto Ticaretinde Mum Grafiklerini Okumak İçin Profesyonel Bir Kılavuz - Kripto Paranızı Nasıl Koruyacağınızı Keşfedin - Emily Dhruv", "01_crypto_candles_dhruv.txt"),
        ("Order Block Trading - Emily Dhruv", "02_order_block_dhruv.txt"),
        ("Scalping Stratejileri - S. Connell", "03_scalping_connell.txt"),
    ],
    "100": [
        ("Price Action ve Order Block Uzmanlığı - James Jecool King", "01_price_order_block_king.txt"),
        ("Scalping Trading İşlemlerinde En İyi 5 Strateji - Para Kazanma Yöntemleri - Andrew C. Ellis", "02_five_scalps_ellis.txt"),
        ("Basit Strateji - Güçlü Bir Günlük Alım Satım Stratejisi - Markus Heitkoetter ve Mark Hodge", "03_simple_strategy_heitkoetter.txt"),
    ],
    "101": [
        ("Basitleştirilmiş Forex - Alpha Balde", "01_simple_forex_balde.txt"),
        ("Forex Online - Eugenio Milani", "02_forex_online_milani.txt"),
        ("Forex Trading - Owen Pagano", "03_forex_pagano.txt"),
    ],
    "102": [
        ("Forex Trading - 30 Günde Hiçbir Şeyden Her şeye - Ross Wright", "01_thirty_days_wright.txt"),
        ("Para Kazanma Stratejisi - Günde Sadece 15 Dakika - Caroline Ayuk", "02_fifteen_minutes_ayuk.txt"),
        ("Forex Trading İşlemlerinden Geçimini Sağlamanın 4 Adımı - Luciano A. Kelly", "03_four_steps_kelly.txt"),
    ],
    "103": [
        ("EURUSD için 3 adet Günlük İşlem Stratejisi - Daniel G. G.", "01_eurusd_three_daniel.txt"),
        ("Kazançlı Hareketli Ortalama Trading Sistemi - Stephan Miller", "02_ma_miller.txt"),
        ("Ultimate MACD Giriş Stratejisi - Richard Krugel", "03_macd_krugel.txt"),
    ],
    "104": [
        ("Gavin Holmes Scalp Stratejisi", "01_gavin_holmes_scalp.txt"),
        ("Madam Lim Trading Sistemi - World Class Trading Stars", "02_madam_lim.txt"),
        ("Trendline Trading Stratejisi - Day and Night Forex", "03_trendline_day_night.txt"),
    ],
    "105": [
        ("Price Action Scalper", "01_price_action_scalper.txt"),
        ("Forex Grid Trade Stratejisi", "02_forex_grid.txt"),
        ("Swing Failure Pattern", "03_swing_failure.txt"),
    ],
    "106": [
        ("Londra Oturumu Forex Trading Sırları - Alberto Sassetti", "01_london_sassetti.txt"),
        ("Düşük Riskli Swing Trading için Gün İçi Zamanlama - Walter Bressert", "02_swing_bressert.txt"),
        ("Nasdaq Endeksi ile Tradingin Sırları", "03_nasdaq_secrets.txt"),
    ],
    "107": [
        ("Forex Trading Şifresi - Alberto Sassetti", "01_forex_code_sassetti.txt"),
        ("Swing Trading için Hisse Tarama Aracı - Abhishek Jain", "02_swing_screener_jain.txt"),
        ("Price Action Trading Stratejileri - Matthew Robert", "03_price_action_robert.txt"),
    ],
    "108": [
        ("Kazançlı Gold Stratejisi - Learn Price Action", "01_gold_price_action.txt"),
        ("Okehiedon Gann System", "02_gann_okehiedon.txt"),
        ("MACD Al ve Sat Sinyalleri", "03_macd_signals.txt"),
    ],
    "109": [
        ("Trading Kurulumları - Falcon FX", "01_falcon_fx.txt"),
        ("Payapa Scalping Stratejisi", "02_payapa_scalp.txt"),
        ("Gün İçi Trading Stratejisi - Gelişmiş Bir Gün İçi İşlem Yöntemini Öğren", "03_intraday_stock_trader.txt"),
    ],
    "110": [
        ("Haftalık Gelir İçin Basit Kurulumlar - Thomas Wood", "01_weekly_wood.txt"),
        ("Çift Vuruş Fibonacci Stratejisi - J Crawford", "02_double_fib_crawford.txt"),
        ("Forex - Investing People - Valeriano", "03_forex_valeriano.txt"),
    ],
    "111": [
        ("Forex Bermuda Trading Stratejisi - Michel Selim", "01_bermuda_selim.txt"),
        ("AK47 Scalping Stratejisi - Türkçe ve İngilizce - Siya Vezi", "02_ak47_vezi.txt"),
        ("Nasdaq Trading Stratejisi - FX Goat", "03_nasdaq_fx_goat.txt"),
    ],
    "112": [
        ("Trading İşlemlerinde İkili Dojinin Sırrı - Vladimir Ribakov", "01_double_doji_ribakov.txt"),
        ("Kanal Ticareti (12 sayfa)", "02_channel_trading.txt"),
        ("Forex - JM Shepal", "03_forex_shepal.txt"),
    ],
    "113": [
        ("Basitleştirilmiş Fibonacci Düzeltmesi -  Forex Gün İçi Ticareti", "01_fibonacci_srinivasan.txt"),
        ("Mum Grafiğiyle Trading Tekniği - Avinash Mudaliar", "02_candles_mudaliar.txt"),
        ("Forex ve Order Block Trading Rehberi - Raymond M. Smith", "03_order_block_smith.txt"),
    ],
    "114": [
        ("Pin Bar Stratejisi (18 sayfa)", "01_pin_bar.txt"),
        ("NFP Stratejisi - Unathi W. Salman", "02_nfp_salman.txt"),
        ("Nasdaq Trading Stratejisi - Thabang Lebese", "03_nasdaq_lebese.txt"),
    ],
    "115": [
        ("Fibonacci Trading Hakkında Her Şey - Bill Poulos", "01_fibonacci_poulos.txt"),
        ("BTMM + ICT Sniper Giriş - Omoemu Festus", "02_btmm_festus.txt"),
        ("Swing Trading - Cafe Du Forex", "03_swing_cafe_du_forex.txt"),
    ],
    "116": [
        ("Trading Sistemi - Giovanni Del Toro", "01_trading_system_del_toro.txt"),
        ("Super Scalper - Gavin Holmes", "02_super_scalper_holmes.txt"),
        ("Forex Mum Çubuğu Pusu İşlemi - Long Hang Seng", "03_candle_ambush_seng.txt"),
    ],
    "117": [
        ("Wyckoff Metodolojisi (31 sayfa)", "01_wyckoff_methodology.txt"),
        ("RSI Trading - Tyler Aaron", "02_rsi_tyler_aaron.txt"),
        ("Güniçi Trading - B. Jonathan", "03_intraday_jonathan.txt"),
    ],
    "118": [
        ("Altın Teknik (64 sayfa)", "01_gold_technical.txt"),
        ("Sizi Zengin Edebilecek 7 Trading Modeli - Charles A. Floyd", "02_seven_patterns_floyd.txt"),
        ("Yüksek Kazançlı Swing Ticaretinin 5 Sırrı - Ivayla Ivanov", "03_five_swing_secrets_ivanov.txt"),
    ],
    "119": [
        ("Forex Systems Research Company Teknik Analiz Kursu", "01_forex_systems_research.txt"),
        ("Forex Trading Kursu - Heiken Ashi Trader", "02_heiken_ashi_course.txt"),
        ("Teknik Analiz Kursu - Bull and Bear Academy", "03_bull_bear_technical.txt"),
    ],
    "120": [
        ("Açıklamalı Price Action Tekniği - Svetlin Minev", "01_price_action_minev.txt"),
        ("Mumların Dili - Vladimir Ribakov", "02_candles_ribakov.txt"),
        ("Trend Çizgileri (43 sayfa)", "03_trend_lines.txt"),
    ],
    "121": [
        ("Price Action - Colibri Trader - Demsu", "01_colibri_price_action.txt"),
        ("Price Action Dinamikleri (29 sayfa)", "02_price_action_dynamics.txt"),
        ("Kazançlı Mum Giriş Çıkış Stratejileri", "03_candle_entries_exits.txt"),
    ],
    "122": [
        ("Haftalık Opsiyonlar ve Vadeli İşlemlerle Trading Döngüleri ve Kırılmalar - Larry Gaines", "01_gaines_cycles_breakouts.txt"),
        ("Güniçi Satın Alma Stratejisi (30 sayfa)", "02_intraday_buy.txt"),
        ("Darvas Box ile Trading - Alpesh Pansheriya", "03_darvas_box.txt"),
    ],
    "123": [
        ("Kanıtlanmış 8 Price Action Stratejisi - Alpesh Pansheriya", "01_eight_price_action.txt"),
        ("Price Action Trading - Tyler Aaron", "02_tyler_price_action.txt"),
        ("Forex Trend Takip Stratejileri - Thomas Carter", "03_carter_trend_follow.txt"),
    ],
    "124": [
        ("3 Basit Opsiyon Stratejisi - Andy Crowder", "01_crowder_options.txt"),
        ("Günlük Trading - Intro Books - Learning is Easy", "02_intro_day_trading.txt"),
        ("Price Action Trends - Laurentiu Damir", "03_damir_trends.txt"),
    ],
    "125": [
        ("Mum Kalıpları - Trading Junkies", "01_trading_junkies_candles.txt"),
        ("Swing Trading için Kesin Kılavuz - Johnathon", "02_johnathon_swing.txt"),
        ("Smart Money Concept - SMC Trading - James Jecool King", "03_king_smc.txt"),
    ],
    "126": [
        ("Kolaylaştırılmış Daily Bias Tespiti", "01_daily_bias.txt"),
        ("Mumlar Hakkında Bilmek İsteyeceğiniz Her Şey - Mark Rose", "02_mark_rose_candles.txt"),
        ("Forex Eğitimi - Market Makers Method", "03_market_makers_method.txt"),
    ],
    "127": [
        ("M1-M5 Forex Scalping Stratejisi", "01_m1_m5_scalping.txt"),
        ("Fibonacci  Geri Çekilme Stratejisi", "02_fibonacci_retracement.txt"),
        ("Order Block - Gabriel Rios", "03_rios_order_block.txt"),
    ],
    "128": [
        ("Arz ve Talep - Soulz", "01_soulz_supply_demand.txt"),
        ("Fibonacci Geri Çekilme Prensibi", "02_fibonacci_principle.txt"),
        ("Fibonacci Geri Çekilme ile Teknik Analiz - M. Jazuli İsmail", "03_ismail_fibonacci.txt"),
    ],
    "129": [
        ("Düşük Zaman Dilimlerinde Order Block Tespiti", "01_low_tf_order_block.txt"),
        ("ICT Blok Tipleri (Orijinal)", "02_ict_block_types.txt"),
        ("ICT Block Örnekleri", "03_ict_block_examples.txt"),
    ],
    "130": [
        ("BYSTRA - Gold Perfect Entry - Orijinal", "01_bystra_gold_entry.txt"),
        ("Fiyat Düzeltmesi ve Trend Dönüşü Kurulumu - Momoh SO", "02_momoh_reversal.txt"),
        ("Günlük Trading Kazanç Paketi - Profit King", "03_profit_king_day_trading.txt"),
    ],
    "131": [
        ("Takas Edilebilir Order Blocklar", "01_tradable_order_blocks.txt"),
        ("Wyckoff Eğitimi - Rise Precision", "02_wyckoff_rise_precision.txt"),
        ("Çökme Sinyali - Borsa Çöküşünü Öngören Tek Sinyal - Tim Morris", "03_morris_crash_signal.txt"),
    ],
    "132": [
        ("Trading Uzmanlığı - Million Moves Presents", "01_trading_mastery.txt"),
        ("M ve W Nihai Gün İçi Trading Stratejisi", "02_mw_king.txt"),
        ("Ayarla ve Unut - Yıllık Ortalama", "03_set_forget_morris.txt"),
    ],
    "133": [
        ("Kripto Ticaretinde Mum Grafiklerini Okumaya Yönelik Profesyonel Bir Kılavuz", "01_crypto_candles_dhruv.txt"),
        ("Orderblock Forex Trading Sırrı", "02_orderblock_forex_king.txt"),
        ("Forex Trading için İçeriden Rehber", "03_forex_insider_caron.txt"),
    ],
    "134": [
        ("Sir Lz Notları", "01_sir_lz_notes.txt"),
        ("Trader Rehberi - Shinta FX", "02_shinta_fx.txt"),
        ("Hedge Stratejileri", "03_hedge_strategies.txt"),
    ],
    "135": [
        ("ICT Stratejisi - James Jecool King", "01_ict_king.txt"),
        ("Fiyat Hareketi Grafiğini Okuma Rehberi - Profit King", "02_price_chart_profit_king.txt"),
        ("Trading Başarısı - Temellerden İleri Seviyeye - Jennifer Jung", "03_trading_success_jung.txt"),
    ],
    "136": [
        ("H4 Zaman Diliminde 200 ve 50 EMA ile Strateji Oluşturma", "01_h4_ema200_50.txt"),
        ("Currency Grail - Benim Gizli Kayıpsız Forex Scalping Sistemim", "02_currency_grail.txt"),
        ("Kolaylaştırılmış Elliott Dalgaları - Acrotec", "03_elliott_acrotec.txt"),
    ],
    "137": [
        ("Yalan Söylemeyen Trading Rehberi - Glennmaru", "01_glennmaru.txt"),
        ("Trading Hub 2.0 - Mr. Khan", "02_trading_hub_khan.txt"),
        ("King of Pips Teknik Analiz Kılavuzu - Alberto Orozco", "03_king_of_pips.txt"),
    ],
    "138": [
        ("Kolaylaştırılmış Mum Grafikleri - James Williams", "01_candles_williams.txt"),
        ("Saçmalık Olmayan Rehber - Trade İşlemlerine Nasıl Başlanır - David Fiacan", "02_fiacan_guide.txt"),
        ("Trading İşlemlerinde Başarılı Olmanın Sırları - Lee Kelvin", "03_kelvin_secrets.txt"),
    ],
    "139": [
        ("1 Aylık Trade Bilgeliği Rehberi - Edward C. Turner", "01_turner_month.txt"),
        ("Yavaş ve İstikrarlı - Robert Glover", "02_glover_slow.txt"),
        ("Başarılı Hisse Senedi Ticareti - Nick Radge", "03_radge_stock.txt"),
    ],
    "140": [
        ("Yeni Başlayanlar İçin Forex - Markets.com", "01_markets_forex.txt"),
        ("Basit Trading Kitabı - Orijinal", "02_simple_trading_original.txt"),
        ("Elliott Dalga Teorisi (Ders 4)", "03_elliott_lesson4.txt"),
    ],
    "141": [
        ("GBPJPY M1 Scalp Stratejisi - Green Forex", "01_gbpjpy_scalp.txt"),
        ("Tüm Zamanların En İyi 100 Trading Kuralı", "02_trading_rules.txt"),
        ("Mum Formasyonları - Alper Ergül", "03_alper_candles.txt"),
    ],
    "142": [
        ("Günlük Trading Sırları - Harvey Walsh", "01_walsh_day_trading.txt"),
        ("En İyi 8 Adet Price Action Kalıbı - Colibri Trader", "02_colibri_patterns.txt"),
        ("LBR Scalp İşlem Kurulumları -  Kevin  Ho", "03_lbr_scalp.txt"),
    ],
    "143": [
        ("Yeni Başlayanlar için Smart Money Konsepti - Derek Salvon", "01_salvon_smc.txt"),
        ("Risk Yönetimi - Abraham Robert C.", "02_abraham_risk.txt"),
        ("Hisse Senedi Ticaretinde Zafer - 2020 ABD Yatırım Şampiyonunu Stratejisi", "03_oliver_kell.txt"),
    ],
    "144": [
        ("Acemiler için Kripto Day Trading - David T. Allen", "01_crypto_day_allen.txt"),
        ("ICT Trading Rehberi - James Jecool King", "02_ict_king.txt"),
        ("Trading Masters Kalıplar", "03_trading_masters_patterns.txt"),
    ],
    "145": [
        ("ICT Order Block Trading - Derek Salvon", "01_ict_ob_salvon.txt"),
        ("İndikatörleri Birleştirerek Geliştireceğin Güçlü Stratejilerle", "02_indicators_pham.txt"),
        ("Forex Trading - Dinamik Bir Pazarda Başarı İçin Stratejiler ve Taktikler", "03_forex_james.txt"),
    ],
    "146": [
        ("Falcon Trading Teknik Analiz Kursu", "01_falcon_course.txt"),
        ("Forex Trading Manifestosu", "02_forex_manifesto.txt"),
        ("Yapay Zeka ile Daha Akıllı Trading - Chris Miller", "03_ai_trading_miller.txt"),
    ],
    "147": [
        ("Teknik Analiz - Rachana Ranade", "01_ranade_ta.txt"),
        ("Teknik Analiz Kursu - Deriv", "02_deriv_ta.txt"),
        ("Price Action - Digitalgigz Trading Academy", "03_digitalgigz_pa.txt"),
    ],
    "148": [
        ("Price Action Konsepti", "01_price_action_concept.txt"),
        ("Smart Money Kavramları", "02_smart_money_concepts.txt"),
        ("Mum Analizi - Emily Dhruv", "03_candle_analysis_dhruv.txt"),
    ],
    "149": [
        ("Trading Kuralları - Patt Tomas", "01_trading_rules_tomas.txt"),
        ("Güniçi İşlemlerde Ustalaşmak", "02_intraday_mohanty.txt"),
        ("Trading Oyununda Nasıl Kazanılır", "03_trading_game_dhruv.txt"),
    ],
    "150": [
        ("Dow Teorisi - Michael Young", "01_dow_young.txt"),
        ("Alfa Crypto Ders Notları", "02_alfa_crypto.txt"),
        ("Kripto Para Grafikleri", "03_crypto_charts.txt"),
    ],
    "151": [
        ("Piyasa Yapıcı Yöntemi - Modül 1", "01_market_maker_module.txt"),
        ("Price Action Mum Rehberi - We Trade Daily", "02_price_action_candles.txt"),
        ("Mum Rehberi -  Darrell Jobman", "03_candle_guide_jobman.txt"),
    ],
    "152": [
        ("Günlük Alım Satım Stratejileri - Scotty Ratford", "01_day_trading_ratford.txt"),
        ("Basitleştirilmiş SMC (Akıllı Para Konsepti) Trading Rehberi", "02_smc_brown.txt"),
        ("Price Action ve Orderblock ile İleri Düzey Piyasa Yapısı Trading", "03_pa_ob_king.txt"),
    ],
    "153": [
        ("Payapa Trading Stratejisi", "01_payapa.txt"),
        ("Temel Formasyonlar Rehberi - Branko Petruci", "02_patterns_petruci.txt"),
        ("Order Block ile Gelişmiş Trading Rehberi", "03_order_block_smith.txt"),
    ],
    "154": [
        ("Forex Swing Trading - Abraham Robert C.", "01_forex_swing_abraham.txt"),
        ("Günlük Alım Satım - Para Kazanmanın ve Başarıya Ulaşmanın Gizli Stratejileri", "02_day_trading_anthony.txt"),
        ("Teknik Analiz ve Dow Teorisi - Mustafa", "03_dow_mustafa.txt"),
    ],
    "155": [
        ("Swing Trading Kuralları - Paul Welch", "01_swing_rules_welch.txt"),
        ("Kolaylaştırılmış Günlük Trading - Trader University", "02_day_trading_kratter.txt"),
        ("Arz ve Talep Trading Rehberi - Kenny Brandon", "03_supply_demand_brandon.txt"),
    ],
    "156": [
        ("Teknik Analiz ve Fiyat Hareketi - En Kapsamlı Rehber", "01_ta_price_action_wilson.txt"),
        ("Smart Money Konseptleri 2.0 - Forex Trading", "02_smc_kavi.txt"),
        ("Forex Trading - Bruce Copson", "03_forex_copson.txt"),
    ],
    "157": [
        ("Başarılı Traderların Sırları - İkinci Baskı - MetaStock", "01_metastock_secrets.txt"),
        ("Forexin Sırları - John Powell", "02_forex_secrets_powell.txt"),
        ("Başarılı Traderların Sırları - Sagar Nandi", "03_secrets_nandi.txt"),
    ],
    "158": [
        ("Günlük Hisse Senedi Ticaretimin Sırları - Richard D. Wyckoff", "01_wyckoff_daily_stock.txt"),
        ("Başarılı Forex Ticareti için 10 Anahtar - Jared F. Martinez", "02_martinez_ten_keys.txt"),
        ("Ortalamaya Dönüş Günlük Trading - David Harnett", "03_harnett_mean_reversion.txt"),
    ],
    "159": [
        ("Basitleştirilmiş Günlük Trading Teknikleri - Michael S. Jenkins", "01_jenkins_day_trading.txt"),
        ("200 Kısa Trading Psikolojisi - Yvan Byeajee", "02_trading_psychology_byeajee.txt"),
        ("Adım Adım Trade - Alexander Elder", "03_step_by_step_elder.txt"),
    ],
    "160": [
        ("Akıllı Para Konseptinde Ustalaşma - Forex Piyasasının Ayrıntılı Analizi - David E. Morrison", "01_smart_money_morrison.txt"),
        ("Price Action Kursu", "02_price_action_course.txt"),
        ("Order Block - Mete Kaplan", "03_order_block_kaplan.txt"),
    ],
    "161": [
        ("Price Action - Raoul Hunter", "01_price_action_hunter.txt"),
        ("İşleme Giriş Noktasının Belirlenmesi - Momoh SO", "02_entry_momoh.txt"),
        ("Fiyat Aşırı Alım ve Aşırı Satım Sinyali - Momoh SO", "03_extremes_momoh.txt"),
    ],
    "162": [
        ("Çizgiyi Takas Etmek - Trend Çizgilerini Kullanarak Dönüşleri Tespit Etmek ve Trendleri Yakalamak - Jeffery Kennedy", "01_trade_the_line_kennedy.txt"),
        ("Arz ve Talep Ticaretini Kolayca Öğrenin - Jason Applebaum", "02_supply_demand_applebaum.txt"),
        ("Andrews Pitchfork Kullanarak Bereketli Trading Kazançları Elde Edin - Bryan V Post", "03_pitchfork_post.txt"),
    ],
    "163": [
        ("Büyük Piyasa Hareketlerini Nasıl Yakalayabilirsiniz - L.R. Thomas", "01_big_moves_thomas.txt"),
        ("Yüksek İvmeli Hisselerde İşlem Yapmayı Öğrenin - Matthew R. Kratter", "02_momentum_stocks_kratter.txt"),
        ("Forex İçin Gelişmiş Teknik Analiz - Wayne Walker", "03_advanced_forex_walker.txt"),
    ],
    "164": [
        ("Grafik Kalıpları (33 sayfa)", "01_chart_patterns.txt"),
        ("Price Action - Daniel Stones", "02_price_action_stones.txt"),
        ("Japon Mum Grafik Teknikleri - James Abbott", "03_candles_abbott.txt"),
    ],
    "165": [
        ("Japon Mum Çubuklarına Kolay Bir Yaklaşım - Stefano Calicchio", "01_candles_calicchio.txt"),
        ("Günlük Alım Satım - Para Kazanmanın ve Başarıya Ulaşmanın Gizli Stratejileri (Orijinal) - Anthony Smith", "02_day_trading_smith.txt"),
        ("Price Action - Derek Salvon (48 sayfa)", "03_price_action_salvon.txt"),
    ],
    "166": [
        ("Arz ve Talep Trading Kitabı - Daniel Stones", "01_supply_demand_stones.txt"),
        ("Karlı Bir Trading Stratejisi Nasıl Oluşturulur - Heikin Ashi Trader", "02_build_strategy_heikin_ashi.txt"),
        ("Forex Kungfu Shaolin", "03_forex_kungfu_shaolin.txt"),
    ],
    "167": [
        ("Bir Aralıkta Nasıl İşlem Yapılır - Heikin Ashi Trader", "01_range_heikin_ashi.txt"),
        ("Price Action ve Piyasa Yapısı - Bill Simons", "02_structure_simons.txt"),
        ("Görünür ve Tuzaklı Trading - Deivid FX", "03_trapped_trading_deivid.txt"),
    ],
    "168": [
        ("Fibonacci Düzeltmesi Uzmanlığı - Lalit Mohanty", "01_fibonacci_mohanty.txt"),
        ("Scalping Stratejileri 101 - Usiere Uko", "02_scalping_uko.txt"),
        ("Profesyonel Price Action Trading Rehberi - Kenny Brandon", "03_price_action_brandon.txt"),
    ],
    "169": [
        ("Price Action Three Lines - R. Rana", "01_three_lines.txt"),
        ("Price Action Kırılımları - Laurentiu Damir", "02_breakouts_damir.txt"),
        ("Price Action Quasimodo (QM) Konu Anlatımı", "03_quasimodo.txt"),
    ],
    "170": [
        ("Göstergeyle Scalping El Kitabı", "01_indicator_scalping_ferrazzi.txt"),
        ("Scalping İşlemlerine İlişkin Kesin Kılavuz", "02_scalping_guide.txt"),
        ("Yüksek Başarı Olasılığına Sahip Scalping Stratejileri El Kitabı", "03_scalping_carson.txt"),
    ],
    "171": [
        ("E-mini Dow ve Mini DAX için Hızlı Al-Sat", "01_emini_dax_scalping.txt"),
        ("En Kazançlı 10 Trading Stratejisi - Nikhil Porwal", "02_ten_strategies_porwal.txt"),
        ("Forex Trading Stratejileri (53 sayfa)", "03_forex_strategies.txt"),
    ],
    "172": [
        ("Trendline Breakout Stratejisi (62 sayfa)", "01_trendline_breakout.txt"),
        ("Price Action Kurulumları (90 sayfa)", "02_price_action_setups.txt"),
        ("Forex Trading Stratejisi - Quantum Globe", "03_quantum_globe.txt"),
    ],
    "173": [
        ("Forex Range Trading with Price Action - Laurentiu Damir", "01_forex_range_damir.txt"),
        ("BO Turbo Trader Price Action Kılavuzu", "02_bo_turbo_price_action.txt"),
        ("Scalping Kılavuzu - Gary Norden", "03_scalping_norden.txt"),
    ],
    "174": [
        ("Gelişmiş Fibonacci Trading Kavramları - Jim Kane", "01_fibonacci_jim_kane.txt"),
        ("VWAP - Brian Shannon", "02_vwap_brian_shannon.txt"),
        ("Ichimoku Grafikleri Rehberi - Nicole Elliott", "03_ichimoku_nicole_elliott.txt"),
    ],
    "175": [
        ("Mum Grafikleri - Clive Lambert", "01_candles_clive_lambert.txt"),
        ("Price Action Trading - Indrazith Shantharaj", "02_price_action_indrazith.txt"),
        ("Yüksek Olasılıklı Mum Desenleri ve Kurulumlar - Stephen Bigalow", "03_candles_stephen_bigalow.txt"),
    ],
    "176": [
        ("Price Action - Atif Choudhury", "01_price_action_atif.txt"),
        ("Başlangıç Seviyesindekiler İçin Trading - Mark McRae", "02_trading_mark_mcrae.txt"),
        ("Traderin El Kitabı - Rob Booker", "03_trader_handbook_rob_booker.txt"),
    ],
    "177": [
        ("Forex Piyasasında Günlük Ticaret - Kar Stratejileri - Ketty Lin", "01_forex_daily_ketty_lin.txt"),
        ("Piyasa Yapıcının Matrixi - Evan J. Christopher", "02_market_maker_matrix_christopher.txt"),
        ("Günlük İşlem Yapmanın Ustalığı - Nataraj Malavade", "03_day_trading_malavade.txt"),
    ],
    "178": [
        ("Price Action - Mustafa Karahan", "01_price_action_karahan.txt"),
        ("Trader - 93 Trading Dersi - Frank Marshall", "02_trading_lessons_marshall.txt"),
        ("Forex Okulu (208 sayfa)", "03_forex_okulu.txt"),
    ],
    "179": [
        ("Günlük Trading İşlemlerinde Nihai Rehber - Al Hill", "01_day_trading_al_hill.txt"),
        ("Penny Stock Trading Sistemi - Donny Lowy", "02_penny_stocks_lowy.txt"),
        ("Forex Teknik Analiz Kursu (212 sayfa)", "03_forex_technical_course.txt"),
    ],
    "180": [
        ("Forex Piyasasında Nasıl Para Kazanılır - Stanislav Grebenshchikov", "01_forex_grebenshchikov.txt"),
        ("4.5 Milyon Dolar Kazanç - Chuck Hughes", "02_trend_following_hughes.txt"),
        ("Forex Hakkında Nihai Kılavuz - Felix Goldstein", "03_forex_goldstein.txt"),
    ],
    "181": [
        ("Algoritmik Trading Kısayol Kodları - Kevin J. Davey", "01_algo_davey.txt"),
        ("Fiyat ve Hacmin Gizli Bilimi - Timothy Ord", "02_price_volume_ord.txt"),
        ("PowerX Stratejisi - Markus Heitkoetter", "03_powerx_heitkoetter.txt"),
    ],
    "182": [
        ("Adım Adım Algoritmik Trading Rehberi - Investors Press", "01_algo_investors_press.txt"),
        ("Mum Grafikleri Hakkında Nihai Rehber - Steve Burns", "02_candles_burns_matov.txt"),
        ("Trading Stratejileri 2022 - Daphne Warner", "03_strategies_warner.txt"),
    ],
    "183": [
        ("Gelişmiş Teknik Analiz - Jon Fibonacci", "01_advanced_ta_fibonacci.txt"),
        ("Ne Zaman Hisse Senedi ve Kripto Varlık Alınır - Javier Luque", "02_when_buy_luque.txt"),
        ("Piyasalar Arası Analiz Kullanarak Forex Trading - Dean Grey", "03_intermarket_grey.txt"),
    ],
    "184": [
        ("Swing and Day Trading - Thomas N. Bulkowski", "01_swing_day_bulkowski.txt"),
        ("Sistematik Trading - Robert Carver", "02_systematic_carver.txt"),
        ("Traderlar için Döngü Analitiği - İleri Düzey Teknik Trading Kavramları", "03_cycle_ehlers.txt"),
    ],
    "185": [
        ("Teknik Analiz Modülü - NCFM", "01_ta_ncfm.txt"),
        ("Alfaları Bulmak - Ticaret Stratejileri Geliştirmek", "02_alpha_tulchinsky.txt"),
        ("Son Derece Etkili Yatırımcıların 7 Basit Stratejisi", "03_seven_strategies_patel.txt"),
    ],
    "186": [
        ("Online Trading ve Yatırımın 10 Sırrı - Jim Berg", "01_ten_secrets_berg.txt"),
        ("Karlı Kısa Vadeli Trading Stratejileri - Rakesh Bansal", "02_short_term_bansal.txt"),
        ("Teknik Analiz Rehberi - Rankia", "03_ta_rankia.txt"),
    ],
    "187": [
        ("Günde Sadece 1 Trade - Michael Jardine", "01_one_trade_jardine.txt"),
        ("Gelişmiş Forex Trading - Edward Day", "02_advanced_forex_day.txt"),
        ("S&P 500 Endeksinde Günlük Trading - Arthur H. Ullrich", "03_sp500_intraday_ullrich.txt"),
    ],
    "188": [
        ("Gelişmiş Price Action Tekniği", "01_advanced_price_action.txt"),
        ("Bir Keşiş Gibi Trade Yap", "02_trade_like_monk.txt"),
        ("Başarılı Yatırımcılar Pozisyonlarını Neden ve Nasıl Boyutlandırıyor", "03_position_sizing_basso.txt"),
    ],
    "189": [
        ("Elliott Dalga Ticareti Hakkında Görsel Rehber", "01_elliott_visual_guide.txt"),
        ("Smart Money Kavramının Kutsal Kitabı", "02_smart_money_bible.txt"),
        ("Sakin Trader - Aklınızı Kaybetmeden Kazanın", "03_calm_trader.txt"),
    ],
    "190": [
        ("Day Trading - David Bennett", "01_day_trading_bennett.txt"),
        ("Elektronik Günlük Traderların Sırları", "02_electronic_day_traders.txt"),
        ("Ticaretin Kutsal Kasesi Risk Yönetimi", "03_risk_holy_grail.txt"),
    ],
    "191": [
        ("Price Action Sistemini Anlamak - Bob Volman", "01_price_action_volman.txt"),
        ("Trade İşlemlerinde Risk Yönetimi Kılavuzu", "02_risk_management_guide.txt"),
        ("Forex ile Finansal Özgürlük - Greg Secker", "03_financial_freedom_secker.txt"),
    ],
    "192": [
        ("Day Trading - Douglas Allen", "01_day_trading_allen.txt"),
        ("Hızlı Para - O Kadar da Hızlı Değil", "02_fast_money_kovac.txt"),
        ("Finans Psikolojisi - Forex Investment Lounge", "03_finance_psychology.txt"),
    ],
    "193": [
        ("Vadeli İşlemlerle Trend Takibi - Alex Greyserman", "01_futures_trend_greyserman.txt"),
        ("En İyi Kaybeden Kazanır - Tom Hougaard (250 sayfa)", "02_best_loser_hougaard.txt"),
        ("Traderlar İçin Mental Fitness - Norman Hallett", "03_mental_fitness_hallett.txt"),
    ],
    "194": [
        ("Derinlemesine Wyckoff Metodolojisi - Ruben Villahermosa", "01_wyckoff_villahermosa.txt"),
        ("Kanitatif Momentum - Wesley R. Gray ve Jack R. Vogel", "02_quant_momentum_gray_vogel.txt"),
        ("Swing Traderlar için Zamanlama Çözümleri - Robert T.H. Lee", "03_swing_timing_lee_tryde.txt"),
    ],
    "195": [
        ("Trend Ticareti Sanatı - Michael Parness", "01_trend_parness.txt"),
        ("Smart Money Gölgesinde Trading - Gavin Holmes", "02_smart_money_holmes.txt"),
        ("Teknik Analiz ile Trendi Tahmin Etmek - Louis B. Mendelsohn", "03_trend_mendelsohn.txt"),
    ],
    "196": [
        ("Kaldıraçlı Trading - Robert Carver", "01_leveraged_carver.txt"),
        ("Borsada İşe Yarayan Stratejiler - Jake Bernstein", "02_stock_strategies_bernstein.txt"),
        ("Süper Forex Sistemi - En Kazançlı 16 Strateji", "03_super_forex_system.txt"),
    ],
    "197": [
        ("Trading Rejimi Analizi - Murray Gunn", "01_regime_gunn.txt"),
        ("Thalesians Trading - Saeed Amen", "02_thalesians_amen.txt"),
        ("Teknik Analizde Atılımlar - Bloomberg - David Keller", "03_breakthroughs_keller.txt"),
    ],
    "198": [
        ("Etkili Trading Sistemlerinin Oluşturulması ve Değerlendirilmesi - Thomas Stridsman", "01_effective_systems_stridsman.txt"),
        ("Fiyat Kalıpları - Martin Pring", "02_price_patterns_pring.txt"),
        ("Daha Yüksek Olasılıklı Emtia Ticareti - Carley Garner", "03_commodity_garner.txt"),
    ],
    "199": [
        ("O_Neil Disciples ile Trading Kokpitinde - Gil Morales", "01_oneil_morales.txt"),
        ("Breakout Traderları için Erken Giriş Noktaları - Moneyu101", "02_early_breakout_moneyu101.txt"),
        ("NSE Teknik Analiz Kursu", "03_nse_technical_analysis.txt"),
    ],
    "200": [
        ("Craig Harris_in Forex Trading Metodolojisi", "01_craig_harris.txt"),
        ("Forex Analizi ve Trading - T. J. Marta", "02_forex_analysis_marta.txt"),
        ("Döviz Piyasasında Ustalaşmak - Jay Norris", "03_forex_mastery_norris.txt"),
    ],
    "201": [
        ("Entegre Çatal Analizi - Dr. Mircea Dologa", "01_integrated_pitchfork_dologa.txt"),
        ("RDS Forex Sistemi - Stephanie Radkay", "02_rds_forex_radkay.txt"),
        ("Day Trading - Justin Kuepper", "03_day_trading_kuepper.txt"),
    ],
    "202": [
        ("Küçük Yatırımcılar İçin Günlük İşlemler 2.0", "01_day_trading_small_investors.txt"),
        ("Toni Hansen_in Pazarı - Destek ve Direnci Anlamak", "02_toni_hansen_support.txt"),
        ("Forex Devrimi - Peter Rosenstreich", "03_forex_revolution_rosenstreich.txt"),
    ],
    "203": [
        ("Forex Ticaretinin 10 Temel Ögesi - Jared F. Martinez", "01_forex_ten_elements_martinez.txt"),
        ("Forex Trading Sırları - James Dicks", "02_forex_secrets_dicks.txt"),
        ("Forex - Vahram Sayadov", "03_forex_sayadov.txt"),
    ],
    "204": [
        ("OrangeRoshan Paylaşımları - SRDC 1 - MatiasFX", "01_orange_roshan_srdc.txt"),
        ("Borsa Sihirbazı Gibi Trade Yapın - Mark Minervini", "02_minervini_stock_wizard.txt"),
        ("Phantom_un Hediyesi", "03_phantom_gift.txt"),
    ],
    "205": [
        ("Teknik Analiz Dersi (182 sayfa)", "01_teknik_analiz_dersi.txt"),
        ("Sam Seiden Eğitim Notları", "02_sam_seiden_notes.txt"),
        ("Trading İşlemlerine Yeni Başlayanlar İçin Kılavuz - Alessio Rastani - Orijinal", "03_alessio_rastani.txt"),
    ],
    "206": [
        ("Price is Everything - Orijinal Kaynak", "01_price_is_everything.txt"),
        ("Basitleştirilmiş Volatil Piyasalar - Guy Cohen", "02_volatile_markets_cohen.txt"),
        ("Yeni Başlayanlar İçin Forex - Marc Stuart", "03_forex_marc_stuart.txt"),
    ],
    "207": [
        ("Zamandaki Değer - Dr. Alexander Elder", "01_elder_value_in_time.txt"),
        ("100e Katlayanlar - 1e 100 Getiren Hisseleri Nasıl Bulabilirsiniz", "02_hundred_baggers_mayer.txt"),
        ("Yeni Başlayanlar İçin Forex Trading - William Rogers ve George Evans", "03_forex_rogers_evans.txt"),
    ],
    "208": [
        ("En Kapsamlı Forex Trading Kılavuzu - Joshua Hoerning", "01_forex_hoerning.txt"),
        ("Borsa Yatırımı - Elle J.C.", "02_stock_investing_elle_jc.txt"),
        ("Yıldız Trader Olmak İçin Rehber - Karen Foo", "03_karen_foo_star_trader.txt"),
    ],
    "209": [
        ("Gün İçi Trading Taktikleri - Greg Capra", "01_intraday_capra.txt"),
        ("Her Operasyonda Kazanma Stratejileri - Oliver L. Velez", "02_velez_strategies.txt"),
        ("Kalabalığa Karşı Trading - John F. Summa", "03_summa_crowd.txt"),
    ],
    "210": [
        ("İşe Yarayan Trade Kuralları - Jason Alan Jankovsky", "01_jankovsky_rules.txt"),
        ("Kazanmak için 7 Grafik Aracı - Malcolm Pryor", "02_pryor_chart_tools.txt"),
        ("Mum Grafiklerini Anlamak - Russell Rhoads", "03_rhoads_candlesticks.txt"),
    ],
    "211": [
        ("Birinci Gün - Trader - John Sussex", "01_sussex_first_day.txt"),
        ("Grafiklerle Trade Yaparak Nasıl Para Kazanılır - Ashwani Gujral", "02_gujral_charts.txt"),
        ("Günlük Trading için Tam Kapsamlı Kılavuz - Markus Heitkoetter", "03_heitkoetter_day_trading.txt"),
    ],
    "212": [
        ("Trend Takibinin Kutsal Kitabı - Andrew Abraham", "01_abraham_trend_following.txt"),
        ("Mum Grafikleriyle Nasıl Para Kazanırsınız - Balkrishna M. Sadekar", "02_sadekar_candles.txt"),
        ("Trading Çiftleri - Mark Whistler", "03_whistler_pairs.txt"),
    ],
    "213": [
        ("Kanıta Dayalı Teknik Analiz - David R. Aronson", "01_aronson_evidence.txt"),
        ("Klasik Trading Grafik Kalıpları - Thomas N. Bulkowski", "02_bulkowski_classic.txt"),
        ("Profesyonel Otomatik Trading - Teori ve Pratik - Eugene A. Durenard", "03_durenard_auto.txt"),
    ],
    "214": [
        ("Teknik Piyasa İndikatörleri Ansiklopedisi - Robert W. Colby", "01_colby_indicators.txt"),
        ("Piyasa Genişliği Göstergelerine İlişkin Tam Kılavuz - Gregory L. Morris", "02_morris_breadth.txt"),
        ("Quantum Trading - Fabio Oreste", "03_oreste_quantum.txt"),
    ],
    "215": [
        ("MIDAS Teknik Analiz - Günümüz Piyasalarında", "01_midas.txt"),
        ("Hacime Dayalı Teknik Analiz - Kirk Northington", "02_volume_based.txt"),
        ("Kısa Bir Teknik Analiz Kursu - Perry J. Kaufman", "03_kaufman_course.txt"),
    ],
}
books = books_by_batch[batch]
for needle, output_name in books:
    path = next(p for p in root.rglob("*.pdf") if needle.casefold() in p.name.casefold())
    reader = PdfReader(str(path), strict=False)
    output = out / output_name
    with output.open("w", encoding="utf-8") as f:
        f.write(f"SOURCE: {path}\nPAGES: {len(reader.pages)}\n")
        for i, page in enumerate(reader.pages, 1):
            try:
                body = page.extract_text() or ""
            except Exception as e:
                body = f"[EXTRACTION ERROR: {e}]"
            f.write(f"\n\n=== PDF PAGE {i} ===\n{body}\n")
    print(path.name, len(reader.pages), output.stat().st_size, flush=True)
