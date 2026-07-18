# Take a number and display its largest factor

num = int(input("Enter a number :"))

for v in range(num // 2, 0, -1 ):
    if num % v == 0:
        print('Largest Factor : ', v)
        break

