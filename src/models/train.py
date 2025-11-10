import os
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def train(processed_path):
    df = pd.read_parquet(processed_path)
    if "target" not in df.columns:
        raise ValueError("Processed data must contain a 'target' column for this simple trainer.")
    X = df.drop("target", axis=1)
    y = df["target"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    clf = RandomForestClassifier(n_estimators=50, random_state=42)
    clf.fit(X_train, y_train)
    preds = clf.predict(X_test)
    acc = accuracy_score(y_test, preds)
    os.makedirs("models", exist_ok=True)
    joblib.dump(clf, "models/model.joblib")
    print(f"Training complete. Accuracy: {acc:.4f}. Model saved to models/model.joblib")

if __name__ == "__main__":
    path = os.path.join("data","processed","example_features.parquet")
    if os.path.exists(path):
        train(path)
    else:
        print("No feature file found. Run feature builder first.")
