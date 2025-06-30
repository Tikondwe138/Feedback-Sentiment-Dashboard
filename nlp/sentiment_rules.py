from textblob import TextBlob
from typing import List, Union

def classify_sentiment(text: Union[str, None]) -> str:
    """
    Classify sentiment using TextBlob polarity.
    Returns: 'positive', 'negative', 'neutral', or 'no feedback entered'
    """
    if not text or not text.strip():
        return "no feedback entered"
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.1:
        return "positive"
    elif polarity < -0.1:
        return "negative"
    else:
        return "neutral"

def classify_sentiments(texts: List[Union[str, None]]) -> List[str]:
    """
    Classify a list of texts using TextBlob sentiment analysis.
    Handles empty or None entries gracefully.
    """
    return [classify_sentiment(t) for t in texts]