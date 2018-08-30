import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import axes3d
import chart.is_chart as is_chart
import chart.cfs_chart as cfs_chart
from matplotlib.font_manager import FontProperties
import matplotlib
# matplotlib.use('Agg')
import industry
import stock_reader
import data_preprocessor

def draw_profitablity_subplot_for_year(str_reportdate):
    plt.style.use('ggplot')
    dfo = pd.read_excel('../data/is_cfs_bs_begin_房地产.xlsx', converters={'reportdate': str})
    # df = dfo[dfo['stock_code']=='SH600983']
    dfo = dfo[dfo['exists'] == 'both']
    df = dfo[dfo['reportdate'] == str_reportdate]
    # df.fillna(0,inplace=True)
    fig, ax = plt.subplots(figsize=(120, 8))
    # fig = plt.figure()
    ax = fig.add_subplot(111)
    width = 0.1
    # t = df['reportdate']
    stock_code = df['stock_code']
    stock_name = df['stock_name']
    # bti = df['biztotinco']
    # bi=df['bizinco']
    # inteinco=df['inteinco']
    # pouninco=df['pouninco']
    # otherbizinco= df['otherbizinco']
    # btc = df['biztotcost']
    # bc = df['bizcost']
    # pp= df['perprofit']
    # biztax= df['biztax']
    # salesexpe= df['salesexpe']
    # manaexpe= df['manaexpe']
    # finexpe= df['finexpe']
    # asseimpaloss= df['asseimpaloss']
    # inveinco= df['inveinco']
    # nonoreve= df['nonoreve']
    # nonoexpe= df['nonoexpe']
    # noncassetsdisl= df['noncassetsdisl']
    # incotaxexpe= df['incotaxexpe']
    # netprofit= df['netprofit']
    # print(dfo)
    roe = df['roe']
    roa = df['roa']
    ni_div_sr = df['ni_div_sr']
    sr_div_a = df['sr_div_a']

    ind = np.arange(len(stock_code))  # the x locations for the groups
    x = [0, 1]
    y = [0, 1]
    ax.plot(ind, roe, color='red', label='roe')
    ax.plot(ind, roa, color='yellow', label='roa')
    ax.plot(ind, ni_div_sr, color='green', label='ni/sr')
    ax.plot(ind, sr_div_a, color='blue', label='sr/a')
    ax.legend()
    # plt.plot(x, y)
    ax.set_xticks(ind + width / 2)
    font = FontProperties(fname=r"C:\\windows\\fonts\\simsun.ttc")
    ax.set_xticklabels(stock_code + "_" + stock_name, size='small', rotation=90, fontproperties=font)
    plt.show()

def draw_profitablity_subplot_for_stock(str_stock_code):
    plt.style.use('ggplot')
    dfo = pd.read_excel('../data/is_cfs_bs_begin_房地产.xlsx', converters={'reportdate': str})
    # df = dfo[dfo['stock_code']=='SH600983']
    dfo = dfo[dfo['exists'] == 'both']
    df = dfo[dfo['stock_code'] == str_stock_code]
    # df.fillna(0,inplace=True)
    fig, ax = plt.subplots(figsize=(120, 8))
    # fig = plt.figure()
    ax = fig.add_subplot(111)
    width = 0.1
    t = df['reportdate']
    stock_code = df['stock_code']
    stock_name = df['stock_name']
    # bti = df['biztotinco']
    # bi=df['bizinco']
    # inteinco=df['inteinco']
    # pouninco=df['pouninco']
    # otherbizinco= df['otherbizinco']
    # btc = df['biztotcost']
    # bc = df['bizcost']
    # pp= df['perprofit']
    # biztax= df['biztax']
    # salesexpe= df['salesexpe']
    # manaexpe= df['manaexpe']
    # finexpe= df['finexpe']
    # asseimpaloss= df['asseimpaloss']
    # inveinco= df['inveinco']
    # nonoreve= df['nonoreve']
    # nonoexpe= df['nonoexpe']
    # noncassetsdisl= df['noncassetsdisl']
    # incotaxexpe= df['incotaxexpe']
    # netprofit= df['netprofit']
    # print(dfo)
    roe = df['roe']
    roa = df['roa']
    ni_div_sr = df['ni_div_sr']
    sr_div_a = df['sr_div_a']

    ind = np.arange(len(t))  # the x locations for the groups
    x = [0, 1]
    y = [0, 1]
    ax.plot(ind, roe, color='red', label='roe')
    ax.plot(ind, roa, color='yellow', label='roa')
    ax.plot(ind, ni_div_sr, color='green', label='ni/sr')
    ax.plot(ind, sr_div_a, color='blue', label='sr/a')
    ax.legend()
    # plt.plot(x, y)
    ax.set_xticks(ind + width / 2)
    font = FontProperties(fname=r"C:\\windows\\fonts\\simsun.ttc")
    ax.set_xticklabels(t, size='small', rotation=90, fontproperties=font)
    plt.show()
if __name__ == "__main__":
    # draw_profitablity_subplot_for_year('20161231')
    draw_profitablity_subplot_for_stock('SZ000002')

