import pandas as pd
import numpy as np

filePath = '/Volumes/MUYOUNG/LZL/C2black00001.csv'
data = pd.read_csv(filePath)
# change the column heading below
x = data.Time[2:].to_numpy()
y = data.Ampl[2:].to_numpy()

mean = np.mean(y)
stdev = np.std(y)
percentage = stdev/mean*100

print('mean is ' + str(mean) + ' V')
print('stdev is '+ str(stdev) + ' V')
print('percentage is ' + str(percentage) + ' %')