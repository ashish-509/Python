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
