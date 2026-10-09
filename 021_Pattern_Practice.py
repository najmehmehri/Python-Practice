"""
Pattern Practice - 11 Different Shapes and Functions

This file contains:
- Diamond (rhombus) pattern
- Line intersection calculation
- Distance between two points
- Trapezoid area
- Triangle area
- Number triangle pattern
- Hollow square
- Right triangle
- Solid square
- Hollow square (alternative)
- Hollow parallelogram
"""

import math

 
# 1. Diamond Pattern (Rhombus)
 
def diamond_pattern():
    a = int(input("Enter size of diamond: "))
    j = 1
    
    for i in range(a):
        print(" " * (a - i), "*" * j, sep="")
        j += 2
    
    print("*" * ((2) * a + (1)))
    j -= 2

    for i in range(1, a + 1):
        print(" " * i, "*" * j, sep="")
        j -= 2


 
# 2. Line Intersection (Fixed with clear naming) 
def line_intersection(slope1, intercept1, slope2, intercept2):
    if slope1 == slope2:
        return None  # Parallel lines
    
    x = (intercept2 - intercept1) / (slope1 - slope2)
    y = slope1 * x + intercept1
    return (round(x, 2), round(y, 2))


 
# 3. Distance Between Two Points
def distance_between_points(x1, y1, x2, y2):
    return round(math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2)), 2)


 
# 4. Trapezoid Area
def trapezoid_area(base1, base2, height):
    return height * (base1 + base2) / 2


 
# 5. Triangle Area
def triangle_area(base, height):
    return (base * height) / 2


 
# 6. Number Triangle Pattern (Power of 2)
def number_triangle():
    rowCount = int(input("Enter number of rows: "))
    temp = 0
    
    for i in range(rowCount):
        print((rowCount - i - 1) * " ", end="")
        
        print(temp, end=" ")
        
        for j in range(i):
            temp *= 2
            print(temp, end=" ")

        for j in range(i - 1, -1, -1):
            temp //= 2
            print(temp, end=" ")
        
        print()
        temp = 1


 
# 7. Hollow Square (Fixed)
def hollow_square():
    n = int(input("Enter size: "))
    c = input("Enter character: ")
    
    for i in range(n):
        if i == 0 or i == n - 1:
            print(c * n)
        else:
            print(c + " " * (n - 2) + c)


 
# 8. Right Triangle
def right_triangle():
    n = int(input("Enter size: "))
    c = input("Enter character: ")
    
    for i in range(1, n + 1):
        print(c * i)


 
# 9. Solid Square
def solid_square():
    n = int(input("Enter size: "))
    c = input("Enter character: ")
    
    for i in range(n):
        print(c * n)


 
# 10. Hollow Square Alternative
def hollow_square_alt():
    s = '*'
    size = 6
    
    for i in range(size):
        if i == 0 or i == size - 1:
            print(size * str('*'))
        else:
            print(s, s, sep=(size - 2) * '  ')


 
# 11. Hollow Parallelogram (Fixed)
def hollow_parallelogram():
    n = int(input("Enter size: "))
    
    print(' ' * (n - 1) + '*' * n)
    
    for i in range(1, n - 1):
        print(' ' * (n - 1 - i) + '*' + ' ' * (n - 2) + '*')
    
    if n > 1:
        print('*' * n)


 
#Test
 
if __name__ == "__main__":
    
    print("=" * 60)
    print("PATTERN PRACTICE - 11 DIFFERENT SHAPES & FUNCTIONS")
    print("=" * 60)
    
    print("\n--- 1. Diamond Pattern ---")
    diamond_pattern()
    
    print("\n--- 2. Line Intersection ---")
    print(f"Intersection of y=7x+5 and y=3x+2: {line_intersection(7, 5, 3, 2)}")
    
    print("\n--- 3. Distance Between Points ---")
    print(f"Distance between (2,4) and (6,8): {distance_between_points(2, 4, 6, 8)}")
    
    print("\n--- 4. Trapezoid Area ---")
    print(f"Trapezoid area (bases=1,2 height=4): {trapezoid_area(1, 2, 4)}")
    
    print("\n--- 5. Triangle Area ---")
    print(f"Triangle area (base=2, height=6): {triangle_area(2, 6)}")
    
    print("\n--- 6. Number Triangle ---")
    number_triangle()
    
    print("\n--- 7. Hollow Square ---")
    hollow_square()
    
    print("\n--- 8. Right Triangle ---")
    right_triangle()
    
    print("\n--- 9. Solid Square ---")
    solid_square()
    
    print("\n--- 10. Hollow Square (Alternative) ---")
    hollow_square_alt()
    
    print("\n--- 11. Hollow Parallelogram ---")
    hollow_parallelogram()
    
    print("\n" + "=" * 60)
    print("ALL TESTS COMPLETED")
    print("=" * 60)