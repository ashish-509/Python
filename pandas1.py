import pandas as pd # importing pandas

df1 = pd.read_csv('csvFile.csv') # Read csv file into dataframe.

print(df1)
print(pd)


# A Series is a one-dimensional labeled array in Pandas. Creating a series from a list :
data = [10, 20, 30, 40, 50]
series = pd.Series(data)
print(series)
print(series[2])        # access element with label 2 (output is : 30)
print(series.iloc[3])   # access element at position 3 (output is : 40)
print(series[1:4])      # access a range of elements 


# A DataFrame is a two-dimensional labeled data structure with columns of potentially different data types

data2 = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data2)
print(df)
print(df.iloc[2])   # Access the third row by position
print(df.loc[1])    # Access the second row by label


print('\n\n This is braker for clear console... \n\n')
unique_dates = df['Age'].unique()
print(unique_dates)


df.to_csv('trading_data.csv', index=False) # saving dataFrames to csv file.