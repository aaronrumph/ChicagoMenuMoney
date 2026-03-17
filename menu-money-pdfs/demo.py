import pandas as pd

df = pd.read_csv("AllMenu2012-2025.csv")

for col in df.columns:
    print(df[col].unique())
