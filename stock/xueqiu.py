import urllib.request
import json
import eastmoneyStockList
import readStockList
import MySQLdb
import xlrd
import xlwt
from xlutils.copy import copy
import os
import urllib.request
import json
import sys

def getHeaders ():
    return {#'X-Requested-With': 'XMLHttpRequest',
           #'Referer': 'http://xueqiu.com/p/ZH010389',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
           #'Host': 'xueqiu.com',
           #'Connection':'keep-alive',
           #'Accept':'*/*',
           'cookie':'xq_a_token=a8d434ddd975f5752965fa782596bd0b5b008376; xq_a_token.sig=ke78qTMMk1J4blZPe-jY53Uy9Ec; xq_r_token=437547d929e3cc54630bfd58136879694e1ae4a9; xq_r_token.sig=iYuNwCitZuVpyfkOu6_LLtaQn6E; s=et11okl5s2; u=811511157993130; device_id=da9025ffdb657b9460445f57e7be5368; aliyungf_tc=AQAAADToGVkdRgIACbB+3oLvs1StU/PX; __utma=1.800988467.1511158014.1511339632.1511406223.5; __utmc=1; __utmz=1.1511158014.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); Hm_lvt_1db88642e346389874251b5a1eded6e3=1511157995,1511226946,1511233574,1511329392; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1511406315'
    }
def getData(shOrSz,rangeStart,rangeEnd,urlPattern,fileName):
    f = open(fileName+".txt", "wb+")
    XUEQIU_DOMAIN='https://xueqiu.com'
    headers = getHeaders()
    stockList = readStockList.readStockList(shOrSz,rangeStart,rangeEnd)
    print(stockList)
    results = []
    for stock in stockList:
        result=[]
        url = XUEQIU_DOMAIN+urlPattern+'?symbol=' + stock+'&size=10000&page=1'
        print(url)
        f.write(url.encode('utf-8'))
        result.append(url)
        req = urllib.request.Request(url, headers=headers)
        content = urllib.request.urlopen(req).read().decode('utf-8')
        print(content)
        f.write(content.encode('utf-8'))
        result.append(content)
        results.append(result)
    f.close()
    return results

def getFieldColDict(shOrSz,workbook):
    fieldColDict = dict()
    oldSheet = workbook.sheet_by_index(0)
    if (shOrSz == 'SZ'):
        oldSheet = workbook.sheet_by_index(1)
    for col in range(oldSheet.ncols):
        fieldColDict[oldSheet.cell_value(0, col)] = col
    return fieldColDict

def writeF10Xls(shOrSz, fromRow, results,fileName):
    fileName1 = fileName+".xls"
    oldwb = xlrd.open_workbook(fileName1, 'r')
    fieldColDict = getFieldColDict(shOrSz,oldwb)
    newwb = copy(oldwb)
    sheet = newwb.get_sheet(0)
    if(shOrSz=='SZ'):
        sheet = newwb.get_sheet(1)
    row = fromRow
    for i in range(0, len(results)):
        result = results[i]
        href = result[0]
        jsonStr=result[1]
        data=json.loads(jsonStr)
        if (('list' in data)& (data['list'] is not None)):
            listJson = data['list']
            for item in listJson:
                sheet.write(row, 1, href)
                for key, value in item.items():
                    col=fieldColDict.get(key,-1)
                    if(col==-1):
                        if(fieldColDict):
                            col=max(fieldColDict.values())+1
                        else:
                            col=2
                        sheet.write(0,col,key)
                        fieldColDict[key]=col
                        print('newly added col:'+key)
                    sheet.write(row, col, value)
                row=row+1
    os.remove(fileName1)
    newwb.save(fileName1)
    print(row)
    return row