import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Define demo movie review data
positive_reviews = ["I loved the movie!", "Great plot and acting.", "Highly recommended."]
negative_reviews = ["Terrible movie, waste of time.", "Awful acting and poor storyline.", "I regret watching it."]

# Combine positive and negative reviews
reviews = positive_reviews + negative_reviews
# Assign labels: 1 for positive reviews, 0 for negative reviews
labels = [1] * len(positive_reviews) + [0] * len(negative_reviews)

# Convert text data to lowercase and tokenize characters
text = ''.join(reviews).lower()
chars = sorted(list(set(text)))
char_to_idx = {char: idx for idx, char in enumerate(chars)}

# Prepare input sequences
seq_length = 20
input_seqs = []
target_labels = []
for review, label in zip(reviews, labels):
    for i in range(0, len(review) - seq_length, 1):
        input_seq = review[i:i + seq_length]
        input_seqs.append([char_to_idx.get(char, 0) for char in input_seq])  # Using char_to_idx.get(char, 0) to handle unseen characters
        target_labels.append(label)

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
model.fit(X, y, epochs=10, batch_size=128, verbose=1)

# Save model if needed
# model.save("sentiment_analysis_model.h5")
