# Task 1: Load and Explore the Dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# Display first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Check data types and missing values
print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

# Clean the dataset 
df.fillna(df.mean(numeric_only=True), inplace=True)

# Task 2: Basic Data Analysis
print("\nStatistical Summary:")
print(df.describe())

# Group by species and compute mean of numerical columns
grouped = df.groupby('species').mean()
print("\nMean values grouped by species:")
print(grouped)

# Task 3: Data Visualization
sns.set(style="whitegrid")

# 1. Line Chart (simulated time-series using index)
plt.figure(figsize=(10, 4))
plt.plot(df.index, df['sepal length (cm)'], label='Sepal Length', color='blue')
plt.title('Sepal Length Over Sample Index')
plt.xlabel('Sample Index')
plt.ylabel('Sepal Length (cm)')
plt.legend()
plt.tight_layout()
plt.show()

# 2. Bar Chart: Average Petal Length per Species
plt.figure(figsize=(8, 4))
sns.barplot(x='species', y='petal length (cm)', data=df, palette='viridis')
plt.title('Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Petal Length (cm)')
plt.tight_layout()
plt.show()

# 3. Histogram: Distribution of Sepal Width
plt.figure(figsize=(8, 4))
sns.histplot(df['sepal width (cm)'], bins=20, kde=True, color='orange')
plt.title('Distribution of Sepal Width')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# 4. Scatter Plot: Sepal Length vs Petal Length
plt.figure(figsize=(8, 4))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df, palette='deep')
plt.title('Sepal Length vs Petal Length by Species')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.tight_layout()
plt.show()

#Error handling example for CSV loading
try:
    custom_df = pd.read_csv('your_dataset.csv')
except FileNotFoundError:
    print("Error: CSV file not found.")
except pd.errors.ParserError:
    print("Error: Could not parse the CSV file.")
except Exception as e:
    print(f"Unexpected error: {e}")