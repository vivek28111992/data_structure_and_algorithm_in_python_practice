# Reversing data using a Stack
# A function that reverses the order of lines in a file.

from array_based_stack_implemenatation import ArrayStack

# def reverse_file(filename):
#     """Overwrite given file with its contents line-by-line reversed."""
#     S = ArrayStack()
#     original = open(filename)
#     for line in original:
#         S.push(line.rstrip('\n'))                   # we will re-insert newlines when writing
#     original.close()

#     # now we overwrite with contents in LIFO order
#     output = open(filename, 'w')                    # reopening file overwrites original
#     while not S.is_empty():
#         output.write(S.pop() + '\n')                # re-insert newline characters
#     output.close()

# reverse_file('d:/data_structure_and_algorithm_in_python_practice/5. Stack/test.txt')

def reverse_file(filename):
    """Overwrite given file with its contents line-by-line reversed."""
    S = ArrayStack()
    with open(filename) as file:                    # Use file to refer to the file object
        print('f ', file)
        for line in file:
            S.push(line.rstrip('\n'))               # we will re-insert newlines when writing
    
    # now we overwrite with contents in LIFO order
    with open(filename, 'w') as file:                       # reopening file overwrites original
        while not S.is_empty():
            file.write(S.pop() + '\n')

reverse_file('d:/data_structure_and_algorithm_in_python_practice/5. Stack/test.txt')

