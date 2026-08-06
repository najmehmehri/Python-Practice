"""
File Processing - Sort Words in Each Line

This program:
1. Sorts words in a string alphabetically
2. Checks if a file exists
3. Reads a file, sorts words in each line, and saves the result
"""

import os


def sort_words_in_string(line):
    words = line.split()
    sorted_words = sorted(words)
    return ' '.join(sorted_words)


def file_exists(file_path):
    return os.path.exists(file_path)


def process_file(file_path):
   
    # Check if file exists
    if not file_exists(file_path):
        print(f"Error: File '{file_path}' not found!")
        return
    
    # Read file and process each line
    sorted_lines = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line_num, line in enumerate(file):
            # Remove extra spaces and newline
            cleaned_line = line.strip()
            
            # Sort words in the line
            sorted_line = sort_words_in_string(cleaned_line)
            
            # Store in dictionary
            sorted_lines[line_num] = sorted_line
    
    # Append the sorted result to the file
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write("\n" + "=" * 40 + "\n")
        file.write("Sorted lines:\n")
        for line_num, sorted_line in sorted_lines.items():
            file.write(f"Line {line_num}: {sorted_line}\n")
    
    print(f"✅ Processed {len(sorted_lines)} lines from '{file_path}'")
    return sorted_lines


 
# Test Functions
 

if __name__ == "__main__":
    
    print("=" * 50)
    print("Test 1: Sort words in a string")
    print("=" * 50)
    result1 = sort_words_in_string("you are a programmer")
    print(f"Result: {result1}")
    
    print("\n" + "=" * 50)
    print("Test 2: Check if file exists")
    print("=" * 50)
    # Test with a sample address
    test_address = "E:\\Files\\najmeh.txt"
    if file_exists(test_address):
        print(f"✅ File '{test_address}' exists")
    else:
        print(f"❌ File '{test_address}' not found")
    
    print("\n" + "=" * 50)
    print("Test 3: Process file")
    print("=" * 50)
    # Use a local test file instead
    with open("test.txt", "w") as f:
        f.write("you are a programmer\n")
        f.write("hello world\n")
        f.write("python is fun\n")
    
    process_file("test.txt")
    
    # Show the result
    print("\nFinal content of test.txt:")
    with open("test.txt", "r") as f:
        print(f.read())