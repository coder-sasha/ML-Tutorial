"""
This script demonstrates some useful usage of pandas DataFrame
"""
import pandas as pd

print(f"Work with Pandas Dataframes")
df = pd.DataFrame({
    "Col1": [1, 4, 8, 7, 9],
    "Col2": ['A', 'Column', 'With', 'A', 'String'],
    "Col3": [1.23, 23.5, 45.6, 32.1234, 89.453],
    "Col4": [True, False, True, False, True]
})

print(f"\n=== Simple dataframe")
print(df.head())

# using Python special variable _
print(f"\n=== using Python special variable: '_'")
df = pd.DataFrame([[1, -1, 13], [3, -3, 21], [5, -5, 42], [7, -7, 64]], columns=["Pos", "Neg", "col42"])
print(f"The whole dataframe:\n {df}\n\nThe column 'col42:'")
for _, row in df.iterrows():
    print(row["col42"])

# read dataset muesli75 into dataframe - 75 records describing different brands of this product
print(f"\n\n=== work with muesli")
df_msl = pd.read_csv('muesli75.csv')
print(df_msl.head(10))

print(f"\n=== the list of all columns names")
columns = df_msl.columns.to_list()
print(columns)

# select rows
print(f"\n=== select rows with name containing 'Raisins'")
raisin = df_msl['names'].str.contains('Raisins', case=False, na=False)
print(df_msl[raisin])
print(f"\n=== select rows with calories between 150 and 250")
clrs = (df_msl['calories'] > 150) & (df_msl['calories'] < 250)
print(df_msl[clrs])

# grouping dataframe
print(f"\n=== grouping in dataframe")
group = df_msl.groupby('mfr').get_group('P')
print(group)

# drawing some charts
import matplotlib.pyplot as plt

print(f"\n=== draw histogram from the dataframe 'group'")
group.plot(kind='bar', x='names', rot=45)
plt.show()
