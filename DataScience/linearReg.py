import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_csv('DataScience\\data\\data_01.csv')
print(type(data))
X = data.iloc[:,0]

Y = data.iloc[:,1]
plt.scatter(x, y)
# plt.show()

# Costruzione del modello - dichiarazione parametri
m = 0
c = 0

L = 0.001  # learning Rate
epochs = 1000  # numero di iterazioni su cui utilizzare la discesa del gradiente

n = len(X)  # numero di esempi del dataset

for i in range(epochs):
    Y_pred = m * X + c  # predizione di y

    D_m = (-2 / n) * sum(X * (Y - Y_pred))  # derivata prima rispetto ad m
    D_c = (-2 / n) * sum(Y - Y_pred)  # derivata prima rispetto a c

    m -= L * D_m  # aggiornamento del parametro m
    c -= L * D_c  # aggiornamento del parametro c

print (m, c)