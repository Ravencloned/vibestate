import pandas as pd
import os

def build_features(df):
    # placeholder: if numeric columns exist, return as-is
    return df

if __name__ == "__main__":
    p = os.path.join("data","processed","example_clean.parquet")
    if os.path.exists(p):
        df = pd.read_parquet(p)
        feats = build_features(df)
        feats.to_parquet(os.path.join("data","processed","example_features.parquet"), index=False)
        print("Saved example_features.parquet")
    else:
        print("No cleaned data to build features from.")
