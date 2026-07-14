**List Indexing, List Slicing, List Methods, Tuples in Python, aur Tuple Methods**.

# 1. LIST INDEXING (Python)

List ek collection hoti hai jisme multiple values store kar sakte hain.

Example:

```python id="1j3p8z"
l1 = [7, 9, 12, 15, 20]
```

List ka har element ka ek **index number** hota hai.

```
Index:    0   1   2   3   4
Value:    7   9  12  15  20
```

### Accessing elements:

```python id="c2q4yy"
print(l1[0])
print(l1[2])
```

Output:

```
7
12
```

---

## Negative Indexing

Python mein last element ka index `-1` hota hai.

```
Index:   -5  -4  -3  -2  -1
Value:    7   9  12  15  20
```

Example:

```python id="qk1w0j"
print(l1[-1])
print(l1[-2])
```

Output:

```
20
15
```

---

# 2. LIST SLICING

Slicing ka matlab hai list ka ek part nikalna.

Syntax:

```python
list[start:end]
```

**Note:** End index include nahi hota.

Example:

```python id="j8w9a2"
l1 = [7, 9, 12, 15, 20]

print(l1[0:2])
```

Output:

```
[7, 9]
```

Kyun?

```
l1[0:2]

0 included ✅
1 included ✅
2 excluded ❌
```

---

### More examples:

```python id="6t4t7s"
print(l1[1:4])
```

Output:

```
[9, 12, 15]
```

---

### Start omit karna:

```python id="7c4y1z"
print(l1[:3])
```

Output:

```
[7, 9, 12]
```

---

### End omit karna:

```python id="qv1x8d"
print(l1[2:])
```

Output:

```
[12, 15, 20]
```

---

### Step slicing:

Syntax:

```python
list[start:end:step]
```

Example:

```python id="5fd7sh"
print(l1[0:5:2])
```

Output:

```
[7, 12, 20]
```

Har doosra element lega.

---

# 3. LIST METHODS

Lists **mutable** hoti hain (change ho sakti hain).

Example:

```python id="9jz6gk"
l1 = [7, 9, 12]
```

---

## 1. append()

End mein element add karta hai.

```python id="2jzq5d"
l1.append(15)

print(l1)
```

Output:

```
[7, 9, 12, 15]
```

---

## 2. insert()

Specific index par value add karta hai.

```python id="6yq8n4"
l1.insert(1, 100)

print(l1)
```

Output:

```
[7, 100, 9, 12]
```

---

## 3. extend()

Do lists ko combine karta hai.

```python id="x8g5rp"
a = [1,2]
b = [3,4]

a.extend(b)

print(a)
```

Output:

```
[1,2,3,4]
```

---

## 4. remove()

Value remove karta hai.

```python id="b0xw5s"
l1.remove(9)

print(l1)
```

Output:

```
[7,12]
```

---

## 5. pop()

Index se remove karta hai aur value return karta hai.

```python id="6m0w3f"
x = l1.pop(1)

print(x)
```

---

## 6. clear()

Puri list empty kar deta hai.

```python id="j7v1kp"
l1.clear()

print(l1)
```

Output:

```
[]
```

---

## 7. sort()

Ascending order mein arrange karta hai.

```python id="y5h9qk"
l1 = [5,1,8,3]

l1.sort()

print(l1)
```

Output:

```
[1,3,5,8]
```

---

## 8. reverse()

List ulta karta hai.

```python id="w3z0pk"
l1.reverse()

print(l1)
```

---

## 9. index()

Element ka index deta hai.

```python id="1g8b6r"
l1 = [7,9,12]

print(l1.index(9))
```

Output:

```
1
```

---

## 10. count()

Value kitni baar hai count karta hai.

```python id="z6t2qa"
l1 = [1,2,2,3]

print(l1.count(2))
```

Output:

```
2
```

---

# 4. TUPLES IN PYTHON

Tuple bhi list jaisa collection hai, lekin **immutable** hota hai.

Matlab tuple banne ke baad change nahi kar sakte.

### List:

```python
id="r5v8xy"
a = [1,2,3]
a[0] = 10
```

Allowed hai.

---

### Tuple:

```python id="8bq3wf"
t = (1,2,3)

t[0] = 10
```

Error:

```
TypeError
```

---

## Tuple banana:

```python id="5h2v0p"
t = (10,20,30)

print(t)
```

---

## Single element tuple:

Galat:

```python
t = (5)
```

Ye integer hai.

Sahi:

```python id="q5n1fz"
t = (5,)
```

Comma zaroori hai.

---

## Tuple indexing:

```python id="8x6v9p"
t = (10,20,30)

print(t[0])
```

Output:

```
10
```

---

## Tuple slicing:

```python id="w8v5km"
t = (10,20,30,40)

print(t[1:3])
```

Output:

```
(20,30)
```

---

# 5. TUPLE METHODS

Tuple immutable hota hai isliye iske methods kam hain.

Sirf **2 methods** hoti hain:

---

## 1. count()

Element kitni baar hai.

```python id="9m5xq2"
t = (1,2,2,3)

print(t.count(2))
```

Output:

```
2
```

---

## 2. index()

Element ka position deta hai.

```python id="m8z3kx"
t = (10,20,30)

print(t.index(20))
```

Output:

```
1
```

---

# List vs Tuple Difference

| List                     | Tuple               |
| ------------------------ | ------------------- |
| `[]` brackets            | `()` brackets       |
| Mutable                  | Immutable           |
| Zyada methods            | Sirf 2 methods      |
| Thoda slow               | Thoda fast          |
| Data change ho sakta hai | Data fixed hota hai |

---

### Yaad rakhne ka shortcut:

```
LIST:
append
insert
extend
remove
pop
clear
sort
reverse
index
count

TUPLE:
count
index
```
