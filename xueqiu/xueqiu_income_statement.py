#-*-coding:utf-8 -*-
import urllib.request
import json
import readStockList
# import MySQLdb
import xlrd
import xlwt

import os
# from xueqiu import getHeaders
# from xueqiu import get_data
# from xueqiu import write_f10_xls
import xueqiu
import pandas as pd

def getIncomeStatements(shOrSz,rangeStart,rangeEnd):
    headers = xueqiu.get_headers()
    stockList = readStockList.readStockList(shOrSz,rangeStart,rangeEnd)
    print(stockList)
    incomeStatements = []
    for stock in stockList:
        incomeStatement=[]
        url = 'https://xueqiu.com/stock/f10/incstatement.json?symbol=' + stock
        print(url)
        incomeStatement.append(url)
        req = urllib.request.Request(url, headers=headers)
        content = urllib.request.urlopen(req).read().decode('utf-8')
        print(content)
        data = json.loads(content)
        incomeStatement.append(json.dumps(data))
        incomeStatements.append(incomeStatement)
    return incomeStatements


def get_file_name(name):
    return '../data/is_'+name+'.xlsx'

def get_is_for_1_stock(str_stock_code):
    # stock_list=readStockList.read_industry_stock_list_by_code(stock_code)
    # data = get_data(stock_list, '/stock/f10/balsheet.json?size=10000&page=1', '../data/bs_'+stock_id)
    str_response=xueqiu.get_response('https://xueqiu.com/stock/f10/incstatement.json?size=10000&page=1&symbol='+str_stock_code)
    # write_f10_xls(1, data, '../data/bs_'+stock_id)
    json_data = json.loads(str_response)

    if (('list' in json_data) & (json_data['list'] is not None)):
        json_list = json_data['list']
        str_list=json.dumps(json_list)
        df = pd.read_json(str_list, orient='records')
        df.to_excel(get_file_name(str_stock_code))



# if __name__=="__main__":
#     #SH 287-17
#     #SZ 0-951
#     shOrSz='SZ'
#     rangeStart=951
#     rangeEnd=952
#     fromRow=18276
#     writeXlsIncomeStatements(shOrSz,fromRow,getIncomeStatements(shOrSz,rangeStart,rangeEnd))



def get_is_for_range_stocks():
    #SH 0-287-1779
    #SZ 0-951
    #fromRow=1
    sh_sz='SZ'
    range_start=2871
    range_end=2908
    fromRow=1
    stock_list = readStockList.read_industry_stock_list(range_start, range_end)
    data = xueqiu.get_data(stock_list, '/stock/f10/incstatement.json?size=10000&page=1','../data/is_家电')
    xueqiu.write_f10_xls(fromRow,data,'../data/is_家电')

if __name__=="__main__":
    get_is_for_1_stock('SZ000333')