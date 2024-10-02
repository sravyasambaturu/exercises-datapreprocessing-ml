# Step 1: Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# Step 2: Load the Iris dataset
dataset = pd.read_csv('iris.csv')

# Step 3: Identify features and the dependent variable
# Features are in all columns except the last one
# Dependent variable (species) is in the last column
X = dataset.iloc[:, :-1].values  # Extract features as numpy array
y = dataset.iloc[:, -1].values   # Extract dependent variable as numpy array

# Step 4: Print X and y to verify their creation
print("Matrix of Features (X):")
print(X)
print("\nDependent Variable Vector (y):")
print(y)
