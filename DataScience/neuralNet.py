# Simple neural network MNIST database
import numpy as np
import struct as st
from matplotlib import pyplot as plt
import time

imgPath = r'DataScience\data\MNIST\train-images.idx3-ubyte'
labelsPath = r'DataScience\data\MNIST\train-labels.idx1-ubyte'

with open(imgPath, 'rb') as imageFile:#open context manager, read file in binary format
    imageFile.seek(0)#specify bit offset
    magic = st.unpack('>4b',imageFile.read(4))#magic number
    imageFile.seek(4)#specify bit offset
    imgNumb = st.unpack('>i',imageFile.read(4))#number of imgs
    imageFile.seek(8)#specify bit offset
    nRows = st.unpack('>i', imageFile.read(4))#number of rows
    imageFile.seek(12)#specify bit offset
    nCols = st.unpack('>i', imageFile.read(4))#number of colums

nOfBytes = imgNumb[0]*nRows[0]*nCols[0]*1



with open(imgPath, 'rb') as imageFile:#open context manager, read file in binary format
    imageFile.seek(16)#specify bit offset
    imgArray = np.asarray(st.unpack('>' + f'{nOfBytes}' + 'B',imageFile.read(nOfBytes))).reshape((imgNumb[0],nRows[0], nCols[0]))
    




def mImageShow(array: list):
    for i in range(len(array)):
        plt.imshow(array[i])
        plt.pause(1)#plt pause image frame
        plt.clf()#plt clear image to show next one
    return None

mImageShow(imgArray)