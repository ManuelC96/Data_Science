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
        print (distance)

    distance = distance ** (1 / p)
    return distance


def normMatrix(matrix: list):
    # formula = point in range / range == (x - xMin)/(xMax - xMin)
    turnedMx = []
    normMx = []

    for i in range(len(matrix[0])):
        turnCol = [row[i] for row in matrix]
        turnedMx.append(turnCol)
    print(turnedMx)
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
    
    print(distances)
    distances.sort(key= lambda t : t[1])
    print(distances)





m = [
    [5.1, 3.5, 1.4, 0.2],
    [4.9, 3.1, 1.1, 0.1],
    [5.7, 2.1, 0.8, 0.4],
    [4.1, 0.5, 1.1, 0.15],
]


getNeighbors(3,[5.7, 2.1, 0.8, 0.4], m)