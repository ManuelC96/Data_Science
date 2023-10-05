import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


df = pd.read_csv('DataScience\data\position_salaries.csv')



x = df.iloc[:, 1:2].values
y = df.iloc[:,2].values
print(y)


xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=.3, random_state= 1)


poly = PolynomialFeatures(degree = 4)
Xpoly = poly.fit_transform(x)
print(Xpoly)
print(x)

model = LinearRegression()
model.fit(Xpoly, y)


plt.scatter(x, y, color='red')
plt.plot(x, model.predict(Xpoly), color='green')

plt.show()


