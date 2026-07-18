# Take a number and display whether it is prime

num = int(input("Enter a number :"))

for v in range(2, num // 2 + 1):
    if num % v == 0:
        print(f'Not a Prime Number as it has {v} as factor')
        break
else:
    print("Prime Number!")
