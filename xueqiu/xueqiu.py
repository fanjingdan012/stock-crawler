#  -*- coding: utf-8 -*-

import urllib.request
import json
#import eastmoney.eastmoneyStockList
import readStockList
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
        'device_id=2190831616ca50845068b5e57ac16812; s=fh1146h1wd; _ga=GA1.2.1023145669.1516348405; __utmz=1.1533125297.21.7.utmcsr=fanjingdan012.github.io|utmccn=(referral)|utmcmd=referral|utmcct=/stock-overview/; xq_a_token=584d0cf8d5a5a9809761f2244d8d272bac729ed4; xq_a_token.sig=x0gT9jm6qnwd-ddLu66T3A8KiVA; xq_r_token=98f278457fc4e1e5eb0846e36a7296e642b8138a; xq_r_token.sig=2Uxv_DgYTcCjz7qx4j570JpNHIs; _gid=GA1.2.215616112.1534734083; u=961534734084008; Hm_lvt_1db88642e346389874251b5a1eded6e3=1532916905,1533125297,1533354344,1534734084; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1534734101; __utma=1.1023145669.1516348405.1533125297.1534734104.22; __utmc=1; __utmt=1; __utmb=1.1.10.1534734104'
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


