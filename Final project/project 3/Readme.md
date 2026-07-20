<div align="center">

# -- ! Titanic Dataset — Survival Analysis (EDA) ! --
### *Exploratory Data Analysis of Passenger Survival on the Titanic*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-DataAnalysis-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge&logo=plotly&logoColor=white)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-4C72B0?style=for-the-badge&logo=python&logoColor=white)](https://seaborn.pydata.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)

<br/>

> *"Every passenger's story is a data point — together they reveal who survived, and why."*

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [📊 Dataset Description](#-dataset-description)
- [🔬 Analysis Steps](#-analysis-steps)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Insights](#-results--insights)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 📌 Overview

The **Titanic Dataset — Survival Analysis** project is a Jupyter Notebook–based exploratory data analysis of the classic Titanic passenger dataset. It investigates which factors — such as **gender, passenger class, age, and fare** — most strongly influenced a passenger's chances of survival, using **Pandas** for data wrangling and **Matplotlib/Seaborn** for visualization.

This project is designed to:
- Practice data cleaning: handling missing values and dropping unusable columns
- Explore survival patterns using cross-tabulations and group-wise statistics
- Visualize relationships between survival and passenger class, age, fare, and embarkation point
- Draw evidence-based conclusions about who was more likely to survive

---

## 🎯 Problem Statement

> **Objective:** Analyze the Titanic passenger dataset to identify the key factors affecting survival.

Given a dataset of individual passenger records (class, sex, age, fare, family size, embarkation port, and survival outcome), the notebook must clean the data, compute survival statistics across different groups, and produce visualizations that reveal how gender, class, age, and fare relate to survival.

| 📂 Feature | 📄 Type | 🔍 Description |
|------------|---------|----------------|
| Data Loading & Cleaning | ETL | Reads CSV, fills missing Age/Embarked, drops Cabin |
| Survival by Gender | Cross-tab | Compares survival counts between male and female passengers |
| Survival by Class | Cross-tab / Visualization | Compares survival across 1st, 2nd, and 3rd class |
| Age & Fare Analysis | Visualization | Distribution and boxplots relative to survival |
| Correlation Analysis | Visualization | Heatmap of numeric feature relationships |
| Embarkation Analysis | Visualization | Survival counts by port of embarkation |

The goal is to demonstrate **practical exploratory data analysis (EDA) skills** through a clean, well-documented notebook.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 📥 **CSV Data Loading** | Reads the Titanic dataset with Pandas |
| 🧹 **Data Cleaning** | Fills missing `Age` with median, `Embarked` with mode, drops the sparse `Cabin` column |
| 👫 **Survival by Gender** | Cross-tabulation of survival counts by sex |
| 🎟️ **Survival by Class** | Cross-tabulation and count plot of survival by passenger class |
| 📊 **Age Distribution** | Histogram with KDE curve showing passenger age spread |
| 💰 **Fare vs Survival** | Boxplot comparing fare distribution between survivors and non-survivors |
| 🔥 **Correlation Heatmap** | Relationships between numeric features like Age, Fare, Pclass, and Survived |
| ⚓ **Embarkation Analysis** | Count plot of survival split by port of embarkation |

---

## 🏗️ Project Structure

```
📦 titanic-survival-analysis/
│
├── 📄 pro_3.ipynb              ← Main Jupyter Notebook (analysis & visualizations)
├── 📄 Titanic-Dataset.csv      ← Dataset (891 passenger records)
│
└── 📄 README.md                ← Project documentation
```

---

## 🔄 Project Workflow

```
Load Dataset (CSV)
      │
      ▼
┌─────────────────────────────┐
│   Data Inspection           │  ← Shape, columns, info, describe, nulls
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│   Data Cleaning             │  ← Fill Age (median), Embarked (mode),
│                              │    drop Cabin column
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  Survival Cross-Tabulation  │  ← By Sex, by Pclass, group means (Age/Fare)
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│   Visual Analysis           │  ← Class, Age, Fare, Embarked plots
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│   Correlation Heatmap       │  ← Numeric feature relationships
└────────────┬────────────────┘
             │
             ▼
        Key Findings ✅
```

---

## 📊 Dataset Description

The dataset `Titanic-Dataset.csv` contains **891 passenger records** with the following columns:

| Column | Description |
|--------|-------------|
| `PassengerId` | Unique identifier for each passenger |
| `Survived` | Survival outcome (0 = No, 1 = Yes) |
| `Pclass` | Passenger class (1st, 2nd, 3rd) |
| `Name` | Passenger name |
| `Sex` | Gender of the passenger |
| `Age` | Age in years |
| `SibSp` | Number of siblings/spouses aboard |
| `Parch` | Number of parents/children aboard |
| `Ticket` | Ticket number |
| `Fare` | Fare paid |
| `Cabin` | Cabin number (mostly missing) |
| `Embarked` | Port of embarkation (C, Q, S) |

---

## 🔬 Analysis Steps

### 1️⃣ Import Libraries
Loads `pandas`, `numpy`, `matplotlib`, and `seaborn`.

### 2️⃣ Load & Inspect the Dataset
Reads the CSV and previews the first/last rows, shape, columns, data types, and statistical summary.

### 3️⃣ Missing Value & Duplicate Check
Checks for null values in each column and counts duplicate rows.

### 4️⃣ Data Cleaning
Fills missing `Age` values with the median, missing `Embarked` values with the mode, and drops the largely-empty `Cabin` column.

### 5️⃣ Survival Counts & Cross-Tabulations
Computes overall survival counts, and cross-tabulates survival against `Sex` and `Pclass`. Also computes average `Age` and `Fare` grouped by survival outcome.

### 6️⃣ Survival by Passenger Class
Count plot visualizing survival split across the three passenger classes.

### 7️⃣ Age Distribution
Histogram with a KDE overlay showing how passenger ages are distributed.

### 8️⃣ Fare vs Survival
Boxplot comparing the fare distribution between passengers who survived and those who didn't.

### 9️⃣ Correlation Heatmap
Heatmap of correlations between numeric features (`Age`, `Fare`, `Pclass`, `Survived`, etc.).

### 🔟 Overall Survival & Embarkation Analysis
Count plots showing the overall survival split and survival counts by port of embarkation.

### 1️⃣1️⃣ Conclusion
Summarizes key findings — such as higher survival among women and first-class passengers — into an overall narrative.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| 🐍 **Python 3.8+** | Core programming language |
| 🐼 **Pandas** | Data loading, cleaning, and cross-tabulation |
| 🔢 **NumPy** | Numerical operations |
| 📊 **Matplotlib** | Custom plot styling and layout |
| 🎨 **Seaborn** | Count plots, histograms, boxplots, heatmaps |
| 📓 **Jupyter Notebook** | Interactive analysis environment |

---

## 📈 Results & Insights

- 👩 **Female passengers had a significantly higher survival rate** than male passengers.
- 🎟️ **First-class passengers were more likely to survive** than second- and third-class passengers.
- 👶 **Younger passengers showed a slightly higher survival rate.**
- 💰 **Passengers who paid higher fares generally had better chances of survival**, reflecting their class advantage.
- 🧹 **Missing values were successfully handled** (Age via median, Embarked via mode), making the dataset fully suitable for analysis.
- ⚓ **Port of embarkation also shows a visible relationship with survival counts.**

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 📓 **End-to-End Workflow** | Covers inspection, cleaning, and visualization in one notebook |
| 📊 **Diverse Visualizations** | Count plots, histograms, boxplots, and a correlation heatmap |
| 🧹 **Clean Data Pipeline** | Handles missing values and drops unusable columns |
| 📚 **Educational** | A classic, beginner-friendly dataset for practicing EDA techniques |
| 🔁 **Reusable Structure** | Each analysis section is modular and easy to extend |
| 🧪 **Extensible** | Easy to add feature engineering or predictive modeling on top |

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

[![GitHub](https://img.shields.io/badge/GitHub-yourhandle-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/)

> *"Every insight starts with clean data — just like every visualization starts with a single plot."*

**🎓 Role:** Data Analyst | Python & Data Science Enthusiast \
**📍 Location:** India\
**🛠️ Skills:** Python · Pandas · Data Visualization · Exploratory Data Analysis · Jupyter Notebook

</div>

---

## 🙏 Acknowledgements

Special thanks to the following resources and communities that made this project possible:

- 📚 [Pandas Documentation](https://pandas.pydata.org/docs/) — Official data analysis library reference
- 📊 [Matplotlib Documentation](https://matplotlib.org/stable/index.html) — Plotting library reference
- 🎨 [Seaborn Documentation](https://seaborn.pydata.org/) — Statistical visualization reference
- 📓 [Jupyter Project](https://jupyter.org/) — Interactive notebook environment
- 🚢 [Kaggle — Titanic: Machine Learning from Disaster](https://www.kaggle.com/c/titanic) — Original source of the dataset
- 💬 [Stack Overflow Community](https://stackoverflow.com/) — Problem-solving support
- 📖 [Kaggle Learn](https://www.kaggle.com/learn) — Data science and Python courses

---

<div align="center">

---

*Made with ❤️ and ☕ — Last updated: 20 July, 2026*

</div>
