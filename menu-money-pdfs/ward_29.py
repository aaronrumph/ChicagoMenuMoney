import pandas as pd

menu_csv = "AllMenu2012-2025.csv"
df = pd.read_csv(menu_csv)

for i in range(1, 51):
    ward_df = df[df["ward"] == i]
    df.to_csv(f"ward_{i}.csv")
