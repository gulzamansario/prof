Aapka ye question **Recursion + Backtracking + Decision Making (Take/Skip) + Subset Sum Pattern** par based hai. Iske liye sirf same type ke questions solve karna enough nahi hai. Pehle ye concepts clear hone chahiye:

* Recursion tree banana
* Take / Not Take choice
* Remaining target maintain karna
* Index / current number track karna
* Unique elements ka concept
* Counting all possible ways
* Pruning (optimization)

Neeche ek **15 Questions ka practice paper** hai jo gradually easy → hard jayega aur is topic ke concepts strong karega.

---

# Recursion + Backtracking Practice Paper

## Topic: Sum of Unique Nth Powers / Take-Not Take Pattern

---

## Level 1: Recursion Foundation

### Q1. Sum of First N Natural Numbers

**Problem:**

Given N, recursively calculate:

```
1 + 2 + 3 + .... + N
```

Example:

```
Input:
5

Output:
15
```

Concept:

* Base case
* Recursive relation

---

### Q2. Power Calculation Using Recursion

Calculate:

```
a^n
```

without using built-in power function.

Example:

```
Input:
2 5

Output:
32
```

Concept:

* Recursive multiplication

---

### Q3. Count Ways to Reach N

You can move:

* 1 step
* 2 steps

Find number of ways to reach N.

Example:

```
Input:
4

Output:
5
```

Explanation:

```
1+1+1+1
1+1+2
1+2+1
2+1+1
2+2
```

Concept:

* Recursion tree
* Counting paths

---

# Level 2: Subset / Take Skip Pattern

---

## Q4. Subset Sum Problem

Given array and target.

Find if any subset gives target.

Example:

```
arr=[2,3,5,7]
target=10


Output:
True
```

Because:

```
3+7=10
```

Concept:

Take:

```
3
```

Skip:

```
3
```

---

## Q5. Count Subsets With Given Sum

Find total subsets whose sum equals target.

Example:

```
arr=[1,2,3,4]
target=5


Output:
2
```

Because:

```
1+4
2+3
```

Concept:

* Counting recursion answers

---

## Q6. Partition Equal Subset Sum

Given array, check if it can divide into two groups having equal sum.

Example:

```
Input:

[1,5,11,5]


Output:

True
```

Because:

```
11
+
1+5+5
```

Concept:

Subset sum

---

# Level 3: Unique Selection Problems

---

## Q7. Sum of Unique Nth Powers ⭐

(Main Question)

Find number of ways to represent A:

```
A = x1^N + x2^N + x3^N...
```

Conditions:

* numbers unique
* positive integers only

Example:

```
A=10
N=2


Output:

1
```

Because:

```
1²+3²
```

Concept:

Take / Skip recursion

---

## Q8. Combination Sum

Given numbers and target.

Find all combinations.

Numbers can repeat.

Example:

```
arr=[2,3,6,7]

target=7


Output:

[
[7],
[2,2,3]
]
```

Concept:

Difference between:

```
repeat allowed
```

and

```
unique allowed
```

---

## Q9. Combination Sum II

Same as above.

But:

* Each number can be used only once.

Example:

```
arr=[10,1,2,7,6,1,5]

target=8


Output:

[
[1,7],
[1,2,5],
[2,6]
]
```

Concept:

Unique selection

---

# Level 4: Backtracking Deep Understanding

---

## Q10. Generate All Subsets

Given:

```
arr=[1,2,3]
```

Generate:

```
[]
[1]
[2]
[3]
[1,2]
[1,3]
[2,3]
[1,2,3]
```

Concept:

Binary decision tree

---

## Q11. Generate Subsets With Duplicate Elements

Input:

```
[1,2,2]
```

Output:

```
[
[],
[1],
[2],
[1,2],
[2,2],
[1,2,2]
]
```

No duplicate subsets.

Concept:

Sorting + Backtracking

---

## Q12. Count Ways To Make Amount

Coins:

```
[1,2,5]

Amount=5
```

Output:

```
4
```

Ways:

```
5

2+2+1

2+1+1+1

1+1+1+1+1
```

Concept:

Unbounded recursion

---

# Level 5: Advanced Backtracking

---

## Q13. Partition String Into Palindromes

Input:

```
"aab"
```

Output:

```
[
["a","a","b"],
["aa","b"]
]
```

Concept:

Choose / Backtrack

---

## Q14. N Queens Problem

Place N queens on chess board.

Example:

```
N=4
```

Output:

```
2 solutions
```

Concept:

Pure backtracking

---

## Q15. Word Search

Given board:

```
[
['A','B','C'],
['D','E','F'],
['G','H','I']
]
```

Find word:

```
ABE
```

Output:

```
True
```

Concept:

DFS + Backtracking

---

# Extra Challenge Questions (Interview Level)

## Q16. Target Sum

Given:

```
nums=[1,1,1,1,1]

target=3
```

Assign:

```
+
-
```

Find number of ways.

---

## Q17. Minimum Difference Partition

Divide array into two subsets such that difference is minimum.

Example:

```
[1,6,11,5]

Output:

1
```

---

## Q18. Count Unique Paths With Obstacles

Grid:

```
0 = open
1 = blocked
```

Find number of paths.

---

# Recommended Solving Order

Aap is order me solve karo:

```
Q1
 ↓
Q3
 ↓
Q4
 ↓
Q5
 ↓
Q7  ⭐
 ↓
Q8
 ↓
Q9
 ↓
Q10
 ↓
Q11
 ↓
Q12
 ↓
Q14
```

 **Q4, Q5, Q7, Q9, Q10**