import pandas as pd
import numpy as np
import csv

# data = np.array([1,2,3,4,5,6,7,8,66,88])

# # create a series
# # s = pd.Series(data)
# # print(s)
# # print(s[::-1])
# # print(s.head())
# # print(s.tail())

# # # create a dataFrame
# # dF = pd.read_csv("items.csv")
# # print(pd.DataFrame(dF))


# # ceate a df based on series
# s1 = pd.Series([1,2,3,4])
# s2 = pd.Series([66,7,23,9])
# s3 = pd.Series(['a',list((1,2,3)),'c',9])
# # print(s1.min())
# # print(s1.max())
# # print(s1.tail())
# # print(s1.describe())
# # df = pd.DataFrame(
# #     {
# #         's1' : s1,
# #         's2' : s2,
# #         's3' : s3

# #     }
# # )#dataframe can contain any type of data

# # print(df)
# # print(df.describe())
# # print(df.describe().T)

# PANDAS define the step

# define DataSet
df = pd.DataFrame({
    "nome":["Mark","Andrea","Luca","Alex","Jack","Max","Lou","Kim","Frank","Sam","Paul"],
    "zona":["Sud","Nord","Sud","Nord","Sud","Sud","Centro","Centro","Nord","Sud","Centro"],
    "incassi":[49000,52000,49000,34000,52000,72000,49000,55000,67000,65000,67000],
    "spese":[42000,43000,50000,44000,38000,39000,42000,60000,39000,44000,45000]
})

# work with data set
# - set index 
df.set_index('nome', inplace=True)

# - filter

# select for column [normal viz] [[tabel viz]]
print(df[["zona","incassi", "spese"]])
# iloc interger location based row column
print(df.iloc[0:2,0:2])
# iloc access a group of rows and columns by label
print(df.loc["Mark","zona"])

# - order
# 