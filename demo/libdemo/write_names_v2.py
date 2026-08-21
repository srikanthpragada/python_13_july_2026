names = ['Ben', 'Joe', 'Gary', 'Kevin', 'Henry']

with open("names.txt", "wt") as f:
    for name in names:
        f.write(name + '\n')
