from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"C:\\windows\\fonts\\simsun.ttc")

# plt.plot([1,2,3])
# plt.title(u"测试",fontproperties=font)

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import style
import bs_chart
if __name__ == "__main__":
    style.use('ggplot')
    dateparse = lambda dates: pd.datetime.strptime(dates, '%Y%m%d')
    dfo=pd.read_excel('../data/bs_化工行业.xls',skiprows=1,parse_dates=['reportdate'],date_parser=dateparse)
    # fig, ax = plt.subplots(figsize=(15,8))
    fig = plt.figure()
    ax = fig.add_subplot(211)
    width=0.3
    df = dfo[dfo['reportdate']=='20170930']
    df.fillna(0, inplace=True)
    name = df['name']
    a = df['totasset']
    ca = df['totcurrasset']
    la = df['totalnoncassets']
    ind = np.arange(len(name))  # the x locations for the groups
    b=df['totliabsharequi']
    cl=df['totalcurrliab']
    ll=df['totalnoncliab']
    l=df['totliab']
    e=df['righaggr']
    bs_chart.draw_bs_bars(ax, ind, width, ca, la, cl, ll, e)

    ax.set_xticks(ind + width / 2)
    ax.set_xticklabels(name,size='small',rotation=90,fontproperties=font)




    ax2 = fig.add_subplot(212)
    width=0.3
    df2 = dfo[dfo['code']=='SH600618']
    bs_chart.draw_bs_subplot(ax2, df2)

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

