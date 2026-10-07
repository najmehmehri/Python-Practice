"""
Special 4-Digit Numbers
"""

from math import pow

def find_special_numbers():
    results = []
    for i in range(1000, 10000):  # all 4-digit numbers
        
        # Extract digits
        units = i % 10
        temp = i // 10
        tens = temp % 10
        temp //= 10
        hundreds = temp % 10
        temp //= 10
        thousands = temp % 10
        
        # Check the condition
        if (units + pow(thousands, 4)) == (pow(tens, 2) + pow(hundreds, 3)):
            results.append(i)
    
    return results


if __name__ == "__main__":
    numbers = find_special_numbers()
    print("Special 4-digit numbers:", numbers)
    
    # Print with better formatting
    print("\nList:")
    for num in numbers:
        print(num, end="  ")