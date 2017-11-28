
#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from lxml import html
from bs4 import BeautifulSoup
def crawStockList():
    page = requests.get('http://quote.eastmoney.com/stock_list.html')
    soup = BeautifulSoup(page.text,'lxml')
    print (soup.select('.qox .quotebody ul li a'))
    links = soup.select('.qox .quotebody ul li a')
    stockList = []
    for i in links:
        href=i.attrs['href']
        stockList.append(href[27:35].upper())
    return stockList
if __name__ == "__main__":
    print(crawStockList())
