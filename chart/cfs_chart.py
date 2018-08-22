import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import axes3d

def draw_cfs_biz_cash_bar(ax,position,width,bizcashinfl,bizcashoutf,mananetr):
    biz_cash_in_flow_bar = ax.bar(position, bizcashinfl, width, color='salmon',label='biz cash in flow')
    #bar 8 cfs op cash out + op cash net
    biz_cash_out_flow_bar = ax.bar(position, bizcashoutf, width/2, bottom=mananetr, color='skyblue',label='biz cash out flow')
    mananetr_bar = ax.bar(position, mananetr, width/2, color='darkviolet',label='biz cash net flow')


def draw_cfs_invest_cash_bar(ax,position,width,invcashinfl,invcashoutf,invnetcashflow):
    invcashinflb = ax.bar(position, invcashinfl, width,label='invest cash in flow')
    invcashoutfb = ax.bar(position, invcashoutf, width/2, bottom=invnetcashflow,label='invest cash out flow')
    invnetcashflowb = ax.bar(position, invnetcashflow, width/2,label='invest cash net flow')


def draw_cfs_finance_cash_bar(ax,position,width,fincashinfl,fincashoutf,finnetcflow):
    fincashinflb = ax.bar(position, fincashinfl, width,label='finance cash in flow')
    fincashoutfb = ax.bar(position, fincashoutf, width/2, bottom=finnetcflow,label='finance cash out flow')
    finnetcflowb = ax.bar(position, finnetcflow, width/2,label='finance cash net flow')

def draw_cfs_subplot(ax):
    width = 0.1
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

    ind = np.arange(len(t))  # the x locations for the groups
    draw_cfs_biz_cash_bar(ax, ind, width*2, bizcashinfl, bizcashoutf, mananetr)
    draw_cfs_invest_cash_bar(ax, ind + 2 * width, width*2, invcashinfl, invcashoutf, invnetcashflow)
    draw_cfs_finance_cash_bar(ax,ind + 4 * width,width*2,fincashinfl,fincashoutf,finnetcflow)

    ax.set_xticks(ind + width / 6)
    ax.set_xticklabels(t)
    for tick in ax.get_xticklabels():
        tick.set_rotation(90)
    ax.legend(loc='upper right')


if __name__ == "__main__":
    dfo = pd.read_excel('../data/cfs1.xls', skiprows=1)
    plt.style.use('ggplot')
    df = dfo[dfo['code'] == 'SZ000333']
    df.fillna(0, inplace=True)
    fig, ax = plt.subplots(figsize=(120, 8))
    draw_cfs_subplot(ax)
    plt.show()

