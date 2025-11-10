import joblib
import pandas as pd
import os
from sklearn.metrics import classification_report

def evaluate(model_path, data_path):
    clf = joblib.load(model_path)
    df = pd.read_parquet(data_path)
    if "target" not in df.columns:
        raise ValueError("evaluation data must contain a 'target' column")
    X = df.drop("target", axis=1)
    y = df["target"]
    preds = clf.predict(X)
    print(classification_report(y, preds))

if __name__ == "__main__":
    model = "models/model.joblib"
    data = os.path.join("data","processed","example_features.parquet")
    if os.path.exists(model) and os.path.exists(data):
        evaluate(model, data)
    else:
        print("Model or data not found.")
