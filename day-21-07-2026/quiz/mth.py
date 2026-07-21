import math

# Sabhi functions aur constants print karne ke liye
all_items = dir(math)

# Un-wanted internal methods (__doc__, __name__ etc.) ko filter karne ke liye:
functions_and_constants = [item for item in all_items if not item.startswith('_')]

print(functions_and_constants)