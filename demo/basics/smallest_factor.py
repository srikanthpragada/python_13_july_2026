# Take a number and display its smallest factor

num = int(input("Enter a number :"))

for v in range(2, num//2 + 1):
    if num % v == 0:
        print('Smallest Factor : ', v)
        break
else:
    print(num)



