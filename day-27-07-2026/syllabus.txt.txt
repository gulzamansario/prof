# 1. Remove adjacent matching characters from a string containing only **A** and **B** so that no two adjacent characters are the same.
```python
def remove_adjacent(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)

# Example
print(remove_adjacent("AABBBAB"))  # Output: "AB"
```
# 2. Given **N** numbers, calculate the sum of their factorials modulo **107**.

```python
def factorial_mod(n, mod=107):
    fact = 1
    for i in range(1, n+1):
        fact = (fact * i) % mod
    return fact

def sum_factorials_mod(numbers):
    total = 0
    for num in numbers:
        total = (total + factorial_mod(num)) % 107
    return total

# Example
print(sum_factorials_mod([3, 4, 5]))  # Output: sum of 3! + 4! + 5! mod 107
```

# 3. Find the index of one character that can be removed to make a string a palindrome. Return **-1** if it is already a palindrome or impossible.

```python
def palindrome_index(s):
    if s == s[::-1]:
        return -1
    
    n = len(s)
    for i in range(n//2):
        if s[i] != s[n-1-i]:
            # Try removing left character
            if s[i+1:n-i] == s[i+1:n-i][::-1]:
                return i
            # Try removing right character
            if s[i:n-1-i] == s[i:n-1-i][::-1]:
                return n-1-i
    return -1

# Example
print(palindrome_index("abca"))  # Output: 1 (remove 'b')
```

# 4. Check whether a password is strong based on length, uppercase, lowercase, digits, and special characters.

```python
def is_strong_password(password):
    if len(password) < 8:
        return False
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    
    return has_upper and has_lower and has_digit and has_special

# Example
print(is_strong_password("Abc@1234"))  # Output: True
```

# 5. find the Sum of Palindromes 0 to 100
```python
def sum_palindromes_0_to_100():
    total = 0
    for i in range(101):
        if str(i) == str(i)[::-1]:
            total += i
    return total

# Example
print(sum_palindromes_0_to_100())  # Output: 500
```

# 6. Given two integers, determine the number of common divisors they share.

```python
def common_divisors(a, b):
    count = 0
    min_num = min(a, b)
    for i in range(1, min_num + 1):
        if a % i == 0 and b % i == 0:
            count += 1
    return count

# Example
print(common_divisors(12, 18))  # Output: 4 (1,2,3,6)
```

# 7. Find the number of ways to represent an integer **A** as the sum of unique natural numbers raised to the **Nth** power.

```python
def power_sum(A, N):
    def backtrack(target, start, current_sum):
        if current_sum == target:
            return 1
        if current_sum > target:
            return 0
        
        count = 0
        for i in range(start, int(target**(1/N)) + 2):
            power = i ** N
            count += backtrack(target, i+1, current_sum + power)
        return count
    
    return backtrack(A, 1, 0)

# Example
print(power_sum(10, 2))  # Output: 1 (1² + 3² = 10)
```

# 8. Find the second smallest distinct element in an array.
```python
def second_smallest(arr):
    distinct = list(set(arr))
    if len(distinct) < 2:
        return None
    distinct.sort()
    return distinct[1]

# Example
print(second_smallest([4, 2, 2, 3, 1]))  # Output: 2
```
# 9. Count the number of words in a camelCase string.
```python
def count_camelcase_words(s):
    if not s:
        return 0
    count = 1  # First word starts with lowercase
    for char in s:
        if char.isupper():
            count += 1
    return count

# Example
print(count_camelcase_words("camelCaseString"))  # Output: 3
```

# 10. Determine whether a given string is a pangram.
```python
def is_pangram(s):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return alphabet.issubset(set(s.lower()))

# Example
print(is_pangram("The quick brown fox jumps over the lazy dog"))  # Output: True
```

# 11. Find the elements present in the second array but missing from the first array.

```python
def missing_elements(arr1, arr2):
    set1 = set(arr1)
    return [x for x in arr2 if x not in set1]

# Example
print(missing_elements([1, 2, 3], [2, 3, 4, 5]))  # Output: [4, 5]
```

# 12. Find all integers that are multiples of every element in the first array and factors of every element in the second array.

```python
def between_two_sets(a, b):
    from math import gcd
    from functools import reduce
    
    def lcm(x, y):
        return x * y // gcd(x, y)
    
    lcm_a = reduce(lcm, a)
    gcd_b = reduce(gcd, b)
    
    count = 0
    for i in range(lcm_a, gcd_b + 1, lcm_a):
        if gcd_b % i == 0:
            count += 1
    return count

# Example
print(between_two_sets([2, 4], [16, 32, 96]))  # Output: 3
```
# 13. Given **n** people in a room, calculate the total number of handshakes if each pair shakes hands exactly once.

```python
def handshakes(n):
    return n * (n - 1) // 2

# Example
print(handshakes(5))  # Output: 10
```

# 14. Rotate an array to the left by **d** positions.
```python
def left_rotate(arr, d):
    n = len(arr)
    d = d % n  # Handle d > n
    return arr[d:] + arr[:d]

# Example
print(left_rotate([1, 2, 3, 4, 5], 2))  # Output: [3, 4, 5, 1, 2]
```

# 15. Find the sum of all prime numbers from **1** to **N**.
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_primes(N):
    return sum(i for i in range(2, N+1) if is_prime(i))

# Example
print(sum_primes(10))  # Output: 17 (2+3+5+7)
```

# 16. Sort the elements of an integer array in ascending or descending order.

```python
def sort_array(arr, ascending=True):
    return sorted(arr) if ascending else sorted(arr, reverse=True)

# Example
print(sort_array([3, 1, 4, 1, 5], True))   # Output: [1, 1, 3, 4, 5]
print(sort_array([3, 1, 4, 1, 5], False))  # Output: [5, 4, 3, 1, 1]
```

# 17. Generate the first **N** numbers of the Fibonacci sequence.
```python
def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

# Example
print(fibonacci(7))  # Output: [0, 1, 1, 2, 3, 5, 8]
```
# 18. Reverse the elements of an array.
```python
def reverse_array(arr):
    return arr[::-1]

# Example
print(reverse_array([1, 2, 3, 4]))  # Output: [4, 3, 2, 1]
```

# 19. Perform a postorder traversal of a binary tree and organize the nodes diagonally.

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diagonal_traversal(root):
    from collections import defaultdict
    
    diagonal_map = defaultdict(list)
    
    def postorder(node, d):
        if not node:
            return
        postorder(node.left, d + 1)
        postorder(node.right, d)
        diagonal_map[d].append(node.val)
    
    postorder(root, 0)
    
    result = []
    for d in sorted(diagonal_map.keys()):
        result.extend(diagonal_map[d])
    return result

# Example
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
print(diagonal_traversal(root))
```

# 20. Find the absolute difference between the sums of the primary and secondary diagonals of a square matrix.

```python
def diagonal_difference(matrix):
    n = len(matrix)
    primary_sum = sum(matrix[i][i] for i in range(n))
    secondary_sum = sum(matrix[i][n-1-i] for i in range(n))
    return abs(primary_sum - secondary_sum)

# Example
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(diagonal_difference(matrix))  # Output: 0
```

# 21. Find the smallest and largest elements in an unsorted array without sorting it.

```python
def min_max_unsorted(arr):
    if not arr:
        return None, None
    
    minimum = maximum = arr[0]
    for num in arr:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num
    return minimum, maximum

# Example
print(min_max_unsorted([3, 1, 7, 4, 2]))  # Output: (1, 7)
```

# 22. Find the missing number from an array containing numbers from **1** to **N** with one number missing.

```python
def missing_number(arr, N):
    expected_sum = N * (N + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

# Example
print(missing_number([1, 2, 4, 5], 5))  # Output: 3
```

# 23. Find the median of an odd-sized list.
```python
def find_median(arr):
    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    return sorted_arr[n // 2]

# Example
print(find_median([3, 1, 7, 5, 2]))  # Output: 3
```
# 24. Determine whether a given element exists in a binary tree.
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def search_binary_tree(root, target):
    if not root:
        return False
    if root.val == target:
        return True
    return search_binary_tree(root.left, target) or search_binary_tree(root.right, target)

# Example
root = TreeNode(1, TreeNode(2), TreeNode(3))
print(search_binary_tree(root, 3))  # Output: True
```
# 25. Detect whether a linked list contains a loop (cycle).
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    if not head:
        return False
    
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Example
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3
node3.next = node2  # Creates cycle
print(has_cycle(node1))  # Output: True
```