import numpy as np

# Define a simple linear regression function: y = mx + c
def linear_regression(m, c, x):
    return m * x + c

# Define the mean squared error (MSE) loss function
def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

# Implement mini-batch gradient descent algorithm to optimize parameters m and c
def mini_batch_gradient_descent(x, y_true, batch_size=2, learning_rate=0.01, epochs=100):
    # Initialize parameters m and c
    m = 0
    c = 0
    n = len(x)
    
    # Perform mini-batch gradient descent
    for _ in range(epochs):
        # Shuffle the data
        indices = np.random.permutation(n)
        x_shuffled = x[indices]
        y_shuffled = y_true[indices]
        
        # Partition the data into mini-batches
        for i in range(0, n, batch_size):
            x_batch = x_shuffled[i:i+batch_size]
            y_batch = y_shuffled[i:i+batch_size]
            
            # Calculate predicted values
            y_pred = linear_regression(m, c, x_batch)
            
            # Calculate gradients
            dm = (-2/batch_size) * np.sum(x_batch * (y_batch - y_pred))
            dc = (-2/batch_size) * np.sum(y_batch - y_pred)
            
            # Update parameters using gradients
            m -= learning_rate * dm
            c -= learning_rate * dc
    
    return m, c

# Dummy data for demonstration
x = np.array([1, 2, 3, 4, 5])
y_true = np.array([3, 5, 7, 9, 11])

# Apply mini-batch gradient descent algorithm
m_optimized, c_optimized = mini_batch_gradient_descent(x, y_true)

# Print optimized parameters
print("Optimized slope (m):", m_optimized)
print("Optimized intercept (c):", c_optimized)
