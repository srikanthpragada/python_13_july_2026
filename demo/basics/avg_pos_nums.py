# take numbers until 0 is given and print avg of positive numbers

total = 0
count = 0

while True:
    num = int(input("Enter a number :"))
    if num == 0:
        break

    if num < 0:
        continue

    total += num
    count += 1

print('Average = ', total // count)