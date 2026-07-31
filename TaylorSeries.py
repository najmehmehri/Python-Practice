"""
Sine using Taylor Series (odd powers only)
sin(x) = x - x^3/3! + x^5/5! - x^7/7! + ...
"""
def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n-1)

def pow(x, n):
    if n == 0:
        return 1
    return x * pow(x, n-1)

x = int(input("x = "))
n_terms = int(input("number of odd terms (e.g., 3 means up to x^5): "))

sums = 0
sign = 1

for i in range(1, 2*n_terms, 2):   # i = 1,3,5,...
    sums += sign * (pow(x, i) / fact(i))
    sign = -sign

print(f"sin({x}) ≈ {sums}")