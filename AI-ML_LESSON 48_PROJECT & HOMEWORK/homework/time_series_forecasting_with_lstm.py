import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
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

# Reshape data for LSTM input (samples, timesteps, features)
X = X.reshape(-1, 1, 1)

# Define LSTM model
model = Sequential([
    LSTM(10, input_shape=(1, 1)),
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
plt.plot(y, label='Actual')
plt.plot(predictions, label='Predicted')
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Actual vs Predicted Time Series')
plt.legend()
plt.show()
