
<div align="center">

# 🎓 Student Data Organizer

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)
![Type](https://img.shields.io/badge/Type-CLI%20App-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)

> 📋 **A Python-based command-line application to manage student records with full CRUD operations.**

</div>

---

## 📌 Table of Contents

- [📖 About](#-about)
- [✨ Features](#-features)
- [🛠️ Tech Stack](#️-tech-stack)
- [🚀 How to Run](#-how-to-run)
- [📂 Project Structure](#-project-structure)
- [🖥️ Output Screenshots](#️-output-screenshots)
- [🧠 Concepts Used](#-concepts-used)

---

## 📖 About

The **Student Data Organizer** is an interactive terminal-based application built in Python. It allows users to **add**, **view**, **update**, and **delete** student records, as well as track all subjects offered across enrolled students.

---

## ✨ Features

| # | Feature | Description |
|---|---------|-------------|
| 1 | ➕ **Add Student** | Enter full student details including ID, name, age, grade, DOB, and subjects |
| 2 | 📋 **Display All Students** | View all stored student records in a formatted list |
| 3 | ✏️ **Update a Student** | Modify an existing student's details by their ID |
| 4 | 🗑️ **Delete a Student** | Remove a student record permanently by their ID |
| 5 | 📚 **Display Subjects Offered** | View the unique set of all subjects across students |
| 6 | 🚪 **Exit** | Cleanly exit the program |

---

## 🛠️ Tech Stack

- 🐍 **Language:** Python 3.10+
- 🔧 **Data Structures Used:**
  - `list` — stores student records
  - `dict` — represents individual student objects
  - `tuple` — groups immutable student info (ID + DOB)
  - `set` — tracks unique subjects offered

---

## 🚀 How to Run

```bash
# Clone the repository
git clone https://github.com/your-username/student-data-organizer.git

# Navigate to the project folder
cd student-data-organizer

# Run the program
python project_3.py
```

> ✅ No external libraries required. Just plain Python!

---

## 📂 Project Structure

```
student-data-organizer/
│
├── project_3.py        # Main application file
├── README.md           # Project documentation
└── outputs/
    ├── pro3_output_1.png
    ├── pro3_output_2.png
    └── pro3_output_3.png
```

---

## 🖥️ Output Screenshots

### 🟢 Output 1 — Adding a Student & Displaying Records

> Demonstrated adding student **Yashvi** (ID: 101) with subjects Hindi, Gujarati, English — then displaying all students.

![Output 1](pro3_output_1.png)

---

### 🟡 Output 2 — Updating & Deleting a Student + Viewing Subjects

> Updated student ID 101's name to **Charmi** with new grade and subjects → Deleted student 101 → Displayed subjects offered (science, math, gujarati).

![Output 2](pro3_output_2.png)

---

### 🔴 Output 3 — Subjects Offered & Exit

> Final view of all unique subjects stored in the set, followed by a clean exit.

![Output 3](pro3_output_3.png)

---

## 🧠 Concepts Used

```python
✅ while True loop with match-case (Python 3.10+)
✅ list  →  storing multiple student dicts
✅ dict  →  each student as key-value pairs
✅ tuple →  grouping student_id + dob as immutable pair
✅ set   →  automatically tracks unique subjects
✅ List comprehension for subject parsing
✅ f-strings for formatted output
```

---

<div align="center">

### 💡 Made with ❤️ using Python

*Feel free to fork, star ⭐, and contribute!*

</div>
