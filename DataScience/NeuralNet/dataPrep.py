# simple neural network mnist database
import numpy as np
import struct as st
import time
import os
import pandas as pd
from zipfile import ZipFile as zf
from matplotlib import pyplot as plt

imgpath = r'C:\Users\mchiocchetta\Desktop\Data_Science\dataSets\MNIST\train-images.idx3-ubyte'
labelspath = r'C:\Users\mchiocchetta\Desktop\Data_Science\dataSets\MNIST\train-labels.idx1-ubyte'

# extract numbers froms MNIST
with open(imgpath, 'rb') as imagefile:#open context manager, read file in binary format
    imagefile.seek(0)#specify bit offset
    magic = st.unpack('>4b',imagefile.read(4))#magic number
    imagefile.seek(4)#specify bit offset
    imgnumb = st.unpack('>i',imagefile.read(4))#number of imgs
    imagefile.seek(8)#specify bit offset
    nrows = st.unpack('>i', imagefile.read(4))#number of rows
    imagefile.seek(12)#specify bit offset
    ncols = st.unpack('>i', imagefile.read(4))#number of colums

nofbytes = imgnumb[0]*nrows[0]*ncols[0]*1

with open(imgpath, 'rb') as imagefile:#open context manager, read file in binary format
    imagefile.seek(16)#specify bit offset
    # imgArray = np.asarray(st.unpack('>' + f'{nofbytes}' + 'B',imagefile.read(nofbytes))).reshape((imgnumb[0],nrows[0], ncols[0]))

    xVar = np.asarray(st.unpack('>' + f'{nofbytes}' + 'B',imagefile.read(nofbytes))).reshape((imgnumb[0],(nrows[0] * ncols[0]))) 
#/////////////////////////////////////////////////////////////////////////////////////////////// 
#///////////////////////////////////////////////////////////////////////////////////////////////

# extract labels from MNIST 
with open(labelspath, 'rb') as labelfile:
    labelfile.seek(0)
    magic = st.unpack(">4b", labelfile.read(4))
    # print(magic)
    labelfile.seek(4)
    labelnumb = st.unpack('>i',labelfile.read(4))
    # print(labelnumb)
    
totalbytes = labelnumb[0]

with open(labelspath, "rb") as labelfile:
    labelfile.seek(8) 
    labels = np.asarray(st.unpack(">" + f"{totalbytes}" + "b", labelfile.read(totalbytes))).reshape((totalbytes))
#///////////////////////////////////////////////////////////////////////////////////////////////     
#///////////////////////////////////////////////////////////////////////////////////////////////

# def mimageshow(array: list):
#     for i in range(len(array)):
#         plt.imshow(array[i])
#         plt.pause(1)#plt pause image frame
#         plt.clf()#plt clear image to show next one
#     return none

# mimageshow(imgaArray)
#///////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////////

# Create CSV file for better management
csvLabels = list()
for i in range(784):
    csvLabels.append(f"pixel-{i}")
print(len(csvLabels))

with open(r"C:\Users\mchiocchetta\Desktop\Data_Science\dataSets\MNIST\MNIST.csv", 'w',) as f:
    f.write("%s"%("number,"))
    for j in range(len(csvLabels)):
        
        if j <= 782:
            f.write("%s"%(csvLabels[j]+','))
        else:
            f.write("%s"%(csvLabels[j]))
    f.write('\n')
    for k in range(len(labels)):
        f.write(str(labels[k])+",")
    
        for l in range(len(xVar[k])):
            if l <= 782:
                f.write(str(xVar[k][l])+',')
            else:
                f.write(str(xVar[k][l]))
        f.write("\n")

# with zf("MNIST.zip", mode='w') as zFile:
#     zFile.write(r"C:\Users\mchiocchetta\Desktop\Data_Science\dataSets\MNIST\MNIST.csv")

# os.remove(r"C:\Users\mchiocchetta\Desktop\Data_Science\dataSets\MNIST\MNIST.csv")