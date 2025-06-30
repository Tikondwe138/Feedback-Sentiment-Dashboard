import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from typing import List, Dict

def extract_keywords_by_sentiment(
    df: pd.DataFrame,
    text_col: str = "feedback",
    sentiment_col: str = "sentiment",
    top_n: int = 10
) -> Dict[str, List[str]]:
    """
    Extract top N keywords for each sentiment class.
    Returns a dict: {sentiment: [keywords]}
    """
    keywords = {}
    sentiments = df[sentiment_col].unique()
    for sentiment in sentiments:
        texts = df[df[sentiment_col] == sentiment][text_col].astype(str)
        vectorizer = CountVectorizer(stop_words="english", max_features=top_n)
        X = vectorizer.fit_transform(texts)
        keywords[sentiment] = vectorizer.get_feature_names_out().tolist()