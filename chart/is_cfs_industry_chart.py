import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import axes3d
import industry
import chart.is_chart as is_chart
import chart.cfs_chart as cfs_chart
import chart.is_cfs_chart as is_cfs_chart
import stock_reader
from matplotlib.font_manager import FontProperties

def merge_industry_is_cfs(str_industry):
    df_cfs_all = pd.read_excel('../data/cfs_'+str_industry+'.xlsx')
    df_is_all = pd.read_excel('../data/is_'+str_industry+'.xlsx')
    df_merged = pd.merge(df_cfs_all, df_is_all, left_on=['stock_code','enddate'], right_on = ['stock_code','enddate'],copy=True, indicator='both',suffixes=('_cfs','_is'))
    # df_merged.fillna(0, inplace=True)
    df_merged.to_excel('../data/is_cfs_'+str_industry+'.xlsx')
    return df_merged


if __name__ == "__main__":
    plt.style.use('ggplot')
    str_industry='电气设备'
        #'传媒'
    # step 1 append
    df_industry = stock_reader.read_sw_industry_stock_df(str_industry)
    industry.append_reports_for_industry(str_industry,df_industry)

    # step 2 merge
    df_is_cfs=merge_industry_is_cfs(str_industry)

    # step 2.1 read merged excel
    dateparse = lambda dates: pd.datetime.strptime(dates, '%Y%m%d')
    df_is_cfs = pd.read_excel('../data/is_cfs_'+str_industry+'.xlsx', parse_dates=['enddate'], date_parser=dateparse)
    # df_is_cfs = pd.read_excel('../data/is_cfs_'+str_industry+'.xlsx',converters={'enddate':str})

    # print(df_is_cfs.keys())
    str_enddate='20101231'
    df_is_cfs=df_is_cfs[df_is_cfs['enddate']==str_enddate]
    df_is_cfs = df_is_cfs.sort_values(by=['bizinco'],ascending=False)
    # df_is_cfs = df_is_cfs[df_is_cfs['code']=='SZ000552']
    fig, ax = plt.subplots(figsize=(50, 20))
    # print(df_is_cfs)
    is_cfs_chart.draw_industry_is_cfs_subplot(ax,df_is_cfs)

    plt.savefig('../data/charts/is_cfs_'+str_industry+'_'+str_enddate+'.jpg')
    plt.show()

