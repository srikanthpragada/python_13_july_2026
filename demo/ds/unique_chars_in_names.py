# unique chars in 5 names

names = ['Anders', 'Joe', 'Dave', 'Rick', 'Martin']
uchars = set()   # empty set

for name in names:
    uchars = uchars | set(name)

print(uchars)

