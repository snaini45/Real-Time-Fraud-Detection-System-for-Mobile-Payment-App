
import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv('creditcard_2023.csv')

# Handle missing values
df = df.dropna()

# Feature scaling from amount
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df['scaled_amount'] = scaler.fit_transform(df[['Amount']])
df.drop(['Amount'], axis=1, inplace=True)

# Save preprocessed data
df.to_csv('preprocessed_creditcard.csv', index=False)
print("Data preprocessing completed.")
