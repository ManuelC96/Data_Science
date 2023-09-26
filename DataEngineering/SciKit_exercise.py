import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
from sklearn.datasets import fetch_california_housing, load_iris, make_blobs, make_regression
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# dataset = load_iris()

# x = dataset.data
# y = dataset.target
# labels = dataset.feature_names
# print(y)
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.5, random_state=42)\

# model = LogisticRegression(max_iter=200)
# model.fit(x_train, y_train)

# preds = model.predict(x_test)
# print("accurancy", accuracy_score(y_test, preds) * 100, '%')


# df = pd.DataFrame(
#     x, 
#     columns = labels 
# )

# # print(df)
# corr = df.corr()
# print(corr)

# # plt.figure(figsize=(10,5))
# # sns.heatmap(corr,
# #         xticklabels=corr.columns,
# #         yticklabels=corr.columns)
# # plt.title('Mappa delle correlazioni')
# # plt.show()


# X, y = make_blobs(n_samples=500, centers=3, cluster_std=1., random_state=42)
# print(X)
# print('Dimensioni X:', X.shape)
# print('Dimensioni y:', y.shape)

# plt.scatter(X [:,0], X[:,1], c=y, s=25)
# plt.show()

dataset = fetch_california_housing()
print(dataset.DESCR)
x = dataset.data
y = dataset.target
print(y)
print(len(y))
labels = dataset.feature_names

for id, feature_name in enumerate(labels):
    plt.figure(figsize=(20, 6))
    sns.scatterplot(x=y, y=x[:, id], s=10, alpha=0.25).set(title=feature_name)
    plt.show()
    a = input()
    if a == 1:
        continue1