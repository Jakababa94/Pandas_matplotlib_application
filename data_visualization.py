import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset from csv file
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

#simulated time series of sepal and petal lengths
#Line Chart of Sepal and Petal Lengths Over Time
df['Day'] = range(1, len(df) + 1)

plt.figure(figsize=(10, 5))
plt.plot(df['Day'], df['sepal_length'], label='Sepal Length', color='blue')
plt.plot(df['Day'], df['petal_length'], label='Petal Length', color='green')

plt.title('Sepal and Petal Lengths Over Time')
plt.xlabel('Day')
plt.ylabel('Length (cm)')
plt.legend()
plt.grid(True)
plt.show()

# Bar Chart of Average Sepal Length by Species
plt.figure(figsize=(10, 5))
sns.barplot(x='species', y='sepal_length', data=df, palette='viridis')
plt.title('Average Sepal Length by Species')
plt.xlabel('Species')
plt.ylabel('Average Sepal Length (cm)')
plt.grid(True)
plt.show()

# Histogram of Sepal Length Distribution
plt.figure(figsize=(10, 5))
plt.hist(df['sepal_length'], bins=20, color='blue', alpha=0.7)
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Scatter Plot of Sepal Length vs. Petal Length
plt.figure(figsize=(10, 5))
plt.scatter(df['sepal_length'], df['petal_length'], c='blue', alpha=0.5)
plt.title('Sepal Length vs. Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.grid(True)
plt.show()