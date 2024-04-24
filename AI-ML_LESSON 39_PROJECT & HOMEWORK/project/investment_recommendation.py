# Import necessary libraries
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Dummy financial data (example)
# Features: Age, Income, Savings
# Target: Investment Recommendation (1 for recommended, 0 for not recommended)
X = np.array([[25, 50000, 20000], [35, 60000, 25000], [45, 70000, 30000], [30, 55000, 22000], [40, 65000, 27000]])
y = np.array([0, 0, 1, 0, 0])

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build a simple investment recommendation model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate model performance
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)
