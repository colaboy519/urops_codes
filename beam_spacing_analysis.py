import imageio
import numpy as np
import glob
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

files = glob.glob('./*.tiff')

dist1_images = []
dist2_images = []
dist3_images = []

for i in range(len(files)):    
    if 'a' in files[i]:
        dist1_images.append(np.array(imageio.imread(files[i]))[:,:,2].astype('float64'))
    elif 'b' in files[i]:
        dist2_images.append(np.array(imageio.imread(files[i]))[:,:,2].astype('float64'))
    elif 'c' in files[i]:
        dist3_images.append(np.array(imageio.imread(files[i]))[:,:,2].astype('float64'))
    
image1 = np.asarray(sum(dist1_images))
image2 = np.asarray(sum(dist2_images))
image3 = np.asarray(sum(dist3_images))

images = [image1, image2, image3]

#fig, ax = plt.subplots(len(images))

for j in range(len(images)):
    column_image = images[j].sum(axis=0)
    
    threshold = column_image.max()/(np.e**2)
    locMax = np.where(column_image == column_image.max())[0][0]
    
    pos = []
    for i in range(len(column_image)):
        if column_image[i] <= threshold:
            pos.append(i)
            
    dpos = np.diff(pos)
    max_dpos = np.where(dpos == dpos.max())[0][0]
    
    cleft_w = pos[max_dpos]
    cright_w = pos[max_dpos + 1]
    
    cdiameter = (cright_w  - cleft_w)*3.75*10**(-6)/2
    
    print('Distance', j, ':', cdiameter*10**(3), 'mm')
    
    row_image = images[j].sum(axis=1)
    threshold = row_image.max()/(np.e**2)
    locMax = np.where(row_image == row_image.max())[0][0]
    
    pos = []
    for i in range(len(row_image)):
        if row_image[i] <= threshold:
            pos.append(i)
            
    dpos = np.diff(pos)
    max_dpos = np.where(dpos == dpos.max())[0][0]
    
    rleft_w = pos[max_dpos]
    rright_w = pos[max_dpos + 1]
    
    rdiameter = (rright_w  - rleft_w)*3.75*10**(-6)/2
    
    print('Distance', j, ':', rdiameter*10**(3), 'mm')