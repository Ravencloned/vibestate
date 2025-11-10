import os
import pandas as pd

RAW_DIR = os.path.join("data","raw")
PROCESSED_DIR = os.path.join("data","processed")
os.makedirs(PROCESSED_DIR, exist_ok=True)

def load_raw_csv(filename):
    path = os.path.join(RAW_DIR, filename)
    return pd.read_csv(path)

def save_parquet(df, name):
    df.to_parquet(os.path.join(PROCESSED_DIR, name), index=False)

if __name__ == "__main__":
    example = os.path.join(RAW_DIR, "example.csv")
    if os.path.exists(example):
        df = load_raw_csv("example.csv")
        save_parquet(df, "example.parquet")
        print("Processed example.csv -> example.parquet")
    else:
        print("No data found in data/raw. Place raw files there or run scripts/download_data.ps1")
