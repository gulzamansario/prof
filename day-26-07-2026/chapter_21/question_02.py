# 22. Find Missing Number in 1-100 Array

# Problem Understanding:
# Given an array containing numbers from 1 to N (in this case N=100) with one number missing, find the missing number.

# Mathematical Approach:

# 1. Calculate expected sum: N(N+1)/2
# 2. Calculate actual sum: sum of array elements
# 3. Missing number = Expected sum - Actual sum

# Example:

# · Array: [1,2,3,5,6] (missing 4)
# · Expected sum (1-6): 21
# · Actual sum: 17
# · Missing: 4

# Other Approaches:

# · XOR method: XOR all numbers from 1 to N, then XOR with all array elements
# · Result will be the missing number
# · Works even if numbers are unsorted

# Pros of XOR Method:

# · No risk of integer overflow
# · Works for very large N

# ---


arr = [0, 1, 2, 3, 4,6,  7, 8, 9]

for i in range(0, 10, 1):
    if i not in arr:
        print(i)


