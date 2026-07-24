<div align="center">

# -- ! Retail Sales Analyzer ! --
### *Menu-Driven Python Project for Retail Sales Data Analysis using Pandas, NumPy & Visualization*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge&logo=plotly&logoColor=white)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-4C8CBF?style=for-the-badge&logo=python&logoColor=white)](https://seaborn.pydata.org/)

<br/>

> *"Data is only powerful when it tells a story — this project turns raw sales numbers into insights."*

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [🗂️ Dataset Description](#️-dataset-description)
- [⚙️ Module-wise Functionality](#️-module-wise-functionality)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Insights](#-results--insights)
- [🏆 Advantages](#-advantages)
- [🚀 How to Run](#-how-to-run)
- [📄 License](#-license)
- [👤 Author](#-author)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 📌 Overview

The **Retail Sales Analyzer** is a menu-driven Python project built using **Object-Oriented Programming** that reads, cleans, analyzes, and visualizes retail sales data using **Pandas**, **NumPy**, **Matplotlib**, and **Seaborn**. The program presents an interactive text menu that keeps running until the user chooses to exit, allowing repeated exploration of the dataset.

This project is designed to:
- Strengthen understanding of **Pandas** DataFrames and data cleaning techniques
- Apply **NumPy** for statistical computation (sum, mean, max, min, standard deviation)
- Practice **OOP concepts** using a dedicated `RetailAnalyzer` class
- Build **data visualizations** using Matplotlib and Seaborn (bar chart, line chart, heatmap)

---

## 🎯 Problem Statement

> **Objective:** Build an interactive console-based tool to load, clean, analyze, and visualize retail sales data.

A retail business generates a dataset of daily product sales with occasional missing values. The program must load this dataset, handle missing data, compute key sales metrics, filter records by category, generate a statistical summary, and visualize sales trends — all through a simple, menu-driven interface.

| 📂 Feature | 📄 Type | 🔍 Description |
|------------|---------|----------------|
| Load Dataset | Data I/O | Reads `retail_sales.csv` into a Pandas DataFrame |
| Missing Value Handling | Data Cleaning | Detects and fills missing values in each column |
| Sales Metrics | Analysis | Computes total, average, max, min sales & top product |
| NumPy Analysis | Statistics | Uses NumPy for sum, mean, max, min & standard deviation |
| Filter by Category | Query | Filters records matching a user-given category |
| Visualization | Charts | Bar chart, line chart, and correlation heatmap |

The goal is to demonstrate **practical data analysis skills** through a clean, class-based, menu-driven Python program.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 🔁 **Infinite Menu Loop** | Program runs continuously until user selects Exit |
| 📥 **Dataset Loading** | Loads `retail_sales.csv` safely with file-existence check |
| 🧹 **Missing Value Handling** | Detects nulls and fills them using mean/default values |
| 📊 **Sales Metrics Report** | Total, Average, Maximum, Minimum Sales & Most Popular Product |
| 🔢 **NumPy Statistical Analysis** | Sum, Mean, Max, Min, and Standard Deviation using NumPy arrays |
| 📐 **Sales Percentage** | Adds a new column showing each sale's contribution to total sales |
| 🔍 **Category-wise Filtering** | Filters and displays records for a chosen category |
| 📋 **Dataset Summary** | Shape, columns, data types, info, and statistical description |
| 📈 **Data Visualization** | Bar chart, line chart, and correlation heatmap using Matplotlib & Seaborn |
| 🛡️ **Safe Execution** | Handles "No data loaded" and "No Record Found" cases gracefully |

---

## 🏗️ Project Structure

```
📦 retail-sales-analyzer/
│
├── 📄 Data.ipynb            ← Main Jupyter Notebook (entry point)
├── 📄 retail_sales.csv      ← Retail sales dataset
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
│   Display Main Menu         │  ← 12 Options: Load / Analyze / Visualize / Exit
└────────────┬────────────────┘
             │
     ┌───────┴─────────────────────────────┐
     ▼                                      ▼
┌──────────────────┐               ┌──────────────────────┐
│  Load & Clean     │               │   Analyze & Filter    │
│  (Options 1-4)    │               │   (Options 5-9)       │
└─────────┬─────────┘               └──────────┬────────────┘
          │                                    │
          ▼                                    ▼
┌──────────────────┐               ┌──────────────────────┐
│ Load CSV          │               │ Metrics / NumPy /     │
│ Check & Fill Nulls │               │ Percentage / Filter   │
└─────────┬─────────┘               └──────────┬────────────┘
          │                                    │
          └───────────────┬────────────────────┘
                           ▼
                ┌──────────────────────┐
                │ Display / Visualize   │
                │ (Options 10-11)       │
                └──────────┬─────────────┘
                           │
                           ▼
                  Loop Back to Menu
                           │
                  (Choice: 12) Exit ✅
```

---

## 🗂️ Dataset Description

The dataset `retail_sales.csv` contains **1000 records** of daily retail transactions.

| Column | Type | Description |
|--------|------|--------------|
| `Date` | str | Date of the transaction |
| `Product` | str | Product name (e.g., Jeans, Chair, Watch, Sofa) |
| `Category` | str | Product category (Fashion, Furniture, Accessories, etc.) |
| `Price` | float64 | Unit price of the product |
| `Quantity Sold` | float64 | Number of units sold |
| `Total Sales` | float64 | Total sales value (Price × Quantity Sold) |
| `Sales Percentage` | float64 | Contribution of each sale to total sales (added at runtime) |

**Sample Record:**
```
Date         Product   Category      Price   Quantity Sold   Total Sales
2025-01-01   Jeans     Fashion       1500.0  10.0             15000.0
```

---

## ⚙️ Module-wise Functionality

### 1️⃣ Load Dataset
Reads `retail_sales.csv` into a Pandas DataFrame using `pd.read_csv()`, with a file-existence check to avoid runtime errors.

### 2️⃣ Display Dataset
Prints the first 5 records of the dataset using `.head()`.

### 3️⃣ Check Missing Values
Uses `.isnull().sum()` to report the number of missing values per column.

### 4️⃣ Fill Missing Values
Fills numeric columns (`Price`, `Quantity Sold`, `Total Sales`) with their **mean**, and text columns (`Product`, `Category`, `Date`) with default placeholder values.

### 5️⃣ Calculate Sales Metrics
Computes **Total Sales**, **Average Sales**, **Maximum Sale**, **Minimum Sale**, and the **Most Popular Product** using `.sum()`, `.mean()`, `.max()`, `.min()`, and `.mode()`.

### 6️⃣ NumPy Analysis
Converts the `Total Sales` column into a NumPy array and computes `np.sum()`, `np.mean()`, `np.max()`, `np.min()`, and `np.std()`.

### 7️⃣ Sales Percentage
Adds a new `Sales Percentage` column showing each transaction's share of the overall total sales.

### 8️⃣ Filter Data
Filters and displays all records matching a user-entered category (e.g., "Furniture").

### 9️⃣ Dataset Summary
Displays dataset **shape**, **columns**, **data types**, `.info()` output, and `.describe()` statistical summary.

### 🔟 Display Updated Dataset
Shows the first 10 rows of the dataset after cleaning and the added `Sales Percentage` column.

### 1️⃣1️⃣ Data Visualization
Generates three visual insights using **Matplotlib** and **Seaborn**:
- 📊 **Bar Chart** — Total Sales grouped by Category
- 📈 **Line Chart** — Total Sales trend across records
- 🔥 **Heatmap** — Correlation between numeric columns

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| 🐍 **Python 3.8+** | Core programming language |
| 🐼 **Pandas** | Data loading, cleaning, and analysis |
| 🔢 **NumPy** | Statistical computation on sales data |
| 📊 **Matplotlib** | Bar chart and line chart visualization |
| 🌊 **Seaborn** | Correlation heatmap |
| 🧩 **OOP (Class-based Design)** | `RetailAnalyzer` class encapsulating all functionality |
| 🖥️ **Jupyter Notebook** | Interactive development and execution environment |

---

## 📈 Results & Insights

After running the analyzer on the dataset, the following insights are produced:

- 💰 **Total Sales:** ₹79,011,831.57 across 1000 transactions
- 📊 **Average Sales:** ₹79,011.83 per transaction
- 🔺 **Maximum Sale:** ₹1,000,000.00
- 🔻 **Minimum Sale:** ₹20.00
- 🏆 **Most Popular Product:** Bag
- 📐 **Standard Deviation:** ₹149,076.76 — indicating high variability in sale amounts
- 🧹 **50 missing values** detected and successfully cleaned in every column

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🎓 **Practical Data Analysis** | Combines cleaning, statistics, and visualization in one workflow |
| 🧩 **OOP-based Design** | Clean, reusable, and well-organized class structure |
| 🔄 **Reusability** | Each analysis step is a standalone method that can be reused independently |
| 📚 **Educational** | Demonstrates real-world use of Pandas, NumPy, Matplotlib, and Seaborn together |
| 🖥️ **Interactive Menu** | Lets users explore the dataset step-by-step at their own pace |
| ⚡ **Robust Error Handling** | Gracefully handles missing data and empty filter results |
| 🧪 **Extensible** | Easy to add new metrics, filters, or chart types |
| 📖 **Readable Code** | Clear method-wise separation makes the logic easy to follow |

---

## 🚀 How to Run

1. Make sure **Python 3.8+**, **Pandas**, **NumPy**, **Matplotlib**, and **Seaborn** are installed:
   ```bash
   pip install pandas numpy matplotlib seaborn
   ```
2. Keep `retail_sales.csv` in the same folder as `Data.ipynb`.
3. Open `Data.ipynb` in **Jupyter Notebook / JupyterLab**.
4. Run all cells and follow the on-screen menu to explore the dataset.

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for full details.

```
MIT License — Free to use, modify, and distribute with attribution.
```

---

## 👤 Author

<div align="center">

### Yashvi Jasani

> *"Every dataset has a story — analysis is how we let it speak."*

**🎓 Role:** Python Developer | Data Analysis Enthusiast \
**📍 Location:** India\
**🛠️ Skills:** Python · Pandas · NumPy · Data Visualization · OOP

</div>

---

## 🙏 Acknowledgements

Special thanks to the following resources and communities that made this project possible:

- 📚 [Python Official Docs](https://docs.python.org/3/) — Official Python language reference
- 🐼 [Pandas Documentation](https://pandas.pydata.org/docs/) — Data analysis and manipulation
- 🔢 [NumPy Documentation](https://numpy.org/doc/) — Numerical computing reference
- 📊 [Matplotlib Documentation](https://matplotlib.org/stable/index.html) — Visualization reference
- 🌊 [Seaborn Documentation](https://seaborn.pydata.org/) — Statistical data visualization
- 💬 [Stack Overflow Community](https://stackoverflow.com/) — Problem-solving support
- 📖 [Kaggle Learn](https://www.kaggle.com/learn) — Python and data analysis courses

---

<div align="center">

---

*Made with ❤️ and ☕ — Last updated: 18 July, 2026*

</div>
