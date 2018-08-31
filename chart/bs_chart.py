# -*- coding: utf-8 -*-
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

def draw_detailed_current_asset_bars(ax,position,width,curfds,tradfinasset,notesrece,accorece,prep,
                                     premrece,interece,dividrece,otherrece,expotaxrebarece,subsrece,
                                     margrece,intelrece,inve,prepexpe,unseg,expinoncurrasset,othercurrasse,
                                     currassetitse,currasseform,la):
    num_bottom=la
    ax.bar(position + width, currasseform, width, bottom=num_bottom, label='current asset form')
    num_bottom+=currasseform
    ax.bar(position + width, currassetitse, width, bottom=num_bottom, label='current asset itse')
    num_bottom += currassetitse
    ax.bar(position + width, othercurrasse, width, bottom=num_bottom, label='other Current Asset')

    num_bottom += othercurrasse
    ax.bar(position + width, expinoncurrasset, width, bottom=num_bottom,
           label='exp in one year non Current Asset')

    num_bottom += expinoncurrasset
    ax.bar(position + width, unseg, width, bottom=num_bottom,
           label='Current Asset Profit & loss of assets pending disposal')

    num_bottom += unseg
    ax.bar(position + width, prepexpe, width,
           bottom=num_bottom,
           label='unamortized expense')
    num_bottom += prepexpe

    num_bottom=draw_bar(ax,position+width,inve,width,num_bottom,'inventory')
    ax.bar(position + width, intelrece, width, label='internal receivable', bottom=num_bottom)
    num_bottom += intelrece
    ax.bar(position + width, margrece, width, bottom=num_bottom, label='marg receivable')
    num_bottom += margrece
    ax.bar(position + width, subsrece, width, bottom=num_bottom, label='subs receivable')
    num_bottom += subsrece
    ax.bar(position + width, expotaxrebarece, width, bottom=num_bottom, label='export tax reba receivable')
    num_bottom += expotaxrebarece
    ax.bar(position + width, otherrece, width, bottom=num_bottom, label='other receivable')
    num_bottom += otherrece
    ax.bar(position + width, dividrece, width, bottom=num_bottom, label='dividend receivable')
    num_bottom += dividrece

    ax.bar(position + width, interece, width, bottom=num_bottom, label='interest receivable')

    num_bottom += interece
    ax.bar(position + width, premrece, width, bottom=num_bottom, label='premium receivable')

    num_bottom += premrece
    ax.bar(position + width, prep, width, bottom=num_bottom, label='prepayments')

    num_bottom += prep
    ax.bar(position + width, accorece, width, bottom=num_bottom, label='accounts receivable')
    num_bottom += accorece
    ax.bar(position + width, notesrece, width, bottom=num_bottom,label='notes receivable')
    num_bottom += notesrece
    ax.bar(position + width, tradfinasset, width, bottom=num_bottom,label='trade finance asset')
    num_bottom += tradfinasset
    ax.bar(position + width, curfds, width, bottom=num_bottom,label='cash')

# 非流动资产合计	特殊处理本身不平总资产	特殊处理格式不同总资产	资产总计	短期借款	交易性金融负债	应付票据	应付账款	预收款项	应付职工薪酬	应交税费	应付利息	应付股利	其他应交款	应付保证金	内部应付款	其他应付款	预提费用	预计流动负债	应付分保账款	国际票证结算	国内票证结算	一年内的递延收益	应付短期债券	一年内到期的非流动负债	其他流动负债	特殊处理本身不平流动负债	特殊处理格式不同流动负债	流动负债合计	长期借款	应付债券	长期应付款	专项应付款	预计非流动负债	长期递延收益	递延所得税负债	其他非流动负债	特殊处理本身不平长期负债	特殊处理格式不同长期负债	非流动负债合计	特殊处理本身不平负债合计	特殊处理格式不同负债合计	负债合计	实收资本(或股本)	资本公积	减：库存股	专项储备	盈余公积	一般风险准备	未确定的投资损失	未分配利润	拟分配现金股利	外币报表折算差额	特殊处理本身不平股东权益	特殊处理格式不同股东权益	归属于母公司股东权益合计	少数股东权益	特殊处理本身不平股东权益	特殊处理格式不平股东权益	所有者权益(或股东权益)合计	特殊处理本身不平负债及权益	特殊处理格式不同负债及权益	负债和所有者权益	结算备付金	拆出资金	衍生金融资产	应收分保账款	应收分保合同准备金	买入返售金融资产	向中央银行借款	吸收存款及同业存放	拆入资金	衍生金融负债	卖出回购金融资产款	应付手续费及佣金	保险合同准备金	代理买卖证券款	代理承销证券款
# ,totalnoncassets	totassetitse	totalasseform	totasset
# 固定资产原值	累计折旧	固定资产净值	固定资产减值准备
# fixedasseimmo	accudepr	fixedassenetw	fixedasseimpa
def draw_detailed_long_term_asset_bars(ax,position,width,
                                       lendandloan,avaisellasse,holdinvedue,longrece,equiinve,otherlonginve,
                                       inveprop,fixedassenet,consprog,engimate,fixedasseclea,prodasse,comasse,
                                       hydrasset,intaasset,deveexpe,goodwill,logprepexpe,tradshartrad,
                                       defetaxasset,othernoncasse,noncasseitse,noncasseform):
    ax.bar(position, noncasseform, width, label='non current asset form')
    num_bottom=noncasseform
    num_bottom = draw_bar(ax, position, noncasseitse, width, num_bottom, 'non current asset itse')
    num_bottom = draw_bar(ax, position, othernoncasse, width, num_bottom, 'other non current asset')
    num_bottom = draw_bar(ax, position, defetaxasset, width, num_bottom, 'deferred income tax asset')
    num_bottom = draw_bar(ax, position, tradshartrad, width, num_bottom, 'trad share trad')#股权分置流通权
    num_bottom = draw_bar(ax, position, logprepexpe, width, num_bottom, 'Long-term prepaid expenses')
    num_bottom = draw_bar(ax, position, deveexpe, width, num_bottom, 'develop expense')
    num_bottom = draw_bar(ax, position, intaasset, width, num_bottom, 'Intangible assets')
    num_bottom = draw_bar(ax, position, hydrasset, width, num_bottom, 'oil and gas asset')
    num_bottom = draw_bar(ax, position, comasse, width, num_bottom, 'common bio asset')
    num_bottom = draw_bar(ax, position, prodasse, width, num_bottom, 'production bio asset')
    num_bottom = draw_bar(ax, position, fixedasseclea, width, num_bottom, 'fixed asset clean up')
    num_bottom = draw_bar(ax, position, engimate, width, num_bottom, 'engineer material')
    num_bottom = draw_bar(ax, position, consprog, width, num_bottom, 'Construction in progress')
    num_bottom = draw_bar(ax, position, fixedassenet, width, num_bottom, 'fixed asset')
    num_bottom = draw_bar(ax, position, inveprop, width, num_bottom, 'investment property')
    num_bottom = draw_bar(ax, position, otherlonginve, width, num_bottom, 'other long term investment')
    num_bottom = draw_bar(ax, position, equiinve, width, num_bottom, 'long term equity investment')
    num_bottom = draw_bar(ax, position, longrece, width, num_bottom, 'long term receivable')
    num_bottom = draw_bar(ax, position, holdinvedue, width, num_bottom, 'yield to maturity')
    num_bottom = draw_bar(ax, position, avaisellasse, width, num_bottom, 'available for sale finance asset')
    num_bottom = draw_bar(ax, position, lendandloan, width, num_bottom, 'loan')


# 短期借款	交易性金融负债	应付票据	应付账款	预收款项	应付职工薪酬	应交税费	应付利息	应付股利	其他应交款	应付保证金	内部应付款	其他应付款	预提费用	预计流动负债	应付分保账款	国际票证结算	国内票证结算	一年内的递延收益	应付短期债券	一年内到期的非流动负债	其他流动负债	特殊处理本身不平流动负债	特殊处理格式不同流动负债	流动负债合计
#  		totalcurrliab
def draw_detailed_current_liability_bars(ax,position,width,
                                         shorttermborr, tradfinliab, notespaya, accopaya, advapaym, copeworkersal,
                                         taxespaya, intepaya, divipaya, otherfeepaya,margrequ,intelpay,otherpay,accrexpe,
                                         expecurrliab,copewithreinrece,inteticksett,dometicksett,defereve,shorttermbdspaya,
                                         duenoncliab,othercurreliabi,currliabitse,currliabform,num_bottom):
    num_bottom=num_bottom
    num_bottom = draw_bar(ax, position, currliabform, width, num_bottom, 'non current asset itse')
    num_bottom = draw_bar(ax, position, currliabitse, width, num_bottom, 'other non current asset')
    num_bottom = draw_bar(ax, position, othercurreliabi, width, num_bottom, 'other current liability')
    num_bottom = draw_bar(ax, position, duenoncliab, width, num_bottom, 'trad share trad')
    num_bottom = draw_bar(ax, position, shorttermbdspaya, width, num_bottom, 'Long-term prepaid expenses')
    num_bottom = draw_bar(ax, position, defereve, width, num_bottom, 'develop expense')
    num_bottom = draw_bar(ax, position, dometicksett, width, num_bottom, 'Intangible assets')
    num_bottom = draw_bar(ax, position, inteticksett, width, num_bottom, 'oil and gas asset')
    num_bottom = draw_bar(ax, position, copewithreinrece, width, num_bottom, 'common bio asset')
    num_bottom = draw_bar(ax, position, expecurrliab, width, num_bottom, 'production bio asset')
    num_bottom = draw_bar(ax, position, accrexpe, width, num_bottom, 'fixed asset clean up')
    num_bottom = draw_bar(ax, position, otherpay, width, num_bottom, 'engineer material')
    num_bottom = draw_bar(ax, position, intelpay, width, num_bottom, 'Construction in progress')
    num_bottom = draw_bar(ax, position, margrequ, width, num_bottom, 'fixed asset')
    num_bottom = draw_bar(ax, position, otherfeepaya, width, num_bottom, 'investment property')
    num_bottom = draw_bar(ax, position, divipaya, width, num_bottom, 'other long term investment')
    num_bottom = draw_bar(ax, position, intepaya, width, num_bottom, 'long term equity investment')
    num_bottom = draw_bar(ax, position, taxespaya, width, num_bottom, 'long term receivable')
    num_bottom = draw_bar(ax, position, copeworkersal, width, num_bottom, 'yield to maturity')
    num_bottom = draw_bar(ax, position, advapaym, width, num_bottom, 'available for sale finance asset')
    num_bottom = draw_bar(ax, position, accopaya, width, num_bottom, 'accounts payable')
    num_bottom = draw_bar(ax, position, notespaya, width, num_bottom, 'notes payable')
    num_bottom = draw_bar(ax, position, tradfinliab, width, num_bottom, 'trade finance liability')
    num_bottom = draw_bar(ax, position, shorttermborr, width, num_bottom, 'short term borrow')


# 长期借款	应付债券	长期应付款	专项应付款	预计非流动负债	长期递延收益	递延所得税负债	其他非流动负债	特殊处理本身不平长期负债	特殊处理格式不同长期负债	非流动负债合计	特殊处理本身不平负债合计	特殊处理格式不同负债合计	负债合计
# longborr	bdspaya	longpaya	specpaya	expenoncliab	longdefeinco	defeincotaxliab	othernoncliabi	longliabitse	longliabform	totalnoncliab	totliabitse	totliabform	totliab
def draw_detailed_long_term_liability_bars(ax,position,width,
                                           longborr, bdspaya, longpaya, specpaya, expenoncliab, longdefeinco,
                                           defeincotaxliab, othernoncliabi, longliabitse, longliabform,num_bottom):
    num_bottom=num_bottom
    num_bottom = draw_bar(ax, position, longliabform, width, num_bottom, 'non current asset itse')
    num_bottom = draw_bar(ax, position, longliabitse, width, num_bottom, 'other non current asset')
    num_bottom = draw_bar(ax, position, othernoncliabi, width, num_bottom, 'other current liability')
    num_bottom = draw_bar(ax, position, defeincotaxliab, width, num_bottom, 'trad share trad')
    num_bottom = draw_bar(ax, position, longdefeinco, width, num_bottom, 'Long-term prepaid expenses')
    num_bottom = draw_bar(ax, position, expenoncliab, width, num_bottom, 'develop expense')
    num_bottom = draw_bar(ax, position, specpaya, width, num_bottom, 'Intangible assets')
    num_bottom = draw_bar(ax, position, longpaya, width, num_bottom, 'oil and gas asset')
    num_bottom = draw_bar(ax, position, bdspaya, width, num_bottom, 'common bio asset')
    num_bottom = draw_bar(ax, position, longborr, width, num_bottom, 'production bio asset')


# 实收资本(或股本)	资本公积	减：库存股	专项储备	盈余公积	一般风险准备	未确定的投资损失	未分配利润	拟分配现金股利	外币报表折算差额	特殊处理本身不平股东权益	特殊处理格式不同股东权益	归属于母公司股东权益合计	少数股东权益	特殊处理本身不平股东权益	特殊处理格式不平股东权益	所有者权益(或股东权益)合计	特殊处理本身不平负债及权益	特殊处理格式不同负债及权益	负债和所有者权益	结算备付金	拆出资金	衍生金融资产	应收分保账款	应收分保合同准备金	买入返售金融资产	向中央银行借款	吸收存款及同业存放	拆入资金	衍生金融负债	卖出回购金融资产款	应付手续费及佣金	保险合同准备金	代理买卖证券款	代理承销证券款
# paidincapi	capisurp	treastk	specrese	rese	generiskrese	unreinveloss	undiprof	topaycashdivi	curtrandiff	sharrighitse	sharrightform	paresharrigh	minysharrigh	righaggritse	rightaggrform	righaggr	rightotitse	rightotform	totliabsharequi	settresedepo	plac	derifinaasset	reinrece	reincontrese	purcresaasset	cenbankborr	deposit	fdsborr	deriliab	sellrepasse	copepoun	insucontrese	actitradsecu	actiundesecu
def draw_detailed_equity_bars(ax,position,width,
                              paidincapi, capisurp, treastk, specrese, rese, generiskrese, unreinveloss, undiprof,
                              topaycashdivi, curtrandiff, sharrighitse, sharrightform, paresharrigh, minysharrigh,
                              righaggritse, rightaggrform):
    ax.bar(position, rightaggrform, width, label='non current asset form')
    num_bottom=rightaggrform
    num_bottom = draw_bar(ax, position, righaggritse, width, num_bottom, 'non current asset itse')
    num_bottom = draw_bar(ax, position, minysharrigh, width, num_bottom, 'other non current asset')
    num_bottom = draw_bar(ax, position, paresharrigh, width, num_bottom, 'other current liability')
    num_bottom = draw_bar(ax, position, sharrightform, width, num_bottom, 'trad share trad')
    num_bottom = draw_bar(ax, position, sharrighitse, width, num_bottom, 'Long-term prepaid expenses')
    num_bottom = draw_bar(ax, position, curtrandiff, width, num_bottom, 'develop expense')
    num_bottom = draw_bar(ax, position, topaycashdivi, width, num_bottom, 'Intangible assets')
    num_bottom = draw_bar(ax, position, undiprof, width, num_bottom, 'oil and gas asset')
    num_bottom = draw_bar(ax, position, unreinveloss, width, num_bottom, 'common bio asset')
    num_bottom = draw_bar(ax, position, generiskrese, width, num_bottom, 'production bio asset')
    num_bottom = draw_bar(ax, position, rese, width, num_bottom, 'fixed asset clean up')
    num_bottom = draw_bar(ax, position, specrese, width, num_bottom, 'engineer material')
    num_bottom = draw_bar(ax, position, treastk, width, num_bottom, 'Construction in progress')
    num_bottom = draw_bar(ax, position, capisurp, width, num_bottom, 'fixed asset')
    num_bottom = draw_bar(ax, position, paidincapi, width, num_bottom, 'investment property')


def draw_bar(ax,position,series,width,num_bottom,str_label):
    ax.bar(position, series, width, bottom=num_bottom, label=str_label)
    num_bottom += series
    return num_bottom




def draw_bs_subplot(ax,df):
    width = 0.1
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
    longrece = df['longrece']
    equiinve = df['equiinve']
    otherlonginve = df['otherlonginve']
    inveprop = df['inveprop']
    fixedassenet = df['fixedassenet']
    consprog = df['consprog']
    engimate = df['engimate']
    fixedasseclea = df['fixedasseclea']
    prodasse = df['prodasse']
    comasse = df['comasse']
    hydrasset = df['hydrasset']
    intaasset = df['intaasset']
    deveexpe = df['deveexpe']
    goodwill = df['goodwill']
    logprepexpe = df['logprepexpe']
    tradshartrad = df['tradshartrad']
    defetaxasset = df['defetaxasset']
    othernoncasse = df['othernoncasse']
    noncasseitse = df['noncasseitse']
    noncasseform = df['noncasseform']

    ind = np.arange(len(t))  # the x locations for the groups

    b = df['totliabsharequi']
    cl = df['totalcurrliab']
    shorttermborr = df['shorttermborr']
    tradfinliab = df['tradfinliab']
    notespaya = df['notespaya']
    accopaya = df['accopaya']
    advapaym = df['advapaym']
    copeworkersal = df['copeworkersal']
    taxespaya = df['taxespaya']
    intepaya = df['intepaya']
    divipaya = df['divipaya']
    otherfeepaya = df['otherfeepaya']
    margrequ = df['margrequ']
    intelpay = df['intelpay']
    otherpay = df['otherpay']
    accrexpe = df['accrexpe']
    expecurrliab = df['expecurrliab']
    copewithreinrece = df['copewithreinrece']
    inteticksett = df['inteticksett']
    dometicksett = df['dometicksett']
    defereve = df['defereve']
    shorttermbdspaya = df['shorttermbdspaya']
    duenoncliab = df['duenoncliab']
    othercurreliabi = df['othercurreliabi']
    currliabitse = df['currliabitse']
    currliabform = df['currliabform']

    ll = df['totalnoncliab']
    l = df['totliab']
    e = df['righaggr']

    longborr = df['longborr']
    bdspaya = df['bdspaya']
    longpaya = df['longpaya']
    specpaya = df['specpaya']
    expenoncliab = df['expenoncliab']
    longdefeinco = df['longdefeinco']
    defeincotaxliab = df['defeincotaxliab']
    othernoncliabi = df['othernoncliabi']
    longliabitse = df['longliabitse']
    longliabform = df['longliabform']
    totalnoncliab = df['totalnoncliab']
    totliabitse = df['totliabitse']
    totliabform = df['totliabform']
    totliab = df['totliab']
    paidincapi = df['paidincapi']
    capisurp = df['capisurp']
    treastk = df['treastk']
    specrese = df['specrese']
    rese = df['rese']
    generiskrese = df['generiskrese']
    unreinveloss = df['unreinveloss']
    undiprof = df['undiprof']
    topaycashdivi = df['topaycashdivi']
    curtrandiff = df['curtrandiff']
    sharrighitse = df['sharrighitse']
    sharrightform = df['sharrightform']
    paresharrigh = df['paresharrigh']
    minysharrigh = df['minysharrigh']
    righaggritse = df['righaggritse']
    rightaggrform = df['rightaggrform']
    righaggr = df['righaggr']
    rightotitse = df['rightotitse']
    rightotform = df['rightotform']
    totliabsharequi = df['totliabsharequi']
    settresedepo = df['settresedepo']
    plac = df['plac']
    derifinaasset = df['derifinaasset']
    reinrece = df['reinrece']
    reincontrese = df['reincontrese']
    purcresaasset = df['purcresaasset']
    cenbankborr = df['cenbankborr']
    deposit = df['deposit']
    fdsborr = df['fdsborr']
    deriliab = df['deriliab']
    sellrepasse = df['sellrepasse']
    copepoun = df['copepoun']
    insucontrese = df['insucontrese']
    actitradsecu = df['actitradsecu']
    actiundesecu = df['actiundesecu']

    draw_bs_bars(ax,ind,width,ca,la,cl,ll,e)
    draw_detailed_current_asset_bars(ax,ind-2*width,width,curfds, tradfinasset, notesrece, accorece, prep,
    premrece, interece, dividrece, otherrece, expotaxrebarece, subsrece,
    margrece, intelrece, inve, prepexpe, unseg, expinoncurrasset, othercurrasse,
    currassetitse, currasseform, la)

    draw_detailed_long_term_asset_bars(ax, ind-width, width,
                                       lendandloan, avaisellasse, holdinvedue, longrece, equiinve, otherlonginve,
                                       inveprop, fixedassenet, consprog, engimate, fixedasseclea, prodasse, comasse,
                                       hydrasset, intaasset, deveexpe, goodwill, logprepexpe, tradshartrad,
                                       defetaxasset, othernoncasse, noncasseitse, noncasseform)
    draw_detailed_current_liability_bars(ax, ind+2*width, width,
                                         shorttermborr, tradfinliab, notespaya, accopaya, advapaym, copeworkersal,
                                         taxespaya, intepaya, divipaya, otherfeepaya, margrequ, intelpay, otherpay,
                                         accrexpe,
                                         expecurrliab, copewithreinrece, inteticksett, dometicksett, defereve,
                                         shorttermbdspaya,
                                         duenoncliab, othercurreliabi, currliabitse, currliabform, ll+e)
    draw_detailed_long_term_liability_bars(ax, ind+2*width, width,
                                           longborr, bdspaya, longpaya, specpaya, expenoncliab, longdefeinco,
                                           defeincotaxliab, othernoncliabi, longliabitse, longliabform, e)
    draw_detailed_equity_bars(ax, ind+2*width, width,
                              paidincapi, capisurp, treastk, specrese, rese, generiskrese, unreinveloss, undiprof,
                              topaycashdivi, curtrandiff, sharrighitse, sharrightform, paresharrigh, minysharrigh,
                              righaggritse, rightaggrform)
    ax.set_xticks(ind + width / 2)
    ax.set_xticklabels(t)
    for tick in ax.get_xticklabels():
        tick.set_rotation(90)
    ax.legend(loc='upper right')

def draw_industry_bs_subplot(ax,df):
    width=0.1

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

    ax.set_xticks(ind + width / 4)
    font = FontProperties(fname=r"C:\\windows\\fonts\\simsun.ttc")
    ax.set_xticklabels(name,size='small',rotation=90,fontproperties=font)
    ax.legend(loc='upper right')


def draw_is_cfs_chart_for_stock(str_stock_code):
    style.use('ggplot')
    fig, ax = plt.subplots(figsize=(15,8))
    # fig = plt.figure(figsize=(15,8))
    dateparse = lambda dates: pd.datetime.strptime(dates, '%Y%m%d')
    width=0.3
    df2 = pd.read_excel('../data/bs/bs_'+str_stock_code+'.xlsx')# dfo#[dfo['code']=='SZ002287']
    df2.fillna(0, inplace=True)
    draw_bs_subplot(ax, df2)
    plt.savefig('../data/charts/bs_' + str_stock_code+ '.jpg')
    plt.show()

def draw_industry_bs_chart_for_date(str_industry,str_reportdate):
    style.use('ggplot')
    # fig, ax = plt.subplots(figsize=(15,8))
    fig = plt.figure(figsize=(50, 20))
    dateparse = lambda dates: pd.datetime.strptime(dates, '%Y%m%d')
    dfo = pd.read_excel('../data/bs/bs_' + str_industry + '.xlsx', parse_dates=['reportdate'], date_parser=dateparse)
    df = dfo[dfo['reportdate'] == str_reportdate]
    df.fillna(0, inplace=True)
    df = df.sort_values(by=['totasset'], ascending=False)
    ax = fig.add_subplot(111)
    draw_industry_bs_subplot(ax, df)

    # ax2 = fig.add_subplot(212)
    # width=0.3
    # df2 = pd.read_excel('../data/bs_SZ002172.xlsx')# dfo#[dfo['code']=='SZ002287']
    # draw_bs_subplot(ax2, df2)

    plt.savefig('../data/charts/bs_' + str_industry + '_' + str_reportdate + '.jpg')
    plt.show()


if __name__ == '__main__':
    # draw_industry_bs_chart_for_date('电子','20171231')
    draw_is_cfs_chart_for_stock('SZ000002')












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

