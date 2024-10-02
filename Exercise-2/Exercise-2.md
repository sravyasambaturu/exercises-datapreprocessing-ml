### Coding Exercise 2: Handling Missing Data in a Dataset for Machine Learning

In this exercise, we will learn how to handle missing data in a dataset using Python and the `SimpleImputer` class from scikit-learn.

#### Instructions:

1. **Import the necessary Python libraries**:  
   For data preprocessing, you need the `pandas` and `numpy` libraries, as well as `SimpleImputer` from `sklearn.impute`.

2. **Load the dataset**:  
   The dataset name is `'pima-indians-diabetes.csv'`. Load it into a pandas DataFrame using the `read_csv` function from pandas.

3. **Identify missing data**:  
   Identify missing data in the DataFrame using pandas methods such as `isnull` and `sum`. Print out the number of missing entries in each column.

4. **Handle missing data**:  
   Replace missing data with the mean value of the respective columns. This is done by configuring an instance of the `SimpleImputer` class.

5. **Fit the imputer**:  
   Fit the imputer to the DataFrame's numerical columns to calculate the mean value of each column.

6. **Transform the data**:  
   Use the `transform` method to replace missing values with the calculated mean values.

7. **Update the matrix of features**:  
   Assign the result of the `transform` method to the appropriate columns of the DataFrame.

8. **Print the updated matrix**:  
   Verify the changes by printing the updated matrix of features.

Hint 1: To load the Pima Indians Diabetes Database dataset into a pandas DataFrame, use the pd.read_csv function. The dataset name is 'pima-indians-diabetes.csv'.

Hint 2: Missing data in the DataFrame can be identified using pandas methods like isnull and sum. Consider using df.isnull().sum() to get the number of missing values in each column.

Hint 3: The SimpleImputer class from sklearn.impute is handy in handling missing data. You can configure an instance of this class with a strategy to replace missing values. For example, to replace missing values with the mean, use imputer = SimpleImputer(missing_values=np.nan, strategy='mean').

Hint 4: After configuring the SimpleImputer, fit it on your DataFrame. Use imputer.fit(df) to fit imputer to the DataFrame.

Hint 5: The transform method of the SimpleImputer class is used to replace missing data. You can apply it on the DataFrame like so: df_imputed = imputer.transform(df).
