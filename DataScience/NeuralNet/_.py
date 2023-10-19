
import numpy as np
import pandas as pd
data = np.array([[1,2,3],["r","r","r"]])
print(data.shape)
data = data.T
print(data)




# # data = np.random.randint(10, size=(50))
# # np.random.shuffle(data)
# # zeros = np.zeros((data.size, data.max() + 1))
# # zeros[np.arange(data.size), data] = 1 
# # # print(data)
# # # print(zeros)


# # def sigmoid(X):
# #     return 1 / (1 + np.exp(-X))


# # X = np.random.randint(0, 10, size= (5,5))
# # print(X)

# # print(sigmoid(X))


# # def softmax(X):
# #     return np.around(np.exp(X) / (np.sum(np.exp(X))),decimals=3)


# # print(softmax(X))

# # prepare data
# data = pd.read_csv(r"C:\Users\mchiocchetta\Desktop\Data_Science\dataSets\MNIST\MNIST.csv") 

# m, n = data.shape

# data = np.array(data)
# np.random.shuffle(data)


# dataDev = data[:1000].T
# yDev = dataDev[0] 
# xDev = dataDev[1: n]

# dataTrain = data[1000: m ].T

# yTrain = dataTrain[0]
# xTrain = dataTrain[1:n]

# # define parameter w and b (weights an biases)
# def initParam():
#     W1 = np.array(np.random.randn(10, 784),dtype=np.float128 )#define random weights between data and first neuron layer
#     B1 = np.random.randn(10, 1)
#     W2 = np.random.randn(10,10)
#     B2 = np.random.randn(10,1)
#     return W1, B1, W2, B2

# def sigmoid(X):
   
#     return 1 / (1 + np.exp(-X))
    

# # def softMax(X):
# #     return np.exp(X) / np.sum(np.exp(X))
    

# # def oneHot(Y):
# #     oneHotY = np.zeros((Y.size, Y.max() + 1))
# #     oneHotY[np.arange(Y.size), Y] = 1
# #     oneHotY = oneHotY.T
# #     return oneHotY




# # # define forward prop 
# # def forwardProp(W1, B1, W2, B2, X):
# #     Z1 = W1.dot(X) + B1
# #     A1 = sigmoid(Z1) 
# #     Z2 = W2.dot(A1) + B2
# #     A2 = softMax(Z2)
# #     return Z1, A1, Z2, B2

# # W1, B1, W2, B2 = initParam()
# # print(forwardProp(W1, B1, W2, B2, xTrain))

# x = np.array([1,2,3,4,5,6,7], dtype=np.float128)