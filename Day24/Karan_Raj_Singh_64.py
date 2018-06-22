# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 12:00:28 2018

@author: Karan
"""

from sklearn.datasets import load_iris
iris = load_iris()
iris=iris.data

from sklearn.decomposition import PCA
pca = PCA(n_components=2)
iris = pca.fit_transform(iris)

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3, init='k-means++', random_state=0)
y_means = kmeans.fit_predict(iris)

import matplotlib.pyplot as plt

plt.scatter(iris[y_means==0,0], iris[y_means==0,1], s=100, c='red', label='Setosa')
plt.scatter(iris[y_means==1,0], iris[y_means==1,1], s=100, c='blue', label='Virginica')
plt.scatter(iris[y_means==2,0], iris[y_means==2,1], s=100, c='green', label='Versicolor')
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s=300, c='yellow',label='Centroids')
plt.title('Cluster of Iris')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.show()