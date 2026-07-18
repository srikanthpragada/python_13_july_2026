
total = 0

for i in range(1, 6):
    num = int(input("Enter a number [0 to stop] :"))
    if num == 0:
        break
    total += num

print('Total :', total)