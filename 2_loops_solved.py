# 1. Counting Positive Numbers
# Problem: Given a list of numbers, count how many are positive.
# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

def count_positive_numbers():
    numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
    count = 0

    for num in numbers:
        if (num >= 0):
            count += 1

    print (count)

# count_positive_numbers()


# 2. Sum of Even Numbers
# Problem: Calculate the sum of even numbers up to a given number n.

def sum_of_even_numbers():
    sum = 0
    number = int(input("Enter the number : "))

    for i in range (number+1):
        if (i % 2 == 0):
            sum += i
    
    print ("The sum of even numbers upto ", number, " is : ", sum)

# sum_of_even_numbers()



# 3. Multiplication Table Printer
# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.


def mul_table_printer():
    number = int(input("Enter the number : "))

    for i in range (1, 11):
        if (i == 5):
            continue
        print(number, "x", i, "=", number * i)

# mul_table_printer()


# 4. Reverse a String
# Problem: Reverse a string using a loop.

def reverse_a_string1():
    string = input("Enter a string : ")
    reverse_string = ""

    for i in range (1, len(string)+1):
        reverse_string += string[-i]

    print(reverse_string)

def reverse_a_string2():
    string = input("Enter a string : ")
    reverse_string = ""

    for char in string:
        reverse_string = char + reverse_string

    print(reverse_string)

# reverse_a_string1()
# reverse_a_string2()


# 5. Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character.


def first_non_repeated_character():
    string = input("Enter a string : ")
    for char in string:
        if string.count(char) == 1:
            print ("The First Non-Repeated Character is : ", char)
            break

# first_non_repeated_character()


# 6. Factorial Calculator
# Problem: Compute the factorial of a number using a while loop.

def calculate_factorial():
    number = int(input("Enter a number : "))
    factorial = 1

    while (number > 0):
        factorial *= number
        number -= 1

    print ("The factorial is : ", factorial)

# calculate_factorial()


# 7. Validate Input
# Problem: Keep asking the user for input until they enter a number between 1 and 10.

def validate_input():
    while True:
        number = int(input("Enter a number between 1 and 10 : "))
        if (1<number<10):
            break

# validate_input()


# 8. Prime Number Checker
# Problem: Check if a number is prime.

def check_prime_number():
    number = int(input("Enter a number : "))
    isPrime = "is a Prime number."

    for i in range (2, number):
        if (number % i == 0):
            isPrime = "is not a prime number."

    print (number, isPrime)

# check_prime_number()



# 9. List Uniqueness Checker
# Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.
# items = ["apple", "banana", "orange", "apple", "mango"]

def list_uniqueness_checker ():
    items = ["apple", "banana", "orange", "apple", "mango"]

    seen = set()

    for item in items:
        if item in seen:
            print ("Duplicate found and duplicate is : ", item)
            break
        seen.add(item)

# list_uniqueness_checker()



# 10. Exponential Backoff
# Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.


def exponential_backoff():

    import time

    wait_time = 1
    max_retries = 5
    attempts = 0

    while (attempts < max_retries):
        print ("\nattempts = ", attempts+1, "\nWait time = ", wait_time)
        time.sleep(wait_time)
        wait_time *= 2
        attempts += 1

exponential_backoff()