"""
Perfect Numbers
"""
def is_perfect(number):
    if number < 1:
        return False
    
    total = 0
    for i in range(1, number):
        if number % i == 0:
            total += i
    
    return total == number


count = int(input("How many numbers? "))
perfect_numbers = []

for i in range(count):
    num = int(input("Enter a number: "))
    if is_perfect(num):
        perfect_numbers.append(num)

print("Perfect numbers are:", perfect_numbers)