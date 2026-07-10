"""
Harshad Numbers (Niven Numbers)
"""

def is_harshad(number):
    digit_sum = sum(int(d) for d in str(abs(number)))
    
    if digit_sum == 0:
        return False
    
    return number % digit_sum == 0


def get_harshad_numbers():
    count = int(input("How many numbers? "))
    harshad_numbers = []
    
    for i in range(count):
        num = int(input(f"Enter number {i+1}: "))
        if is_harshad(num):
            harshad_numbers.append(num)
    
    return harshad_numbers


# Test
if __name__ == "__main__":
    result = get_harshad_numbers()
    print("Harshad numbers:", result)