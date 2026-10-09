"""
Simple Calculator Class
"""

class Calculator:
    def add(self, a, b):
        print(f"{a} + {b} = {a + b}")

    def subtract(self, a, b):
        print(f"{a} - {b} = {a - b}")

    def multiply(self, a, b):
        print(f"{a} × {b} = {a * b}")

    def divide(self, a, b):
        if b != 0:
            print(f"{a} ÷ {b} = {a / b}")
        else:
            print("Error: Cannot divide by zero!")


# Create an object
my_calc = Calculator()

# Test all methods
my_calc.add(10, 5)
my_calc.subtract(10, 5)
my_calc.multiply(10, 5)
my_calc.divide(10, 5)
my_calc.divide(10, 0)  # Testing division by zero