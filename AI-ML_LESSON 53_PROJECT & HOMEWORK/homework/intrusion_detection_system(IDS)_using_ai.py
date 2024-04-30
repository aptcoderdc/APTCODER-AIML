import numpy as np
from sklearn.decomposition import PCA
from sklearn.ensemble import IsolationForest

# Dummy data for intrusion detection
def generate_data(num_samples=1000):
    normal_data = np.random.normal(loc=0, scale=1, size=(num_samples, 10))  # Normal data
    intrusion_data = np.random.uniform(low=-5, high=5, size=(int(num_samples * 0.1), 10))  # Intrusion data
    data = np.vstack((normal_data, intrusion_data))
    labels = np.concatenate((np.zeros(len(normal_data)), np.ones(len(intrusion_data))))
    return data, labels

# Generate dummy data
X, y = generate_data()

# Apply dimensionality reduction
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Train Isolation Forest model
clf = IsolationForest(contamination=0.1, random_state=42)
clf.fit(X)

# Predictions
y_pred = clf.predict(X)

# Display results
print("Intrusion Detection Results:")
print("Predicted labels:", y_pred)
