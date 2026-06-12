
<div align="center">

# 🏢 Employee Management System
### Python OOP Project

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OOP](https://img.shields.io/badge/OOP-Concepts-FF6B6B?style=for-the-badge&logo=codeigniter&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-4CAF50?style=for-the-badge&logo=checkmarx&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

> *A Python-based Employee Management System demonstrating core OOP principles including Inheritance, Encapsulation, and Polymorphism.*

</div>

---

## 📚 Table of Contents

- [About the Project](#-about-the-project)
- [OOP Concepts Used](#-oop-concepts-used)
- [Class Hierarchy](#-class-hierarchy)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [How to Run](#-how-to-run)
- [Output Screenshots](#-output-screenshots)
- [Menu Flow Chart](#-menu-flow-chart)
- [Class Details](#-class-details)

---

## 🌟 About the Project

This project is a **console-based Employee Management System** built using **Python Object-Oriented Programming (OOP)** concepts. It manages three types of entities:

| Entity | Description |
|--------|-------------|
| 👤 **Person** | Base class with name and age |
| 👷 **Employee** | Inherits from Person; adds Employee ID and Salary |
| 🧑‍💼 **Manager** | Inherits from Employee; adds Department info |

---

## 🧩 OOP Concepts Used

```
✅ Encapsulation   — Private attributes with Getters & Setters
✅ Inheritance     — Person → Employee → Manager (Multi-level)
✅ Polymorphism    — display() method overridden in each class
✅ Abstraction     — Clean interface via methods
```

---

## 🌲 Class Hierarchy

```
        ┌──────────────────┐
        │      Person      │
        │  - __name        │
        │  - __age         │
        │  + set/get/display│
        └────────┬─────────┘
                 │  inherits
        ┌────────▼─────────┐
        │     Employee     │
        │  - __emp_id      │
        │  - __salary      │
        │  + set/get/display│
        └────────┬─────────┘
                 │  inherits
        ┌────────▼─────────┐
        │     Manager      │
        │  - __department  │
        │  + set/get/display│
        └──────────────────┘
```

---

## ✨ Features

- 🔐 **Private Attributes** — All data is encapsulated using name mangling (`__attribute`)
- 📝 **CRUD Operations** — Create and View records for Person, Employee, Manager
- 🔄 **Multi-Level Inheritance** — 3-level class hierarchy
- 🧾 **Interactive Menu** — Easy-to-use terminal interface
- 💡 **Method Overriding** — Each class has its own `display()` method
- 🔁 **Loop-Based Navigation** — Continuous interaction until user exits

---

## 📁 Project Structure

```
project_5/
│
├── 📄 project_5.py          # Main Python file
├── 🖼️ pro_5_output_1.png    # Output Screenshot 1
├── 🖼️ pro_5_output_2.png    # Output Screenshot 2
├── 🖼️ pro_5_output_3.png    # Output Screenshot 3
└── 📘 README.md             # This file
```

---

## ▶️ How to Run

```bash
# Clone or download the project
# Navigate to the project folder

python project_5.py
```

**Requirements:**
- Python 3.x (No external libraries needed)

---

## 📸 Output Screenshots

### 🖥️ Screenshot 1 — Creating Person, Employee & Manager

![Output 1](pro_5_output_1.png)

> 🟢 User creates a **Person** (choice 1), an **Employee** (choice 2), and begins creating a **Manager** (choice 3).

---

### 🖥️ Screenshot 2 — Completing Manager + Viewing Records

![Output 2](pro_5_output_2.png)

> 🟡 Manager is created with department "sales". Then records for **Person** and **Employee** are displayed using choice 4.

---

### 🖥️ Screenshot 3 — Viewing Manager Details & Exit

![Output 3](pro_5_output_3.png)

> 🔴 **Manager** details are displayed, then the user exits with choice 5. "Goodbye!" is printed.

---

## 🗺️ Menu Flow Chart

```
                    ┌─────────────────────┐
                    │       START         │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │   Show Menu (1-5)   │
                    └──────────┬──────────┘
                               │
          ┌────────────────────┼───────────────────┐
          │                    │                   │
    ┌─────▼──────┐      ┌──────▼─────┐      ┌─────▼──────┐
    │  Choice 1  │      │  Choice 2  │      │  Choice 3  │
    │  Create    │      │  Create    │      │  Create    │
    │  Person    │      │  Employee  │      │  Manager   │
    └─────┬──────┘      └──────┬─────┘      └─────┬──────┘
          │                    │                   │
          └────────────────────▼───────────────────┘
                               │
                    ┌──────────▼──────────┐
                    │     Choice 4?       │
                    │  Show Details Sub   │
                    │  Menu (1/2/3)       │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │     Choice 5?       │
                    │     Exit System     │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │    Print Goodbye    │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │        END          │
                    └─────────────────────┘
```

---

## 🔍 Class Details

### 👤 Person Class
| Method | Type | Description |
|--------|------|-------------|
| `set_name(name)` | Setter | Sets the person's name |
| `set_age(age)` | Setter | Sets the person's age |
| `get_name()` | Getter | Returns the name |
| `get_age()` | Getter | Returns the age |
| `display()` | Method | Prints person details |

### 👷 Employee Class *(extends Person)*
| Method | Type | Description |
|--------|------|-------------|
| `set_emp_id(emp_id)` | Setter | Sets employee ID |
| `set_salary(salary)` | Setter | Sets salary |
| `get_emp_id()` | Getter | Returns employee ID |
| `get_salary()` | Getter | Returns salary |
| `display()` | Method | Prints employee details (overrides Person) |

### 🧑‍💼 Manager Class *(extends Employee)*
| Method | Type | Description |
|--------|------|-------------|
| `set_department(dept)` | Setter | Sets the department |
| `get_department()` | Getter | Returns the department |
| `display()` | Method | Prints manager details (overrides Employee) |

---

## 📊 OOP Concept Summary Chart

| Concept | Used | Where |
|---------|------|-------|
| 🔐 Encapsulation | ✅ Yes | Private `__attributes` in all classes |
| 🧬 Inheritance | ✅ Yes | Person → Employee → Manager |
| 🔄 Polymorphism | ✅ Yes | `display()` method in all 3 classes |
| 🧩 Abstraction | ✅ Yes | Getter/Setter methods hide internal data |
| 🏗️ Constructor | ⚠️ Note | `_init_` used (should be `__init__`) |

> ⚠️ **Note:** The `_init_` method in the code should ideally be `__init__` for proper constructor behavior. The code works because Python calls `__init__` automatically on object creation, and the setters initialize the values before use.

---

## 👩‍💻 Author

> **Created by:** Yashvi  
> **Project:** Python OOP — Employee Management System  
> **Language:** Python 3.x  

---

<div align="center">

### ⭐ If you found this project helpful, give it a star!

![Footer](https://img.shields.io/badge/Made%20with-❤️%20Python-blue?style=for-the-badge)

</div>
