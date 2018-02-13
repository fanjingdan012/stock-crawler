#多序列条状图
#解决的方法吧每个类别占据的空间，分为多个部分，想要显示几个长条，将其分为几个部分，建议在增加一个额外的空间， 以便区分两个相邻的类别
import matplotlib.pyplot as plt
import numpy as np



import pandas as pd
import numpy as np
#使用pandas读取excel文件
df=pd.read_excel('../data/bs1.xls')
# names=['code','reportdate','totasset','totliabsharequi']
# df = df[df['code']=='SH600060']
print (df)

plt.style.use('ggplot')


#excel文件的写出
#data.to_excel("abc.xlsx",sheet_name="abc",index=False,header=True)  #该条语句会运行失败，原因在于写入的对象是np数组而不是DataFrame对象,只有DataFrame对象才能使用to_excel方法。

# DataFrame(data).to_excel("abc.xlsx",sheet_name="123",index=False,header=True)

#excel文件和pandas的交互读写，主要使用到pandas中的两个函数,一个是pd.ExcelFile函数,一个是to_excel函数




# index = np.arange(5)
# values1 = [5, 7, 3, 4, 6]
# values2 = [6, 6, 4, 5, 7]
# values3 = [5, 6, 5, 4, 6]
#
# plt.axis([0, 5, 0, 8])
# plt.title("A Multiseries Bar Chart", fontsize = 0)
# plt.bar(index, df[(df[''])], bw, color = 'b')
# plt.bar(index+bw, values2, bw, color = 'g')
# plt.bar(index+2*bw, values3, bw, color = 'r')
# plt.xticks(index+1.5*bw, ['A', 'B', 'C', 'D', 'E'])
# plt.show()