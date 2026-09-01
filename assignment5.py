"""
NumPy Practice Program
Covers Q1 to Q5
"""

import numpy as np
# Q.1 
print("=" * 60)
print("Q.1 - Basic Operations on 1D Array")
print("=" * 60)

arr1 = np.array([10, 20, 30, 40, 50])
print("Original array:", arr1)

add_result = arr1 + 2
print("a) After adding 2 to all elements:", add_result)

mul_result = arr1 * 3
print("b) After multiplying all elements by 3:", mul_result)

div_result = arr1 / 2
print("c) After dividing all elements by 2:", div_result)


# Q2
print("\n" + "=" * 60)
print("Q.2 - Reverse Array & Most Frequent Value")
print("=" * 60)

arr = np.array([1, 2, 3, 6, 4, 5])
reversed_arr = arr[::-1]
print("a) Original array:", arr)
print("   Reversed array:", reversed_arr)

def most_frequent_with_indices(a):
    values, counts = np.unique(a, return_counts=True)
    max_count = counts.max()
    most_frequent_values = values[counts == max_count]
    result = {}
    for val in most_frequent_values:
        indices = np.where(a == val)[0]
        result[val] = indices
    return result, max_count

print("\nb) Most Frequent Value(s) and their indices:")

# i.
x = np.array([1, 2, 3, 4, 5, 1, 2, 1, 1, 1])
res_x, count_x = most_frequent_with_indices(x)
print(f"   i. Array x = {x}")
for val, idx in res_x.items():
    print(f"      Most frequent value: {val} (count={count_x}), Indices: {idx}")

# ii.
y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3])
res_y, count_y = most_frequent_with_indices(y)
print(f"   ii. Array y = {y}")
for val, idx in res_y.items():
    print(f"      Most frequent value: {val} (count={count_y}), Indices: {idx}")


# Q3
print("\n" + "=" * 60)
print("Q.3 - 2D Array Row/Column Access")
print("=" * 60)

arr_2d = np.array([[10, 20, 30],
                    [40, 50, 60],
                    [70, 80, 90]])

print("2D Array:\n", arr_2d)

# a) 1st row, 2nd column  -> index [0, 1]
val_a = arr_2d[0, 1]
print("a) 1st row, 2nd column element:", val_a)

# b) 3rd row, 1st column -> index [2, 0]
val_b = arr_2d[2, 0]
print("b) 3rd row, 1st column element:", val_b)


# Q4
print("\n" + "=" * 60)
print("Q.4 - linspace, Array Properties, Transpose")
print("=" * 60)

Your_Name = np.linspace(10, 100, 25)
print("Array (Your_Name):\n", Your_Name)

print("\nDimensions (ndim):", Your_Name.ndim)
print("Shape:", Your_Name.shape)
print("Total elements (size):", Your_Name.size)
print("Data type (dtype):", Your_Name.dtype)
print("Total bytes consumed (nbytes):", Your_Name.nbytes)

# Transpose using reshape()
transposed_reshape = Your_Name.reshape(25, 1)
print("\nTranspose using reshape(25,1) - shape:", transposed_reshape.shape)
print(transposed_reshape.T if False else transposed_reshape[:5], "... (showing first 5 rows)")

# Transpose using .T attribute
transposed_T = Your_Name.T
print("\nUsing .T attribute directly on 1D array:")
print("Shape after .T:", transposed_T.shape)
print("""
Explanation: reshape(25,1) changes the 1D array into a 2D column vector of shape (25,1).
  This visually represents a "transposed" version of a row vector.

""")

print("=" * 60)
print("Q.5 - 2D Array Statistics, Reshape & Resize")
print("=" * 60)

ucs420_YourName = np.array([[10, 20, 30, 40],
                             [50, 60, 70, 80],
                             [90, 15, 20, 35]])

print("Original Array (ucs420_YourName):\n", ucs420_YourName)

# Statistics
mean_val = np.mean(ucs420_YourName)
median_val = np.median(ucs420_YourName)
max_val = np.max(ucs420_YourName)
min_val = np.min(ucs420_YourName)
unique_vals = np.unique(ucs420_YourName)

print("\nMean:", mean_val)
print("Median:", median_val)
print("Max:", max_val)
print("Min:", min_val)
print("Unique elements:", unique_vals)

reshaped_ucs420_YourName = ucs420_YourName.reshape(4, 3)
print("\nReshaped Array (4x3) - reshaped_ucs420_YourName:\n", reshaped_ucs420_YourName)

# Resize to 2 rows x 3 columns 
resized_ucs420_YourName = np.resize(ucs420_YourName, (2, 3))
print("\nResized Array (2x3) - resized_ucs420_YourName:\n", resized_ucs420_YourName)

print("\nProgram completed successfully.")