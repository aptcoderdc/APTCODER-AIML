import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

# Step 1: Dataset Preparation
iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 2: Model Development
model = MLPClassifier(hidden_layer_sizes=(10,), activation='relu', solver='adam', max_iter=1000, random_state=42)
model.fit(X_train, y_train)

# Step 3: Model Evaluation
accuracy = model.score(X_test, y_test)
print("Test Accuracy:", accuracy)

# Step 4: Conclusion
print("Simple neural network model for Iris dataset completed.")
