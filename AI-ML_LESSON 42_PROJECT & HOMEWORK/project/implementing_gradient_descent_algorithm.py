import numpy as np

# Define a simple linear regression function: y = mx + c
def linear_regression(m, c, x):
    return m * x + c

# Define the mean squared error (MSE) loss function
def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

# Implement gradient descent algorithm to optimize parameters m and c
def gradient_descent(x, y_true, learning_rate=0.01, epochs=100):
    # Initialize parameters m and c
    m = 0
    c = 0
    n = len(x)
    
    # Perform gradient descent
    for _ in range(epochs):
        # Calculate predicted values
        y_pred = linear_regression(m, c, x)
        
        # Calculate gradients
        dm = (-2/n) * np.sum(x * (y_true - y_pred))
        dc = (-2/n) * np.sum(y_true - y_pred)
        
        # Update parameters using gradients
        m -= learning_rate * dm
        c -= learning_rate * dc
    
    return m, c

# Dummy data for demonstration
x = np.array([1, 2, 3, 4, 5])
y_true = np.array([3, 5, 7, 9, 11])

# Apply gradient descent algorithm
m_optimized, c_optimized = gradient_descent(x, y_true)

# Print optimized parameters
print("Optimized slope (m):", m_optimized)
print("Optimized intercept (c):", c_optimized)
