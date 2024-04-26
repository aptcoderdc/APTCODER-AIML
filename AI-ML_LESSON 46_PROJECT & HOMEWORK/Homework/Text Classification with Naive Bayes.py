import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Sample data for sentiment analysis
texts = ["I love this movie!", "This movie is terrible.", "The acting was superb.", "I didn't like the plot."]
labels = [1, 0, 1, 0]  # 1 for positive, 0 for negative sentiment

# Split data into train and test sets
train_texts, test_texts, train_labels, test_labels = train_test_split(texts, labels, test_size=0.2, random_state=42)

# Vectorize text data
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(train_texts)
X_test = vectorizer.transform(test_texts)

# Train a Naive Bayes classifier
classifier = MultinomialNB()
classifier.fit(X_train, train_labels)

# Predict on the test set
predictions = classifier.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(test_labels, predictions)
print("Test Accuracy:", accuracy)
