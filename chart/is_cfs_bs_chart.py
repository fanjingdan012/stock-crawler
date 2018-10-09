import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import axes3d
import industry
import chart.is_chart as is_chart
import chart.bs_chart as bs_chart
import chart.cfs_chart as cfs_chart
import chart.is_cfs_chart as is_cfs_chart
import stock_reader
from matplotlib.font_manager import FontProperties
import data_preprocessor




def draw_industry_is_cfs_bs_subplot(ax,df,x):
    width = 0.10
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


    # bs vars
    t = df['reportdate']
    a = df['totasset']
    ca = df['totcurrasset']
    la = df['totalnoncassets']

    b = df['totliabsharequi']
    cl = df['totalcurrliab']
    ll = df['totalnoncliab']
    l = df['totliab']
    e = df['righaggr']

    if x=='stock_code':
        ind = np.arange(len(stock_name))  # the x locations for the groups
    else:
        ind = np.arange(len(t))

    # bar1 inco
    # btib = ax.bar(ind, bti, width*8,color='silver')

    # bar 2 inco
    bar2_position=ind-width*4
    is_chart.draw_is_income_bar(ax,bar2_position,width*6,bi,otherbizinco,inveinco,pouninco,inteinco)

    # bar 3 co
    # bar3_position=ind - 3 * width
    # rects3 = ax.bar(bar3_position, btc, width, bottom=pp,color='blue')

    # bar 4 co

    bar4_position=ind -1.5 * width-width*4
    is_chart.draw_is_cost_bar(ax, bar4_position, width * 2, bc, biztax, salesexpe, manaexpe, finexpe, asseimpaloss, pp)

    # bar 6 co
    bar5_position = bar4_position
    is_chart.draw_is_net_profit_bar(ax, bar5_position, width, nonoreve, nonoexpe, noncassetsdisl, incotaxexpe,
                                    netprofit)
    # cfs bars
    bar6_position=ind+1.5*width-width*4
    cfs_chart.draw_cfs_biz_cash_bar(ax, bar6_position, width * 2, bizcashinfl, bizcashoutf, mananetr)

    # bs bars
    bs_position = ind
    bs_chart.draw_bs_bars(ax,bs_position,width,ca,la,cl,ll,e)
    ax.set_xticks(ind )
    font = FontProperties(fname=r"C:\\windows\\fonts\\simsun.ttc",size='xx-large')
    if x=='stock_code':
        ax.set_xticklabels(stock_code+"_"+stock_name, size='xx-large', rotation=90, fontproperties=font)
    else:
        ax.set_xticklabels(t, size='xx-large', rotation=90, fontproperties=font)
    ax.legend(loc='upper left')



def read_df_by_industry(str_industry):
    dateparse = lambda dates: pd.datetime.strptime(dates, '%Y%m%d')
    df_is_cfs_bs = pd.read_excel('../data/is_cfs_bs_' + str_industry + '.xlsx', parse_dates=['enddate'],
                                 date_parser=dateparse)
    # df_is_cfs = pd.read_excel('../data/is_cfs_'+str_industry+'.xlsx',converters={'enddate':str})
    # print(df_is_cfs.keys())
    return df_is_cfs_bs


def filter_df_by_enddate(df_is_cfs_bs,str_enddate):
    df_is_cfs_bs = df_is_cfs_bs[df_is_cfs_bs['enddate'] == str_enddate]
    df_is_cfs_bs = df_is_cfs_bs.sort_values(by=['bizinco'],ascending=False)
    return df_is_cfs_bs


def filter_df_by_stock_code(df_is_cfs_bs,str_stock_code):
    df_is_cfs_bs = df_is_cfs_bs[df_is_cfs_bs['stock_code'] == str_stock_code]
    df_is_cfs_bs['is_year_report'] = df_is_cfs_bs['enddate'].map(lambda d: d.strftime("%Y%m%d").endswith('1231'))
    df_is_cfs_bs = df_is_cfs_bs[df_is_cfs_bs['is_year_report'] == True]
    df_is_cfs_bs = df_is_cfs_bs.sort_values(by=['reportdate'], ascending=True)
    return df_is_cfs_bs


def draw_industry_is_cfs_bs_chart_for_stock(str_industry,str_stock_code):
    plt.style.use('ggplot')
    fig, ax = plt.subplots(figsize=(20, 8))

    df_is_cfs_bs = read_df_by_industry(str_industry)
    df_is_cfs_bs = filter_df_by_stock_code(df_is_cfs_bs, str_stock_code)
    # plt.title('stock:' + df_is_cfs_bs['stock_name'][0])
    draw_industry_is_cfs_bs_subplot(ax, df_is_cfs_bs, x='enddate')
    plt.savefig('../data/charts/is_cfs_bs_' + str_stock_code + '.jpg')
    plt.show()


def draw_industry_is_cfs_bs_chart_for_enddate(str_industry,str_enddate):
    plt.style.use('ggplot')
    fig, ax = plt.subplots(figsize=(200, 20))
    plt.title('date:'+str_enddate)
    # plt.ylabel('Damped oscillation')
    # plt.suptitle('This is a somewhat long figure title', fontsize=16)
    df_is_cfs_bs = read_df_by_industry(str_industry)
    df_is_cfs_bs=filter_df_by_enddate(df_is_cfs_bs,str_enddate)
    # print(df_is_cfs)
    draw_industry_is_cfs_bs_subplot(ax, df_is_cfs_bs, x='stock_code')
    plt.savefig('../data/charts/is_cfs_bs_'+str_industry+"_"+str_enddate+'.jpg')
    plt.show()




