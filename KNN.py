# K-nearest neighbors


class Point:
    def __init__(self, x, y) -> None:
        self.x_axis = x
        self.y_axis = y

    def getDistance(self, point):
        import math

        distance = math.sqrt(
            math.pow(point.y_axis - self.y_axis, 2)
            + math.pow(point.x_axis - self.x_axis, 2)
        )
        return distance


p1 = Point(2, 4)
p2 = Point(3, 7)


m = [
    [5.1, 3.5, 1.4, 0.2],
    [4.9, 3.1, 1.1, 0.1],
    [5.7, 2.1, 0.8, 0.4],
    [4.1, 0.5, 1.1, 0.15],
]


def dataNorm(matrix: list):
    # formula = point in range / range == (x - xMin)/(xMax - xMin)
    m = []
    for i in range(len(matrix[0])):
        turnCol = [row[i] for row in matrix]
        m.append(turnCol)

    return m


def getMinMaxVals(dataset: list):
    m = []

    for el in dataset:
        mContainer = list()
        minVal = min(el)
        maxVal = max(el)
        mContainer.append(minVal)
        mContainer.append(maxVal)
        m.append(mContainer)

    return m


newM = dataNorm(m)
print(getMinMaxVals(newM))
