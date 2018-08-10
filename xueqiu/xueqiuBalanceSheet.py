#-*-coding:utf-8 -*-
import urllib.request
import json
import readStockList
# import MySQLdb
import xlrd
import xlwt
# from xlutils.copy import copy
import os
from xueqiu import get_data
from xueqiu import get_response
from xueqiu import getFieldColDict
from xueqiu import write_f10_xls
import pandas as pd
import datetime


def writeXls(shOrSz, fromRow, results):
    FILE_NAME='bs.xls'
    oldwb = xlrd.open_workbook(FILE_NAME, 'r')
    fieldColDict = getFieldColDict(oldwb)
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
                        col=max(fieldColDict.values())+1
                        sheet.write(0,col,key)
                        fieldColDict[key]=col
                        print('newly added col:'+key)
                    sheet.write(row, col, value)
                row=row+1
    os.remove(FILE_NAME)
    newwb.save(FILE_NAME)
    print(row)
    return row


def get_bs_for_1_stock(str_stock_code):
    # stock_list=readStockList.read_industry_stock_list_by_code(stock_code)
    # data = get_data(stock_list, '/stock/f10/balsheet.json?size=10000&page=1', '../data/bs_'+stock_id)
    str_response=get_response('https://xueqiu.com/stock/f10/balsheet.json?size=10000&page=1&symbol='+str_stock_code)
    # write_f10_xls(1, data, '../data/bs_'+stock_id)
    json_data = json.loads(str_response)

    if (('list' in json_data) & (json_data['list'] is not None)):
        json_list = json_data['list']
        str_list=json.dumps(json_list)
        df = pd.read_json(str_list, orient='records')
        df.to_excel(get_file_name(str_stock_code))


def get_file_name(name):
    return '../data/bs_'+name+'.xlsx'


def get_bs_for_range_stocks():
    # SH 0-287-1779
    # SZ 0-951
    # fromRow=1
    sh_sz = 'SZ'
    range_start = 2871
    range_end = 2908
    fromRow = 1
    stock_list = readStockList.read_industry_stock_list2('化工行业')
    data = get_data(stock_list, '/stock/f10/balsheet.json?size=10000&page=1', '../data/bs_化工行业')
    write_f10_xls(fromRow, data, '../data/bs_化工行业')

if __name__=="__main__":
    get_bs_for_1_stock('SH600926')
