from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Step 1: Prepare Data
X, y = load_iris(return_X_y=True)

# Step 2: Train the original model
clf_original = DecisionTreeClassifier(random_state=42)
clf_original.fit(X, y)
original_accuracy = accuracy_score(y, clf_original.predict(X))

# Step 3: Implement Pruning
# Decision trees in scikit-learn do not support pruning after training.
# So, we'll train a new decision tree with a maximum depth to simulate pruning.
max_depth = 3
clf_pruned = DecisionTreeClassifier(max_depth=max_depth, random_state=42)
clf_pruned.fit(X, y)
pruned_accuracy = accuracy_score(y, clf_pruned.predict(X))

# Step 4: Implement Quantization (for demonstration purposes)
# We won't quantize the model in this example since scikit-learn does not provide built-in support for quantization.

# Step 5: Evaluate Performance
print("Original Model Accuracy:", original_accuracy)
print("Pruned Model Accuracy:", pruned_accuracy)
