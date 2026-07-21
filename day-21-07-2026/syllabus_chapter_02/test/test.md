# Python Practice Test Paper

## Topic: GCD, Divisors & Mathematical Logic

**Total Questions: 10**

### Q1. Count the Divisors

Write a Python function that accepts a positive integer **N** and returns the total number of positive divisors of that number.

**Example:**

```
Input:
N = 18

Output:
6
```

**Explanation:**

18 has the following divisors:

```
1, 2, 3, 6, 9, 18
```

---

### Q2. Find the Greatest Common Divisor (Without Built-in Function)

Write a function that takes two integers and returns their Greatest Common Divisor (GCD).

**Restriction:**
Do not use `math.gcd()`.

**Example**

```
Input:
24 36

Output:
12
```

---

### Q3. Count Common Divisors

Two students scored **M** and **B** points in a competition.

Write a function that returns how many positive integers divide **both** scores.

**Example**

```
Input:
12 18

Output:
4
```

**Explanation**

Common divisors are

```
1
2
3
6
```

---

### Q4. Print Common Divisors

Instead of counting them, print all common divisors of two numbers in ascending order.

**Example**

```
Input:
20 30

Output:
1
2
5
10
```

---

### Q5. Largest Common Divisor

Write a program that returns the largest positive integer that divides both numbers.

**Restriction**

Do not use `math.gcd()`.

---

### Q6. Are They Co-prime?

Two numbers are called **co-prime** if their GCD is **1**.

Write a function that returns:

```
True
```

if the numbers are co-prime, otherwise

```
False
```

**Example**

```
Input:
8 15

Output:
True
```

---

### Q7. Sum of Common Divisors

Write a function that returns the **sum** of all common divisors of two numbers.

**Example**

```
Input:
12 18

Output:
12
```

**Explanation**

```
1 + 2 + 3 + 6 = 12
```

---

### Q8. Divisors in a Range

Write a function that takes two numbers:

* N
* X

Return how many numbers between **1** and **N** divide **X** exactly.

**Example**

```
Input:
N = 10
X = 24

Output:
8
```

**Explanation**

Numbers are

```
1
2
3
4
6
8
12 (not counted because >10)
24 (not counted because >10)
```

So answer is

```
6
```

---

### Q9. HCF of Multiple Numbers

Write a function that accepts **three integers** and returns their Highest Common Factor (HCF).

**Example**

```
Input:
24 36 60

Output:
12
```

---

### Q10. Interview Level Question

Mentah and Balaj both participated in five different contests.

Their scores are stored in two lists.

```
Mentah = [12, 18, 24, 30, 36]

Balaj  = [18, 24, 30, 42, 48]
```

For every pair of scores at the same index, calculate the number of common divisors and return the result in a new list.

**Example Output**

```
[4, 8, 8, 4, 6]
```

---

# Rules

* ❌ Do not use ChatGPT.
* ❌ Do not use Google.
* ❌ Do not use AI code completion.
* ✅ Use Python functions.
* ✅ Write clean code.
* ✅ Test your program with multiple inputs.
