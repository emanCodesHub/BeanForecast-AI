import streamlit as st

# -------------------------
# Page Config
# -------------------------
st.set_page_config(
    page_title="BeanForecast AI",
    page_icon="☕",
    layout="wide"
)

# -------------------------
# Load CSS
# -------------------------
with open("app/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -------------------------
# Hero Section
# -------------------------
st.markdown("""
<div class='hero'>
<h1 class='glow'>☕ BeanForecast AI</h1>
<h3>AI Powered Coffee Shop Revenue Prediction</h3>
<p>
Predict your coffee shop's daily revenue using Machine Learning.
</p>
</div>
""", unsafe_allow_html=True)

st.write("")
st.markdown("""
<div class="floating" style="font-size:90px;text-align:center;">
☕
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="glow">
☕ BeanForecast AI
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h2>🤖 AI Prediction</h2>
<p>Predict Coffee Shop Revenue</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="typewriter">
AI Powered Coffee Shop Revenue Prediction
</div>
""", unsafe_allow_html=True)

# -------------------------
# KPI Cards
# -------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class='card'>
        <h3>🎯 Accuracy</h3>
        <div class='metric'>94%</div>
        <p>Linear Regression Model</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='card'>
        <h3>📊 Dataset</h3>
        <div class='metric'>5000</div>
        <p>Rows</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='card'>
        <h3>🤖 AI Model</h3>
        <div class='metric'>Ready</div>
        <p>Prediction Pipeline</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# -------------------------
# About Project
# -------------------------
st.subheader("📌 About This Project")

st.write("""
BeanForecast AI is an end-to-end Machine Learning project built to predict
daily coffee shop revenue using business-related features.

The model analyzes:

- 🌡 Temperature
- 👣 Foot Traffic
- 💵 Average Order Value
- 📅 Day of Week
- 🍂 Season
- 🎁 Promotions
- 🎉 Holidays
- 🌙 Ramadan
- ☕ Top Selling Product
""")

st.write("")

# -------------------------
# Features
# -------------------------
st.subheader("🚀 Features")

c1, c2 = st.columns(2)

with c1:
    st.success("✅ Machine Learning Prediction")
    st.success("✅ Interactive Dashboard")
    st.success("✅ Beautiful Dark Theme")

with c2:
    st.success("✅ Business Analytics")
    st.success("✅ Real Time Prediction")
    st.success("✅ Portfolio Ready Project")

st.write("")
st.write("")

# -------------------------
# Performance
# -------------------------
st.subheader("📈 Model Performance")

col1, col2, col3 = st.columns(3)

col1.metric("MAE", "103")
col2.metric("RMSE", "130")
col3.metric("R² Score", "0.94")

st.divider()

st.info("👉 Open the **Predict** page from the left sidebar to estimate daily revenue.")