# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 12:43:29 2018

@author: Karan
"""

import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("deliveryfleet.csv")

iv = dataset.iloc[:,1:].values

from sklearn.cluster import KMeans

#part 1
kmeans = KMeans(n_clusters = 2, init = 'k-means++', random_state=0)
y_means = kmeans.fit_predict(iv)

plt.scatter(iv[y_means==0,0], iv[y_means==0,1], s=100, c='red', label='Rural Drivers')
plt.scatter(iv[y_means==1,0], iv[y_means==1,1], s=100, c='blue', label='Urban Drivers')

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='yellow', label='Centroid')
plt.title('Cluster of Drivers')
plt.xlabel('Distance Feature')
plt.ylabel('Speeding Feature')
plt.legend()
plt.show()

#part 2
kmeans = KMeans(n_clusters = 4, init = 'k-means++', random_state=0)
y_means = kmeans.fit_predict(iv)

plt.scatter(iv[y_means==0,0], iv[y_means==0,1], s=100, c='red', label='Rural Drivers FSL')
plt.scatter(iv[y_means==1,0], iv[y_means==1,1], s=100, c='blue', label='Urban Drivers FSL')
plt.scatter(iv[y_means==2,0], iv[y_means==2,1], s=100, c='green', label='Urban Drivers UFSL')
plt.scatter(iv[y_means==3,0], iv[y_means==3,1], s=100, c='cyan', label='Rural Drivers UFSL')

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='yellow', label='Centroid')
plt.title('Cluster of Drivers')
plt.xlabel('Distance Feature')
plt.ylabel('Speeding Feature')
plt.legend()
plt.show()