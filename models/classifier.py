import pickle
from typing import List

MODEL_PATH = "models/sentiment_model.pkl"

def load_model(model_path: str = MODEL_PATH):
    """Load and return the sentiment analysis model."""
    with open(model_path, "rb") as f:
        return pickle.load(f)

def predict_sentiment(model, texts: List[str]) -> List[str]:
    """Predict sentiment for a list of texts using the loaded model."""