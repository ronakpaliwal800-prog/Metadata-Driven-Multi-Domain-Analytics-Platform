# load.py
from sqlalchemy import create_engine
import psycopg2
import pandas as pd
from config import DB_CONFIG

def load_data(df: pd.DataFrame):
    """
    Load data into PostgreSQL table.
    """
    conn_str = f"postgresql+psycopg2://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
    engine = create_engine(conn_str)
    df.to_sql('orders', engine, if_exists='replace', index=False)
    print("🗄️ Data loaded into PostgreSQL")
