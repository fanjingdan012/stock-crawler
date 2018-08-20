import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import axes3d


def config_is_cfs_subplot(ax,df):
    width = 0.12
    # cfs var
    t = df['enddate']
    opcashinfl = df['bizcashinfl']
    opcashoutf = df['bizcashoutf']
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
    bizincob = ax.bar(bar2_position, bi, width*6, bottom=inveinco + pouninco + inteinco + otherbizinco,color='pink')
    otherbizincob = ax.bar(bar2_position, otherbizinco, width*6, bottom=inveinco + pouninco + inteinco,color='lightcoral')
    inteincob = ax.bar(bar2_position, inteinco, width*6, bottom=inveinco + pouninco,color='yellow')
    pounincob = ax.bar(bar2_position, pouninco, width*6, bottom=inveinco,color='khaki')
    inveincob = ax.bar(bar2_position, inveinco, width*6,color='gold')

    # bar 3 co
    # bar3_position=ind - 3 * width
    # rects3 = ax.bar(bar3_position, btc, width, bottom=pp,color='blue')

    # bar 4 co
    bar4_position=ind -2 * width
    bcb = ax.bar(bar4_position, bc, width, bottom=pp + asseimpaloss + finexpe + manaexpe + salesexpe + biztax,color='lightskyblue')
    biztaxb = ax.bar(bar4_position, biztax, width, bottom=pp + asseimpaloss + finexpe + manaexpe + salesexpe,color='navy')
    salesexpeb = ax.bar(bar4_position, salesexpe, width, bottom=pp + asseimpaloss + finexpe + manaexpe,color='royalblue')
    manaexpeb = ax.bar(bar4_position, manaexpe, width, bottom=pp + asseimpaloss + finexpe,color='mediumblue')
    finexpeb = ax.bar(bar4_position, finexpe, width, bottom=pp + asseimpaloss,color='green')
    asseimpalossb = ax.bar(bar4_position, asseimpaloss, width, bottom=pp,color='cornflowerblue')
    ppb = ax.bar(bar4_position, pp, width,color='purple')

    # bar 5 inco
    nonoreveb = ax.bar(ind -1 * width, nonoreve, width, bottom=pp,color='black')

    # bar 6 co
    bar5_position = ind
    nonoexpeb = ax.bar(bar5_position, nonoexpe, width, bottom=netprofit + incotaxexpe + noncassetsdisl,color='darkslateblue')
    noncassetsdislb = ax.bar(bar5_position, noncassetsdisl, width, bottom=netprofit + incotaxexpe,color='darkblue')
    incotaxexpeb = ax.bar(bar5_position, incotaxexpe, width, bottom=netprofit,color='black')
    netprofitb = ax.bar(bar5_position, netprofit, width,color='m')

    # cfs bars
    # bar 7 cfs op cash in
    opcashinflb = ax.bar(ind + 1 * width, opcashinfl, width, color='red')
    #bar 8 cfs op cash out + op cash net
    opcashoutfb = ax.bar(ind + 2 * width, opcashoutf, width, bottom=mananetr, color='blue')
    mananetrb = ax.bar(ind + 2 * width, mananetr, width, color='purple')

    # invcashinflb = ax.bar(ind + 2 * width, invcashinfl, width)
    # invcashoutfb = ax.bar(ind + 3 * width, invcashoutf, width, bottom=invnetcashflow)
    # invnetcashflowb = ax.bar(ind + 3 * width, invnetcashflow, width)
    #
    # fincashinflb = ax.bar(ind + 4 * width, fincashinfl, width)
    # fincashoutfb = ax.bar(ind + 5 * width, fincashoutf, width, bottom=finnetcflow)
    # finnetcflowb = ax.bar(ind + 5 * width, finnetcflow, width)

    ax.set_xticks(ind )
    ax.set_xticklabels(t)
    for tick2 in ax.get_xticklabels():
        tick2.set_rotation(90)


if __name__ == "__main__":
    plt.style.use('ggplot')
    df_cfs = pd.read_excel('../data/cfs_SH600839.xlsx')#, skiprows=1
    df_is = pd.read_excel('../data/is_SH600839.xlsx')
    df_cfs.fillna(0, inplace=True)
    df_is.fillna(0, inplace=True)
    # print(df_cfs.keys())

    df_is_cfs = pd.merge(df_cfs, df_is, on='enddate',copy=True, indicator='both',suffixes=('_cfs','_is'))
    # df_is_cfs.to_excel('../data/is_cfs_SH600839.xlsx')
    # df_is_cfs.fillna(0, inplace=True)
    # print(df_is_cfs.keys())
    # df_is_cfs=[df_is_cfs['enddate']>'20080331']
    fig, ax = plt.subplots(figsize=(20, 8))
    config_is_cfs_subplot(ax,df_is_cfs)
    plt.show()

