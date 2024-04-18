# Basic Data Compression with Autoencoders Homework
import numpy as np
import matplotlib.pyplot as plt

# Sample grayscale image data (3x3 pixels)
images = np.array([
    [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6], [0.7, 0.8, 0.9]],
    [[0.9, 0.8, 0.7], [0.6, 0.5, 0.4], [0.3, 0.2, 0.1]],
    [[0.5, 0.5, 0.5], [0.5, 0.5, 0.5], [0.5, 0.5, 0.5]]
])

# Flatten the images
X = images.reshape(len(images), -1)

# Define autoencoder architecture (1 hidden layer)
input_dim = X.shape[1]
encoding_dim = 2
hidden_dim = 3

# Initialize weights and biases randomly
weights = {
    'encoder': np.random.randn(input_dim, encoding_dim),
    'decoder': np.random.randn(encoding_dim, input_dim)
}
biases = {
    'encoder': np.random.randn(encoding_dim),
    'decoder': np.random.randn(input_dim)
}

# Implement autoencoder forward pass
def forward_pass(X, weights, biases):
    # Encoder
    encoding = np.dot(X, weights['encoder']) + biases['encoder']
    # Decoder
    reconstructed = np.dot(encoding, weights['decoder']) + biases['decoder']
    return encoding, reconstructed

# Train the autoencoder (skip for simplicity)

# Perform forward pass to compress and reconstruct images
encoded, reconstructed = forward_pass(X, weights, biases)

# Visualize original and reconstructed images
fig, axes = plt.subplots(nrows=2, ncols=len(images), figsize=(10, 4))
for i in range(len(images)):
    axes[0, i].imshow(images[i], cmap='gray')
    axes[0, i].axis('off')
    axes[1, i].imshow(reconstructed[i].reshape(3, 3), cmap='gray')
    axes[1, i].axis('off')
axes[0, 0].set_title('Original')
axes[1, 0].set_title('Reconstructed')
plt.tight_layout()
plt.show()
