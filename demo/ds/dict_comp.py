st = "hello"
d = {}  # empty dict
for c in st:
    d[c] = ord(c)

print(d)

# Dict comprehension
d = {c: ord(c) for c in st}
print(d)
