# Lambda Function
# Problem: Create a lambda function to compute the cube of a number.

cube = lambda x : x ** 3

# print (cube(4))


# Function with *args
# Problem: Write a function that takes variable number of arguments and returns their sum.

def sum_all(*args):
    return sum (args)

print(sum_all(1,2))
print(sum_all(1,2,3))
print(sum_all(1,2,3,4))


# 8. Function with **kwargs
# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.

def print_kwargs (**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_kwargs(name="Ashish", level="Bachelor")
print_kwargs(name="Mukesh", level="Bachelor", faculty="Electronics")




# Generator Function with yield
# Problem: Write a generator function that yields even numbers up to a specified limit.

def even_generator(limit):
    for i in range (2, limit+1, 2):
        yield i                     # yield is used in place of return

for num in even_generator(10):
    print (num)



# Recursive Function
# Problem: Create a recursive function to calculate the factorial of a number.

def recursive_factorial(number):
    if (number == 0 or number == 1):
        return 1
    else:
        return number * recursive_factorial(number-1)
    
print("The factorial of 5 is : ",recursive_factorial(5))