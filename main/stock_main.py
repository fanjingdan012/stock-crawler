import xueqiu.xueqiu_crawler as xueqiu_crawler
import stock_reader
import industry
import data_preprocessor
import chart.is_cfs_bs_chart as is_cfs_bs_chart
if __name__=="__main__":
    str_industry = '电子'
    # step 0 download
    # df=stock_reader.read_sw_industry_stock_df(str_industry)
    # # stock_codes=[ "SH600651" ]
    # for stock_code in df['stock_code']:
    #     xueqiu_crawler.get_reports_for_1_stock(stock_code)
    #
    #
    # # step 1 append
    # df_industry = stock_reader.read_sw_industry_stock_df(str_industry)
    # industry.append_reports_for_industry(str_industry,df_industry)

    # # step 2 merge is cfs
    # df_is_cfs = data_preprocessor.merge_industry_is_cfs(str_industry)

    # step 3 merge is_cfs bs
    # df_is_cfs = data_preprocessor.merge_industry_is_cfs_bs(str_industry)

    # step 4 draw chart
    is_cfs_bs_chart.draw_industry_is_cfs_bs_chart_for_stock(str_industry,'SZ002415')
    # is_cfs_bs_chart.draw_industry_is_cfs_bs_chart_for_enddate('电子','20171231')