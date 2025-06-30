import re
from typing import List
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

def clean_text(text: str) -> str:
    """Lowercase, remove symbols, and stopwords from text."""
    # Lowercase
    text = text.lower()
    # Remove non-alphabetic characters
    text = re.sub(r'[^a-z\s]', '', text)
    # Remove stopwords
    words = [word for word in text.split() if word not in ENGLISH_STOP_WORDS]
    return ' '.join(words)

def preprocess_texts(texts: List[str]) -> List[str]:
    """Clean and normalize a list of texts."""
    return [clean_text(t) for t in texts]