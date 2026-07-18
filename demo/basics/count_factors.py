# Take a number and display its factors

num = int(input("Enter a number :"))
count = 0
for v in range(2,  num // 2 + 1):
    if num % v == 0:
        count += 1

print(count)

