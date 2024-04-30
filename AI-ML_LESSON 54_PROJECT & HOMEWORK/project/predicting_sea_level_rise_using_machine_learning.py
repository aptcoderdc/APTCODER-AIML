import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Dummy data for sea level rise prediction
years = np.arange(2000, 2021).reshape(-1, 1)  # Years from 2000 to 2020
sea_levels = np.array([0.2, 0.3, 0.5, 0.6, 0.8, 1.0, 1.2, 1.3, 1.5, 1.7, 1.9, 2.1, 2.3, 2.5, 2.7, 2.9, 3.1, 3.3, 3.5, 3.7, 3.9]).reshape(-1, 1)  # Sea level rise data (in meters)

# Train linear regression model
model = LinearRegression()
model.fit(years, sea_levels)

# Predict sea levels for future years
future_years = np.arange(2021, 2051).reshape(-1, 1)
predicted_sea_levels = model.predict(future_years)

# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(years, sea_levels, color='blue', label='Actual Sea Levels')
plt.plot(np.concatenate((years, future_years)), np.concatenate((sea_levels, predicted_sea_levels)), color='red', linestyle='--', label='Predicted Sea Levels')
plt.xlabel('Year')
plt.ylabel('Sea Level (meters)')
plt.title('Predicted Sea Level Rise')
plt.legend()
plt.grid(True)
plt.show()
