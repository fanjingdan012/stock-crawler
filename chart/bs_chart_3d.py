from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import chart.bs_chart as bs_chart

def mm():

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for c, z in zip(['r', 'g', 'b', 'y'], [30, 20, 10, 0]):
        xs = np.arange(20)
        ys = np.random.rand(20)

        # You can provide either a single color or an array. To demonstrate this,
        # the first bar of each set will be colored cyan.
        cs = [c] * len(xs)
        cs[0] = 'c'
        ax.bar(xs, ys, zs=z, zdir='y', color=cs, alpha=0.8)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()

if __name__ == '__main__':



    # fig, ax = plt.subplots(figsize=(15,8))

    # dateparse = lambda dates: pd.datetime.strptime(dates, '%Y%m%d')
    # dfo = pd.read_excel('../data/bs_化工行业.xls', skiprows=1, parse_dates=['reportdate'], date_parser=dateparse)
    dfo = pd.read_excel('../data/bs_化工行业.xls', skiprows=1)

    dfo.fillna(0, inplace=True)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # df = dfo[dfo['reportdate'] == '20170930']
    # bs_chart.draw_industry_bs_subplot(ax,dfo)
    df = dfo
    for t in  df['reportdate']:
        xs = np.arange(20)
        ys = np.random.rand(20)
        width = 0.3

        name = df['name']
        a = df['totasset']
        ca = df['totcurrasset']
        la = df['totalnoncassets']
        ind = np.arange(len(name))  # the x locations for the groups
        b = df['totliabsharequi']
        cl = df['totalcurrliab']
        ll = df['totalnoncliab']
        l = df['totliab']
        e = df['righaggr']

        position=ind
        # current_asset_bar = ax.bar(position, ca, width, bottom=la, label='current asset')
        # long_term_asset_bar = ax.bar(position, la, width, label='long term asset bar')
        # equity_bar = ax.bar(position + width, e, width, color='y', label='equity')
        # long_term_liability_bar = ax.bar(position + width, ll, width, bottom=e, color='b', label='long term liability')
        # current_liability_bar = ax.bar(position + width, cl, width, bottom=e + ll, label='current liability')
        equity_bar = ax.bar(position + width, e,zs=t, zdir='y', color='y', label='equity')
        # ax.set_xticks(ind + width / 2)
        # font = FontProperties(fname=r"C:\\windows\\fonts\\simsun.ttc")
        # ax.set_xticklabels(name, size='small', rotation=90, fontproperties=font)
        # ax.legend(loc='upper right')

        # ax.bar(xs, ys, zs=z, zdir='y',  alpha=0.8)

    plt.show()
