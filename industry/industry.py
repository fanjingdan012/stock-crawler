import numpy as np
import pandas as pd
# def get_sw_industries_dict():
#     return dict
def collect_reports_for_industry(stock_code_list):
    for i, stock_code in enumerate(stock_code_list):

        # df_cfs = pd.read_excel('../data/cfs_'+stock_code+'.xlsx')  # , skiprows=1
        # df_is = pd.read_excel('../data/is_'+stock_code+'.xlsx')
        df_bs = pd.read_excel('../data/bs_'+stock_code+'.xlsx')
        # df_cfs['code'] = stock_code
        # df_is['code'] = stock_code
        df_bs['code'] = stock_code
        print("read:%s" % (stock_code))
        if i==0:
            # df_cfs_all = df_cfs
            # df_is_all = df_is
            df_bs_all = df_bs
        else:
            # df_cfs_all=df_cfs_all.append(df_cfs)
            # df_is_all = df_is_all.append(df_is)
            df_bs_all = df_bs_all.append(df_bs)

    # df_cfs_all.fillna(0, inplace=True)
    # df_is_all.fillna(0, inplace=True)
    df_bs_all.fillna(0, inplace=True)
    # print(df_cfs.keys())
    # df_cfs_all.to_excel('../data/cfs_采掘行业.xlsx')
    df_bs_all.to_excel('../data/bs_采掘行业.xlsx')
