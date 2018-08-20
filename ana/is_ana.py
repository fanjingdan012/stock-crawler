import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import axes3d

# def config_is_subplot1(ax):




def config_is_subplot(ax2):
    # inco o
    bizincob2 = ax2.bar(ind , bi, width*6, bottom=otherbizinco, color='silver')
    otherbizincob2 = ax2.bar(ind , otherbizinco, width*6,color='g' )
    # co o
    bcb2 = ax2.bar(ind + width, -bc, width,bottom=otherbizinco+bi)
    biztaxb2 = ax2.bar(ind + width, -biztax, width,bottom=otherbizinco+bi-bc)
    salesexpeb2 = ax2.bar(ind + width, -salesexpe, width,bottom=otherbizinco+bi-bc-biztax)
    manaexpeb2 = ax2.bar(ind + width, -manaexpe, width,bottom=otherbizinco+bi-bc-biztax-salesexpe)

    # inco f
    inteincob2 = ax2.bar(ind + 2*width, inteinco, width,bottom=noncassetsdisl+nonoreve+inveinco+pouninco)
    pounincob2 = ax2.bar(ind + 2*width, pouninco, width,bottom=noncassetsdisl+nonoreve+inveinco)
    inveincob2 = ax2.bar(ind + 2*width, inveinco, width,bottom=noncassetsdisl+nonoreve)
    nonoreveb2 = ax2.bar(ind + 2*width, nonoreve, width,bottom=noncassetsdisl)
    noncassetsdislb2 = ax2.bar(ind + 2*width, noncassetsdisl, width)
    # co f
    finexpeb2 = ax2.bar(ind + 3*width, finexpe, width,bottom=incotaxexpe+nonoexpe+asseimpaloss)
    asseimpalossb2 = ax2.bar(ind + 3*width, asseimpaloss, width,bottom=incotaxexpe+nonoexpe)
    nonoexpeb2 = ax2.bar(ind + 3*width, nonoexpe, width,bottom=incotaxexpe)
    incotaxexpeb2 = ax2.bar(ind + 3*width, incotaxexpe, width)
    # netprofitb    = ax.bar(ind + 5*width, netprofit, width)
    # ppb2 = ax2.bar(ind +width, pp, width, color='y')

if __name__ == "__main__":
    plt.style.use('ggplot')

    dfo = pd.read_excel('../data/is_SZ000333.xlsx')
    df = dfo#[dfo['code']=='SH600983']
    df.fillna(0,inplace=True)
    # fig, ax = plt.subplots(figsize=(120,8))
    fig = plt.figure()
    ax = fig.add_subplot(211)
    width=0.1
    t = df['enddate']
    bti = df['biztotinco']
    bi=df['bizinco']
    inteinco=df['inteinco']
    pouninco=df['pouninco']
    otherbizinco= df['otherbizinco']
    btc = df['biztotcost']
    bc = df['bizcost']
    pp= df['perprofit']
    biztax= df['biztax']
    salesexpe= df['salesexpe']
    manaexpe= df['manaexpe']
    finexpe= df['finexpe']
    asseimpaloss= df['asseimpaloss']
    inveinco= df['inveinco']
    nonoreve= df['nonoreve']
    nonoexpe= df['nonoexpe']
    noncassetsdisl= df['noncassetsdisl']
    incotaxexpe= df['incotaxexpe']
    netprofit= df['netprofit']



    ind = np.arange(len(t))  # the x locations for the groups
    # bar1 inco
    rects1 = ax.bar(ind, bti, width)
    # bar 2 inco
    bizincob = ax.bar(ind + width, bi, width, bottom=inveinco+pouninco+inteinco+otherbizinco)
    otherbizincob = ax.bar(ind + width, otherbizinco, width, bottom=inveinco+pouninco+inteinco)
    inteincob = ax.bar(ind + width, inteinco, width,bottom=inveinco+pouninco)
    pounincob = ax.bar(ind + width, pouninco, width,bottom=inveinco)
    inveincob = ax.bar(ind + width, inveinco, width)
    # bar 3 co
    rects3 = ax.bar(ind + 2*width, btc, width,bottom=pp)
    # bar 4 co
    rects4 = ax.bar(ind + 3*width, bc, width,bottom=pp+asseimpaloss+finexpe+manaexpe+salesexpe+biztax)
    biztaxb = ax.bar(ind + 3*width, biztax, width,bottom=pp+asseimpaloss+finexpe+manaexpe+salesexpe)
    salesexpeb = ax.bar(ind + 3*width, salesexpe, width,bottom=pp+asseimpaloss+finexpe+manaexpe)
    manaexpeb = ax.bar(ind + 3*width, manaexpe, width,bottom=pp+asseimpaloss+finexpe)
    finexpeb = ax.bar(ind + 3*width, finexpe, width,bottom=pp+asseimpaloss)
    asseimpalossb = ax.bar(ind + 3*width, asseimpaloss, width,bottom=pp)
    ppb    = ax.bar(ind + 3*width, pp, width)
    # bar 5 inco
    nonoreveb = ax.bar(ind + 4*width, nonoreve, width,bottom=pp)
    # bar 6 co
    nonoexpeb = ax.bar(ind + 5*width, nonoexpe, width,bottom=netprofit+incotaxexpe+noncassetsdisl)
    noncassetsdislb = ax.bar(ind + 5*width, noncassetsdisl, width,bottom=netprofit+incotaxexpe)
    incotaxexpeb = ax.bar(ind + 5*width, incotaxexpe, width,bottom=netprofit)
    netprofitb    = ax.bar(ind + 5*width, netprofit, width)

    ax.set_xticks(ind + width / 6)
    ax.set_xticklabels(t)


    # ax2 managing is
    ax2 = fig.add_subplot(212)

    config_is_subplot(ax2)


    ax.set_xticks(ind + width / 2)
    ax.set_xticklabels(t)
    plt.show()
