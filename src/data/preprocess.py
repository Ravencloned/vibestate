import pandas as pd
import os

def basic_clean(df):
    # simple placeholder cleaning: drop NA and reset index
    df = df.dropna().reset_index(drop=True)
    return df

if __name__ == "__main__":
    path = os.path.join("data","processed","example.parquet")
    if os.path.exists(path):
        df = pd.read_parquet(path)
        df = basic_clean(df)
        df.to_parquet(os.path.join("data","processed","example_clean.parquet"), index=False)
        print("Saved example_clean.parquet")
    else:
        print("Processed file not found. Run src/data/make_dataset.py first.")
