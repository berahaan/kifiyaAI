# ☀️ Solar Data Discovery: Solar Farm Potential Analysis (Benin, Sierra Leone, Togo)

**A Data Science Project for the 10 Academy Solar Data Discovery Challenge**

Identify the **highest-potential regions for solar farm installation** across West Africa by analyzing historical solar irradiance data from **Benin, Sierra Leone, and Togo**. This project covers the complete data science pipeline, from **cleaning and EDA** to **cross-country comparison** and deployment of an **interactive Streamlit dashboard**.

---

## 🎯 Project Goals

This challenge aimed to transform raw solar farm data into actionable insights for strategic energy planning.

* **Data Quality:** Profile, clean, and pre-process raw solar datasets to ensure analysis reliability.
* **Deep Dive EDA:** Perform statistical analysis and visualize key solar metrics: **Global Horizontal Irradiance (GHI)**, **Direct Normal Irradiance (DNI)**, and **Diffuse Horizontal Irradiance (DHI)**.
* **Comparative Analysis:** Systematically compare solar potential across all three countries.
* **Interactive Insights:** Develop a user-friendly, dynamic **Streamlit dashboard** for exploring data and informing investment decisions.

---

## 🛠️ Technology Stack & Key Deliverables

### Tools Used
* **Python:** Core programming language.
* **Libraries:** Pandas, NumPy (Data Manipulation/Cleaning), Matplotlib, Seaborn (Static Visualization), Scipy (Statistical Testing).
* **Dashboard:** **Streamlit** (Interactive Web Application).

### Deliverables
| Artifact | Description | Location |
| :--- | :--- | :--- |
| **Interactive Dashboard** | Live, dynamic data exploration and comparison tool. | `app/main.py` |
| **Final Report** | Comprehensive analysis, methodology, and key insights. | `reports/Final_Report.pdf` |
| **EDA Notebooks** | Detailed steps for data cleaning and exploratory analysis. | `notebooks/` |
| **Clean Data** | The processed and cleaned datasets ready for modeling/viz. | `data/` |

---

## 📂 Repository Structure

The project is organized for clarity and reproducibility.

```
📁 solar-challenge-week1/
├── app/
│   └── main.py              # Streamlit dashboard
├── data/
│   ├── benin-malanvile.csv
│   ├── sierraleone-bumbuna.csv
│   └── togo-dapaong_qc.csv
├── notebooks/
│   └── <country>_eda.ipynb  # EDA notebooks
├── scripts/
│   └── README.md
├── reports/
│   ├── Interim_Report.pdf
│   ├── Final_Report.pdf
│   └── dashboard_screenshot.png
├── requirements.txt
└── README.md
```

---

## 📈 Analysis & Development Highlights

### 1. Data Cleaning & Pre-processing
* **Quality Check:** Summarized datasets using `.describe()` and performed missing value analysis.
* **Outlier Treatment:** Identified and treated extreme outliers in solar irradiance and wind speed using the Z-score method.
* **Imputation:** Missing values in critical columns were imputed using the median strategy to preserve data distribution.

### 2. Exploratory Data Analysis (EDA)
* **Time Series:** Visualized daily and hourly trends for GHI, DNI, DHI, and ambient temperature.
* **Correlation Analysis:** Used **heatmaps** and scatter plots to understand the relationships between solar radiation, temperature, and humidity.
* **Performance:** Analyzed the impact of maintenance/cleaning events on module performance (ModA & ModB).
* **Wind Patterns:** Visualized wind speed and direction distributions using **wind rose plots**.

### 3. Cross-Country Comparison
* **Statistical Comparison:** Used **boxplots** and summary tables to directly compare GHI, DNI, and DHI metrics across Benin, Sierra Leone, and Togo.
* **Significance Testing (Optional):** Utilized statistical tests (ANOVA/Kruskal-Wallis) to validate the significance of observed differences in solar potential.
* **Key Insight:** Highlighted the country with the **highest median GHI** and overall superior solar potential for investment.

### 4. Interactive Dashboard (Streamlit)
* The final product is an interactive dashboard built with **Streamlit** (`app/main.py`).
* **Features:** Country-specific dropdowns, dynamic plots of irradiance, correlation heatmaps, summary statistics, and a dedicated **"Compare All Countries"** view for cross-analysis.

---

## 🚀 Getting Started

Follow these steps to clone the repository and run the interactive dashboard locally.

### 1. Clone the Repository
```bash
git clone [https://github.com/berahaan/solar-challenge-week0.git](https://github.com/berahaan/solar-challenge-week0.git)
cd solar-challenge-week0
```

2. Environment Setup & Dependencies
Create and activate a virtual environment, then install the necessary packages.

# Using venv (Recommended)
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
# Install dependencies
pip install -r requirements.txt
3. Run the Streamlit Dashboard
Execute the main application file:
```
streamlit run app/main.py
```

- The application will automatically open in your web browser (usually at http://localhost:8501).
- Select a country (Benin, Sierra Leone, or Togo) from the sidebar dropdown.
- Explore the dynamic visualizations, heatmaps, and summary statistics.
- Use the "Compare All Countries" feature for a direct analysis of GHI across the regions.
