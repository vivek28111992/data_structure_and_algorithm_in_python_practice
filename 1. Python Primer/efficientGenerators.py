# Generators
# Implementation of efficient generator for finding all the factors

def factors(n):                     # generator that computes factors
    k = 1
    while k * k < n:                # while k < sqrt(n)
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k * k == n:                  # special case if n is perfect square
        yield k

# print(list(factors(49)))

res = factors(49)

for n in res:
    print(n)