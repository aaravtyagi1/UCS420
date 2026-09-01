import numpy as np

#Q1=

print("========== Q1 ==========")

temperature = np.array([25, 28, 31, 35, 38, 27, 33, 40])

corrected_temperature = temperature + 2
print("\na. Corrected temperatures:", corrected_temperature)

fahrenheit = (corrected_temperature * 9 / 5) + 32
print("b. Temperatures in Fahrenheit:", fahrenheit)

greater_than_32 = temperature[temperature > 32]
print("c. Readings greater than 32°C:", greater_than_32)

count = np.sum(temperature > 32)
print("d. Number of readings greater than 32°C:", count)

#Q2

print("\n========== Q2 ==========")

steps = np.array([
    [5000, 6200, 7100],
    [8000, 7500, 9000],
    [4500, 5100, 4800],
    [9000, 8500, 9500]
])
total_steps = np.sum(steps)
print("\na. Total steps:", total_steps)

mean_steps = np.mean(steps)
print("b. Mean steps:", mean_steps)

maximum = np.max(steps)
minimum = np.min(steps)

print("c. Maximum steps:", maximum)
print("   Minimum steps:", minimum)

# d. Total steps for each day
daily_totals = np.sum(steps, axis=0)
print("d. Total steps for each day:", daily_totals)

# e. Total steps for each user
user_totals = np.sum(steps, axis=1)
print("e. Total steps for each user:", user_totals)

# f. Position of maximum value
max_position = np.unravel_index(np.argmax(steps), steps.shape)
print("f. Position of maximum value:", max_position)


#Q3
print("\n========== Q3 ==========")

# a. Create the original array
original = np.array([1, 2, 3, 4, 5, 6])
print("\na. Original array:", original)

# b. Create a slice from index 1 to 4
subset = original[1:5]
print("b. Subset:", subset)

subset[0] = 999

print("\nc. After modifying subset:")
print("Original:", original)
print("Subset:", subset)

copied_array = original[1:5].copy()
copied_array[0] = 500

print("\nd. After modifying copied array:")
print("Original:", original)
print("Copied array:", copied_array)

matrix = np.arange(1, 13).reshape(3, 4)

print("\ne. 3 x 4 Matrix:")
print(matrix)

print("\nf. First row:", matrix[0])

print("Last row:", matrix[-1])

print("Second column:", matrix[:, 1])

print("Rows 1-2 and columns 2-3:")
print(matrix[1:3, 2:4])

flattened = matrix.flatten()
raveled = matrix.ravel()

print("\ng. Using flatten():", flattened)
print("Using ravel():", raveled)

raveled[0] = 999

print("\nh. After modifying ravel():")
print("Original matrix:")
print(matrix)
print("Raveled array:", raveled)

matrix = np.arange(1, 13).reshape(3, 4)

flattened = matrix.flatten()
flattened[0] = 500

print("\ni. After modifying flatten():")
print("Original matrix:")
print(matrix)
print("Flattened array:", flattened)

print("\nj. Matrix properties:")
print("Shape:", matrix.shape)
print("Dimensions (ndim):", matrix.ndim)
print("Size:", matrix.size)
print("Data type (dtype):", matrix.dtype)


#Q4

print("\n========== Q4 ==========")

y = np.array([40, 65, 30, 85])

X = np.array([
    [6, 70, 3],
    [5, 50, 6],
    [8, 80, 2],
    [4, 30, 8]
])

print("\na. Shape of X:", X.shape)
print("Dimensions of X:", X.ndim)

X_transpose = X.T

print("\nb. X.T:")
print(X_transpose)

XtX = X.T @ X

print("\nc. X.T @ X:")
print(XtX)

inverse_XtX = np.linalg.inv(XtX)

print("\nd. Inverse of X.T @ X:")
print(inverse_XtX)


beta = np.linalg.inv(X.T @ X) @ X.T @ y

print("\ne. OLS Coefficients (Beta):")
print(beta)

print("\nf. Coefficient Interpretation:")
print("Sleep hours coefficient:", beta[0])
print("Activity level coefficient:", beta[1])
print("Stress level coefficient:", beta[2])

new_user = np.array([5, 40, 7])

predicted_score = new_user @ beta

print("\ng. New user:", new_user)
print("Predicted assistance score:", predicted_score)