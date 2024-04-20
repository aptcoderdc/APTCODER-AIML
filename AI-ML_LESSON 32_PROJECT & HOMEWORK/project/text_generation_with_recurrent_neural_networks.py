import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Define input text data
text = "hello world"

# Create character mappings
chars = sorted(list(set(text)))
char_to_idx = {char: idx for idx, char in enumerate(chars)}
idx_to_char = {idx: char for char, idx in char_to_idx.items()}

# Prepare input and target sequences
seq_length = 3
input_seqs = []
target_chars = []
for i in range(len(text) - seq_length):
    input_seq = text[i:i + seq_length]
    target_char = text[i + seq_length]
    input_seqs.append([char_to_idx[char] for char in input_seq])
    target_chars.append(char_to_idx[target_char])

# Reshape input sequences for model training
X = np.reshape(input_seqs, (len(input_seqs), seq_length, 1))
X = X / float(len(chars))
y = np.eye(len(chars))[target_chars]

# Build LSTM model
model = Sequential([
    LSTM(128, input_shape=(X.shape[1], X.shape[2])),
    Dense(len(chars), activation='softmax')
])
model.compile(loss='categorical_crossentropy', optimizer='adam')

# Train model
model.fit(X, y, epochs=100, batch_size=1, verbose=2)

# Generate text using trained model
start_idx = np.random.randint(0, len(input_seqs) - 1)
pattern = input_seqs[start_idx]
generated_text = ''.join([idx_to_char[idx] for idx in pattern])

for i in range(50):
    x = np.reshape(pattern, (1, seq_length, 1))
    x = x / float(len(chars))
    prediction = model.predict(x, verbose=0)
    index = np.argmax(prediction)
    result = idx_to_char[index]
    generated_text += result
    pattern.append(index)
    pattern = pattern[1:]

print("Generated Text:")
print(generated_text)
