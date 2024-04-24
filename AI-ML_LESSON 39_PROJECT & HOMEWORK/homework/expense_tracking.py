# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Dummy financial data (example)
# Monthly expenses over 6 months
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
expenses = [1000, 1200, 1100, 1300, 1400, 1500]

# Plot the monthly expenses
plt.plot(months, expenses, marker='o')
plt.title('Monthly Expenses Tracking')
plt.xlabel('Month')
plt.ylabel('Expense (USD)')
plt.grid(True)
plt.show()
