# set operations

### 1. `union()`

**Purpose:** Dono sets ke **saare unique elements** ko combine karta hai.

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))
```

**Output:**

```python
{1, 2, 3, 4, 5}
```

Shortcut:

```python
print(a | b)
```

---

### 2. `intersection()`

**Purpose:** Sirf **common elements** return karta hai.

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a.intersection(b))
```

**Output:**

```python
{3}
```

Shortcut:

```python
print(a & b)
```

---

### 3. `difference()`

**Purpose:** Pehle set ke woh elements jo doosre set mein **nahin** hain.

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a.difference(b))
```

**Output:**

```python
{1, 2}
```

Shortcut:

```python
print(a - b)
```

---

### 4. `symmetric_difference()`

**Purpose:** Dono sets ke **uncommon elements** return karta hai (common elements hata deta hai).

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a.symmetric_difference(b))
```

**Output:**

```python
{1, 2, 4, 5}
```

Shortcut:

```python
print(a ^ b)
```

---

### 5. `issubset()`

**Purpose:** Check karta hai ke **ek set ke saare elements doosre set mein maujood hain ya nahi**.

```python
a = {1, 2}
b = {1, 2, 3, 4}

print(a.issubset(b))
```

**Output:**

```python
True
```

---

### 6. `issuperset()`

**Purpose:** Check karta hai ke **kya pehle set mein doosre set ke saare elements hain**.

```python
a = {1, 2, 3, 4}
b = {1, 2}

print(a.issuperset(b))
```

**Output:**

```python
True
```

---

## 📌 Easy Trick to Remember

| Method                   | Meaning                       |
| ------------------------ | ----------------------------- |
| `union()`                | Sab unique elements (Combine) |
| `intersection()`         | Sirf common elements          |
| `difference()`           | Pehle set ke unique elements  |
| `symmetric_difference()` | Sirf uncommon elements        |
| `issubset()`             | "Kya A, B ke andar hai?"      |
| `issuperset()`           | "Kya A ke andar B poora hai?" |

### Example with Same Sets

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))                  # {1, 2, 3, 4, 5}
print(a.intersection(b))           # {3}
print(a.difference(b))             # {1, 2}
print(a.symmetric_difference(b))   # {1, 2, 4, 5}
print(a.issubset(b))               # False
print(a.issuperset(b))             # False
```

