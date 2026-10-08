"""
Least Common Multiple (LCM)
Implementation 1: Brute force (checking multiples)
Implementation 2: Using formula LCM = (a * b) / GCD
"""

# Method 1: Brute force (your code)
def lcm_bruteforce(n, m):
    start = max(n, m)
    z = start
    while True:
        if (z % n == 0) and (z % m == 0):
            return z
        z += 1


# Using GCD (faster)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm_formula(a, b):
    return abs(a * b) // gcd(a, b)


# Test 
if __name__ == "__main__":
    a, b = 12, 8
    
    print(f"LCM of {a} and {b}")
    print(f"Method 1 (brute force): {lcm_bruteforce(a, b)}")
    print(f"Method 2 (formula): {lcm_formula(a, b)}")