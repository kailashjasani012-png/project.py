<div align="center">

# 📔 Personal Journal Manager

### *Interactive Console-Based Journal with File Handling in Python*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![File I/O](https://img.shields.io/badge/File%20I%2FO-Read%2FWrite%2FDelete-FF6F00?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![OOP](https://img.shields.io/badge/OOP-Class%20%26%20Methods-4CAF50?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Console](https://img.shields.io/badge/Console-Interactive%20CLI-9C27B0?style=for-the-badge&logo=windowsterminal&logoColor=white)](https://www.python.org/)

<br/>

> *"A journal is a mirror of your thoughts — code it, save it, and search it anytime."*

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [📝 Feature Breakdown](#-feature-breakdown)
- [🖥️ Output Screenshots](#️-output-screenshots)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Insights](#-results--insights)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 📌 Overview

The **Personal Journal Manager** is a beginner-friendly, interactive Python console application that demonstrates core programming concepts such as **file handling**, **object-oriented programming (OOP)**, **exception handling**, **user input management**, and **string operations**. The program presents a menu-driven interface that runs continuously until the user chooses to exit.

This project is designed to:
- Strengthen understanding of Python **file I/O** — read, write, append, and delete
- Practice **OOP** with a clean `JournalManager` class and methods
- Apply **exception handling** for robust and crash-safe operations
- Use **timestamp-based entries** to simulate a real journal experience

---

## 🎯 Problem Statement

> **Objective:** Build a console-based interactive personal journal that lets users add, view, search, and delete entries using Python file handling.

You are building a text-based journal utility for everyday use. The program must accept user choices from a menu and execute the corresponding task — adding a new entry with a timestamp, viewing all saved entries, searching by keyword or date, or deleting all journal entries.

| 📂 Feature | 📄 Type | 🔍 Description |
|------------|---------|----------------|
| Add Entry | File Write (Append) | Writes a timestamped entry to `journal.txt` |
| View Entries | File Read | Reads and displays all saved entries |
| Search Entry | File Read + Filter | Searches entries by keyword or date |
| Delete Entries | File Delete | Removes the journal file after confirmation |
| Menu System | Loop + Conditionals | Continuously shows options until Exit is selected |

The goal is to demonstrate **file handling and OOP in Python** through a clean, menu-driven interactive program.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 🔁 **Infinite Menu Loop** | Program runs continuously until user selects Exit |
| 📝 **Add Journal Entry** | Appends a new entry with auto-generated timestamp |
| 📖 **View All Entries** | Reads and displays all entries from the journal file |
| 🔍 **Search by Keyword/Date** | Finds entries matching a user-provided keyword |
| 🗑️ **Delete All Entries** | Deletes the journal file after user confirmation |
| 🕒 **Auto Timestamp** | Every entry is tagged with `YYYY-MM-DD HH:MM:SS` format |
| ⚠️ **Exception Handling** | Handles `FileNotFoundError`, `PermissionError`, and general exceptions |
| ✅ **Confirmation Prompt** | Deletion requires typing `yes` to confirm — prevents accidental loss |
| 🏗️ **OOP Design** | Entire logic wrapped in a `JournalManager` class |

---

## 🏗️ Project Structure

```
📦 personal-journal-manager/
│
├── 📄 project_6.py          ← Main Python script (entry point)
├── 📄 journal.txt           ← Auto-generated journal file (created on first entry)
│
└── 📄 README.md             ← Project documentation
```

---

## 🔄 Project Workflow

```
Program Start
      │
      ▼
┌─────────────────────────────┐
│     Display Main Menu       │  ← Options: Add / View / Search / Delete / Exit
└────────────┬────────────────┘
             │
    ┌────────┼────────┬──────────┐
    ▼        ▼        ▼          ▼
┌───────┐ ┌───────┐ ┌────────┐ ┌────────┐
│  1    │ │  2    │ │   3    │ │   4    │
│ Add   │ │ View  │ │ Search │ │ Delete │
│ Entry │ │ All   │ │ Entry  │ │ All    │
└──┬────┘ └───┬───┘ └───┬────┘ └───┬────┘
   │          │         │          │
   ▼          ▼         ▼          ▼
Append    Read file   Filter    Confirm
to file   & display  entries   & remove
   │          │         │       journal.txt
   └──────────┴─────────┴──────────┘
                   │
                   ▼
          Loop Back to Menu
                   │
           (Choice: 5) Exit ✅
```

---

## 📝 Feature Breakdown

### ✍️ 1. Add a New Entry

> Prompts the user for a journal entry and saves it with a timestamp.

**Logic:**
```python
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open(self.filename, "a", encoding="utf-8") as file:
    file.write(f"[{timestamp}]")
    file.write(entry + "")
    file.write("-" * 40 + "\n")
```

**Key Concepts:**
| Concept | Detail |
|---------|--------|
| `open(..., "a")` | Append mode — adds to file without erasing existing content |
| `datetime.now()` | Gets current system time |
| `strftime(...)` | Formats timestamp as `YYYY-MM-DD HH:MM:SS` |
| Separator line | `"-" * 40` creates a visual divider between entries |

---

### 📖 2. View All Entries

> Reads the entire journal file and displays all saved entries.

**Logic:**
```python
with open(self.filename, "r", encoding="utf-8") as file:
    content = file.read()
    if content.strip():
        print(content)
    else:
        print("No journal entries found.")
```

**Key Concepts:**
| Concept | Detail |
|---------|--------|
| `open(..., "r")` | Read mode — opens file for reading |
| `file.read()` | Reads entire file content as a string |
| `content.strip()` | Checks if file is not empty or blank |
| `FileNotFoundError` | Caught if journal file doesn't exist yet |

---

### 🔍 3. Search for an Entry

> Searches entries by matching a keyword or date against each entry block.

**Logic:**
```python
for line in lines:
    temp_entry += line
    if "-" * 40 in line:
        if keyword in temp_entry.lower():
            matching_entries.append(temp_entry)
        temp_entry = ""
```

**Key Concepts:**
| Concept | Detail |
|---------|--------|
| `file.readlines()` | Reads file line by line into a list |
| Entry block detection | Each entry ends with a `"----"` separator |
| `.lower()` | Case-insensitive keyword matching |
| Accumulator pattern | Builds each entry in `temp_entry` before checking |

---

### 🗑️ 4. Delete All Entries

> Deletes the journal file after the user confirms with `yes`.

**Logic:**
```python
if os.path.exists(self.filename):
    confirm = input("Are you sure? (yes/no): ").lower()
    if confirm == "yes":
        os.remove(self.filename)
```

**Key Concepts:**
| Concept | Detail |
|---------|--------|
| `os.path.exists()` | Checks if the file exists before attempting deletion |
| `os.remove()` | Permanently deletes the file |
| Confirmation input | Prevents accidental deletion |
| `PermissionError` | Caught if file is locked by another process |

---

## 🖥️ Output Screenshots

### 📸 Screenshot 1 — Adding an Entry & Viewing All Entries

> User adds a new journal entry, then views all saved entries in the journal.

![Add and View Entry](output_1.png)

---

### 📸 Screenshot 2 — Viewing Entries & Searching by Keyword

> All entries are displayed, followed by a keyword search returning the matching entry.

![View and Search Entry](output_2.png)

---

### 📸 Screenshot 3 — Deleting All Entries & Error Handling

> User confirms deletion, then tries to view — correctly shows file-not-found error. Invalid menu input (6) is also handled.

![Delete and Error Handling](output_3.png)

---

### 📸 Screenshot 4 — Invalid Input & Graceful Exit

> Program handles invalid input gracefully and exits cleanly with a goodbye message.

![Exit Output](output_4.png)

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| 🐍 **Python** | 3.8+ | Core programming language |
| 📁 **os module** | Built-in | File existence check and deletion |
| 🕒 **datetime module** | Built-in | Auto-generating timestamps for entries |
| 📖 **File I/O** | Built-in | Reading, writing, and appending to `journal.txt` |
| 🏗️ **OOP (Class)** | Built-in | `JournalManager` class encapsulates all functionality |
| 🛡️ **Exception Handling** | Built-in | `try/except` for robust error management |
| 🖨️ **print() / input()** | Built-in | Console I/O and user interaction |

---

## 📈 Results & Insights

After running the program, the following outputs are produced:

- ✅ **Timestamped Entries** — Every journal entry is saved with an exact date and time
- 📖 **Full View** — All entries are displayed clearly with separator lines
- 🔍 **Keyword Search** — Finds and displays only entries containing the searched word or date
- 🗑️ **Safe Deletion** — Entries are deleted only after explicit user confirmation
- ⚠️ **Error Feedback** — File-not-found, invalid input, and permission errors all handled gracefully
- 🔁 **Persistent Menu** — Program loops back after every task until manually exited

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🎓 **Beginner Friendly** | Covers file I/O, OOP, and exception handling in one project |
| 🏗️ **OOP Design** | Clean class-based structure — easy to extend or reuse |
| 🛡️ **Crash Safe** | All file operations are wrapped in `try/except` blocks |
| 🕒 **Auto Timestamps** | Entries are automatically dated — no manual input needed |
| 📚 **Educational** | Demonstrates `open()`, `os.remove()`, `readlines()`, and `datetime` |
| 🖥️ **No Dependencies** | Runs with pure Python — no external libraries needed |
| ⚡ **Lightweight** | Single-file script, instantly runnable from any terminal |
| 🧪 **Extensible** | Easy to add features like edit entry, export to PDF, or date filter |

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for full details.

```
MIT License — Free to use, modify, and distribute with attribution.
```

---

## 👤 Author

<div align="center">

### Ayush Isamaliya

[![GitHub](https://img.shields.io/badge/GitHub-isamaliya16-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/isamaliya16)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ayush-isamaliya-686533312/)

> *"Every journal entry starts with one line — just like every program starts with a single print."*

**🎓 Role:** Junior Python Developer | Programming Enthusiast \
**📍 Location:** India\
**🛠️ Skills:** Python · File Handling · OOP · CLI Applications · Exception Handling

</div>

---

## 🙏 Acknowledgements

Special thanks to the following resources and communities that made this project possible:

- 📚 [Python Official Docs](https://docs.python.org/3/) — Official Python language reference
- 📁 [Real Python — File I/O](https://realpython.com/read-write-files-python/) — In-depth file handling tutorials
- 🏗️ [Real Python — OOP](https://realpython.com/python3-object-oriented-programming/) — Object-oriented programming in Python
- 🛡️ [GeeksForGeeks — Exception Handling](https://www.geeksforgeeks.org/python-exception-handling/) — Error handling patterns
- 🖥️ [W3Schools Python](https://www.w3schools.com/python/) — Beginner Python reference
- 🕒 [Python datetime Docs](https://docs.python.org/3/library/datetime.html) — Datetime module reference
- 💬 [Stack Overflow Community](https://stackoverflow.com/) — Problem-solving support
- 📖 [Kaggle Learn](https://www.kaggle.com/learn) — Python and programming courses

---

<div align="center">

---

*Made with ❤️ and ☕ — Last updated: June 2026*

</div>
