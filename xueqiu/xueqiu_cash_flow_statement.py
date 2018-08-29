#-*-coding:utf-8 -*-
# from xueqiu import get_data
# from xueqiu import write_f10_xls
import stock_reader
import urllib.request
import json
import stock_reader


import os
import xueqiu

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
    return '../data/cfs/cfs_'+name+'.xlsx'







