### Coding Exercise 1: Importing and Preprocessing a Dataset for Machine Learning

In this exercise, we will explore data preprocessing with Python using the popular Iris dataset.

#### Instructions:

1. **Import the necessary Python libraries**:  
   You will need the `pandas` library for loading and manipulating data. Also, import `numpy` and `train_test_split` from `sklearn.model_selection`.

2. **Load the Iris dataset**:  
   The Iris dataset is stored in a CSV file named `'iris.csv'`. Use the `pandas` function `read_csv()` to load this file and store it in a DataFrame. Assign the DataFrame to a variable named `dataset`.

3. **Identify the features and the dependent variable**:  
   - The features (independent variables) in the Iris dataset are the lengths and widths of the petals and sepals.
   - The dependent variable is the species of the Iris.
   - The features are stored in all columns except the last one in your DataFrame.
   - The dependent variable is stored in the last column.

4. **Create the matrix of features (X) and the dependent variable vector (y)**:  
   - Use the `iloc` indexer in pandas to select these subsets of the data and store them in variables `X` and `y`, respectively.
   - You should use the `.values` attribute to extract the data as numpy arrays.

5. **Print X and y**:  
   Finally, print the matrix of features (`X`) and the dependent variable vector (`y`) to verify their creation. You can use the `print()` function for this.

Hint 1: Use import pandas as pd to import the pandas library, which provides the read_csv function for loading the Iris dataset.

Hint 2: The read_csv function from pandas is used to read a CSV file into a DataFrame. Use it like this: pd.read_csv('filename.csv').

Hint 3: A matrix of features (X) and the dependent variable vector (y) can be created from a dataset like this: X = dataset.iloc[:, :-1].values and y = dataset.iloc[:, -1].values. This uses the iloc indexer to select all rows and all columns except the last one for X, and all rows of the last column for y.

Hint 4: Remember to print your matrix of features (X) and dependent variable vector (y) to verify their creation. You can simply use the print function for this.

