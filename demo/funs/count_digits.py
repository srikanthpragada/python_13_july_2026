def count_digits(s):
    count = 0
    for c in s:
        if c.isdigit():
            count += 1

    return count


c = count_digits('abc123')
print(c)


