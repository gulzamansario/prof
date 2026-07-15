Tum jis question par kaam kar rahe ho uska core concept hai **Stack + Bracket Matching**.

Tumhara current code:

```python
st = "a(b(c)d)"

new_arr = []

for chr in st:
    if "(" in chr:
        new_arr.append(chr)
    else:
        pass

n_r = "".join(new_arr)
print(n_r)
```

Isme tum sirf `"("` ko collect kar rahe ho, lekin actual problem mein hume **open aur close brackets ko match karna hota hai**.

---

# Question Overview: Valid Parentheses / Bracket Matching

## Problem:

Ek string di gayi hai jisme brackets hain:

```
( )
```

Check karo brackets **properly closed hain ya nahi**.

---

## Rule:

### Jab `(` aaye:

Stack mein add karo:

```
push
```

Example:

```
(
```

Stack:

```
[
(
]
```

---

### Jab `)` aaye:

Stack ka top remove karo:

```
pop
```

Example:

```
()
```

Process:

```
(
push

)
pop
```

Stack:

```
[]
```

Matlab pair complete hai.

---

# Example 1

Input:

```python
st = "(()()())"
```

Process:

```
(
stack = [(]

(
stack = [(,(]

)
remove (
stack = [(]

(
stack = [(,(]

)
remove (
stack = [(]

(
stack = [(,(]

)
remove (
stack = [(]

)
remove (
stack = []
```

End mein stack empty hai:

```
Valid ✅
```

---

# Example 2

Input:

```python
st = "(()"
```

Process:

```
(
stack = [(]

(
stack = [(,(]

)
pop

stack = [(]
```

End mein stack empty nahi hai:

```
Invalid ❌
```

---

# Example 3

Input:

```python
st = "())"
```

Process:

```
(
stack = [(]

)
pop

stack = []

)
```

Ab remove karne ke liye kuch nahi hai.

```
Invalid ❌
```

---

# Basic Logic (Pseudocode)

```
stack = []

for character in string:

    agar character "(" hai:
        stack mein add karo

    agar character ")" hai:
        agar stack empty hai:
            invalid
        warna:
            stack se remove karo


agar stack empty hai:
    valid

warna:
    invalid
```

---

# Related Practice Questions (Same Pattern)

### Q1. Valid Parentheses

Input:

```python
"(()())"
```

Output:

```
True
```

---

### Q2. Check Invalid Brackets

Input:

```python
"(()"
```

Output:

```
False
```

---

### Q3. Remove Outer Parentheses

Input:

```python
"(()())(())"
```

Output:

```
()()()
```

---

### Q4. Count Maximum Depth

Input:

```python
"(1+(2*3)+((8)/4))+1"
```

Output:

```
3
```

---

### Q5. Minimum Brackets Add Karne Hain

Input:

```python
"()))(("
```

Output:

```
4
```

---

## Yaad rakhne ka pattern:

```
Opening bracket "("
        ↓
      PUSH


Closing bracket ")"
        ↓
      POP
```

**Stack empty at end = Valid bracket**

Ye pattern coding interviews mein bahut common hai. Tumhara `adjacent duplicate removal` wala stack question aur ye bracket wala question dono ka base concept same hai: **"Last stored element ko check karna (LIFO)."**
