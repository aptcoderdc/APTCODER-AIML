import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Define demo weather data
past_temperatures = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
future_days = 5

# Prepare input sequences
seq_length = 3
input_seqs = []
target_temperatures = []
for i in range(len(past_temperatures) - seq_length - future_days):
    input_seq = past_temperatures[i:i + seq_length]
    target_temp = past_temperatures[i + seq_length:i + seq_length + future_days]
    input_seqs.append(input_seq)
    target_temperatures.append(target_temp)

# Reshape input sequences for model training
X = np.reshape(input_seqs, (len(input_seqs), seq_length, 1))
X = X / float(max(past_temperatures))
y = np.array(target_temperatures) / float(max(past_temperatures))

# Build LSTM model
model = Sequential([
    LSTM(128, input_shape=(X.shape[1], X.shape[2])),
    Dense(future_days)
])
model.compile(loss='mean_squared_error', optimizer='adam')

# Train model
model.fit(X, y, epochs=50, batch_size=1, verbose=1)

# Save model if needed
# model.save("weather_prediction_model.h5")
