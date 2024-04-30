import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Function to generate dummy weather data
def generate_weather_data(start_date, end_date):
    dates = pd.date_range(start=start_date, end=end_date)
    temperature = np.random.randint(-10, 40, size=len(dates))
    humidity = np.random.randint(0, 100, size=len(dates))
    wind_speed = np.random.randint(0, 50, size=len(dates))
    rainfall = np.random.rand(len(dates)) * 10  # Random rainfall values between 0 and 10
    weather_data = pd.DataFrame({'Date': dates, 'Temperature': temperature, 'Humidity': humidity, 'Wind_Speed': wind_speed, 'Rainfall': rainfall})
    return weather_data

# Define start and end dates
start_date = '2022-01-01'
end_date = '2022-12-31'

# Generate weather data
weather_data = generate_weather_data(start_date, end_date)

# Display weather data
print("Sample Weather Data:")
print(weather_data.head())

# Plot weather trends
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(weather_data['Date'], weather_data['Temperature'], color='orange')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Variation')

plt.subplot(2, 2, 2)
plt.plot(weather_data['Date'], weather_data['Humidity'], color='blue')
plt.xlabel('Date')
plt.ylabel('Humidity (%)')
plt.title('Humidity Variation')

plt.subplot(2, 2, 3)
plt.plot(weather_data['Date'], weather_data['Wind_Speed'], color='green')
plt.xlabel('Date')
plt.ylabel('Wind Speed (km/h)')
plt.title('Wind Speed Variation')

plt.subplot(2, 2, 4)
plt.hist(weather_data['Rainfall'], bins=20, color='purple', alpha=0.7)
plt.xlabel('Rainfall (mm)')
plt.ylabel('Frequency')
plt.title('Rainfall Distribution')

plt.tight_layout()
plt.show()

# Preprocess data
X = weather_data[['Temperature', 'Humidity', 'Wind_Speed']].values
y = weather_data['Rainfall'].values

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate model
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Plot actual vs predicted rainfall
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, color='blue')
plt.plot([0, max(y_test)], [0, max(y_test)], color='red', linestyle='--')
plt.xlabel('Actual Rainfall')
plt.ylabel('Predicted Rainfall')
plt.title('Actual vs Predicted Rainfall')
plt.grid(True)
plt.show()
