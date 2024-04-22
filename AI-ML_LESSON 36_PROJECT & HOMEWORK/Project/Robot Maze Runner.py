import numpy as np

# Define maze environment
maze = np.array([
    [0, 0, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [1, 0, 0, 1, 0],
    [0, 1, 0, 0, 1],
    [1, 0, 1, 0, 0]
])

# Define parameters
gamma = 0.9  # Discount factor
epsilon = 0.1  # Exploration rate
alpha = 0.1  # Learning rate
num_episodes = 1000

# Initialize Q-table
q_table = np.zeros((maze.shape[0], maze.shape[1], 4))  # 4 actions: up, down, left, right

# Define actions
actions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # (dy, dx)

# Q-learning algorithm

for episode in range(num_episodes):
    state = (0, 0)  # Starting state
    while state != (4, 4):  # Goal state
        if np.random.rand() < epsilon:
            action = np.random.randint(0, 4)  # Random action
        else:
            action = np.argmax(q_table[state[0], state[1]])

        next_state = (state[0] + actions[action][0], state[1] + actions[action][1])
        
        # Check if next_state is within the maze boundaries
        if 0 <= next_state[0] < maze.shape[0] and 0 <= next_state[1] < maze.shape[1]:
            reward = -1 if maze[next_state[0], next_state[1]] == 0 else -5  # Penalty for hitting a wall
            q_table[state[0], state[1], action] += alpha * (reward + gamma * np.max(q_table[next_state[0], next_state[1]]) - q_table[state[0], state[1], action])
            state = next_state
        else:
            # If next_state is out of bounds, penalize and stay in the same state
            reward = -5
            q_table[state[0], state[1], action] += alpha * (reward - q_table[state[0], state[1], action])

# Robot navigation
state = (0, 0)
while state != (4, 4):
    action = np.argmax(q_table[state[0], state[1]])
    state = (state[0] + actions[action][0], state[1] + actions[action][1])
    print("Robot moved to:", state)
