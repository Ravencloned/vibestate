import joblib
import pandas as pd
import os

def predict(model_path, data_path):
    clf = joblib.load(model_path)
    df = pd.read_parquet(data_path)
    preds = clf.predict(df)
    return preds

if __name__ == "__main__":
    model = "models/model.joblib"
    data = os.path.join("data","processed","example_features.parquet")
    if os.path.exists(model) and os.path.exists(data):
        print(predict(model, data)[:10])
    else:
        print("Model or data not found.")
