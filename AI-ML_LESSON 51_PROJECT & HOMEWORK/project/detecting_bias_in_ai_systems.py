import numpy as np

# Dummy function to detect bias in AI systems
def detect_bias(data):
    # Dummy bias detection algorithm
    # Check for gender bias in predictions
    gender_bias = np.random.choice(['Male', 'Female', 'Neutral'], p=[0.3, 0.3, 0.4])
    return gender_bias

# Dummy AI system predictions
ai_predictions = np.random.randint(0, 2, size=(100))  # Random binary predictions

# Detect bias in AI predictions
bias_detected = detect_bias(ai_predictions)

# Display bias detection result
print("Bias Detected in AI System:", bias_detected)
