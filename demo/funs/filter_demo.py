def ispositive(n):
    return n > 0

nums = [-10, 5, 8, -20, 9]

for n in filter(ispositive, nums):
    print(n)

