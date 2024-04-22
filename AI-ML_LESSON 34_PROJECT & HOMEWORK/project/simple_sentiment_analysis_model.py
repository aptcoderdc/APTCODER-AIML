# Import necessary libraries
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Define sample data (positive and negative sentences)
positive_sentences = ["I love this movie!"]
negative_sentences = ["I hate Mondays.", "The service was terrible.", "Worst movie ever!" ,"The food was worst."]

# Combine positive and negative sentences
sentences = positive_sentences + negative_sentences
# Assign labels: 1 for positive sentences, 0 for negative sentences
labels = np.array([1] * len(positive_sentences) + [0] * len(negative_sentences))

# Create a CountVectorizer to convert text data into numerical format
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(sentences)

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)

# Build a Naive Bayes classifier
model = MultinomialNB()
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate model performance
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)