# Simple Time Series Analysis Homework

import numpy as np

# Generate random time series data
np.random.seed(0)
time = np.arange(0, 100)
data = np.random.randn(100)

# Calculate basic statistics
mean_value = np.mean(data)
std_dev = np.std(data)
max_value = np.max(data)
min_value = np.min(data)

# Print the results
print("Mean:", mean_value)
print("Standard Deviation:", std_dev)
print("Maximum Value:", max_value)
print("Minimum Value:", min_value)
