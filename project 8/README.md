<div align="center">

# -- ! NumPy Analyzer ! --
### *An Interactive Console-Based Tool for NumPy Array Creation, Math, and Statistics*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Array%20Operations-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![OOP](https://img.shields.io/badge/OOP-Class%20Based-FF6F00?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Console](https://img.shields.io/badge/Console-Interactive%20CLI-4CAF50?style=for-the-badge&logo=windowsterminal&logoColor=white)](https://www.python.org/)

<br/>

> *"An array is just numbers — until you know how to talk to it."*

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [🧩 Class Design — `DataAnalytics`](#-class-design--dataanalytics)
- [🖥️ Program Walkthrough & Output](#️-program-walkthrough--output)
- [🛠️ Tech Stack](#️-tech-stack)
- [⚠️ Known Issues](#️-known-issues)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 📌 Overview

The **NumPy Analyzer** is a menu-driven, console-based Python application built around a single OOP class, `DataAnalytics`, that wraps a NumPy array and exposes a rich set of operations on it. The program runs in an infinite loop, presenting the user with a main menu until they choose to exit.

This project is designed to:
- Practice **object-oriented design** by wrapping NumPy functionality inside a class with a private array and property accessors
- Apply **NumPy fundamentals** — creation, indexing, slicing, stacking, splitting, searching, sorting, filtering
- Build a **robust CLI** with `match-case` menus, nested sub-menus, and exception handling
- Compute **aggregate statistics** on array data

---

## 🎯 Problem Statement

> **Objective:** Build a console-based interactive tool that lets a user create NumPy arrays and perform indexing, mathematical, structural, and statistical operations on them.

You are building a utility for anyone learning NumPy. The program must accept user choices from a menu and execute the corresponding task — creating arrays, performing element-wise math, combining/splitting arrays, searching/sorting/filtering, or computing statistics like sum, mean, median, standard deviation, and variance.

| 📂 Feature | 📄 Type | 🔍 Description |
|------------|---------|----------------|
| Array Creation | Menu Option 1 | Builds a 1D or 2D array from user input |
| Mathematical Operations | Menu Option 2 | Element-wise add, subtract, multiply, divide |
| Combine / Split | Menu Option 3 | Vertical stacking and array splitting |
| Search, Sort, Filter | Menu Option 4 | Value search, row-wise sort, conditional filter |
| Aggregates & Statistics | Menu Option 5 | Sum, mean, median, std deviation, variance |

The goal is to demonstrate **class-based NumPy array handling** through a clean, menu-driven interactive program.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 🔁 **Infinite Menu Loop** | Program runs continuously until user selects Exit (Option 6) |
| 🧱 **Encapsulated Array** | Internal array stored as a private attribute (`__array`) behind a property |
| 🔢 **1D & 2D Array Creation** | Built dynamically from space-separated user input via `from_string()` |
| 🎯 **Indexing & Slicing** | Element access via tuple indices, range slicing via `start:end` syntax |
| ➕➖✖️➗ **Element-wise Math** | Addition, subtraction, multiplication, and safe division |
| 🧩 **Combine / Split** | Vertical stacking (`vstack`) and equal-section splitting (`array_split`) |
| 🔍 **Search** | Locates all positions of a target value using `np.where` |
| ↕️ **Sort** | Row-wise sort using `np.sort(axis=-1)` |
| 🧪 **Filter** | Conditional filtering using `>`, `<`, `>=`, `<=`, `==` |
| 📊 **Statistics Menu** | Sum, Mean, Median, Standard Deviation, Variance |
| ⚠️ **Exception Handling** | `try/except` blocks guard against invalid input and shape mismatches |

---

## 🏗️ Project Structure

```
📦 numpy-analyzer/
│
├── 📄 numpy_anaylizer.py     ← Main Python script (entry point)
│
└── 📄 README.md              ← Project documentation
```

---

## 🔄 Project Workflow

```
Program Start
      │
      ▼
┌─────────────────────────────┐
│   Display Main Menu         │  ← 1.Create 2.Math 3.Combine/Split 4.Search/Sort/Filter 5.Stats 6.Exit
└────────────┬────────────────┘
             │
   ┌─────────┼──────────┬───────────────┬────────────┐
   ▼         ▼           ▼               ▼            ▼
┌────────┐ ┌────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐
│Create  │ │Math Ops│ │Combine/Split│ │Search/Sort/│ │ Aggregates │
│Array   │ │+ - * / │ │ vstack/split│ │  Filter    │ │ & Stats    │
└───┬────┘ └───┬────┘ └──────┬─────┘ └──────┬─────┘ └──────┬─────┘
    │          │             │              │              │
    ▼          ▼             ▼              ▼              ▼
┌─────────────────────────────────────────────────────────────┐
│               Print Result / Error to Console                │
└────────────────────────────┬───────────────────────────────-─┘
                              │
                              ▼
                       Loop Back to Menu
                              │
                       (Choice: 6) Exit ✅
```

---

## 🧩 Class Design — `DataAnalytics`

The entire logic sits inside one class that wraps a NumPy array as a private field, with public methods for every operation.

### 🔐 1. Array Storage

```python
def __init__(self, data=None):
    self.__array = (
        np.array(data, dtype=int)
        if data is not None
        else np.empty((0,), dtype=int)
    )
```
The array is name-mangled (`__array`) and exposed only through a `@property` getter/setter — data always stays `int` dtype.

### 🏭 2. Array Creation from Input

```python
@classmethod
def from_string(cls, string_data, shape):
    flat = np.fromstring(string_data, sep=" ", dtype=int)
    return cls(flat.reshape(shape))
```
Turns raw space-separated input like `"1 2 3"` into a properly shaped array.

### ✂️ 3. Slice Parsing

```python
@staticmethod
def parse_slice(slice_str):
    if not slice_str or ":" not in slice_str:
        return slice(None)
    parts = slice_str.split(":")
    start = int(parts[0]) if parts[0] else None
    end = int(parts[1]) if parts[1] else None
    return slice(start, end)
```
Converts a `"start:end"` string into a real Python `slice` object for indexing.

### ➕ 4. Element-wise Math (with shape guard)

```python
def _check_shape(self, other_arr):
    if self.__array.shape != other_arr.shape:
        raise ValueError("Arrays must have identical dimensions!")

def elementwise_add(self, other_arr):
    self._check_shape(other_arr)
    return np.add(self.__array, other_arr)
```
Every math method (`add`, `subtract`, `multiply`, `divide`) validates shapes first via `_check_shape`.

### 🔍 5. Search, Sort, Filter

```python
def search_value(self, value):
    return np.where(self.__array == value)

def sort_array(self):
    return np.sort(self.__array, axis=-1)

def filter_condition(self, operator, threshold):
    match operator:
        case ">":  mask = self.__array > threshold
        case "<":  mask = self.__array < threshold
        case "==": mask = self.__array == threshold
        ...
    return self.__array[mask]
```
Uses Python 3.10+ `match-case` for clean conditional dispatch.

---

## 🖥️ Program Walkthrough & Output

### 1️⃣ Creating a 1D Array + Indexing

The program opens with the main menu. Choosing **Option 1 → 1D Array** builds `[1 2 3]` from user input, then **Indexing (Option 1)** retrieves the element at index `0`.

![Create array and indexing output](images/output_01.png)

---

### 2️⃣ Element-wise Addition & Division (started)

**Option 2 → Addition** correctly adds `[1 2 3] + [4 5 6] = [5 7 9]`. Division is then selected next.

![Addition output](images/output_02.png)

---

### 3️⃣ Subtraction & Multiplication

**Subtraction** gives `[-3 -3 -3]` and **Multiplication** gives `[4 10 18]` — both element-wise and correct.

![Subtraction and multiplication output](images/output_03.png)

---

### 4️⃣ Division Bug & Combine Arrays

**Division** fails with a dtype casting error (`float64` → `int64`), because `np.divide` naturally returns floats but the output buffer (`out=np.zeros_like(...)`) is forced to `int`. Afterward, **Combine Arrays** (vertical stack) works fine.

![Division error and combine output](images/output_04.png)

---

### 5️⃣ Split Array & Search

**Split Array** into 3 sections gives `[1]`, `[2]`, `[3]`. **Search a value (2)** is then selected.

![Split array output](images/output_05.png)

---

### 6️⃣ Search Result & Sort

The value `2` is found at index `1`. **Sort** then confirms the array is already sorted: `[1 2 3]`.

![Search and sort output](images/output_06.png)

---

### 7️⃣ Filter & Statistics Bug (Sum)

**Filter (`> 1`)** correctly returns `[2 3]`. Then **Statistics → Sum** fails with `'DataAnalytics' object has no attribute 'compute_sum'` — this method was never implemented in the class.

![Filter output and sum error](images/output_07.png)

---

### 8️⃣ Statistics Bugs (Mean, Median start)

**Mean** also fails the same way (`compute_mean` doesn't exist). **Median** is selected next.

![Mean error output](images/output_08.png)

---

### 9️⃣ Median Works, Standard Deviation Fails

**Median** correctly returns `2.0` (this is the only stat method actually implemented). **Standard Deviation** fails — `compute_std` doesn't exist either.

![Median success and std error output](images/output_09.png)

---

### 🔟 Variance Fails & Program Exit

**Variance** also fails (`compute_variance` missing). Choosing **Option 6** exits the program with a goodbye message.

![Variance error and exit output](images/output_10.png)

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| 🐍 **Python** | 3.10+ | Core language (uses `match-case` syntax) |
| 🔢 **NumPy** | Any recent | Array creation, math, stacking, splitting, search, sort |
| 🧱 **OOP** | Built-in | Encapsulation via private attributes and `@property` |
| 🏭 **classmethod / staticmethod** | Built-in | Alternate constructors and utility parsing |
| ⚠️ **try/except** | Built-in | Input validation and error handling |
| 🖨️ **print() / input()** | Built-in | Console I/O and user interaction |

---

## ⚠️ Known Issues

Based on the actual program run captured above, the following bugs currently exist in `numpy_anaylizer.py`:

| # | Issue | Where | Cause |
|---|-------|-------|-------|
| 1 | **Division crashes** | `elementwise_divide()` | `out=np.zeros_like(self.__array)` forces an `int` output buffer, but true division naturally produces `float64`, causing a casting error |
| 2 | **`compute_sum` missing** | Statistics Menu → Option 1 | Method not defined in `DataAnalytics` class |
| 3 | **`compute_mean` missing** | Statistics Menu → Option 2 | Method not defined in `DataAnalytics` class |
| 4 | **`compute_std` missing** | Statistics Menu → Option 4 | Method not defined in `DataAnalytics` class |
| 5 | **`compute_variance` missing** | Statistics Menu → Option 5 | Method not defined in `DataAnalytics` class |
| 6 | **3D Array option is a dead end** | Array Creation Menu → Option 3 | Menu lists "3D Array" but `main()` only handles `case "1"` and `case "2"` |

**Suggested fix for division:**
```python
def elementwise_divide(self, other_arr):
    self._check_shape(other_arr)
    return np.divide(
        self.__array, other_arr,
        out=np.zeros_like(self.__array, dtype=float),
        where=other_arr != 0
    )
```

**Suggested fix for missing statistics methods** — add alongside `compute_median`:
```python
def compute_sum(self):
    return float(np.sum(self.__array))

def compute_mean(self):
    return float(np.mean(self.__array))

def compute_std(self):
    return float(np.std(self.__array))

def compute_variance(self):
    return float(np.var(self.__array))
```

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🎓 **Educational** | Demonstrates encapsulation, class methods, static methods, and NumPy fundamentals together |
| 🔄 **Reusable Class** | `DataAnalytics` can be imported and reused outside the CLI |
| 🛡️ **Safe by Design** | Shape checks and `try/except` blocks prevent most crashes from bad input |
| 🖥️ **No External Dependencies** | Only requires `numpy` — no other packages needed |
| ⚡ **Single-File Script** | Instantly runnable from any terminal with Python 3.10+ |
| 🧪 **Extensible** | Easy to plug in the missing aggregate methods and true 3D array support |

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for full details.

```
MIT License — Free to use, modify, and distribute with attribution.
```

---

## 👤 Author

<div align="center">

### Your Name Here

[![GitHub](https://img.shields.io/badge/GitHub-yourhandle-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/)

> *"Debugging is just talking to your array until it tells you what went wrong."*

**🎓 Role:** Python Developer | NumPy Enthusiast \
**📍 Location:** India\
**🛠️ Skills:** Python · NumPy · OOP · CLI Applications · Debugging

</div>

---

## 🙏 Acknowledgements

Special thanks to the following resources that made this project possible:

- 📚 [NumPy Official Docs](https://numpy.org/doc/stable/) — Official NumPy reference
- 🐍 [Python Official Docs](https://docs.python.org/3/) — Official Python language reference
- 🔀 [Python `match` statement — PEP 634](https://peps.python.org/pep-0634/) — Structural pattern matching reference
- 🖥️ [W3Schools NumPy](https://www.w3schools.com/python/numpy/default.asp) — Beginner NumPy reference
- 💬 [Stack Overflow Community](https://stackoverflow.com/) — Problem-solving support

---

<div align="center">

---

*Last updated: 09 July, 2026*

</div>
