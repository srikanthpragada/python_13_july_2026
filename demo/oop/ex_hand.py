v = "a0"
try:
    n = int(v)
    print(100 / n)
except ValueError as e:
    print('Invalid Number! -->', e)
except ZeroDivisionError:
    print('Zero is not valid number!')

print('The End!')


