# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 13:07:12 2025

Match grouping symbols

@author: willt
"""

# method will read a text file, 
# identify any mismatched grouping symbols, 
# and convert the second iteration to the proper symbol


def fix_mismatched_symbols(file_path):
    with open(file_path, "r") as f:
        data = f.read()
        
    symbols = {'{': '}', '[': ']', '(': ')'}
    openers = set(symbols.keys())
    closers = set(symbols.values())
    
    stack = [] 
    corrections = {} # {index : correct_char}
    
    # tally mismatches using stack
    for i, char in enumerate(data): # changes data into an iteratable list 
        if char in openers: #first checks for opener symbols
            stack.append(char) # adds opener symbols to the stack list
            
        elif char in closers: # if the character is in closers, check stack
            if stack: # every key from symbols is fair game.
                last_open = stack[-1] # unpack the tuple
                expected_closer = symbols[last_open] 
                if expected_closer == char:
                    stack.pop() # pop the last item in (the corresponding character)
                else:
                    corrections[i] = expected_closer
                    stack.pop()
            else: # ignore non stack symbols
                pass
    # apply corrections            
    data_list = list(data)
    for fix_index, correct_char in corrections.items():
        print(f"Fixing index {fix_index}: '{data_list[fix_index]}' -> '{correct_char}'")
        data_list[fix_index] = correct_char
                
    fixed_data = ''.join(data_list)
    
    print("\nOriginal data: ")
    print(data)
    print("\nFixed data: ")
    return fixed_data

# example output for testing purposes
# file_path = r"C:\Users\willt\mismatched_original.txt"
# with open(file_path, "w") as f:
#     f.write("{1, 4, 6) ... (6, 4, 1} ... [6, 1, 4} ... {1, 6, 4]... example: (a{b)}")
      
# fix_mismatched_symobols(file_path, use this for assignment)
def main():
    file_path = input("Enter path to text file for matching group symbols: ").strip()
    try:
        fixed_output = fix_mismatched_symbols(file_path)
        
        output_path = file_path.replace(".txt", "_fixed.txt")
        with open(output_path, "w") as f:
            f.write(fixed_output)
        print(f"{fixed_output}")
        print(f"\nFixed file saved to {output_path}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")

if __name__ == "__main__":
    main()

