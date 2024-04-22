from textblob import TextBlob

# Sample text for sentiment analysis
text = "I love this product! It's amazing."

# Perform sentiment analysis using TextBlob
blob = TextBlob(text)
sentiment = blob.sentiment

# Print sentiment polarity and subjectivity
print("Sentiment Polarity:", sentiment.polarity)
print("Sentiment Subjectivity:", sentiment.subjectivity)

# Classify sentiment
if sentiment.polarity > 0:
    print("Sentiment: Positive")
elif sentiment.polarity == 0:
    print("Sentiment: Neutral")
else:
    print("Sentiment: Negative")
