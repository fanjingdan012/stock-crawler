# -*- coding: utf-8 -*-
import requests
import matplotlib.pyplot as plt
import re
plt.style.use('ggplot')
import csv
class Stock(object):
    def __init__(self, date,code ,name,TCLOSE,HIGH,LOW,TOPEN,LCLOSE,CHG,PCHG,TURNOVER,VOTURNOVER,VATURNOVER,TCAP,MCAP):
        self.date = date
        self.code = code
        self.name = name
        self.TCLOSE = TCLOSE
        self.HIGH = HIGH
        self.LOW = LOW
        self.TOPEN = TOPEN
        self.LCLOSE = LCLOSE
        self.CHG = CHG
        self.PCHG = PCHG
        self.TURNOVER = TURNOVER
        self.VOTURNOVER = VOTURNOVER
        self.VATURNOVER = VATURNOVER
        self.TCAP = TCAP
        self.MCAP = MCAP

# page = requests.get('http://quotes.money.163.com/service/chddata.html?code=0601857&start=20071105&end=20071106&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP')
# print(page.text)
# 
# xq = requests.get('https://xueqiu.com/v4/stock/quotec.json?code=SH601318')
# print(xq.text)
# lines = page.text.split('\n')
# for line in lines:
#     line = line.encode('utf-8')
    # fields = line.split(',')
    # if fields.__len__()==16:
    #     stk0601857 = Stock(fields[0],fields[1],fields[2],fields[3],fields[4],fields[5],fields[6],fields[7],fields[8],fields[9],fields[10],fields[11],fields[12],fields[13],fields[14])
    #     print(stk0601857.name)

# if __name__ == '__main__':
#     print("a")
#
#     f_csv = csv.reader(page.text)
#     headers = next(f_csv)
#     for row in f_csv:
#         print(row)


