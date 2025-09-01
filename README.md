# Base-20 Number Converter
oumiyhoi
## 📌 Overview
This project implements a simple Python function `base20` that converts a decimal (base-10) number into a base-20 representation.  
In this system:
- The digits `0–19` are represented by the letters `A–T`.  
- Example conversions:
  - `0 → A`
  - `19 → T`
  - `20 → BA`

This project is part of **Software Lab – III (Assignment 2)**, integrated with Jira for project management and GitHub for version control.

---

## 🛠️ Features
- Converts any non-negative base-10 integer into base-20 string.
- Handles edge cases (e.g., `0 → A`).
- Uses remainder and division method for conversion.
- Clean and reusable function.

---

## 💻 Usage
### Code Example
```python
from base20 import base20

print(base20(0))     # A
print(base20(19))    # T
print(base20(20))    # BA
print(base20(400))   # KKA
