import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="👨‍💻",
    layout="wide"
)

# Load CSS
with open("app/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("👨‍💻 About BeanForecast AI")

st.markdown("""
## ☕ BeanForecast AI

BeanForecast AI is a Machine Learning project developed to predict
daily coffee shop revenue using business and environmental factors.

This system helps coffee shop owners estimate expected revenue and
make better business decisions.
""")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("📌 Project Details")

    st.info("""
**Project Name:** BeanForecast AI

**Algorithm:** Linear Regression

**Language:** Python

**Framework:** Streamlit

**Machine Learning:** Scikit-Learn

**Visualization:** Plotly

**Dataset:** 5000 Coffee Shop Records
""")

with col2:
    st.subheader("👨‍💻 Developer")

    st.success("""
Name: Eman

Role: AI / Machine Learning Student

University Project

BeanForecast AI Version 2.0
""")

st.divider()

st.subheader("🚀 Features")

st.markdown("""
- ✅ AI Revenue Prediction
- ✅ Business Insights
- ✅ Interactive Dashboard
- ✅ Analytics Charts
- ✅ Machine Learning Model
- ✅ Premium Dark UI
""")

st.divider()

st.markdown(
    "<center><h3>☕ Thank you for using BeanForecast AI ❤️</h3></center>",
    unsafe_allow_html=True
)