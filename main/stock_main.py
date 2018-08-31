import xueqiu.xueqiu_crawler as xueqiu_crawler
import stock_reader
import industry
import data_preprocessor
import chart.is_cfs_bs_chart as is_cfs_bs_chart
if __name__=="__main__":
    str_industry = '房地产'
    # # step 0 download
    # df=stock_reader.read_sw_industry_stock_df(str_industry)
    # for stock_code in df['stock_code']:
    #     xueqiu_crawler.get_reports_for_1_stock(stock_code)


    # # step 1 append
    # df_industry = stock_reader.read_sw_industry_stock_df(str_industry)
    # industry.append_reports_for_industry(str_industry,df_industry)

    # # step 2 merge is cfs
    # df_is_cfs = data_preprocessor.merge_industry_is_cfs(str_industry)

    # step 3 merge is_cfs bs
    # df_is_cfs = data_preprocessor.merge_industry_is_cfs_bs_match_enddate_bsdate(str_industry)
    # df_is_cfs = data_preprocessor.merge_industry_is_cfs_bs_match_begindate_bsdate(str_industry)

    #step 3.1 calculate some rates
    # data_preprocessor.calc_profit_ability(str_industry)

    # step 4 draw chart
    # df = stock_reader.read_sw_industry_stock_df(str_industry)
    # for stock_code in df['stock_code']:
    # is_cfs_bs_chart.draw_industry_is_cfs_bs_chart_for_stock(str_industry, 'SZ000002')
    # enddates=['20161231','20151231','20141231','20131231','20121231','20111231','20101231' ]
    # for enddate in enddates:
    #     is_cfs_bs_chart.draw_industry_is_cfs_bs_chart_for_enddate(str_industry, enddate)

    # is_cfs_bs_chart.draw_industry_is_cfs_bs_chart_for_stock(str_industry,'SZ002415')
    # is_cfs_bs_chart.draw_industry_is_cfs_bs_chart_for_enddate(str_industry,'20171231')