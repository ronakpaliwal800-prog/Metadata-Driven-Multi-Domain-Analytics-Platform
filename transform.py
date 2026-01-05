# transform.py
import pandas as pd

def transform_data(df: pd.DataFrame):
    """
    Perform simple data transformations:
    - Strip whitespace from column names
    - Convert order_date to datetime
    """
    df.columns = df.columns.str.strip()
    if "order_date" in df.columns:
        df["order_date"] = pd.to_datetime(df["order_date"])
    print("🔄 Transformation complete")
    return df
