from xlrd import open_workbook
def readStockList(shOrSz,rangeStart,rangeEnd):
    stockList=[]
    stockxls = './stocks.xlsx'
    with open(stockxls, 'rb') as f:
        book = open_workbook(stockxls)
        #print(open_workbook(file_contents=mmap(f.fileno(),0,access=ACCESS_READ)))
        #sheet = book.sheet_by_index(0)
        sheet = book.sheet_by_name(u'SH')
        if(shOrSz=='SZ'):
            sheet = book.sheet_by_name(u'SZ')
        for i in range(rangeStart,rangeEnd):
                stockList.append(sheet.cell_value(i, 0))
    return stockList
