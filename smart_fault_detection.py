# -----------------------------
# SMART FAULT DETECTION SYSTEM
# -----------------------------

from itertools import product

# ---------- LOGIC GATES ----------
def AND(a, b): return a & b
def OR(a, b): return a | b
def NOT(a): return 0 if a else 1
def XOR(a, b): return a ^ b


# ---------- CIRCUIT DEFINITION ----------
# Example Circuit:
# Y = (A AND B) OR (NOT C)

def circuit(inputs, fault=None):
    A, B, C = inputs

    # Gate 1
    g1 = AND(A, B)
    if fault == ("g1", 0): g1 = 0
    if fault == ("g1", 1): g1 = 1

    # Gate 2
    g2 = NOT(C)
    if fault == ("g2", 0): g2 = 0
    if fault == ("g2", 1): g2 = 1

    # Output Gate
    Y = OR(g1, g2)
    if fault == ("Y", 0): Y = 0
    if fault == ("Y", 1): Y = 1

    return Y


# ---------- FAULT LIST ----------
fault_list = [
    ("g1", 0), ("g1", 1),
    ("g2", 0), ("g2", 1),
    ("Y", 0),  ("Y", 1)
]


# ---------- TEST VECTOR GENERATION ----------
test_vectors = list(product([0, 1], repeat=3))


# ---------- FAULT DETECTION ----------
def detect_faults():
    detected_faults = {}

    for fault in fault_list:
        for vector in test_vectors:
            good_output = circuit(vector)
            faulty_output = circuit(vector, fault)

            if good_output != faulty_output:
                detected_faults.setdefault(fault, []).append(vector)

    return detected_faults


# ---------- MAIN ----------
if __name__ == "__main__":
    detected = detect_faults()

    print("\nSMART FAULT DETECTION REPORT")
    print("-" * 35)

    for fault, vectors in detected.items():
        print(f"\nFault Detected: {fault}")
        print("Test Vectors:")
        for v in vectors:
            print(f"  A={v[0]} B={v[1]} C={v[2]}")

    print("\nTotal Faults Detected:", len(detected), "/", len(fault_list))
