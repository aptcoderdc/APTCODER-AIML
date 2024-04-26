import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Reshape, Conv2D, Conv2DTranspose
from tensorflow.keras.optimizers import Adam

# Load CIFAR-10 dataset
(X_train, _), (_, _) = cifar10.load_data()

# Normalize data and reshape
X_train = X_train.astype('float32') / 255.0

# Define autoencoder model for color images
autoencoder = Sequential([
    # Encoder
    Conv2D(32, kernel_size=3, strides=2, padding='same', activation='relu', input_shape=(32, 32, 3)),
    Conv2D(64, kernel_size=3, strides=2, padding='same', activation='relu'),
    Flatten(),
    Dense(256, activation='relu'),

    # Decoder
    Dense(4096, activation='relu'),
    Reshape((8, 8, 64)),
    Conv2DTranspose(64, kernel_size=3, strides=2, padding='same', activation='relu'),
    Conv2DTranspose(32, kernel_size=3, strides=2, padding='same', activation='relu'),
    Conv2DTranspose(3, kernel_size=3, strides=1, padding='same', activation='sigmoid')
])

# Compile autoencoder
autoencoder.compile(loss='mse', optimizer=Adam(learning_rate=0.001))

# Function to train autoencoder
def train_autoencoder(epochs=10, batch_size=128):
    autoencoder.fit(X_train, X_train, epochs=epochs, batch_size=batch_size)

# Train the autoencoder
train_autoencoder()

# Generate colorful artwork
def generate_artwork(n=10):
    noise = np.random.normal(0, 1, (n, 32, 32, 3))  # Generate noise for color images
    generated_images = autoencoder.predict(noise)
    plt.figure(figsize=(10, 10))
    for i in range(n):
        plt.subplot(1, n, i+1)
        plt.imshow(generated_images[i])
        plt.axis('off')
    plt.show()

# Generate and display colorful artwork
generate_artwork()
