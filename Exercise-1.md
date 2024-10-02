Coding Exercise 1: Importing and Preprocessing a Dataset for Machine Learning
In this exercise, you will explore data preprocessing with Python.

Instructions:

Import the necessary Python libraries: You will need the pandas library for this exercise. Also import numpy and train_test_split from sklearn.model_selection.

Load the Iris dataset: The Iris dataset is stored in a CSV file named 'iris.csv'. Use the pandas function read_csv to load this file and store it in a DataFrame. Assign the DataFrame to a variable named dataset.

Identify the features and the dependent variable: The features (independent variables) in the Iris dataset are the lengths and widths of the petals and sepals, and the dependent variable is the species of the Iris. The features are stored in all columns except the last one in your DataFrame, and the dependent variable is stored in the last column.

Create the matrix of features (X) and the dependent variable vector (y): Use the iloc indexer in pandas to select these subsets of the data and store them in variables X and y respectively. You should use the .values attribute to extract the data as numpy arrays.

Print X and y: Finally, print the matrix of features (X) and the dependent variable vector (y) to verify their creation. You can use the print function for this.

Hint 1: Use import pandas as pd to import the pandas library, which provides the read_csv function for loading the Iris dataset.

Hint 2: The read_csv function from pandas is used to read a CSV file into a DataFrame. Use it like this: pd.read_csv('filename.csv').

Hint 3: A matrix of features (X) and the dependent variable vector (y) can be created from a dataset like this: X = dataset.iloc[:, :-1].values and y = dataset.iloc[:, -1].values. This uses the iloc indexer to select all rows and all columns except the last one for X, and all rows of the last column for y.

Hint 4: Remember to print your matrix of features (X) and dependent variable vector (y) to verify their creation. You can simply use the print function for this.

1. Import necessary libraries: We first import the necessary libraries for this exercise. pandas is a library providing high-performance, easy-to-use data structures and data analysis tools. numpy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays. The train_test_split function from sklearn.model_selection is used to split the dataset into training and test sets.

# Importing the necessary libraries
import numpy as np
import pandas as pd
fromsklearn.model_selection import train_test_split
2. Load the dataset: We use the read_csv function from pandas to load the Iris dataset from a CSV file. The loaded dataset is a DataFrame object which is a two-dimensional size-mutable, potentially heterogeneous tabular data structure with labeled axes (rows and columns).

# Loading the Iris dataset dataset = pd.read_csv('iris.csv')
3. Create the matrix of features and dependent variable vector: We extract the matrix of features (X) and dependent variable vector (y) from the DataFrame. The iloc indexer is used to select all rows and all columns except the last one for X, and all rows of the last column for y. The .values attribute is used to extract the data as numpy arrays.

# Creating the matrix of features (X) and the dependent variable vector (y) X = dataset.iloc[:, :-1].values y = dataset.iloc[:, -1].values
4. Print X and y: Finally, we print out the matrix of features and dependent variable vector to verify their creation.

# Printing the matrix of features and the dependent variable vector
print(X)
print(y)
