import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

# Generate synthetic time series data
def generate_time_series(num_points=1000):
    time = np.arange(0, num_points)
    amplitude = np.sin(time * 0.1)
    noise = np.random.randn(num_points) * 0.1
    return amplitude + noise

# Create time series data
time_series_data = generate_time_series()

# Prepare data for training
X = time_series_data[:-1]
y = time_series_data[1:]

# Define simple neural network model
model = Sequential([
    Dense(10, input_dim=1, activation='relu'),
    Dense(1)
])

# Compile the model
model.compile(optimizer=Adam(learning_rate=0.001), loss='mse')

# Train the model
history = model.fit(X, y, epochs=50, batch_size=32, verbose=0)

# Plot loss during training
plt.plot(history.history['loss'])
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Training Loss')
plt.show()

# Generate predictions
predictions = model.predict(X)

# Plot actual vs predicted time series
plt.plot(X, label='Actual')
plt.plot(predictions, label='Predicted')
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Actual vs Predicted Time Series')
plt.legend()
plt.show()
