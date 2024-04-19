# Homework: Model Deployment Evaluation

# Dummy data for demonstration purposes
X_test = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
y_test = [0, 1, 0]

# Dummy predictions for demonstration purposes
predictions = [0, 1, 0]

# Compute accuracy
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, predictions)

# Print the accuracy
print("Model Accuracy:", accuracy)
