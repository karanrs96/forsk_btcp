# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 10:15:42 2018

@author: Karan
"""

import pandas as pd

dataset = pd.read_csv("crime_data.csv")

iv = dataset.iloc[:, [1,2,4]].values

from sklearn.decomposition import PCA
pca = PCA(n_components=2)
iv = pca.fit_transform(iv)
#explained_variance = pca.explained_variance_ratio_

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3, init='k-means++', random_state=0)
y_means = kmeans.fit_predict(iv)

import matplotlib.pyplot as plt

plt.scatter(iv[y_means==0,0], iv[y_means==0,1], s=100, c='red',label='Murder')
plt.scatter(iv[y_means==1,0], iv[y_means==1,1], s=100, c='blue',label='Assault')
plt.scatter(iv[y_means==2,0], iv[y_means==2,1], s=100, c='green',label='Rape')
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s=300, c='yellow',label='Centroids')
plt.title('Cluster of Crimes')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.show()