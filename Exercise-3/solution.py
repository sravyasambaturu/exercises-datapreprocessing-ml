# Step 1: Importing the necessary libraries
import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

# Step 2: Load the Titanic dataset
df = pd.read_csv('titanic.csv')

# Step 3: Identify categorical features
categorical_features = ['Sex', 'Embarked', 'Pclass']

# Step 4: Implement an instance of the ColumnTransformer class
ct = ColumnTransformer(
    transformers=[
        ('encoder', OneHotEncoder(), categorical_features)
    ], remainder='passthrough')

# Step 5: Apply the fit_transform method on the ColumnTransformer
X = ct.fit_transform(df)

# Step 6: Convert the output into a NumPy array
X = np.array(X)

# Step 7: Use LabelEncoder to encode the 'Survived' column
le = LabelEncoder()
y = le.fit_transform(df['Survived'])

# Step 8: Print the updated matrix of features and the dependent variable
print("Updated matrix of features: \n", X)
print("Updated dependent variable vector: \n", y)
