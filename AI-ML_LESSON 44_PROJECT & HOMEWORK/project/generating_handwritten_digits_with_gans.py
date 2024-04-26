import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Reshape, Flatten
from tensorflow.keras.optimizers import Adam

# Load MNIST dataset
(X_train, _), (_, _) = mnist.load_data()

# Normalize data and reshape
X_train = X_train.astype('float32') / 255.0
X_train = X_train.reshape((-1, 28*28))

# Define generator model
generator = Sequential([
    Dense(128, input_dim=100, activation='relu'),
    Dense(784, activation='sigmoid'),
    Reshape((28, 28))
])

# Define discriminator model
discriminator = Sequential([
    Flatten(input_shape=(28, 28)),
    Dense(128, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compile discriminator
discriminator.compile(loss='binary_crossentropy', optimizer=Adam(learning_rate=0.0002), metrics=['accuracy'])

# Combine generator and discriminator into GAN
discriminator.trainable = False
gan = Sequential([generator, discriminator])
gan.compile(loss='binary_crossentropy', optimizer=Adam(learning_rate=0.0002))

# Function to train GAN
def train_gan(epochs=100, batch_size=128):
    for epoch in range(epochs):
        noise = np.random.normal(0, 1, (batch_size, 100))
        generated_images = generator.predict(noise)
        real_images = X_train[np.random.randint(0, X_train.shape[0], batch_size)]

        # Ensure generated_images have the correct shape
        generated_images = generated_images.reshape((-1, 28, 28))

        # Ensure real_images have the correct shape
        real_images = real_images.reshape((-1, 28, 28))

        X = np.concatenate([real_images, generated_images])
        y_dis = np.zeros(2 * batch_size)
        y_dis[:batch_size] = 0.9  # Label smoothing

        discriminator.trainable = True
        d_loss = discriminator.train_on_batch(X, y_dis)

        noise = np.random.normal(0, 1, (batch_size, 100))
        y_gen = np.ones(batch_size)
        discriminator.trainable = False
        g_loss = gan.train_on_batch(noise, y_gen)

        if epoch % 100 == 0:
            print(f'Epoch: {epoch} | D Loss: {d_loss[0]} | G Loss: {g_loss}')

# Train the GAN
train_gan()



# Generate fake handwritten digits
def generate_digits(n=10):
    noise = np.random.normal(0, 1, (n, 100))
    generated_images = generator.predict(noise)
    plt.figure(figsize=(10, 10))
    for i in range(n):
        plt.subplot(1, n, i+1)
        plt.imshow(generated_images[i], cmap='gray')
        plt.axis('off')
    plt.show()

# Generate and display fake handwritten digits
generate_digits()
