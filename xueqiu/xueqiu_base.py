#  -*- coding: utf-8 -*-

import urllib.request
import json
#import eastmoney.eastmoneyStockList
import stock_reader
#import MySQLdb
import xlrd
import xlwt
# from xlutils.copy import copy
import os
import json
import sys


def get_headers ():
    return {#'X-Requested-With': 'XMLHttpRequest',
           #'Referer': 'http://xueqiu.com/p/ZH010389',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
           #'Host': 'xueqiu.com',
           #'Connection':'keep-alive',
           #'Accept':'*/*',
           'cookie':
           'device_id=2190831616ca50845068b5e57ac16812; s=fh1146h1wd; _ga=GA1.2.1023145669.1516348405; Hm_lvt_1db88642e346389874251b5a1eded6e3=1538983746,1539323491,1539658510,1539684873; __utmc=1; __utmz=1.1539684873.30.8.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); aliyungf_tc=AQAAADLqJCbnVQcAafyfc+whRVV2mMnm; xq_a_token=8bb19a6c97ce8d72f0be4bcd51c906d270351669; xq_a_token.sig=D4IqV9nRrz2tk-MvcHsG0JxH_Jg; xq_r_token=892351a6205473ee21f05d419e3d2833127e1b1f; xq_r_token.sig=_E0ixyb9ctAQc_TN-YXfd28l7HQ; u=301540361430380; _gid=GA1.2.2123854954.1540361430; _gat_gtag_UA_16079156_4=1; __lnkrntdmcvrd=-1; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1540361449; __utma=1.1023145669.1516348405.1539684873.1540361450.31; __utmt=1; __utmb=1.1.10.1540361450'
    }


def get_response(url):
    headers = get_headers()
    req = urllib.request.Request(url, headers=headers)
    content = urllib.request.urlopen(req).read().decode('utf-8')
    return content


def get_data(stock_list, urlPattern, fileName):
    """
    deprecated
    """
    f = open(fileName+".txt", "a",encoding='utf-8')
    XUEQIU_DOMAIN = 'https://xueqiu.com'

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
        content = get_response(url)
        print(content)
        f.write(content)
        f.write('\n')
        result.append(content)
        results.append(result)
    f.close()
    return results




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


