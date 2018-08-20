import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import axes3d


def config_is_cfs_subplot(ax,df_cfs,df_is):
    width = 0.12
    # cfs var
    t = df_cfs['enddate']
    opcashinfl = df_cfs['bizcashinfl']
    opcashoutf = df_cfs['bizcashoutf']
    mananetr = df_cfs['mananetr']

    invcashinfl = df_cfs['invcashinfl']
    invcashoutf = df_cfs['invcashoutf']
    invnetcashflow = df_cfs['invnetcashflow']

    fincashinfl = df_cfs['fincashinfl']
    fincashoutf = df_cfs['fincashoutf']
    finnetcflow = df_cfs['finnetcflow']




    # is var
    t = df_is['enddate']
    bti = df_is['biztotinco']
    bi = df_is['bizinco']
    inteinco = df_is['inteinco']
    pouninco = df_is['pouninco']
    otherbizinco = df_is['otherbizinco']
    btc = df_is['biztotcost']
    bc = df_is['bizcost']
    pp = df_is['perprofit']
    biztax = df_is['biztax']
    salesexpe = df_is['salesexpe']
    manaexpe = df_is['manaexpe']
    finexpe = df_is['finexpe']
    asseimpaloss = df_is['asseimpaloss']
    inveinco = df_is['inveinco']
    nonoreve = df_is['nonoreve']
    nonoexpe = df_is['nonoexpe']
    noncassetsdisl = df_is['noncassetsdisl']
    incotaxexpe = df_is['incotaxexpe']
    netprofit = df_is['netprofit']

    ind = np.arange(len(t))  # the x locations for the groups

    # bar1 inco
    # btib = ax.bar(ind, bti, width*8,color='silver')

    # bar 2 inco
    bar2_position=ind
    bizincob = ax.bar(bar2_position, bi, width*6, bottom=inveinco + pouninco + inteinco + otherbizinco,color='salmon')
    otherbizincob = ax.bar(bar2_position, otherbizinco, width*6, bottom=inveinco + pouninco + inteinco,color='lightcoral')
    inteincob = ax.bar(bar2_position, inteinco, width*6, bottom=inveinco + pouninco,color='yellow')
    pounincob = ax.bar(bar2_position, pouninco, width*6, bottom=inveinco,color='khaki')
    inveincob = ax.bar(bar2_position, inveinco, width*6,color='gold')

    # bar 3 co
    # bar3_position=ind - 3 * width
    # rects3 = ax.bar(bar3_position, btc, width, bottom=pp,color='blue')

    # bar 4 co
    bar4_position=ind -2 * width
    bcb = ax.bar(bar4_position, bc, width, bottom=pp + asseimpaloss + finexpe + manaexpe + salesexpe + biztax,color='blue')
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
    df_cfs = pd.read_excel('../data/cfs_SZ000333.xlsx')#, skiprows=1
    df_is = pd.read_excel('../data/is_SZ000333.xlsx')
    df_cfs.fillna(0, inplace=True)
    df_is.fillna(0,inplace=True)
    fig, ax = plt.subplots(figsize=(20, 8))
    config_is_cfs_subplot(ax,df_cfs,df_is)
    plt.show()

