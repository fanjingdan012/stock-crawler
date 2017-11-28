#-*-coding:utf-8 -*-


from xueqiu import get_data
from xueqiu import write_price_xls

if __name__ == "__main__":
    #SH 0-287-1779
    #SZ 0-951
    #fromRow=1
    sh_sz = 'SZ'
    range_start = 3
    range_end = 4
    data = get_data(sh_sz, range_start, range_end, '/stock/forchartk/stocklist.json?period=1d&type=normal', '../data/price/price')
    write_price_xls( data, '../data/price/')
