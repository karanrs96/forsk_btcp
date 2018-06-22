# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 13:24:27 2018

@author: Karan
"""

import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("tshirts.csv")

iv = dataset.iloc[:,1:].values

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state=0)
y_means = kmeans.fit_predict(iv)

plt.scatter(iv[y_means==0,0], iv[y_means==0,1], s=100, c='red', label='Medium')
plt.scatter(iv[y_means==1,0], iv[y_means==1,1], s=100, c='blue', label='Large')
plt.scatter(iv[y_means==2,0], iv[y_means==2,1], s=100, c='green', label='Small')

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='yellow', label='Centroid')
plt.title('Cluster of T-Shirts')
plt.xlabel('Height (inches)')
plt.ylabel('Weight (pounds)')
plt.legend()
plt.show()
