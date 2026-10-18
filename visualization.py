import plotly.express as px

# -----------------------------
# Sales by Category
# -----------------------------
def category_sales_chart(df):

    temp = df.copy()
    temp["Total"] = temp["quantity"] * temp["price"]

    category_sales = (
        temp.groupby("category", as_index=False)["Total"]
        .sum()
        .rename(columns={"Total": "Total Sales"})
    )

    fig = px.bar(
        category_sales,
        x="category",
        y="Total Sales",
        color="category",
        title="Sales by Category"
    )

    return fig


# -----------------------------
# Gender Distribution
# -----------------------------
def gender_chart(df):

    gender = (
        df["gender"]
        .value_counts()
        .reset_index()
    )

    gender.columns = ["Gender", "Count"]

    fig = px.pie(
        gender,
        names="Gender",
        values="Count",
        title="Gender Distribution"
    )

    return fig


# -----------------------------
# Shopping Mall Revenue
# -----------------------------
def mall_sales_chart(df):

    temp = df.copy()
    temp["Total"] = temp["quantity"] * temp["price"]

    mall = (
        temp.groupby("shopping_mall", as_index=False)["Total"]
        .sum()
        .rename(columns={"Total": "Total Sales"})
    )

    fig = px.bar(
        mall,
        x="shopping_mall",
        y="Total Sales",
        color="shopping_mall",
        title="Revenue by Shopping Mall"
    )

    return fig


# -----------------------------
# Payment Method
# -----------------------------
def payment_chart(df):

    payment = (
        df["payment_method"]
        .value_counts()
        .reset_index()
    )

    payment.columns = ["Payment Method", "Count"]

    fig = px.pie(
        payment,
        names="Payment Method",
        values="Count",
        title="Payment Method Distribution"
    )

    return fig


# -----------------------------
# Age Distribution
# -----------------------------
def age_chart(df):

    fig = px.histogram(
        df,
        x="age",
        nbins=20,
        title="Age Distribution"
    )

    return fig


# -----------------------------
# Monthly Sales Trend
# -----------------------------
def monthly_sales_chart(df):

    temp = df.copy()

    temp["Total"] = temp["quantity"] * temp["price"]

    temp["Month"] = temp["invoice_date"].dt.to_period("M").astype(str)

    monthly = (
        temp.groupby("Month", as_index=False)["Total"]
        .sum()
    )

    fig = px.line(
        monthly,
        x="Month",
        y="Total",
        markers=True,
        title="Monthly Sales Trend"
    )

    return fig