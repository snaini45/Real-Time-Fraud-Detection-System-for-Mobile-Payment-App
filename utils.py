
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def scale_amount(df):
    scaler = StandardScaler()
    df['scaled_amount'] = scaler.fit_transform(df[['Amount']])
    df.drop(['Amount'], axis=1, inplace=True)
    return df
