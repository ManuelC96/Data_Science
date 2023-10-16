# Simple neural network MNIST database
import numpy as np
import struct as st

imgPath = r'DataScience\data\MNIST\train-images.idx3-ubyte'
labelsPath = r'DataScience\data\MNIST\train-labels.idx1-ubyte'

with open(imgPath, 'rb') as imageFile:
    imageFile.seek(0)#specify bit offset
    magic = st.unpack('>4b',imageFile.read(4))#magic number
    imageFile.seek(4)#specify bit offset
    imgNumb = st.unpack('>i',imageFile.read(4))#number of imgs
    imageFile.seek(8)#specify bit offset
    nRows = st.unpack('>i', imageFile.read(4))#number of rows
    imageFile.seek(12)#specify bit offset
    ncols = st.unpack('>i', imageFile.read(4))#number of colums



print(magic)
print(imgNumb)
print(nRows)
print(ncols)