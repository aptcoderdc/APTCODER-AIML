import numpy as np
from qiskit import QuantumCircuit, Aer, execute
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Quantum Circuit for Coin Flip
def coin_flip_circuit():
    qc = QuantumCircuit(1, 1)
    qc.h(0)  # Apply Hadamard gate for superposition
    qc.measure(0, 0)  # Measure the qubit
    return qc

# Simulate Quantum Coin Flip
def simulate_coin_flip(qc, shots=1000):
    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc, backend, shots=shots)
    result = job.result()
    counts = result.get_counts(qc)
    return counts

# Collect Data
def collect_data():
    X = []
    y = []
    heads_count = 0
    tails_count = 0
    for _ in range(1000):
        qc = coin_flip_circuit()
        counts = simulate_coin_flip(qc)
        if '0' in counts and heads_count < 500:
            X.append(1)  # Heads
            y.append(0)
            heads_count += 1
        elif tails_count < 500:
            X.append(0)  # Tails
            y.append(1)
            tails_count += 1
    return np.array(X).reshape(-1, 1), np.array(y)


# Machine Learning Model
def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LogisticRegression()
    model.fit(X_train, y_train)
    accuracy = model.score(X_test, y_test)
    return model, accuracy

# Main
if __name__ == "__main__":
    X, y = collect_data()
    model, accuracy = train_model(X, y)
    print("Accuracy:", accuracy)
