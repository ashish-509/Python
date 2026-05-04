# Rewrite a loop-heavy solution using:
    # list comprehension
    # lambda + map/filter



# Example 1: Using list comprehension to create a list of squares

numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print("Squares using list comprehension:", squares)


# Example 2: Using lambda and map to create a list of squares

squares_lambda = list(map(lambda x: x**2, numbers))
print("Squares using lambda and map:", squares_lambda)


# Example 3: Using list comprehension with a condition to filter even numbers

even_numbers = [x for x in numbers if x % 2 == 0]
print("Even numbers using list comprehension:", even_numbers)


# Example 4: Using lambda and filter to get even numbers

even_numbers_lambda = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers using lambda and filter:", even_numbers_lambda)

