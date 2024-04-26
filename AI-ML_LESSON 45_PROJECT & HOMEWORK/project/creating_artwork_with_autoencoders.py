# Importing libraries
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Load Fashion MNIST dataset
(X_train, _), (_, _) = fashion_mnist.load_data()

# Normalize data
X_train = X_train.astype('float32') / 255.0

# Flatten the images
X_train = X_train.reshape((-1, 28*28))

# Define autoencoder model
autoencoder = Sequential([
    Dense(128, activation='relu', input_shape=(784,)),
    Dense(64, activation='relu'),
    Dense(32, activation='relu'),
    Dense(64, activation='relu'),
    Dense(128, activation='relu'),
    Dense(784, activation='sigmoid')
])

# Compile the model
autoencoder.compile(optimizer='adam', loss='binary_crossentropy')

# Train the autoencoder
autoencoder.fit(X_train, X_train, epochs=20, batch_size=256, shuffle=True)

def generate_artwork(n=10):
    noise = np.random.normal(0, 1, (n, 784))  # Generate noise of shape (n, 784)
    generated_images = autoencoder.predict(noise)
    plt.figure(figsize=(10, 10))
    for i in range(n):
        plt.subplot(1, n, i+1)
        plt.imshow(generated_images[i].reshape(28, 28), cmap='gray')
        plt.axis('off')
    plt.show()


# Generate and display new artwork
generate_artwork()
