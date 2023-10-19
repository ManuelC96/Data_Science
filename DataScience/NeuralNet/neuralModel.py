# Neural model

import numpy as np
import struct as st
import time
import pandas as pd
from matplotlib import pyplot as plt


# prepare data
data = pd.read_csv(r"C:\Users\mchiocchetta\Desktop\Data_Science\dataSets\MNIST\MNIST.csv") 

m, n = data.shape

data = np.array(data)
np.random.shuffle(data)


dataDev = data[:1000].T
yDev = dataDev[0] 
xDev = dataDev[1: n]

dataTrain = data[1000: m ].T

yTrain = dataTrain[0]
xTrain = dataTrain[1:n]
print(xTrain.shape)


# define parameter w and b (weights an biases)
def initParam():
    W1 = np.random.randn(10, 784)#define random weights between data and first neuron layer
    print(W1.shape)
    B1 = np.random.randn(10, 1)
    W2 = np.random.randn(10,10)
    B2 = np.random.randn(10,1)
    return W1, B1, W2, B2

def sigmoid(X):
   
    return 1 / (1 + np.exp(-X))
    

def softMax(X):
    return np.exp(X) / np.sum(np.exp(X))
    

def oneHot(Y):
    oneHotY = np.zeros((Y.size, Y.max() + 1))
    oneHotY[np.arange(Y.size), Y] = 1
    oneHotY = oneHotY.T
    return oneHotY




# define forward prop 
def forwardProp(W1, B1, W2, B2, X):
    Z1 = W1.dot(X) + B1
    A1 = sigmoid(Z1) 
    Z2 = W2.dot(A1) + B2
    A2 = softMax(Z2)
    return Z1, A1, Z2, B2, Z1.shape

W1, B1, W2, B2 = initParam()
print(forwardProp(W1, B1, W2, B2, xTrain))


# define model erro
def cost(prediction, label):
    Cost = np.sqrt(np.sum(prediction - label)) 
    return Cost

# define backwarprop
def backwardProp(Z1, A1, Z2, A2, X, Y):
    m = Y.size 
    Y = oneHot(Y) 
    # find how each parameter and function influenced the cost
    # chain roule: 


    








































































































    
    