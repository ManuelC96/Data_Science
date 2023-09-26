import sklearn as sk

from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
# /-------------------------------------------------/
# /BASIC SCIKIT-LEARN WORKFLOW----------------------/
# /-------------------------------------------------/

# load a dataset
iris = datasets.load_iris()

# visualize dataSet
# print(iris.DESCR)

# create data for training model
x = iris.data
y = iris.target

print(x)
print(y)

# create training and validation dataset for model
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.2, random_state=1)

# implementation of a classifier based on logistic regression
ppn = LogisticRegression(random_state=10, max_iter=1000)

# algo training 
ppn.fit(x_train, y_train)

# accurancy test
y_pred = ppn.predict(x_test)
print(accuracy_score(y_test, y_pred))