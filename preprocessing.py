import pandas as pd

def clean_data(df):

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove missing values
    df = df.dropna()

    # Convert invoice_date to datetime
    df["invoice_date"] = pd.to_datetime(
        df["invoice_date"],
        format="mixed",
        dayfirst=True,
        errors="coerce"
    )

    return df