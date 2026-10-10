"""
List Practice - 14 Different Operations

This file contains various list operations including:
- Set operations (intersection)
- Removing elements
- Finding max/min with all indices
- Counting duplicates
- Filtering and transforming elements
- Reversing lists
- Swapping lists
- Generating odd numbers
- Building lists in reverse order
- Variable arguments function

"""

# 1. Intersection of two random lists
import random
def list_intersection():
    n = int(input("Please enter length of list: "))
    L = [random.randint(1, 10) for _ in range(n)]
    K = [random.randint(1, 10) for _ in range(n)]
    
    intersection = list(set(L) & set(K))
    
    print(f"List 1: {L}")
    print(f"List 2: {K}")
    print(f"Common elements: {intersection}")
    return intersection


# 2. Remove all occurrences of a guess
def remove_all_occurrences():
    n = int(input("Please enter length of list: "))
    L = []
    for i in range(n):
        k = int(input("Please enter a number: "))
        L.append(k)
    
    print(f"Original list: {L}")
    
    guess = int(input("Enter number to remove: "))
    
    # Method 1: Using list comprehension (recommended)
    L = [x for x in L if x != guess]
    
    print(f"After removing {guess}: {L}")
    return L

# 3 & 4. Find max and min with all indices (Fixed)
def find_max_min_with_indices():
    n = int(input("Please enter length of list: "))
    L = []
    for i in range(n):
        k = int(input("Please enter a number: "))
        L.append(k)
    
    if not L:
        print("List is empty")
        return
    
    Max = max(L)
    Min = min(L)
    
    print(f"List: {L}")
    print(f"Maximum: {Max} at indices: ", end="")
    for idx, val in enumerate(L):
        if val == Max:
            print(idx, end=" ")
    print()
    
    print(f"Minimum: {Min} at indices: ", end="")
    for idx, val in enumerate(L):
        if val == Min:
            print(idx, end=" ")
    print()

# 5. Count repeated elements
def count_duplicates():
    n = int(input("Please enter length of list: "))
    L = []
    for i in range(n):
        k = int(input("Please enter a number: "))
        L.append(k)
    
    repeated = {i: L.count(i) for i in L if L.count(i) > 1}
    
    if repeated:
        print(f"List: {L}")
        print("Duplicate elements:")
        for key in sorted(repeated):
            print(f"  {key} : {repeated[key]} times")
    else:
        print("No duplicates found")
    
    return repeated

# 6. Keep evens, double odds
def process_even_odd():
    n = int(input("Please enter length of list: "))
    L = []
    for i in range(n):
        k = int(input("Please enter a number: "))
        if k % 2 == 0:
            L.append(k)
        else:
            L.append(k * 2)
    
    print(f"Processed list: {L}")
    return L

# 7. Separate multiples of 2 and 3
def separate_multiples():
    random.seed() 
    L = [random.randint(1, 1000) for _ in range(20)]
    
    multiples_of_2 = [x for x in L if x % 2 == 0]
    multiples_of_3 = [x for x in L if x % 3 == 0]
    
    print(f"Original list (20 random numbers): {L}")
    print(f"Even numbers (multiples of 2): {multiples_of_2}")
    print(f"Multiples of 3: {multiples_of_3}")
    
    return multiples_of_2, multiples_of_3


# 8. Extend lists (commented in original, cleaned up)
def extend_lists():
    L = list(range(1, 11))
    K = list(range(11, 21))
    L.extend(K)
    
    print(f"Combined list (1 to 20): {L}")
    return L


# 9. Guess the number game (Fixed)
def guess_number_game():
    n = int(input("Please enter length of list: "))
    L = []
    for i in range(n):
        k = int(input("Enter a number: "))
        L.append(k)
    
    guess = int(input("Make a guess: "))
    
    if guess in L:
        print(f"WellDone!!! {guess} is in the list!")
        print(f"Position(s): ", end="")
        for idx, val in enumerate(L):
            if val == guess:
                print(idx, end=" ")
        print()
    else:
        print(f"Sorry, {guess} is not in the list.")
        print(f"The list contains: {L}")


# 10. Reverse list using slicing
def reverse_list_slicing():
    n = int(input("Enter a number: "))
    L = [random.randint(1, n) for _ in range(n + 1)]
    
    print(f"Original list: {L}")
    print(f"Reversed list: {L[::-1]}")
    return L[::-1]


# 11. Swap two lists
def swap_lists():
    n = int(input("Enter a number: "))
    L = [random.randint(1, n) for _ in range(n + 1)]
    K = [random.randint(1, n) for _ in range(n + 1)]
    
    print(f"Original L: {L}")
    print(f"Original K: {K}")
    
    # Swap the lists
    L, K = K, L
    
    print(f"After swap - L: {L}")
    print(f"After swap - K: {K}")
    
    return L, K


# 12. Odd numbers 1-200 in reverse
def odd_numbers_reverse():
    odd_numbers = [x for x in range(1, 201) if x % 2 == 1]
    reversed_odd = odd_numbers[::-1]
    
    print(f"Odd numbers 1-200 reversed: {reversed_odd}")
    return reversed_odd


# 13. Build list in reverse order (n to 1)
def reverse_order_build():
    n = int(input("Enter a number: "))
    L = [i for i in range(n, 0, -1)]
    
    print(f"List from {n} to 1: {L}")
    return L


# 14. Variable arguments sum function
def sums(*nums):
    """Sum any number of arguments"""
    return sum(nums)


def test_variable_args():
    L = [1, 2, 4, 5, 6, 10]
    
    print(f"List: {L}")
    print(f"Sum using sums(*L): {sums(*L)}")
    print(f"Sum using built-in sum(): {sum(L)}")
    print(f"Sum of (1,2,3): {sums(1, 2, 3)}")
# Main Test

if __name__ == "__main__":
    
    print("=" * 60)
    print("LIST PRACTICE - 14 DIFFERENT OPERATIONS")
    print("=" * 60)
    
    # Test all functions
    print("\n--- 1. List Intersection ---")
    list_intersection()
    
    print("\n--- 2. Remove All Occurrences ---")
    remove_all_occurrences()
    
    print("\n--- 3 & 4. Max/Min with All Indices ---")
    find_max_min_with_indices()
    
    print("\n--- 5. Count Duplicates ---")
    count_duplicates()
    
    print("\n--- 6. Keep Evens, Double Odds ---")
    process_even_odd()
    
    print("\n--- 7. Separate Multiples of 2 and 3 ---")
    separate_multiples()
    
    print("\n--- 8. Extend Lists ---")
    extend_lists()
    
    print("\n--- 9. Guess Number Game ---")
    guess_number_game()
    
    print("\n--- 10. Reverse List with Slicing ---")
    reverse_list_slicing()
    
    print("\n--- 11. Swap Lists ---")
    swap_lists()
    
    print("\n--- 12. Odd Numbers 1-200 in Reverse ---")
    odd_numbers_reverse()
    
    print("\n--- 13. Reverse Order Build (n to 1) ---")
    reverse_order_build()
    
    print("\n--- 14. Variable Arguments Sum ---")
    test_variable_args()
    
    print("\n" + "=" * 60)
    print("ALL TESTS COMPLETED")
    print("=" * 60)
