import numpy as np

array = np.arange(0,20).reshape(5,4)

# axis=1 row

# axis=0 column


# it = np.nditer(array, flags = ["f_index"])

# while not it.finished:
#     print("%d, %d"%(it[0], it.index))
#     iteratorList = it.iternext()

# print(iteratorList)
# #------------------------------------------------

# it = np.nditer(array, flags = ["c_index"])

# while not it.finished:
#     print("%d, %d"%(it[0], it.index))
#     iteratorList = it.iternext()

# print(iteratorList)
# #------------------------------------------------
# it = np.nditer(array, flags = ["multi_index"])

# for i in it:
#     print(i, it.multi_index )

# print(list(it))
#------------------------------------------------
# it = np.nditer(array)

# for i in it:
#     print(i, type(i) )
#------------------------------------------------

# a = np.arange(0,5)
# b = np.arange(10).reshape(2,5)

# for x, y in np.nditer([a,b]):
#     print(x, y, x*y)

# #------------------------------------------------
# a = np.arange(30, 42)
# print(a)
# b = a.reshape(3,4)
# print(b)
# print(b.T)
# print(b.T.shape,"\n" ,b.T)

#------------------------------------------------
# a = np.array([1,2,3])
# b = np.array([4,5,6])
# print(np.concatenate([a, b]))

# a = np.array([[1],[2],[3]])
# b = np.array([[4],[5],[6]])
# print(np.concatenate([a, b]))

# a = np.array([1,2,3])
# b = np.array([4,5,6])
# print(np.vstack([a, b]))# vStack colunms
# print(np.hstack([a, b]))# hStack row

a = np.array([[1,5],[2,5],[3,5]])
b = np.array([[4,5],[5,5],[6,5]])
# print(np.vstack([a, b]))
# print(np.hstack([a, b]))

# print(np.stack([a,b], axis = 1))
# print(np.stack([a,b], axis = 1).shape)


# g = np.random.default_rng(seed=3)

# a = g.integers(low=0, high=10, size=8)

# Statistic
mx = np.array([[1,24,36], [5,54,16], [77,29,2]])
print(mx)
print('')
print(mx.max(axis=1))
print('')
print(mx.max(axis=0))
