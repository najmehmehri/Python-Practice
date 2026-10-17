"""
Frequency Analysis - Matrix Column Rare Elements
"""

import random


def least_frequent(*nums):
  
    nums_list = list(nums)
    # Find the element with minimum count
    least = min(set(nums_list), key=nums_list.count)
    return least


def column_least_frequent(matrix):
   
    # Transpose matrix to get columns as rows
    columns = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    
    # Find least frequent element in each column
    result = [least_frequent(*col) for col in columns]
    return result


def create_random_matrix(size):
    matrix = []
    for i in range(size):
        row = [random.randint(1, 2000) for _ in range(size)]
        matrix.append(row)
    return matrix


def find_column_of_max_rare(matrix):
   
    # Get least frequent element of each column
    rare_elements = column_least_frequent(matrix)
    
    # Find the maximum of these rare elements
    max_rare = max(rare_elements)
    
    # Find which column has this element
    column_index = rare_elements.index(max_rare)
    
    # Extract that column
    target_column = [row[column_index] for row in matrix]
    
    return rare_elements, max_rare, column_index, target_column


 
# Test
 

if __name__ == "__main__":
    
    print("=" * 50)
    print("Test 1: Least frequent in list")
    print("=" * 50)
    result1 = least_frequent(8, 2, 4, 3, 8, 2, 8, 3, 2, 4, 2)
    print(f"Least frequent: {result1}")
    
    print("\n" + "=" * 50)
    print("Test 2: Fixed matrix")
    print("=" * 50)
    matrix_fixed = [[17, 2, 7], [4, 28, 24], [11, 9, 35]]
    print("Matrix:")
    for row in matrix_fixed:
        print(row)
    
    rare_fixed = column_least_frequent(matrix_fixed)
    print(f"\nLeast frequent in each column: {rare_fixed}")
    
    print("\n" + "=" * 50)
    print("Test 3: Random matrix")
    print("=" * 50)
    random_matrix = create_random_matrix(3)
    print("Random matrix:")
    for row in random_matrix:
        print(row)
    
    rare, max_val, col_idx, column = find_column_of_max_rare(random_matrix)
    print(f"\nLeast frequent in each column: {rare}")
    print(f"Maximum among these: {max_val}")
    print(f"Column index: {col_idx}")
    print(f"That column: {column}")