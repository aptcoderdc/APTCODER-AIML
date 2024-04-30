import numpy as np
from qiskit import QuantumCircuit, Aer, execute
from sklearn.metrics import mean_squared_error

# Quantum Circuit for Random Number Generation
def random_number_circuit(num_qubits=4):
    qc = QuantumCircuit(num_qubits, num_qubits)
    for i in range(num_qubits):
        qc.h(i)  # Apply Hadamard gate for superposition
    qc.measure(range(num_qubits), range(num_qubits))  # Measure all qubits
    return qc

# Generate Random Numbers
def generate_random_numbers(qc, shots=1000):
    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc, backend, shots=shots)
    result = job.result()
    counts = result.get_counts(qc)
    return counts

# Analyze Randomness
def analyze_randomness(counts):
    random_numbers = [int(key, 2) for key in counts.keys()]
    mean = np.mean(random_numbers)
    variance = np.var(random_numbers)
    mse = mean_squared_error(np.arange(2**num_qubits), random_numbers)
    return mean, variance, mse

# Main
if __name__ == "__main__":
    num_qubits = 4
    qc = random_number_circuit(num_qubits)
    counts = generate_random_numbers(qc)
    mean, variance, mse = analyze_randomness(counts)
    print("Mean:", mean)
    print("Variance:", variance)
    print("Mean Squared Error:", mse)
