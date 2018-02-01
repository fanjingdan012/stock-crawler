import tushare as ts


df1 = ts.get_industry_classified()
df1.to_csv('c:/day/industry.csv')
df = ts.get_hist_data('000875')
#直接保存
df.to_csv('c:/day/000875.csv')

#选择保存
# df.to_csv('c:/day/000875.csv',columns=['open','high','low','close'])