# This is a placeholder for the final homework code.
# The final homework should include concepts from all 19 lessons.
# Below is a simple example demonstrating a homework showcase.

# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Dummy data for demonstration
# You can replace this with real data or more complex dummy data
# For simplicity, we will use randomly generated data
np.random.seed(0)
X = np.random.rand(100, 10)  # 100 samples, 10 features

# Step 1: Data preprocessing with Pandas
# Dummy DataFrame for demonstration
df = pd.DataFrame(X, columns=[f"feature_{i+1}" for i in range(X.shape[1])])

# Step 2: Data visualization with Matplotlib and Seaborn
# Plotting a histogram of one feature
plt.hist(df['feature_1'], bins=20, color='blue', alpha=0.5)
plt.xlabel('Feature 1')
plt.ylabel('Frequency')
plt.title('Histogram of Feature 1')
plt.show()

# Step 3: Dimensionality reduction with PCA
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Plotting PCA results
plt.scatter(X_pca[:, 0], X_pca[:, 1], c='r', marker='o')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA Projection')
plt.show()
