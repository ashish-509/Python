# Given a CSV dataset:
    # handle missing values
    # filter rows based on condition
    # compute mean, median



import pandas as pd

# Load the dataset
df = pd.read_csv('dataset.csv')

# Handle missing values (e.g., fill with mean)
df.fillna(df.mean(), inplace=True)

# Filter rows based on a condition (e.g., column 'A' > 10)
filtered_df = df[df['A'] > 10]

# Compute mean and median for a specific column (e.g., column 'B')
mean_value = df['B'].mean()
median_value = df['B'].median()

print("Mean of column B:", mean_value)
print("Median of column B:", median_value)