from xlrd import open_workbook
import pandas as pd


def read_stock_list(sh_sz, range_start, range_end):
    stock_list = []
    stockxls = '../data/stocks.xlsx'
    with open(stockxls, 'rb') as f:
        book = open_workbook(stockxls)
        # print(open_workbook(file_contents=mmap(f.fileno(),0,access=ACCESS_READ)))
        # sheet = book.sheet_by_index(0)
        sheet = book.sheet_by_name(u'SH')
        if sh_sz == 'SZ':
            sheet = book.sheet_by_name(u'SZ')
        for i in range(range_start, range_end):
            stock_list.append(sheet.cell_value(i, 0))
    return stock_list


def read_industry_stock_list(range_start, range_end):
    stock_list = []
    stockxls = '../data/industry.xlsx'
    with open(stockxls, 'rb') as f:
        book = open_workbook(stockxls)
        # print(open_workbook(file_contents=mmap(f.fileno(),0,access=ACCESS_READ)))
        sheet = book.sheet_by_index(0)
        for i in range(range_start, range_end):
            stock_list.append(sheet.cell_value(i, 0))
    return stock_list


def read_sw_industry_stock_df(industry):
    dfo = pd.read_csv('../data/SwClass.csv')
    df = dfo[dfo['industry'] == industry]
    df=df[df['is_end'] == 'N']
    return df


def read_sw_industry_stock_df_by_code(stock_code):
    dfo = pd.read_csv('../data/SwClass.csv')
    df = dfo[dfo['stock_code'] == stock_code]
    return df