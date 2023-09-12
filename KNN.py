# K-nearest neighbors




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







class KNNClssifier():
    def __init__(self, k = 5, p = 2, x = [] , y = []):
        self.k = k
        self.p = p
        self.x = list(x)
        self.y = list(y)
        self.xNorm = self.normMatrix(x)

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
        
    def minkowskiDistance(self, v1, v2):
        dim = len(v1)
        distance = 0

        for d in range(dim):
            distance += abs(v1[d] - v2[d]) ** self.p
            

        distance = distance ** (1 / self.p)
        return distance
    
    def getNeighbors(self, testRow):
        distances = []
        for i in range(len(self.xNorm)):
            row = self.xNorm[i]
            dist = minkowskiDistance(row, testRow)
            distances.append(
                (i, dist),
            )
        
        distances.sort(key= lambda t : t[1])
        kNeighbors = []
        for i in range(self.k):
            kNeighbors.append(distances[i][0])
        return kNeighbors
    
    def classFromNeighbors(self, distances : list):
        d = {}
        for i in distances:
            y = self.y[i]
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
    
    def predict(self, row, appenToDataSet = True):
        neighbors = self.getNeighbors(row)
        prediction = self.classFromNeighbors(neighbors)
        if appenToDataSet:
            self.x.append(row)
            self.y.append(prediction)
            self.xNorm = self.normMatrix(self.x)

        return prediction

    def evaluate(self, dataSet, classes):
        predictions = list()
        for row in dataSet:
            d = self.x[:]
            d.append(row)
            n = self.normMatrix(d)
            nRow = n[-1]
            predictions.append(self.predict(nRow, appenToDataSet=False))
        
        correct = 0

        for i in range(len(predictions)):
            pred = predictions[i]
            if pred == classes[i]:
                correct += 1
        return correct / len(classes)



import csv

columns = []
pokemonDataset = []

with open("Pokemon.csv") as f:
    reader = csv.reader(f)
    columns = next(reader)
    for row in reader:
        pokemonDataset.append(row)



inputColums = columns[5:11]
inputFeature = [[int(col) for col in row[5:11]] for row in pokemonDataset]
ouputLabels =  [0 if row[-1] == "False" else 1 for row in pokemonDataset]

print(inputFeature)


from sklearn.model_selection import train_test_split

xTrain, xTest, yTrain, yTest = train_test_split(

    inputFeature,
    ouputLabels,
    test_size= 0.3,
    random_state=42,
    stratify=ouputLabels

)


# print(xTrain)
print(yTrain)


legendaryClassifier