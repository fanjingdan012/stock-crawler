# -*- coding: utf-8 -*-
import xlrd
import xlwt
from datetime import date,datetime
import pandas as pd


def set_style(name,height,bold=False):
    style = xlwt.XFStyle()  # 初始化样式

    font = xlwt.Font()  # 为样式创建字体
    font.name = name # 'Times New Roman'
    font.bold = bold
    font.color_index = 4
    font.height = height

    # borders= xlwt.Borders()
    # borders.left= 6
    # borders.right= 6
    # borders.top= 6
    # borders.bottom= 6

    style.font = font
    # style.borders = borders

    return style


def write_excel(fileName):
    f = xlwt.Workbook()
    sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True)
    row0 = [u'业务',u'状态',u'北京',u'上海',u'广州',u'深圳',u'状态小计',u'合计']
    column0 = [u'机票',u'船票',u'火车票',u'汽车票',u'其它']
    status = [u'预订',u'出票',u'退票',u'业务小计']

    for i in range(0,len(row0)):
        sheet1.write(0,i,row0[i])
    f.save(fileName)

    book = xlrd.open_workbook(fileName)
    #print(open_workbook(file_contents=mmap(f.fileno(),0,access=ACCESS_READ)))
    #sheet = book.sheet_by_index(0)
    for s in book.sheets():
        print ('Sheet:',s.name)
        for i in range(s.nrows):
            print( s.cell_value(i, 1))


def write_xlsx_pd():
    df = pd.DataFrame([['a', 'b'], ['c', 'd']],
    index = ['row 1', 'row 2'],
    columns = ['col 1', 'col 2'])

    df = pd.read_json(_, orient='records')


    df.to_excel('aa.xlsx', sheet_name='Random Data')


if __name__ == '__main__':
    #generate_workbook()
    #read_excel()
    write_xlsx_pd()