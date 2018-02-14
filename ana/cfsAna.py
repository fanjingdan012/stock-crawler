import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


dfo=pd.read_excel('../data/cfs1.xls',skiprows=1)

plt.style.use('ggplot')


from mpl_toolkits.mplot3d import axes3d

df = dfo[dfo['code']=='SZ000333']
df.fillna(0,inplace=True)
fig, ax = plt.subplots(figsize=(120,8))
width=0.1
t = df['enddate']
bizcashinfl = df['bizcashinfl']
bizcashoutf = df['bizcashoutf']
mananetr = df['mananetr']

invcashinfl = df['invcashinfl']
invcashoutf = df['invcashoutf']
invnetcashflow = df['invnetcashflow']

fincashinfl = df['fincashinfl']
fincashoutf = df['fincashoutf']
finnetcflow = df['finnetcflow']

ind = np.arange(len(t))  # the x locations for the groups
bizcashinflb = ax.bar(ind, bizcashinfl, width)
bizcashoutfb = ax.bar(ind+width, bizcashoutf, width,bottom=mananetr)
mananetrb = ax.bar(ind+width, mananetr, width)

invcashinflb = ax.bar(ind+2*width, invcashinfl, width)
invcashoutfb = ax.bar(ind+3*width, invcashoutf, width,bottom=invnetcashflow)
invnetcashflowb = ax.bar(ind+3*width, invnetcashflow, width)

fincashinflb = ax.bar(ind+4*width, fincashinfl, width)
fincashoutfb = ax.bar(ind+5*width, fincashoutf, width,bottom=finnetcflow)
finnetcflowb= ax.bar(ind+5*width, finnetcflow, width)
ax.set_xticks(ind + width / 6)
ax.set_xticklabels(t)
plt.show()

