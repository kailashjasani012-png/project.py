<div align="center">

# -- ! Air Quality Analysis — Multi-City Dataset ! --
### *Daily Pollution Trends & Weather Relationships Across 10 Indian Cities*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-DataAnalysis-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge&logo=plotly&logoColor=white)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-4C72B0?style=for-the-badge&logo=python&logoColor=white)](https://seaborn.pydata.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)

<br/>

> *"The air we breathe leaves a trail of data — every spike and dip tells a seasonal story."*

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

The **Air Quality Analysis — Multi-City Dataset** project is a Jupyter Notebook–based exploratory data analysis of daily air quality readings across **10 Indian cities**. It uses **Pandas** for cleaning and aggregation, and **Matplotlib/Seaborn** for visualization, to uncover pollution trends over time, seasonal patterns, and how weather conditions (temperature, humidity, wind speed) relate to air quality.

This project is designed to:
- Practice cleaning grouped time-series data using city-wise median imputation
- Extract time-based features (month, day of week) from date columns
- Visualize AQI trends over time and across cities and seasons
- Study relationships between pollutants, weather, and overall AQI through correlation analysis

*Note: The dataset used is a simulated ~220-day daily record (10 cities) built with realistic seasonal pollution patterns (winter spikes, monsoon dips) and typical PM2.5/PM10/NO2/SO2/CO/O3 relationships, since no live internet feeds (e.g., CPCB or OpenAQ) were available in the environment. The same code works identically on a real dataset.*

---

## 🎯 Problem Statement

> **Objective:** Analyze daily air quality data across multiple cities to understand pollution levels, seasonal trends, and their relationship with weather conditions.

Given a daily-records dataset containing pollutant concentrations (PM2.5, PM10, NO2, SO2, CO, O3), weather readings, and computed AQI values for 10 cities, the notebook must clean the data, engineer time-based features, and produce visualizations that reveal city-wise pollution levels, seasonal patterns, pollutant distributions, and correlations with weather.

| 📂 Feature | 📄 Type | 🔍 Description |
|------------|---------|----------------|
| Data Loading & Cleaning | ETL | Reads CSV, fills missing readings per city, parses dates |
| Feature Engineering | Transformation | Extracts month, month name, and day of week |
| AQI Category Analysis | Visualization | Distribution of days across AQI categories |
| City & Seasonal Trends | Visualization | City-wise average AQI, monthly seasonal pattern, time trend |
| Pollutant Analysis | Visualization | Distribution and city comparison of key pollutants |
| Weather Correlation | Statistics | Relationship between AQI, pollutants, temperature, wind, humidity |

The goal is to demonstrate **practical exploratory data analysis (EDA) skills** on environmental time-series data.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 📥 **CSV Data Loading** | Reads the multi-city air quality dataset with Pandas |
| 🧹 **Group-Wise Data Cleaning** | Fills missing pollutant/weather values using each city's own median |
| 🗓️ **Date Feature Engineering** | Extracts month, month name, and day of week from the date column |
| 🚦 **AQI Category Distribution** | Bar chart of days across Good → Severe AQI categories |
| 🏙️ **City-Wise AQI Ranking** | Bar chart of average AQI per city |
| 📈 **AQI Trend Over Time** | Line chart tracking AQI for all 10 cities across the full period |
| 🍂 **Seasonal Pattern** | Monthly average AQI bar chart to reveal seasonal spikes/dips |
| 🧪 **Pollutant Comparison** | City-wise PM2.5/PM10 bar chart and distribution histograms |
| 🌦️ **Weather Correlation** | Heatmap and regression plots linking AQI with wind speed and temperature |
| 🗺️ **City × Category Heatmap** | Crosstab heatmap of AQI category counts per city |

---

## 🏗️ Project Structure

```
📦 air-quality-multi-city-analysis/
│
├── 📄 pro_4.ipynb                     ← Main Jupyter Notebook (analysis & visualizations)
├── 📄 Air_Quality_Cities_Dataset.csv  ← Dataset (10 cities, ~220-day daily records)
│
└── 📄 README.md                       ← Project documentation
```

---

## 🔄 Project Workflow

```
Load Dataset (CSV)
      │
      ▼
┌─────────────────────────────┐
│   Data Cleaning             │  ← City-wise median fill, date parsing
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│   Feature Engineering       │  ← Month, Month Name, Day of Week
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│   AQI Category & City       │  ← Category distribution, city-wise ranking
│   Analysis                  │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  Trend & Seasonal Analysis  │  ← Time trend, monthly seasonal pattern
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  Pollutant & Weather        │  ← Distributions, correlation heatmap,
│  Correlation                │    wind/temperature regression plots
└────────────┬────────────────┘
             │
             ▼
        Key Insights ✅
```

---

## 📊 Dataset Description

The dataset `Air_Quality_Cities_Dataset.csv` contains **2,200 daily records** across **10 Indian cities**, with the following columns:

| Column | Description |
|--------|-------------|
| `City` | Name of the city |
| `Region` | Geographic region of the city |
| `Date` | Date of the record |
| `PM2.5` | Fine particulate matter concentration (µg/m³) |
| `PM10` | Coarse particulate matter concentration (µg/m³) |
| `NO2` | Nitrogen dioxide concentration |
| `SO2` | Sulfur dioxide concentration |
| `CO` | Carbon monoxide concentration |
| `O3` | Ozone concentration |
| `Temperature` | Daily temperature (°C) |
| `Humidity` | Relative humidity (%) |
| `Wind_Speed` | Wind speed |
| `AQI` | Computed Air Quality Index |
| `AQI_Category` | AQI classification (Good, Satisfactory, Moderate, Poor, Very Poor, Severe) |

---

## 🔬 Analysis Steps

### 1️⃣ Import Libraries
Loads `pandas`, `numpy`, `matplotlib`, and `seaborn`, and sets the plotting style.

### 2️⃣ Load the Dataset
Reads the CSV file into a DataFrame and previews shape, columns, and info.

### 3️⃣ Data Cleaning
Checks for missing values and duplicates, converts the `Date` column to datetime, and fills missing pollutant/weather readings using each city's own median.

### 4️⃣ Feature Engineering
Extracts `Month`, `Month_Name`, and `DayOfWeek` from the date column for seasonal analysis.

### 5️⃣ Overall AQI Category Distribution
Bar chart showing how many city-days fall into each AQI category (Good through Severe).

### 6️⃣ City-Wise Average AQI
Ranks the 10 cities by their average AQI.

### 7️⃣ AQI Trend Over Time
Line chart tracking each city's AQI across the full ~220-day period.

### 8️⃣ Seasonal Pattern: Monthly Average AQI
Bar chart of average AQI per month, revealing seasonal spikes and dips.

### 9️⃣ Pollutant Comparison Across Cities
Bar chart comparing average PM2.5 and PM10 levels across cities.

### 🔟 Distribution of Key Pollutants
Histograms with KDE overlays for PM2.5, NO2, SO2, and AQI.

### 1️⃣1️⃣ Relationship Between Pollution and Weather
Correlation heatmap linking AQI, pollutants, temperature, humidity, and wind speed.

### 1️⃣2️⃣ AQI vs Wind Speed / Temperature
Regression plots showing how wind speed and temperature relate to AQI.

### 1️⃣3️⃣ City-Wise AQI Category Breakdown
Heatmap crosstab of the number of days each city spent in each AQI category.

### 1️⃣4️⃣ Key Insights
Summarizes findings such as winter AQI spikes, PM2.5 as the dominant AQI driver, and the negative correlation between wind speed and AQI.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| 🐍 **Python 3.8+** | Core programming language |
| 🐼 **Pandas** | Data loading, cleaning, and group-wise aggregation |
| 🔢 **NumPy** | Numerical operations |
| 📊 **Matplotlib** | Line charts and custom plot layouts |
| 🎨 **Seaborn** | Bar plots, histograms, regression plots, heatmaps |
| 📓 **Jupyter Notebook** | Interactive analysis environment |

---

## 📈 Results & Insights

- ❄️ **Winter months show a clear spike in AQI** across all cities, consistent with reduced dispersion, temperature inversions, and increased heating/burning activity.
- 🧪 **PM2.5 is the dominant driver of AQI**, showing the strongest correlation with overall AQI among all measured pollutants.
- 💨 **Wind speed is negatively correlated with AQI** — higher wind speeds disperse pollutants, while calm conditions let pollution accumulate.
- 🌡️ **Temperature shows a negative relationship with AQI** in this data, reflecting the winter-pollution-spike pattern.
- 🏙️ **Pollution levels vary significantly by city**, with some cities consistently ranking in "Poor" or "Very Poor" categories.

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 📓 **End-to-End Workflow** | Covers loading, cleaning, feature engineering, and visualization |
| 📊 **Rich Visual Variety** | Bar charts, line trends, histograms, regression plots, and heatmaps |
| 🧹 **Smart Imputation** | Uses city-wise medians instead of a single global fill value |
| 📚 **Educational** | Demonstrates real-world environmental time-series EDA practices |
| 🔁 **Reusable Structure** | Each analysis section is modular and easy to extend |
| 🧪 **Extensible** | Easy to plug in real CPCB/OpenAQ data with no code changes |

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
- 🌫️ [CPCB — Central Pollution Control Board](https://cpcb.nic.in/) — Reference for real-world air quality monitoring
- 💬 [Stack Overflow Community](https://stackoverflow.com/) — Problem-solving support
- 📖 [Kaggle Learn](https://www.kaggle.com/learn) — Data science and Python courses

---

<div align="center">

---

*Made with ❤️ and ☕ — Last updated: 20 July, 2026*

</div>
