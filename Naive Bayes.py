# NAIVE BAYES

# Given the details of patient we nee t predict whether the patient survived or not.

# Import the required libraries

# For mathematical calculations
import numpy as np

# For handling datasets
import pandas as pd

# For plotting graphs
from matplotlib import pyplot as plt

# Import sklearn library for Naive Bayes
from sklearn.naive_bayes import GaussianNB

# Import dataset

# Import the csv file
df = pd.read_csv('data.csv')

print df.head()

# Lot the classes against features

# We plot the data to see dependency of any feature on the class
plt.xlabel('Feature')
plt.ylabel('Survived')

X = df.loc[:,'Age']
Y = df.loc[:,'Survived']
plt.scatter(X,Y,color='blue' ,label='Age')

X = df.loc[:,'Year']
Y = df.loc[:,'Survived']
plt.scatter(X,Y,color='green' ,label='Year')

X = df.loc[:,'Nodes']
Y = df.loc[:,'Survived']
plt.scatter(X,Y,color='red' ,label='Nodes')

plt.legend(loc = 4,prop={'size':7})
plt.show()


# Prepare data for training

#Prepare the training set
x = df.loc[:,'Age':'Nodes']
y = df.loc[:,'Survived']

# Train the model

clf = GaussianNB()

clt.fit(X,Y)

# Test the model

# Testing the model(Returns the class)
prediction = clf.predict([[12,70,12],[13,20,13]])
print prediction