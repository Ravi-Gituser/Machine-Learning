# LINEAR REGRESSION ALGORITHM

#Import required Libraries

# For mathematical calculations
import numpy as np

# For handling datasets
import pandas as pd

# For plotting graphs
from matplotlib import pyplot as plt

#Import the sklearn library for linear regression
from sklearn.linear_model import LinearRegression


# Import dataset

#Import the csv file
df = pd.read_csv('data.csv'.delim_whitespace=True)

#prints the top 5 rows
print df.head()


# Prepare data for training

# Prepare the training set
x_train = df['Father'].values[:,np.newaxis]
y_train = df['Son'].values


# Train the model

lm = LinearRegression()
lm.fit(x_train,y_train)


# Test the model

# Prepare the test data
x_test = [[72.8],[61.1],[67.4],[70.2],[75.6],[60.2],[65.3],[59.2]]

# Test the model

predictions = lm.predict(x_test)
print predictions


# Plot the best fit line

#Plot the training data
plt.scatter(x_train,y_train,color='b')

# Plot the best fit line using predicted value
plt.plot(x_test,predictions,color='black',linewidth=3)
plt.xlabel('Father height in inches')
plt.ylabel('Son height in inches')
plt.show()

