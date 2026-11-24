import pandas as pd

df = pd.read_csv(
    "data/Sample - Superstore.csv",
    encoding="latin1"
)

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")

for i, col in enumerate(df.columns, start=1):
    print(f"{i}. {col}")
