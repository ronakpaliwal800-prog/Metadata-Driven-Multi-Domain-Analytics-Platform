# validation.py
import pandas as pd

def validate_data(df: pd.DataFrame):
    errors = []

    # Check for missing values
    if df.isnull().sum().sum() > 0:
        errors.append("Missing values detected")

    # Check for negative prices or quantities
    if "price" in df.columns and (df["price"] < 0).any():
        errors.append("Negative prices found")
    if "quantity" in df.columns and (df["quantity"] < 0).any():
        errors.append("Negative quantities found")

    # Check date format
    if "order_date" in df.columns:
        try:
            pd.to_datetime(df["order_date"])
        except Exception:
            errors.append("Invalid date format in order_date")

    if errors:
        print("⚠️ Data Validation Errors:")
        for e in errors:
            print("-", e)
        return False
    else:
        print("✅ Data validation passed")
        return True
