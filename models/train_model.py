import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

DATA_PATH = "../data/labeled_feedback.csv"  # Update path as needed
MODEL_PATH = "sentiment_model.pkl"

def train():
    # Load data
    df = pd.read_csv(DATA_PATH)
    X = df["feedback"]
    y = df["sentiment"]

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Vectorize text
    vectorizer = TfidfVectorizer()
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    # Train model
    clf = LogisticRegression(max_iter=1000)
    clf.fit(X_train_vec, y_train)

    # Save model and vectorizer together
    with open(MODEL_PATH, "wb") as f:
        pickle.dump({"vectorizer": vectorizer, "model": clf}, f)

    print("Model trained and saved to", MODEL_PATH)
    print("Test accuracy:", clf.score(X_test_vec, y_test))

if __name__ == "__main__":
    train()