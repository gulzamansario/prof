Great idea. Since you're practicing for Python interviews, here are **10 questions** based on **string validation and character checking**. They gradually increase in difficulty.

---

# Python Practice Paper – String Validation (10 Questions)

## Q1 (Easy) – Contains a Digit

Write a function that returns `True` if a string contains **at least one digit**, otherwise `False`.

**Input**

```text
"Usman123"
```

**Output**

```text
True
```

---

## Q2 (Easy) – Contains an Uppercase Letter

Return `True` if the string contains **at least one uppercase letter**.

**Input**

```text
"pythonRocks"
```

**Output**

```text
True
```

---

## Q3 (Easy) – Contains a Lowercase Letter

Check whether the string contains **at least one lowercase letter**.

**Input**

```text
"HELLO"
```

**Output**

```text
False
```

---

## Q4 (Easy-Medium) – Special Character Checker

Return `True` if the string contains **at least one special character**.

**Example Special Characters**

```
! @ # $ % ^ & * ( ) _ + - =
```

**Input**

```text
"Hello@123"
```

**Output**

```text
True
```

---

## Q5 (Medium) – Username Validator

A valid username:

* Length between **5 and 15**
* Only letters and digits
* No spaces
* No special characters

Return `True` or `False`.

**Input**

```text
"Usman123"
```

**Output**

```text
True
```

---

## Q6 (Medium) – PIN Validator

A valid PIN:

* Exactly **6 digits**
* No letters
* No special characters

**Input**

```text
"123456"
```

**Output**

```text
True
```

---

## Q7 (Medium) – Email Format Checker (Basic)

Check whether a string contains:

* One `@`
* At least one `.` after `@`

Don't use regex.

**Input**

```text
"user@gmail.com"
```

**Output**

```text
True
```

---

## Q8 (Medium-Hard) – Password Strength Checker

A password is valid if it contains:

* 12–20 characters
* One uppercase
* One lowercase
* One digit
* One special character

Return `True` or `False`.

---

## Q9 (Hard) – Character Counter

Given a string, return:

* Number of uppercase letters
* Number of lowercase letters
* Number of digits
* Number of special characters

**Input**

```text
"Usman@123"
```

**Output**

```text
Uppercase: 1
Lowercase: 5
Digits: 3
Special: 1
```

---

## Q10 (Interview Level) – Strongest Password

Return:

* `"Weak"`
* `"Medium"`
* `"Strong"`

Rules:

**Weak**

* Length < 8

**Medium**

* Length ≥ 8
* Contains letters and digits

**Strong**

* Length ≥ 15
* Uppercase
* Lowercase
* Digit
* Special character

**Example**

Input

```text
Python@123456789
```

Output

```text
Strong
```

---

## 💡 Methods You'll Practice

By solving these, you'll become comfortable with:

* `len()`
* `any()`
* `all()`
* `isalpha()`
* `isdigit()`
* `isalnum()`
* `islower()`
* `isupper()`
* `count()`
* `in`
* `for` loops
* Boolean logic

These are common in Python coding interviews and help build strong string-processing skills.
