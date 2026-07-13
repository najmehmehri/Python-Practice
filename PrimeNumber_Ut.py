"""
Prime number utilities: check, find in range, and filter two-digit primes.
"""
def IsPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def FindPrimes(a, b):
    for x in range(a, b + 1):
        if IsPrime(x):
            print(f"{x} is prime")
        else:
            print(f"{x} is not prime")

def TwoDigit_Primes():
    count = int(input("How many numbers? "))
    primes = []
    
    for i in range(count):
        num = int(input(f"Enter number {i+1}: "))
        if IsPrime(num):
            primes.append(num)
    
    PrimesList = [p for p in primes if 10 <= p <= 99]
    return PrimesList
#Exercise
Number = int(input("Please enter a number:"))
for i in range(2,Number):
    if IsPrime(i):
        print(i)
    

# Test
if __name__ == "__main__":
    a = int(input("a: "))
    b = int(input("b: "))
    FindPrimes(a, b)
    
    result = TwoDigit_Primes()
    print("Two-digit prime numbers:", result)
