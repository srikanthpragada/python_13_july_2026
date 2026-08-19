v = "0"
try:
    n = int(v)
    print(100 / n)
except ValueError:
    print('Invalid Number!')
finally:
    print('Finally!')


print('The End!')


