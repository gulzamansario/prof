# ### Q8. Divisors in a Range

# Write a function that takes two numbers:

# * N
# * X                           

# Return how many numbers between **1** and **N** divide **X** exactly.

# **Example**

# ```
# Input:
# N = 10
# X = 24

# Output:
# 8
# ```

# **Explanation**

# Numbers are

# ```
# 1
# 2
# 3
# 4
# 6
# 8
# 12 (not counted because >10)
# 24 (not counted because >10)
# ```

# So answer is

# ```
# 6
# ```

# ---

N = 10
X = 24

for i in range(1, N+1):
    if X % i == 0:
        print(i)