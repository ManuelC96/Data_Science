# Simple neural network MNIST database
import numpy as np
import struct as st

imgPath = r'DataScience\data\MNIST\train-images.idx3-ubyte'
labelsPath = r'DataScience\data\MNIST\train-labels.idx1-ubyte'

with open(imgPath, 'rb') as imageFile:
    imageFile.seek(0)#specify bit offset
    magic = st.unpack('>4b',imageFile.read(4))#magic number

print(magic)