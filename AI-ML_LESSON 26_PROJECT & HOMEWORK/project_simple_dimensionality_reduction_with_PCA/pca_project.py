# Simple Dimensionality Reduction with PCA Project
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# Generate random 2D data
np.random.seed(0)
X = np.random.randn(100, 2)  # 100 points in 2D space

# Apply PCA
pca = PCA(n_components=1)  # Reduce to 1 dimension
X_pca = pca.fit_transform(X)

# Plot original and reduced-dimensional data
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.scatter(X[:, 0], X[:, 1], color='blue')
plt.title("Original Data")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")

plt.subplot(1, 2, 2)
plt.scatter(X_pca, np.zeros_like(X_pca), color='red')
plt.title("Reduced Dimensionality Data")
plt.xlabel("Principal Component 1")

plt.tight_layout()
plt.show()
