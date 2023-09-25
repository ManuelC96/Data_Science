import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


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

# PANDAS define the steps

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
# print(df[["zona","incassi", "spese"]])
# # iloc interger location based row column
# print(df.iloc[0:2,0:2])
# # iloc access a group of rows and columns by label
# print(df.loc["Mark","zona"])
# # group
# gr = df.groupby(["zona"])
# print(gr.groups)
# # - order
# 


# Exercise Netflix
# data processing
df = pd.read_csv("netflix_titles.csv")
df.head
df.shape
df.isnull().any()
df.isnull().sum()
df.isnull().sum().sum()
df.director.fillna('NoDirector', inplace=True)
df.director
df.cast.fillna('NoCast', inplace=True)
df.cast
df.country.fillna('NoCast', inplace=True)
df.country
df.dropna(subset=["date_added","rating","duration"], inplace = True)
# print(df.isnull().any())

minYear = df["release_year"].min()
maxYear = df["release_year"].max()
minYear
maxYear
df.groupby('rating').groups
df.groupby('rating').get_group('PG-13')
df.groupby('rating').get_group('PG-13').sort_values(by = ['release_year'])

# for i in range(0,len(df.type.value_counts())):
#     label = df.type.value_counts().index[i]
#     print(label)
#     number = df.type.value_counts().iloc[i]
#     print(number)



    
# plt.figure(figsize=(12, 6))
# plt.title("Series vs Films")
# plt.pie(df.type.value_counts(),
#         labels = df.type.value_counts().index,
#         colors=['green', "blue"],
#         autopct="%1.2f%%"
#         )

# plt.show()

genres = df.listed_in.str.split(',',expand = True)
# print(df.listed_in.head())
# print(genres.shape)
genres = genres.stack()
# print(type(genres))
# print(genres.shape)

# print(genres.value_counts())
# print(genres.value_counts().index)

df_cast = df[df['cast'] != "NoCast"]

print(df_cast)

actors = df['cast'].str.split(',', expand=True)
print(actors)

actors = actors.stack() 
df.rating.unique()
df.rating.unique().any()


plt.figure(figsize=(12, 6))
plt.pie(df.rating.value_counts(), labels = df.rating.value_counts().index, autopct="%1.2f%%" )
# plt.show()


from collections import Counter

def return_counter(dataframe, column_name, limit):
    c = Counter(dataframe[column_name].values)
    most_commonm = c.most_common(limit)
    print(dict(most_commonm))

return_counter(df, 'country', 3)

df_Martin = df(df['director'] == 'Martin Scorsese')