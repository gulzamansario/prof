# most important Dictionary & Set methods

## Dictionary Methods

| Method           | What it does                  | Example                 |
| ---------------- | ----------------------------- | ----------------------- |
| `dict.keys()`    | Returns all keys              | `d.keys()`              |
| `dict.values()`  | Returns all values            | `d.values()`            |
| `dict.items()`   | Returns key-value pairs       | `d.items()`             |
| `dict.get(key)`  | Gets value safely             | `d.get("name")`         |
| `dict.update()`  | Updates dictionary            | `d.update({"age": 20})` |
| `dict.pop(key)`  | Removes key and returns value | `d.pop("age")`          |
| `dict.popitem()` | Removes last inserted item    | `d.popitem()`           |
| `dict.clear()`   | Removes all items             | `d.clear()`             |
| `dict.copy()`    | Makes a copy                  | `d.copy()`              |

### Example

```python
d = {"name": "Ali", "age": 20}

print(d.keys())
print(d.values())
print(d.items())
print(d.get("name"))

d.update({"city": "Lahore"})
print(d)

d.pop("age")
print(d)
```

---

## Set Methods

| Method      | What it does                      | Example            |
| ----------- | --------------------------------- | ------------------ |
| `add()`     | Adds one item                     | `s.add(5)`         |
| `update()`  | Adds multiple items               | `s.update([6, 7])` |
| `remove()`  | Removes item (error if absent)    | `s.remove(5)`      |
| `discard()` | Removes item (no error if absent) | `s.discard(5)`     |
| `pop()`     | Removes a random item             | `s.pop()`          |
| `clear()`   | Removes all items                 | `s.clear()`        |
| `copy()`    | Makes a copy                      | `s.copy()`         |

### Set Operations

| Operator/Method      | Usage                                  |                  |
| -------------------- | -------------------------------------- | ---------------- |
| Union                | `a                                     | b`or`a.union(b)` |
| Intersection         | `a & b` or `a.intersection(b)`         |                  |
| Difference           | `a - b` or `a.difference(b)`           |                  |
| Symmetric Difference | `a ^ b` or `a.symmetric_difference(b)` |                  |

### Checking Relationships

| Method         | Usage             |
| -------------- | ----------------- |
| `issubset()`   | `a.issubset(b)`   |
| `issuperset()` | `a.issuperset(b)` |
| `isdisjoint()` | `a.isdisjoint(b)` |

### Example

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))

a.add(6)
a.remove(2)
print(a)
```

### Exam/Interview Most Important Methods

* **Dictionary:** `keys()`, `values()`, `items()`, `get()`, `update()`, `pop()`, `clear()`, `copy()`
* **Set:** `add()`, `update()`, `remove()`, `discard()`, `pop()`, `union()`, `intersection()`, `difference()`, `symmetric_difference()`, `issubset()`, `issuperset()`

