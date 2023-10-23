import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

# Gradient Descent

def yFunc(x):
    return x**2

def derivative(x):
    return 2*x

x = np.arange(-100, 100, 0.1)
y = yFunc(x)
pos = -100
currentPosition = (pos, yFunc(pos))

learningRate = 0.10

for _ in range(500):
    print(currentPosition[0])
    print(derivative(currentPosition[0]))
    print(learningRate * derivative(currentPosition[0]))
    newX = currentPosition[0] - learningRate * derivative(currentPosition[0])
    newY = yFunc(newX)
    currentPosition = (newX, newY)

    plt.plot(x, y)
    plt.scatter(currentPosition[0], currentPosition[1], color = 'Red')
    plt.pause(0.01)
    plt.clf()






