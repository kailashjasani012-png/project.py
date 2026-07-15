<div align="center">

# -- ! Sales Data Analyzer ! --
### *Interactive Console-Based Sales Data Analysis & Visualization Tool*

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-DataFrames-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Numpy](https://img.shields.io/badge/Numpy-Arrays-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge&logo=plotly&logoColor=white)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-4C72B0?style=for-the-badge)](https://seaborn.pydata.org/)
[![Console](https://img.shields.io/badge/Console-Interactive%20CLI-4CAF50?style=for-the-badge&logo=windowsterminal&logoColor=white)](https://www.python.org/)

<br/>

> *"Behind every good decision is a dataset that was explored properly."*

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [📂 Dataset](#-dataset)
- [🔍 Part A — Data Loading & Exploration](#-part-a--data-loading--exploration)
- [🧹 Part B — Data Cleaning](#-part-b--data-cleaning)
- [🧮 Part C — DataFrame & Numpy Operations](#-part-c--dataframe--numpy-operations)
- [📊 Part D — Statistical Analysis](#-part-d--statistical-analysis)
- [📈 Part E — Data Visualization](#-part-e--data-visualization)
- [🛠️ Tech Stack](#️-tech-stack)
- [▶️ How to Run](#️-how-to-run)
- [📈 Results & Insights](#-results--insights)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 📌 Overview

The **Sales Data Analyzer** is an interactive, menu-driven Python console application built around an object-oriented `SalesDataAnalyzer` class. It loads sales data from a CSV file and lets the user explore, clean, transform, analyze, and visualize it — all through a simple text-based menu, without ever touching a Jupyter cell manually.

This project is designed to:
- Demonstrate real-world use of **Pandas** for data loading, cleaning, and transformation
- Apply **Numpy** for array creation, indexing, slicing, and vectorized math
- Practice **object-oriented programming** (constructors, destructors, encapsulated methods)
- Build **Matplotlib** and **Seaborn** visualizations directly from user choices
- Provide a reusable, menu-driven workflow for analyzing any tabular sales dataset

---

## 🎯 Problem Statement

> **Objective:** Build a console-based interactive tool to load, clean, analyze, and visualize sales data end-to-end.

You are building a data analysis utility for a sales dataset containing transaction-level records (product, region, sales, profit, and date). The program must let a user load the dataset, explore its structure, handle missing values, perform statistical and DataFrame operations, and generate a variety of charts — all driven from a single main menu.

| 📂 Feature | 📄 Type | 🔍 Description |
|------------|---------|----------------|
| Data Loader | I/O | Loads a CSV file or generates a synthetic dataset |
| Data Explorer | Inspection | Shows head, tail, columns, dtypes, and info |
| Data Cleaner | Preprocessing | Detects and handles missing values |
| DataFrame Ops | Transformation | Combine, split, search, sort, filter, aggregate, pivot |
| Statistical Analyzer | Analytics | Describe, std, variance, percentiles |
| Visualizer | Charts | Bar, line, scatter, pie, histogram, stack, heatmap, box plot, subplots |

The goal is to demonstrate **practical data-analysis skills** through a clean, class-based, menu-driven program.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 🔁 **Infinite Menu Loop** | Program runs continuously until user selects Exit |
| 🏗️ **Object-Oriented Design** | Core logic encapsulated inside the `SalesDataAnalyzer` class |
| 📥 **Flexible Data Loading** | Load an existing CSV or auto-generate a synthetic sales dataset |
| 🔍 **Data Exploration** | Head, tail, column list, dtypes, and full `.info()` / `.describe()` |
| 🧹 **Missing Value Handling** | View, mean-fill, drop, or replace missing values |
| 🔢 **Numpy Integration** | Convert columns to arrays; demonstrate indexing & slicing |
| ➕ **Vectorized Math** | Add, subtract, multiply, or divide a column by a constant |
| 🔗 **Combine / Split Data** | Concat, merge, or join datasets; split by category column |
| 🔎 **Search, Sort & Filter** | Query rows by value, sort by column, filter with operators |
| 📊 **Aggregate Functions** | Sum, mean, count, min, max on any numeric column |
| 📐 **Pivot Tables** | Summarize data with custom index/columns/values/aggfunc |
| 📈 **9 Chart Types** | Bar, Line, Scatter, Pie, Histogram, Stack, Heatmap, Box Plot, Subplots |
| 💾 **Save Visualizations** | Export the last generated plot to an image file |
| ⚠️ **Robust Error Handling** | Graceful messages for missing files, bad columns, and invalid choices |

---

## 🏗️ Project Structure

```
📦 sales-data-analyzer/
│
├── 📓 sales_Data_analyzer.ipynb   ← Main notebook (SalesDataAnalyzer class + menu)
├── 📄 sales_data.csv              ← Sample sales dataset (input)
│
└── 📄 README.md                   ← Project documentation
```

---

## 🔄 Project Workflow

```
Program Start
      │
      ▼
┌─────────────────────────────┐
│   Display Main Menu         │  ← 8 top-level options
└────────────┬────────────────┘
             │
   ┌─────────┼───────────┬───────────┬───────────┬────────────┬──────────────┬────────┐
   ▼         ▼            ▼           ▼           ▼            ▼              ▼        ▼
┌────────┐┌─────────┐┌───────────┐┌──────────┐┌────────────┐┌─────────────┐┌────────┐┌──────┐
│ Load   ││ Explore ││ DataFrame ││ Handle   ││ Descriptive││ Visualize   ││ Save   ││ Exit │
│ Dataset││ Data    ││ Operations││ Missing  ││ Statistics ││ Data        ││ Plot   ││  ✅  │
└───┬────┘└────┬────┘└─────┬─────┘└────┬─────┘└──────┬─────┘└──────┬──────┘└───┬────┘└──────┘
    │          │           │           │             │             │           │
    ▼          ▼           ▼           ▼             ▼             ▼           ▼
  CSV /     head/tail/  Numpy/Math/  view/fillna/  describe/std/  9 chart    Export
  synthetic  dtypes/    combine/     drop/replace   var/quantile  types      last figure
  dataset    info       split/...                                (matplotlib/
                                                                    seaborn)
             │
             ▼
     Loop Back to Menu
```

---

## 📂 Dataset

The bundled `sales_data.csv` contains transaction-level sales records with the following columns:

| Column | Type | Description |
|--------|------|--------------|
| `SalesID` | Integer | Unique identifier for each transaction |
| `Date` | Date | Transaction date |
| `Product` | Categorical | Product name (Product A–E) |
| `Region` | Categorical | Sales region (North, South, East, West Coast, Central) |
| `Sales` | Numeric | Sales amount (contains some missing values) |
| `Profit` | Numeric | Profit earned on the transaction |
| `Year` | Integer | Year extracted from the transaction date |

> The program can also **auto-generate a synthetic version** of this dataset via `generate_synthetic_dataset()` if no CSV is available.

---

## 🔍 Part A — Data Loading & Exploration

### 📝 1. Loading the Dataset

The `load_data()` method reads a CSV into a Pandas DataFrame with full exception handling for missing files and empty files.

**Logic:**
```python
def load_data(self, file_path: str) -> None:
    try:
        self.data = pd.read_csv(file_path)
        print(f"Dataset loaded successfully from '{file_path}'!")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
```

### 🗺️ 2. Exploring the Dataset

The `explore_data()` sub-menu offers a quick inspection toolkit:

| Option | Action |
|--------|--------|
| 1 | Display the first 5 rows (`head()`) |
| 2 | Display the last 5 rows (`tail()`) |
| 3 | Display column names |
| 4 | Display data types |
| 5 | Display full info + `describe(include='all')` |

---

## 🧹 Part B — Data Cleaning

> Handled entirely through the `clean_data()` sub-menu.

| Option | Action |
|--------|--------|
| 1 | Display rows containing missing values |
| 2 | Fill missing numeric values with the column mean |
| 3 | Drop rows containing missing values |
| 4 | Replace missing values with a user-specified value |

**Example — mean fill:**
```python
numeric_cols = self.data.select_dtypes(include=np.number).columns
self.data[numeric_cols] = self.data[numeric_cols].apply(
    lambda col: col.fillna(col.mean())
)
```

---

## 🧮 Part C — DataFrame & Numpy Operations

### 🔢 3. Numpy Array Operations

Converts any numeric column to a Numpy array and demonstrates indexing/slicing (`arr[0]`, `arr[-1]`, `arr[:3]`, `arr[::2]`).

### ➕ 4. Mathematical Operations

Applies a constant to an entire column via vectorized Numpy math — add, subtract, multiply, or divide.

### 🔗 5. Combine, Split, Search, Sort, Filter

| Function | Description |
|----------|--------------|
| `combine_data()` | Concat, merge, or join with another CSV |
| `split_data()` | Group and split the DataFrame by a chosen column |
| `search_sort_filter()` | Search by value, sort ascending/descending, filter with `==`, `!=`, `>`, `<`, `>=`, `<=` |

### 📐 6. Aggregate Functions & Pivot Tables

`aggregate_functions()` computes sum, mean, count, min, and max on any numeric column, while `create_pivot_table()` builds a custom pivot summary using `pd.pivot_table()`.

---

## 📊 Part D — Statistical Analysis

`statistical_analysis()` reports descriptive statistics for a chosen numeric column:

```python
print(series.describe())
print(f"Standard Deviation: {series.std()}")
print(f"Variance: {series.var()}")
print(f"25th percentile: {series.quantile(0.25)}")
print(f"50th percentile (median): {series.quantile(0.50)}")
print(f"75th percentile: {series.quantile(0.75)}")
```

---

## 📈 Part E — Data Visualization

The `visualize_data()` sub-menu supports **9 chart types**, each rendered with Matplotlib or Seaborn and cached in `self.last_figure` for export:

| # | Chart Type | Library |
|---|------------|---------|
| 1 | Bar Plot | Matplotlib |
| 2 | Line Plot | Matplotlib |
| 3 | Scatter Plot | Matplotlib |
| 4 | Pie Chart | Matplotlib |
| 5 | Histogram | Matplotlib |
| 6 | Stack Plot | Matplotlib |
| 7 | Correlation Heatmap | Seaborn |
| 8 | Box Plot | Seaborn |
| 9 | Multiple Subplots | Matplotlib |

The last generated figure can be exported at any time through `save_visualization()`, which saves it to a filename of your choice (e.g., `plot.png`).

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| 🐍 **Python 3.10+** | Core programming language (uses `match-case`) |
| 🐼 **Pandas** | DataFrame loading, cleaning, transformation, aggregation |
| 🔢 **Numpy** | Array creation, indexing, slicing, vectorized math |
| 📊 **Matplotlib** | Bar, line, scatter, pie, histogram, stack plot, subplots |
| 🎨 **Seaborn** | Correlation heatmap, box plot |
| 🖨️ **input() / print()** | Console I/O and interactive menu navigation |
| 🧱 **OOP** | Encapsulated logic inside the `SalesDataAnalyzer` class |

---

## ▶️ How to Run

1. Install the required libraries:
   ```bash
   pip install pandas numpy matplotlib seaborn
   ```
2. Open `sales_Data_analyzer.ipynb` in Jupyter Notebook / JupyterLab (or run the extracted script).
3. Run the main cell — the interactive menu will appear in the output/console.
4. Choose **Option 1 → Load from an existing CSV file**, and enter the path to `sales_data.csv`.
5. Navigate through the menu to explore, clean, analyze, and visualize the data.

---

## 📈 Results & Insights

After running the program on `sales_data.csv`, the following outputs are produced:

- ✅ **Full Dataset Overview** — structure, data types, and summary statistics
- 🧹 **Cleaned Data** — missing `Sales` values identified and handled (mean-fill / drop / replace)
- 🔢 **Numeric Insights** — sum, mean, standard deviation, and percentiles for `Sales` and `Profit`
- 📊 **Regional & Product Trends** — visualized through bar plots, pie charts, and pivot tables
- 🔗 **Correlation Analysis** — heatmap revealing relationships between `Sales`, `Profit`, and `Year`
- 💾 **Exportable Charts** — any generated visualization can be saved as an image file

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🎓 **End-to-End Workflow** | Covers loading, cleaning, analysis, and visualization in one tool |
| 🧱 **Object-Oriented** | Clean, reusable, and extensible class-based design |
| 🔄 **Reusability** | Works with any similarly structured CSV, not just the sample dataset |
| 📚 **Educational** | Demonstrates practical Pandas, Numpy, Matplotlib, and Seaborn usage |
| 🖥️ **No External Setup** | Runs from a single notebook with standard data-science libraries |
| 🧪 **Extensible** | Easy to add new chart types, cleaning strategies, or aggregations |
| 🛡️ **Input Safety** | Invalid columns, files, and menu choices are caught and reported |

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

> *"Good analysis starts with asking the right question of the data — this project is my answer."*

**🎓 Role:** Python Developer | Data Analysis Enthusiast \
**📍 Location:** India \
**🛠️ Skills:** Python · Pandas · Numpy · Matplotlib · Seaborn · Data Analysis · OOP

</div>

---

## 🙏 Acknowledgements

Special thanks to the following resources and communities that made this project possible:

- 📚 [Python Official Docs](https://docs.python.org/3/) — Official Python language reference
- 🐼 [Pandas Documentation](https://pandas.pydata.org/docs/) — DataFrame operations reference
- 🔢 [Numpy Documentation](https://numpy.org/doc/) — Array operations reference
- 📊 [Matplotlib Documentation](https://matplotlib.org/stable/index.html) — Plotting reference
- 🎨 [Seaborn Documentation](https://seaborn.pydata.org/) — Statistical visualization reference
- 💬 [Stack Overflow Community](https://stackoverflow.com/) — Problem-solving support
- 📖 [Kaggle Learn](https://www.kaggle.com/learn) — Python and data analysis courses

---

<div align="center">

---

*Made with ❤️ and ☕ — Last updated: 15 July, 2026*

</div>
