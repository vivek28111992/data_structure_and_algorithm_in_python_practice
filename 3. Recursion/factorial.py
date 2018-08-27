# The Factorial Function
# A recursive implementataion of the factorial function.

def factorial(n):
    if n < 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n * factorial(n-1)

res = factorial(5)
print(res)
