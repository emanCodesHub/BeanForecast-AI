import streamlit as st

# ----------------------------
# Page Config
# ----------------------------

st.set_page_config(
    page_title="BeanForecast AI",
    page_icon="☕",
    layout="wide"
)

# ----------------------------
# Load CSS
# ----------------------------

with open("app/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ----------------------------
# Sidebar
# ----------------------------

st.sidebar.image("https://img.icons8.com/color/96/coffee-to-go.png", width=80)

st.sidebar.title("BeanForecast AI")

st.sidebar.markdown("---")

st.sidebar.success("Machine Learning Project")

st.sidebar.write("Developer")

st.sidebar.info("👩‍💻 Eman")

st.sidebar.write("Algorithm")

st.sidebar.info("Linear Regression")

# ----------------------------
# HERO
# ----------------------------

st.markdown("""

<div class="hero">

<h1>☕ BeanForecast AI</h1>

<h3>AI Powered Coffee Shop Revenue Prediction</h3>

<p>

Predict Daily Coffee Shop Revenue using Machine Learning.

</p>

</div>

""", unsafe_allow_html=True)

# ----------------------------
# Dashboard Cards
# ----------------------------

col1,col2,col3=st.columns(3)

with col1:

    st.markdown("""

<div class="card">

<h3>📈 Model</h3>

<div class="metric">

Linear Regression

</div>

</div>

""",unsafe_allow_html=True)

with col2:

    st.markdown("""

<div class="card">

<h3>🎯 Accuracy</h3>

<div class="metric">

94%

</div>

</div>

""",unsafe_allow_html=True)

with col3:

    st.markdown("""

<div class="card">

<h3>☕ Project</h3>

<div class="metric">

BeanForecast AI

</div>

</div>

""",unsafe_allow_html=True)

st.write("")

st.header("🚀 Welcome")

st.write("Fill the prediction form below to estimate today's coffee shop revenue.")