# Python's List Class
# Measuring the amortized cost of append for Python's list class.

from time import time                   # import time function from time module

def compute_average(n):
    """Perform n appends to an empty list & return average time elapsed."""
    data = []
    start = time()
    print(start)                              # record the start time (in seconds)
    for k in range(n):
        data.append(None)
    end = time()                                # record the end time (in seconds)
    return (end - start) / n                    # compute average per operation

print(compute_average(500))
