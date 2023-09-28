# multiple variabe in linear regression
# y = [m1 * x1 + m2 * x2 + m3 * x3 + ... m(n) * x(n)] + b + error

# chek for linear relationship between indipend and dipendent variable(if linear ok else not)
# check for multicollinearity between dependent variables(if colinear not ok else ok)

import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

dataPath = 'DataScience\data\data_02.csv'

data = pd.read_csv(dataPath)

def normalizer(data):
    maxVal = max(data)#max value
    minVal = min(data)#min value

    normArr = np.zeros(shape=(len(data),1))

    for i in range(len(data)):

        iNorm = (data[i] - minVal) / (maxVal - minVal)
        normArr[i] = iNorm
    
    return normArr            


