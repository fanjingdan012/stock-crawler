import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import axes3d
import industry

def config_is_cfs_subplot(ax,df):
    width = 0.12
    # cfs var

    stock_code = df['code']
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

    bar4_position=ind -1.5 * width

    bcb = ax.bar(bar4_position, bc, width*2, bottom=pp + asseimpaloss + finexpe + manaexpe + salesexpe + biztax,color='skyblue')
    biztaxb = ax.bar(bar4_position, biztax, width*2, bottom=pp + asseimpaloss + finexpe + manaexpe + salesexpe,color='navy')
    salesexpeb = ax.bar(bar4_position, salesexpe, width*2, bottom=pp + asseimpaloss + finexpe + manaexpe,color='dodgerblue')
    manaexpeb = ax.bar(bar4_position, manaexpe, width*2, bottom=pp + asseimpaloss + finexpe,color='lightskyblue')
    finexpeb = ax.bar(bar4_position, finexpe, width*2, bottom=pp + asseimpaloss,color='palegreen')
    asseimpalossb = ax.bar(bar4_position, asseimpaloss, width*2, bottom=pp,color='cornflowerblue')
    ppb = ax.bar(bar4_position, pp, width*2,color='purple')



    # bar 6 co
    bar5_position = bar4_position

    # nonoreveb = ax.bar(bar2_position, nonoreve, width * 6, bottom=inveinco + pouninco + inteinco + otherbizinco,
    #                    color='black')
    #
    # nonoexpeb = ax.bar(bar5_position, nonoexpe, width, bottom=netprofit + incotaxexpe + noncassetsdisl,color='darkslateblue')
    nonopb=ax.bar(bar5_position, nonoreve-nonoexpe, width, bottom=netprofit + incotaxexpe + noncassetsdisl,color='darkslateblue')

    noncassetsdislb = ax.bar(bar5_position, noncassetsdisl, width, bottom=netprofit + incotaxexpe,color='darkblue')
    incotaxexpeb = ax.bar(bar5_position, incotaxexpe, width, bottom=netprofit,color='black')
    netprofitb = ax.bar(bar5_position, netprofit, width,color='m')

    # cfs bars
    # bar 7 cfs op cash in
    bar6_position=ind+1.5*width
    opcashinflb = ax.bar(bar6_position, opcashinfl, width*2, color='salmon')
    #bar 8 cfs op cash out + op cash net
    opcashoutfb = ax.bar(bar6_position, opcashoutf, width, bottom=mananetr, color='skyblue')
    mananetrb = ax.bar(bar6_position, mananetr, width, color='darkviolet')

    # invcashinflb = ax.bar(ind + 2 * width, invcashinfl, width)
    # invcashoutfb = ax.bar(ind + 3 * width, invcashoutf, width, bottom=invnetcashflow)
    # invnetcashflowb = ax.bar(ind + 3 * width, invnetcashflow, width)
    #
    # fincashinflb = ax.bar(ind + 4 * width, fincashinfl, width)
    # fincashoutfb = ax.bar(ind + 5 * width, fincashoutf, width, bottom=finnetcflow)
    # finnetcflowb = ax.bar(ind + 5 * width, finnetcflow, width)

    ax.set_xticks(ind )
    ax.set_xticklabels(stock_code)
    for tick2 in ax.get_xticklabels():
        tick2.set_rotation(90)

def merge_is_cfs():
    df_cfs_all = pd.read_excel('../data/cfs_采掘行业.xlsx')
    df_is_all = pd.read_excel('../data/is_采掘行业.xlsx')
    df_is_cfs = pd.merge(df_cfs_all, df_is_all, left_on=['code','enddate'], right_on = ['code','enddate'],copy=True, indicator='both',suffixes=('_cfs','_is'))
    df_is_cfs.to_excel('../data/is_cfs_采掘行业.xlsx')


if __name__ == "__main__":
    plt.style.use('ggplot')

    #caijue
    stock_code_list = ["SZ000552", "SZ000571", "SZ000655", "SZ000723", "SZ000762", "SZ000780", "SZ000937", "SZ000968",
                       "SZ000983", "SZ002128", "SZ002207", "SZ002554", "SZ002629", "SZ002738", "SZ002828", "SZ300157",
                       "SZ300164", "SZ300191", "SH600121", "SH600123", "SH600157", "SH600188", "SH600295", "SH600339",
                       "SH600348", "SH600395", "SH600397", "SH600403", "SH600408", "SH600508", "SH600532", "SH600546",
                       "SH600583", "SH600725", "SH600740", "SH600758", "SH600759", "SH600777", "SH600792", "SH600871",
                       "SH600971", "SH600997", "SH601001", "SH601011", "SH601015", "SH601088", "SH601101", "SH601225",
                       "SH601666", "SH601699", "SH601808", "SH601857", "SH601898", "SH601918", "SH601969", "SH603113",
                       "SH603505", "SH603619", "SH603727", "SH603979"]

    # industry.collect_reports_for_industry(stock_code_list)


    df_is_cfs = pd.read_excel('../data/is_cfs_采掘行业.xlsx',converters={'enddate':str})
    # df_is_cfs.fillna(0, inplace=True)
    # print(df_is_cfs.keys())
    df_is_cfs=df_is_cfs[df_is_cfs['enddate']=='20161231']
    # df_is_cfs = df_is_cfs[df_is_cfs['code']=='SZ000552']
    fig, ax = plt.subplots(figsize=(20, 8))
    # print(df_is_cfs)
    config_is_cfs_subplot(ax,df_is_cfs)
    plt.show()

