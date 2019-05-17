import numpy as np
import random
from sklearn.neighbors import NearestNeighbors


def match_features(features1, features2):
    matches = []
    confidences = []
    knn = NearestNeighbors(3)
    knn.fit(features1)

    dist, ind = knn.kneighbors(features2, 2)

    for i in range(len(ind)):
        index = ind[i]
        distances = dist[i]

        if distances[0] / distances[1] < 0.95:
            matches.append([index[0], i])
            confidences.append(1 - distances[0])

    return matches, confidences
