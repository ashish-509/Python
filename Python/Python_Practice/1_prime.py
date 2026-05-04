# Print all prime numbers from 1 to N efficiently.

def prime_upto_n (n):

    if n < 2:
        return []

    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    return [i for i in range(n + 1) if primes[i]]

n = int(input("Enter a number to find all prime numbers up to it : "))
print(prime_upto_n(n))

