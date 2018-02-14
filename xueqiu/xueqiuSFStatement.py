#-*-coding:utf-8 -*-
from xueqiu import get_data
from xueqiu import write_f10_xls
import readStockList

if __name__ == "__main__":
    #SH 0-287-1779
    #SZ 0-951
    range_start=2871
    range_end=2908
    fromRow=1
    stock_list = readStockList.read_industry_stock_list2('家电行业')
    data = get_data( stock_list, '/stock/f10/cfstatement.json?size=10000&page=1', '../data/cfs_家电')
    write_f10_xls(fromRow, data, '../data/cfs_家电')


