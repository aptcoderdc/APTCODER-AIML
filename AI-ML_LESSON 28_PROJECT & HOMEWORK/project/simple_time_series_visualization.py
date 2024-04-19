# Simple Time Series Visualization Project

import numpy as np
import matplotlib.pyplot as plt

# Generate random time series data
np.random.seed(0)
time = np.arange(0, 100)
data = np.random.randn(100)

# Plot the time series data
plt.figure(figsize=(10, 5))
plt.plot(time, data, color='blue')
plt.title('Simple Time Series Visualization')
plt.xlabel('Time')
plt.ylabel('Data')
plt.grid(True)
plt.show()
