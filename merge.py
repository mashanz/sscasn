import pandas as pd

# Load the first CSV file
df1 = pd.read_csv('output1.csv')
df2 = pd.read_csv('output2.csv')
df3 = pd.read_csv('output3.csv')
df4 = pd.read_csv('output4.csv')
df5 = pd.read_csv('output5.csv')
df6 = pd.read_csv('output6.csv')
df7 = pd.read_csv('output7.csv')

# Merge the two DataFrames using pd.concat
merged_df = pd.concat([df1, df2, df3, df4, df5, df6, df7])

# Save the merged DataFrame to a new CSV file
merged_df.to_csv('merged.csv', index=False)