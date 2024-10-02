### Coding Exercise 3: Encoding Categorical Data for Machine Learning

In this exercise, we will explore how to encode categorical data using `OneHotEncoder` and `LabelEncoder` in Python.

#### Instructions:

1. **Import the necessary libraries**:  
   We will use `pandas` for data manipulation, `numpy` for numerical operations, and the required classes from scikit-learn for encoding categorical data.

2. **Load the Titanic dataset**:  
   The Titanic dataset is loaded into a pandas DataFrame using the `read_csv` function. The dataset name is `'titanic.csv'`.

3. **Identify categorical features**:  
   Identify the categorical features in the dataset that need to be encoded. In this case, the features are `'Sex'`, `'Embarked'`, and `'Pclass'`.

4. **Apply OneHotEncoding**:  
   Create an instance of the `ColumnTransformer` class and pass the `OneHotEncoder()` along with the list of categorical features.

5. **Fit and transform the data**:  
   Use the `fit_transform()` method on the `ColumnTransformer` instance to apply OneHotEncoding to the categorical features.

6. **Convert the output into a NumPy array**:  
   The result of the `fit_transform()` is a sparse matrix. Convert it into a dense NumPy array for further use.

7. **Encode the dependent variable**:  
   The 'Survived' column is the dependent variable (binary categorical) and will be encoded using `LabelEncoder`.

8. **Print the updated matrix of features and the dependent variable**:  
   Verify the transformation by printing both the matrix of features and the dependent variable.

Hint 1: Use pd.read_csv('titanic.csv') to load the Titanic dataset. Dataset name is 'titanic.csv'.

Hint 2: Identify the categorical features in your dataset using categorical_features = ['Sex', 'Embarked', 'Pclass'].

Hint 3: Create an instance of the ColumnTransformer class using

pythonCopy code
ct = ColumnTransformer( transformers=[ ('encoder', OneHotEncoder(), categorical_features) ], remainder='passthrough' )
Hint 4: Fit and transform the categorical features using X = ct.fit_transform(df).

Hint 5: Convert the output into a NumPy array using X = np.array(X).

Hint 6: Encode the dependent variable using

pythonCopy code
le = LabelEncoder() y = le.fit_transform(df['Survived'])variable using
Hint 7: Print the updated matrix of features and the dependent variable vector
