data = [10, 20, 10, 10, 40, 50, 30, 20]

nums = []
dnums = set()
for v in data:
    if v not in nums:
        nums.append(v)
    else:
        dnums.add(v)

print(dnums)
