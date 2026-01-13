from itertools import product
import matplotlib.pyplot as plt

# ---------- LOGIC GATES ----------
def AND(a, b): return a & b
def OR(a, b): return a | b
def NOT(a): return 0 if a else 1

# ---------- CIRCUIT ----------
# Y = (A AND B) OR (NOT C)
def circuit(inputs, fault=None):
    A, B, C = inputs

    g1 = AND(A, B)
    if fault == ("g1", 0): g1 = 0
    if fault == ("g1", 1): g1 = 1

    g2 = NOT(C)
    if fault == ("g2", 0): g2 = 0
    if fault == ("g2", 1): g2 = 1

    Y = OR(g1, g2)
    if fault == ("Y", 0): Y = 0
    if fault == ("Y", 1): Y = 1

    return Y

# ---------- FAULT LIST ----------
fault_list = [
    ("g1", 0), ("g1", 1),
    ("g2", 0), ("g2", 1),
    ("Y", 0), ("Y", 1)
]

# ---------- TEST VECTORS ----------
test_vectors = list(product([0, 1], repeat=3))

# ---------- FAULT DETECTION ----------
def detect_faults():
    detected_faults = {}

    for fault in fault_list:
        for vector in test_vectors:
            good = circuit(vector)
            faulty = circuit(vector, fault)

            if good != faulty:
                detected_faults.setdefault(fault, []).append(vector)

    return detected_faults

# ---------- GRAPH ----------
def plot_fault_coverage(detected_faults):
    fault_names = []
    coverage = []

    for fault in fault_list:
        name = f"{fault[0]}-SA{fault[1]}"
        fault_names.append(name)
        coverage.append(len(detected_faults.get(fault, [])))

    plt.figure()
    plt.bar(fault_names, coverage)
    plt.xlabel("Faults")
    plt.ylabel("No. of Detecting Test Vectors")
    plt.title("Fault Coverage Analysis")
    plt.show()

# ---------- MAIN ----------
if __name__ == "__main__":
    detected = detect_faults()

    print("\nSMART FAULT DETECTION REPORT")
    print("-" * 35)

    for fault, vectors in detected.items():
        print(f"\nFault Detected: {fault}")
        for v in vectors:
            print(f"  A={v[0]} B={v[1]} C={v[2]}")

    print("\nTotal Faults Detected:", len(detected), "/", len(fault_list))

    # Plot graph
    plot_fault_coverage(detected)
