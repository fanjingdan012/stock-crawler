# -*-coding:utf-8 -*-
import urllib.request
import json
import stock_reader
import MySQLdb
import xlrd
import xlwt
from xlutils.copy import copy
import os
from xueqiu import getData


def writeXls(shOrSz, fromRow, results):
    FILE_NAME = 'bonus.xls'
    oldwb = xlrd.open_workbook(FILE_NAME, 'rw')
    newwb = copy(oldwb)
    sheet = newwb.get_sheet(0)
    if (shOrSz == 'SZ'):
        sheet = newwb.get_sheet(1)
    row = fromRow
    for i in range(0, len(results)):
        result = results[i]
        href = result[0]
        jsonStr = result[1]
        data = json.loads(jsonStr)
        if (('list' in data) & (data['list'] is not None)):
            listJson = data['list']
            for item in listJson:
                sheet.write(row, 1, href)
                if ('bonusimpdate' in item):
                    sheet.write(row, 2, item['bonusimpdate'])
                if ('bonusyear' in item):
                    sheet.write(row, 3, item['bonusyear'])
                if ('cur' in item):
                    sheet.write(row, 4, item['cur'])
                if ('bonusskratio' in item):
                    sheet.write(row, 5, item['bonusskratio'])
                if ('tranaddskraio' in item):
                    sheet.write(row, 6, item['tranaddskraio'])
                if ('recorddate' in item):
                    sheet.write(row, 7, item['recorddate'])
                if ('exrightdate' in item):
                    sheet.write(row, 8, item['exrightdate'])
                if ('cdividend' in item):
                    sheet.write(row, 9, item['cdividend'])
                if ('fdividendbh' in item):
                    sheet.write(row, 10, item['fdividendbh'])
                if ('tranaddsklistdate' in item):
                    sheet.write(row, 11, item['tranaddsklistdate'])
                if ('bonussklistdate' in item):
                    sheet.write(row, 12, item['bonussklistdate'])
                if ('tranaddskaccday' in item):
                    sheet.write(row, 13, item['tranaddskaccday'])
                if ('bonusskaccday' in item):
                    sheet.write(row, 14, item['bonusskaccday'])
                if ('symbol' in item):
                    sheet.write(row, 15, item['symbol'])
                if ('secode' in item):
                    sheet.write(row, 16, item['secode'])
                if ('divitype' in item):
                    sheet.write(row, 17, item['divitype'])
                if ('taxfdividendbh' in item):
                    sheet.write(row, 18, item['taxfdividendbh'])
                if ('taxcdividend' in item):
                    sheet.write(row, 19, item['taxcdividend'])
                if ('divibegdate' in item):
                    sheet.write(row, 20, item['divibegdate'])
                if ('summarize' in item):
                    sheet.write(row, 21, item['summarize'])
                row = row + 1
    os.remove(FILE_NAME)
    newwb.save(FILE_NAME)
    print(row)
    return row


if __name__ == "__main__":
    # SH 0-287-1779
    # SZ 0-951
    # fromRow=1
    shOrSz = 'SZ'
    rangeStart = 800
    rangeEnd = 951
    fromRow = 7737
    writeXls(shOrSz, fromRow, getData(shOrSz, rangeStart, rangeEnd, '/stock/f10/bonus.json'))
