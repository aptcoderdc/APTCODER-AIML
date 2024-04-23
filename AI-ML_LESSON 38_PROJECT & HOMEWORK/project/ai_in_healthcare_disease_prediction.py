# Import necessary libraries
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Dummy healthcare data (example)
# Features: Age, Blood Pressure, Cholesterol Level
# Target: Disease (1 for presence, 0 for absence)
X = np.array([[25, 120, 180], [45, 140, 220], [60, 160, 240], [35, 130, 200], [50, 150, 230]])
y = np.array([0, 1, 1, 0, 1])

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build a simple disease prediction model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate model performance
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)
