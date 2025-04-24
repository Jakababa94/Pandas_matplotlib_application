import pandas as pd

# Load dataset from csv file
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
print(df.head())

# data types and missing values
print(df.info())
print(df.isnull().sum())

# Clean the dataset by either filling or dropping any missing values.
# In this case, there are no missing values, so we don't need to do anything.

# Basic statistics of the dataset with numerical colums
print(df.describe())

# Grouping a category column and getting the mean of the numerical columns
print(df.groupby('species').mean())

# compare mean petal length of each species
print(df.groupby('species')['petal_length'].mean())
# compare mean petal width of each species
print(df.groupby('species')['petal_width'].mean())