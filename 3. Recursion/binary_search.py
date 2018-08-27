# Binary Search
# An implementation of the binary search algorithm.

def binary_search(data, target, low, high):
    """Return True if target is found in indicated portion of a Python list.

    The search only considers the portion from data[low] to data[high] inclusive.
    """

    if low > high:                  # interval is empty; no match
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            # recur on the portion left of the middle
            return binary_search(data, target, low, mid - 1)
        else:
            # recur on the portion right of the middle
            return binary_search(data, target, mid + 1, high)

print(binary_search([1, 2, 3, 4, 5, 6, 7, 8], 3, 1, 8))
