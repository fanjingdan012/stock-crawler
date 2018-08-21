import xueqiu_balance_sheet
import xueqiu_cash_flow_statement
import xueqiu_income_statement


def get_reports_for_1_stock(stock_code_str):
    # xueqiu_balance_sheet.get_bs_for_1_stock(stock_code_str)
    xueqiu_cash_flow_statement.get_cfs_for_1_stock(stock_code_str)
    xueqiu_income_statement.get_is_for_1_stock(stock_code_str)


if __name__=="__main__":
    # stock_code_str='SH600795'
    stock_code_list = ["SZ000552","SZ000571","SZ000655","SZ000723","SZ000762","SZ000780","SZ000937","SZ000968","SZ000983","SZ002128","SZ002207","SZ002554","SZ002629","SZ002738","SZ002828","SZ300157","SZ300164","SZ300191","SH600121","SH600123","SH600157","SH600188","SH600295","SH600339","SH600348","SH600395","SH600397","SH600403","SH600408","SH600508","SH600532","SH600546","SH600583","SH600725","SH600740","SH600758","SH600759","SH600777","SH600792","SH600871","SH600971","SH600997","SH601001","SH601011","SH601015","SH601088","SH601101","SH601225","SH601666","SH601699","SH601808","SH601857","SH601898","SH601918","SH601969","SH603113","SH603505","SH603619","SH603727","SH603979"]
    for stock_code in stock_code_list:
        get_reports_for_1_stock(stock_code)
        print("craw:%s" % (stock_code))