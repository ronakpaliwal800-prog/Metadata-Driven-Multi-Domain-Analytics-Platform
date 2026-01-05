# extract.py
import pandas as pd

def extract_data(file_path):
    """
    Extract data from a CSV file.
    """
    df = pd.read_csv(file_path)
    print(f"📥 Extracted {len(df)} records")
    return df
