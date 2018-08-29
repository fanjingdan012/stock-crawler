import pandas as pd


# name is stock_code or industry(chinese)
def merge_industry_is_cfs(name):
    df_cfs_all = pd.read_excel('./data/cfs_'+name+'.xlsx')
    df_is_all = pd.read_excel('./data/is_'+name+'.xlsx')
    df_merged = pd.merge(df_cfs_all, df_is_all, left_on=['stock_code','enddate'], right_on = ['stock_code','enddate'],copy=True, indicator='both',suffixes=('_cfs','_is'))
    # df_merged.fillna(0, inplace=True)
    df_merged.to_excel('../data/is_cfs_'+name+'.xlsx')
    return df_merged


def merge_industry_is_cfs_bs(name):
    df_cfs_all = pd.read_excel('./data/is_cfs_'+name+'.xlsx')
    df_is_all = pd.read_excel('./data/bs_'+name+'.xlsx')
    df_cfs_all.fillna(0, inplace=True)
    df_is_all.fillna(0, inplace=True)
    df_merged = pd.merge(df_cfs_all, df_is_all, left_on=['stock_code','enddate'], right_on = ['stock_code','reportdate'],copy=True, indicator='exists',suffixes=('_is_cfs','_bs'))
    # df_merged.fillna(0, inplace=True)
    df_merged.to_excel('./data/is_cfs_bs_'+name+'.xlsx')
    return df_merged


def merge_is_cfs(name):
    df_cfs = pd.read_excel('./data/is_cfs_' + name + '.xlsx')
    df_is = pd.read_excel('./data/bs_' + name + '.xlsx')
    df_cfs.fillna(0, inplace=True)
    df_is.fillna(0, inplace=True)
    df_merged = pd.merge(df_cfs, df_is, on='enddate',copy=True, indicator='both',suffixes=('_cfs','_is'))
    df_merged.to_excel('./data/is_cfs_bs_' + name + '.xlsx')
    return df_merged