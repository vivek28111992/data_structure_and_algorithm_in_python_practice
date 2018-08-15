# Catching an Exception
# Handle two or more types of errors in the same way, we can use a single except-statement

age = -1                    # an initially invalid choice
while age <= 0:
    try:
        age = int(input('Enter your age in years: '))
        if age <= 0:
            print('Your age must be positive')
    except (ValueError, EOFError):
        print('Invalid Response')