names = ['Ben', 'Joe', 'Gary', 'Kevin', 'Henry']

f = open("names.txt", "wt") # create names.txt

for name in names:
    f.write(name + '\n')

f.close()
