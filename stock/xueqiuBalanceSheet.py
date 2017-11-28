#-*-coding:utf-8 -*-
import urllib.request
import json
import readStockList
import MySQLdb
import xlrd
import xlwt
from xlutils.copy import copy
import os
from xueqiu import getData
from xueqiu import getFieldColDict



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

if __name__=="__main__":
    #SH 0-287-1779
    #SZ 0-951
    #fromRow=1
    shOrSz='SZ'
    rangeStart=100
    rangeEnd=300
    fromRow=1861
    writeXls(shOrSz,fromRow,getData(shOrSz,rangeStart,rangeEnd,'/stock/f10/balsheet.json'))