import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np





data = pd.read_csv('DataScience\\data\\data_01.csv')
print(type(data))
X = data.iloc[:,0]
Y = data.iloc[:,1]
plt.scatter(X, Y)


# model building - parameter declaration
m = 0
c = 0

L = 0.001  # learning Rate
epochs = 1000  # gradient descendant iterations

n = len(X)  # exemples number

for i in range(epochs):
    Y_pred = m * X + c  # y pred

    D_m = (-2 / n) * sum(X * (Y - Y_pred))  # derivative against m
    D_c = (-2 / n) * sum(Y - Y_pred)  # derivative against c

    m -= L * D_m  # updating m
    c -= L * D_c  # updating c

print (m, c)

y_pred = m*X + c # liner eq formula based on predictions

plt.plot([min(X), max(X)], [min(y_pred), max(y_pred)], color = "red")
plt.show()