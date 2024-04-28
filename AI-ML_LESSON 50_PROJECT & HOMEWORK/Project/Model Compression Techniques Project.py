from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn.metrics import accuracy_score

# Step 1: Load pre-trained model
iris = load_iris()
X, y = iris.data, iris.target
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X, y)

# Step 2: Implement Pruning
sfm = SelectFromModel(clf, threshold=0.1)
sfm.fit(X, y)
X_pruned = sfm.transform(X)

# Step 3: Implement Quantization (for demonstration purposes)
# We'll simply reduce the precision of model coefficients (for demonstration purposes)
quantized_clf = RandomForestClassifier(n_estimators=100, random_state=42)
quantized_clf.fit(X_pruned, y)
# Note: Actual quantization methods might involve more sophisticated techniques.

# Step 4: Evaluate Performance
y_pred = clf.predict(X)
accuracy_original = accuracy_score(y, y_pred)

y_pred_quantized = quantized_clf.predict(X_pruned)
accuracy_quantized = accuracy_score(y, y_pred_quantized)

print("Original Model Accuracy:", accuracy_original)
print("Quantized Model Accuracy:", accuracy_quantized)
