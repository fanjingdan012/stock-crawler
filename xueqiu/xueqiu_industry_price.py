#-*-coding:utf-8 -*-
from xueqiu import get_data
from xueqiu import write_f10_xls
from xueqiu import getHeaders
from xueqiu import getFieldColDict
import urllib.request
import xueqiu
import readStockList
import pandas as pd
import numpy as np
import xlrd
import xlwt
from xlutils.copy import copy
import os
import json

def read_industry_df():
    dfo = pd.read_excel('../data/zjh_industry.xlsx')
    df = dfo[dfo['级别'] == 2]
    return df

def get_xueqiu_industry_quote(industry_df,  file_name):
    f = open(file_name + ".txt", "a", encoding='utf-8')
    headers = getHeaders()
    # stock_list = readStockList.read_stock_list(sh_sz, range_start, range_end)
    print(industry_df)
    results = []
    for index, row in industry_df.iterrows():
        industry_code = row['行业代码']
        result = [industry_code]
        url = 'https://xueqiu.com/industry/quote_order.json?page=1&size=10000&order=desc&exchange=CN&orderBy=percent&level2code='+industry_code
        print(url)
        f.write(url)
        f.write('\n')
        result.append(row['行业名称'])
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

def write_f10_xls(fromRow, results,fileName):
    fileName1 = fileName+".xls"
    oldwb = xlrd.open_workbook(fileName1, 'r')
    fieldColDict = getFieldColDict(oldwb)
    newwb = copy(oldwb)
    sheet = newwb.get_sheet(0)
    sheet.write(0, 0, 'industry_code')
    sheet.write(0, 1, 'industry_name')
    sheet.write(0, 2, 'url')
    row = fromRow
    for i in range(0, len(results)):
        result = results[i]
        stock=result[0]
        name = result[1]
        href = result[2]
        jsonStr=result[3]
        data=json.loads(jsonStr)
        if (('data' in data)& (data['data'] is not None)):
            listJson = data['data']
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

if __name__ == "__main__":
    #SH 0-287-1779
    #SZ 0-951
    range_start=2871
    range_end=2908
    fromRow=1
    industry_df = read_industry_df()
    data = get_xueqiu_industry_quote(industry_df, '../data/industry_quote/2018-02-28')
    write_f10_xls(fromRow, data, '../data/industry_quote/2018-02-28')





