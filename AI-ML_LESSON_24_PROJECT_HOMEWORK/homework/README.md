Step 1: Data Collection

You can gather data on children's heights at different ages. You can use your own data if available, or you can find datasets online. Here's a simplified example of how your data might look:
Age (years)
Height (inches)
2
34
3
37
4
40
5
42
6
45
7
47

Step 2: Data Preprocessing

You'll need to split your data into features (age) and the target variable (height). Then, you can split the data into training and testing sets.

import numpy as np
from sklearn.model_selection import train_test_split

# Sample data

age = np.array([2, 3, 4, 5, 6, 7])
height = np.array([34, 37, 40, 42, 45, 47])

# Split data into training and testing sets

X_train, X_test, y_train, y_test = train_test_split(age, height, test_size=0.2, random_state=42)

# Reshape features to be 2D arrays

X_train = X_train.reshape(-1, 1)
X_test = X_test.reshape(-1, 1)

Step 3: Building and Training the Model

Now, let's create a linear regression model and train it using the training data.
from sklearn.linear_model import LinearRegression

# Create linear regression model

model = LinearRegression()

# Train the model

model.fit(X_train, y_train)

Step 4: Making Predictions

Once the model is trained, we can use it to make predictions on the testing data.

# Make predictions

y_pred = model.predict(X_test)

Step 5: Evaluating the Model

Finally, we can evaluate the performance of our model by comparing the predicted heights to the actual heights.

from sklearn.metrics import mean_squared_error

# Calculate mean squared error

mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

You can also visualize the results by plotting the actual heights against the predicted heights.
import matplotlib.pyplot as plt

# Plot actual vs predicted heights

plt.scatter(X_test, y_test, color='black')
plt.plot(X_test, y_pred, color='blue', linewidth=3)
plt.xlabel('Age (years)')
plt.ylabel('Height (inches)')
plt.title('Actual vs Predicted Heights')
plt.show()

This project provides a simple introduction to linear regression, where you predict a continuous value (height) based on a single feature (age). It's a great way for kids to understand the basics of supervised learning and how it can be applied to real-world scenarios.
