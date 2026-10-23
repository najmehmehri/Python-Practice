"""
Matrix Practice - 16 Different Operations

This file contains various matrix operations including:
- Creating random matrices
- Matrix sum, average, max per row
- Matrix addition and multiplication
- Special matrices (zero, one, triangular, diagonal)
- Determinant and inverse (2x2)
- Row swapping
- Scalar multiplication
- Multiplication table

"""

import random

#Create a matrix with random values
def create_random_matrix(rows, cols, min_val=1, max_val=20):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(random.randint(min_val, max_val))
        matrix.append(row)
    return matrix


def print_matrix(matrix, title="Matrix"):
    print(f"\n{title}:")
    for row in matrix:
        for val in row:
            print(f"{val:5}", end="")
        print()


# 1. Matrix Total Sum, Average, Max per Row
def matrix_total_sum(matrix):
    total = 0
    for row in matrix:
        total += sum(row)
    return total

#Get maximum value from each row
def matrix_max_per_row(matrix):
    return [max(row) for row in matrix]

#Create a matrix and analyze it
def analyze_matrix():
    R = int(input("Enter rows: "))
    C = int(input("Enter columns: "))
    
    matrix = create_random_matrix(R, C, 1, 20)
    total = matrix_total_sum(matrix)
    average = total / (R * C)
    max_per_row = matrix_max_per_row(matrix)
    
    print_matrix(matrix, "Matrix")
    print(f"Sum of all elements: {total}")
    print(f"Average: {average:.2f}")
    print(f"Max per row: {max_per_row}")
    
    return matrix


# 2. Matrix Multiplication (Element-wise)
def element_wise_square(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix[i][j] ** 2
    
    return result


def square_matrix():
    x = int(input("Enter no. of rows: "))
    y = int(input("Enter no. of columns: "))
    
    print("Enter first matrix elements:")
    a = [[float(input()) for _ in range(y)] for _ in range(x)]
    
    print_matrix(a, "Original Matrix")
    
    result = element_wise_square(a)
    print_matrix(result, "Element-wise Square")
    
    return result


# 3. Display Matrix
def display_matrix():
    R = int(input("Enter rows: "))
    C = int(input("Enter columns: "))
    
    matrix = create_random_matrix(R, C, 10, 100)
    
    print_matrix(matrix, "Random Matrix")
    return matrix


# 4. Multiplication Table (1-10)
def multiplication_table():
    numbers = list(range(1, 11))
    multiples = {}
    
    for i in range(1, 11):
        multiples[str(i)] = [e * i for e in numbers]
    
    print("\nMultiplication Table (1-10):")
    for i in range(1, 11):
        print(f"{i:2}: {multiples[str(i)]}")
    
    return multiples


# 5. Identity-like Matrix (0 on diagonal, 1 elsewhere)
def off_diagonal_ones():
    size = 5
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            if i == j:
                row.append(0)
            else:
                row.append(1)
        matrix.append(row)
    
    print_matrix(matrix, "5x5 Matrix (0 on diagonal, 1 elsewhere)")
    return matrix


# 6. Upper Triangular Random Matrix
def upper_triangular_random():
    R = int(input("Enter rows: "))
    C = int(input("Enter columns: "))
    
    matrix = []
    for i in range(R):
        row = []
        for j in range(C):
            if i > j:
                row.append(0)
            else:
                row.append(random.randint(1, 100))
        matrix.append(row)
    
    print_matrix(matrix, "Upper Triangular Matrix")
    return matrix


# 7. Row Parity Matrix (1 for odd rows, 0 for even)
def row_parity_matrix():
    R = int(input("Enter rows: "))
    C = int(input("Enter columns: "))
    
    matrix = []
    for i in range(R):
        row = []
        for j in range(C):
            if i % 2 == 1:  # odd row (1-indexed thinking)
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    
    print_matrix(matrix, "Row Parity Matrix")
    return matrix


# 8. Matrix Operations (Sum, Multiplication, Determinant, Inverse)
def matrix_addition(A, B):
    rows = len(A)
    cols = len(A[0])
    return [[A[i][j] + B[i][j] for j in range(cols)] for i in range(rows)]


def matrix_multiplication(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    cols_B = len(B[0])
    
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    return result

#Calculate determinant of 2x2 matrix
def determinant_2x2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

#Calculate inverse of 2x2 matrix
def inverse_2x2(matrix):
    det = determinant_2x2(matrix)
    if det == 0:
        return None
    
    inverse = [
        [matrix[1][1] / det, -matrix[0][1] / det],
        [-matrix[1][0] / det, matrix[0][0] / det]
    ]
    return inverse

#Demonstrate various matrix operations
def matrix_operations_demo():
    n1 = random.randint(1, 5)
    n2 = random.randint(1, 5)
    
    A = create_random_matrix(n1, n2, 1, 10)
    B = create_random_matrix(n1, n2, 1, 10)
    
    print_matrix(A, "Matrix A")
    print_matrix(B, "Matrix B")
    
    # Matrix addition
    try:
        sum_matrix = matrix_addition(A, B)
        print_matrix(sum_matrix, "A + B")
    except:
        print("Matrices must have same dimensions for addition")
    
    # Matrix multiplication
    try:
        B_T = list(zip(*B))
        product = [[sum(a * b for a, b in zip(row, col)) for col in B_T] for row in A]
        print_matrix(product, "A × B")
    except:
        print("Matrix multiplication requires compatible dimensions")
    
    # 2x2 determinant and inverse
    det_matrix = create_random_matrix(2, 2, 1, 10)
    print_matrix(det_matrix, "2x2 Matrix for Determinant")
    det = determinant_2x2(det_matrix)
    print(f"Determinant: {det}")
    
    inv = inverse_2x2(det_matrix)
    if inv:
        print_matrix(inv, "Inverse (rounded)")
    else:
        print("Matrix is singular (determinant = 0), cannot invert")


# 9. Scalar Multiplication
def scalar_multiply():
    R = int(input("Enter rows: "))
    C = int(input("Enter columns: "))
    k = int(input("Enter scalar: "))
    
    matrix = create_random_matrix(R, C, 1, 100)
    print_matrix(matrix, "Original Matrix")
    
    if k != 0:
        result = [[element * k for element in row] for row in matrix]
        print_matrix(result, f"Matrix × {k}")
        return result
    else:
        print("Scalar must not be zero")
        return None


# 10. Matrix Multiplication (User Input Dimensions)
def matrix_multiplication_user():
    R1 = int(input("Enter rows of first matrix: "))
    C1 = int(input("Enter columns of first matrix: "))
    C2 = int(input("Enter columns of second matrix: "))
    
    matrix1 = create_random_matrix(R1, C1, 10, 100)
    matrix2 = create_random_matrix(C1, C2, 10, 100)  # Note: rows of second = cols of first
    
    print_matrix(matrix1, "Matrix A")
    print_matrix(matrix2, "Matrix B")
    
    # Matrix multiplication
    result = [[sum(a * b for a, b in zip(row, col)) for col in zip(*matrix2)] for row in matrix1]
    print_matrix(result, "A × B")
    
    return result


# 11. Swap Two Rows
def swap_rows():
    R = int(input("Enter rows: "))
    C = int(input("Enter columns: "))
    row1 = int(input("Enter first row to swap (0-indexed): "))
    row2 = int(input("Enter second row to swap (0-indexed): "))
    
    matrix = create_random_matrix(R, C, 10, 100)
    print_matrix(matrix, "Original Matrix")
    
    # Swap rows
    matrix[row1], matrix[row2] = matrix[row2], matrix[row1]
    print_matrix(matrix, f"After swapping row {row1} and row {row2}")
    
    return matrix

# 12. Sum of Specific Row and Column (Fixed)
def sum_row_and_column():
    R = int(input("Enter rows: "))
    C = int(input("Enter columns: "))
    target_row = int(input("Enter target row (0-indexed): "))
    target_col = int(input("Enter target column (0-indexed): "))
    
    matrix = create_random_matrix(R, C, 1, 10)
    print_matrix(matrix, "Matrix")
    
    if target_row < R:
        row_sum = sum(matrix[target_row])
        print(f"Sum of row {target_row}: {row_sum}")
    else:
        print(f"Row {target_row} out of range")
    
    if target_col < C:
        col_sum = sum(matrix[i][target_col] for i in range(R))
        print(f"Sum of column {target_col}: {col_sum}")
    else:
        print(f"Column {target_col} out of range")
    
    return matrix


# 13. Lower Triangular Matrix (1 on and below diagonal)
def lower_triangular_ones():
    R = int(input("Enter rows: "))
    C = int(input("Enter columns: "))
    
    matrix = []
    for i in range(R):
        row = []
        for j in range(C):
            if i >= j:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    
    print_matrix(matrix, "Lower Triangular Matrix (1 on/below diagonal)")
    return matrix


# 14. Matrix with i+j values (except center)
def matrix_ij_sum():
    R = int(input("Enter rows: "))
    C = int(input("Enter columns: "))
    
    matrix = []
    for i in range(R):
        row = []
        for j in range(C):
            if i == 1 and j == 1 and R > 1 and C > 1:
                row.append(1)
            else:
                row.append(i + j)
        matrix.append(row)
    
    print_matrix(matrix, f"Matrix (i+j, center=1)")
    return matrix


# 15. Sequential Matrix (1 to R²) - Fixed
def sequential_matrix():
    R = int(input("Enter size (rows = columns): "))
    
    matrix = []
    value = 1
    for i in range(R):
        row = []
        for j in range(R):
            row.append(value)
            value += 1
        matrix.append(row)
    
    print_matrix(matrix, f"Sequential Matrix (1 to {R*R})")
    return matrix


# 16. 2x2 Determinant and Inverse (Clean Version)
def inverse_2x2_demo():
    """Calculate determinant and inverse of a random 2x2 matrix"""
    matrix = create_random_matrix(2, 2, 1, 10)
    print_matrix(matrix, "2x2 Matrix")
    
    # Determinant
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    print(f"Determinant: {det}")
    
    if det != 0:
        # Inverse
        inverse = [
            [matrix[1][1] / det, -matrix[0][1] / det],
            [-matrix[1][0] / det, matrix[0][0] / det]
        ]
        print_matrix(inverse, "Inverse (rounded to 2 decimals)")
        
        # Rounded version for display
        inverse_rounded = [[round(val, 2) for val in row] for row in inverse]
        print_matrix(inverse_rounded, "Inverse (rounded to 2 decimal places)")
    else:
        print("Matrix is singular, cannot compute inverse")
    
    return matrix


# Test
if __name__ == "__main__":
    
    print("=" * 60)
    print("MATRIX PRACTICE - 16 DIFFERENT OPERATIONS")
    print("=" * 60)
    
    print("\n--- 1. Matrix Analysis (Sum, Average, Max per Row) ---")
    analyze_matrix()
    
    print("\n--- 2. Element-wise Square ---")
    square_matrix()
    
    print("\n--- 3. Display Matrix ---")
    display_matrix()
    
    print("\n--- 4. Multiplication Table (1-10) ---")
    multiplication_table()
    
    print("\n--- 5. Off-Diagonal Ones Matrix ---")
    off_diagonal_ones()
    
    print("\n--- 6. Upper Triangular Random Matrix ---")
    upper_triangular_random()
    
    print("\n--- 7. Row Parity Matrix ---")
    row_parity_matrix()
    
    print("\n--- 8. Matrix Operations Demo ---")
    matrix_operations_demo()
    
    print("\n--- 9. Scalar Multiplication ---")
    scalar_multiply()
    
    print("\n--- 10. Matrix Multiplication ---")
    matrix_multiplication_user()
    
    print("\n--- 11. Swap Rows ---")
    swap_rows()
    
    print("\n--- 12. Sum of Row and Column ---")
    sum_row_and_column()
    
    print("\n--- 13. Lower Triangular Matrix ---")
    lower_triangular_ones()
    
    print("\n--- 14. Matrix with i+j Values ---")
    matrix_ij_sum()
    
    print("\n--- 15. Sequential Matrix ---")
    sequential_matrix()
    
    print("\n--- 16. 2x2 Determinant and Inverse ---")
    inverse_2x2_demo()
    
    print("\n" + "=" * 60)
    print("ALL TESTS COMPLETED")
    print("=" * 60)