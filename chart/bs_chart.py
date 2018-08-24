from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import style
from matplotlib.font_manager import FontProperties


def draw_bs_bars(ax,position,width,ca,la,cl,ll,e):
    current_asset_bar = ax.bar(position, ca, width, bottom=la, label='current asset')
    long_term_asset_bar = ax.bar(position, la, width, label='long term asset bar')
    equity_bar = ax.bar(position + width, e, width, color='y',label='equity')
    long_term_liability_bar = ax.bar(position + width, ll, width, bottom=e, color='b',label='long term liability')
    current_liability_bar = ax.bar(position + width, cl, width, bottom=e + ll,label='current liability')

# def draw_detailed_current_asset_bars(ax,position,width,):
#     cash_bar=ax.bar(position + width, curfds, width, bottom=la,label='cash')
#     cash_bar=ax.bar(position + width, tradfinasset, width, bottom=la,label='cash')
#     cash_bar=ax.bar(position + width, notesrece, width, bottom=la,label='cash')
#     cash_bar=ax.bar(position + width, accorece, width, bottom=la,label='cash')
#     cash_bar=ax.bar(position + width, prep, width, bottom=la,label='cash')
#     cash_bar=ax.bar(position + width, premrece, width, bottom=la,label='cash')


# curfds	tradfinasset	notesrece	accorece	prep	premrece	interece	dividrece	otherrece	expotaxrebarece	subsrece	margrece	intelrece	inve	prepexpe	unseg	expinoncurrasset	othercurrasse	currassetitse	currasseform	totcurrasset	lendandloan	avaisellasse	holdinvedue


def draw_bs_subplot(ax,df):
    width = 0.3
    t = df['reportdate']
    a = df['totasset']
    ca = df['totcurrasset']

    curfds = df['curfds']
    tradfinasset=df['tradfinasset']
    notesrece = df['notesrece']
    accorece = df['accorece']
    prep = df['prep']
    premrece = df['premrece']
    interece = df['interece']
    dividrece = df['dividrece']
    otherrece = df['otherrece']
    expotaxrebarece = df['expotaxrebarece']
    subsrece = df['subsrece']
    margrece = df['margrece']
    intelrece = df['intelrece']
    inve = df['inve']
    prepexpe = df['prepexpe']
    unseg = df['unseg']
    expinoncurrasset = df['expinoncurrasset']
    othercurrasse = df['othercurrasse']
    currassetitse = df['currassetitse']
    currasseform = df['currasseform']
    totcurrasset = df['totcurrasset']
    lendandloan = df['lendandloan']
    avaisellasse = df['avaisellasse']
    holdinvedue = df['holdinvedue']

    la = df['totalnoncassets']
    ind = np.arange(len(t))  # the x locations for the groups

    b = df['totliabsharequi']
    cl = df['totalcurrliab']
    ll = df['totalnoncliab']
    l = df['totliab']
    e = df['righaggr']

    draw_bs_bars(ax,ind,width,ca,la,cl,ll,e)
    ax.set_xticks(ind + width / 2)
    ax.set_xticklabels(t)
    for tick in ax.get_xticklabels():
        tick.set_rotation(90)
    ax.legend(loc='upper right')

def draw_industry_bs_subplot(ax,df):
    width=0.3

    name = df['stock_name']
    a = df['totasset']
    ca = df['totcurrasset']
    la = df['totalnoncassets']
    ind = np.arange(len(name))  # the x locations for the groups
    b=df['totliabsharequi']
    cl=df['totalcurrliab']
    ll=df['totalnoncliab']
    l=df['totliab']
    e=df['righaggr']
    draw_bs_bars(ax, ind, width, ca, la, cl, ll, e)

    ax.set_xticks(ind + width / 2)
    font = FontProperties(fname=r"C:\\windows\\fonts\\simsun.ttc")
    ax.set_xticklabels(name,size='small',rotation=90,fontproperties=font)
    ax.legend(loc='upper right')

if __name__ == '__main__':

    style.use('ggplot')
    str_industry = '电气设备'
    str_reportdate='20171231'
    # fig, ax = plt.subplots(figsize=(15,8))
    fig = plt.figure(figsize=(50, 20))
    dateparse = lambda dates: pd.datetime.strptime(dates, '%Y%m%d')
    dfo = pd.read_excel('../data/bs_'+str_industry+'.xlsx',  parse_dates=['reportdate'], date_parser=dateparse)
    df = dfo[dfo['reportdate'] == str_reportdate]
    df.fillna(0, inplace=True)
    df = df.sort_values(by=['totasset'], ascending=False)
    ax = fig.add_subplot(111)
    draw_industry_bs_subplot(ax,df)

    # ax2 = fig.add_subplot(212)
    # width=0.3
    # df2 = pd.read_excel('../data/bs_SZ002172.xlsx')# dfo#[dfo['code']=='SZ002287']
    # draw_bs_subplot(ax2, df2)

    plt.savefig('../data/charts/bs_' + str_industry + '_' + str_reportdate + '.jpg')
    plt.show()












# fig = plt.figure()
# ax1 = fig.add_subplot(111, projection='3d')
#
# x3 = [1,2,3,4,5,6,7,8,9,10]
# y3 = [5,6,7,8,2,5,6,3,7,2]
# z3 = np.zeros(10)
#
# dx = np.ones(10)
# dy = np.ones(10)
# dz = [1,2,3,4,5,6,7,8,9,10]
#
# ax1.bar3d(x3, y3, z3, dx, dy, dz)
#
#
# ax1.set_xlabel('x axis')
# ax1.set_ylabel('y axis')
# ax1.set_zlabel('z axis')
#
# plt.show()

