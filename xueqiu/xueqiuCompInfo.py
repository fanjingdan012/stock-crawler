#-*-coding:utf-8 -*-
import urllib.request
import json
import stock_reader
import MySQLdb
import xlrd
import xlwt
from xlutils.copy import copy
import os
from xueqiu import getHeaders
def getCompInfo(shOrSz,rangeStart,rangeEnd):
    headers = getHeaders()
    stockList = stock_reader.readStockList(shOrSz, rangeStart, rangeEnd)
    print(stockList)


    # db = MySQLdb.connect(host="localhost", user="root", passwd="Initial0", db="stock", use_unicode=True, charset="utf8")
    # c = db.cursor()

    compInfos = []
    for stock in stockList:
        compInfo=[]
        url = 'https://xueqiu.com/stock/f10/compinfo.json?symbol=' + stock
        print(url)
        compInfo.append(url)
        req = urllib.request.Request(url, headers=headers)
        content = urllib.request.urlopen(req).read().decode('utf-8')
        print(content)
        data = json.loads(content)
        compInfo.append(json.dumps(data))
        compInfos.append(compInfo)
    return compInfos


def writeXlsCompInfos(shOrSz,rangeStart,rangeEnd,compInfos):
    oldwb = xlrd.open_workbook('stocks.xls', 'rw')
    newwb = copy(oldwb)
    sheet = newwb.get_sheet(0)
    if(shOrSz=='SZ'):
        sheet = newwb.get_sheet(1)
   # s1 = unicode('哈', 'utf - 8')


    for i in range(0,len(compInfos)):
        compInfo = compInfos[i]
        sheet.write(i + rangeStart, 1, compInfo[0])
        jsonStr=compInfo[1]
        # json.encode('utf-8')
        # jsonStr.encode('utf-8').decode("unicode-escape")
        data=json.loads(jsonStr)
        if (('tqCompInfo' in data)& (data['tqCompInfo'] is not None)):
            compname = data['tqCompInfo']['compname']
            engname = data['tqCompInfo']['engname']
            comptype1 = data['tqCompInfo']['comptype1']
            comptype2 = data['tqCompInfo']['comptype2']
            founddate = data['tqCompInfo']['founddate']
            orgtype = data['tqCompInfo']['orgtype']
            regcapital = data['tqCompInfo']['regcapital']
            authcapsk = data['tqCompInfo']['authcapsk']
            chairman = data['tqCompInfo']['chairman']
            manager = data['tqCompInfo']['manager']
            legrep = data['tqCompInfo']['legrep']
            bsecretary = data['tqCompInfo']['bsecretary']
            bsecretarytel = data['tqCompInfo']['bsecretarytel']
            bsecretaryfax = data['tqCompInfo']['bsecretaryfax']
            seaffrepr = data['tqCompInfo']['seaffrepr']
            seagttel = data['tqCompInfo']['seagttel']
            seagtfax = data['tqCompInfo']['seagtfax']
            seagtemail = data['tqCompInfo']['seagtemail']
            authreprsbd = data['tqCompInfo']['authreprsbd']
            leconstant = data['tqCompInfo']['leconstant']
            accfirm = data['tqCompInfo']['accfirm']
            regaddr = data['tqCompInfo']['regaddr']
            officeaddr = data['tqCompInfo']['officeaddr']
            officezipcode = data['tqCompInfo']['officezipcode']
            comptel = data['tqCompInfo']['comptel']
            compfax = data['tqCompInfo']['compfax']
            compemail = data['tqCompInfo']['compemail']
            compurl = data['tqCompInfo']['compurl']
            servicetel = data['tqCompInfo']['servicetel']
            servicefax = data['tqCompInfo']['servicefax']
            compintro = data['tqCompInfo']['compintro']
            bizscope = data['tqCompInfo']['bizscope']
            majorbiz = data['tqCompInfo']['majorbiz']
            bizscale = data['tqCompInfo']['bizscale']
            compcode = data['tqCompInfo']['compcode']
            compsname = data['tqCompInfo']['compsname']
            region = data['tqCompInfo']['region']
            regptcode = data['tqCompInfo']['regptcode']
            listdate = data['tqCompInfo']['listdate']
            issprice = data['tqCompInfo']['issprice']
            onlactissqty = data['tqCompInfo']['onlactissqty']
            actissqty = data['tqCompInfo']['actissqty']
            sheet.write(i + rangeStart, 2, compname)
            sheet.write(i + rangeStart, 3, engname)
            sheet.write(i + rangeStart, 4, comptype1)
            sheet.write(i + rangeStart, 5, comptype2)
            sheet.write(i + rangeStart, 6, founddate)
            sheet.write(i + rangeStart, 7, orgtype)
            sheet.write(i + rangeStart, 8, regcapital)
            sheet.write(i + rangeStart, 9, authcapsk)
            sheet.write(i + rangeStart, 10, chairman)
            sheet.write(i + rangeStart, 11, manager)
            sheet.write(i + rangeStart, 12, legrep)
            sheet.write(i + rangeStart, 13, bsecretary)
            sheet.write(i + rangeStart, 14, bsecretarytel)
            sheet.write(i + rangeStart, 15, bsecretaryfax)
            sheet.write(i + rangeStart, 16, seaffrepr)
            sheet.write(i + rangeStart, 17, seagttel)
            sheet.write(i + rangeStart, 18, seagtfax)
            sheet.write(i + rangeStart, 19, seagtemail)
            sheet.write(i + rangeStart, 20, authreprsbd)
            sheet.write(i + rangeStart, 21, leconstant)
            sheet.write(i + rangeStart, 22, accfirm)
            sheet.write(i + rangeStart, 23, regaddr)
            sheet.write(i + rangeStart, 24, officeaddr)
            sheet.write(i + rangeStart, 25, officezipcode)
            sheet.write(i + rangeStart, 26, comptel)
            sheet.write(i + rangeStart, 27, compfax)
            sheet.write(i + rangeStart, 28, compemail)
            sheet.write(i + rangeStart, 29, compurl)
            sheet.write(i + rangeStart, 30, servicetel)
            sheet.write(i + rangeStart, 31, servicefax)
            sheet.write(i + rangeStart, 32, compintro)
            sheet.write(i + rangeStart, 33, bizscope)
            sheet.write(i + rangeStart, 34, majorbiz)
            sheet.write(i + rangeStart, 35, bizscale)
            sheet.write(i + rangeStart, 36, compcode)
            sheet.write(i + rangeStart, 37, compsname)
            sheet.write(i + rangeStart, 38, region)
            sheet.write(i + rangeStart, 39, regptcode)
            sheet.write(i + rangeStart, 40, listdate)
            sheet.write(i + rangeStart, 41, issprice)
            sheet.write(i + rangeStart, 42, onlactissqty)
            sheet.write(i + rangeStart, 43, actissqty)
            sheet.write(i + rangeStart, 44, json.dumps(data['tqCompInfo']['tqCompBoardmapList']))
            sheet.write(i + rangeStart, 45, json.dumps(data['tqCompInfo']['tqCompIndustryList']))

        else:
            sheet.write(i+rangeStart,2,'null')
    os.remove('stocks.xls')
    newwb.save('stocks.xls')
def readJson(content,compInfo):
    # db = MySQLdb.connect(host="localhost", user="root", passwd="Initial0", db="stock", use_unicode=True, charset="utf8")
    # c = db.cursor()
    # content='{"tqCompInfo":{"compname":"江苏怡达化学股份有限公司","engname":"Jiangsu Yida Chemical Co.,ltd.","comptype1":"Z","comptype2":"Z09","founddate":"19960620","orgtype":"民营企业","regcapital":8015.0,"authcapsk":0,"chairman":"刘准","manager":"刘准","legrep":"刘准","bsecretary":"蔡国庆","bsecretarytel":"0510-86600202","bsecretaryfax":"0510-86609388","seaffrepr":null,"seagttel":null,"seagtfax":null,"seagtemail":null,"authreprsbd":null,"leconstant":"北京国枫律师事务所","accfirm":"天衡会计师事务所(特殊普通合伙)","regaddr":"江苏省江阴市西石桥球庄村","officeaddr":"江苏省江阴市西石桥球庄村","officezipcode":"214441","comptel":"0510-86600202","compfax":"0510-86609388","compemail":"ydhx8101@yidamail.com","compurl":"www.yidachem.com","servicetel":null,"servicefax":null,"compintro":"    公司前身江阴市怡达化工有限公司,成立于1996年6月20日;2012年8月14日整体变更为股份有限公司,更名为江苏怡达化学股份有限公司。","bizscope":"醇醚、醇醚醋酸酯系列产品的生产(按安全生产许可证所列范围经营);危险化学品经营(按许可证所列范围和方式经营);醇醚、醇醚酯系列产品(不含危险化学品)的生产;机动车制动液、汽车发动机冷却液产品的生产、销售;化工产品及原料(不含危险化学品)的销售;化工产品及其生产技术的研究、开发;自营和代理各类商品及技术的进出口业务(但国家限定企业经营或禁止进出口的商品和技术除外)。(依法须经批准的项目,经相关部门批准后方可开展经营活动)","majorbiz":"醇醚及醇醚酯类有机化工产品的技术研发、生产及销售。","bizscale":"9","compcode":"80304567","compsname":"怡达股份","region":"CN320000","regptcode":"214441","listdate":1510675200000,"issprice":16.71,"onlactissqty":1804.5,"actissqty":2005.0,"tqCompBoardmapList":[{"keyname":"江苏省","keycode":"CN320000","keynameacronym":null,"boardcode":"1102","boardname":"地区代码(省级)"},{"keyname":"无锡市","keycode":"CN320200","keynameacronym":null,"boardcode":"1103","boardname":"地区代码(市级)"}],"tqCompIndustryList":[{"level2name":"化学制品","level2nameacronym":null,"level2code":"220300","compcode":null}]}}'

    data = json.loads(content)
    if('tqCompInfo' in data):
        if('compname' in data['tqCompInfo']):
            compname = data['tqCompInfo']['compname']
            engname = data['tqCompInfo']['engname']
            comptype1 = data['tqCompInfo']['comptype1']
            comptype2 = data['tqCompInfo']['comptype2']
            founddate = data['tqCompInfo']['founddate']
            orgtype = data['tqCompInfo']['orgtype']
            regcapital = data['tqCompInfo']['regcapital']
            authcapsk = data['tqCompInfo']['authcapsk']
            chairman = data['tqCompInfo']['chairman']
            manager = data['tqCompInfo']['manager']
            legrep = data['tqCompInfo']['legrep']
            bsecretary = data['tqCompInfo']['bsecretary']
            bsecretarytel = data['tqCompInfo']['bsecretarytel']
            bsecretaryfax = data['tqCompInfo']['bsecretaryfax']
            seaffrepr = data['tqCompInfo']['seaffrepr']
            seagttel = data['tqCompInfo']['seagttel']
            seagtfax = data['tqCompInfo']['seagtfax']
            seagtemail = data['tqCompInfo']['seagtemail']
            authreprsbd = data['tqCompInfo']['authreprsbd']
            leconstant = data['tqCompInfo']['leconstant']
            accfirm = data['tqCompInfo']['accfirm']
            regaddr = data['tqCompInfo']['regaddr']
            officeaddr = data['tqCompInfo']['officeaddr']
            officezipcode = data['tqCompInfo']['officezipcode']
            comptel = data['tqCompInfo']['comptel']
            compfax = data['tqCompInfo']['compfax']
            compemail = data['tqCompInfo']['compemail']
            compurl = data['tqCompInfo']['compurl']
            servicetel = data['tqCompInfo']['servicetel']
            servicefax = data['tqCompInfo']['servicefax']
            compintro = data['tqCompInfo']['compintro']
            bizscope = data['tqCompInfo']['bizscope']
            majorbiz = data['tqCompInfo']['majorbiz']
            bizscale = data['tqCompInfo']['bizscale']
            compcode = data['tqCompInfo']['compcode']
            compsname = data['tqCompInfo']['compsname']
            region = data['tqCompInfo']['region']
            regptcode = data['tqCompInfo']['regptcode']
            listdate = data['tqCompInfo']['listdate']
            issprice = data['tqCompInfo']['issprice']
            onlactissqty = data['tqCompInfo']['onlactissqty']
            actissqty = data['tqCompInfo']['actissqty']
    # industrycode = data['tqCompInfo']['tqCompIndustryList'][0]['level2code']
    #c.execute('INSERT INTO STOCK (compname,engname,comptype1,comptype2,founddate,orgtype,regcapital,authcapsk,chairman,manager,legrep,bsecretary,bsecretarytel,bsecretaryfax,seaffrepr,seagttel,seagtfax,seagtemail,authreprsbd,leconstant,accfirm,regaddr,officeaddr,officezipcode,comptel,compfax,compemail,compurl,servicetel,servicefax,compintro,bizscope,majorbiz,bizscale,compcode,compsname,region,regptcode,listdate,issprice,onlactissqty,actissqty,industrycode) VALUES ( %s, %s, %s, %s, %s, %f, %f, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s, %s, %s, %s, %s, %s, %s,%s, %f, %d, %d, %s)', [compname,engname,comptype1,comptype2,founddate,orgtype,regcapital,authcapsk,chairman,manager,legrep,bsecretary,bsecretarytel,bsecretaryfax,seaffrepr,seagttel,seagtfax,seagtemail,authreprsbd,leconstant,accfirm,regaddr,officeaddr,officezipcode,comptel,compfax,compemail,compurl,servicetel,servicefax,compintro,bizscope,majorbiz,bizscale,compcode,compsname,region,regptcode,listdate,issprice,onlactissqty,actissqty,industrycode])
    # c.execute('INSERT INTO STOCK ('
    #           'compname,engname,comptype1,comptype2,founddate,orgtype,regcapital,authcapsk,chairman,manager,legrep,bsecretary,bsecretarytel,bsecretaryfax,seaffrepr,seagttel,seagtfax,seagtemail,authreprsbd,leconstant,accfirm,regaddr,officeaddr,officezipcode,comptel,compfax,compemail,compurl,servicetel,servicefax,compintro,bizscope,majorbiz,bizscale,compcode,compsname,region,regptcode,listdate,issprice,onlactissqty,actissqty,industrycode) VALUES ( '
    #           '%s,       %s,      %s,       %s,         %s,     %s,     %s,        %s,        %s,     %s,     %s,     %s,        %s,           %s,           %s,       %s,      %s,      %s,           %s,       %s,       %s,      %s,     %s,        %s,         %s,      %s,       %s,      %s,    %s,        %s,        %s,        %s,     %s,      %s,     %s,       %s,     %s,      %s,       %s,     %s,      %s,            %s,      %s )', [
    #            compname,engname,comptype1,comptype2,founddate,orgtype,regcapital,authcapsk,chairman,manager,legrep,bsecretary,bsecretarytel,bsecretaryfax,seaffrepr,seagttel,seagtfax,seagtemail,authreprsbd,leconstant,accfirm,regaddr,officeaddr,officezipcode,comptel,compfax,compemail,compurl,servicetel,servicefax,compintro,bizscope,majorbiz,bizscale,compcode,compsname,region,regptcode,listdate,issprice,onlactissqty,actissqty,industrycode])
    #
    #
    #
    # db.commit()
    # c.close()
    # db.close()
if __name__=="__main__":
    shOrSz='SZ'
    rangeStart=500
    rangeEnd=951
    writeXlsCompInfos(shOrSz,rangeStart,rangeEnd,getCompInfo(shOrSz,rangeStart,rangeEnd))