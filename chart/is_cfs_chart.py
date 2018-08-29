import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import axes3d
import chart.is_chart as is_chart
import chart.cfs_chart as cfs_chart
from matplotlib.font_manager import FontProperties
import matplotlib
matplotlib.use('Agg')
import industry
import stock_reader
import data_preprocessor


def draw_is_cfs_subplot(ax,df):
    width = 0.12
    # cfs var
    t = df['enddate']
    bizcashinfl = df['bizcashinfl']
    bizcashoutf = df['bizcashoutf']
    mananetr = df['mananetr']

    invcashinfl = df['invcashinfl']
    invcashoutf = df['invcashoutf']
    invnetcashflow = df['invnetcashflow']

    fincashinfl = df['fincashinfl']
    fincashoutf = df['fincashoutf']
    finnetcflow = df['finnetcflow']




    # is var
    t = df['enddate']
    bti = df['biztotinco']
    bi = df['bizinco']
    inteinco = df['inteinco']
    pouninco = df['pouninco']
    otherbizinco = df['otherbizinco']
    btc = df['biztotcost']
    bc = df['bizcost']
    pp = df['perprofit']
    biztax = df['biztax']
    salesexpe = df['salesexpe']
    manaexpe = df['manaexpe']
    finexpe = df['finexpe_is']
    asseimpaloss = df['asseimpaloss']
    inveinco = df['inveinco']
    nonoreve = df['nonoreve']
    nonoexpe = df['nonoexpe']
    noncassetsdisl = df['noncassetsdisl']
    incotaxexpe = df['incotaxexpe']
    netprofit = df['netprofit_is']

    ind = np.arange(len(t))  # the x locations for the groups

    # bar1 inco
    # btib = ax.bar(ind, bti, width*8,color='silver')

    # bar 2 inco
    bar2_position=ind
    is_chart.draw_is_income_bar(ax,bar2_position,width*6,bi,otherbizinco,inveinco,pouninco,inteinco)

    # bar 3 co
    # bar3_position=ind - 3 * width
    # rects3 = ax.bar(bar3_position, btc, width, bottom=pp,color='blue')

    # bar 4 co

    bar4_position=ind -1.5 * width
    is_chart.draw_is_cost_bar(ax, bar4_position, width*2, bc, biztax, salesexpe, manaexpe, finexpe, asseimpaloss, pp)

    # bar 6 co
    bar5_position = bar4_position
    is_chart.draw_is_net_profit_bar(ax,bar5_position,width,nonoreve,nonoexpe,noncassetsdisl,incotaxexpe,netprofit)

    # cfs bars
    # bar 7 cfs op cash in
    bar6_position=ind+1.5*width
    cfs_chart.draw_cfs_biz_cash_bar(ax,bar6_position,width*2,bizcashinfl,bizcashoutf,mananetr)


    ax.set_xticks(ind )
    ax.set_xticklabels(t)
    # for tick2 in ax.get_xticklabels():
    #     tick2.set_rotation(90)
    font = FontProperties(fname=r"C:\\windows\\fonts\\simsun.ttc")
    ax.set_xticklabels(t, size='small', rotation=90, fontproperties=font)
    ax.legend(loc='upper right')


def draw_industry_is_cfs_subplot(ax,df):
    width = 0.12
    # cfs var

    stock_code = df['stock_code']
    stock_name = df['stock_name_cfs']
    bizcashinfl = df['bizcashinfl']
    bizcashoutf = df['bizcashoutf']
    mananetr = df['mananetr']

    invcashinfl = df['invcashinfl']
    invcashoutf = df['invcashoutf']
    invnetcashflow = df['invnetcashflow']

    fincashinfl = df['fincashinfl']
    fincashoutf = df['fincashoutf']
    finnetcflow = df['finnetcflow']




    # is var
    t = df['enddate']
    bti = df['biztotinco']
    bi = df['bizinco']
    inteinco = df['inteinco']
    pouninco = df['pouninco']
    otherbizinco = df['otherbizinco']
    btc = df['biztotcost']
    bc = df['bizcost']
    pp = df['perprofit']
    biztax = df['biztax']
    salesexpe = df['salesexpe']
    manaexpe = df['manaexpe']
    finexpe = df['finexpe_is']
    asseimpaloss = df['asseimpaloss']
    inveinco = df['inveinco']
    nonoreve = df['nonoreve']
    nonoexpe = df['nonoexpe']
    noncassetsdisl = df['noncassetsdisl']
    incotaxexpe = df['incotaxexpe']
    netprofit = df['netprofit_is']

    ind = np.arange(len(t))  # the x locations for the groups

    # bar1 inco
    # btib = ax.bar(ind, bti, width*8,color='silver')

    # bar 2 inco
    bar2_position=ind
    is_chart.draw_is_income_bar(ax,bar2_position,width*6,bi,otherbizinco,inveinco,pouninco,inteinco)

    # bar 3 co
    # bar3_position=ind - 3 * width
    # rects3 = ax.bar(bar3_position, btc, width, bottom=pp,color='blue')

    # bar 4 co

    bar4_position=ind -1.5 * width
    is_chart.draw_is_cost_bar(ax, bar4_position, width * 2, bc, biztax, salesexpe, manaexpe, finexpe, asseimpaloss, pp)


    # bar 6 co
    bar5_position = bar4_position
    is_chart.draw_is_net_profit_bar(ax, bar5_position, width, nonoreve, nonoexpe, noncassetsdisl, incotaxexpe,
                                    netprofit)
    # cfs bars
    bar6_position=ind+1.5*width
    cfs_chart.draw_cfs_biz_cash_bar(ax, bar6_position, width * 2, bizcashinfl, bizcashoutf, mananetr)

    ax.set_xticks(ind )
    font = FontProperties(fname=r"C:\\windows\\fonts\\simsun.ttc")
    ax.set_xticklabels(stock_name, size='small', rotation=90, fontproperties=font)
    ax.legend(loc='upper right')

def read_df_by_industry_and_enddate(str_industry,str_enddate):
    dateparse = lambda dates: pd.datetime.strptime(dates, '%Y%m%d')
    df_is_cfs = pd.read_excel('../data/is_cfs_'+str_industry+'.xlsx', parse_dates=['enddate'], date_parser=dateparse)
    # df_is_cfs = pd.read_excel('../data/is_cfs_'+str_industry+'.xlsx',converters={'enddate':str})
    # print(df_is_cfs.keys())
    df_is_cfs=df_is_cfs[df_is_cfs['enddate']==str_enddate]
    df_is_cfs = df_is_cfs.sort_values(by=['bizinco'],ascending=False)
    # df_is_cfs = df_is_cfs[df_is_cfs['code']=='SZ000552']
    return df_is_cfs

def draw_industry_is_cfs_chart_for_enddate(str_industry,str_enddate):
    plt.style.use('ggplot')
    fig, ax = plt.subplots(figsize=(50, 20))
    df_is_cfs = read_df_by_industry_and_enddate(str_industry, str_enddate)
    # print(df_is_cfs)
    draw_industry_is_cfs_subplot(ax, df_is_cfs)
    plt.savefig('../data/charts/is_cfs_' + str_industry + '_' + str_enddate + '.jpg')
    plt.show()


def draw_is_cfs_chart_for_stock(str_stock_code):
    plt.style.use('ggplot')
    df_cfs = pd.read_excel('../data/cfs/cfs_'+str_stock_code+'.xlsx')#, skiprows=1
    df_is = pd.read_excel('../data/is/is_'+str_stock_code+'.xlsx')
    df_cfs.fillna(0, inplace=True)
    df_is.fillna(0, inplace=True)
    # print(df_cfs.keys())

    df_is_cfs = pd.merge(df_cfs, df_is, on='enddate',copy=True, indicator='both',suffixes=('_cfs','_is'))
    # df_is_cfs.to_excel('../data/is_cfs_SH600839.xlsx')
    # df_is_cfs.fillna(0, inplace=True)
    # print(df_is_cfs.keys())
    # df_is_cfs=[df_is_cfs['enddate']>'20080331']
    fig, ax = plt.subplots(figsize=(20, 8))
    draw_is_cfs_subplot(ax,df_is_cfs)
    plt.show()


if __name__ == "__main__":
    # draw_industry_is_cfs_chart_for_enddate('电子','20171231')
    draw_is_cfs_chart_for_stock('SH600839')