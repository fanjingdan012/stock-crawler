#-*-coding:utf-8 -*-
from xueqiu import get_data
from xueqiu import write_f10_xls
import readStockList
import urllib.request
import json
import readStockList
# import MySQLdb
import xlrd
import xlwt
# from xlutils.copy import copy
import os
import xueqiu
# from xueqiu import get_data
# from xueqiu import get_response
# from xueqiu import getFieldColDict
# from xueqiu import write_f10_xls
import pandas as pd
import datetime


def get_cfs_for_1_stock(str_stock_code):
    # stock_list=readStockList.read_industry_stock_list_by_code(stock_code)
    # data = get_data(stock_list, '/stock/f10/balsheet.json?size=10000&page=1', '../data/bs_'+stock_id)
    str_response=xueqiu.get_response('https://xueqiu.com/stock/f10/cfstatement.json?size=10000&page=1&symbol='+str_stock_code)
    # write_f10_xls(1, data, '../data/bs_'+stock_id)
    json_data = json.loads(str_response)

    if (('list' in json_data) & (json_data['list'] is not None)):
        json_list = json_data['list']
        str_list=json.dumps(json_list)
        df = pd.read_json(str_list, orient='records')
        df.to_excel(get_file_name(str_stock_code))


def get_file_name(name):
    return '../data/cfs_'+name+'.xlsx'

def get_cfs_for_range_stocks():
    #SH 0-287-1779
    #SZ 0-951
    range_start=2871
    range_end=2908
    fromRow=1
    stock_list = readStockList.read_industry_stock_list2('家电行业')
    data = get_data( stock_list, '/stock/f10/cfstatement.json?size=10000&page=1', '../data/cfs_家电')
    write_f10_xls(fromRow, data, '../data/cfs_家电')


if __name__ == "__main__":
    get_cfs_for_1_stock('SZ000333')


