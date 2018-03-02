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
    dfo = pd.read_excel('../data/zjh_industry.xlsx',skiprows=1)
    df = dfo[dfo['level'] == 2]
    return df

def get_xueqiu_industry_quote(industry_df,  file_name):
    f = open(file_name + ".txt", "a", encoding='utf-8')
    headers = getHeaders()
    # stock_list = readStockList.read_stock_list(sh_sz, range_start, range_end)
    print(industry_df)
    results = []
    for index, row in industry_df.iterrows():
        industry_code = row['code']
        result = [industry_code]
        url = 'https://xueqiu.com/industry/quote_order.json?page=1&size=10000&order=desc&exchange=CN&orderBy=percent&level2code='+industry_code
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

def write_f10_xls(fromRow, results,fileName):
    fileName1 = fileName+".xls"
    oldwb = xlrd.open_workbook(fileName1, 'r')
    fieldColDict = getFieldColDict(oldwb)
    newwb = copy(oldwb)
    sheet = newwb.get_sheet(0)
    sheet.write(0, 0, 'industry2_code')
    sheet.write(0, 1, 'industry2_name')
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
def get_merged_zjh_industry():
    dfo1 = pd.read_excel('../data/zjh_industry.xlsx', skiprows=1,usecols='B,C,D,E')
    df_industry2 = dfo1[dfo1['level'] == 2]
    df_industry2.rename(columns={'code': 'industry2_code'}, inplace=True)
    df_industry2.rename(columns={'name': 'industry2_name'}, inplace=True)
    del df_industry2['level']
    df_industry1 = dfo1[dfo1['level'] == 1]
    df_industry1.rename(columns={'code': 'industry1_code'}, inplace=True)
    df_industry1.rename(columns={'name': 'industry1_name'}, inplace=True)
    del df_industry1['level']
    del df_industry1['parent_code']
    df_industry = pd.merge(df_industry1, df_industry2, left_on='industry1_code',right_on='parent_code',how='outer')
    del df_industry['parent_code']
    return df_industry

def write_csv(date):
    df_industry = get_merged_zjh_industry()
    dfo = pd.read_excel('../data/industry_quote/'+date+".xls")
    df_merge = pd.merge(df_industry, dfo, how='right')
    df_merge.to_csv('../data/industry_quote/'+date+".csv" , index=False,encoding = "utf-8")




if __name__ == "__main__":
    write_csv('2018-03-02')
    # industry_df = read_industry_df()
    # data = get_xueqiu_industry_quote(industry_df, '../data/industry_quote/2018-03-02')
    # write_f10_xls(1, data, '../data/industry_quote/2018-03-02')





