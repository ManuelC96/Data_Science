
import numpy as np

# data = np.array([[1,2,3],["r","r","r"]])
# print(data)
# data = data.T
# print(data)




data = np.random.randint(10, size=(50))
np.random.shuffle(data)
zeros = np.zeros((data.size, data.max() + 1))
zeros[np.arange(data.size), data] = 1 
print(data)
print(zeros)
