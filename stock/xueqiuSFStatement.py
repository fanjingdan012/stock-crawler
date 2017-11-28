#-*-coding:utf-8 -*-


from xueqiu import getData
from xueqiu import writeF10Xls

if __name__=="__main__":
    #SH 0-287-1779
    #SZ 0-951
    #fromRow=1
    shOrSz='SZ'
    rangeStart=100
    rangeEnd=110
    fromRow=6167
    writeF10Xls(shOrSz,fromRow,getData(shOrSz,rangeStart,rangeEnd,'/stock/f10/cfstatement.json','cfs'),'cfs')