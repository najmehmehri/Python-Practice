"""
Multiplication Table
Problem: Generate and display a multiplication table from 1 to n.
"""

n = int(input("Enter a number: "))

# Create list of numbers 1 to n
numbers = list(range(1, n + 1))

# Create dictionary of multiplication table
multiplication_table = {}
for i in range(1, n + 1):
    multiplication_table[str(i)] = [i * e for e in numbers]

# Print the table
print("\nMultiplication Table:")
for row in multiplication_table:
    print(multiplication_table[row])