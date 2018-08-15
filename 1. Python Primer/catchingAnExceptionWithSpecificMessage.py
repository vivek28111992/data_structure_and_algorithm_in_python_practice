# Catching an Exception
# Provide a more specific error message, or perhaps to allow the execption to interrupt the loop and be propagated to a higher context.

age = -1                    # an initially invalid choice
while age <= 0:
    try:
        age = int(input('Enter your age in years: '))
        if age <= 0:
            print('Your age must be positive')
    except ValueError:
        print('That is an invalid age specification')
        raise
    except EOFError:
        print('There was an unexpected error reading input.')
        raise                   # let's re-raise this exception
