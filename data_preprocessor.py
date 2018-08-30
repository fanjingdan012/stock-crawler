import pandas as pd
import datetime

# name is stock_code or industry(chinese)
def merge_industry_is_cfs(name):
    df_cfs_all = pd.read_excel('../data/cfs_'+name+'.xlsx')
    df_is_all = pd.read_excel('../data/is_'+name+'.xlsx')
    df_merged = pd.merge(df_cfs_all, df_is_all, left_on=['stock_code','enddate'], right_on = ['stock_code','enddate'],copy=True, indicator='both',suffixes=('_cfs','_is'))
    # df_merged.fillna(0, inplace=True)
    df_merged.to_excel('../data/is_cfs_'+name+'.xlsx')
    return df_merged


def merge_industry_is_cfs_bs_match_enddate_bsdate(name):
    df_cfs_all = pd.read_excel('../data/is_cfs_'+name+'.xlsx')
    df_is_all = pd.read_excel('../data/bs_'+name+'.xlsx')
    df_cfs_all.fillna(0, inplace=True)
    df_is_all.fillna(0, inplace=True)
    df_merged = pd.merge(df_cfs_all, df_is_all, left_on=['stock_code','enddate'], right_on = ['stock_code','reportdate'],copy=True, indicator='exists',suffixes=('_is_cfs','_bs'))
    # df_merged.fillna(0, inplace=True)
    df_merged.to_excel('../data/is_cfs_bs_'+name+'.xlsx')
    return df_merged


def merge_industry_is_cfs_bs_match_begindate_bsdate(name):

    df_cfs_all = pd.read_excel('../data/is_cfs_'+name+'.xlsx', converters={'enddate': str,'begindate_is':str})
    df_cfs_all['is_year_report'] = df_cfs_all['enddate'].map(lambda d: d.endswith('1231'))
    df_cfs_all['begindate_minus1d'] = df_cfs_all['begindate_is'].map(lambda d: (pd.datetime.strptime(d, '%Y%m%d')-datetime.timedelta(days=1)).strftime("%Y%m%d"))

    df_cfs_all = df_cfs_all[df_cfs_all['is_year_report'] == True]
    df_cfs_all.fillna(0, inplace=True)
    df_cfs_all.to_excel('../data/is_cfs_yearly_' + name + '.xlsx')


    # df_is_cfs_bs = pd.read_excel('../data/is_cfs_bs_' + str_industry + '.xlsx', parse_dates=['enddate'],
    #                              date_parser=dateparse)
    df_bs_all = pd.read_excel('../data/bs_' + name + '.xlsx', converters={'reportdate': str})
    df_bs_all['is_year_report'] = df_bs_all['reportdate'].map(lambda d: d.endswith('1231'))
    df_bs_all = df_bs_all[df_bs_all['is_year_report'] == True]
    df_bs_all.fillna(0, inplace=True)
    df_bs_all.to_excel('../data/bs_yearly_' + name + '.xlsx')

    now = datetime.datetime.now()
    date = now + datetime.timedelta(days=1)

    df_merged = pd.merge(df_cfs_all, df_bs_all, left_on=['stock_code','begindate_minus1d'], right_on = ['stock_code','reportdate'],how='outer',copy=True, indicator='exists',suffixes=('_is_cfs','_bs'))
    # df_merged.fillna(0, inplace=True)
    df_merged.to_excel('../data/is_cfs_bs_begin_'+name+'.xlsx')
    return df_merged

def calc_profit_ability(name):
    df_is_cfs_bs_begin = pd.read_excel('../data/is_cfs_bs_begin_' + name + '.xlsx', converters={'reportdate': str})
    df_is_cfs_bs_begin['roe'] = df_is_cfs_bs_begin['netprofit_is']/df_is_cfs_bs_begin['righaggr']
    df_is_cfs_bs_begin['roa'] = df_is_cfs_bs_begin['netprofit_is']/df_is_cfs_bs_begin['totasset']
    df_is_cfs_bs_begin['ni_div_sr'] = df_is_cfs_bs_begin['netprofit_is']/df_is_cfs_bs_begin['biztotinco']
    df_is_cfs_bs_begin['sr_div_a'] = df_is_cfs_bs_begin['biztotinco']/df_is_cfs_bs_begin['totasset']
    df_is_cfs_bs_begin.to_excel('../data/is_cfs_bs_begin_'+name+'.xlsx')


def merge_is_cfs(name):
    df_cfs = pd.read_excel('../data/is_cfs_' + name + '.xlsx')
    df_is = pd.read_excel('../data/bs_' + name + '.xlsx')
    df_cfs.fillna(0, inplace=True)
    df_is.fillna(0, inplace=True)
    df_merged = pd.merge(df_cfs, df_is, on='enddate',copy=True, indicator='both',suffixes=('_cfs','_is'))
    df_merged.to_excel('../data/is_cfs_bs_' + name + '.xlsx')
    return df_merged