import statistics
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------------------------ this funciton is to calcualte average and stdv of a 2D data set ------------------------------------------------
filePath = 'put file path here'
data = pd.read_csv(filePath)
# add code here: that ignores any number of lines of heading
# add code here: to read different types of data file: csv, ascii, etc
# change the column heading below to mathch the actual data file heading
x = data.Time[2:].to_numpy()
y = data.Ampl[2:].to_numpy()

mean = np.mean(y)
stdev = np.std(y)

#add unit at the back
print('mean is ' + str(mean))
print('stdev is '+ str(stdev))


# ------------------------------------------------ This function is to plot 2 sets of 2D data on the same graph ------------------------------------------------
filePath1 = 'put file1 path here'
filePath2 = 'put file2 path here'
data1 = pd.read_csv(filePath)
data2 = pd.read_csv(filePath)
# add code here: that ignores any number of lines of heading
# change the column heading below
x1 = data1.Time[2:].to_numpy()
y1 = data1.Ampl[2:].to_numpy()
x2 = data2.Time[2:].to_numpy()
y2 = data2.Ampl[2:].to_numpy()

#plot the two data sets)
plt.plot(x1,y1, 'or', label='data1')
plt.plot(x2,y2, 'ob', label='data2')
plt.legend()
plt.xlabel('time')
plt.ylabel('voltage')
plt.show()