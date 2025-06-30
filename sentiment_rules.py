def analyze_sentiment(text):
    """A simple rule-based sentiment analyzer."""
    positive_words = ['good', 'great', 'excellent', 'happy', 'love', 'awesome', 'fantastic', 'positive']
    negative_words = ['bad', 'terrible', 'poor', 'sad', 'hate', 'awful', 'horrible', 'negative']

    text = text.lower()
    pos = sum(word in text for word in positive_words)
    neg = sum(word in text for word in negative_words)

    if pos > neg:
        return "Positive"
    elif neg > pos:
        return "Negative"
    elif text.strip() == "":
        return "No feedback entered"
    else:
        return "Neutral"