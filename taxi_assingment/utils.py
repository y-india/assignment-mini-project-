import pandas as pd

def load_data(path):
    return pd.read_parquet(path)

def get_missing_values(df):
    return df.isnull().sum()

def print_5(df):
    print(df.head(5))
    