# Raising an Exception
# The sqrt function in Python's math library performs error-checking

def sqrt(x):
    if not isinstance(x, (int, float)):
        raise TypeError('x must be numeric')
    elif x < 0:
        raise ValueError('x cannot be negative')
    else:
        return x ** 0.5

print('{0:.4}'.format(sqrt(-57)))