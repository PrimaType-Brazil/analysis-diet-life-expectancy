import pandas as pd

df = pd.read_csv('../data/raw/primates_dataset.csv')
print(df.to_string())

df.dropna(inplace=True)
df.drop(columns=['social_behavior', 'genetic_variation', 'latitude', 'longitude'], axis=1, inplace=True)

print(df.to_string())

df.to_csv('../data/processed/first_clean.csv', index=False)