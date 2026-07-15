# ## Q5. Valid Parentheses

# Given:

# ```
# ()
# {}
# []
# ```

# Check if brackets are balanced.

# Example:

# ```
# Input:

# {[()]}

# Output:

# True
# ```

# Concept:

# Stack

# ---

stack = []
pat1 = "[]"
pat2 = "{}" 
pat3 = "()"
stack.append("()")
stack.append("[]")
for ch in stack:
    if ch[0] + ch[1] == pat1 or ch[0] + ch[1] == pat2 or ch[0] + ch[1] == pat3:
        print(1)
    else:
        print(0)