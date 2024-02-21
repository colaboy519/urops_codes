import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

filePath1 = '/Users/JohnnyLin/Desktop/Dzmitry_Lab /UROPS/F1 wed00000.csv'
filePath2 = False
data1 = pd.read_csv(filePath1)
if (filePath2):
    data2 = pd.read_csv(filePath2)
# add code here: that ignores any number of lines of heading
# change the column heading below
if  (filePath1):
    x1 = data1.Time[2:].to_numpy()
    y1 = data1.Ampl[2:].to_numpy()
if (filePath2):
    x2 = data2.Time[2:].to_numpy()
    y2 = data2.Ampl[2:].to_numpy()

#plot the two data sets
plt.plot(x1,y1, 'or', label='data1')
# plt.plot(x2,y2, 'ob', label='data2')
plt.legend()
plt.xlabel('time')
plt.ylabel('voltage')
plt.show()