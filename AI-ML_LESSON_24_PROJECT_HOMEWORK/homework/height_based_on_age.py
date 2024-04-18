import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Sample data
age = np.array([2, 3, 4, 5, 6, 7])
height = np.array([34, 37, 40, 42, 45, 47])

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(age, height, test_size=0.2, random_state=42)

# Reshape features to be 2D arrays
X_train = X_train.reshape(-1, 1)
X_test = X_test.reshape(-1, 1)

# Create linear regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate mean squared error
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Plot actual vs predicted heights
plt.scatter(X_test, y_test, color='black')
plt.plot(X_test, y_pred, color='blue', linewidth=3)
plt.xlabel('Age (years)')
plt.ylabel('Height (inches)')
plt.title('Actual vs Predicted Heights')
plt.show()

