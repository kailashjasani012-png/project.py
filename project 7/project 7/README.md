<div align="center">

# 🛠️ Multi Utility Toolkit

### *Interactive Console-Based Python Utility Application*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Modules](https://img.shields.io/badge/Modules-datetime%20%7C%20math%20%7C%20random%20%7C%20uuid-FF6F00?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Console](https://img.shields.io/badge/Console-Interactive%20CLI-4CAF50?style=for-the-badge&logo=windowsterminal&logoColor=white)](https://www.python.org/)
[![File I/O](https://img.shields.io/badge/FileIO-Create%20%7C%20Read%20%7C%20Write-9C27B0?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

<br/>

> *"One toolkit to rule them all — datetime, math, random, files and more, all in one place."*

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [⏰ Part 1 — Datetime & Time Operations](#-part-1--datetime--time-operations)
- [🔢 Part 2 — Mathematical Operations](#-part-2--mathematical-operations)
- [🎲 Part 3 — Random Data Generation](#-part-3--random-data-generation)
- [🆔 Part 4 — UUID Generator](#-part-4--uuid-generator)
- [📁 Part 5 — File Operations](#-part-5--file-operations)
- [🔍 Part 6 — Module Explorer](#-part-6--module-explorer)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Output Screenshots](#-results--output-screenshots)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 📌 Overview

The **Multi Utility Toolkit** is a powerful, menu-driven Python console application that brings together six different utility modules in one place. Built using Python's standard library, it demonstrates a wide range of core programming concepts including:

- **Date & time manipulation** using the `datetime` and `time` modules
- **Mathematical computations** using the `math` module
- **Random data generation** using the `random` module
- **UUID generation** using the `uuid` module
- **File I/O operations** using Python's built-in `open()`
- **Dynamic module inspection** using `importlib`

This project is designed to:
- Combine multiple Python standard libraries into one unified CLI tool
- Demonstrate menu-driven, loop-based program design
- Practice user input handling, error handling, and modular coding
- Build a reusable utility that can be extended easily

---

## 🎯 Problem Statement

> **Objective:** Build a multi-feature console-based Python tool covering time, math, random, UUID, file, and module utilities.

| 📂 Feature | 📄 Module Used | 🔍 Description |
|------------|---------------|----------------|
| Datetime Operations | `datetime`, `time` | Display time, date difference, stopwatch, timer |
| Mathematical Operations | `math` | Factorial, compound interest, trig, area |
| Random Data Generation | `random` | Numbers, lists, passwords, OTP |
| UUID Generation | `uuid` | Universally unique identifier |
| File Operations | Built-in I/O | Create, write, read, append files |
| Module Explorer | `importlib` | Inspect any Python module's attributes |

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 🔁 **Infinite Menu Loop** | Runs continuously until the user selects Exit |
| ⏰ **Datetime Suite** | Current time, date diff, format, stopwatch, countdown |
| 🔢 **Math Suite** | Factorial, compound interest, trig values, circle & rectangle area |
| 🎲 **Random Suite** | Random int, random list, password generator, OTP |
| 🆔 **UUID Generator** | One-click UUID v4 generation |
| 📁 **File Operations** | Full CRUD-style file handling (create, write, read, append) |
| 🔍 **Module Explorer** | Dynamically inspect any Python module using `importlib` |
| ⚠️ **Error Handling** | Invalid choices and missing files are handled gracefully |
| 🖥️ **CLI Interface** | Simple, clean, text-based menu navigation |

---

## 🏗️ Project Structure

```
📦 multi-utility-toolkit/
│
├── 📄 import_datetime_py.py     ← Main script (entry point with all menus)
├── 📄 import.datetime.py        ← File utility helper functions
├── 📄 math_py.py                ← Math helper functions
├── 📄 __init___py.py            ← Package init file
│
└── 📄 README.md                 ← Project documentation
```

---

## 🔄 Project Workflow

```
Program Start
      │
      ▼
┌──────────────────────────────────┐
│       Display Main Menu          │
│  1. Datetime  2. Math  3. Random │
│  4. UUID  5. File  6. Module  7. Exit │
└──────────────┬───────────────────┘
               │
    ┌──────────┼──────────┐
    ▼          ▼          ▼
[Datetime]  [Math]  [Random/UUID/File/Module]
    │          │          │
    ▼          ▼          ▼
┌──────────────────────────────┐
│    Execute Selected Feature  │
└──────────────┬───────────────┘
               │
               ▼
        Loop Back to Menu
               │
          (Choice: 7) Exit ✅
```

---

## ⏰ Part 1 — Datetime & Time Operations

### Sub-menu Options:
1. Display Current Date and Time
2. Difference Between Two Dates
3. Format a Date
4. Stopwatch
5. Countdown Timer

**Key Concepts Used:**

| Concept | Detail |
|---------|--------|
| `datetime.datetime.now()` | Fetches current date & time |
| `strptime` / `strftime` | Parse and format date strings |
| `time.time()` | Used for stopwatch (elapsed time) |
| `time.sleep(1)` | Used for countdown timer |

**Sample Output:**
```
Current Date & Time : 2026-06-24 13:23:10.322132
Difference : 1082 days
14/04/2026
Elapsed Time : 0.41 seconds
Time Up!
```

> 📸 **Screenshots below** show all datetime features in action.

---

## 🔢 Part 2 — Mathematical Operations

### Sub-menu Options:
1. Factorial
2. Compound Interest
3. Trigonometry (Sin, Cos, Tan)
4. Area of Shapes (Circle / Rectangle)

**Key Formulas Used:**

| Operation | Formula |
|-----------|---------|
| Factorial | `math.factorial(n)` |
| Compound Interest | `P * (1 + r/100) ^ t` |
| Trigonometry | `math.sin/cos/tan(radians)` |
| Circle Area | `π × r²` |
| Rectangle Area | `length × breadth` |

**Sample Output:**
```
Factorial = 6
Compound Interest = 2420.0
Sin = 0.4999999...   Cos = 0.866...   Tan = 0.577...
Area = 153.94  (Circle, r=7)
Area = 70.0    (Rectangle, 7×10)
```

---

## 🎲 Part 3 — Random Data Generation

### Sub-menu Options:
1. Random Number (1–100)
2. Random List (5 elements)
3. Random Password (custom length)
4. Random OTP (4-digit)

**Sample Output:**
```
53
[73, 91, 38, 11, 77]
Password = BMAV$9MWSDYpt5ACK3o6dOBCmAJjkKUwNrMYY$acqQVzw  (45 chars)
OTP = 3269
```

---

## 🆔 Part 4 — UUID Generator

Generates a random UUID v4 using Python's `uuid` module.

**Sample Output:**
```
Generated UUID
007aedb5-5e12-42f4-aa2e-6b9bc4c69c62
```

---

## 📁 Part 5 — File Operations

### Sub-menu Options:
1. Create File
2. Write File
3. Read File
4. Append File

**Sample Session:**
```
File Name : student.txt → file created successfully!
Enter Data : yashvi,18,45 → data written successfully!
File Content: yashvi,18,45
Enter Data : yashvi,78,23 → data appended successfully!
```

---

## 🔍 Part 6 — Module Explorer

Dynamically loads any Python module using `importlib` and displays all its attributes.

**Sample Output (math module):**
```
['__doc__', '__loader__', 'acos', 'asin', 'atan', 'cos', 'factorial', 'floor', 'log', 'pi', 'sin', 'sqrt', 'tan', ...]
```

---

## 📈 Results & Output Screenshots

### 🖥️ Main Menu & Datetime Operations

![Main Menu and Datetime](output_1.png)

*Main menu with all 7 options and Datetime sub-menu showing current date/time.*

---

![Date Difference and Format](output_4.png)

*Date difference calculation (1082 days) and date formatting.*

---

![Countdown Timer](output_5.png)

*Countdown timer from 10 to 1 and back to main menu.*

---

### 🔢 Mathematical Operations

![Factorial and Compound Interest](output_6.png)

*Factorial of 3 = 6, Compound Interest on ₹2000 at 10% for 2 years = ₹2420.*

---

![Trigonometry and Circle Area](output_7.png)

*Trig values for 30° and area calculations for Circle (r=7) and Rectangle (7×10).*

---

### 🎲 Random Data Generation

![Random Number and List](output_8.png)

*Random number: 53, Random list: [73, 91, 38, 11, 77].*

---

![Random Password and OTP](output_10.png)

*45-character random password and 4-digit OTP generation.*

---

### 🆔 UUID & File Operations

![UUID Generation and File Create](output_11.png)

*UUID generated and student.txt file created and written successfully.*

---

![File Read and Append](output_2.png)

*Reading file content (yashvi,18,45) and appending new data.*

---

### 🔍 Module Explorer

![Module Explorer - math](output_3.png)

*All attributes of the `math` module displayed dynamically via importlib.*

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| 🐍 **Python** | 3.8+ | Core programming language |
| ⏰ **datetime** | Built-in | Date/time operations |
| ⏱️ **time** | Built-in | Stopwatch and countdown |
| 🔢 **math** | Built-in | Mathematical functions |
| 🎲 **random** | Built-in | Random data generation |
| 🆔 **uuid** | Built-in | UUID generation |
| 📦 **importlib** | Built-in | Dynamic module loading |
| 📁 **open()** | Built-in | File I/O operations |
| 🔁 **While/Match** | Built-in | Menu loop and branching |

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🎓 **Educational** | Covers 6+ Python standard library modules in one project |
| 🔄 **Modular Design** | Each feature is isolated in its own function |
| 📚 **Reusable** | Helper functions in separate files (math_py, import.datetime) |
| 🖥️ **No Dependencies** | Runs with pure Python — no external libraries needed |
| ⚡ **Lightweight** | Small codebase, instantly runnable from any terminal |
| 🧪 **Extensible** | Easy to add new features (calculator, unit converter, etc.) |
| 📖 **Readable Code** | Clean `match-case` structure makes logic easy to follow |
| 🛡️ **Error Handling** | FileNotFoundError and invalid module names are caught |

---

## 📄 License

This project is licensed under the **MIT License** — free to use, modify, and distribute with attribution.

```
MIT License — Free to use, modify, and distribute with attribution.
```

---

## 👤 Author

<div align="center">

### Yashvi Jasani

[![GitHub](https://img.shields.io/badge/GitHub-Profile-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/)

> *"Every great toolkit starts with a single utility — keep building, keep growing."*

**🎓 Role:** Python Developer | Programming Enthusiast  
**📍 Location:** India  
**🛠️ Skills:** Python · CLI Applications · Standard Library · File I/O · Logic Building

</div>

---

## 🙏 Acknowledgements

Special thanks to the following resources and communities:

- 📚 [Python Official Docs](https://docs.python.org/3/) — Official Python language reference
- 🔁 [Real Python](https://realpython.com/) — In-depth Python tutorials
- 📐 [GeeksForGeeks](https://www.geeksforgeeks.org/) — Python examples and explanations
- 🖥️ [W3Schools Python](https://www.w3schools.com/python/) — Beginner Python reference
- 💬 [Stack Overflow Community](https://stackoverflow.com/) — Problem-solving support
- 📖 [Kaggle Learn](https://www.kaggle.com/learn) — Python and programming courses

---

<div align="center">

---

*Made with ❤️ and ☕ — Last updated: June 2026*

</div>
