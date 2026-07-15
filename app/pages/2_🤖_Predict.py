import streamlit as st
import pandas as pd
import joblib
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Revenue Prediction",
    page_icon="☕",
    layout="wide"
)



# -----------------------------
# Title
# -----------------------------
st.title("☕ BeanForecast AI")
st.subheader("Coffee Shop Revenue Prediction Dashboard")

# -----------------------------
# Load ML Model
# -----------------------------
pipeline = joblib.load("models/beanforecast_pipeline.pkl")

st.markdown("### 📝 Enter Coffee Shop Details")

# -----------------------------
# Input Layout
# -----------------------------
col1, col2 = st.columns(2)

with col1:

    day = st.selectbox(
        "📅 Day of Week",
        [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
        ]
    )

    month = st.slider("📆 Month", 1, 12, 1)

    season = st.selectbox(
        "🍂 Season",
        [
            "Winter",
            "Spring",
            "Summer",
            "Autumn"
        ]
    )

    weekend = st.selectbox("🏖 Weekend", [0, 1])

    holiday = st.selectbox("🎉 Holiday", [0, 1])

    ramadan = st.selectbox("🌙 Ramadan", [0, 1])

    promotion = st.selectbox("🎁 Promotion", [0, 1])

with col2:

    nearby = st.selectbox("🎵 Nearby Event", [0, 1])

    temperature = st.number_input(
        "🌡 Temperature (°C)",
        value=25
    )

    rainfall = st.number_input(
        "🌧 Rainfall (mm)",
        value=0.0
    )

    foot = st.number_input(
        "👣 Foot Traffic",
        value=200
    )

    avg = st.number_input(
        "💵 Average Order Value",
        value=500.0
    )

    product = st.selectbox(
        "☕ Top Selling Product",
        [
            "Latte",
            "Espresso",
            "Cappuccino",
            "Americano",
            "Mocha"
        ]
    )

    hours = st.number_input(
        "🕒 Working Hours",
        value=12
    )

st.write("")

if st.button("🚀 Predict Revenue", use_container_width=True):

    input_data = pd.DataFrame({
        "DayOfWeek": [day],
        "Month": [month],
        "Season": [season],
        "Weekend": [weekend],
        "Holiday": [holiday],
        "Ramadan": [ramadan],
        "Promotion": [promotion],
        "NearbyEvent": [nearby],
        "TemperatureC": [temperature],
        "RainfallMM": [rainfall],
        "FootTraffic": [foot],
        "AvgOrderValue": [avg],
        "TopSellingProduct": [product],
        "WorkingHours": [hours]
    })

    prediction = pipeline.predict(input_data)
        # -----------------------------
    # Prediction Result
    # -----------------------------
    revenue = prediction[0]

    st.markdown("---")

    st.success(f"💰 Predicted Revenue: Rs. {revenue:,.2f}")

    if revenue >= 1500:
        st.balloons()
        st.success("🟢 Excellent Business Day Expected!")

    elif revenue >= 1000:
        st.warning("🟡 Average Business Day Expected")

    else:
        st.error("🔴 Low Revenue Expected")

    # -----------------------------
    # AI Business Insights
    # -----------------------------
    st.markdown("## 🤖 AI Business Insights")

    insights = []

    if revenue > 1700:
        insights.append("🟢 Excellent revenue is expected today.")

    elif revenue > 1200:
        insights.append("🟡 Good revenue is expected today.")

    else:
        insights.append("🔴 Revenue may be lower than usual.")

    if promotion == 1:
        insights.append("🎁 Promotion campaign is likely to increase sales.")

    if weekend == 1:
        insights.append("☕ Weekend usually brings more customers.")

    if holiday == 1:
        insights.append("🎉 Holiday may increase customer visits.")

    if ramadan == 1:
        insights.append("🌙 Ramadan may affect customer buying patterns.")

    if nearby == 1:
        insights.append("🎵 Nearby events can increase customer traffic.")

    if temperature > 32:
        insights.append("🥤 Hot weather may increase cold drink sales.")

    elif temperature < 15:
        insights.append("☕ Cold weather may increase coffee sales.")

    if rainfall > 10:
        insights.append("🌧 Heavy rain may reduce walk-in customers.")

    if foot > 350:
        insights.append("🚶 High foot traffic detected.")

    elif foot < 150:
        insights.append("⚠ Low foot traffic detected.")

    if avg > 600:
        insights.append("💳 Customers are spending more per order.")

    if hours > 12:
        insights.append("🕒 Longer working hours may increase revenue.")

    for item in insights:
        st.info(item)

    # -----------------------------
    # KPI Cards
    # -----------------------------
    st.markdown("---")
    st.subheader("📊 Business Summary")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "💰 Revenue",
            f"Rs. {revenue:,.2f}"
        )

    with c2:

        if revenue >= 1500:
            status = "Excellent"

        elif revenue >= 1000:
            status = "Average"

        else:
            status = "Low"

        st.metric(
            "📈 Status",
            status
        )

    with c3:
        st.metric(
            "👣 Foot Traffic",
            foot
        )


        # -----------------------------
    # Revenue Performance
    # -----------------------------
    st.markdown("---")
    st.subheader("📈 Revenue Performance")

    score = min(revenue / 2000, 1.0)

    st.progress(score)

    st.caption(f"Business Score : {score*100:.1f}%")

    # -----------------------------
    # AI Recommendations
    # -----------------------------
    st.markdown("## 💡 AI Recommendations")

    recommendations = []

    if promotion == 0:
        recommendations.append("🎁 Consider running promotions to boost sales.")

    if foot < 200:
        recommendations.append("📢 Increase marketing to attract more customers.")

    if rainfall > 10:
        recommendations.append("🚚 Offer delivery discounts during rainy weather.")

    if weekend == 1:
        recommendations.append("☕ Stock extra coffee and snacks for weekend demand.")

    if hours < 10:
        recommendations.append("🕒 Increase working hours to serve more customers.")

    if avg < 400:
        recommendations.append("💳 Introduce combo deals to increase average order value.")

    if len(recommendations) == 0:
        st.success("✅ Everything looks great! Keep your current strategy.")

    for rec in recommendations:
        st.warning(rec)

    # -----------------------------
    # PDF Report
    # -----------------------------
    st.markdown("---")
    st.subheader("📄 Download Prediction Report")

    if st.button("📥 Generate PDF Report"):

        pdf_file = "Coffee_Revenue_Report.pdf"

        doc = SimpleDocTemplate(pdf_file)
        styles = getSampleStyleSheet()

        story = []

        story.append(Paragraph("BeanForecast AI", styles["Title"]))
        story.append(Paragraph("Coffee Shop Revenue Prediction Report", styles["Heading2"]))
        story.append(Paragraph("<br/>", styles["Normal"]))

        story.append(Paragraph(f"<b>Predicted Revenue:</b> Rs. {revenue:,.2f}", styles["BodyText"]))
        story.append(Paragraph(f"<b>Day:</b> {day}", styles["BodyText"]))
        story.append(Paragraph(f"<b>Season:</b> {season}", styles["BodyText"]))
        story.append(Paragraph(f"<b>Temperature:</b> {temperature} °C", styles["BodyText"]))
        story.append(Paragraph(f"<b>Foot Traffic:</b> {foot}", styles["BodyText"]))
        story.append(Paragraph(f"<b>Average Order Value:</b> Rs. {avg}", styles["BodyText"]))
        story.append(Paragraph(f"<b>Working Hours:</b> {hours}", styles["BodyText"]))

        story.append(Paragraph("<br/>AI Insights", styles["Heading2"]))

        for item in insights:
            story.append(Paragraph(item, styles["BodyText"]))

        doc.build(story)

        with open(pdf_file, "rb") as file:
            st.download_button(
                "⬇ Download PDF",
                file,
                file_name="Coffee_Revenue_Report.pdf",
                mime="application/pdf"
            )

    st.success("🎉 Prediction Completed Successfully!")