# Write a function to check whether a number is a palindrome (without converting to string).

def is_palindrome (num):

    original_num = num
    reversed_num = 0

    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10

    return original_num == reversed_num


num = int(input("Enter a number to check for palindrome : "))
print(is_palindrome(num))