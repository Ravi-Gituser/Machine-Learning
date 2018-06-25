# K-MEANS CLUSTERING


# Import required libraries

# For mathematical calculations
import numpy as np

# For handling datasets
import pandas pd

#For plotting graphs
from matplotlib import pyplot as plt

#Import the sklearn library for KMeans clustering
from sklearn.cluster import KMeans


#Import dataset

# Import the csv file
df = pd.read_csv('data.csv')

print df.head()


# Train the model

# Assign the number of clusters
k=2

kmeans = KMeans(n_clusters=k)

# Train the model
kmeans = kmeans.fit(df)

# array that contains cluster number
labels = means.labels_

#array of size k with co-ordinates of centroids
centroids = kmeans.cluster_centers_


# Test the model

# Prepare the test data
x_test = [[4671.67],[2.885,61],[1.666,90],[5.623,54],[2.678,80],[1.875,60]]

# Test the model (return the cluster number)
prediction = kmeans.predict(x_test)

print prediction


# Plot the clusters

# Plot the points representing their cluster number
colors = ['blue','red','green','black']
y = 0
for x in labels:
                 # Plot the points according to their clusters and assign different colors.
				 plt.scatter(df.iloc[y,0], df.iloc[y,1] , color=colors[x])
				 y+=1
				 
for x in range(k):
                  # Plot the centroids 
				  lines = plt.plot(centroids[x,0],centroids[x,1],'kx')
				  # Make the centroid larger
				  plt.setp(lines,ms=15.0)
				  plt.setp(lines,mew=2.0)
				  
title = ('No. of clusters (k) = {}').format(k)
plt.title(title)
plt.xlabel('eruptions(mins)')
plt.ylabel('waiting(mins)')
plt.show()