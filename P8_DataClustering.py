import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
from typing import Tuple, Dict, List
import numpy as np
from functools import reduce
from sklearn.cluster import KMeans

data = pd.read_csv('data/top10s_clean.csv', index_col=0)
data = pd.DataFrame(data, columns=['dance', 'popularity'])
kmeans = KMeans(n_clusters=4).fit(data)
centroids = kmeans.cluster_centers_
print(centroids)
plt.scatter(data['dance'], data['popularity'],
            c=kmeans.labels_.astype(float), s=50, alpha=0.5)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
plt.title("Popularidad con relacion al baile de la cancion")
plt.ylabel("Popularidad")
plt.xlabel("Baile")
plt.show()
plt.savefig("img/P8_clustering")
plt.close()

print(data)
