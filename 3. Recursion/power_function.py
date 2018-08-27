# Power Function
# Computing the power function using trivial recursion.

def power(x, n):
    """Compute the value x**n for integer n."""
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)

print(power(5, 7))
