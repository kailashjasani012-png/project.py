<div align="center">

# -- ! Stock Market Data Analysis ! --
### *Trend, Volume & Return Analysis of Historical Stock Market Data*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-DataAnalysis-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge&logo=plotly&logoColor=white)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-4C72B0?style=for-the-badge&logo=python&logoColor=white)](https://seaborn.pydata.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)

<br/>

> *"Every candle on a chart is a data point — trends are just patterns waiting to be read."*

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

The **Stock Market Data Analysis** project is a Jupyter Notebook–based exploratory data analysis of historical stock market records. It uses **Pandas** and **NumPy** for data cleaning and statistics, and **Matplotlib/Seaborn** for visualization, to study closing price trends, trading volume, moving averages, daily returns, and relationships between price-related features.

This project is designed to:
- Practice a complete data cleaning pipeline using mean/median imputation for missing values
- Analyze price trends using 20-day and 50-day moving averages
- Study the distribution of daily returns and closing prices
- Identify highest/lowest closing prices and monthly performance patterns

---

## 🎯 Problem Statement

> **Objective:** Analyze historical stock market data to understand price trends, trading activity, and return behavior.

Given a dataset of daily stock records (Open, High, Low, Close, Adjusted Close, Volume, Company, Sector, and computed indicators), the notebook must clean the data, compute descriptive statistics, and produce visualizations that reveal closing price trends, moving averages, return distributions, and correlations between key price features.

| 📂 Feature | 📄 Type | 🔍 Description |
|------------|---------|----------------|
| Data Loading & Cleaning | ETL | Reads CSV, fills missing prices/volume/moving averages |
| Descriptive Statistics | Analysis | Mean, median, and standard deviation of numeric features |
| Trend Analysis | Visualization | Closing price trend and monthly trading volume |
| Moving Averages | Visualization | 20-day and 50-day moving averages vs closing price |
| Return Analysis | Visualization | Distribution of daily returns |
| Correlation Analysis | Visualization | Heatmap across Open, High, Low, Close, Volume, Return |

The goal is to demonstrate **practical exploratory data analysis (EDA) skills** on financial time-series data.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 📥 **CSV Data Loading** | Reads the stock market dataset with Pandas |
| 🧹 **Data Cleaning** | Fills missing `Open`/`Close` with mean, `Volume` with median, moving averages with mean, and `Daily_Return` with 0 |
| 📊 **Descriptive Statistics** | Mean, median, and standard deviation for key numeric columns |
| 📈 **Closing Price Trend** | Line chart of closing price over time |
| 📦 **Trading Volume Trend** | Monthly average trading volume line chart |
| 📉 **Moving Averages** | Closing price plotted against 20-day and combined 20-day/50-day moving averages |
| 🎯 **Daily Return Distribution** | Histogram with KDE overlay of daily returns |
| 🔥 **Correlation Heatmap** | Relationships between Open, High, Low, Close, Volume, and Daily Return |
| 🏆 **Highest/Lowest Close** | Identifies and visualizes the highest and lowest closing price records |
| 🗓️ **Monthly Performance** | Average closing price by month |
| 🔗 **Pair Plot** | Multivariate visualization across key price and volume features |

---

## 🏗️ Project Structure

```
📦 stock-market-data-analysis/
│
├── 📄 pro_5.ipynb                ← Main Jupyter Notebook (analysis & visualizations)
├── 📄 stock_market_data.csv      ← Dataset (daily stock market records)
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
│   Data Inspection           │  ← Shape, dtypes, info, describe, nulls
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│   Handle Missing Values     │  ← Mean (Open/Close/MAs), median (Volume),
│                              │    0 (Daily_Return)
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  Descriptive Statistics     │  ← Mean, median, std deviation
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  Trend & Moving Average     │  ← Closing price trend, volume trend,
│  Visualization               │    20-day / 50-day MAs
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  Return & Correlation       │  ← Daily return distribution,
│  Analysis                   │    correlation heatmap
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  Highest/Lowest & Monthly   │  ← Extreme closing prices, monthly
│  Performance + Pair Plot    │    averages, pair plot
└─────────────────────────────┘
```

---

## 📊 Dataset Description

The dataset `stock_market_data.csv` contains **1,200 daily stock records** with the following columns:

| Column | Description |
|--------|-------------|
| `Date` | Trading date |
| `Open` | Opening price |
| `High` | Highest price of the day |
| `Low` | Lowest price of the day |
| `Close` | Closing price |
| `Adj Close` | Adjusted closing price |
| `Volume` | Number of shares traded |
| `Company` | Company/stock name |
| `Sector` | Industry sector |
| `Moving_Average_20` | 20-day moving average of closing price |
| `Moving_Average_50` | 50-day moving average of closing price |
| `Daily_Return` | Day-over-day percentage return |

---

## 🔬 Analysis Steps

### 1️⃣ Import Libraries
Loads `pandas`, `numpy`, `matplotlib`, and `seaborn`, and sets the plotting style.

### 2️⃣ Load & Inspect the Dataset
Reads the CSV and previews the first rows, shape, column names, data types, and statistical summary.

### 3️⃣ Missing Value Check
Identifies missing values across all columns.

### 4️⃣ Handle Missing Values
Fills `Open` and `Close` with their mean, `Volume` with its median, `Moving_Average_20`/`Moving_Average_50` with their mean, and `Daily_Return` with 0.

### 5️⃣ Descriptive Statistics
Computes mean, median, and standard deviation for `Open`, `High`, `Low`, `Close`, `Adj Close`, and `Volume`.

### 6️⃣ Closing Price Trend
Line chart of closing price over time, after sorting by date.

### 7️⃣ Monthly Average Trading Volume
Line chart of average trading volume aggregated by year-month.

### 8️⃣ Moving Averages
Two charts: closing price vs 20-day moving average, and closing price with both 20-day and 50-day moving averages.

### 9️⃣ Daily Return Distribution
Histogram with KDE overlay showing how daily returns are distributed.

### 🔟 Correlation Heatmap
Heatmap of correlations between `Open`, `High`, `Low`, `Close`, `Volume`, and `Daily_Return`.

### 1️⃣1️⃣ Highest & Lowest Closing Price
Identifies the record with the highest and lowest closing price and visualizes each with a bar chart.

### 1️⃣2️⃣ Monthly Stock Performance
Extracts the month name and computes/visualizes average closing price by month.

### 1️⃣3️⃣ Distribution of Closing Prices
Histogram with KDE overlay of the overall closing price distribution.

### 1️⃣4️⃣ Pair Plot
Multivariate pair plot across `Open`, `High`, `Low`, `Close`, `Volume`, and `Daily_Return`.

### 1️⃣5️⃣ Final Insights & Conclusion
Summarizes trend patterns, moving average behavior, return concentration around zero, and feature correlations.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| 🐍 **Python 3.8+** | Core programming language |
| 🐼 **Pandas** | Data loading, cleaning, and aggregation |
| 🔢 **NumPy** | Numerical operations |
| 📊 **Matplotlib** | Line charts, bar charts, and trend visualizations |
| 🎨 **Seaborn** | Histograms, heatmaps, and pair plots |
| 📓 **Jupyter Notebook** | Interactive analysis environment |

---

## 📈 Results & Insights

- 📈 **Stock prices showed fluctuations** over the selected time period, reflecting typical market volatility.
- 📉 **20-day and 50-day moving averages** helped identify short-term and long-term price trends.
- 🎯 **Daily returns were mostly concentrated around zero**, indicating that large daily swings were relatively less frequent.
- 🔗 **Correlation analysis showed a strong relationship** between Open, High, Low, and Close prices.
- 🗓️ **Monthly analysis revealed variation** in average closing prices across different months.
- 📦 **Trading volume changed over time**, indicating different levels of market activity across the period.

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 📓 **End-to-End Workflow** | Covers inspection, cleaning, statistics, and visualization in one notebook |
| 📊 **Diverse Visualizations** | Line charts, bar charts, histograms, heatmaps, and pair plots |
| 🧹 **Practical Imputation** | Uses appropriate mean/median/zero-fill strategies per column |
| 📚 **Educational** | Demonstrates real-world financial time-series EDA practices |
| 🔁 **Reusable Structure** | Each analysis section is modular and easy to extend |
| 🧪 **Extensible** | Easy to add more indicators (RSI, MACD) or predictive modeling |

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
- 🔢 [NumPy Documentation](https://numpy.org/doc/) — Numerical computing reference
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
