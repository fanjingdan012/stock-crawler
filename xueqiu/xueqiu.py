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
           'cookie':'device_id=bfb52968438e18b2ff72f911fc12a605; s=eb17c099s1; aliyungf_tc=AQAAAHb7ilL4EgEACbB+3naX4bau6aED; __utmc=1; __utmz=1.1520233626.11.5.utmcsr=fanjingdan012.github.io|utmccn=(referral)|utmcmd=referral|utmcct=/stock-crawler/index.html; Hm_lvt_1db88642e346389874251b5a1eded6e3=1520233626,1520233656,1520233731,1520233773; xq_a_token=19f5e0044f535b6b1446bb8ae1da980a48bbe850; xq_a_token.sig=aaTVFAX9sVcWtOiu-5L8dL-p40k; xq_r_token=6d30415b5f855c12fd74c6e2fb7662ea40272056; xq_r_token.sig=rEvIjgpbifr6Q_Cxwx7bjvarJG0; u=361520406370054; __utma=1.455231070.1516958117.1520233626.1520406371.12; __utmt=1; __utmb=1.2.10.1520406371; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1520406375'
    }


def get_data(stock_list, urlPattern, fileName):
    f = open(fileName+".txt", "a",encoding='utf-8')
    XUEQIU_DOMAIN = 'https://xueqiu.com'
    headers = getHeaders()
    # stock_list = readStockList.read_stock_list(sh_sz, range_start, range_end)
    print(stock_list)
    results = []
    for index, row in stock_list.iterrows():
        stock=row['code']
        result = [stock]
        url = XUEQIU_DOMAIN+urlPattern+'&symbol=' + stock
        print(url)
        f.write(url)
        f.write('\n')
        result.append(row['name'])
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


def getFieldColDict( workbook):
    field_col_dict = dict()
    old_sheet = workbook.sheet_by_index(0)
    for col in range(old_sheet.ncols):
        field_col_dict[old_sheet.cell_value(0, col)] = col
    return field_col_dict


def write_f10_xls(fromRow, results,fileName):
    fileName1 = fileName+".xls"
    oldwb = xlrd.open_workbook(fileName1, 'r')
    fieldColDict = getFieldColDict(oldwb)
    newwb = copy(oldwb)
    sheet = newwb.get_sheet(0)
    sheet.write(0, 0, 'code')
    sheet.write(0, 1, 'name')
    sheet.write(0, 2, 'url')
    row = fromRow
    for i in range(0, len(results)):
        result = results[i]
        stock=result[0]
        name = result[1]
        href = result[2]
        jsonStr=result[3]
        data=json.loads(jsonStr)
        if (('list' in data)& (data['list'] is not None)):
            listJson = data['list']
            for item in listJson:
                sheet.write(row, 0, stock)
                sheet.write(row, 1, name)
                sheet.write(row, 2, href)
                for key, value in item.items():
                    col=fieldColDict.get(key,-1)
                    if(col==-1):
                        if(fieldColDict):
                            col=max(fieldColDict.values())+1
                        else:
                            col=3
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


