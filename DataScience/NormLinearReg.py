import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

# normalized linear reg
data = pd.read_csv('DataScience\\data\\data_01.csv')


x = data.iloc[:,0]

y = data.iloc[:,1]



def normalizer(data):
    maxVal = max(data)#max value
    minVal = min(data)#min value

    normArr = np.zeros(shape=(len(data),1))

    for i in range(len(data)):

        iNorm = (data[i] - minVal) / (maxVal - minVal)
        normArr[i] = iNorm
    
    return normArr# normalized array


normX = normalizer(x)# x avriables
normY = normalizer(y)#y variables

# usigng gradiend descent on MSE to calculate the besat fit values for m and q
def gradienDescent(cicle: int,
    epochs: int, 
    learningRate: float , 
    x : float,
    y : float,
    m = 0, 
    q = 0, 
    ):
    '''
    Gradient descent algorithm
    :param cicle: number of training cicles
    :param epochs: number of subtraining cicles
    :param learningRate: recommended rate 0.001 - 0.1
    :param x: x variables in dataset
    :param y: y variables in dataset
    :param m: slope(set to 0)
    :param q: y axis interceptor(set to 0)
    '''


    n = len(x)
 
    for c in range(cicle):
        for ep in range(epochs):

            yPred = m * x + q

            mDrv = (-2/n) * sum(x * (y - yPred))#derivate mse against m
            qDrv = (-2/n) * sum(y - yPred)#derivate the mse against q
            m -= learningRate * mDrv #update m
            q -= learningRate * qDrv #update q
    
    return (m[0], q[0],)


m = gradienDescent(cicle= 1, epochs= 500, learningRate= 0.01, x= normX, y= normY)[0]
q = gradienDescent(cicle= 1, epochs= 500, learningRate= 0.01, x= normX, y= normY)[1]
print(m, q)
yPred = normX * m + q
print(yPred)

plt.scatter(normX, normY)
plt.plot([min(normX), max(normX)],[min(yPred), max(yPred)], color = "red")
plt.scatter([np.mean(normX)],[np.mean(normY)], color = "black", marker='o', linewidths=8)

plt.show()

# animating the process
# cicles = 100
# for i in range(cicles):
#     m = gradienDescent(cicle= i, epochs= 500, learningRate= 0.01, x= normX, y= normY)[0]
#     q = gradienDescent(cicle= i, epochs= 500, learningRate= 0.01, x= normX, y= normY)[1]
#     yPred = normX * m + q
#     plt.scatter(normX, normY)
#     plt.plot([min(normX), max(normX)],[min(yPred), max(yPred)], color = "red")
#     plt.scatter([np.mean(normX)],[np.mean(normY)], color = "black", marker='o', linewidths=8)

#     plt.pause(0.01)
#     plt.clf()