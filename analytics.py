import pandas as pd

# -----------------------------
# Dashboard Metrics
# -----------------------------
def calculate_metrics(df):

    total_sales = (df["quantity"] * df["price"]).sum()

    total_customers = df["customer_id"].nunique()

    average_age = round(df["age"].mean(), 2)

    total_categories = df["category"].nunique()

    metrics = {
        "Total Sales": total_sales,
        "Total Customers": total_customers,
        "Average Age": average_age,
        "Categories": total_categories
    }

    return metrics


# -----------------------------
# Business Insights
# -----------------------------
def business_insights(df):

    temp = df.copy()
    temp["Total"] = temp["quantity"] * temp["price"]

    insights = {

        "Best Category":
            temp.groupby("category")["Total"].sum().idxmax(),

        "Top Shopping Mall":
            temp.groupby("shopping_mall")["Total"].sum().idxmax(),

        "Popular Payment":
            temp["payment_method"].mode()[0],

        "Average Purchase":
            round(temp["Total"].mean(), 2),

        "Total Items Sold":
            int(temp["quantity"].sum()),

        "Most Common Age":
            int(temp["age"].mode()[0])

    }

    return insights