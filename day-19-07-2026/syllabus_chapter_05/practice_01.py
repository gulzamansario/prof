# ## Q1

# Write a program to print all palindrome numbers from **0 to 50**.

# Example Output

# ```text
# 0 1 2 3 4 5 6 7 8 9 11 22 33 44
# ```

for i in range(0, 51, 1):
    new_num = str(i)
    if new_num[::-1] == new_num:
        print(new_num)
    else:
        pass