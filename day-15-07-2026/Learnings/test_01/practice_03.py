# ---

# ## Q3. Check If String Has Adjacent Same Characters

# Return True if any adjacent characters are same.

# Example:

# ```
# Input:

# ABBA

# Output:

# True
# ```

# ---

same = "ABBA"

stack =[]
for chr in same:
    if chr and chr[-1][0] == chr:
        t = 1
    else:
        t = 0
print(t)
    