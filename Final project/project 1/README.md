<div align="center">

# -- ! COVID-19 Data Analysis & Visualization ! --
### *Time Series Exploration of Global COVID-19 Spread (20 Countries)*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-DataAnalysis-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge&logo=plotly&logoColor=white)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-4C72B0?style=for-the-badge&logo=python&logoColor=white)](https://seaborn.pydata.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)

<br/>

> *"Data tells the story of the pandemic — one curve, one country, one day at a time."*

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

The **COVID-19 Data Analysis & Visualization** project is a Jupyter Notebook–based data science workflow that explores the spread of COVID-19 over time across **20 countries**. It uses **Pandas** for data wrangling and **Matplotlib/Seaborn** for visualization to uncover trends in cases, recoveries, deaths, testing, and death rates.

This project is designed to:
- Practice end-to-end data analysis: loading, cleaning, and exploring a time-series dataset
- Visualize global and country-wise pandemic trends using multiple chart types
- Compute derived metrics such as death rate, recovery rate, and cases per million
- Study relationships between population, testing, and case counts through correlation analysis

*Note: The dataset used is a simulated ~110-day daily time series (20 countries) built using a realistic epidemic (logistic growth) curve per country, since no live internet feeds (e.g., Johns Hopkins / Our World in Data) were available in the environment.*

---

## 🎯 Problem Statement

> **Objective:** Analyze and visualize the trajectory of the COVID-19 pandemic across countries and continents using a structured time-series dataset.

Given a daily records dataset containing case counts, deaths, recoveries, and testing numbers for 20 countries, the notebook must clean the data, compute summary statistics, and produce a series of visualizations that reveal global trends, country-level comparisons, and rate-based insights (death rate, recovery rate, cases per million).

| 📂 Feature | 📄 Type | 🔍 Description |
|------------|---------|----------------|
| Data Loading & Cleaning | ETL | Reads CSV, checks nulls/duplicates, parses dates |
| Global Trend Analysis | Visualization | Cumulative cases, deaths, recoveries over time |
| Country Comparison | Visualization | Case trajectories for top countries |
| Continent Analysis | Visualization | Trend lines grouped by continent |
| Rate Metrics | Computation | Death rate, recovery rate, cases per million |
| Correlation Study | Statistics | Heatmap across population, cases, deaths, tests |

The goal is to demonstrate **practical exploratory data analysis (EDA) skills** through a clean, well-documented notebook.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 📥 **CSV Data Loading** | Reads the time-series dataset with Pandas |
| 🧹 **Data Cleaning** | Checks for missing values, duplicates, and parses date columns |
| 🌍 **Global Trend Charts** | Cumulative cases, deaths, and recoveries plotted over time |
| 📉 **7-Day Rolling Average** | Smooths daily new-case noise to reveal the underlying wave |
| 🌐 **Country & Continent Comparison** | Line plots comparing top 8 countries and continent-wise trends |
| 🏆 **Latest Snapshot Rankings** | Top 10 countries by total cases, death rate, and cases per million |
| 🧪 **Testing vs Cases Analysis** | Log-log scatter plot of total tests vs total cases |
| 🔥 **Correlation Heatmap** | Relationships between population, cases, deaths, recoveries, and tests |

---

## 🏗️ Project Structure

```
📦 covid-19-data-analysis/
│
├── 📄 pro_1.ipynb                ← Main Jupyter Notebook (analysis & visualizations)
├── 📄 covid_19_timeseries.csv    ← Dataset (20 countries, ~110-day daily records)
│
└── 📄 README.md                  ← Project documentation
```

---

## 🔄 Project Workflow

```
Load Dataset (CSV)
      │
      ▼
┌─────────────────────────────┐
│   Data Cleaning & Parsing   │  ← Nulls, duplicates, date conversion
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│   Global Trend Analysis     │  ← Cumulative cases/deaths/recoveries
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  Country & Continent Trends │  ← Top 8 countries, continent-wise lines
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│   Latest Snapshot Metrics   │  ← Death rate, recovery rate, per-million
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  Testing vs Cases + Corr.   │  ← Scatter plot & heatmap
└────────────┬────────────────┘
             │
             ▼
        Key Insights ✅
```

---

## 📊 Dataset Description

The dataset `covid_19_timeseries.csv` contains **2,200 daily records** across **20 countries**, with the following columns:

| Column | Description |
|--------|-------------|
| `country` | Name of the country |
| `continent` | Continent the country belongs to |
| `population` | Total population of the country |
| `date` | Date of the record |
| `total_cases` | Cumulative confirmed cases |
| `new_cases` | New cases reported that day |
| `total_deaths` | Cumulative deaths |
| `new_deaths` | New deaths reported that day |
| `total_recovered` | Cumulative recoveries |
| `total_tests` | Cumulative tests conducted |

---

## 🔬 Analysis Steps

### 1️⃣ Import Libraries
Loads `pandas`, `numpy`, `matplotlib`, and `seaborn`, and sets the plotting style.

### 2️⃣ Load the Dataset
Reads the CSV file into a DataFrame and previews shape, columns, and info.

### 3️⃣ Data Cleaning
Checks for missing values and duplicate rows, converts the `date` column to datetime, and sorts records by country and date.

### 4️⃣ Global Trend Over Time
Plots cumulative total cases, recoveries, and deaths across all countries combined.

### 5️⃣ Daily New Cases (Global)
Plots raw daily new cases along with a 7-day rolling average to smooth out noise.

### 6️⃣ Country-Wise Case Trajectories
Compares cumulative case curves for the top 8 countries by total cases.

### 7️⃣ Continent-Wise Trend
Groups cumulative cases by continent and plots trend lines using Seaborn.

### 8️⃣ Latest Snapshot — Top 10 Countries
Ranks countries by total cases as of the most recent date in the dataset.

### 9️⃣ Death Rate & Recovery Rate
Computes `death_rate_%` and `recovery_rate_%` per country and visualizes the highest death rates.

### 🔟 Cases per Million Population
Normalizes case counts by population to enable fair per-capita comparison.

### 1️⃣1️⃣ Testing vs Cases
Log-log scatter plot comparing total tests against total cases, sized by population.

### 1️⃣2️⃣ Correlation Heatmap
Shows correlation coefficients between population, cases, deaths, recoveries, and tests.

### 1️⃣3️⃣ Key Insights
Summarizes findings such as the S-shaped logistic growth pattern of the global curve and how the 7-day rolling average clarifies underlying wave trends.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| 🐍 **Python 3.8+** | Core programming language |
| 🐼 **Pandas** | Data loading, cleaning, and aggregation |
| 🔢 **NumPy** | Numerical operations |
| 📊 **Matplotlib** | Line charts and scatter plots |
| 🎨 **Seaborn** | Statistical visualizations (bar plots, heatmaps, line plots) |
| 📓 **Jupyter Notebook** | Interactive analysis environment |

---

## 📈 Results & Insights

- 🌍 The global cumulative case curve follows a **clear S-shaped (logistic) growth pattern**, typical of early pandemic waves.
- 📉 The **7-day rolling average** significantly smooths daily reporting noise and reveals the true wave shape.
- 🌐 **Country trajectories vary widely** — some show steep early peaks, others a slower, later climb.
- ☠️ **Death rate and recovery rate** vary meaningfully across countries, highlighting differences in healthcare response.
- 🧪 **Testing volume correlates with reported cases**, visible in the log-log scatter comparison.
- 🔥 The **correlation heatmap** confirms strong relationships between population, total cases, and total tests.

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 📓 **End-to-End Workflow** | Covers loading, cleaning, analysis, and visualization in one notebook |
| 📊 **Multiple Chart Types** | Line plots, bar plots, scatter plots, and heatmaps |
| 🔁 **Reusable Structure** | Each analysis section is modular and easy to extend |
| 📚 **Educational** | Demonstrates real-world EDA practices step by step |
| 🖥️ **No External Data Needed** | Uses a self-contained, realistic simulated dataset |
| 🧪 **Extensible** | Easy to add more metrics, countries, or time ranges |

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
- 💬 [Stack Overflow Community](https://stackoverflow.com/) — Problem-solving support
- 📖 [Kaggle Learn](https://www.kaggle.com/learn) — Data science and Python courses

---

<div align="center">

---

*Made with ❤️ and ☕ — Last updated: 20 July, 2026*

</div>
