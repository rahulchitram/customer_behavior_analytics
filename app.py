import streamlit as st
import pandas as pd

from analytics import calculate_metrics, business_insights
from preprocessing import clean_data
from visualization import (
    category_sales_chart,
    gender_chart,
    mall_sales_chart,
    payment_chart,
    age_chart,
    monthly_sales_chart
)
from reports import generate_report

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------
st.set_page_config(
    page_title="Customer Behavior Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------------------------------------------
# Title
# ---------------------------------------------------
st.title("📊 Customer Behavior Analytics Dashboard")
st.markdown("Analyze customer shopping behavior using interactive dashboards.")
st.divider()

# ---------------------------------------------------
# Upload CSV
# ---------------------------------------------------
uploaded_file = st.file_uploader(
    "Upload Customer Shopping Dataset",
    type=["csv"]
)

if uploaded_file is not None:

    # -----------------------------
    # Read Dataset
    # -----------------------------
    df = pd.read_csv(uploaded_file)

    # -----------------------------
    # Clean Dataset
    # -----------------------------
    df = clean_data(df)

    # -----------------------------
    # Sidebar Filters
    # -----------------------------
    st.sidebar.header("🔍 Filters")

    gender = st.sidebar.multiselect(
        "Gender",
        options=sorted(df["gender"].unique()),
        default=sorted(df["gender"].unique())
    )

    category = st.sidebar.multiselect(
        "Category",
        options=sorted(df["category"].unique()),
        default=sorted(df["category"].unique())
    )

    mall = st.sidebar.multiselect(
        "Shopping Mall",
        options=sorted(df["shopping_mall"].unique()),
        default=sorted(df["shopping_mall"].unique())
    )

    payment = st.sidebar.multiselect(
        "Payment Method",
        options=sorted(df["payment_method"].unique()),
        default=sorted(df["payment_method"].unique())
    )

    # -----------------------------
    # Apply Filters
    # -----------------------------
    df = df[
        (df["gender"].isin(gender)) &
        (df["category"].isin(category)) &
        (df["shopping_mall"].isin(mall)) &
        (df["payment_method"].isin(payment))
    ]

    # -----------------------------
    # Calculate Metrics
    # -----------------------------
    metrics = calculate_metrics(df)
    insights = business_insights(df)

    st.success("Dataset Uploaded Successfully ✅")

    # =================================================
    # KPI CARDS
    # =================================================
    st.subheader("📈 Dashboard Metrics")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "💰 Total Sales",
        f"${metrics['Total Sales']:,.2f}"
    )

    c2.metric(
        "👥 Customers",
        metrics["Total Customers"]
    )

    c3.metric(
        "🎂 Average Age",
        metrics["Average Age"]
    )

    c4.metric(
        "🛍 Categories",
        metrics["Categories"]
    )

    st.divider()

    # =================================================
    # DATASET INFO
    # =================================================
    st.subheader("📋 Dataset Information")

    info1, info2 = st.columns(2)

    with info1:
        st.write(f"**Rows:** {df.shape[0]}")
        st.write(f"**Columns:** {df.shape[1]}")

    with info2:
        st.write(f"**Missing Values:** {df.isnull().sum().sum()}")
        st.write(f"**Duplicate Rows:** {df.duplicated().sum()}")

    st.divider()

    # =================================================
    # DATA PREVIEW
    # =================================================
    st.subheader("📄 Dataset Preview")

    st.dataframe(df, use_container_width=True)

    st.divider()

    # =================================================
    # CHARTS
    # =================================================
    st.subheader("📊 Interactive Charts")

    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(
            category_sales_chart(df),
            use_container_width=True
        )

    with col2:
        st.plotly_chart(
            gender_chart(df),
            use_container_width=True
        )

    col3, col4 = st.columns(2)

    with col3:
        st.plotly_chart(
            mall_sales_chart(df),
            use_container_width=True
        )

    with col4:
        st.plotly_chart(
            payment_chart(df),
            use_container_width=True
        )

    col5, col6 = st.columns(2)

    with col5:
        st.plotly_chart(
            age_chart(df),
            use_container_width=True
        )

    with col6:
        st.plotly_chart(
            monthly_sales_chart(df),
            use_container_width=True
        )

    st.divider()

    # =================================================
    # BUSINESS INSIGHTS
    # =================================================
    st.subheader("📌 Business Insights")

    i1, i2, i3 = st.columns(3)

    with i1:
        st.info(f"🏆 Best Category\n\n{insights['Best Category']}")

    with i2:
        st.info(f"🏬 Top Shopping Mall\n\n{insights['Top Shopping Mall']}")

    with i3:
        st.info(f"💳 Popular Payment Method\n\n{insights['Popular Payment']}")

    i4, i5, i6 = st.columns(3)

    with i4:
        st.success(f"💰 Average Purchase\n\n${insights['Average Purchase']:,.2f}")

    with i5:
        st.success(f"🛒 Total Items Sold\n\n{insights['Total Items Sold']}")

    with i6:
        st.success(f"👥 Most Common Age\n\n{insights['Most Common Age']}")

    st.divider()

    # =================================================
    # DOWNLOAD FILTERED DATA
    # =================================================
    st.subheader("📥 Download Filtered Dataset")

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇️ Download CSV",
        data=csv,
        file_name="filtered_customer_data.csv",
        mime="text/csv"
    )

    st.divider()

    # =================================================
    # PDF REPORT
    # =================================================
    st.subheader("📄 Generate Report")

    if st.button("Generate PDF Report"):

        pdf_path = generate_report(metrics, insights)

        with open(pdf_path, "rb") as pdf:

            st.download_button(
                label="📥 Download PDF",
                data=pdf,
                file_name="Customer_Report.pdf",
                mime="application/pdf"
            )

    st.divider()

    # =================================================
    # FOOTER
    # =================================================
    st.markdown(
        """
        ### 📌 Customer Behavior Analytics Dashboard

        **Technologies Used**

        - Python
        - Streamlit
        - Pandas
        - Plotly
        - ReportLab

        **Developed by:** Rahul
        """
    )