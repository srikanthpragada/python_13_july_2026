data = [10, 20, 10, 10, 40, 50, 30, 20]

for v in set(data):
    if data.count(v) > 1:
        print(v)
