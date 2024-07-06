import pandas as pd

df = pd.read_csv('../data/processed/first_clean.csv')

print(df.to_string())

df.sort_values(by=['species_name', 'year', 'habitat_region'], inplace=True)

print(df.to_string())

df.drop(columns=['year', 'species_id', 'health_status'], axis=1, inplace=True)

print(df.to_string())

df.to_parquet()

df = df.groupby(['species_name', 'habitat_region', 'diet'], group_keys=True).mean(numeric_only=True).reset_index(inplace=True)

print(df.to_string())

df.to_csv('../data/processed/primates_dataset.csv', index=False)