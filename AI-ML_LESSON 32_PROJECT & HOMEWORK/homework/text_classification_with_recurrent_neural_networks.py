import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Define input text data (e.g., spam and ham messages)
spam_messages = ["You've won a prize! Claim it now.", "Hey, how are you doing?", "Click this link to buy now!"]
ham_messages = ["Let's meet for lunch tomorrow.", "Just finished my homework.", "Reminder: Parent-Teacher meeting tomorrow."]

# Create character mappings
chars = sorted(list(set(''.join(spam_messages + ham_messages))))
char_to_idx = {char: idx for idx, char in enumerate(chars)}
idx_to_char = {idx: char for char, idx in char_to_idx.items()}

# Prepare input and target sequences
seq_length = 20
input_seqs = []
target_labels = []
for message in spam_messages + ham_messages:
    for i in range(0, len(message) - seq_length, 1):
        input_seq = message[i:i + seq_length]
        input_seqs.append([char_to_idx[char] for char in input_seq])
        target_labels.append(1 if message in spam_messages else 0)

# Reshape input sequences for model training
X = np.reshape(input_seqs, (len(input_seqs), seq_length, 1))
X = X / float(len(chars))
y = np.eye(2)[target_labels]

# Build LSTM model
model = Sequential([
    LSTM(256, input_shape=(X.shape[1], X.shape[2])),
    Dense(2, activation='softmax')
])
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train model
model.fit(X, y, epochs=10, batch_size=128)
