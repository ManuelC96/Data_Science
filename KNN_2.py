#sitePackages  
import numpy as np
from matplotlib import pyplot as plt
from collections import Counter

# K nearest neighbors algorithm
points = {
    "blue":[[2,4,5],[1,3,3],[2,3,1],[3,2,2],[2,1,4]],
    "red":[[5,6,5],[4,5,4],[4,6,1],[6,6,6],[5,4,7]]

}

newPoint = [7,3,4] 



class KNN():
    # initializer
    def __init__(self, dataSet, k = 3, ) -> None:
        self.k = k
        self.point = dataSet

    def predict(self, newPoint):
        distances = []

        for category in self.point:
            for point in self.point[category]:
                distance = self.euclidianDistance(point, newPoint)
                distances.append([distance, category])


        categories = [ category[1] for category in sorted(distances, key= lambda e: e[0])[:self.k] ]
        result = Counter(categories).most_common(1)[0][0]
        return result

    def euclidianDistance(self,p: list, q: list):

        distances = np.sqrt(np.sum((np.array(p) - np.array(q))**2))
        return distances


clf = KNN(points)
newClass = clf.predict(newPoint)
color = "#FF0000" if newClass == "red" else "#104DCA"


# visulize

fig = plt.figure(figsize=(15, 12))
axes = fig.add_subplot(projection="3d")
axes.set_facecolor(color="black")
axes.grid(True, color="#323232")
axes.figure.set_facecolor("#121212")
axes.tick_params(axis="x", color="white")
axes.tick_params(axis="y", color="white")

for point in points["blue"]:
    axes.scatter(point[0], point[1], point[2], color="#104DCA", s=60)

for point in points["red"]:
    axes.scatter(point[0], point[1], point[2],color="#FF0000", s=60)

axes.scatter(newPoint[0], newPoint[1], newPoint[2],color=color, marker="*", s=200, zorder=100 )

for point in points["blue"]:
    axes.plot([point[0], newPoint[0] ], [point[1], newPoint[1]], [point[2], newPoint[2]], color="#104DCA", linestyle="--", linewidth=1 )

for point in points["red"]:
    axes.plot([point[0], newPoint[0] ], [point[1], newPoint[1]], [point[2], newPoint[2]], color="#FF0000", linestyle="--", linewidth=1 )

plt.show()