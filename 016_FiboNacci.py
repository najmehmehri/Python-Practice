"""
Fibonacci Sequence - 4 Different Implementations

The Fibonacci sequence: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

This file contains 4 different ways to generate Fibonacci numbers:
1. recursive_fibonacci() - Simple recursive approach (educational, but slow for large n)
2. iterative_fibonacci() - Efficient loop-based approach (recommended for most cases)
3. fibonacci_list() - Returns a list of Fibonacci numbers
4. fibonacci_generator() - Memory-efficient generator for very large sequences

"""

# Implementation 1: Recursive (Simple but Slow)
def fibonacci_recursive(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci_recursive(n - 2) + fibonacci_recursive(n - 1)


def print_fibonacci_recursive(n):
    for i in range(1, n + 1):
        print(fibonacci_recursive(i), end=" ")
    print()


# Implementation 2: Iterative (Fast & Efficient)

def fibonacci_iterative(n):
    if n == 1 or n == 2:
        return 1
    
    a, b = 1, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


def print_fibonacci_iterative(n):
    if n == 0:
        return
    
    a, b = 1, 1
    print(a, end=" ")
    
    if n == 1:
        print()
        return
    
    print(b, end=" ")
    
    for _ in range(3, n + 1):
        a, b = b, a + b
        print(b, end=" ")
    print()


# Implementation 3: Return as List
def fibonacci_list(n):
    if n <= 0:
        return []
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    
    result = [1, 1]
    while len(result) < n:
        result.append(result[-1] + result[-2])
    
    return result

# Implementation 4: Generator (Memory Efficient)

def fibonacci_generator(n):
    if n <= 0:
        return
    
    a, b = 1, 1
    count = 0
    
    while count < n:
        yield a
        a, b = b, a + b
        count += 1
# Test 

if __name__ == "__main__":
    
    print("=" * 50)
    print("FIBONACCI IMPLEMENTATIONS")
    print("=" * 50)
    
    n = int(input("Enter a number: "))
    
    print("\n" + "-" * 50)
    print(f"Method 1 - Recursive (n={n}):")
    print("Warning: Recursive method is slow for n > 35!")
    if n <= 35:
        print_fibonacci_recursive(n)
    else:
        print(f"Skipping recursive method because {n} is too large (would be very slow)")
    
    print("\n" + "-" * 50)
    print(f"Method 2 - Iterative (n={n}):")
    print_fibonacci_iterative(n)
    
    print("\n" + "-" * 50)
    print(f"Method 3 - List (n={n}):")
    result_list = fibonacci_list(n)
    print(result_list)
    
    print("\n" + "-" * 50)
    print(f"Method 4 - Generator (n={n}):")
    print("Generating values one by one:")
    for value in fibonacci_generator(n):
        print(value, end=" ")
    print()
    
    print("\n" + "-" * 50)
    print(f"Sum of first {n} Fibonacci numbers: {sum(fibonacci_list(n))}")
    print("=" * 50)
