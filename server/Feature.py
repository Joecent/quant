"""
features cantain the data keys that we need to fetch from specific data format

prepare tushare:
 import tushare as ts
 ts.set_token('b82f1bd5e6a33947a66041c85c4a382a6758a1b8e4b8473c26db48d1')
 pro = ts.pro_api()
"""


"""
  fundamental list contains fina indicators which meannings from  https://tushare.pro/document/2?doc_id=79, also look in FUNDAMENTAL.md
  or just fetch from tushare use api like below:
  df = pro.fina_indicator(ts_code='600000.SH')
  fundamental_list = df.keys().tolist()
"""

fundamental_list =  ['ts_code', 'ann_date', 'end_date', 'eps', 'dt_eps', 'total_revenue_ps', 'revenue_ps', 'capital_rese_ps', 'surplus_rese_ps', 'undist_profit_ps', 'extra_item', 'profit_dedt', 'gross_margin', 'current_ratio', 'quick_ratio', 'cash_ratio', 'ar_turn', 'ca_turn', 'fa_turn', 'assets_turn', 'op_income', 'ebit', 'ebitda', 'fcff', 'fcfe', 'current_exint', 'noncurrent_exint', 'interestdebt', 'netdebt', 'tangible_asset', 'working_capital', 'networking_capital', 'invest_capital', 'retained_earnings', 'diluted2_eps', 'bps', 'ocfps', 'retainedps', 'cfps', 'ebit_ps', 'fcff_ps', 'fcfe_ps', 'netprofit_margin', 'grossprofit_margin', 'cogs_of_sales', 'expense_of_sales', 'profit_to_gr', 'saleexp_to_gr', 'adminexp_of_gr', 'finaexp_of_gr', 'impai_ttm', 'gc_of_gr', 'op_of_gr', 'ebit_of_gr', 'roe', 'roe_waa', 'roe_dt', 'roa', 'npta', 'roic', 'roe_yearly', 'roa2_yearly', 'debt_to_assets', 'assets_to_eqt', 'dp_assets_to_eqt', 'ca_to_assets', 'nca_to_assets', 'tbassets_to_totalassets', 'int_to_talcap', 'eqt_to_talcapital', 'currentdebt_to_debt', 'longdeb_to_debt', 'ocf_to_shortdebt', 'debt_to_eqt', 'eqt_to_debt', 'eqt_to_interestdebt', 'tangibleasset_to_debt', 'tangasset_to_intdebt', 'tangibleasset_to_netdebt', 'ocf_to_debt', 'turn_days', 'roa_yearly', 'roa_dp', 'fixed_assets', 'profit_to_op', 'q_saleexp_to_gr', 'q_gc_to_gr', 'q_roe', 'q_dt_roe', 'q_npta', 'q_ocf_to_sales', 'basic_eps_yoy', 'dt_eps_yoy', 'cfps_yoy', 'op_yoy', 'ebt_yoy', 'netprofit_yoy', 'dt_netprofit_yoy', 'ocf_yoy', 'roe_yoy', 'bps_yoy', 'assets_yoy', 'eqt_yoy', 'tr_yoy', 'or_yoy', 'q_sales_yoy', 'q_op_qoq', 'equity_yoy']

"""

  technical list contain price and volume features from:https://tushare.pro/document/2?doc_id=27, also look in TECHNICAL.md 
  df = ts.pro_bar(ts_code='600000.SH', adj='qfq', start_date='20180101', end_date='20181011', factors=['tor', 'vr'])
  technical_list = df.keys().tolist()
"""
technical_list = ['ts_code', 'trade_date', 'open', 'high', 'low', 'close', 'pre_close', 'change', 'pct_chg', 'vol', 'amount', 'turnover_rate', 'volume_ratio']

# (TODO) there are so many index portforlios in tushare and we should check the useful ones
"""

  index list contain index status features from: https://tushare.pro/document/2?doc_id=94
there are different companies giving their index portforlios, first we use CSI(中证指数)

  use index portforlio to firgure out the bias between industry field and specific stock

  csi index list contains index portforlios it has
  csi_index_list = pro.index_basic(market='CSI')
  csi weight contain the stock's weight in one portforlio
  csi_weight = pro.index_weight(index_code = '000803.CSI')
  csi daily present the daliy value of one  portforlio
  csi_daily = pro.index_daily(ts_code='000821.CSI')

"""
index_list = []

"""
market list include index from 'https://tushare.pro/document/2?doc_id=128'
use 12 market index, refer index code to specific index
000001.SH 上证指数
000005.SH 商业指数
000006.SH 地产指数
000016.SH 上证50
000300.SH 沪深300 上证
000905.SH 中证500 上证
399001.SZ 深证成指
399005.SZ 中小板指
399006.SZ 创业板指
399016.SZ 深证创新
399300.SZ 沪深300 深证
399905.SZ 中证500 深证
"""
market_list = ['index_code', 'trade_date', 'total_mv', 'float_mv', 'total_share', 'float_share', 'free_share', 'turnover_rate', 'turnover_rate_f', 'pe', 'pe_ttm', 'pb']

