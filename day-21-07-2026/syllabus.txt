Practical Scenarios for Software Developer/Speed Programmer

Detailed Explanations of Each Problem

---

1. String with A & B - Remove Adjacent Matches

Problem Understanding:
You receive a string containing only characters 'A' and 'B'. Your goal is to transform it so that no two adjacent characters are the same. You can only delete characters (you cannot rearrange them).

Key Insight:

· A valid final string must alternate: ABABAB... or BABABA...
· Since we can only delete characters, we need to count how many characters must be removed to achieve alternating pattern
· Each time we see two same characters adjacent, one must be deleted

Example:

· Input: "AAABBB" → We can delete to get "AB" (delete 4 characters)
· Input: "ABAB" → Already alternating, delete 0 characters

---

2. Sum of Factorials Modulo 107

Problem Understanding:
Given N numbers, calculate (factorial of each number) modulo 107, then sum all these results modulo 107.

Important Observation:

· For any number ≥ 107, factorial contains 107 as a factor, so (factorial % 107) = 0
· This dramatically simplifies the problem - we only need to calculate factorial for numbers less than 107

Mathematical Concept:

· The modulus operation means we work with remainders after division by 107
· Factorial grows extremely fast, but modulo operation keeps numbers manageable
· For numbers ≥ MOD, factorial ≡ 0 (mod MOD)

---

3. Palindrome by Removing One Character

Problem Understanding:
Given a string of lowercase letters, find the index of one character that can be removed to make the string a palindrome. If the string is already a palindrome or impossible, return -1.

Approach Strategy:

· Use two pointers (left and right) moving toward each other
· When characters at left and right don't match:
  · Try removing the left character and check if remaining substring is palindrome
  · Try removing the right character and check if remaining substring is palindrome
· If either works, return that index
· If neither works, return -1

Example:

· "racecar" → Already palindrome → return -1
· "abca" → Remove 'b' to get "aca" → return 1 (index of 'b')
· "abcde" → No single removal creates palindrome → return -1

---

4. Password Strength Checker

Problem Understanding:
Validate a password against multiple criteria to determine if it's "strong".

Requirements Breakdown:

1. Length: 15-30 characters
2. At least one digit (0-9)
3. At least one lowercase letter (a-z)
4. At least one uppercase letter (A-Z)
5. At least one special character (!@#$%^&*() etc.)

Implementation Approach:

· Check length first (cheapest operation)
· Use regex patterns or character iteration to check each condition
· Provide specific feedback for each failing condition
· Return a boolean result with explanation

Edge Cases:

· Empty password
· Password with only digits
· Password with only letters

---

5. Sum of Palindromes from 0 to 100

Problem Understanding:
A palindrome reads the same forwards and backwards. Find the sum of all numbers from 0 to 100 that are palindromes.

Palindromes in range 0-100:

· Single-digit: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
· Two-digit: 11, 22, 33, 44, 55, 66, 77, 88, 99
· Three-digit: 101 (but this is > 100, so not included)

Mathematical Sum:

· Sum of 0-9 = 45
· Sum of 11, 22, ..., 99 = 11 × (1+2+...+9) = 11 × 45 = 495
· Total = 45 + 495 = 540

Key Concept:

· Check palindrome by comparing string with its reverse
· str(num) == str(num)[::-1]

---

6. Common Divisors of Two Numbers

Problem Understanding:
Given two numbers M (Mentah's points) and B (Balaj's points), find how many positive integers are divisors of BOTH numbers.

Mathematical Insight:

· Common divisors of two numbers are exactly the divisors of their GCD (Greatest Common Divisor)
· Example: M=12, B=18 → GCD=6 → Divisors of 6: 1,2,3,6 → Count = 4

Computing GCD:

· Use Euclidean algorithm
· Then count divisors of the GCD
· To count divisors efficiently, iterate up to sqrt(GCD)

Example:

· M=36, B=48 → GCD=12 → Divisors: 1,2,3,4,6,12 → Count = 6

---

7. Sum of Nth Powers of Unique Natural Numbers

Problem Understanding:
Find the number of ways to express integer A as a sum of unique natural numbers raised to the Nth power.

Example:

· A=10, N=2 → Ways: 1²+3² = 1+9 = 10, so 1 way
· A=100, N=2 → 6²+8² = 36+64 = 100, etc.

Conceptual Breakdown:

· Natural numbers: positive integers (1, 2, 3, ...)
· "Unique" means each number can be used at most once
· "Nth power" means raise each number to power N

Recursive Strategy:

· At each step, try using the current number or skipping it
· Keep track of remaining sum and next number to consider
· Base cases: sum reached exactly → 1 way; sum exceeded → 0 ways

---

8. Second Smallest Number in Array

Problem Understanding:
Find the second smallest distinct number in an array of numbers.

Examples:

· [5, 2, 8, 1, 3] → Smallest=1, Second smallest=2
· [1, 1, 2, 3] → Smallest=1, Second smallest=2 (distinct)
· [7, 7, 7] → No second smallest (all elements equal)

Two-Pointer Approach:

· Track smallest and second_smallest simultaneously
· Initialize both to infinity
· For each number:
  · If smaller than smallest: update second = smallest, smallest = num
  · Else if smaller than second and not equal to smallest: update second = num

Efficiency:

· Single pass through array: O(n)
· Works for unsorted arrays

---

9. Count Words in Camel Case String

Problem Understanding:
Camel case combines words where first word is all lowercase, and each subsequent word starts with an uppercase letter, followed by lowercase letters.

Examples:

· "hello" → 1 word
· "helloWorld" → 2 words
· "helloWorldJava" → 3 words
· "iLoveProgramming" → 3 words

Counting Strategy:

· Start with count = 1 (first word)
· Count every uppercase letter encountered
· Total words = 1 + number_of_uppercase_letters

Alternative Approach:

· Split the string at each uppercase letter
· Count the number of resulting parts

---

10. Pangram Checker

Problem Understanding:
Determine if a string contains every letter of the English alphabet (26 letters), ignoring case.

Approach:

· Convert string to lowercase (or uppercase)
· Create a set of letters in the string
· Check if the set contains all 26 letters

Example:

· "The quick brown fox jumps over the lazy dog" → Pangram ✓
· "Hello World" → Not a pangram ✗ (missing many letters)

Optimization:

· Can use a boolean array of size 26 instead of set
· Iterate through string and mark seen letters
· Return true only if all 26 letters are marked

---

11. Missing Elements from First Array

Problem Understanding:
Given two arrays, find which elements in the second array are NOT present in the first array.

Example:

· Array1: [1, 2, 3, 4, 5]
· Array2: [2, 4, 6, 8]
· Missing: [6, 8]

Implementation Strategy:

· Convert first array to a set (for O(1) lookup)
· Iterate through second array
· Check if each element exists in the set
· Collect elements that don't exist

Complexity Analysis:

· Time: O(m + n) where m,n are array lengths
· Space: O(m) for the set

---

12. Between Two Arrays

Problem Understanding:
Find all integers that satisfy two conditions:

1. Every element in first array is a factor of the integer
2. The integer is a factor of every element in second array

Example:

· arr1 = [2, 4] → Integer must be divisible by 2 and 4
· arr2 = [16, 32, 96] → Integer must divide 16, 32, and 96
· Candidates: 4, 8, 16

Logical Approach:

1. Find LCM of first array → Integer must be multiple of this
2. Find GCD of second array → Integer must divide this
3. Find all multiples of LCM that divide GCD
4. Count valid integers

Simpler Approach:

· Iterate through range from max(arr1) to min(arr2)
· Test each number against both conditions

---

13. Handshake Problem

Problem Understanding:
In a room with n people, if every person shakes hands with every other person exactly once, how many handshakes occur?

Mathematical Formula:

· Number of handshakes = C(n, 2) = n(n-1)/2
· Each handshake involves 2 people, and each pair shakes once

Example:

· n = 5 → 5 × 4 / 2 = 10 handshakes
· n = 10 → 10 × 9 / 2 = 45 handshakes

Formula Derivation:

· First person shakes hands with (n-1) people
· Second person already shook with first, so shakes with (n-2) remaining
· This pattern continues: (n-1) + (n-2) + ... + 1 = n(n-1)/2

Rounding:

· The formula always yields an integer result (no rounding needed)

---

14. Left Rotation of Array

Problem Understanding:
Rotate an array to the left by d positions. Elements shifted off the left end wrap around to the right.

Example:

· Array: [1, 2, 3, 4, 5]
· Rotate left by 2: [3, 4, 5, 1, 2]

Implementation Methods:

Method 1 - Slicing:

```
return arr[d:] + arr[:d]
```

Method 2 - In-place reversal:

1. Reverse the entire array
2. Reverse first (n-d) elements
3. Reverse last d elements

Important Consideration:

· If d > n, use d = d % n to handle large rotations efficiently

---

15. Sum of Prime Numbers Up to N

Problem Understanding:
Find the sum of all prime numbers from 1 to N (inclusive).

Definition:

· Prime number: integer > 1 with exactly two divisors (1 and itself)

Sieve of Eratosthenes Algorithm:

1. Create boolean array of size N+1, initially all True
2. Mark 0 and 1 as False (not prime)
3. For each prime p from 2 to sqrt(N):
   · Mark all multiples of p as False
4. Sum all indices where value is True

Example:

· N = 10 → Primes: 2, 3, 5, 7 → Sum = 17

Time Complexity:

· Sieve of Eratosthenes: O(N log log N)
· Much faster than checking each number individually

---

16. Sort Array Elements

Problem Understanding:
Sort the elements of an integer array in ascending (or descending) order.

Approach Options:

1. Built-in Sort:

· Python: sorted(arr) or arr.sort()
· Most programming languages provide built-in sorting

2. Manual Sorting Algorithms:

· Bubble Sort: Simple but O(n²)
· Quick Sort: O(n log n) average, divides and conquers
· Merge Sort: O(n log n), stable sorting
· Selection Sort: O(n²), repeatedly finds minimum element

3. Counting Sort (if range is small):

· Useful when array elements are within a small range
· O(n + k) where k is range of values

---

17. Fibonacci Sequence

Problem Understanding:
Generate and print the first N numbers of the Fibonacci sequence.

Definition:

· F(0) = 0, F(1) = 1
· F(n) = F(n-1) + F(n-2) for n ≥ 2

Sequence:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

Approaches:

1. Iterative:

```
Initialize a = 0, b = 1
For i in range(n):
    Print a
    a, b = b, a + b
```

2. Recursive (inefficient for large n):

```
if n <= 1: return n
return fib(n-1) + fib(n-2)
```

3. Dynamic Programming (memoization):

· Store computed results in a cache
· O(n) time complexity

---

18. Reverse an Array

Problem Understanding:
Reverse the order of elements in an integer array.

Example:

· Input: [1, 2, 3, 4, 5]
· Output: [5, 4, 3, 2, 1]

Implementation Methods:

Method 1 - Slicing:

```
return arr[::-1]
```

Method 2 - In-place using Two Pointers:

```
left, right = 0, len(arr) - 1
while left < right:
    swap arr[left] and arr[right]
    left += 1
    right -= 1
```

Method 3 - Using Stack:

· Push all elements onto a stack
· Pop to reverse the order

Space Considerations:

· In-place reversal: O(1) extra space
· Slicing: O(n) extra space

---

19. Postorder Traversal Using Recursive Diagonals

Problem Understanding:
Traverse a binary tree in postorder (left, right, root) and organize nodes by diagonals.

Postorder Traversal:

· Visit left subtree → Visit right subtree → Visit root

Diagonals Concept:

· All nodes on the same diagonal have the same (left - right) value
· When traversing:
  · Moving left: diagonal index increases (or decreases depending on definition)
  · Moving right: diagonal index stays the same

Algorithm:

1. Create a map from diagonal index to list of node values
2. Recursively traverse:
   · Left child: diag + 1
   · Right child: diag (or diag, depending on convention)
   · Postorder ensures children are processed before parent

Why Diagonal Traversal:

· Useful for visualizing tree structure
· Diagonal numbering helps identify same-slope nodes

---

20. Absolute Difference of Diagonal Sums

Problem Understanding:
Given a square matrix, calculate the absolute difference between the sum of the primary diagonal and the secondary diagonal.

Primary Diagonal:

· Elements where row index = column index
· Matrix[i][i] for i from 0 to n-1

Secondary Diagonal:

· Elements where row index + column index = n-1
· Matrix[i][n-1-i] for i from 0 to n-1

Example:

```
Matrix: [1, 2, 3]
        [4, 5, 6]
        [7, 8, 9]

Primary sum: 1 + 5 + 9 = 15
Secondary sum: 3 + 5 + 7 = 15
Difference: |15 - 15| = 0
```

Edge Cases:

· For odd n, the center element is counted in both diagonals
· This is correct as it appears in both diagonal definitions

---

21. Smallest and Largest in Unsorted Array

Problem Understanding:
Find both the minimum and maximum values in an array without sorting it first.

Single Pass Algorithm:

1. Initialize min = max = arr[0]
2. For each remaining element:
   · If element < min: update min
   · If element > max: update max
3. Return both values

Why Single Pass:

· Efficient: O(n) time complexity
· Memory efficient: O(1) extra space
· Works with any unsorted array

Edge Cases:

· Empty array: return None
· Array with one element: min = max = that element
· Negative numbers: handled correctly by value comparisons

Comparison with Sorting:

· Sorting takes O(n log n), unnecessary overhead
· Single pass is optimal for finding both extremes

---

22. Find Missing Number in 1-100 Array

Problem Understanding:
Given an array containing numbers from 1 to N (in this case N=100) with one number missing, find the missing number.

Mathematical Approach:

1. Calculate expected sum: N(N+1)/2
2. Calculate actual sum: sum of array elements
3. Missing number = Expected sum - Actual sum

Example:

· Array: [1,2,3,5,6] (missing 4)
· Expected sum (1-6): 21
· Actual sum: 17
· Missing: 4

Other Approaches:

· XOR method: XOR all numbers from 1 to N, then XOR with all array elements
· Result will be the missing number
· Works even if numbers are unsorted

Pros of XOR Method:

· No risk of integer overflow
· Works for very large N

---

23. Find Median of Odd-Sized List

Problem Understanding:
The median is the middle element of a sorted list. When the list has an odd number of elements, the median is the element at position (n+1)/2 after sorting.

Algorithm:

1. Sort the list
2. Return element at index n//2 (for 0-indexed arrays)
3. For odd n, this returns the exact middle element

Example:

· Unsorted: [7, 3, 1, 5, 9]
· Sorted: [1, 3, 5, 7, 9]
· Median: 5 (index 2 = n//2)

Why Odd N Only:

· For even N, median is average of two middle elements
· Problem specifies odd number of elements only

Alternate Approaches:

· Selection algorithm: O(n) without full sorting
· Quickselect: Partition-based selection

---

24. Find Element in Binary Tree

Problem Understanding:
Search for a target element N in a binary tree and return whether it exists.

Binary Tree Characteristics:

· Each node has at most two children (left and right)
· No ordering constraint (unlike Binary Search Tree)

Search Algorithm:

1. If current node is null: return false
2. If current node's value equals target: return true
3. Recursively search left subtree
4. Recursively search right subtree
5. Return true if found in either subtree

Complexity:

· Time: O(n) in worst case (must visit all nodes)
· Space: O(h) where h is tree height (recursion stack)

Traversal Types:

· Preorder: root, left, right
· Inorder: left, root, right
· Postorder: left, right, root
· Any traversal works for existence check

---

25. Find Loop in Linked List

Problem Understanding:
Detect whether a linked list contains a cycle (loop), where a node's next pointer eventually points back to an earlier node.

Floyd's Cycle Detection Algorithm (Tortoise and Hare):

Key Concept:

· Use two pointers: slow moves 1 step, fast moves 2 steps
· If there's a cycle, they will eventually meet
· If fast reaches null, no cycle exists

Algorithm Steps:

1. Initialize slow = head, fast = head
2. While fast and fast.next exist:
   · Move slow one step
   · Move fast two steps
   · If slow == fast: cycle detected
3. If fast reaches null: no cycle

Why It Works:

· In a cycle, the distance between fast and slow decreases by 1 each iteration
· They must meet when fast catches up to slow

Further Applications:

· Find the start of the cycle
· Determine cycle length
· Remove the cycle

Alternative Approaches:

· Hash table: Store visited nodes
· Time complexity: O(n), Space complexity: O(n)