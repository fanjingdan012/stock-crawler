import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    # Read the file
    #df = pd.read_excel("bonus.xls")
    # Output the number of rows
    #print("Total rows: {0}".format(len(df)))
    # See which headers are available
    #print(list(df))
    #print(df[df['href']=='https://xueqiu.com/stock/f10/bonus.json?symbol=SH600000'].count())
    x = np.linspace(-1, 1, 50)
    y = 2*x + 1
    plt.figure()
    plt.plot(x, y)
    plt.show()