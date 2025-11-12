import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

st.set_page_config(page_title="Solar Data Discovery Dashboard", layout="wide")

st.title("🌞 Solar Data Discovery Dashboard")
st.markdown("### Compare Solar Energy Potential Across West African Countries")

# Map user selection to actual filenames
COUNTRY_FILES = {
    "Benin": "data/benin-malanvile.csv",
    "Sierra Leone": "data/sierraleone-bumbuna.csv",
    "Togo": "data/togo-dapaong_qc.csv"
}

# Load datasets
@st.cache_data
def load_data(country):
    path = COUNTRY_FILES[country]
    if not os.path.exists(path):
        st.error(f"❌ Data file not found for {country}: {path}")
        return pd.DataFrame()  # return empty DataFrame
    return pd.read_csv(path)

# Country selector
country = st.selectbox("🌍 Select a country:", list(COUNTRY_FILES.keys()))
df = load_data(country)

if df.empty:
    st.stop()

st.write(f"### 📄 Data Preview for {country}")
st.dataframe(df.head())

# Summary Statistics
st.subheader("📊 Summary Statistics")
st.write(df.describe())

# Solar Radiation Plots
st.subheader("☀️ Solar Radiation Metrics")

fig, ax = plt.subplots(1, 3, figsize=(15, 4))

sns.boxplot(y=df["GHI"], ax=ax[0], color="gold")
ax[0].set_title("Global Horizontal Irradiance (GHI)")

sns.boxplot(y=df["DNI"], ax=ax[1], color="orange")
ax[1].set_title("Direct Normal Irradiance (DNI)")

sns.boxplot(y=df["DHI"], ax=ax[2], color="skyblue")
ax[2].set_title("Diffuse Horizontal Irradiance (DHI)")

st.pyplot(fig)

# Correlation Heatmap
st.subheader("🔗 Correlation Heatmap")
numeric_df = df.select_dtypes(include="number")
corr = numeric_df.corr()
fig, ax = plt.subplots(figsize=(8, 5))
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)

# KPI Summary Cards
st.subheader("⚡ Quick Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Mean GHI", round(df["GHI"].mean(), 2))
col2.metric("Mean DNI", round(df["DNI"].mean(), 2))
col3.metric("Mean DHI", round(df["DHI"].mean(), 2))

# Insights Section
st.markdown("### 💡 Key Insights")
if country == "Benin":
    st.success("Benin (Malanvile) shows consistently high irradiance values — ideal for large-scale solar farms.")
elif country == "Togo":
    st.info("Togo (Dapaong) demonstrates reliable mid-range irradiance, suitable for hybrid solar systems.")
else:
    st.warning("Sierra Leone (Bumbuna) shows slightly lower direct irradiance due to higher humidity and cloud cover.")
# Compare all countries side by side
st.subheader("🌍 Country Comparison")

# Load all data for comparison
@st.cache_data
def load_all_data():
    dfs = []
    for c, path in COUNTRY_FILES.items():
        if os.path.exists(path):
            df = pd.read_csv(path)
            df["Country"] = c
            dfs.append(df)
    return pd.concat(dfs, ignore_index=True)

all_df = load_all_data()

fig, ax = plt.subplots(figsize=(10, 5))
sns.boxplot(data=all_df, x="Country", y="GHI", palette="Set2", ax=ax)
ax.set_title("Comparison of Global Horizontal Irradiance (GHI) Across Countries")
st.pyplot(fig)
