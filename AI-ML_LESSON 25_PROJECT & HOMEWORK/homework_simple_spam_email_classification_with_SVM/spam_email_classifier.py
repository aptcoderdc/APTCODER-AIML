# Simple Spam Email Classification with SVM Homework
from sklearn import svm
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Sample email data (spam and non-spam)
emails = [
    ("Hey, buy our latest product!", "spam"),
    ("Reminder: Your appointment tomorrow", "spam"),
    ("Hey, buy our recent item!", "spam"),
    ("Get rich quick scheme inside", "spam"),
    ("Meeting agenda attached", "non-spam")
]

# Separate text and labels
X = [email[0] for email in emails]
y = [email[1] for email in emails]

# Convert text data into numerical features
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

# Train the SVM model
clf = svm.SVC(kernel='linear')
clf.fit(X_train, y_train)

# Test the model
y_pred = clf.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
