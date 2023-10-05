# multiple variabe in linear regression
# y = [m1 * x1 + m2 * x2 + m3 * x3 + ... m(n) * x(n)] + b + error

# check for linear relationship between indipend and dipendent variable(if linear ok else not)
# check for multicollinearity between dependent variables(if colinear not ok else ok)

import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# collect data
# dataPath = 'DataScience\data\ecomm_data.csv'
# df = pd.read_csv(dataPath)

# # check relationship between data
# # correlation = pd.plotting.scatter_matrix(df)
# # plt.show()

# # create dataser with selected feature
# x = df[["Time on App","Length of Membership"]]
# y = df['Yearly Amount Spent']

# # regression model 
# xTrain, xTest, yTrain, yTest = train_test_split(x,y,test_size=.5, random_state=42)
# model = LinearRegression()
# model.fit(xTrain, yTrain)

# print('slope: ', model.coef_)
# print('intercept: ', model.intercept_)

# # plotting the results
# yPred = model.predict(xTest)
# plt.scatter(range(len(list(xTest.iloc[:,1]))), yPred, color='black')
# plt.scatter(range(len(list(xTest.iloc[:,1]))), yTest, color='red', alpha=.8)
# # plt.plot([min(xTest), max(xTest)], [min(yPred), max(yPred)], color='red')
# plt.show()

# # calculate model performance
# from sklearn.metrics import mean_squared_error

# mse = mean_squared_error(yTest, yPred)
# print(mse)

# data
df = pd.read_csv("DataScience\data\insurance.csv")
# convert non num data in num data
df['sex'] = df['sex'].astype('category')
df['sex'] = df['sex'].cat.codes
df['smoker'] = df['smoker'].astype('category')
df['smoker'] = df['smoker'].cat.codes
df['region'] = df['region'].astype('category')
df['region'] = df['region'].cat.codes
# check for NAN data in data set
df.isnull().sum()

# extract independant variable
x = df.drop(columns='expenses')

# extract dependant variable
y = df['expenses']

# split dataset in training and test
xTrain, xTest, yTrain, yTest = train_test_split(x, y, random_state=42, test_size=.3)

# model
model = LinearRegression()
model.fit(xTrain, yTrain)

# intercept and slope
print(model.coef_)
print(model.intercept_)

# test model for prediction
yPred = model.predict(xTrain)

# visualize the model
plt.scatter(yTrain, yPred)
plt.xlabel('actual expenses')
plt.ylabel('pred expenses')
# plt.show()

# model goodness
from sklearn.metrics import r2_score
r2Score = r2_score(yTrain, yPred)
print(r2Score * 100, '%')