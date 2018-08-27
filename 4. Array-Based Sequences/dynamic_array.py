# Dynamic Array
# An experiment to explore the relationship between a list's length and its underlying size in Python.

import sys                  # provides getsizeof function
data = []
for k in range(10):                  # NOTE: must fix choice of n
    a = len(data)                   # number of elements
    b = sys.getsizeof(data)         # actual size in bytes
    print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
    data.append(None)               # increase length by one