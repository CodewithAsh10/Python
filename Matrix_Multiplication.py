import numpy as np

def input_matrix(name):
    print(f"Enter the elements of matrix {name} row by row:")
    matrix = []
    for i in range(3):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        if len(row) != 3:
            print("Please enter exactly 3 numbers.")
            return input_matrix(name)
        matrix.append(row)
    return np.array(matrix)

# Input matrices
matrix_A = input_matrix("A")
matrix_B = input_matrix("B")

# Perform matrix multiplication
result = np.dot(matrix_A, matrix_B)

# Display results
print("\nMatrix A:")
print(matrix_A)

print("\nMatrix B:")
print(matrix_B)

print("\nMatrix Multiplication Result (A * B):")
print(result)
