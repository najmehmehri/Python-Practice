"""
Strong Numbers (Factorions)
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def find_strong_numbers():
    results = []
    for i in range(100, 1000):  # all 3-digit numbers
        
        # Extract digits
        units = i % 10
        temp = i // 10
        tens = temp % 10
        temp //= 10
        hundreds = temp % 10
        
        # Sum of factorials of digits
        digit_sum = factorial(units) + factorial(tens) + factorial(hundreds)
        
        if digit_sum == i:
            results.append(i)
    
    return results


if __name__ == "__main__":
    numbers = find_strong_numbers()
    print("Strong 3-digit numbers:", numbers)
    
    for num in numbers:
        u = num % 10
        t = (num // 10) % 10
        h = (num // 100) % 10
        print(f"\n{num} = {h}! + {t}! + {u}! = {factorial(h)} + {factorial(t)} + {factorial(u)}")