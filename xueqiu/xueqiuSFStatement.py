#-*-coding:utf-8 -*-


from xueqiu import get_data
from xueqiu import write_f10_xls

if __name__ == "__main__":
    #SH 0-287-1779
    #SZ 0-951
    #fromRow=1
    shOrSz = 'SZ'
    rangeStart = 120
    rangeEnd = 130
    fromRow = 7450
    data = get_data(shOrSz, rangeStart, rangeEnd, '/stock/f10/cfstatement.json', '../data/cfs')
    write_f10_xls(shOrSz, fromRow, data, '../data/cfs')
