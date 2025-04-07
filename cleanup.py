import pandas as pd
import numpy as np

# Example DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', None],
    'Age': ['25', 'Thirty', '35', '40', '45'],
    'Salary': ['50000.50', '60000', 'Not Disclosed', None, '75000'],
    'Join_Date': ['2022-01-01', 'Invalid Date', '2020-07-15', '2021-03-12', '2023-05-10']
}

df = pd.DataFrame(data)

# Display original DataFrame
print("Original DataFrame:")
print(df)

# Data Cleanup
# 1. Handle missing values
df['Name'] = df['Name'].fillna('Test')  # Replace missing values in 'Name'
df['Salary'] = df['Salary'].fillna('0')  # Replace missing values in 'Salary'

# 2. Convert columns to correct data types
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')  # Convert 'Age' to numeric
df['Salary'] = pd.to_numeric(df['Salary'].str.replace('Not Disclosed', '0'), errors='coerce')  # Clean and convert 'Salary'
df['Join_Date'] = pd.to_datetime(df['Join_Date'], errors='coerce')  # Convert 'Join_Date' to datetime

# 3. Replace certain values
df['Age'] = df['Age'].fillna(df['Age'].mean())  # Replace NaN in 'Age' with the mean
df['Salary'] = df['Salary'].replace(0, np.nan)  # Replace 0 in 'Salary' with NaN

# Display cleaned DataFrame
print("\nCleaned DataFrame:")
print(df)
