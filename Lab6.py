import pandas as pd

# Read the CSV file
# Replace 'data.csv' with your actual file name
df = pd.read_csv('C:/Users/Deekshith/Downloads/experience.csv')

# 1. Display the content of the file
print("Full DataFrame:")
print(df)

# 2. Find the total number of rows and columns
rows, columns = df.shape
print("\nNumber of rows:", rows)
print("Number of columns:", columns)

# 3. Calculate the length of the dataframe
print("\nLength of DataFrame:", len(df))

# 4. Display the first 2 rows only
print("\nFirst 2 rows:")
print(df.head(2))
