# Simple Model Deployment Project

# Import necessary libraries
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Define a simple dataset for demonstration
X_train = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
y_train = np.array([0, 1, 0])

# Train a simple model (Random Forest classifier)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Define a function to make predictions
def predict(input_data):
    prediction = model.predict(input_data)
    return prediction

# Example usage
input_data = np.array([[1, 2, 3]])  # Example input data
output = predict(input_data)
print("Prediction:", output)
