import xueqiu.xueqiu_balance_sheet as xueqiu_balance_sheet
import xueqiu.xueqiu_cash_flow_statement as xueqiu_cash_flow_statement
import xueqiu.xueqiu_income_statement as xueqiu_income_statement
import stock_reader


def get_reports_for_1_stock(stock_code):
    xueqiu_balance_sheet.get_bs_for_1_stock(stock_code)
    xueqiu_cash_flow_statement.get_cfs_for_1_stock(stock_code)
    xueqiu_income_statement.get_is_for_1_stock(stock_code)
    print("craw:%s" % (stock_code))


if __name__=="__main__":
    df=stock_reader.read_sw_industry_stock_df('电子')
    # stock_codes=[
    #     "SH600651"
    # ]
    for stock_code in df['stock_code']:
        get_reports_for_1_stock(stock_code)
