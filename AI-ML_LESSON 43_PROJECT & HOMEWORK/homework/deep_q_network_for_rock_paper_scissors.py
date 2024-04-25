import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

# Dummy Rock-Paper-Scissors data
X = np.random.randint(0, 3, size=(100, 3))
y = np.random.randint(0, 3, size=(100,))

# Define DQN model
model = Sequential([
    Dense(24, input_dim=3, activation='relu'),
    Dense(24, activation='relu'),
    Dense(3, activation='softmax')
])

# Create Adam optimizer with specified learning rate
optimizer = Adam(learning_rate=0.001)

# Compile model with optimizer and loss function
model.compile(loss='sparse_categorical_crossentropy', optimizer=optimizer)

# Train DQN agent
model.fit(X, y, epochs=10, batch_size=32)

# Save trained model
model.save('dqn_rock_paper_scissors.h5')
