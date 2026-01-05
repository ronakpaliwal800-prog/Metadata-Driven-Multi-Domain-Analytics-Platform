# main.py
from extract import extract_data
from transform import transform_data
from load import load_data
from validation import validate_data

# ETL pipeline
df = extract_data("data/raw/orders.csv")
df = transform_data(df)

if validate_data(df):
    load_data(df)
