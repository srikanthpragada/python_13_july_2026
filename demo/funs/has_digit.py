def has_digit(s):
    for c in s:
        if c.isdigit():
            return True
        
    return False


print(has_digit('Hello'))
print(has_digit('Python 3.14'))