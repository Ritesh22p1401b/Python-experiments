import numpy as np

# Define the filename
filename = 'data.csv'

# Use genfromtxt to load the dataset
# Set 'dtype=None' to automatically detect the data types
data = np.genfromtxt(filename, delimiter=',', dtype=None, encoding=None, names=True)

# Display the loaded dataset
print("Imported dataset:")
print(data)

# Accessing specific columns
names = data['Name']
ages = data['Age']
marks = data['Marks']

print("\nNames:", names)
print("Ages:", ages)
print("Marks:", marks)
