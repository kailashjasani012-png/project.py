<div align="center">

# 🏢 Employee Management System

### *Python OOP Project — Inheritance, Encapsulation & Polymorphism in Action*

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OOP](https://img.shields.io/badge/Paradigm-OOP-FF6B6B?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-4CAF50?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [❓ Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [📁 Project Structure](#-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [🛠️ Tech Stack](#️-tech-stack)
- [📸 Results & Insights](#-results--insights)
- [✅ Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 📌 Overview

The **Employee Management System** is a console-based Python application that demonstrates the core principles of **Object-Oriented Programming (OOP)**. Using a three-level class hierarchy — `Person → Employee → Manager` — this project showcases how real-world entities can be modeled using classes, encapsulation (getters/setters), and inheritance.

The system provides a simple interactive menu where users can create and view records for persons, employees, and managers.

---

## ❓ Problem Statement

In many beginner Python projects, OOP concepts are taught in isolation without a practical context. This project bridges that gap by building a real, working system that uses:

- **Inheritance** to avoid code duplication across `Person`, `Employee`, and `Manager`
- **Encapsulation** to protect data using private attributes and getter/setter methods
- **Polymorphism** through overriding the `display()` method in each subclass

The goal is to design a system that cleanly manages multiple types of organizational records while following OOP best practices.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🧑 Create Person | Store name and age for a basic person record |
| 👔 Create Employee | Extends Person with Employee ID and Salary |
| 🗂️ Create Manager | Extends Employee with a Department field |
| 👁️ Show Details | View stored details for any of the three record types |
| 🔒 Encapsulation | Private attributes with getter/setter methods in all classes |
| ♻️ Inheritance | `Employee` inherits from `Person`; `Manager` inherits from `Employee` |
| 🔄 Polymorphism | Each class overrides `display()` to show relevant fields |
| 🚪 Exit | Gracefully exit the system with a farewell message |

---

## 📁 Project Structure

```
📦 Employee Management System
 ┣ 📄 project_5.py          ← Main Python source file
 ┣ 📄 README.md             ← Project documentation (this file)
 ┣ 🖼️ pro_5_output_1.png   ← Output screenshot 1 (Create Person/Employee)
 ┣ 🖼️ pro_5_output_2.png   ← Output screenshot 2 (Create Manager / Show Person & Employee)
 ┗ 🖼️ pro_5_output_3.png   ← Output screenshot 3 (Show Manager / Exit)
```

---

## 🔄 Project Workflow

```
START
  │
  ▼
┌─────────────────────────────────────┐
│        Main Menu (loop)             │
│  1. Create Person                   │
│  2. Create Employee                 │
│  3. Create Manager                  │
│  4. Show Details                    │
│  5. Exit                            │
└─────────────────────────────────────┘
  │         │         │         │
  ▼         ▼         ▼         ▼
Person   Employee  Manager   Display
(name,   (Person   (Employee  Sub-menu
 age)    + id,      + dept)  → choose
         salary)             record type
                               │
                               ▼
                         Print Details
                         via display()
```

**Class Hierarchy:**

```
Person
  └── Employee  (inherits Person)
        └── Manager  (inherits Employee)
```

Each class has:
- **Private attributes** (name mangling with `__`)
- **Setters** to assign values
- **Getters** to retrieve values
- **`display()`** method to print details (overridden in each class)

---

## 🛠️ Tech Stack

| Technology | Usage |
|---|---|
| 🐍 **Python 3.x** | Core programming language |
| 🧱 **OOP Concepts** | Classes, Inheritance, Encapsulation, Polymorphism |
| 💻 **CLI / Terminal** | Console-based interactive interface |
| 📦 **No external libraries** | Pure Python standard library only |

---

## 📸 Results & Insights

### 🖥️ Output 1 — Creating Person & Employee

![Output 1](pro_5_output_1.png)

> The user creates a **Person** (name: yashvi, age: 17) and an **Employee** (name: yashvi, age: 17, emp_id: e134, salary: 2000). Both records are created successfully through the interactive menu.

---

### 🖥️ Output 2 — Creating Manager & Viewing Records

![Output 2](pro_5_output_2.png)

> The user creates a **Manager** (same details + department: sales). Then using option 4, the Person and Employee details are displayed cleanly, showing the correct data stored via encapsulated attributes.

---

### 🖥️ Output 3 — Viewing Manager Details & Exiting

![Output 3](pro_5_output_3.png)

> The **Manager Details** are shown including all inherited fields (name, age, emp_id, salary) plus the manager-specific `Department: sales`. The user then exits with option 5, triggering the goodbye message.

**Key Insights:**
- Inheritance drastically reduces code repetition — `Manager` reuses all `Person` and `Employee` logic
- Encapsulation ensures data integrity — private attributes can only be accessed through controlled methods
- The `display()` override in each class is a clean example of **polymorphism in practice**

---

## ✅ Advantages

- ✔️ **Beginner-friendly** — simple menu-driven interface with no complex dependencies
- ✔️ **Demonstrates core OOP** — all four pillars (abstraction, encapsulation, inheritance, polymorphism) are present
- ✔️ **Extensible** — easily add new roles (e.g., `Director`, `Intern`) by extending existing classes
- ✔️ **Clean code structure** — each class has a single, well-defined responsibility
- ✔️ **No external libraries needed** — runs on any standard Python 3 installation
- ✔️ **Reusable pattern** — the getter/setter pattern used here mirrors real-world enterprise Java/Python codebases

---

## 📄 License

```
MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so.
```

---

## 👤 Author

<div align="center">

| Field | Details |
|---|---|
| 👩‍💻 **Name** | Yashvi |
| 🎓 **Project Type** | Python OOP Learning Project |
| 📘 **Topic** | Employee Management System |
| 🔢 **Project No.** | Project 5 |

</div>

---

## 🙏 Acknowledgements

- 💡 Inspired by classic **OOP design principles** taught in computer science fundamentals
- 📚 Thanks to the **Python documentation** for clear guidance on class design and name mangling
- 🧑‍🏫 Special thanks to all **educators and mentors** who promote learning through hands-on projects
- 🌐 Community resources like **GeeksforGeeks**, **W3Schools**, and **Real Python** for OOP references

---

<div align="center">

*Made with ❤️ using Python*

⭐ *If you found this project helpful, consider giving it a star!* ⭐

</div>
