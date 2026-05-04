# Implement Fibonacci:
#     using recursion
#     using dynamic programming (memoization)


# Using recursion

def fibonacci_recursion (num):

    if num <= 0:
        return 0
    elif num == 1:
        return 1
    
    else:
        return fibonacci_recursion(num - 1) + fibonacci_recursion(num - 2)


# Using dynamic programming (memoization)

def fibonacci_memoization (num, memo={}):

    if num in memo:
        return memo[num]

    if num <= 0:
        return 0
    elif num == 1:
        return 1
    
    else:
        memo[num] = fibonacci_memoization(num - 1, memo) + fibonacci_memoization(num - 2, memo)
        return memo[num]



num = int(input("Enter a number to find its Fibonacci : "))
print("Fibonacci using recursion : ", fibonacci_recursion(num))
print("Fibonacci using memoization : ", fibonacci_memoization(num))


