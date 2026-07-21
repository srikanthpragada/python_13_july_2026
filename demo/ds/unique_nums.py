# Take numbers until 0 and print all unqiue numbers

nums = []   # empty list

while True:
    n = int(input("Enter a number [0 to stop] :"))
    if n == 0:
        break

    if n not in nums:
        nums.append(n)


for n in nums:
    print(n, end = ' ')