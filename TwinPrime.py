"""
Twin Prime Numbers

Problem: Find all twin prime pairs (p, p+2) where both numbers are prime
and less than n.
"""

n = int(input("Enter a number: "))

firstPrime = 2
for i in range(3, n):
    flag = True
    for j in range(2, int(i/2) + 1):
        if i % j == 0:
            flag = False
            break
    if flag:
        if i - firstPrime == 2:
            print(firstPrime, i)
        firstPrime = i