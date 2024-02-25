import numpy as np
from qiskit import QuantumCircuit, Aer, execute

# Define the quantum circuit
num_qubits = 2
qc = QuantumCircuit(num_qubits)

# Apply a Hadamard gate to the first qubit
qc.h(0)

# Apply a controlled-NOT (CNOT) gate between the first and second qubits
qc.cx(0, 1)

# Measure the qubits
qc.measure_all()

# Simulate the quantum circuit
backend = Aer.get_backend('qasm_simulator')
job = execute(qc, backend, shots=1000)
result = job.result()
counts = result.get_counts(qc)

print(counts)
