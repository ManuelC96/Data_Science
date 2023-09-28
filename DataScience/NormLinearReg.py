import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

# normalized linear reg
data = pd.read_csv('DataScience\\data\\data_01.csv')
print(data)

x = data.iloc[:,0]
print(x)
y = data.iloc[:,1]
print(y)


def normalizer(data):
    maxVal = max(data)#max value
    minVal = min(data)#min value

    normArr = np.zeros(shape=(len(data),1))

    for i in range(len(data)):

        iNorm = (data[i] - minVal) / (maxVal - minVal)
        normArr[i] = iNorm
    
    return normArr


normX = normalizer(x)
normY = normalizer(y)


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
    :param x: x variable in dataset
    :param y: y variable in dataset
    :param m: slope(set to 0)
    :param q: y axis interceptor(set to 0)
    '''


    n = len(x)
 
    for c in range(cicle):
        for ep in range(epochs):

            yPred = m * x + q

            mDrv = (-2/n) * sum(x * (y - yPred))
            qDrv = (-2/n) * sum(y - yPred)
            m -= learningRate * mDrv
            q -= learningRate * qDrv
    
    return (m[0], q,)


m = gradienDescent(cicle= 10, epochs= 500, learningRate= 0.01, x= normX, y= normY)[0]
q = gradienDescent(cicle= 10, epochs= 500, learningRate= 0.01, x= normX, y= normY)[1]

yPred = normX * m + q
print(yPred)

plt.scatter(normX, normY)
plt.plot([min(normX), max(normX)],[min(yPred), max(yPred)], color = "red")
plt.show()


def test_function(p1, p2, p3):
    """
    test_function does blah blah blah.

    :param p1: describe about parameter p1
    :param p2: describe about parameter p2
    :param p3: describe about parameter p3
    :return: describe what it returns
    """ 
    pass