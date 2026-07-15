import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title="Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 BeanForecast Analytics Dashboard")

# Load Dataset
df = pd.read_csv("data/BeanForecast_AI_Advanced_Dataset_5000_Rows.csv")

# ===========================
# KPI Cards
# ===========================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("💰 Total Revenue", f"Rs. {df['DailyRevenue'].sum():,.0f}")

with col2:
    st.metric("📈 Average Revenue", f"Rs. {df['DailyRevenue'].mean():,.2f}")

with col3:
    st.metric("☕ Average Foot Traffic", int(df["FootTraffic"].mean()))

st.divider()

# ===========================
# Monthly Revenue
# ===========================

st.subheader("📈 Monthly Revenue")

monthly = df.groupby("Month")["DailyRevenue"].mean().reset_index()

fig = px.line(
    monthly,
    x="Month",
    y="DailyRevenue",
    markers=True,
    title="Average Monthly Revenue"
)

st.plotly_chart(fig, use_container_width=True)

# ===========================
# Top Selling Products
# ===========================

st.subheader("☕ Top Selling Products")

product = df["TopSellingProduct"].value_counts().reset_index()
product.columns = ["Product", "Count"]

fig2 = px.bar(
    product,
    x="Product",
    y="Count",
    color="Count",
    title="Top Selling Products"
)

st.plotly_chart(fig2, use_container_width=True)

# ===========================
# Temperature vs Revenue
# ===========================

st.subheader("🌡 Temperature vs Revenue")

fig3 = px.scatter(
    df,
    x="TemperatureC",
    y="DailyRevenue",
    color="Season",
    title="Temperature vs Revenue"
)

st.plotly_chart(fig3, use_container_width=True)

# ===========================
# Promotion Impact
# ===========================

st.subheader("🎁 Promotion Impact")

promo = df.groupby("Promotion")["DailyRevenue"].mean().reset_index()

fig4 = px.bar(
    promo,
    x="Promotion",
    y="DailyRevenue",
    color="Promotion",
    title="Promotion Impact on Revenue"
)

st.plotly_chart(fig4, use_container_width=True)

# ===========================
# Foot Traffic
# ===========================

st.subheader("👣 Foot Traffic Distribution")

fig5 = px.histogram(
    df,
    x="FootTraffic",
    nbins=30,
    title="Customer Foot Traffic"
)

st.plotly_chart(fig5, use_container_width=True)

st.success("✅ Analytics Dashboard Loaded Successfully!")