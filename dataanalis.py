import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Data Acquisition
# For this example, let's assume you have a CSV file named 'sales_data.csv' with columns: 'Date', 'Sales'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('sales_data.csv')

# Step 2: Data Analysis
# Let's do some basic analysis on the sales data

# Display the first few rows of the DataFrame
print("First few rows of the dataset:")
print(df.head())

# Summary statistics of the numeric columns
print("\nSummary statistics of the dataset:")
print(df.describe())

# Step 3: Data Visualization
# Let's visualize the sales data

# Plotting sales over time
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Sales'], marker='o', linestyle='-')
plt.title('Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Step 4: Further Analysis
# You can perform further analysis as per your requirement, such as calculating monthly or yearly sales, finding trends, etc.
# For example, let's calculate monthly sales

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Extract month and year from 'Date' column
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year

# Group by month and calculate total sales
monthly_sales = df.groupby(['Year', 'Month'])['Sales'].sum()

# Plotting monthly sales
plt.figure(figsize=(10, 6))
monthly_sales.plot(kind='bar')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()
