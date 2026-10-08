"""
Khayyam Pascal Triangle
"""

def factorial(number):
    p = 1
    for i in range(1, number + 1):
        p *= i
    return p

def combination(m, n):
    return factorial(m) // (factorial(n) * factorial(m - n))

rows = int(input("Enter number of rows: "))

for i in range(rows):
    print(" " * (rows - i), end="")
    
    for j in range(i + 1):
        print(combination(i, j), end=" ")
    
    print()  