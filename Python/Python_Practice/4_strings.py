# Find the first non-repeating character in a string.


def first_non_repeating_character(s):
    char_count = {}
    
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char in s:
        if char_count[char] == 1:
            return char

    return None 


# Example usage:

input_string = input("Enter a string : ")
result = first_non_repeating_character(input_string)

if result:
    print(f"The first non-repeating character in '{input_string}' is: '{result}'")
else:    
    print(f"There are no non-repeating characters in '{input_string}'.")                       

