from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import style


def draw_bs_bars(ax,position,width,ca,la,cl,ll,e):
    current_asset_bar = ax.bar(position, ca, width, bottom=la, label='current asset')
    long_term_asset_bar = ax.bar(position, la, width, label='long term asset bar')
    equity_bar = ax.bar(position + width, e, width, color='y',label='equity')
    long_term_liability_bar = ax.bar(position + width, ll, width, bottom=e, color='b',label='long term liability')
    current_liability_bar = ax.bar(position + width, cl, width, bottom=e + ll,label='current liability')


def draw_bs_subplot(ax,df):
    width = 0.3
    t = df['reportdate']
    a = df['totasset']
    ca = df['totcurrasset']
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


if __name__ == '__main__':

    style.use('ggplot')
    dfo=pd.read_excel('../data/bs_SH600795.xlsx')

    # fig, ax = plt.subplots(figsize=(15,8))
    fig = plt.figure()
    ax = fig.add_subplot(211)
    draw_bs_subplot(ax,dfo)


    ax2 = fig.add_subplot(212)
    width=0.3
    df2 = pd.read_excel('../data/bs_SZ002172.xlsx')# dfo#[dfo['code']=='SZ002287']

    draw_bs_subplot(ax2, df2)
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

