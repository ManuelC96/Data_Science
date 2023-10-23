import numpy as np
import struct as st
import time
import pandas as pd
import shutil
from matplotlib import pyplot as plt

# extraxt zip file
# shutil.unpack_archive(r"C:\Users\manue\Downloads\Data_Science\dataSets\MNIST\MNIST.zip",r"C:\Users\manue\Downloads\Data_Science\DataScience\NeuralNet")

data = pd.read_csv(r"C:\Users\manue\Downloads\Data_Science\dataSets\MNIST\MNIST.csv") 

m, n = data.shape

data = np.array(data)
np.random.shuffle(data)
# data division
div = .1
limit = len(data)-int(len(data) * div)
print(limit)

dataDev = data[:limit].T
yDev = dataDev[0] 
xDev = dataDev[1: n]

dataTrain = data[limit: m ].T
print(dataTrain)
yTrain = dataTrain[0]

xTrain = dataTrain[1:n]


# define parameter w and b (weights an biases)
def initParam():
    W1 = np.random.randn(10, 784, )#define random weights between data and first neuron layer
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

Y = oneHot(yTrain)
a =1
# define forward prop 
def forwardProp(W1, B1, W2, B2, X):
    Z1 = W1.dot(X) + (-B1)
    # print(Z1.shape)
    A1 = sigmoid(Z1) 
    # print(A1.shape)
    Z2 = W2.dot(A1) + (-B2)
    # print(Z2.shape)
    A2 = softMax(Z2)
    # print(A2.shape)
    return Z1, A1, Z2, B2

W1, B1, W2, B2 = initParam()
Z1, A1, Z2, A2 = forwardProp(W1, B1, W2, B2, xTrain)

# define model error
def cost(prediction, label):
    Cost = (np.power((prediction - label), 2))
    Cost = Cost.T
    totCosts = []
    for i in range(len(Cost)):
        elCost = np.sum(Cost[i])
        totCosts.append(elCost)
    return totCosts

    
def stdDev(X):
    Tot = 0
    for k in range(len(X)):
        Tot += X[k]
    Tot = Tot/len(X)
    Tot = np.sqrt(Tot)
    return Tot
   
errorX = cost(A2, Y)
print(stdDev(errorX))


# define backwardprop
def backwardProp(Z1, A1, Z2, A2, Y, X):
    m = Y.size 
    Y = oneHot(Y) 
    # find influences of W and b on cost
    # W1 = W1 - alpha * dCost/dW1
    # b1 = b1 - alpha * dCost/db1 
    # W2 = W2 - alpha * dCost/dW2 
    # b2 = b2 - alpha * dCost/db2
    # for backward we only need dCost/d(W[n] and b[n])


#     return dCdW1, dCdB1, dCdW2, dCdB2
    
# # print(backwardProp(Z1, A1, Z2, B2, yTrain, xTrain))

# def paramUpdate(W1, B1, W2, B2, dW1, dB1, dW2, dB2, alpha):
#     W1 = W1 - alpha * dW1.T
#     B1 = B1 - alpha * dB1.T    
#     W2 = W2 - alpha * dW2.T
#     B2 = B2 - alpha * dB2.T
#     return W1, B1, W2, B2

# def gradientDescent(X, Y, Cicles, subCicles):
#     W1, B1, W2, B2 = initParam()    
#     for i in range(Cicles):
#         for j in range(subCicles):

#             Z1, A1, Z2, A2 = forwardProp(W1, B1, W2, B2, X)
#             dCdW1, dCdB1, dCdW2, dCdB2 = backwardProp(Z1, A1, Z2, A2, Y,X)
#             W1, B1, W2, B2 = paramUpdate(W1, B1, W2, B2, dCdW1, dCdB1, dCdW2, dCdB2, alpha=0.01)
#     return  W1, B1, W2, B2 


# print(gradientDescent(xTrain, yTrain, 10, 10))




