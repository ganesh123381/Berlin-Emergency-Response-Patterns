import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings 
warnings.filterwarnings("ignore")

st.set_page_config(page_title="Berlin Emergency Analysis", layout="wide")

# === LOAD DATA ===
@st.cache_data
def load_data():
    df = pd.read_csv(
       r"C:\Users\vgane\OneDrive\Desktop\BF-Open-Data-main\Datasets\Berlin_Missions_2020_2025.csv",
        parse_dates=["mission_created_date"],
        low_memory=False
    )
    df = df.drop(columns=["Unnamed: 0"], errors="ignore")
    df["year"] = df["mission_created_date"].dt.year

    mission_map = {
        "Rettungsdienst": "EMS",
        "Brand": "Fire",
        "Technische Hilfeleistung": "Technical Rescue",
        "Notfallrettung": "Emergency Rescue",
        "Krankentransport": "Patient Transport"
    }
    df["mission_type_en"] = df["mission_type"].map(mission_map).fillna("Other")
    return df

df = load_data()

# === SIDEBAR SELECTION ===
st.sidebar.title("Filters")
district = st.sidebar.selectbox(
    "Select District",
    sorted(df["mission_location_district"].dropna().unique())
)

# === FILTER DATA ===
df_loc = df[df["mission_location_district"] == district]

# === AGGREGATION ===
trend = (
    df_loc
    .groupby(["year", "mission_type_en"], as_index=False)
    .size()
    .rename(columns={"size": "incident_count"})
)

# === TITLE ===
st.title("🚨 District-wise Emergency Incident Trends")
st.subheader(f"📍 Selected District: {district}")

# === PLOT ===
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(
    data=trend,
    x="year",
    y="incident_count",
    hue="mission_type_en",
    marker="o",
    ax=ax
)

ax.set_title("Incident Type Trends (2020–2025)", fontweight="bold")
ax.set_xlabel("Year")
ax.set_ylabel("Number of Incidents")
ax.grid(alpha=0.3)

st.pyplot(fig)

# === KEY INSIGHTS ===
st.markdown("### 🔍 Key Insight")
top_incident = (
    df_loc["mission_type_en"]
    .value_counts()
    .idxmax()
)

st.write(
    f"**{top_incident}** incidents are the most frequent in **{district}** "
    f"between 2020 and 2025."
)
