# Raising an Exception
# An implementation with rigorous error-checking

import collections

def sum(values):
    if not isinstance(values, collections.Iterable):
        raise TypeError('parameter must be an iterable type')
    total = 0
    for v in values:
        if not isinstance(v, (int, float)):
            raise TypeError('elements must be numeric')
        total += v
    return total    

print(sum([3, 2, 3, 4]))