import numpy as np

# Create a sample 2D NumPy array

array = np.array([[10, 20, 30],[40, 50, 60],[70, 80, 90]])


print(f"Original array:{array}")   # Display the original array


col1, col2 = 0, 1  # Define the columns to swap (0-indexed)

array[:, [col1, col2]] = array[:, [col2, col1]] # Swap the columns


# Display the modified array
print(f"Array after swapping columns {col1} and {col2}:")
print(array)
