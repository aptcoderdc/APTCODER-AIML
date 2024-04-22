# Import necessary libraries
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Define sample data (positive and negative sentences)
positive_sentences = ["I love this movie!", "The food was delicious.", "Great experience!"]
negative_sentences = ["I hate Mondays.", "The service was terrible.", "Worst movie ever!"]

# Combine positive and negative sentences
sentences = positive_sentences + negative_sentences
# Assign labels: 1 for positive sentences, 0 for negative sentences
labels = np.array([1] * len(positive_sentences) + [0] * len(negative_sentences))

# Create a CountVectorizer to convert text data into numerical format
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(sentences)

# Build a Naive Bayes classifier
model = MultinomialNB()
model.fit(X, labels)

# Test the model with new sentences
new_sentences = ["The food was amazing!", "I didn't like the service."]
X_new = vectorizer.transform(new_sentences)
predictions = model.predict(X_new)

# Print predictions
for sentence, prediction in zip(new_sentences, predictions):
    sentiment = "Positive" if prediction == 1 else "Negative"
    print(f"Sentence: {sentence} | Sentiment: {sentiment}")
