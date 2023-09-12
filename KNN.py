# K-nearest neighbors


# class Point:
#     def __init__(self, x, y) -> None:
#         self.x_axis = x
#         self.y_axis = y

#     def getDistance(self, point):
#         import math

#         distance = math.sqrt(
#             math.pow(point.y_axis - self.y_axis, 2)
#             + math.pow(point.x_axis - self.x_axis, 2)
#         )
#         return distance


def minkowskiDistance(v1, v2, p=2):
    dim = len(v1)
    distance = 0

    for d in range(dim):
        distance += abs(v1[d] - v2[d]) ** 2
        

    distance = distance ** (1 / p)
    return distance


def normMatrix(matrix: list):
    # formula = point in range / range == (x - xMin)/(xMax - xMin)
    turnedMx = []
    normMx = []

    for i in range(len(matrix[0])):
        turnCol = [row[i] for row in matrix]
        turnedMx.append(turnCol)
    
    for el in turnedMx:
        minVal = min(el)
        maxVal = max(el)
        normVals = []
        for i in el:
            normEl = (i - minVal) / (maxVal - minVal)
            normVals.append(normEl)
        normMx.append(normVals)
    return normMx


def getNeighbors(k, testRow, dataSet):
    distances = []
    for i in range(len(dataSet)):
        row = dataSet[i]
        dist = minkowskiDistance(row, testRow)
        distances.append(
            (i, dist),
        )
    
    distances.sort(key= lambda t : t[1])
    kNeighbors = []
    for i in range(k):
        kNeighbors.append(distances[i][0])
    return kNeighbors






def classFromNeighbors(indices : list, classes : list):
    d = {}
    for i in indices:
        y = classes[i]
        if d.get(y) == None:
            d[y] = 1
        else:
            d[y] += 1

    output = 0
    c = None

    for k, v in d.items():
        if v > output:
            output = v
            c = k
    return c


m = [
    [5.1, 3.5, 1.4, 0.2],
    [4.9, 3.1, 1.1, 0.1],
    [5.7, 2.1, 0.8, 0.4],
    [4.1, 0.5, 1.1, 0.15],
]


n = getNeighbors(3,[5.7, 2.1, 0.8, 0.4], m)

classes = ["fruit", "cereal", "cereal", "fruit"]

print(classFromNeighbors(n, classes))

class KNNClssifier():
    def __init__(self, k = 5, p = 2, x = [] , y = []):
        self.k = k
        self.p = p
        self.x = list(x)
        self.y = list(y)
        self.xNorm = x.normMatrix(x)

    def normMatrix(self, matrix: list):
    # formula = point in range / range == (x - xMin)/(xMax - xMin)
        turnedMx = []
        normMx = []

        for i in range(len(matrix[0])):
            turnCol = [row[i] for row in matrix]
            turnedMx.append(turnCol)
        
        for el in turnedMx:
            minVal = min(el)
            maxVal = max(el)
            normVals = []
            for i in el:
                normEl = (i - minVal) / (maxVal - minVal)
                normVals.append(normEl)
            normMx.append(normVals)
        return normMx
        
    def minkowskiDistance(self, v1, v2, p=2):
        dim = len(v1)
        distance = 0

        for d in range(dim):
            distance += abs(v1[d] - v2[d]) ** 2
            

        distance = distance ** (1 / p)
        return distance