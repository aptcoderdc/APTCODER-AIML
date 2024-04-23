# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Dummy healthcare data (example)
# Patient's Heart Rate over time
time = np.arange(0, 24, 1)  # 24 hours
heart_rate = np.array([60, 62, 63, 65, 70, 72, 75, 78, 80, 82, 85, 86, 87, 90, 92, 95, 100, 98, 95, 92, 88, 85, 80, 75])

# Plot the patient's heart rate over time
plt.plot(time, heart_rate, marker='o')
plt.title('Patient Heart Rate Monitoring')
plt.xlabel('Time (hours)')
plt.ylabel('Heart Rate (bpm)')
plt.grid(True)
plt.show()
