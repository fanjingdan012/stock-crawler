#-*-coding:utf-8 -*-


from xueqiu import get_data
from xueqiu import write_f10_xls

if __name__ == "__main__":
    #SH 0-287-1779
    #SZ 0-951
    #fromRow=1
    shOrSz = 'SZ'
    rangeStart = 170
    rangeEnd = 174
    fromRow = 10449
    data = get_data(shOrSz, rangeStart, rangeEnd, '/stock/f10/cfstatement.json?size=10000&page=1', '../data/cfs')
    write_f10_xls(shOrSz, fromRow, data, '../data/cfs')
