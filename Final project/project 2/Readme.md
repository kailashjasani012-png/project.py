<div align="center">

# -- ! World Happiness Report — EDA & Visualization ! --
### *Exploratory Data Analysis of Global Happiness Scores & Their Drivers*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-DataAnalysis-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge&logo=plotly&logoColor=white)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-4C72B0?style=for-the-badge&logo=python&logoColor=white)](https://seaborn.pydata.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)

<br/>

> *"Happiness is data too — you just need the right lens to see its patterns."*

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

The **World Happiness Report — EDA & Visualization** project is a Jupyter Notebook–based exploratory data analysis that studies global happiness scores and the factors that influence them, such as **GDP per capita, social support, healthy life expectancy, freedom, generosity, and corruption**. It uses **Pandas** for cleaning and aggregation, and **Matplotlib/Seaborn** for rich statistical visualizations.

This project is designed to:
- Practice a complete data cleaning pipeline: handling missing values, duplicates, and inconsistent column names
- Explore relationships between happiness and its key drivers using scatter and regression plots
- Compare happiness levels across countries, regions, and years
- Visualize multivariate relationships using pair plots and grouped comparisons

---

## 🎯 Problem Statement

> **Objective:** Analyze the World Happiness Report dataset to understand which factors most strongly influence happiness scores across countries and regions.

Given a dataset of country-level happiness scores along with socio-economic indicators, the notebook must clean the data, handle missing values, and produce visualizations that reveal the happiest and least happy countries, regional patterns, year-over-year trends, and correlations between happiness and its contributing factors.

| 📂 Feature | 📄 Type | 🔍 Description |
|------------|---------|----------------|
| Data Loading & Cleaning | ETL | Reads CSV, handles nulls, duplicates, column naming |
| Ranking Analysis | Visualization | Top 10 / Bottom 10 happiest countries |
| Correlation Analysis | Visualization | Scatter & regression plots vs happiness score |
| Regional Comparison | Visualization | Average happiness by region, box plot distribution |
| Trend Analysis | Visualization | Year-wise average happiness score |
| Multivariate Analysis | Visualization | Pair plot across key indicators |

The goal is to demonstrate **practical exploratory data analysis (EDA) skills** through a clean, well-documented notebook.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 📥 **CSV Data Loading** | Reads the World Happiness Report dataset with Pandas |
| 🧹 **Data Cleaning** | Fills missing numeric values with mean, categorical with mode, removes duplicates |
| 🏷️ **Column Standardization** | Strips, lowercases, and underscores all column names |
| 🏆 **Top/Bottom Rankings** | Bar charts for the 10 happiest and 10 least happy countries |
| 📈 **Regression Plots** | Relationship of GDP, social support, life expectancy, and freedom with happiness |
| 🌍 **Regional Analysis** | Average happiness score by region with bar and box plots |
| 📅 **Year-Wise Trend** | Line chart showing how average happiness changes over time |
| 🔗 **Pair Plot** | Multivariate visualization across key indicators, colored by region |

---

## 🏗️ Project Structure

```
📦 world-happiness-analysis/
│
├── 📄 pro_2.ipynb              ← Main Jupyter Notebook (analysis & visualizations)
├── 📄 world_happiness.csv      ← Dataset (country-level happiness indicators)
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
│   Data Inspection           │  ← Shape, dtypes, info, describe, sample rows
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│   Handle Missing Values     │  ← Mean for numeric, mode for categorical
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  Remove Duplicates & Clean  │  ← Drop duplicates, standardize column names
│  Column Names               │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│   Ranking & Correlation     │  ← Top/Bottom countries, GDP/support/freedom
│   Visualizations            │    vs happiness score
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  Regional & Yearly Trends   │  ← Region averages, box plots, year-wise line
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│   Pair Plot & Insights      │  ← Multivariate view + final conclusions
└─────────────────────────────┘
```

---

## 📊 Dataset Description

The dataset `world_happiness.csv` contains **1,200 country-year records** with the following columns:

| Column | Description |
|--------|-------------|
| `Country` | Name of the country |
| `Year` | Year of the record |
| `Happiness Score` | Overall reported happiness score |
| `GDP per Capita` | Economic output per person |
| `Social Support` | Perceived availability of social support |
| `Healthy Life Expectancy` | Average healthy life expectancy at birth |
| `Freedom` | Perceived freedom to make life choices |
| `Generosity` | Measure of generosity/charitable behavior |
| `Corruption` | Perceived level of corruption |
| `Region` | Geographic region of the country |

---

## 🔬 Analysis Steps

### 1️⃣ Import Libraries
Loads `pandas`, `numpy`, `matplotlib`, and `seaborn`.

### 2️⃣ Load & Inspect the Dataset
Reads the CSV and inspects the first/last rows, shape, column names, data types, statistical summary, and random samples.

### 3️⃣ Missing Value Analysis
Computes missing value counts and percentages per column, and visualizes them with a missing-values heatmap.

### 4️⃣ Handle Missing Values
Fills missing numeric columns with their mean and missing categorical columns with their mode.

### 5️⃣ Remove Duplicates & Standardize Columns
Drops duplicate rows and cleans column names (strip, lowercase, replace spaces with underscores).

### 6️⃣ Top & Bottom 10 Happiest Countries
Bar charts showing the 10 highest and 10 lowest happiness scores by country.

### 7️⃣ GDP vs Happiness Score
Scatter plot of GDP per capita against happiness score, colored by region.

### 8️⃣ Social Support, Life Expectancy & Freedom vs Happiness
Regression plots showing the relationship between each factor and happiness score.

### 9️⃣ Regional Comparison
Groups data by region to compute and visualize average happiness score, plus a box plot of score distribution per region.

### 🔟 Year-Wise Trend
Line chart of average happiness score across years.

### 1️⃣1️⃣ Pair Plot
Multivariate pair plot across happiness score, GDP, social support, life expectancy, and freedom, colored by region.

### 1️⃣2️⃣ Final Insights & Conclusion
Summarizes which factors most strongly relate to happiness and how patterns vary across regions and years.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| 🐍 **Python 3.8+** | Core programming language |
| 🐼 **Pandas** | Data loading, cleaning, and aggregation |
| 🔢 **NumPy** | Numerical operations |
| 📊 **Matplotlib** | Line charts and custom plots |
| 🎨 **Seaborn** | Bar plots, regression plots, box plots, pair plots |
| 📓 **Jupyter Notebook** | Interactive analysis environment |

---

## 📈 Results & Insights

- 💰 **Countries with higher GDP per capita generally report higher happiness scores.**
- 🤝 **Social support shows a strong positive relationship** with happiness.
- 🏥 **Healthy life expectancy also contributes positively** to happiness levels.
- 🕊️ **Greater freedom to make life choices correlates with higher happiness.**
- 🌍 **Happiness levels vary significantly across regions**, as seen in the regional bar and box plots.
- 📅 **Year-wise analysis** reveals how average global happiness has shifted over time.
- 🔗 GDP, social support, healthy life expectancy, and freedom emerge as the **most influential factors** on happiness score.

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 📓 **End-to-End Workflow** | Covers inspection, cleaning, and visualization in one notebook |
| 📊 **Diverse Visualizations** | Bar charts, scatter plots, regression plots, box plots, and pair plots |
| 🧹 **Robust Cleaning Pipeline** | Handles missing values, duplicates, and messy column names |
| 📚 **Educational** | Demonstrates real-world EDA practices on a socio-economic dataset |
| 🔁 **Reusable Structure** | Each analysis section is modular and easy to extend |
| 🧪 **Extensible** | Easy to add more indicators, regions, or years |

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
- 🌍 [World Happiness Report](https://worldhappiness.report/) — Original inspiration for the dataset
- 💬 [Stack Overflow Community](https://stackoverflow.com/) — Problem-solving support
- 📖 [Kaggle Learn](https://www.kaggle.com/learn) — Data science and Python courses

---

<div align="center">

---

*Made with ❤️ and ☕ — Last updated: 20 July, 2026*

</div>
