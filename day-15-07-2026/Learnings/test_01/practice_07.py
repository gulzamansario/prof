# ## Q6. Remove K Adjacent Same Characters

# Given string and k.

# Remove k consecutive same characters.

# Example:

# ```
# Input:

# deeedbbcccbdaa

# k=3


# Output:

# aa
# ```

# ---
st = "deeedbbcccbdaa"
k = 3
def remove_k_adjacent(st, k):
    stack = []

    for char in st:

        if stack and stack[-1][0] == char:
            # print(stack[-1][0], stack)
            stack[-1][1] += 1

            if stack[-1][1] == k:
                stack.pop()
        else:
            stack.append([char, 1])
    return "".join(char * count for char, count in stack)
print(remove_k_adjacent("deeedbbcccbdaa", 3))
