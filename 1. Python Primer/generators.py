# Generators
# Implementation of a generator for computing those factors

def factors(n):                     # generator that computes factors
    for k in range(1, n+1):
        if n % k == 0:              # divides evenly, thus k is a factor
            yield k                 # yeild this factor as next result

num = 56

# print(list(factors(num)))

resultNum = factors(num)

for n in resultNum:
    print(n)