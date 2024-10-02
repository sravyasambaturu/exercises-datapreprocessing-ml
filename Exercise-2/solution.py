# Step 1: Import the necessary libraries
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

# Step 2: Load the dataset
df = pd.read_csv('pima-indians-diabetes.csv')

# Step 3: Identify missing data
missing_data = df.isnull().sum()

# Step 4: Print the number of missing entries in each column
print("Missing data: \n", missing_data)

# Step 5: Configure an instance of the SimpleImputer class
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

# Step 6: Fit the imputer on the DataFrame
imputer.fit(df)

# Step 7: Apply the transform to the DataFrame
df_imputed = imputer.transform(df)

# Step 8: Print the updated matrix of features
print("Updated matrix of features: \n", df_imputed)
