# Create a generator that yields Fibonacci numbers up to N.


def fibonacci_generator(N):
    a, b = 0, 1
    while a <= N:
        yield a
        a, b = b, a + b


# Example usage:

N = 100
fib_gen = fibonacci_generator(N)
print(f"Fibonacci numbers up to {N}: ", end="")
print(", ".join(str(num) for num in fib_gen))       

