<div align="center">

# 🛠️ Multi Utility Toolkit

### *Interactive Console-Based Python Utility Program*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Modules](https://img.shields.io/badge/Modules-datetime%20%7C%20math%20%7C%20random%20%7C%20uuid-FF6F00?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Console](https://img.shields.io/badge/Console-Interactive%20CLI-4CAF50?style=for-the-badge&logo=windowsterminal&logoColor=white)](https://www.python.org/)
[![File I/O](https://img.shields.io/badge/File-I%2FO%20Operations-9C27B0?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

<br/>

> *"One toolkit, infinite utilities — from time to math, from files to UUIDs."*

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [📸 Output Screenshots](#-output-screenshots)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Insights](#-results--insights)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 📌 Overview

The **Multi Utility Toolkit** is a menu-driven, interactive Python console application that brings together six powerful utility modules under one roof. It is designed to help users perform everyday programming tasks — from date calculations and math operations to file management and random data generation — all from a clean terminal interface.

This project is designed to:
- Demonstrate use of Python's standard library modules: `datetime`, `time`, `math`, `random`, `uuid`, `importlib`
- Practice building menu-driven programs with `match-case` statements
- Apply real-world concepts like file I/O, compound interest, stopwatch, and UUID generation
- Strengthen understanding of user input handling and modular programming

---

## 🎯 Problem Statement

> **Objective:** Build a console-based multi-utility tool that groups different utility functions into submenus.

| 📂 Module | 🔍 Description |
|-----------|----------------|
| Datetime & Time | Date display, difference, formatting, stopwatch, countdown |
| Math Operations | Factorial, compound interest, trigonometry, area of shapes |
| Random Data | Random number, list, password, OTP |
| UUID | Generate unique UUID v4 |
| File Operations | Create, write, read, append files |
| Module Explorer | Inspect Python module attributes using `importlib` |

---

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| 🔁 **Infinite Menu Loop** | Program runs until user selects Exit |
| 📅 **Datetime Operations** | Display current time, date difference, format date, stopwatch, countdown timer |
| 🧮 **Math Utilities** | Factorial, compound interest, trigonometry (sin/cos/tan), area of circle and rectangle |
| 🎲 **Random Data Generator** | Random number, list of 5 numbers, custom-length password, 4-digit OTP |
| 🆔 **UUID Generator** | Generate universally unique UUID v4 |
| 📁 **File Management** | Create, write, read, and append to text files |
| 🔍 **Module Explorer** | Dynamically list attributes of any Python module |
| ⚠️ **Error Handling** | Invalid choices and missing files handled gracefully |

---

## 🏗️ Project Structure

```
📦 multi-utility-toolkit/
│
├── 📄 import_datetime.py     ← Main Python script (entry point)
├── 📄 README.md              ← Project documentation
│
└── 📁 images/               ← Output screenshots
    ├── output_1.png
    ├── output_2.png
    ├── output_3.png
    ├── output_4.png
    ├── output_5.png
    ├── output_7.png
    ├── output_8.png
    ├── output_9.png
    ├── output_10.png
    └── output_11.png
```

---

## 🔄 Project Workflow

```
Program Start
      │
      ▼
┌─────────────────────────────────┐
│        Display Main Menu        │
│  1. Datetime   5. File Ops      │
│  2. Math       6. Module Exp.   │
│  3. Random     7. Exit          │
│  4. UUID                        │
└────────────┬────────────────────┘
             │
    ┌────────┼────────┐
    ▼        ▼        ▼
 Sub-menu  Sub-menu  Exit
 (loops)   (loops)    ✅
    │
    ▼
 Execute Task → Print Output
    │
    └──► Loop back to menu
```

---

## 📸 Output Screenshots

### 🚀 1. Main Menu & Datetime — Current Date/Time

> Program start hota hai clean main menu ke saath. Choice 1 se Datetime sub-menu khulta hai jahan current date & time display hoti hai.

![Main Menu and Datetime](images/output_1.png)

---

### 📅 2. Date Difference & Format Date & Stopwatch

> Kisi bhi do dates ke beech ka difference nikalo, date ko `DD/MM/YYYY` format mein convert karo, aur stopwatch se elapsed time measure karo.

![Date Difference Format Stopwatch](images/output_4.png)

---

### ⏱️ 3. Countdown Timer

> User-defined seconds se countdown shuru hota hai aur "Time Up!" message ke saath khatam hota hai.

![Countdown Timer](images/output_5.png)

---

### 🧮 4. Math — Factorial, Compound Interest & Trigonometry

> Kisi bhi number ka factorial nikalo, compound interest calculate karo, aur degrees mein angle deke Sin/Cos/Tan values pao.

![Factorial Compound Interest Trig](images/output_7.png)

---

### 📐 5. Math — Area of Circle & Rectangle

> Circle aur Rectangle dono ki area calculate karo using `math.pi` aur simple multiplication.

![Area of Shapes](images/output_8.png)

---

### 🎲 6. Random Data — Number, List, Password & OTP

> Ek random number ya 5 numbers ki list generate karo. Custom length ka secure password bhi bana sakte ho.

![Random Number and List](images/output_9.png)

---

### 🔐 7. Random Password (45 chars) & OTP

> 45-character ka strong random password aur 4-digit OTP generate kiya gaya.

![Random Password and OTP](images/output_10.png)

---

### 🆔 8. UUID Generation & File — Create & Write

> Ek globally unique UUID v4 generate hua. Uske baad `student.txt` file create karke usme data likha gaya.

![UUID and File Create Write](images/output_11.png)

---

### 📁 9. File — Read & Append

> File ka content read karke print kiya. Phir naya data append kiya gaya file ke end mein.

![File Read and Append](images/output_2.png)

---

### 🔍 10. Module Explorer & Program Exit

> `math` module ke saare attributes list hue `importlib` se. Phir choice 7 se program gracefully exit hua.

![Module Explorer and Exit](images/output_3.png)

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| 🐍 **Python** | 3.8+ | Core programming language |
| 📅 **datetime** | Built-in | Date and time operations |
| ⏱️ **time** | Built-in | Stopwatch and countdown |
| 🧮 **math** | Built-in | Factorial, trig, area calculations |
| 🎲 **random** | Built-in | Random data generation |
| 🆔 **uuid** | Built-in | UUID v4 generation |
| 🔍 **importlib** | Built-in | Dynamic module inspection |
| 📁 **File I/O** | Built-in | Text file operations |

---

## 📈 Results & Insights

- ✅ **6 Utility Modules** — Each accessible via a dedicated sub-menu
- 📅 **Real-time Date & Time** — Accurate to microseconds using `datetime.datetime.now()`
- 🔐 **Secure Password Generation** — Custom-length passwords using alphanumeric + special chars
- 🆔 **Unique IDs** — UUID v4 values guaranteed to be globally unique
- 📁 **File Persistence** — Data written to and read back from actual text files on disk
- 🔍 **Live Module Inspection** — View all attributes of `math`, `os`, `sys`, or any module

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🎓 **Beginner Friendly** | All standard library — no pip installs needed |
| 🔄 **Modular Design** | Each feature is isolated in its own function |
| 📚 **Educational** | Covers 6 different Python modules in one project |
| 🖥️ **No Dependencies** | Runs with pure Python from any terminal |
| ⚡ **Lightweight** | Single-file script, instantly runnable |
| 🧪 **Extensible** | Easy to add new utilities or sub-menus |
| 📖 **Clean Code** | `match-case` structure keeps logic readable |
| 🛡️ **Input Safety** | `FileNotFoundError` and invalid choices handled |

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

> *"One toolkit, endless possibilities — built line by line, function by function."*

**🎓 Role:** Junior Python Developer | Programming Enthusiast  
**📍 Location:** India  
**🛠️ Skills:** Python · Standard Library · CLI Applications · File I/O · Modular Programming

</div>

---

## 🙏 Acknowledgements

- 📚 [Python Official Docs](https://docs.python.org/3/) — Official Python language reference
- 🧮 [Python math module](https://docs.python.org/3/library/math.html) — Mathematical functions
- 📅 [Python datetime module](https://docs.python.org/3/library/datetime.html) — Date and time handling
- 🎲 [Python random module](https://docs.python.org/3/library/random.html) — Random data generation
- 💬 [Stack Overflow Community](https://stackoverflow.com/) — Problem-solving support
- 📖 [Real Python](https://realpython.com/) — Tutorials and best practices
- 🖥️ [W3Schools Python](https://www.w3schools.com/python/) — Beginner Python reference

---

<div align="center">

---

*Made with ❤️ and ☕ — Last updated: June 2026*

</div>
