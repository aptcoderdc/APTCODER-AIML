# Import necessary library
import numpy as np

# Dummy data for demonstration purposes
y_true = np.array([0, 1, 1, 0, 1, 1, 1, 0, 1, 1])
y_pred = np.array([0, 1, 1, 1, 1, 0, 1, 0, 1, 0])

# Compute confusion matrix
from sklearn.metrics import confusion_matrix
conf_matrix = confusion_matrix(y_true, y_pred)

# Print confusion matrix
print("Confusion Matrix:")
print(conf_matrix)

# Compute precision, recall, and F1-score
from sklearn.metrics import precision_score, recall_score, f1_score
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)

# Print evaluation metrics
print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1)
