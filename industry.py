import numpy as np
import pandas as pd


def append_reports_for_industry(industry,df_industry):
    for i in range(0, len(df_industry)):
        stock_code=df_industry.iloc[i]['stock_code']
        df_cfs = pd.read_excel('../data/cfs/cfs_'+stock_code+'.xlsx')  # , skiprows=1
        df_is = pd.read_excel('../data/is/is_'+stock_code+'.xlsx')
        df_bs = pd.read_excel('../data/bs/bs_'+stock_code+'.xlsx')
        df_cfs['stock_code'] = stock_code
        df_is['stock_code'] = stock_code
        df_bs['stock_code'] = stock_code
        stock_name=df_industry.iloc[i]['stock_name']
        df_cfs['stock_name'] = stock_name
        df_is['stock_name'] = stock_name
        df_bs['stock_name'] = stock_name
        print("read:%s" % (stock_code))
        if i == 0:
            df_cfs_all = df_cfs
            df_is_all = df_is
            df_bs_all = df_bs
        else:
            df_cfs_all= df_cfs_all.append(df_cfs)
            df_is_all = df_is_all.append(df_is)
            df_bs_all = df_bs_all.append(df_bs)

    df_cfs_all.fillna(0, inplace=True)
    df_is_all.fillna(0, inplace=True)
    df_bs_all.fillna(0, inplace=True)
    # print(df_cfs.keys())
    df_cfs_all.to_excel('../data/cfs_'+industry+'.xlsx')
    df_is_all.to_excel('../data/is_'+industry+'.xlsx')
    df_bs_all.to_excel('../data/bs_'+industry+'.xlsx')
