#  -*- coding: utf-8 -*-

import urllib.request
import json
#import eastmoney.eastmoneyStockList
import readStockList
#import MySQLdb
import xlrd
import xlwt
from xlutils.copy import copy
import os
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


def get_data(sh_sz, range_start, range_end, urlPattern, fileName):
    f = open(fileName+".txt", "a",encoding='utf-8')
    XUEQIU_DOMAIN = 'https://xueqiu.com'
    headers = getHeaders()
    stock_list = readStockList.read_stock_list(sh_sz, range_start, range_end)
    print(stock_list)
    results = []
    for stock in stock_list:
        result = [stock]
        url = XUEQIU_DOMAIN+urlPattern+'&symbol=' + stock
        print(url)
        f.write(url)
        f.write('\n')
        result.append(url)
        req = urllib.request.Request(url, headers=headers)
        content = urllib.request.urlopen(req).read().decode('utf-8')
        print(content)
        f.write(content)
        f.write('\n')
        result.append(content)
        results.append(result)
    f.close()
    return results


def getFieldColDict(sh_sz, workbook):
    field_col_dict = dict()
    old_sheet = workbook.sheet_by_index(0)
    if sh_sz == 'SZ':
        old_sheet = workbook.sheet_by_index(1)
    for col in range(old_sheet.ncols):
        field_col_dict[old_sheet.cell_value(0, col)] = col
    return field_col_dict


def write_f10_xls(shOrSz, fromRow, results,fileName):
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
        stock=result[0]
        href = result[1]
        jsonStr=result[2]
        data=json.loads(jsonStr)
        if (('list' in data)& (data['list'] is not None)):
            listJson = data['list']
            for item in listJson:
                sheet.write(row, 0, stock)
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

def write_price_xls(  results,file_dir):

    for i in range(0, len(results)):
        result = results[i]
        stock = result[0]
        href = result[1]
        jsonStr = result[2]
        data = json.loads(jsonStr)
        if (('chartlist' in data) and (data['chartlist'] is not None)):
            field_col_dict = dict()
            newwb = xlwt.Workbook(encoding='utf-8')
            sheet = newwb.add_sheet('Day')
            row = 1
            sheet.write(0, 0, 'stock')
            sheet.write(0, 1, 'href')
            listJson = data['chartlist']
            for item in listJson:
                sheet.write(row, 0, stock)
                sheet.write(row, 1, href)
                for key, value in item.items():
                    col = field_col_dict.get(key,-1)
                    if col == -1:
                        if field_col_dict:
                            col = max(field_col_dict.values())+1
                        else:
                            col = 2
                        sheet.write(0, col, key)
                        field_col_dict[key]=col
                        print('newly added col:'+key)
                    sheet.write(row, col, value)
                row = row+1
        file_name1 = file_dir +stock+ ".xls"
        newwb.save(file_name1)

